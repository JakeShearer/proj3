import unittest
from array_list import *

class TestList(unittest.TestCase):
    def test_eq(self):
      temp_list = make_empty()
      temp_list2 = make_empty()
      self.assertTrue(temp_list == temp_list2)
    def testCreation0(self):
        self.assertEqual(ArrayList([3, 4, 5, None, None], 5), ArrayList([3, 4, 5, None, None], 5))

    def testmake_arraylist0(self):
        self.assertEqual(make_empty(), ArrayList([None, None, None, None, None], 0))

    def testlength0(self):
        self.assertEqual(length(ArrayList([42, 23, None, None], 2)), 2)

    def testlength1(self):
        self.assertEqual(length(ArrayList([42, 23, None, None], 3)), 3)

    def testadd_to_end0(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertEqual(add_to_end(obj, "dog"), obj)
        self.assertEqual(obj, ArrayList([9, 10, "dog", None], 3))

    def testadd_to_end1(self):
        obj = ArrayList([9, 10], 2)
        self.assertEqual(add_to_end(obj, "dog"), obj)
        self.assertEqual(obj, ArrayList([9, 10, "dog", None], 3))

    def testadd0(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertEqual(add(obj, 2, "zebra"), obj)
        self.assertEqual(obj, ArrayList([9, 10, "zebra", None], 3))

    def testadd1(self):
        obj = ArrayList([9, 10], 2)
        self.assertEqual(add(obj, 2, "zebra"), obj)
        self.assertEqual(obj, ArrayList([9, 10, "zebra", None], 3))

    def testadd2(self):
        obj = ArrayList([9, 10], 2)
        self.assertEqual(add(obj, 0, "zebra"), obj)
        self.assertEqual(obj, ArrayList(["zebra", 9, 10, None], 3))

    def testget0(self):
        self.assertEqual(get(ArrayList([9, 10, None, None], 2), 0), 9)

    def testget1(self):
        self.assertEqual(get(ArrayList([9, 10, None, None], 2), 1), 10)

    def testget2(self):
        self.assertRaises(IndexError, get, ArrayList([9, 10, None, None], 2), 2)

    def testget3(self):
        self.assertRaises(IndexError, get, ArrayList([9, 10, None, None], 2), -1)

    def testset0(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertEqual(set(obj, 0, "bb"), obj)
        self.assertEqual(obj, ArrayList(["bb", 10, None, None], 2))

    def testset1(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertEqual(set(obj, 1, "bb"), obj)
        self.assertEqual(obj, ArrayList([9, "bb", None, None], 2))

    def testset2(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertRaises(IndexError, set, obj, 2, "bb")

    def testremove0(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertEqual(remove(obj, 0), obj)
        self.assertEqual(obj, ArrayList([10, None, None, None], 1))

    def testremove1(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertEqual(remove(obj, 1), obj)
        self.assertEqual(obj, ArrayList([9, None, None, None], 1))

    def testremove2(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertRaises(IndexError, remove, obj, 2)

if __name__ == '__main__':
    unittest.main()