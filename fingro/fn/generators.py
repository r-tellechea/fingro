import fingro
import numpy as np
from functools import reduce
from itertools import product, combinations

def cicle_i(group: fingro.Group, i: int) -> tuple[int]:
	list_orbit = [0]
	j = i
	while j != 0:
		list_orbit.append(j)
		j = group.matrix[j, i]
	return set(list_orbit)

def generators(group: fingro.Group) -> tuple[int]:
	if len(group) == 1:
		return (0,)

	cicles = {
		i : cicle_i(group, i) 
			for i in range(1, len(group))
	}

	for n_generators in range(1, len(group) + 1):
		for index_gens in combinations(range(1, len(group)), n_generators):
			index_array = np.array(list(product(* [cicles[i] for i in index_gens])))
			generated_array = reduce(
				lambda array_i, array_j : group.matrix[array_i, array_j],
				(index_array[:, i] for i in range(index_array.shape[1]))
			)
			if len(set(generated_array)) == len(group):
				return index_gens

	raise ValueError('Strange error: Cannot compute the group generators.')
