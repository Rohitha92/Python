#Singly linked list -Implementation


class Node(object):
  
  def __init__(self,val):
    self.val = val
    self.next = None
  
class SinglyLinked(object):  
  
  def __init__(self):
    self.head =None
  
  def insertnode_front(self,val):
    new = Node(val)
    new.next = self.head
    self.head = new
  
  def insertnode_end(self,val):
    new = Node(val)
    temp= self.head
    if(self.head == None):
      self.head = new
      return
    while(temp.next):
        temp =temp.next
    temp.next = new
    
  
  def insert_given(self,val,pos):
    new= Node(val)
    temp = previous=self.head
    if(pos == 0):
      self.insertnode_front(val)
      return
    while(pos!=0):
      previous =temp
      temp = temp.next
      pos = pos-1
    new.next = temp
    previous.next = new
    
  def delete_front(self):
    temp = self.head
    self.head = temp.next
    del temp
  
  def delete_end(self):
    
    temp =self.head
    if(temp.next ==None):
     self.head=0
     print("list empty")
    else :
      while(temp.next):
        previous =temp
        temp =temp.next
      previous.next = None
      del temp
  
  def delete_given(self,pos):
    temp = previous =self.head
    while(pos!=0):
      previous =temp
      temp = temp.next
      pos -=1
    nextnode = temp.next
    previous.next = nextnode
    del temp
    
  def printnodes(self):
    temp = self.head
    while(temp):
      print(temp.val)
      temp = temp.next
  
  
a = SinglyLinked()
a.insertnode_end(3)
a.insertnode_end(5)
a.insertnode_end(7)
a.delete_given(2)
a.printnodes()

    
    
    
    
    