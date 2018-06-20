#Binary tree traversal
# Breadth first (level order)  and Depth first traversal
'''Depth First:
   1. Inorder:    left -> root -> right
   2. Pre-Order:  root -> left -> right
   3. Post-order: left -> right -> root
'''
''' Breadth First also known as level-Order
   1. level 1(root) -> level 2(left, right)-> level3 (left,right)-> so on
   
   2. We use Queue
   
   1. Create empty Queue (Q)
   2. temp= root (start from root)
   3. while temp!= Null
      a. print temp.key
      b. enqueue temp children (left first and then right) to Q
      c. Dequeue a node from Q and assign it to temp
'''
class BinaryTree(object):
  
  def __init__(self, root):
    self.key = root
    self.leftChild = None
    self.rightChild = None
  
  def insertRight(self, newNode):
    if self.rightChild == None:
      self.rightChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.rightChild = self.rightChild
      self.rightChild = t
  
  def insertleft(self, newNode):
    if self.leftChild == None:
      self.leftChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.leftChild = self.leftChild
      self.leftChild = t
  
  def getrootval(self):
    return self.key
  
  def setrootval(self,val):
    self.key = val
    
  def getleftchild(self):
    return self.leftChild


def PrintInorder(root):
    if root != None:
      PrintInorder(root.leftChild)
      print(root.key)
      PrintInorder(root.rightChild)

def PrintPreorder(root):
  if root != None:
    print(root.key)
    PrintPreorder(root.leftChild)
    PrintPreorder(root.rightChild)

def PrintPostorder(root):
  if root:
    PrintPostorder(root.leftChild)
    PrintPostorder(root.rightChild)
    print(root.key)
 
def PrintBreadthFirst(root):
  if root == None:
    return
  
  q =[]
  q.append(root)
  
  while(len(q)>0):
    #print front of q and remove it from q
    print(q[0].key)
    node = q.pop(0)
    
    #enqueue left child
    if node.leftChild is not None:
      q.append(node.leftChild)
    #enqueue right child
    if node.rightChild is not None:
      q.append(node.rightChild)
    
    
  
r = BinaryTree(3)
r.insertleft('l1')
r.insertRight('r1')
r.insertleft('l2')
r.insertRight('r2')
r.insertleft('l3')
PrintInorder(r)
#PrintPreorder(r)
#PrintPostorder(r)
#PrintBreadthFirst(r)