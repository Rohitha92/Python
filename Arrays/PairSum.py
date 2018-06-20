#Array pair sum

def pairsum(mylist, tn): #this is O(n)
  seen = set()
  output = set()
  for num in mylist:
      target = tn - num  #since we know tn will be greater. We need to find the target in out list
      if target not in seen:
         seen.add(num)
         print(seen)
      else:
         output.add((min(target,num), max(num, target)))
  
  return output   
     
 
mylist2 = [4,0,2,2,4]
tn2 = 4
print('\n'.join(map(str,list(pairsum(mylist2, tn2)))))
