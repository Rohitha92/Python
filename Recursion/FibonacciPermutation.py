
def permute(s):
  out =[]
  
  if len(s)==1:
    out= [s]
  
  else:
    for i, let in enumerate(s):
      print(i,let)
      for perm in permute(s[:i]+s[i+1:]):
        out += [let+perm]
  return out

#s1 = "abc"
#print(permute(s1))
#print(s1[1:])

#5 ways of doing fibonacci
#https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/

#iterative fibonacci
def fib_iter(n):
  a,b = 0,1
  for i in range(n):
    a, b = b, a+b
  return a

print(fib_iter(10))


#recursive fibonacci
# O(2^n)
def fib_rec(n):
  if(n==0 or n==1):
    return n
  
  else:
    return fib_rec(n-1)+fib_rec(n-2)
print(fib_rec(10))


#dynamic memoization

def fib_dy(n):
  cache = [None] *(n+1)
  #base class
  if(n==1 or n==0):
    return n
  #check cache
  if cache[n] != None:
    return cache[n]
  
  #keep setting cache
  cache[n] = fib_dy(n-1)+fib_dy(n-2)
  return cache[n]
print(fib_dy(12))


















  