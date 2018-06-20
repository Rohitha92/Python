# Recursion

#.factorial

def fact(n):
  
  if (n ==0):  #base case to terminate the loop
    return 1 
  
  else:
    return n* fact(n-1)
    

#1. Takes integer and find the cumulative sum of 0
# n= 5 then result = 5+4+3+2+1+0

def cumsum(n):
  
  if (n==0):
    return 0
  else:
    return n + cumsum(n-1)
    

#2.Sum of all individual integers in a given number
# n=256 then result = 2+5+6

def sumint(n):
  
  # 123%10 =3 
  # 123/10 =12
  if(len(str(n)==1)):
    return n
  
  else:
    return (n%10)+sumint(int(n/10))
    #4+sumint(123)
    #4+3+sumint(12)
    #4+3+2+sumint(1)
    #4+3+2+1+0

#create function word_split(input, list)
#recursively check and split words accordingly found in given list
#input-> word_slit('ilovedogs',['i','am','dog','love'])
#output -> ['i', 'love', 'dog']

def word_split(mystring, dict_list, output=None):
  
  if output is None:
    output=[]
    
  for word in dict_list:
    
    if mystring.startswith(word):
      output.append(word)
    
      return word_split(mystring[len(word):],dict_list, output)
  
  return output

a = "ilovedogs"
dictlist = ["i","love", "dog"]
print(word_split(a,dictlist))









      
      