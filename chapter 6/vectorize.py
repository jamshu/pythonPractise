#write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.

def vectorize(f):
   def g(l):
      res=[]
      for i in l:
         v=f(i)
         res.append(v)
      return res
   return g

s=vectorize(len)
print s([[1,7,2],[3,4,5,5]])
