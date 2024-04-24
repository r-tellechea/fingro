import fingro

def get_subgroup(H: fingro.Group, G: fingro.Group) -> fingro.Subgroup | None:
	for monomorphism in fingro.compositions.compose_functions.get_monomorphisms(H, G):
		return monomorphism.im
	return None
