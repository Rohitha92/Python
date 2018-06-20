#Unique characters in a string : case sensitive

'''
Return true if all the characters are Unique
'''
'''
1. Read in the characters.
2. Add to seen "set" if not seen
3. if is in seen, return False
4. else return true
'''

def isUnique_String2(a):
  return (len(set(a)) == len(a))
  
  
def isUnique_String(a):
  
  if len(a) ==0:
    return ""
  
  if len(a) ==1:
    return True
  seen = set()
  for i in a:
    if i not in seen:
      seen.add(i)
    else:
      return False

  return True
  
b ="gOooo"
print(isUnique_String2(b))
