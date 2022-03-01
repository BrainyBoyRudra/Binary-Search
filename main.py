
def binarysearch(array,n):
    lower=0
    higher=len(array)-1
    middle=0
    while lower<=higher:
        middle=(lower+higher)//2
        if array[middle] == n:
            
            return n
        else:
            if array[middle] < n:
                lower = middle+1
            else:
                higher = middle-1
    return -1
array = [1,2,3,4,5,6,7,283,928,1938,89183,3338292]
n = int(input('Hi im binary search please enter value to search. '))
output = binarysearch(array,n)
if output!=-1:
    print('Your Search was Succesfull the value you searched was on position  ',output+1)
else :
    print('Could not find your value please try again(error402)')
