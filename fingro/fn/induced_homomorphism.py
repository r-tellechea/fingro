import fingro
import numpy as np

def induced_homomorphism(	
	dom: fingro.Group,
	cod: fingro.Group,
	generator_images: tuple[int],
	name: str='f',
	check_homomorphism: bool=True,
	) -> fingro.Homomorphism:

	im_array = np.array([
		fingro.fn.index_power(cod, generator_images, tup)
			for tup in dom.gen_index
	])
	
	return fingro.Homomorphism(
		f=im_array,
		dom=dom,
		cod=cod,
		name=name,
		check_homomorphism=check_homomorphism,
	)
