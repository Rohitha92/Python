#Implement Queue
#First in First out
#insert items at the First (zero index)
#delete from first (zero index)

class Queue(object):
  
  def __init__(self):
    self.items=[]
  
  def enqueue(self,val): #add to the rear
    self.items.insert(0,val)

  
  def size(self):
    return len(self.items)
  
  def isempty(self):
    return self.items == []
    
  def dequeue(self):  #removes from the front 
    if self.isempty():
      return "queue empty"
    return self.items.pop()
    
a = Queue()
a.enqueue(3)
a.enqueue(4)
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())