import fingro

def is_subgroup(H: fingro.Group, G: fingro.Group) -> bool:
	for monomorfism in fingro.compositions.compose_functions.get_monomorfisms(H, G):
		return True
	return False
