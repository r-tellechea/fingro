import fingro
import pytest

@pytest.fixture
def C1():
	return fingro.families.Cyclic(1)

@pytest.fixture
def C2():
	return fingro.families.Cyclic(2)

@pytest.fixture
def C3():
	return fingro.families.Cyclic(3)

@pytest.fixture
def C4():
	return fingro.families.Cyclic(4)

@pytest.fixture
def C5():
	return fingro.families.Cyclic(5)

@pytest.fixture
def C6():
	return fingro.families.Cyclic(6)

@pytest.fixture
def C7():
	return fingro.families.Cyclic(7)

@pytest.fixture
def C8():
	return fingro.families.Cyclic(8)
