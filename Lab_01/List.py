#  Author:          Mohammad Sadequr Rahman
#  File Name:       List.py
#
#  Description:     List processing: insert, remove, sort, find
#                   this python funtion implement list operations
#


#################################################################
# Helper functions to sort the list
# Here quick sort algorithm implemented
#################################################################
def __partition(array, startIndex, endIndex):       
    partitionIndex = startIndex - 1
    pivot = array[endIndex]    
    for j in range(startIndex, endIndex): 
        if  array[j] <= pivot: 
            partitionIndex = partitionIndex+1 
            array[partitionIndex],array[j] = array[j],array[partitionIndex] 
    array[partitionIndex+1],array[endIndex] = array[endIndex],array[partitionIndex+1] 
    return (partitionIndex + 1) 


def __quickSort(array, startIndex, endIndex): 
    if startIndex < endIndex: 
        partitionIndex = __partition(array, startIndex, endIndex) 
        __quickSort(array, startIndex, partitionIndex-1) 
        __quickSort(array, partitionIndex+1, endIndex)


# List processing functions

###############################################################
#   Insert
#   parameter description.
#       list:       list to be processed
#       size:       size of the list
#       position:   position at where new data to be inserted
#       data:       data to insert into the list
#
#   return
#       retuen 0 if successfull else -1
################################################################
def Insert(list, size, position, data):
    retVal = -1
    if position <= size :
        list[position] = data
        retVal = 0
    return retVal

###############################################################
#   Remove
#   parameter description.
#       list:       list to be processed
#       size:       size of the list
#       data:       data to be deleted from the list
#
#   return
#       retuen 0 if successfull else -1
################################################################
def Remove(list, size, data):
    retVal = -1
    for i in range(size):
        if list[i] == data:
            list[i] = -1
            return 0
    return retVal

###############################################################
#   Find
#   parameter description.
#       list:       list to be processed
#       size:       size of the list
#       data:       data to find from the list
#
#   return
#       retuen 1 if data is found in the list else -1
################################################################
def Find(list, size, data):
    retVal = -1
    for i in range(size):
        if list[i] == data:
            return 1
    return retVal

###############################################################
#   Sort
#   parameter description.
#       list:       list to be processed
#       size:       size of the list
# 
#
#   return
#       nothing
################################################################
def Sort(list, size):
    __quickSort(list, 0, size-1)




# Driver code
if __name__ == '__main__':
    # define maximun element that can hold into the list
    LIST_SIZE = 5
    # devicen list itself. it's actually a python table/array
    List = [ -1 ] * LIST_SIZE
    print("\r\n\r\n\tDriver Application Started\r\n\r\n")
    print("Init list with empty data\r\n\t" + str(List) + "\r\n")
    print("Insert data(25) at position 4")
    Insert(List,LIST_SIZE,4,25)
    print("Insert data(65) at position 0")
    Insert(List,LIST_SIZE,0,65)
    print("Insert data(6) at position 1")
    Insert(List,LIST_SIZE,1,6)
    print("Insert data(90) at position 2")
    Insert(List,LIST_SIZE,2,90)
    print("Insert data(5) at position 3")
    Insert(List,LIST_SIZE,3,5)
    print("List with after insertion\r\n\t" + str(List) + "\r\n")
    print("Remove data 90 from the list")
    Remove(List,LIST_SIZE,90)
    print("List with after Remove\r\n\t" + str(List) + "\r\n")
    print("Insert data(85) at position 2")
    Insert(List,LIST_SIZE,2,85)
    Sort(List,LIST_SIZE)
    print("List with after sorting\r\n\t" + str(List) + "\r\n")
    print("\r\n\r\n\t End Application \r\n\r\n")