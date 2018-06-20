#string compression with case sensitive
'''
input: aaaaAAAb output: a4A3b1
input: aB output: a1B1
'''
'''
1.read in the string. 
2. creat letter count dictionary
3.print the dictionary with key and values in a string
'''


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