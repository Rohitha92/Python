#Implement Deque
#two sided queue. can add/remove from front/rear


class Deque(object):
  
  def __init__(self):
    self.items=[]
    
  def isempty(self):
    return self.items == []
  
  def addRear(self,val):
    self.items.insert(0, val)
  
  def addFront(self,val):
    self.items.append(val)
    
  def removeRear(self):
    if self.isempty():
      return "deque is empty"
    
    return self.items.pop(0)
  
  def printlist(self):
    return self.items
    
  def removeFront(self):
    if self.isempty():
      return "deque is empty"
    return self.items.pop()
  
  def size(self):
    return len(self.items)
  

s= Deque()
s.addFront(1)
s.addFront(3)
s.addRear(4)
s.addRear(6)
print(s.printlist())
s.removeFront()
print(s.printlist())
print(s.size())

d = Deque()
d.addFront('hello')
d.addRear('world')
print(d.removeFront() + " " + d.removeRear())
print(d.isempty())
