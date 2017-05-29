import unittest
from huffman import *
from linked_list import *

class TestList(unittest.TestCase):
   def test_generate_string(self):
      test_tree = HuffmanTree(Node(64, 10, Node(36, 5, None, None), Node(39, 5, None, None)))
      #print (generate_string(test_tree))
      #print (openfile())
   def test_comes_before(self):
      n1 = Leaf(33, 10)
      n2 = Leaf(5, 3)
      n3 = Leaf(33, 9)
      n4 = Leaf(33, 9)
      test_str = ""
      self.assertFalse(comes_before(n1, test_str))
      self.assertFalse(comes_before(n1, n2))
      self.assertTrue(comes_before(n2, n1))
      self.assertTrue(comes_before(n3, n1))
      self.assertFalse(comes_before(n1, n3))
      self.assertTrue(comes_before(n3, n4))
   def test_insert_sorted(self):
      n1 = Pair(Node(33, 3, None, None), Pair(Node(66, 6, None, None), Pair(Node(99, 9, None, None), None)))
      n1 = insert_sorted(n1, Node(44, 4, None, None), comes_before)
      n1 = insert_sorted(n1, Node(33, 4, None, None), comes_before)
      #print (n1)
   def test_build_huffman(self):
      occ_list = List([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0)      
      huff_tree = build_huffman(occ_list)
      print (generate_string(huff_tree))
      print (huff_tree)
      occ_list = openfile()
      huff_tree2 = build_huffman(occ_list)
      print(huff_tree)
      



if __name__ == '__main__':
    unittest.main()