import fingro

def is_subgroup(subgroup: fingro.Group, group: fingro.Group) -> bool:
	for monomorphism in fingro.compositions.compose_functions.get_monomorphisms(subgroup, group):
		return True
	return False
