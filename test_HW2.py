import unittest
import numpy as np
import os
import importlib

repo_files = os.listdir('.')
solution_file = [f for f in repo_files if '.py' in f and 'test' not in f][0]
solution_file = solution_file.split('.')[0]

sol_module = importlib.import_module(solution_file, package=None)

a = 9
b = -8
u = np.array([2, 4, -2, 5])
v = np.array([-2, 9, -5, 4])
w = np.array([6, -1, 2, 2])
x = np.array([[3], [5], [6]])
A = np.array([[2, -1, 7], [3, -6, 4], [0, 3, -1]])
B = np.array([[3, 2, -3], [6, 7, 2], [-4, 2, 1]])


class TestSolution(unittest.TestCase):
    
    def test_prob1_a(self):
        np.testing.assert_equal(sol_module.problem_1a(w, u), 14.)

    def test_prob1_b(self):
        np.testing.assert_equal(sol_module.problem_1b(v, w), -23)

    def test_prob1_c(self):
        np.testing.assert_array_almost_equal(sol_module.problem_1c(v, w), [1.881204482365583, 107.7850772406406])

    def test_prob1_d(self):
        np.testing.assert_array_almost_equal(sol_module.problem_1d(u, v, w, a, b),
											 [[-460.],[ 198.],[-214.],[ -88.]])
    def test_prob1_e(self):
        np.testing.assert_array_almost_equal(sol_module.problem_1e(A, B, x),
											 [[111],[ 125. ],[-114]])

    def test_prob1_f(self):
        np.testing.assert_array_almost_equal(sol_module.problem_1f(A, b, x),
											 [[-1584]])

    def test_prob1_g(self):
        np.testing.assert_array_almost_equal(sol_module.problem_1g(A, B)[0],
											 [[-28,  11,  -1], [-43, -28, -17], [ 22,  19,   5]])
        np.testing.assert_array_almost_equal(sol_module.problem_1g(A, B)[1],
											 [[ 12, -24,  32], [ 33, -42,  68], [ -2,  -5, -21]])

    def test_prob1_h(self):
        np.testing.assert_array_almost_equal(sol_module.problem_1h(A, B)[0],
											 [[18, 26, 26], [30, 40, 42], [25,  1, 14]])
        np.testing.assert_array_almost_equal(sol_module.problem_1h(A, B)[1],
											 [[18, 26, 26], [30, 40, 42], [25,  1, 14]])

    def test_prob1_i(self):
        np.testing.assert_array_almost_equal(sol_module.problem_1i(A), 
                                             [[2., -1.,  7.], [ 3., -6.,  4.], [ 0.,  3., -1.]])


if __name__ == '__main__':
	unittest.main()