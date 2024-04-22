import fingro
from typing import Callable, Type
from itertools import product

def get_morfisms(
		dom: fingro.Group,
		cod: fingro.Group,
		pair_filter: Callable[tuple[fingro.Group], dict[int, tuple[int]]],
		morfism_filter: Callable[fingro.Homomorfism, bool]=(lambda morfism : True),
	) -> tuple[fingro.Homomorfism]:

	dict_assignations = pair_filter(dom, cod)

	if 0 in map(len, dict_assignations.values()):
		return tuple()
	
	list_morfisms = []
	
	for assignation in product(*[dict_assignations[i] for i in range(len(dom))]):
		try:
			morfism = fingro.Homomorfism(
				f = lambda i : assignation[i],
				dom=dom,
				cod=cod,
				check_homomorfism=True,
			)
			if morfism_filter(morfism):
				list_morfisms.append(morfism)
		except:
			pass
	
	return tuple(list_morfisms)
