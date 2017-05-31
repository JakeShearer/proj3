import unittest
from array_list import *

class TestList(unittest.TestCase):
   def test_eq(self):
      temp_list = empty_list()
      temp_list2 = empty_list()
      self.assertTrue(temp_list == temp_list2)
   def test_get(self):
      temp_list = empty_list()
      self.assertRaises(IndexError, get, temp_list, -1)
   def test_set(self):
      temp_list = empty_list()
      self.assertRaises(IndexError, set, temp_list, -1, 6)
   def test_remove(self):
      temp_list = empty_list()
      self.assertRaises(IndexError, remove, temp_list, -1)
      temp_list = List([3,1,4,3], 10, 10)
      #temp_list = remove(temp_list, 1)
      #self.assertEqual(temp_list, List([3,4,3], 10, 10))
   def test_repr(self):
      temp_list = empty_list()
      temp_list = add(temp_list, 0, 1)
      self.assertEqual(repr(temp_list), 'List([1], 1, 1)')
      #print (temp_list)
   def test_length(self):
      temp_list = List([3,1,4,3], 4, 10)
      self.assertEqual(length(temp_list), 4)
      temp_list = empty_list()
      self.assertEqual(length(temp_list), 0)
      temp_list = add(temp_list, 0, 1.1)
      self.assertEqual(length(temp_list), 1)
   def test_add(self):
      temp_list = empty_list()
      temp_list = add(temp_list, 0, 1.1)
      self.assertEqual(temp_list.array[0], 1.1)
      self.assertRaises(IndexError, add, temp_list, -1, 3)
      temp_list = add(temp_list, 1, 5.4)
      self.assertEqual(temp_list.array[1], 5.4)
   def test_add_element(self):
      temp_list = empty_list()
      #temp_list = add_element(temp_list, 0, 1.1)
      #self.assertEqual(temp_list.array[0], 1.1)
      #self.assertRaises(IndexError, add_element, temp_list, -1, 3)
      #temp_list = add_element(temp_list, 1, 5.4)
      #self.assertEqual(temp_list.array[1], 5.4)
   def test_interface(self):
      temp_list = empty_list()
      temp_list = add(temp_list, 0, "Hello!")
      self.assertEqual(length(temp_list), 1)
      get(temp_list, 0)
      temp_list = set(temp_list, 0, "Bye!")
      remove(temp_list, 0)

if __name__ == '__main__':
    unittest.main()