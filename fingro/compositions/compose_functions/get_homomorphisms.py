import fingro

def get_homomorphisms(dom: fingro.Group, cod: fingro.Group) -> list[fingro.Homomorphism]:
	return fingro.compositions.compose_functions.get_morphisms(
		dom=dom,
		cod=cod,
		generator_images_filter=(
			fingro
			.compositions
			.compose_functions
			.gen_im_filter
			.homomorphism_gen_im_filter
		),
		morphism_filter=lambda morphism : True,
	)
