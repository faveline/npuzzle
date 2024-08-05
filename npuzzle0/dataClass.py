from dataclasses import dataclass, field


class dataAlgo:
	def __init__(self, tab, g, order):
		self.tab = tab
		self.g = g
		self.h = 0
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
	fct: int #int is only to initialize, it's really the heuristic function
