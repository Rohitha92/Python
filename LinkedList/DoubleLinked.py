#Doubly linked list implementation

class Node(object):
  
  def __init__(self,val):
    self.val = val
    self.next = None
    self.prev = None

class DoubleLinked(object):
  
  def __init__(self):
    self.head = None
  
  def insert_before(self, val):  #insert before
    new_node = Node(val)
    temp = self.head
    if self.head is None:
      self.head = new_node
    else:
      temp.prev=new_node
      new_node.next = temp
      self.head = new_node
  
  def inset_after(self,val):
    new_node = Node(val)
    temp =self.head
    if self.head is None:
      self.head = new_node
    else:
      while(temp.next):
        temp = temp.next
      temp.next = new_node
      new_node.prev = temp
  
  def print_list(self):
    temp = self.head
    while(temp):
      print(temp.val)
      temp = temp.next

  def reverse_list(self):
    temp = None
    current = self.head
    
    while(current is not None):
      temp = current.prev
      current.prev = current.next
      current.next = temp
      current = current.prev
    if temp is not None:
      self.head = temp.prev

a = DoubleLinked()
a.inset_after(1)
a.inset_after(11)
a.inset_after(13)
a.inset_after(45)
a.reverse_list()
a.print_list()

      
      
      