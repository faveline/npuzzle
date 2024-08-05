from fctAlgo import searchX

def manhattanE(tab: list, goal: list, size: int) -> int:
	"""Manhattan"""
	h = 0
	for i in range(1, size * size):
		a = searchX(tab, size, i)
		b = searchX(goal, size, i)
		h += abs(a[0] - b[0]) + abs(a[1] - b[1])
	return h

def hammingE(tab: list, goal: list, size: int) -> int:
	"""Hamming"""
	h = 0
	for i in range(1, size * size):
		pos = searchX(tab, size, i)
		h += i ^ goal[pos[0]][pos[1]]
	return h

def euclidienneE(tab: list, goal: list, size: int) -> int:
	"""Euclidienne"""
	h = 0
	for i in range(1, size * size):
		a = searchX(tab, size, i)
		b = searchX(goal, size, i)
		h += pow(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2), 0.5)
	return h

def chebyshevE(tab: list, goal: list, size: int) -> int:
	"""Chebyshev"""
	h = 0
	for i in range(1, size * size):
		a = searchX(tab, size, i)
		b = searchX(goal, size, i)
		h += max(abs(a[0] - b[0]), abs(a[1] - b[1]))
	return h

def heur(tab: list, goal: list, size: int, fct) -> int:
	return fct(tab, goal, size)
