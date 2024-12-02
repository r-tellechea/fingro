import pytest
from tests.groups.dihedrals import D4

@pytest.fixture
def group(D4):
	return D4
