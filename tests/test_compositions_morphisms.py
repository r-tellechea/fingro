import fingro
import pytest

from tests import C2, C8, D2, D3, C2xC2

class TestCompositionsHomomorphismGroup:
	@staticmethod
	def test_homomorphism_group(C8):
		Hom_C8_C8 = fingro.compositions.HomomorphismsGroup(C8, C8)
		assert Hom_C8_C8 == C8


class TestCompositionsEndomorphismGroup:
	@staticmethod
	def test_endomorphism_group(C8):
		End_C8_C8 = fingro.compositions.EndomorphismsGroup(C8)
		assert End_C8_C8 == C8


class TestCompositionsIsomorphismGroup:
	@staticmethod
	def test_isomorphism_group(D2, D3, C2xC2):
		Iso_C2xC2_D2 = fingro.compositions.IsomorphismsGroup(C2xC2, D2)
		assert Iso_C2xC2_D2 == D3


class TestCompositionsAutomorphismGroup:
	@staticmethod
	def test_homomorphism_group(C8):
		for p in [2, 3, 5, 7]:
			Aut_Cp = fingro.compositions.AutomorphismsGroup(fingro.families.Cyclic(p))
			C_p_1 = fingro.families.Cyclic(p-1)
			assert Aut_Cp == C_p_1
