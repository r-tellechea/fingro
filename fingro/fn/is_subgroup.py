import fingro

def is_subgroup(H: fingro.Group, G: fingro.Group) -> bool:
	for monomorphism in fingro.compositions.compose_functions.get_monomorphisms(H, G):
		return True
	return False
