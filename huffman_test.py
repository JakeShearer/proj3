import unittest
from huffman import *

class TestList(unittest.TestCase):

   def test_01_textfile(self):
      s = huffman_encode("textfile.txt", "textfile_encoded.bin")
      self.assertEqual(s, "acb")
      # capture errors by running 'diff' on your encoded file
      # with a *known* solution file
      err = os.system("diff textfile_encoded.bin textfile_encoded_soln.bin")
      self.assertEqual(err, 0)
      
if __name__ == '__main__': 
   unittest.main()