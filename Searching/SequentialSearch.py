#sequential search
#ordered input and unorderd input
#search an element(n) in the given list (array)


#unordered: O(n)
def seq_search(array, n):
  
  pos =0  #position
  found = False
  
  while pos < len(array):
    
    if array[pos] == n:
      found = True
    pos = pos+1
  
  return found

#arr =[1,11,2, 18, 3,4,5] #unordered list
#print(seq_search(arr,1))
#print(seq_search(arr,8))

def ordered_seq_search(array,n):
  
  pos =0
  found = False
  stop = False
  
  while(pos<len(array) and not stop ):
    if array[pos]==n:
      found= True
    else:
      if array[pos]> n:
        stop = True
      else:
        pos =pos+1
  
  return found

def ordered_seq_search2(array,n):
  
  pos =0
  found = False
  while(pos<len(array) and array[pos]<=n ):
    
    if array[pos]==n:
      found= True
        
    pos =pos+1
  
  return found


  
arr =[1,3,4,15,18,30,34] #ordered list
print(ordered_seq_search2(arr, 30))