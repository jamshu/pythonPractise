#Write a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.

import time

def profile(f):
  def g(x):
       start=time.time()
       res=f(x)
       end=time.time()
       t=end-start
       print 'time taken for execution is : ',t
  return g

@profile
def square(x):
  return x * x

square(10)

