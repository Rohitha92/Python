#are the two sentences anagrams or not.

import string    

def isAnagram(a,b): #O(n^2)
  values = dict()
  values2 =dict()
  for index, letter in enumerate(string.ascii_lowercase):
     values[letter] = 0
     values2[letter]=0

  list_keys = list(values.keys())
  a =a.replace(' ','').lower()
  b= b.replace(' ','').lower()
  
  if len(a) != len(b):
    return False
  else:
    for i in range(len(a)):
      for k in range(len(list_keys)):
        if a[i] == list_keys[k]:
          values[list_keys[k]] +=1
    
    for i in range(len(b)):
      for k in range(len(list_keys)):
        if b[i] == list_keys[k]:
          values2[list_keys[k]] +=1
    return (values == values2)

def isAnagram2(a,b): #O(n)
  a = a.replace(' ','').lower()
  b = b.replace(' ','').lower()
  
  count = dict()
  
  if len(a) != len(b):
    return False
  
  for i in a:
    if i in count:
      count[i] +=1
    else:
      count[i]=1
  
  for i in b:
    if i in count:
      count[i] -=1
    else:
      count[i]=1
  
  for i in count:
    if count[i] != 0 :
      return False
  
  return True

mystring = "The Morse Code"
mystring2 = "Here comes dots"
print(isAnagram2(mystring, mystring2))




  
