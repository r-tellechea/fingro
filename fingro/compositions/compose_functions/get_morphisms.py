import fingro
import numpy as np
from typing import Callable, Type, Generator
from itertools import product

def get_morphisms(
		dom: fingro.Group,
		cod: fingro.Group,
		pair_filter: Callable[tuple[fingro.Group], dict[int, tuple[int]]],
		morphism_filter: Callable[fingro.Homomorphism, bool]=(lambda morphism : True),
	) -> Generator:

	dict_assignations = pair_filter(dom, cod)
	
	index = 0
	for assignation in product(*[dict_assignations[i] for i in range(len(dom))]):
		try:
			morphism = fingro.Homomorphism(
				f=np.array(assignation),
				dom=dom,
				cod=cod,
				check_homomorphism=True,
				name=f'f{index} : {dom.name} → {cod.name}'
			)
			if morphism_filter(morphism):
				yield morphism
				index += 1
		except ValueError as e:
			if not str(e) == 'Not homomorphism.':
				raise e
