from npuzzleGen import make_puzzle, make_goal
from dataClass import dataAlgo, dataSol
from algoAstar import algoA
from fctAlgo import printTab
import random
import time



def main():
	random.seed()
	timeStart = time.time()
	size = 3
	puzzleIni = make_puzzle(size, True, 10000)
	puzzle = size * [None]
	for i in range(size):
		puzzle[i] = puzzleIni[size * i:size * (i + 1)]
	goalIni = make_goal(size)
	goal = size * [None]
	for i in range(size):
		goal[i] = goalIni[size * i:size * (i + 1)]
	open = []
	close = []
	open.append(dataAlgo(puzzle, 100, [], ""))
	data = dataSol(size, goal)
	printTab("puzzle initiale:", puzzle, data)
	printTab("goal to reach:", goal, data)
	while (True):
		if (algoA(open, close, data) == True):
			print("Time:", time.time() - timeStart)
			break
	

if __name__ == "__main__":
	main()
