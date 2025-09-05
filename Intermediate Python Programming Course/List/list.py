list = [1,2,3,4,5,6,7,8]
# slicing
# [start : end]
print(list[1:5]) # prints start index to end-1 index
print(list[:5]) # prints beginning to end-1 index
print(list[2:]) # prints start index to end of list
#print(list[:]) # prints whole list
print(list[::3]) # prints whole list with step 3
#print(list[2::]) # prints from index 2 to end of list-- works like list[2:] 
print(list[1:len(list)+1:2])
print(list[-1:]) # prints last element of list
print(list[-2:]) # prints last two elements of list
print(list[:-2]) # prints list except last element
print(list[::-1]) # prints list in reverse order
print(list[::-2]) # prints list with step -2 (reverse order)

"""
[- num of elements:] prints number of elements from end
[: -num of elements] prints list except number of elements from end
[:: -1] prints list in reverse order
[:: -steps] prints list with step -2 (reverse order)

"""