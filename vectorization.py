import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()      # current time
c = np.dot(a,b)
toc = time.time()      # current time

print(c)
print("Vectorized version:" + str(1000*(toc-tic)) +"ms")


c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
print("explicit For Loop:" + str(1000*(toc-tic)) + "ms")

"""When you are implementing deep learning algorithms,
   you can get a result back faster.
   It will be much faster if you vectorize your code

   Whenever possible avoid using explicit for loops.
   both GPU and CPU have parallelization instructions
   SIMD instructions = single-instruction-multiple-data

   If we use built-in functions such as np.dot() or other functions
   that don't require you explicitly implementing a for loop."""

   
