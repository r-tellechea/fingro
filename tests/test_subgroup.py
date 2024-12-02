import fingro
import pytest

from tests import D4, C4

@pytest.fixture
def sub_C4_D4(D4):
	return fingro.Subgroup(
		group=D4,
		sub_index=(0, 1, 2, 3),
		name='sub_C4_D4',
	)

@pytest.fixture
def sub_C2_D4(D4):
	return fingro.Subgroup(
		group=D4,
		sub_index=(0, 2),
		name='sub_C2_D4',
	)

@pytest.fixture
def sub_C1_D4(D4):
	return fingro.Subgroup(
		group=D4,
		sub_index=(0,),
		name='sub_C1_D4',
	)

@pytest.fixture
def sub_C2_D4_tau(D4):
	return fingro.Subgroup(
		group=D4,
		sub_index=(0, 4),
		name='sub_C2_D4_tau',
	)


class TestSubgroupInit:
	@staticmethod
	def test_subgroup_init_pass(D4):
		fingro.Subgroup(
			group=D4,
			sub_index=(0, 2),
		)

	@staticmethod
	@pytest.mark.xfail(strict=True)
	def test_subgroup_init_fail(D4):
		fingro.Subgroup(
			group=D4,
			sub_index=(0, 1),
		)


class TestSubgroupProperties:
	@staticmethod
	def test_normal(sub_C4_D4, sub_C2_D4, sub_C2_D4_tau):
		assert sub_C2_D4.normal
		assert sub_C4_D4.normal
		assert not sub_C2_D4_tau.normal

	@staticmethod
	def test_inclusion(sub_C4_D4, C4):
		inclusion = sub_C4_D4.inclusion
		assert isinstance(inclusion, fingro.Homomorphism)
		assert inclusion.inj
		assert inclusion.im == C4


class TestSubgroupArithmetic:
	# TODO: Subgroup Test Arithmetic
	pass


class TestSubgroupRelations:
	# TODO: Subgroup Test Relations
	pass
