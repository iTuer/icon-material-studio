import importlib.util
import struct
import tempfile
import unittest
import zlib
from pathlib import Path
spec = importlib.util.spec_from_file_location('inspector', Path(__file__).parents[1]/'scripts/inspect_icon.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def chunk(t,d):return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
def png(raw, width=1,height=1, depth=8, color=6, interlace=0):
 return b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',width,height,depth,color,0,0,interlace))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')
class InspectorTests(unittest.TestCase):
 def setUp(self):self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
 def tearDown(self):self.temp.cleanup()
 def inspect(self,data):
  p=self.root/'sample.png';p.write_bytes(data);r=m.parse_png_rgba(str(p));self.assertEqual(data,p.read_bytes());return r
 def test_alpha_classes(self):
  r=self.inspect(png(bytes([0,0,0,0,0,100,100,100,250,100,100,100,255]),width=3))
  self.assertEqual(r['fully_opaque_pct'],33.33);self.assertEqual(r['near_opaque_pct'],33.33)
 def test_filters(self):
  # two identical pixels; independently encode every PNG filter
  original=[20,30,40,255]*2
  for f in range(5):
   row=[]
   for i,x in enumerate(original):
    a=original[i-4] if i>=4 else 0
    predictor=[0,a,0,a//2,a][f]
    row.append((x-predictor)&255)
   with self.subTest(filter=f):self.assertEqual(self.inspect(png(bytes([f]+row),width=2))['fully_opaque_pct'],100)
 def test_invalid_filter(self):
  with self.assertRaisesRegex(ValueError,'filter'):self.inspect(png(bytes([5,1,2,3,255])))
 def test_bad_crc(self):
  data=bytearray(png(bytes([0,1,2,3,255])));data[29]^=1
  with self.assertRaisesRegex(ValueError,'CRC'):self.inspect(bytes(data))
 def test_bad_length(self):
  for raw in [b'\0',bytes([0,1,2,3,255,0])]:
   with self.assertRaisesRegex(ValueError,'length'):self.inspect(png(raw))
 def test_truncated(self):
  with self.assertRaises(ValueError):self.inspect(png(bytes([0,1,2,3,255]))[:-4])
 def test_unsupported(self):
  r=self.inspect(png(bytes([0,1,2,3]),color=2));self.assertEqual(r['pixel_inspection'],'unsupported')
 def test_preview(self):
  p=self.root/'a<b.png';p.write_bytes(png(bytes([0,1,2,3,255])))
  r=m.parse_png_rgba(str(p));out=m.write_preview_html(str(p),r,str(self.root/'preview'));s=Path(out).read_text()
  self.assertIn('Native 1:1',s);self.assertIn('width:1px;height:1px',s);self.assertIn('a&lt;b.png',s);self.assertNotIn('opacity: 0.85',s)
if __name__=='__main__':unittest.main()
