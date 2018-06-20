#Binary tree using OOP with nodes and references.

class BinaryTree(object):
  
  def __init__(self,root):
    
    self.key = root
    self.leftChild = None
    self.rightChild = None
    
  def insertLeft(self, newNode):
    if self.leftChild == None:
      self.leftChild = BinaryTree(newNode)
    
    else:  #left child existing
      t = BinaryTree(newNode) #create new node
      t.leftChild = self.leftChild #new node leftchild is existing leftchild
      self.leftChild = t #set newnode as latest leftchild
    
  
  def insertRight(self, newNode):
    
    if self.rightChild ==None:
      self.rightChild = BinaryTree(newNode)
    
    else:
      t = BinaryTree(newNode)
      t.rightChild = self.rightChild
      self.rightChild = t
  
  def getrightChild(self):
    return self.rightChild
  
  def getleftChild(self):
    return self.leftChild
  
  def setRootval(self,val):
    self.key = val
  
  def getRootval(self):
    return self.key


r = BinaryTree(1)
r.insertRight(3)
r.insertRight(4)
print(r.getrightChild().getrightChild().getRootval())