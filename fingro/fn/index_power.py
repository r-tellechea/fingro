import fingro
from functools import reduce

def index_power(group: fingro.Group, index: tuple[int], power: tuple[int]) -> int:
	return reduce(
		lambda i, j : group.matrix[i,j],
		(i
			for i, p in zip(index, power) 
				for _ in range(p)),
		0
	)
