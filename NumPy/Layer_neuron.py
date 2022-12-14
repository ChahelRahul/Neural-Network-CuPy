import timeit

start = timeit.default_timer()
import numpy as np
import random

inputs=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
weights=[[random.random(),random.random(),random.random(),random.random()],
         [random.random(),random.random(),random.random(),random.random()],
         [random.random(),random.random(),random.random(),random.random()]]

biases=[random.randint(0,9),random.randint(0,9),random.randint(0,9)]

layer_outputs=np.dot(weights,inputs)+biases
print(layer_outputs)



stop = timeit.default_timer()

print('Time: ', stop - start)  