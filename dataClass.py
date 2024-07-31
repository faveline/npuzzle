from dataclasses import dataclass, field

@dataclass
class dataAlgo:
	tab: list
	g: int = field(default=0, init=False)
	h: int = field(default=0, init=False)
	f: int = field(default=0, init=False)
	w: int
	order: list
	orderstr: str
	nbrMvt: int = 0

@dataclass
class dataSol:
	totalOpen: int = field(default=1, init=False)
	maxNbr: int = field(default=1, init=False)
	size: int
	goal: list
	success: int = field(default=False, init=False)
