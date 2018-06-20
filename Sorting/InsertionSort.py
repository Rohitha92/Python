#Insertion sort


def Insertion_sort(arr):
  
  for i in range(1,len(arr)):
    cur_val = arr[i]
    j = i-1  #0
    
    #if cur_val is greater than the element in the list, move the list to right arr[0,..j]
    while j>=0 and cur_val < arr[j]:
      arr[j+1]= arr[j]
      j = j-1
    arr[j+1]= cur_val
  return arr

x =[0, 1, 3, -3, 45,4,87,23,12]
print(Insertion_sort(x))