import unittest
from array_list import *
from linked_list import *
import sys
import array_list

#openfile File --> List
#opens a file and returns the number of character occurences
#in the file
def openfile(filename):
   charlist = empty_list()
   charlist.array = [0] * 256
   #print("Input filename:")
   #filename = sys.stdin.readline().strip()
   #print("opening " + filename)
   f = open(str(filename), "r")
   for line in f:
      for ch in line:
         temp = ord(ch)
         charlist.array[temp] += 1               
   #print (charlist)
   return charlist

#print openfile()

#A HuffmanTree is a 
# - Node
# - Leaf
class HuffmanTree:
    def __init__(self, node):
        self.node = node

    def __eq__(self, other):
        return ((type(other) == HuffmanTree)
          and self.node == other.node
        )

    def __repr__(self):
        return ("HuffmanTree({!r})".format(self.node))
        
#A Leaf is a 
# - ascii order(int)
# - frequency(int)
class Leaf:
    def __init__(self, asciirep, freq):
        self.asciirep = asciirep
        self.freq = freq

    def __eq__(self, other):
        return ((type(other) == Leaf)
          and self.asciirep == other.asciirep
          and self.freq == other.freq
        )

    def __repr__(self):
        return ("Leaf({!r}, {!r})".format(self.asciirep, self.freq))

#A Node is a 
# - ascii order(int)
# - frequency(int)
# - Node(left)
# - Node(right)
class Node:
    def __init__(self, asciirep, freq, left, right):
        self.asciirep = asciirep
        self.freq = freq
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.asciirep == other.asciirep
          and self.freq == other.freq
          and self.left == other.left
          and self.right == other.right
        )

    def __repr__(self):
        return ("Node({!r}, {!r}, {!r}, {!r})".format(self.asciirep, self.freq, self.left, self.right))


#generate_string HuffmanTree --> String
#generates a string based on a prefix traversal of a huffman tree
def generate_string(hufftree):
   outstr = ""
   #print (type(hufftree))
   if hufftree == None:
      return outstr
   if isinstance(hufftree, HuffmanTree):
      outstr += hufftree.node.freq * chr(hufftree.node.asciirep)
      #print (outstr)
      outstr += generate_string(hufftree.node.left)
      #print (outstr)
      outstr += generate_string(hufftree.node.right)
      #print (outstr)
   if isinstance(hufftree, Node):
      outstr += hufftree.freq * chr(hufftree.asciirep)
      #print (outstr)
      outstr += generate_string(hufftree.left)
      #print (outstr)
      outstr += generate_string(hufftree.right)
      #print (outstr)
   return outstr
   

#comes_before hufftree hufftree >> boolean
#returns true if tree a comes before tree b
def comes_before(a, b):
   if (((isinstance(a, Node) or isinstance(a, Leaf)) and ((isinstance(b, Node) or isinstance(b, Leaf))))) == False:
      return False
   else:
      if a.freq > b.freq:
         return False
      if a.freq < b.freq:
         return True
      else:
         #if a.asciirep == None:
         #   return True
         if a.asciirep > b.asciirep:
            return False
         #if a.asciirep > b.asciirep:
         #   return True
         else:
            return True

#build_huffman occurences >> HuffmanTree
#build a huffman tree from a given list of occurences
def build_huffman(occurences):
   leaflist = None
   for i in range(0, 256):
      if occurences.array[i] != 0:
         temp = Leaf(i, occurences.array[i])
         #print (temp)
         #print ("adding leaf to linked list")
         leaflist = insert_sorted(leaflist, temp, comes_before)
   out = None
   if leaflist == None:
      return None
   while leaflist.rest != None:
      n1 = leaflist.value
      n2 = leaflist.rest.value
      #print ("n1: " + str(n1))
      #print ("n2: " + str(n2))
      leaflist = remove(leaflist, 0)[1]
      leaflist = remove(leaflist, 0)[1]
      #print ("leaflist after removing first two vals: " + str(leaflist))
      i1 = None
      #print (n1.freq)
      #print (n2.freq)
      if comes_before(n1, n2):
         i1 = Node(n2.asciirep, n1.freq + n2.freq, n1, n2)
         #print ("combined node : " + str(i1))
      #else:
      #   i1 = Node(n1.asciirep, n1.freq + n2.freq, n2, n1)
         #print ("combined node : " + str(i1))
      leaflist = insert_sorted(leaflist, i1, comes_before)
      #print ("OUTPUT" + str(leaflist))
      #print (length(leaflist))
   
   return get(leaflist, 0)

#huffman_to_ascii huffmanTree >> string  
#traverse through a huffmanTree and convert it to a binary string
def huffman_to_codes(huffman, codes, string = ""):
   if huffman == None:
      return None
   if isinstance(huffman, Leaf):
      #print ("hit a leaf")
      #print (string)
      codes[huffman.asciirep] = string
      string = ""
   else:
      #print ("moving left")
      huffman_to_codes(huffman.left, codes, string + "0")
      #print ("moving right")
      huffman_to_codes(huffman.right, codes, string + "1")
   print (codes)
   return codes

   
def huffman_encode(infile, outfile):
   occurences = openfile(infile)
   huffman = build_huffman(occurences)
   emptylist = [0] * 256
   codes = huffman_to_codes(huffman, emptylist)
   print ("****************")
   codestr = ""
   intext = open(infile, "r")
   for line in intext:
      for ch in line:
         codestr += codes[ord(ch)]
   return codestr
   
   
def huffman_decode(infile, outfile):
   pass


#################TEST CASES#################################
class TestList(unittest.TestCase):
   def test_generate_string(self):
      test_tree = HuffmanTree(Node(64, 10, Node(36, 5, None, None), Node(39, 5, None, None)))
      self.assertEqual(generate_string(test_tree), "@@@@@@@@@@$$$$$'''''")
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
      #print (huff_tree)
      huff_tree = build_huffman(occ_list)
      #print ("test with ex1.txt")
      occ_list = List([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0)
      #print (occ_list)
      huff_tree3 = build_huffman(occ_list)
      
   def test_huffman_to_codes(self):
      codes = [None] * 256
      outlist = empty_list()
      occ_list = List([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0)
      huff_tree = build_huffman(occ_list)
      print (huff_tree)
      print (huffman_to_codes(huff_tree, codes))
      #should be 11011011000011011010011010011 with ex2
   def test_eq_repr(self):
      self.maxDiff = None
      occ_list = List([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0)      
      huff_tree = build_huffman(occ_list)
      occ_list = List([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0)      
      huff_tree2 = build_huffman(occ_list)
      print (huff_tree2)
      self.assertEqual(repr(huff_tree), repr(huff_tree))
      huff_tree3 = HuffmanTree(None)
      print (huff_tree3)
      self.assertEqual(repr(huff_tree3), "HuffmanTree(None)")
   def test_huffman_encode(self):
      a = "ex.txt"
      b = "out1.txt"
      self.assertEqual(huffman_encode(a, b), "11011011000011011010011010011")
      huffman_encode("file_blank.txt", "file_blank_encoded.bin")
   def test_open(self):
      f = openfile("ex1.txt")
   def test_huffman_decode(self):
      self.assertEqual(huffman_decode("a", "b"), None)
      
      



if __name__ == '__main__':
    unittest.main()

   
         