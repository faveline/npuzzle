from fctAlgo import searchX


def heur(tab: list, goal: list, size: int) -> int:
	h = 0
	for i in range(size * size):
		h += abs(searchX(tab, size, i)[0] - searchX(goal, size, i)[0]) + \
			abs(searchX(tab, size, i)[1] - searchX(goal, size, i)[1])
	return h
