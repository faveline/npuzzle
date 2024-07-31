from fctAlgo import findSmallF, printTab, searchX, searchList
from dataClass import dataAlgo
from copy import deepcopy
from fctHeur import heur


def Right(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0]][idx[1] + 1]
	newSet.tab[idx[0]][idx[1] + 1] = 0


def Left(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0]][idx[1] - 1]
	newSet.tab[idx[0]][idx[1] - 1] = 0


def Up(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0] + 1][idx[1]]
	newSet.tab[idx[0] + 1][idx[1]] = 0


def Down(idx, newSet):
	newSet.tab[idx[0]][idx[1]] = newSet.tab[idx[0] - 1][idx[1]]
	newSet.tab[idx[0] - 1][idx[1]] = 0


def newSetDRLU(idx, next, open:list , close:list , data, move):
	newSet = dataAlgo(deepcopy(next.tab), next.w, deepcopy(next.order), next.orderstr, next.nbrMvt)
	move(idx, newSet)
	if (newSet.tab == data.goal):
		newSet.orderstr += str(newSet.tab[idx[0]][idx[1]])
		newSet.order.append(newSet.tab)
		newSet.nbrMvt += 1
		print("success!")
		print("Nbr of moves:", newSet.nbrMvt, "\nMoves:", newSet.orderstr, "\nOrder:")
		for i in range(newSet.nbrMvt):
			printTab(" ", newSet.order[i], data)
		data.success = True
		return
	newSet.g = next.g + 1
	if (searchList(newSet, open) == 0 or searchList(newSet, close) == 0):
		return
	newSet.h = heur(newSet.tab, data.goal, data.size)
	newSet.f = newSet.g + newSet.w * newSet.h
	newSet.orderstr += str(newSet.tab[idx[0]][idx[1]]) + " "
	newSet.order.append(newSet.tab)
	newSet.nbrMvt += 1
	data.totalOpen += 1
	open.append(newSet)
	


def algoA(open: list, close: list, data):
	if (len(open) == 0):
		print("Impossible")
		return True
	next = findSmallF(open, close)
	idx = searchX(next.tab, data.size, 0)
	if (idx[0] > 0):
		newSetDRLU(idx, next, open, close, data, Down)
	if (idx[0] < data.size - 1):
		newSetDRLU(idx, next, open, close, data, Up)
	if (idx[1] > 0):
		newSetDRLU(idx, next, open, close, data, Left)
	if (idx[1] < data.size - 1):
		newSetDRLU(idx, next, open, close, data, Right)
	if (data.maxNbr < len(open)):
		data.maxNbr = len(open)
	if (data.success is True):
		print("Max nbr of set:", data.maxNbr)
		print("Nbr total of set:", data.totalOpen)
		return True
	return False
