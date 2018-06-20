#Binary heap using list representation
#Max heap or Min heap



class BinHeap(object):
  
  def __init__(self):
    self.heaplist =[0]
    #the zero in heaplist is to fill the 0th position. so that parent and child numeric calculations will be easy. since parent=p, then left child:2*p and rightchild: 2*p+1
    self.currentsize =0
    
  #insertion
  def perk_up(self, i): #func moves up the nodes to check for max or min as defined and swapping
    
    while(i//2 > 0): #integer division
      
      if self.heaplist[i] < self.heaplist[i//2]:
        temp = self.heaplist[i//2]
        self.heaplist[i//2] = self.heaplist[i]
        self.heaplist[i] = temp
      
      i = i//2
  
  def insert(self, val):
    self.heaplist.append(val)
    self.currentsize = self.currentsize +1
    self.perk_up(self.currentsize)
    
    
  #Delete min
  #the root of the min heap is the smallest. finding is easy.
  #delete of root will include rearranging again.
  #move last item to root and then perk down
  
  def perk_down(self, i):
    while(i*2 <= self.currentsize):
      mc = self.minChild(i)
      if self.heaplist[i] > self.heaplist[mc]:
        temp = self.heaplist[i]
        self.heaplist[i]=self.heaplist[mc]
        self.heaplist[mc] = temp
      i=mc
  
  def minChild(self,i):
    if i*2 +1  > self.currentsize:
      return i*2
    else:
      if self.heaplist[i*2] < self.heaplist[i*2+1]:
        return i*2
      else:
        return i*2+1
  
  def delMin(self):
    returnval = self.heaplist[1] #root node which is min
    self.heaplist[1] = self.heaplist[self.currentsize] #assign end element to root
    self.currentsize = self.currentsize -1 #reduce currentsize since one element will be removed
    self.heaplist.pop()
    self.perk_down(1)
    return returnval
  
  def buildheap_fromList(self, alist):
    i = len(alist)//2
    self.currentsize = len(alist)
    self.heaplist =[0]+alist[:]
    while(i>0):
      self.perk_down(i)
      i=i-1
    
        
a = [3,9,2,10]
b = BinHeap()
b.buildheap_fromList(a)
print(b.delMin())
   
       
       