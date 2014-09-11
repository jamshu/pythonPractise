#Write a function permute to compute all possible permutations of elements of a given list.

import itertools
def all_perms(elements):
  return list(itertools.permutations(elements, len(elements)))
    
print all_perms([1,2,3,5])
