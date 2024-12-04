import fingro
import pytest

import numpy as np

from tests.examples import C2, C3, C7, C8, D2, D7, C2xC2


class TestCompositionsDirectGroup:
	@staticmethod
	def test_direct_group(C2, C3, D2):
		C3xC3 = fingro.Group(
			matrix=np.array([
				[0,1,2, 3,4,5, 6,7,8],
				[1,2,0, 4,5,3, 7,8,6],
				[2,0,1, 5,3,4, 8,6,7],

				[3,4,5, 6,7,8, 0,1,2],
				[4,5,3, 7,8,6, 1,2,0],
				[5,3,4, 8,6,7, 2,0,1],
				
				[6,7,8, 0,1,2, 3,4,5],
				[7,8,6, 1,2,0, 4,5,3],
				[8,6,7, 2,0,1, 5,3,4]
			]),
		)

		assert fingro.compositions.DirectProduct(C3, C3) == C3xC3
		assert fingro.compositions.DirectProduct(C2, C2) == D2

class TestCompositionsSemidirectGroup:
	@staticmethod
	def test_semidirect_group(C2, C7, D7):
		f0, f1 = tuple(
			fingro
			.compositions
			.compose_functions
			.get_homomorphisms(
				C2,
				fingro.compositions.AutomorphismsGroup(C7)
			)
		)
		assert C2 * C7 == fingro.compositions.SemidirectProduct(C2, C7, f0, check_homomorphism=False)
		assert D7 == fingro.compositions.SemidirectProduct(C2, C7, f1, check_homomorphism=False)


class TestCompositionsQuotientGroup:
	@staticmethod
	def test_quotient_group(C2, C8, C2xC2):
		H1 = fingro.Subgroup(C2xC2, sub_index=(0,1))
		H2 = fingro.Subgroup(C8, sub_index=(0,2,4,6))
		H3 = fingro.Subgroup(C8, sub_index=(0,4))
		
		assert C2xC2 / H1 == C2
		assert C8 / H2 == fingro.families.Cyclic(2)
		assert C8 / H3 == fingro.families.Cyclic(4)
