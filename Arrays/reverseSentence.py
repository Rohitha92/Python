#Array- reverse the sentence:

'''
  "sun rises in the east" becomes "east the in rises sun"
'''

def rev_sentence(mystring):
  #stringlist = mystring.split()
  #return (' '.join(map(str,stringlist[::-1])))
  #can combine the above two in one line
  return (' '.join(map(str, mystring.split()[::-1])))


def rev_sentence2(mystring):
  words = []
  n = len(mystring)
  space = [' ']
  
  i=0 
  while i< n:
    if mystring[i] not in space:
      word_start =i 
      while i < n and mystring[i] not in space:
        i +=1
      words.append(mystring[word_start:i])
    
    i +=1
  
  return reverse_list(words)

def reverse_list(mylist):
  sentence = ""
  n = len(mylist)
  for i in range(1,n):
    sentence+= mylist[n-i] + " "
  sentence += mylist[0]  
  return sentence  
  
a = "sun rises in the east"
reversed_Sen = rev_sentence2(a)
print(reversed_Sen)
print(len(a))
print(len(reversed_Sen))
