import fingro

def get_subgroup(subgroup: fingro.Group, group: fingro.Group) -> fingro.Subgroup | None:
	for monomorphism in fingro.compositions.compose_functions.get_monomorphisms(subgroup, group):
		return monomorphism.im
	return None
