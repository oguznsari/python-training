import numpy as np

A = np.random.randn(5) # 5 random Gaussian variables stored in array A
print(A)
print(A.shape)

print(A.T)              # A transpoze
print(np.dot(A, A.T))

# Above A doesn't behave consistently neither a row vector nor a column vector,
# Which makes some of its effects nonintuitive

# So instead of using array; you commit to making it either a column or a row vector.
# A = np.random.randn(5,1) --> column vector
# A = np.random.randn(1,5) --> row vector

B = np.random.rand(5,1)
print(B)
print(B.shape)

print(B.T)
print(np.dot(B, B.T))       # generates 5*5 matrix

# If not entirely sure with dimensions of your vector
# use assertion statement;    which is inexpensive to execute and also helps documentation
if A.shape != (5,1):
    print("Be careful A is not a column vector!")

# If some for some reason you ended up with "rank 1 array", you can reshape it
A = A.reshape((5,1))        # column vector
print(A)

# eleminate "rank 1 arrays"
# simplify your codes
