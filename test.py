import unittest
import nbconvert
import numpy as np

with open("assignment_sol_HW2.ipynb") as f:
	exporter = nbconvert.PythonExporter()
	python_file, _ = exporter.from_file(f)

with open("assignment.py", "w") as f:
	f.write(python_file)

from assignment import *

class TestSolution(unittest.TestCase):
	def __init__(self):
		self.a = 9
		self.b = -8
		self.u = np.array([2, 4, -2, 5])
		self.v = np.array([-2, 9, -5, 4])
		self.w = np.array([6, -1, 2, 2])
		self.x = np.array([[3], [5], [6]])
		self.A = np.array([[2, -1, 7], [3, -6, 4], [0, 3, -1]])
		self.B = np.array([[3, 2, -3], [6, 7, 2], [-4, 2, 1]])

	def test_prob1_a(self):
		np.testing.assert_equal(problem_1a(self.w, self.u), 14.)

	def test_prob1_b(self):
		np.testing.assert_equal(problem_1b(self.v, self.w), -23)

	def test_prob1_c(self):
		np.testing.assert_array_almost_equal(problem_1c(self.v, self.w), [1.881204482365583, 107.7850772406406])

	def test_prob1_d(self):
		np.testing.assert_array_almost_equal(problem_1d(self.u, self.v, self.w, self.a, self.b),
											 [[-460.],[ 198.],[-214.],[ -88.]])
	def test_prob1_e(self):
		np.testing.assert_array_almost_equal(problem_1e(self.A, self.B, self.x),
											 [[111],[ 125. ],[-114]])

	def test_prob1_f(self):
		np.testing.assert_array_almost_equal(problem_1f(self.A, self.b, self.x),
											 [[-1584]])

	def test_prob1_g(self):
		np.testing.assert_array_almost_equal(problem_1g(self.A, self.B)[0],
											 [[-28,  11,  -1], [-43, -28, -17], [ 22,  19,   5]])
		np.testing.assert_array_almost_equal(problem_1g(self.A, self.B)[1],
											 [[ 12, -24,  32], [ 33, -42,  68], [ -2,  -5, -21]])

	def test_prob1_h(self):
		np.testing.assert_array_almost_equal(problem_1h(self.A, self.B)[0],
											 [[18, 26, 26], [30, 40, 42], [25,  1, 14]])
		np.testing.assert_array_almost_equal(problem_1h(self.A, self.B)[1],
											 [[18, 26, 26], [30, 40, 42], [25,  1, 14]])

	def test_prob1_i(self):
		np.testing.assert_array_almost_equal(problem_1i(self.A), [[2., -1.,  7.], [ 3., -6.,  4.], [ 0.,  3., -1.]])


if __name__ == '__main__':
	unittest.main()