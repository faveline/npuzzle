from fctAlgo import findSmallF, printTab, searchX, searchList
from dataClass import dataAlgo
from copy import deepcopy
from fctHeur import heur


RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4


def Right(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0]][idx[1] + 1]
	newSet.tab[idx[0]][idx[1] + 1] = 0
	newSet.parent = RIGHT


def Left(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0]][idx[1] - 1]
	newSet.tab[idx[0]][idx[1] - 1] = 0
	newSet.parent = LEFT


def Up(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0] + 1][idx[1]]
	newSet.tab[idx[0] + 1][idx[1]] = 0
	newSet.parent = UP


def Down(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0] - 1][idx[1]]
	newSet.tab[idx[0] - 1][idx[1]] = 0
	newSet.parent = DOWN


def newSetDRLU(idx, next, open, close, data, move):
	data.totalOpen += 1
	newSet = dataAlgo(deepcopy(next.tab), next.g + 1, deepcopy(next.order))
	move(idx, newSet)
	if (searchList(newSet, close) == 0 or searchList(newSet, open) == 0):
		return

	if (newSet.tab == data.goal):
		newSet.order.append(newSet.tab[idx[0]][idx[1]])
		data.result = newSet.order
		data.resultNbr = newSet.g
		data.success = True
		return

	newSet.h = heur(newSet.tab, data.goal, data.size, data.fct)
	newSet.f = newSet.g + data.w * newSet.h
	newSet.order.append(newSet.tab[idx[0]][idx[1]])
	open.append(newSet)
	

def algoA(open: list, close: list, data):
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
		print("heuristic used:", data.fct)
		print("Nbr of moves:", data.resultNbr, "\nMoves:", data.result)
		return True
	return False
