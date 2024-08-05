from fctAlgo import searchX
from copy import deepcopy

def isSolv(tab: list, goal: int, size: int) -> bool:
	pair0 = (abs(searchX(tab, size, 0)[0] - searchX(goal, size, 0)[0]) + \
			abs(searchX(tab, size, 0)[1] - searchX(goal, size, 0)[1])) % 2
	cpy = deepcopy(tab)
	pairI = 0
	for i in range(1, size * size):
		cpyPos = searchX(cpy, size, i)
		goalPos = searchX(goal, size, i)
		if ((abs(cpyPos[0] - goalPos[0]) + abs(cpyPos[1] - goalPos[1])) == 0):
			continue
		tmp = cpy[goalPos[0]][goalPos[1]]
		cpy[goalPos[0]][goalPos[1]] = i
		cpy[cpyPos[0]][cpyPos[1]] = tmp
		pairI += 1
	pairI = pairI % 2
	if (pairI == pair0):
		return True
	return False
