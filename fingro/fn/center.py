import fingro

def center(group: fingro.Group) -> fingro.Subgroup:
	tup_conmute = (group.matrix == group.matrix.T).all(axis=0)
	center_index = tuple( 
		i
			for i, conmute in enumerate(tup_conmute) 
				if conmute
	)
	center = fingro.Subgroup(
		group=group,
		sub_index=center_index,
		name=f'Z({group.name})',
	)
	center.normal = True
	center.abelian = True
	return center
