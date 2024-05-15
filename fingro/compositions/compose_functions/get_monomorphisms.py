import fingro

def get_monomorphisms(dom: fingro.Group, cod: fingro.Group) -> list[fingro.Homomorphism]:
	return fingro.compositions.compose_functions.get_morphisms(
		dom=dom,
		cod=cod,
		generator_images_filter=(
			fingro
			.compositions
			.compose_functions
			.gen_im_filter
			.monomorphism_gen_im_filter
		),
		morphism_filter=lambda morphism : morphism.inj,
	)
