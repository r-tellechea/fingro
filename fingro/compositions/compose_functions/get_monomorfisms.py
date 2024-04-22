import fingro

def get_monomorfisms(dom: fingro.Group, cod: fingro.Group) -> list[fingro.Homomorfism]:
	return fingro.compositions.compose_functions.get_morfisms(
		dom=dom,
		cod=cod,
		pair_filter=fingro.compositions.compose_functions.pair_filters.monomorfism_pair_filter,
		morfism_filter=lambda morfism : morfism.inj,
	)
