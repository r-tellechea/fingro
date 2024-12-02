import fingro
import pytest

import numpy as np
import plotly.graph_objects as go
import graphviz

from tests import group, C2, C3, C4, C8, D2, D4, C2xC2, C3xC3

class TestGroupInit:
	@staticmethod
	def test_check_matrix_shape():
		# TODO test_check_matrix_shape
		pass

	@staticmethod
	def test_check_group_properties_pass():
		fingro.Group(
			matrix=np.array([
				[0,1,2,3],
				[1,2,3,0],
				[2,3,0,1],
				[3,0,1,2],
			]),
			check_group_properties=True
		)

	@staticmethod
	@pytest.mark.xfail(strict=True)
	def test_check_neutral_element_fail():
		fingro.Group(
			matrix=np.array([
				[0,1,2,3],
				[1,2,3,0],
				[3,3,0,1],
				[3,0,1,2],
			]),
			check_group_properties=True
		)

	@staticmethod
	@pytest.mark.xfail(strict=True)
	def test_check_inverse_element_fail():
		fingro.Group(
			matrix=np.array([
				[0,1],
				[1,1],
			]),
			check_group_properties=True
		)

	@staticmethod
	@pytest.mark.xfail(strict=True)
	def test_check_associativity_fail():
		fingro.Group(
			matrix=np.array([
				[0,1,2],
				[1,0,2],
				[2,2,0],
			]),
			check_group_properties=True
		)

class TestGroupProperties:
	@staticmethod
	def test_abelian(C4, D4):
		assert C4.abelian
		assert not D4.abelian

	@staticmethod
	def test_element_orders(C8, D4):
		assert C8.element_orders == (1,8,4,8,2,8,4,8)
		assert D4.element_orders == (1,4,2,4,2,2,2,2)

	@staticmethod
	def test_len(C8, D4):
		assert len(C8) == 8
		assert len(D4) == 8

class TestGroupVisualization:
	@staticmethod
	def test_fig(group):
		assert isinstance(group.fig(), go.Figure)

	@staticmethod
	def test_fig_subgroups(group):
		assert isinstance(group.fig_subgroups(), graphviz.Digraph)

class TestGroupArithmetic:
	@staticmethod
	def test_direct_product(C3, C3xC3):
		assert C3 * C3 == C3xC3

	@staticmethod
	def test_homomorphisms_group(C3):
		assert C3 ^ C3 == C3

	@staticmethod
	def test_quotient_group():
		# TODO: tests_quotient_group
		pass

class TestGroupRelations:
	@staticmethod
	def test_equal(C2, C3, D2, D4, C2xC2):
		assert C2 == C2
		assert C3 == C3
		assert D4 == D4
		assert D2 == C2xC2
	
	@staticmethod
	def test_not_equal(C8, D4):
		assert C8 != D4
		assert not C8 != C8
	
	@staticmethod
	def test_subgroup(C2, C3, C4):
		assert C2 < C4
		assert not C2 < C3
		assert not C3 < C4
