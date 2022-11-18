import timeit

start = timeit.default_timer()

import random
import numpy as np

input=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
weight=[random.random(),random.random(),random.random(),random.random()]
bias=random.randint(0,9)

output=np.dot(weight,input)+bias
print(output)

stop = timeit.default_timer()

print('Time: ', stop - start)  