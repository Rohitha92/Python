#Implement queue using 2 stacks.
###Use list instead od stack class
'''
1. stack : Last in First out
2. quque : First in First out
###Reversing the stack twice will give out First in First out
3. one stack for reading in
4. next stack for popping
5. add elements to inStack
6. while popping, add from inStack to outStack and popp normally as in stack
'''

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