#Selection sort (Ascending order)
#makes exchange only once through each pass
#select the min and place it at the start

def selection_sort(arr):
  
  n = len(arr)   #7
  for i in range(n): #[0,1,2,3,4,5,6]
    min_el = arr[i]
    #find min val in the remaining
    for k in range(i, n):   #i=2, k=2,3,4,5,6
      if arr[k] < min_el:
        min_el = arr[k]
        arr[i], arr[k] = arr[k], arr[i]
        
  return arr

x = [87,1,10,14,3,0,89,-1,34]
print(selection_sort(x))

