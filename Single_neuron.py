import random

input=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]

weight=[random.random(),random.random(),random.random(),random.random()]

bias=random.randint(0,9)

output=(input[0]*weight[0]+input[1]*weight[1]+input[2]*weight[2]+input[3]*weight[3]+bias)

print(output)