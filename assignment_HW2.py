'''
PGE310 Fall 2021 Homework 2

Welcome to your first assignment in Python! 

This homework is split up into two problems: 

    In Problem 1, you will practice coding scalar, vector, and matrix 
    operations by translating Homework 1 into Python. 
    
    Next, Problem 2 will help you pracitce some graphing and visualization
    using Matplotlib. 

Please see the attached PDF for more detailed instructions.

Please submit this assignment as a Python file (.py) on Github classroom. 
For more comprehensive instructions on how to test and submit your code, 
refer to the posted instructions document on Canvas.

And as always, feel free to contact Dr. P, Alex, Bernie, or Ziming with 
problems, questions, or comments. 

Learning to code can be difficult (and rewarding!), and we're here to help 
you overcome the learning curve!

'''


# Import needed packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

#%%
'''
Problem 1: Scalar, Vector, and Matrix Operations

In the following problem, you will translate Homework 1 into Python. 

Begin by filling in the following scalars, vectors, and matrices from Homework 1.
'''

# alpha
a = 

# beta
b =

# u, v, w, are 1-D NumPy arrays
u =
v = 
w = 

# x, A, B are 2D NumPy arrays
x = 
A = 
B =


#%% Problem 1a
def problem_1a(w, u):
    # type in the expression after the 'result =' in the next line
    result = 
    return result 

answer_1a = problem_1a(w, u)
print('='*50)
print('Problem 1a')
print("Answer 1a = ", answer_1a)

#%% Problem 1b
def problem_1b(v, w):
    # type in the expression after the 'result =' in the next line
    result = 
    return result

answer_1b = problem_1b(v, w)
print('-'*50)
print('Problem 1b')
print("Answer 1b = ", answer_1b)

#%% Problem 1c
def problem_1c(v, w):
    # type in the expression after the 'result =' in the next line
    result_in_radians = 
    result_in_degree = 

    return result_in_radians, result_in_degree

answer_1c = problem_1c(v,w)
print('-'*50)
print('Problem 1c')
print('Answer 1c (radians) =', answer_1c[0])
print('Answer 1d (degrees) =', answer_1c[1])

#%% Problem 1d
def problem_1d(u, v, w, a, b):
    u = u.reshape((1,4))
    v = v.reshape((1,4))
    w = w.reshape((1,4))
    
    # type in the expression after the 'result =' in the next line
    result = 
    return result

answer_1d = problem_1d(u, v, w, a, b)
print('-'*50)
print('Problem 1d')
print('Answer 1d = \n', answer_1d)

#%% Problem 1e
def problem_1e(A, B, x):
    # type in the expression after the 'result =' in the next line
    result = 
    return result

answer_1e = problem_1e(A, B, x)
print('-'*50)
print('Problem 1e')
print('Answer 1e = ', answer_1e)

#%% Problem 1f
def problem_1f(A, b, x):
    # type in the expression after the 'result =' in the next line
    result = 
    return result 

answer_1f = problem_1f(A, b, x)
print('-'*50)
print('Problem 1f')
print('Answer 1f = ', answer_1f)

#%% Problem 1g
def problem_1g(A, B):
    # type in the expression after the 'result =' in the next line
    result_AB = 
    result_BA = 
    return result_AB, result_BA

AB, BA = problem_1g(A, B)
print('-'*50)
print('Problem 1g')
print('AB = \n', AB)
print('BA = \n', BA)

#%% Problem 1h
def problem_1h(A, B):
    # type in the expression after the 'result =' in the next line
    result_LHS = 
    result_RHS = 
    return result_LHS, result_RHS

LHS, RHS = problem_1h(A, B)
print('-'*50)
print('Problem 1h')
print('LHS = \n', LHS)
print('RHS = \n', RHS)


#%% Problem 1i
def problem_1i(A):
    # type in the expression after the 'result =' in the next line
    result = 
    return result 

answer_1i = problem_1i(A)
print('-'*50)
print('Problem 1i')
print('Answer 1i = \n', answer_1i)
print('='*50)


#%%
'''
Problem 2: Matplotlib Plotting


The goal of this problem is to practice plotting with Matplotlib. 
In order to do so, you will create a 2D plot of a chaotic solution to the Lorenz System. 
In the cell below, we have set up, solved, and saved the solution data of the Lorenz System for you. 
You do not need to worry about the details of how we solved it (but we will learn about numerical integration later in the semester!).


Please follow these instructions:

0. Run the cell below without modifying it
1. In the next cell, plot z versus x with a line color of your choice
2. Add a title to the plot
3. Add x and y axis labels
4. Set the range of the x-axis to [-25, 25]
5. Set the range of the y-axis to [0, 50]
6. Show the grid lines

'''

# Do not modify the code below!
def lorenz(X, t, sigma, beta, rho):
        x, y, z = X
        dxdt = sigma*(y-x)
        dydt = x*(rho - z) - y
        dzdt = x*y - beta*z
        return dxdt, dydt, dzdt

sigma = 10
beta = 8/3
rho = 28
t = np.linspace(0,50,10000)        
solution = scipy.integrate.odeint(lorenz, [0, 1, 0], t, args=(sigma, beta, rho))
x = solution[:,0]
y = solution[:,1]
z = solution[:,2]

#%% Make your plot below this line!
plt.plot()
plt.xlabel()
plt.ylabel()
plt.title()
plt.xlim()
plt.ylim()

plt.show()




