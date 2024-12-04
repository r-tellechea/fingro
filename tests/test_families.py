import fingro
import pytest

import numpy as np


class TestFamiliesCyclic:
	@staticmethod
	def test_init():
		C8 = fingro.families.Cyclic(8)
		C8.check_matrix_type_and_shape()
		C8.check_group_properties()

	@staticmethod
	def test_manual():
		C8_family = fingro.families.Cyclic(8)
		C8_manual = fingro.Group(
			matrix=np.array([
				[0,1,2,3, 4,5,6,7],
				[1,2,3,4, 5,6,7,0],
				[2,3,4,5, 6,7,0,1],
				[3,4,5,6, 7,0,1,2],
				
				[4,5,6,7, 0,1,2,3],
				[5,6,7,0, 1,2,3,4],
				[6,7,0,1, 2,3,4,5],
				[7,0,1,2, 3,4,5,6],
			]),
			element_names=[str(i) for i in range(8)],
			name='C8_manual',
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)
		assert C8_family == C8_manual

	@staticmethod
	def test_properties():
		assert fingro.families.Cyclic(8).abelian


class TestFamiliesDihedral:
	@staticmethod
	def test_init():
		D4 = fingro.families.Dihedral(4)
		D4.check_matrix_type_and_shape()
		D4.check_group_properties()

	@staticmethod
	def test_manual():
		D4_family = fingro.families.Dihedral(4)
		D4_manual = fingro.Group(
			matrix=np.array([
				[0,1,2,3, 4,5,6,7],
				[1,2,3,0, 7,4,5,6],
				[2,3,0,1, 6,7,4,5],
				[3,0,1,2, 5,6,7,4],

				[4,5,6,7, 0,1,2,3],
				[5,6,7,4, 3,0,1,2],
				[6,7,4,5, 2,3,0,1],
				[7,4,5,6, 1,2,3,0]
			]),
			element_names=[str(i) for i in range(8)],
			name='D4_manual',
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)
		assert D4_family == D4_manual

	@staticmethod
	def test_properties():
		assert fingro.families.Dihedral(2).abelian
		assert not fingro.families.Dihedral(3).abelian
		assert not fingro.families.Dihedral(4).abelian


class TestFamiliesMultiplicative:
	@staticmethod
	def test_init():
		M5 = fingro.families.Multiplicative(5)
		M5.check_matrix_type_and_shape()
		M5.check_group_properties()

	@staticmethod
	def test_manual():
		M5_family = fingro.families.Multiplicative(5)
		M5_manual = fingro.Group(
			matrix=np.array([
				[0,1,2,3],
				[1,3,0,2],
				[2,0,3,1],
				[3,2,1,0],
			]),
			element_names=[str(i) for i in range(4)],
			name='M5_manual',
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)
		assert M5_family == M5_manual

	@staticmethod
	def test_properties():
		assert fingro.families.Multiplicative(5).abelian
		assert fingro.families.Multiplicative(17).abelian
		assert fingro.families.Multiplicative(67).abelian
