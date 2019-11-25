#  Author:          Mohammad Sadequr Rahman
#  File Name:       List.py
#
#  Description:     Unit test for List processing functions
#                   This file import List and do some testing
#                   using unittest framework.
#                    

import List
import unittest


###############################################################
#   Class for test List operations
################################################################
class TestListOperations(unittest.TestCase):
    """A class to test Opertation on List"""
    size = 10

    def setUp(self):
        self.list = [-1] * self.size


    def test_ListValidInsertion(self):
        expectedResult = 0
        retValue = List.Insert(self.list, self.size, 0, 154)
        self.assertEqual(retValue, expectedResult, 'Valid "Insert" test failed')


    def test_ListInvalidInsertion(self):
        expectedResult = -1
        retValue = List.Insert(self.list, self.size, self.size, 154)
        self.assertEqual(retValue, expectedResult, 'Invalid "Insert" with out of boundery test failed')

    def test_ListValidRemove(self):
        expectedResult = 0
        retValue = List.Insert(self.list, self.size, 5, 154)
        self.assertEqual(retValue, expectedResult, 'Valid "Insert" test failed')
        expectedResult = 0
        retValue = List.Remove(self.list, self.size, 154)
        self.assertEqual(retValue, expectedResult, 'Valid "Remove" test failed')
        
    def test_ListInvalidRemove(self):
        expectedResult = 0
        retValue = List.Insert(self.list, self.size, 5, 154)
        self.assertEqual(retValue, expectedResult, 'Valid "Insert" test failed')
        expectedResult = -1
        retValue = List.Remove(self.list, self.size, 158)
        self.assertEqual(retValue, expectedResult, 'Valid "Remove" test failed')

    def test_ListSortValidEmptyList(self):
        expectedList = [-1] * self.size
        List.Sort(self.list,self.size)
        self.assertEqual(self.list, expectedList, 'Empty list "Sort" test failed')

    def test_ListSortInvalidEmptyList(self):
        expectedList = [0] * self.size
        List.Sort(self.list,self.size)
        self.assertNotEqual(self.list, expectedList, 'Empty list "Sort" test failed')

    def test_ListValidSort(self):
        expectedList = [-1] * self.size
        for i in range(self.size):
            expectedList[i] = i
            self.list[i] = (self.size -1) - i
        List.Sort(self.list,self.size)
        self.assertEqual(self.list, expectedList, 'Valid List "Sort" test failed')



if __name__ == '__main__':
    print("\r\n\tTest application started\r\n")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestListOperations)
    unittest.TextTestRunner(verbosity=2).run(suite)