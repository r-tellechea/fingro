import fingro
import pytest

import numpy as np

from tests.examples import C1, C2, C4, C8, inclusion_C2_C4, projection_C4_C2, isomorphism_C4, isomorphism_not_trivial_C4, endomorphism_subgroup_C4


class TestHomomorphismInit:
	@staticmethod
	def test_check_homomorphism_pass(C4, C8):
		fingro.Homomorphism(
			f=(np.arange(8) % 4),
			dom=C8,
			cod=C4,
			check_homomorphism=True
		)
	
	@staticmethod
	@pytest.mark.xfail(strict=True)
	def test_check_homomorphism_Fail(C4, C8):
		fingro.Homomorphism(
			f=(np.arange(8) // 2),
			dom=C8,
			cod=C4,
			check_homomorphism=True
		)


class TestHomomorphismProperties:
	@staticmethod
	def test_injective(inclusion_C2_C4, projection_C4_C2):
		assert inclusion_C2_C4.inj
		assert not projection_C4_C2.inj

	@staticmethod
	def test_surjective(inclusion_C2_C4, projection_C4_C2):
		assert projection_C4_C2.sur
		assert not inclusion_C2_C4.sur

	@staticmethod
	def test_bijective(isomorphism_C4, endomorphism_subgroup_C4):		
		assert isomorphism_C4.bij
		assert not endomorphism_subgroup_C4.bij

	@staticmethod
	def test_kernel(C1, C2, inclusion_C2_C4, projection_C4_C2):
		assert inclusion_C2_C4.ker == C1
		assert projection_C4_C2.ker == C2

	@staticmethod
	def test_image(C2, inclusion_C2_C4, projection_C4_C2):
		assert inclusion_C2_C4.im == C2
		assert projection_C4_C2.im == C2


class TestHomomorphismArithmetic:
	# TODO: Cambiar esto cuando se definan las igualdades de homomorphismos.
	@staticmethod
	def test_homomorphism_product(
		isomorphism_C4,
		isomorphism_not_trivial_C4,
		endomorphism_subgroup_C4
	):	
		assert np.all(
			(isomorphism_not_trivial_C4
			* isomorphism_not_trivial_C4).f
			== endomorphism_subgroup_C4.f
		)
	
	@staticmethod
	def test_homomorphism_composition(
		isomorphism_C4,
		isomorphism_not_trivial_C4,
	):
		assert np.all(
			(isomorphism_C4
			@ isomorphism_C4).f
			== isomorphism_C4.f
		)
		assert np.all(
			(isomorphism_not_trivial_C4 
			@ isomorphism_not_trivial_C4).f
			== isomorphism_C4.f
		)
