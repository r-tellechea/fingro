import fingro
import numpy as np
from typing import Callable, Type, Generator
from itertools import product

def get_morphisms(
		dom: fingro.Group,
		cod: fingro.Group,
		generator_images_filter: Callable[tuple[fingro.Group], dict[int, tuple[int]]],
		morphism_filter: Callable[fingro.Homomorphism, bool]=(lambda morphism : True),
	) -> Generator:

	dict_assignations = generator_images_filter(dom, cod)
	
	index = 0
	for assignation in product(*[dict_assignations[i] for i in dom.generators]):
		try:
			morphism = fingro.fn.induced_homomorphism(
				dom=dom,
				cod=cod,
				generator_images=assignation,
				name=f'f{index} : {dom.name} → {cod.name}',
				check_homomorphism=True
			)

			if morphism_filter(morphism):
				yield morphism
				index += 1
		except ValueError as e:
			if not str(e) == 'Not homomorphism.':
				raise e
