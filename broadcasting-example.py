import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])

total_cal = A.sum(axis = 0)
percentages = 100*A/total_cal.reshape(1,4)
# reshape is redundant, but this command is constant time
# order one operation: it is very cheap to call it

print(percentages)

"""Broadcasting, we take a matrix A which is (3*4) matrix
    and divide it by a (1*4) matrix

    Python expanded this (1*4) matrix and made (3*4) matrix
    by copying it 3 times vertically"""
