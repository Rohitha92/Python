#Array- find missing element in second list of non negative numbers


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

