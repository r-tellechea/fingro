import fingro

def ker(f: fingro.Homomorphism) -> fingro.Subgroup:
	return fingro.Subgroup(
		group=f.dom,
		sub_index=tuple( i for i in range(len(f.dom)) if f.f(i) == 0 ),
		name=f'ker({f.name})',
	)
