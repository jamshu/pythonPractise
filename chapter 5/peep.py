#Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

def peep(it):
        l = list(it)
	return l[0],l  

print peep(iter(range(5)))
print peep(iter([1,2,6,3,9]))
