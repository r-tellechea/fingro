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
