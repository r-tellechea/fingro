import fingro
import numpy as np
from itertools import product

def next_index(group: fingro.Group, index: tuple[int]) -> tuple[int]:
	array_index = np.array(tuple(product(index, index)))
	return tuple(
		set(
			group.matrix[
				array_index[:,0], 
				array_index[:,1]
			].ravel()
		)
		| set(index)
	)

def genenated_sub_index(group: fingro.Group, index: tuple[int]) -> tuple[int]:
	index_extend = next_index(group, index)
	if len(index) == len(index_extend):
		return index
	else:
		return genenated_sub_index(group, index_extend)

def generated_subgroup(group: fingro.Group, index: tuple[int]) -> fingro.Subgroup:
	sub_index = tuple(sorted(genenated_sub_index(group, index)))
	return fingro.Subgroup(
		group=group,
		sub_index=sub_index,
	)
