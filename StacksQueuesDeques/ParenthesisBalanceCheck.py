#Balanced parenthesis check
'''
1. Read in the input string as a stack.
2. pop out the string and check for equality. 
'''
'''
basically reverse the string and check
'''
class Stack(object):
  
  def __init__(self):
    self.items=[]
  
  def pop(self):
    return self.items.pop()
  
  def push(self,val):
    self.items.append(val)
  
  def pushvalues(self,val):
    for i in val:
      self.items.append(i)
  
  def isempty(self):
    return self.items==[]
  
  def size(self):
    return len(self.items)
    

def ReverString(self): #NOT for parenthesis check 
    if self.size() %2 !=0:
       return False
    n= self.size()
    for i in range(1,n):
      if self.items[n-i] != self.pop():
        return False
    return True
      


def checkParenthesis(mystring): #only for the parenthesis
    
    if len(mystring)%2 !=0:
       return False
   
    opening = set('({[')  #set of opening brackets
    #tuples of matches
    matches = set([ ('(',')'), ('{','}'), ('[',']')])
    
    stack =[]
    
    for paren in mystring:
      if paren in opening:
        print('paren: {}' .format(paren))
        stack.append(paren)
        print('stack before: {}'.format(stack))
      else:
        
        if len(stack)==0:  #i.e, there is no opening paren
          return False
        
        last_open = stack.pop()
        print('stack after pop:{}'.format(stack))
        if (last_open,paren) not in matches:
          return False
      
    return (len(stack) == 0)
        
    

s = Stack()
a = "[]{}[]"
print(checkParenthesis(a))

