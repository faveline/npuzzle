def findSmallF(open: list, close: list):
	"""find and remove the set with the smallest f from the open list"""
	min = open[0].f
	minI = 0
	for i in range(len(open)):
		if (min > open[i].f):
			min = open[i].f
			minI = i
	next = open[minI]
	open.remove(next)
	close.append(next)
	return next

def printTab(info: str, tab: list, data):
	"""print the given tab, started by info"""
	if (info != ""):
		print(info)
	for i in range(data.size):
		print(tab[i])

def searchX(tab: list, size: int, x: int):
	for i in range(size):
		for j in range(size):
			if (tab[i][j] == x):
				return ([i, j])

def searchList(tab, open):
	for i in range(len(open)):
		if (tab.tab == open[i].tab):
			if (tab.g >= open[i].g):
				return 0
			else:
				open.remove(open[i])
				return 1
	return 1