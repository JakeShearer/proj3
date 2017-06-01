import unittest
from linked_list import *

class TestList(unittest.TestCase):
   # Note that this test doesn't assert anything! It just verifies your
   #  class and function definitions.
   def test_remove(self):
      temp_list = Pair("one", Pair("two", None))
      self.assertEqual(remove(temp_list, 0), ("one", Pair("two", None)))
      temp_list2 = None
      self.assertRaises(IndexError, remove, temp_list2, 1)
      self.assertRaises(IndexError, remove, temp_list, 9)
      temp_list3 = Pair("one", None)
      self.assertEqual(remove(temp_list3, 0), ("one", None))
      temp_list4 = Pair("one", Pair("two", None))
      temp_list4 = remove(temp_list, 1)
      self.assertEqual(temp_list4, ('two', Pair('one', None)))
   def test_set(self):
      #temp_list = None
      temp_list2 = Pair("one", Pair("two", None))
      #self.assertEqual(set(temp_list, 0, "one"), None)
      self.assertRaises(IndexError, set, temp_list2, 5, "three")
      self.assertRaises(IndexError, set, temp_list2, -1, "yo")
   def test_get(self):
      temp_list = None
      self.assertRaises(IndexError, get, temp_list, 0)
      temp_list2 = Pair("one", Pair("two", None))
      temp_list2 = add(temp_list2, 2, "three")
      self.assertEqual(get(temp_list2, 1), "two")
      self.assertRaises(IndexError, get, temp_list2, 5)
      temp_list3 = Pair("one", Pair("two", Pair("three", Pair("four", Pair("five", Pair("six", None))))))
      self.assertEqual(get(temp_list3, 3), "four")
      self.assertEqual(get(temp_list3, 5), "six")
      self.assertRaises(IndexError, get, temp_list, -1)
   def test_add(self):
      temp_list = None
      temp_list = add(temp_list, 0, "one")
      temp_list2 = Pair("one", Pair("two", None))
      temp_list2 = add(temp_list2, 2, "three")
      self.assertEqual(temp_list2, Pair("one", Pair("two", Pair("three", None))))
      self.assertEqual(temp_list, Pair("one", None))
      self.assertRaises(IndexError, add, temp_list, 9, "test")
      self.assertRaises(IndexError, add, temp_list, -1, "yo")
      temp_list = add(temp_list, 0, "zero")
      self.assertEqual(temp_list, Pair("zero", Pair("one",None)))
   def test_repr(self):
      temp_list = Pair("this", Pair("is", Pair("a", None)))
      self.assertEqual(repr(temp_list), "'this', 'is', 'a', None")
   def test_interface(self):
      temp_list = make_empty()
      self.assertEqual(temp_list, None)
      temp_list = add(temp_list, 0, "Hello!")
      self.assertEqual(temp_list, Pair("Hello!", None))
      length(temp_list)
      self.assertEqual(length(temp_list), 1)
      get(temp_list, 0)
      self.assertEqual(get(temp_list, 0), "Hello!")
      temp_list = set(temp_list, 0, "Bye!")
      self.assertEqual(get(temp_list, 0), "Bye!")
   def test_remove_help(self):
      temp_list = make_empty()
      self.assertRaises(IndexError, remove_help, temp_list, -1)
      self.assertRaises(IndexError, remove_help, None, 8)
   def test_foreach(self):
      empty_list = None
      self.assertEqual(foreach(empty_list, repr), None)
      temp_list = Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None)))))
      temp_list = foreach(temp_list, math.factorial)
      self.assertEqual(foreach(temp_list, math.factorial), None)

if __name__ == '__main__':
    unittest.main()