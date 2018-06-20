#Implement queue using 2 stacks.


class Queue2Stacks(object):
  
  def __init__(self):
    
    self.inStack =[]
    self.outStack =[]
    
  def enque(self,val):
    self.inStack.append(val)
  
  def deque(self):
    if not self.outStack:
      if self.inStack == []:
        return "empty stack"
      while self.inStack:
        self.outStack.append(self.inStack.pop())
        
    return self.outStack.pop()
  
s = Queue2Stacks()
s.enque(9)
s.enque(10)
s.enque(11)
print(s.deque())
print(s.deque())
print(s.deque())
print(s.deque())
