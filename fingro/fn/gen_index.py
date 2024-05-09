import fingro
from itertools import product

def gen_index(group: fingro.Group) -> tuple[tuple[int]]:
	
	powers = product(*(
		range(n) for n in (
			group.element_orders[i] 
				for i in group.generators
		)
	))

	dict_element_pow = {
		fingro.fn.index_power(group, group.generators, power) : power
			for power in powers
	}

	return tuple(
		dict_element_pow[i]
			for i in range(len(group))
	)	
