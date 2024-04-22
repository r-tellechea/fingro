import fingro
from typing import Callable, Type, Generator
from itertools import product

def get_morfisms(
		dom: fingro.Group,
		cod: fingro.Group,
		pair_filter: Callable[tuple[fingro.Group], dict[int, tuple[int]]],
		morfism_filter: Callable[fingro.Homomorfism, bool]=(lambda morfism : True),
	) -> Generator[fingro.Homomorfism]:

	dict_assignations = pair_filter(dom, cod)
	
	index = 0
	for assignation in product(*[dict_assignations[i] for i in range(len(dom))]):
		try:
			morfism = fingro.Homomorfism(
				f = (lambda i : assignation[i]),
				dom=dom,
				cod=cod,
				check_homomorfism=True,
				name=f'f{index} : {dom.name} → {cod.name}'
			)
			if morfism_filter(morfism):
				yield morfism
				index += 1
		except:
			pass
