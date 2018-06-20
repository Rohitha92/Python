#Bubble sort implementation
#multiple passes throught the list.

##Ascending order


def bubble_sort(arr):
  
  swapped = True
  
  while(swapped):
    swapped = False
    for i in range(len(arr)-1): 
      if arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1]= temp
        swapped = True
  
  return arr
  
#Optimized solution:
#faster since we do not move comparing throughout the array every iteration.  

def bubble_sort2(arr): 
  
  n= len(arr)
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      if arr[j]> arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1]= temp
        swapped = True
    if swapped == False:
      break
  return arr
  
x = [1,5,10,2,5,23,11]
print(bubble_sort2(x))