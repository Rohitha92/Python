#Merge sort -> recursive sort

def merge_sort(arr):
  
  if len(arr)>1:
    mid = len(arr)//2  #integer. not float
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    #divide into single units
    merge_sort(left_half)
    merge_sort(right_half)
    
    i=0 #left_half index
    j=0 #right_half index
    k=0 # arr index
    
    #sorting and merging 
    while(i<len(left_half) and j<len(right_half)):
      
      if(left_half[i]< right_half[j]):
        arr[k] = left_half[i]
        i=i+1
      else:
        arr[k]= right_half[j]
        j=j+1
      k=k+1
    
    while(i<len(left_half)):
      arr[k] = left_half[i]
      i=i+1
      k=k+1
  
    while(j<len(right_half)):
      arr[k] = right_half[j]
      j=j+1
      k= k+1
  
  return arr    

a =[10,2,4,44,23,-2,8,12]
print(merge_sort(a))