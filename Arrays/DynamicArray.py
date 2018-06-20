# dynamic array implementation

import ctypes

class DynamicArray():
  
  def __init__(self):
    self.n=0
    self.capacity = 1
    self.A= self._make_array(self.capacity)
  
  def __len__(self):
    return self.n 
  
  def __getitem__(self,k):
    if not 0<= k <self.n:
      return IndexError('index out of bounds')
    
    return self.A[k]
    
  def _resizeNassign(self, new_cap):
    B = self._make_array(new_cap)
    for n in range(self.n):
      B[n] = self.A[n]
    self.A = B
    self.capacity = new_cap
    
  def append(self, val):
    if self.n == self.capacity:
      self._resizeNassign(2*self.capacity)
    
    self.A[self.n]=val
    self.n +=1
  
  def _make_array(self, new_cap):
    return (new_cap* ctypes.py_object)()
    

a = DynamicArray()
a.append(1)
a.append(2)
print(a[0])
print(a[1])
    
    