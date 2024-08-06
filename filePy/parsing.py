from fctAlgo import searchX
from copy import deepcopy
from npuzzleGen import make_puzzle, make_goal

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

def parserRand(argv):
	try:
		assert argv[2].isdigit()
	except:
		raise Exception("error second arg")
	return int(argv[2])

def allNbr(listNbr, size):
	for i in range(size * size):
		j = 0
		while (j < len(listNbr)):
			if (i == int(listNbr[j])):
				break
			j += 1
		if j == len(listNbr):
			return False
	return True

def parserFile(argv, tab):
	try:
		f = open(argv[2])
	except:
		raise Exception("error second arg")
	size = -1
	nbrLine = 0
	delimiters = ['\n', '\t', '\r', '\v', '\f', ' ']
	for x in f:
		str = x.partition('#')[0]
		if (str.isspace()):
			continue
		if (size == -1):
			try:
				size = int(x)
			except:
				f.close()
				raise Exception("error size in file")
		else:
			try:
				assert [c.isdigit() or c.isspace() for c in str], "error not a number in tab"
				assert len(str.split(' ')) == size, "error too many column"
			except AssertionError as msg:
				f.close()
				raise Exception(msg)
			nbrLine += 1
			for deli in delimiters:
				str = "".join(str.split(deli))
			str.split()
			tab += str
	if nbrLine != size:
		f.close()
		raise Exception("error tab file nbrLine")
	if not allNbr(tab, size):
		f.close()
		raise Exception("error all number have to be present")
	f.close()
	return size


def parser(argc, argv):
	if (argc != 5):
		raise Exception("error number of arguments")
	if (argv[1] == "rand"):
		size = parserRand(argv)
		puzzleIni = make_puzzle(size, True, 10000)
	elif (argv[1] == "file"):
		puzzleIni = []
		size = parserFile(argv, puzzleIni)
	else:
		raise Exception("error first arg")

