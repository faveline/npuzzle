from npuzzleGen import make_puzzle, make_goal
from dataClass import dataAlgo, dataSol
from algoAstar import algoA
from fctAlgo import printTab
import random
import time



def main():
	random.seed()
	
	size = 4
	# puzzleIni = make_puzzle(size, True, 10000)
	puzzleIni = [12, 3, 6, 13, 11, 5, 15, 9, 1, 14, 8, 0, 7, 2, 10, 4] # exemple size4 9sec
	# puzzleIni = [17, 14, 20, 24, 15, 3, 2, 16, 23, 21, 0, 19, 18, 1, 7, 6, 11, 4, 10, 5, 13, 9, 22, 8, 12] # exemple size5 65sec
	# puzzleIni = [8, 5, 2, 4, 3, 6, 0, 7, 1]  # exemple size3
	puzzle = size * [None]
	for i in range(size):
		puzzle[i] = puzzleIni[size * i:size * (i + 1)]
	goalIni = make_goal(size)
	goal = size * [None]
	for i in range(size):
		goal[i] = goalIni[size * i:size * (i + 1)]
	open = []
	close = []
	open.append(dataAlgo(puzzle, 0, []))
	data = dataSol(size, 100, goal, [])
	printTab("puzzle initiale:", puzzle, data)
	printTab("goal to reach:", goal, data)
	timeStart = time.time()
	while (True):
		if (algoA(open, close, data) == True):
			break
	print("Max nbr of open set:", len(open))
	print("Max nbr of close set:", len(close))
	print("Nbr total of set:", data.totalOpen)
	print("Time:", time.time() - timeStart)


if __name__ == "__main__":
	main()


# table de h pour recalculer seulement 2 h a chaque heuristique

# parser a faire pour aleatoire ou tabarg
# resultat en fichier pour tester l'order
# checker if tab valide ou pas