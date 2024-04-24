import fingro
import numpy as np
from itertools import product


def cicle_i(group: fingro.Group, i: int) -> tuple[int]:
	list_orbit = [0]
	j = i
	while j != 0:
		list_orbit.append(j)
		j = group.matrix[j, i]
	return set(list_orbit)


def get_cicles(group: fingro.Group) -> dict[int, set[int]]:
	return {
		(i,) : cicle_i(group, i)
			for i in range(1, len(group)) # We don't want the (0,) : {0,} cicle.
	}


def next_generation_sub_index(group: fingro.Group, index: set[int]) -> set[int]:
	array_index = np.array(tuple(product(index, index)))
	return index | set(
		group.matrix[
			array_index[:,0], 
			array_index[:,1]
		].ravel()
	)


def genenated_sub_index(group: fingro.Group, index: set[int]) -> tuple[int]:
	index_extend = next_generation_sub_index(group, index)
	return (index if len(index) == len(index_extend) 
		else genenated_sub_index(group, index_extend))


def remove_redundant_generators(cicles: dict[tuple[int], set[int]]) -> dict[tuple[int], set[int]]:
	# TODO: There is probably an algorithm to improve this.abs
	# From a partially ordered set, return all maximal elements 
	# (ie, {e in X : ¬exists x in X : e <= x}).

	maximal_cicles = {}

	for i, cicle_i in reversed(cicles.items()):
		
		maximal_cicles = {
			j : cicle_j
				for j, cicle_j in maximal_cicles.items()
					if not cicle_j <= cicle_i 
		}

		if all( len(cicle_i & cicle_j) == 1 for cicle_j in maximal_cicles.values() ):
			maximal_cicles[i] = cicle_i

	maximal_cicles = {
		i : maximal_cicles[i]
			for i in sorted(maximal_cicles)
	}
	return maximal_cicles

def generators(group: fingro.Group) -> tuple[int]:
	
	maximal_cicles = remove_redundant_generators(get_cicles(group))
	
	for i, cicle in maximal_cicles.items():
		if len(cicle) == len(group):
			return i

	list_generator_sets = list(map(set, maximal_cicles.keys()))
	list_generated_sets = list(maximal_cicles.values())
	
	# Two index so we don't repeat union combinations.
	current_computed_index = 0
	next_computed_index = len(list_generated_sets)
	
	while True:
		
		# Step: For each new pair of sets, if is new, compute the generated elements.
		for i, (generator_i, generated_i) in enumerate(zip(list_generator_sets, list_generated_sets)):
			for j, (generator_j, generated_j) in enumerate(zip(
				list_generator_sets[current_computed_index:],
				list_generated_sets[current_computed_index:],
			)):
				generator = generator_i | generator_j
				
				# If the generator is not new, continue.
				if generator in list_generator_sets:
					continue

				generated_base = generated_i | generated_j

				# If the union of the generated sets is in another generated set, 
				# then it generated subgroup has already been generated, so continue. 
				if any(generated_base <= previous_gen 
						for previous_gen in list_generated_sets):
					continue

				generated = genenated_sub_index(group, generated_base)
				
				if len(generated) == len(group):
					return tuple(sorted(generator))

				list_generator_sets.append(generator)
				list_generated_sets.append(generated)
		
		current_computed_index = next_computed_index
		next_computed_index = len(list_generated_sets)
		
		# If no element was added (so we are in an infinite loop).
		if current_computed_index == next_computed_index:
			group.check_group_properties()
			raise ValueError('Strange error: Cannot compute the group generators.')
