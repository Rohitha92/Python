#Array- find the largest continous sum in an array of positive and negative integers

'''
1.read in the array
2.keep on adding the positive numbers
3. return the sum
'''

def largesum(arr):
  if len(arr) == 0:
    return 0
  current_sum = max_sum = arr[0]
  
  for i in arr[1:]:
    current_sum = max(current_sum+i,i)
    max_sum = max(current_sum, max_sum)
  
  return max_sum
  
  
mylist = [1,2,-1,3,4,10,10,-10,-1]
print(largesum(mylist))