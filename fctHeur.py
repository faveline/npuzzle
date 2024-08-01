from fctAlgo import searchX

def heurManAll(tab: list, goal: list, size: int) -> int:
	h = 0
	for i in range(size * size):
		h += abs(searchX(tab, size, i)[0] - searchX(goal, size, i)[0]) + \
			abs(searchX(tab, size, i)[1] - searchX(goal, size, i)[1])
	return h


def heur(tab: list, goal: list, size: int, idx: list) -> int:
	return heurManAll(tab, goal, size)
	# nbr = tab[idx[0]][idx[1]]
	# return abs(idx[0] - searchX(goal, size, nbr)[0]) + \
	# 	abs(idx[1] - searchX(goal, size, nbr)[1])