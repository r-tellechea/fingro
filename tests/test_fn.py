import fingro
import pytest

from tests import C1, C2, C3, C4, C6, C8, D4, D17, sub_C2_D4, inclusion_C2_C4, projection_C4_C2

class TestFnCenter:
	@staticmethod
	def test_center(C8, D4, sub_C2_D4):
		assert fingro.fn.center(C8) == C8
		assert fingro.fn.center(D4) == sub_C2_D4


class TestFnKer:
	@staticmethod
	def test_kernel(C1, C2, inclusion_C2_C4, projection_C4_C2):
		assert fingro.fn.ker(inclusion_C2_C4) == C1
		assert fingro.fn.ker(projection_C4_C2) == C2


class TestFnIm:
	@staticmethod
	def test_image(C2, inclusion_C2_C4, projection_C4_C2):
		assert fingro.fn.im(inclusion_C2_C4) == C2
		assert fingro.fn.im(projection_C4_C2) == C2

class TestFnIsSubgroup:
	@staticmethod
	def test_is_subgroup(C3, C4, C6, D4):
		assert fingro.fn.is_subgroup(C3, C3)
		assert fingro.fn.is_subgroup(C4, C4)
		assert fingro.fn.is_subgroup(C6, C6)
		assert fingro.fn.is_subgroup(D4, D4)

		assert fingro.fn.is_subgroup(C3, C6)
		assert fingro.fn.is_subgroup(C4, D4)

		assert not fingro.fn.is_subgroup(C3, C4)
		assert not fingro.fn.is_subgroup(C3, D4)
		assert not fingro.fn.is_subgroup(C6, D4)

class TestFnIsomorphic:
	@staticmethod
	def test_isomorphic(C3, C4, C6, D4, D17):
		list_groups = [C3, C4, C6, D4, D17]
		for i, Gi in enumerate(list_groups):
			for j, Gj in enumerate(list_groups):
				assert (i == j) == (fingro.fn.isomorphic(Gi, Gj))

class TestFnGetSubgroup:
	@staticmethod
	def test_get_subgroup(C4, D4):
		H = fingro.fn.get_subgroup(C4, D4)
		assert fingro.same_matrix(H.group, D4)
		assert C4 == H
