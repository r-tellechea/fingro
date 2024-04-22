import fingro

def im(f: fingro.Homomorfism) -> fingro.Subgroup:
	return fingro.Subgroup(
		group=f.cod,
		sub_index=tuple(set(f(i) for i in range(len(f.dom)))),
		name=f'im({f.name})',
	)
