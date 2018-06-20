#Binary search

def binary_search(arr, n):
  
  found = False
  first = 0
  last= len(arr)-1
  
  while(first<=last and not found):
    mid = (first+last)//2
    
    if (arr[mid]==n):
      found =True
    else:
      if (n < arr[mid]):
        last = mid-1    #left half
      else:
        first = mid+1  #right half
        
  return found


def recursive_binary_search(arr,n):
  #base class
  if len(arr)==0:
    return False
  
  else:
    mid = len(arr)//2
  
    if(arr[mid]==n):
      return True
    else:
      if(n < arr[mid]):
        return recursive_binary_search(arr[:mid], n)
      else:
        return recursive_binary_search(arr[mid+1:],n)
  
  
  
array = [1,2,3,10,67,89,90] #need sorted array
print(binary_search(array,67))
print(recursive_binary_search(array,67))