import timeit

start = timeit.default_timer()
import cupy as cp
import random
import numpy as np
inputs=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
weights=[[random.random(),random.random(),random.random(),random.random()],
         [random.random(),random.random(),random.random(),random.random()],
         [random.random(),random.random(),random.random(),random.random()]]

biases=[random.randint(0,9),random.randint(0,9),random.randint(0,9)]
inputs=np.array(inputs)
weights=np.array(weights)
biases=np.array(biases)
layer_outputs=cp.dot(weights,inputs,out=None)+biases
print(layer_outputs)



stop = timeit.default_timer()

print('Time: ', stop - start)  