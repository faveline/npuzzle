from fctAlgo import searchX


def result(puzzleIni, data):
	size = data.size
	puzzle = size * [None]
	for i in range(size):
		puzzle[i] = puzzleIni[size * i:size * (i + 1)]
	try:
		f = open("../result.txt", "w")
	except:
		return
	f.write("\n".join([str(ele) for ele in puzzle]) + "\n\n")
	for j in range(len(data.result)):
		idx = searchX(puzzle, size, data.result[j])
		id0 = searchX(puzzle, size, 0)
		puzzle[id0[0]][id0[1]] = data.result[j]
		puzzle[idx[0]][idx[1]] = 0
		f.write("\n".join([str(ele) for ele in puzzle]) + "\n\n")
	f.close()
