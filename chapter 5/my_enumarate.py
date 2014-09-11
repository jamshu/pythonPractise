#The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.

def enumerate(list1):
        res = []
	for item in list1:
		res.append((item,list1.index(item)))
  	return res

print enumerate([2,4,6,1])
  
