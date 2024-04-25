import fingro
import numpy as np

def ker(f: fingro.Homomorphism) -> fingro.Subgroup:
	return fingro.Subgroup(
		group=f.dom,
		sub_index=tuple(np.arange(len(f.dom))[f.f == 0]),
		name=f'ker({f.name})',
	)
