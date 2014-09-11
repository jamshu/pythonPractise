#a function treemap to map a function over nested list.
def treemap(function , list1):
	for item in list1:
		if isinstance(item,list):
			treemap(function , item)
		else:
			position=list1.index(item)
			list1[position] = function(item)
	return list1
print treemap(lambda x: x*3, [1, 2, [3, 4, [5]]])



#[1, 4, [9, 16, [25]]]
