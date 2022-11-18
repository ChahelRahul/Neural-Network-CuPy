import timeit

start = timeit.default_timer()

import random
import cupy as cp
import numpy as np
input=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
weight=[random.random(),random.random(),random.random(),random.random()]
bias=random.randint(0,9)
input=np.array(input)
weight=np.array(weight)
output=cp.dot(weight,input,out=None)+bias
print(output)

stop = timeit.default_timer()

print('Time: ', stop - start)  