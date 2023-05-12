from numpy import *

C = array([[1, 3, 6, 8, 5, 4],
           [9, 23, 7, 16, 40, 2]])

R = C.reshape(2, 2, 3)
print(R)

D = matrix('1, 2; 3, 4; 6, 5')
print(D)

A = linspace(5, 15, 20)
print(A.max())

B = ([[2, 4, 3],
      [7, 1, 5]])
X = matrix('1, 2, 9; 3, 4, 7')
print
y = X.reshape(2, 3)
E = multiply(B, X)
print(E)
