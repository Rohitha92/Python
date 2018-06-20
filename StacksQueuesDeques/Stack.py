#Implement Stack 

class Stack(object):
  def __init__(self):
    self.items =[]
    
  def isempty(self):
    return self.items == []
  
  def push(self, val):
    self.items.append(val)
  
  def pop(self):
    return self.items.pop() #inbuilt
  
  def peek(self):
    return self.items[len(self.items)-1]
  
  def size(self):
    return len(self.items)


s= Stack()
s.push(2)
print(s.isempty())
print(s.pop())
print(s.isempty())
  