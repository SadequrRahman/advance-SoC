#  Author:          Mohammad Arafath Uz Zaman
#  File Name:       list_pytest.py
#
#  Description:     Testing of List processing: test_Insert, test_Remove, test_Find,
#                   test_Sort this python function implement testing of list operations
#

import pytest
from List import *


List = [10, 2, 13, 4, 5]
LIST_SIZE = 5


###############################################################
#   test Insert() function. If insertion is successful
#   Insert() will return 0 and the test passed
################################################################
def test_Insert():
    assert Insert(List,LIST_SIZE,4,25) == 0


###############################################################
#   test Remove() function. If removing is successful
#   Remove() will return 0 and the test passed
################################################################
def test_Remove():
    data = 4
    assert Remove(List,LIST_SIZE,data) == 0


###############################################################
#   test Find() function. If the function can find the
#   element in the list, Find() will return 1
#   and the test passed else failed
################################################################
def test_Find():
    data = 2
    assert Find(List,LIST_SIZE, data) == 1


###############################################################
#   test sort() function. If sorting is successful
#   list will be equal to explicitly sorted list
#   and the test passed else failed
################################################################
def test_Sort():
    new_List = [10, 2, 13, 4]
    Sort(new_List, 4)
    assert new_List == [2, 4, 10, 13]



