from dataclasses import dataclass, field


class dataAlgo:
	def __init__(self, tab, g, hSum, order):
		self.tab = tab
		self.g = g
		self.hSum = hSum
		self.f = 0
		self.order = order
		self.parent = 0
	

@dataclass
class dataSol:
	totalOpen: int = field(default=1, init=False)
	size: int
	w: int
	goal: list
	success: int = field(default=False, init=False)
	result: list
	resultNbr: int = field(default=0, init=False)
	diff0: int = field(default=0, init=False)
	diff1: int = field(default=0, init=False)
