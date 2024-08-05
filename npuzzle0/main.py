from npuzzleGen import make_puzzle, make_goal
from dataClass import dataAlgo, dataSol
from algoAstar import algoA
from fctAlgo import printTab
from parsing import isSolv
from fctHeur import manhattanE, hammingE, euclidienneE, chebyshevE
import random
import time


def main():
	random.seed()
	
	size = 5
	# puzzleIni = make_puzzle(size, True, 10000)
	# puzzleIni = [12, 1, 2, 4, 0, 13, 14, 5, 10, 8, 3, 6, 11, 9, 7, 15] # exemple w=100 1sec w=1 100sec
	# puzzleIni = [12, 3, 6, 13, 11, 5, 15, 9, 1, 14, 8, 0, 7, 2, 10, 4] # exemple size4 9sec
	# puzzleIni = [9, 7, 12, 15, 1, 10, 3, 5, 14, 13, 4, 11, 8, 2, 0, 6] # exemple size4 1sec
	puzzleIni = [17, 14, 20, 24, 15, 3, 2, 16, 23, 21, 0, 19, 18, 1, 7, 6, 11, 4, 10, 5, 13, 9, 22, 8, 12] # exemple size5 65sec
	# puzzleIni = [1, 0, 3, 4, 23, 6, 20, 2, 22, 24, 5, 7, 19, 21, 29, 25, 26, 8, 31, 33, 32, 35, 34, 9, 18, 17, 30, 28, 13, 10, 16, 15, 14, 12, 27, 11] # exmeple s6 h=e 29sec h=m 1s
	# puzzleIni = [0, 5, 3, 1, 6, 4, 8, 2, 7]  # exemple size3
	# puzzleIni = [27, 3, 15, 21, 31, 1, 23, 20, 0, 22, 16, 19, 13, 29, 18, 14, 25, 6, 32, 26, 24, 30, 2, 8, 34, 12, 9, 7, 4, 35, 33, 11, 5, 28, 17, 10] #h=m 460s 62kset h=e 130s 32kset
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
	data = dataSol(size, 100, goal, [], euclidienneE)
	printTab("puzzle initiale:", puzzle, data)
	printTab("goal to reach:", goal, data)
	if (not isSolv(puzzle, goal, size)):
		print("This n-puzzle is unsolvable.")
		return
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

# order et close en np.array, defini d'une tres grande taille pour pas de probleme

# parser a faire pour aleatoire ou tabarg
# resultat en fichier pour tester l'order
