import fingro

def im(f: fingro.Homomorphism) -> fingro.Subgroup:
	return fingro.Subgroup(
		group=f.cod,
		sub_index=tuple(sorted(set(f.f))),
		name=f'im({f.name})',
	)
