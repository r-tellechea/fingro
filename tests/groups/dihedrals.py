import fingro
import pytest

@pytest.fixture
def D1():
	return fingro.families.Dihedral(1)

@pytest.fixture
def D2():
	return fingro.families.Dihedral(2)

@pytest.fixture
def D3():
	return fingro.families.Dihedral(3)

@pytest.fixture
def D4():
	return fingro.families.Dihedral(4)

@pytest.fixture
def D5():
	return fingro.families.Dihedral(5)

@pytest.fixture
def D6():
	return fingro.families.Dihedral(6)

@pytest.fixture
def D7():
	return fingro.families.Dihedral(7)

@pytest.fixture
def D8():
	return fingro.families.Dihedral(8)

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
