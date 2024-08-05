from fctAlgo import searchX


RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

def heurManAll(tab: list, goal: list, size: int) -> int:
	h = 0
	for i in range(size * size):
		h += abs(searchX(tab, size, i)[0] - searchX(goal, size, i)[0]) + \
			abs(searchX(tab, size, i)[1] - searchX(goal, size, i)[1])
	return h


def heurManTab1(puzzle: list, goal: list, size: int, idx: list, move: int):
	
	i = puzzle[idx[0]][idx[1]]
	diff1 = abs(idx[0] - searchX(goal, size, i)[0]) + \
			abs(idx[1] - searchX(goal, size, i)[1])
	if (move == UP):
		diff0 = abs(idx[0] + 1 - searchX(goal, size, 0)[0]) + \
			abs(idx[1] - searchX(goal, size, 0)[1])
	elif (move == DOWN):
		diff0 = abs(idx[0] - 1 - searchX(goal, size, 0)[0]) + \
			abs(idx[1] - searchX(goal, size, 0)[1])
	elif (move == LEFT):
		diff0 = abs(idx[0] - searchX(goal, size, 0)[0]) + \
			abs(idx[1] - 1 - searchX(goal, size, 0)[1])	
	elif (move == RIGHT):
		diff0 = abs(idx[0] - searchX(goal, size, 0)[0]) + \
			abs(idx[1] + 1 - searchX(goal, size, 0)[1])
	else:
		diff0 = 0
	return diff0 + diff1
	

def heurManAllTab(tab: list, puzzle: list, goal: list, size: int):
	tab = [None] * size
	for i in range(size):
		tab[i] = [None] * size
		for j in range(size):
			tab[i][j] = abs(i - searchX(goal, size, puzzle[i][j])[0]) + \
				abs(j - searchX(goal, size, puzzle[i][j])[1])
	return tab


def heur(tab: list, goal: list, size: int) -> int:
	return heurManAll(tab, goal, size)
