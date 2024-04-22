import fingro

def get_monomorphisms(dom: fingro.Group, cod: fingro.Group) -> list[fingro.Homomorphism]:
	return fingro.compositions.compose_functions.get_morphisms(
		dom=dom,
		cod=cod,
		pair_filter=fingro.compositions.compose_functions.pair_filters.monomorphism_pair_filter,
		morphism_filter=lambda morphism : morphism.inj,
	)