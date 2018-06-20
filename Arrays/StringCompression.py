#string compression with case sensitive

def String_comp(a):
  if len(a) == 0:
    return ""
  if len(a) == 1:
    return a+"1"
  
  letters = dict()
  for i in a:
    if i not in letters:
      letters[i] =1 
    else:
      letters[i] +=1 
  output =""
  for i, k in zip(letters.keys(),letters.values()):
    output += (str(i)+str(k))
  return(output)
  
  
b = "aaaabbbCCDEEFF"
print(String_comp(b))
