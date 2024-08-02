from fctAlgo import findSmallF, printTab, searchX, searchList, sumTab, equalArray
from dataClass import dataAlgo
from copy import deepcopy
from fctHeur import heur, heurManTab1


RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4


def Right(idx, newSet, data):
	newSet.parent = RIGHT
	data.diff0 = abs(idx[0] - searchX(data.goal, data.size, 0)[0]) + \
			abs(idx[1] - searchX(data.goal, data.size, 0)[1])
	data.diff0 += abs(idx[0] - searchX(data.goal, data.size, newSet.tab[idx[0]][idx[1] + 1])[0]) + \
			abs(idx[1] + 1 - searchX(data.goal, data.size, newSet.tab[idx[0]][idx[1] + 1])[1])
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0]][idx[1] + 1]
	newSet.tab[idx[0]][idx[1] + 1] = 0

	

def Left(idx, newSet, data):
	newSet.parent = LEFT
	data.diff0 = abs(idx[0] - searchX(data.goal, data.size, 0)[0]) + \
			abs(idx[1] - searchX(data.goal, data.size, 0)[1])
	data.diff0 += abs(idx[0] - searchX(data.goal, data.size, newSet.tab[idx[0]][idx[1] - 1])[0]) + \
			abs(idx[1] - 1 - searchX(data.goal, data.size, newSet.tab[idx[0]][idx[1] - 1])[1])
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0]][idx[1] - 1]
	newSet.tab[idx[0]][idx[1] - 1] = 0

	

def Up(idx, newSet, data):
	newSet.parent = UP
	data.diff0 = abs(idx[0] - searchX(data.goal, data.size, 0)[0]) + \
			abs(idx[1] - searchX(data.goal, data.size, 0)[1])
	data.diff0 += abs(idx[0] + 1 - searchX(data.goal, data.size, newSet.tab[idx[0] + 1][idx[1]])[0]) + \
			abs(idx[1] - searchX(data.goal, data.size, newSet.tab[idx[0] + 1][idx[1]])[1])
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0] + 1][idx[1]]
	newSet.tab[idx[0] + 1][idx[1]] = 0

	

def Down(idx, newSet, data):
	newSet.parent = DOWN
	data.diff0 = abs(idx[0] - searchX(data.goal, data.size, 0)[0]) + \
			abs(idx[1] - searchX(data.goal, data.size, 0)[1])
	data.diff0 += abs(idx[0] - 1 - searchX(data.goal, data.size, newSet.tab[idx[0] - 1][idx[1]])[0]) + \
			abs(idx[1] - searchX(data.goal, data.size, newSet.tab[idx[0] - 1][idx[1]])[1])
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0] - 1][idx[1]]
	newSet.tab[idx[0] - 1][idx[1]] = 0



def newSetDRLU(idx, next, open:list , close:list , data, move):
	data.totalOpen += 1
	newSet = dataAlgo(deepcopy(next.tab), next.g + 1, next.hSum, deepcopy(next.order))
	move(idx, newSet, data)
	if (searchList(newSet, close, data.size) == 0 or searchList(newSet, open, data.size) == 0):
		return
	
	if (equalArray(newSet.tab, data.goal, data.size)):
		newSet.order.append(newSet.tab[idx[0]][idx[1]])
		data.result = newSet.order
		data.resultNbr = newSet.g
		data.success = True
		return
	
	# newSet.h = heur(newSet.tab, data.goal, data.size)
	data.diff1 = heurManTab1(newSet.tab, data.goal, data.size, idx, newSet.parent)
	newSet.hSum += (data.diff1 - data.diff0)
	newSet.f = newSet.g + data.w * newSet.hSum
	
	newSet.order.append(newSet.tab[idx[0]][idx[1]])
	open.append(newSet)
	

def algoA(open: list, close: list, data):
	if (len(open) == 0):
		print("error")
		return True
	next = findSmallF(open, close)
	idx = searchX(next.tab, data.size, 0)
	if (next.parent != UP and idx[0] > 0):
		newSetDRLU(idx, next, open, close, data, Down)
	if (next.parent != DOWN and idx[0] < data.size - 1):
		newSetDRLU(idx, next, open, close, data, Up)
	if (next.parent != RIGHT and idx[1] > 0):
		newSetDRLU(idx, next, open, close, data, Left)
	if (next.parent != LEFT and idx[1] < data.size - 1):
		newSetDRLU(idx, next, open, close, data, Right)
	if (data.success is True):
		print("success!")
		print("Nbr of moves:", data.resultNbr, "\nMoves:", data.result)
		return True
	# print(len(open), len(close), data.totalOpen)
	return False
