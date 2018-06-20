#Array- find missing element in second list of non negative numbers
'''
1. brute force iterating will work with O(n^2).
2. Sort the arrays. assign the larger array to arr1
2. use zip function to zip the nmbers after sorting. one of the longer list(list-1) will not be in zip.
3. compare the numbers. if not equal, return that number from list-1.
4. if all are equal, the remaining letter in list1 is the missing number.
'''

def finder(arr1, arr2): #O(nlogn)
  
  if (len(arr1) < len(arr2)):
    temp = arr1
    arr1 = arr2
    arr2 = temp
  
  arr1.sort()
  arr2.sort()
  for num1,num2 in zip(arr1,arr2):
    if num1 != num2:
      return num1
  
  return arr1[-1]
  
  
mylist1 = [2,4,3,5,1]
mylist2 = [1,2,3,4,5,6]
x=finder(mylist1, mylist2)
print(f'missing number: {x}')

