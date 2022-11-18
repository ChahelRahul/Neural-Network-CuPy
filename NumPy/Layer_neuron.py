import random

input=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
weight0=[random.random(),random.random(),random.random(),random.random()]
weight1=[random.random(),random.random(),random.random(),random.random()]
weight2=[random.random(),random.random(),random.random(),random.random()]

bias0=random.randint(0,9)
bias1=random.randint(0,9)
bias2=random.randint(0,9)

output=[#Neuron 0:
        input[0]*weight0[0]+input[1]*weight0[1]+input[2]*weight0[2]+input[3]*weight0[3]+bias0,
        #Neuron 1:
        input[0]*weight1[0]+input[1]*weight1[1]+input[2]*weight1[2]+input[3]*weight1[3]+bias1,
        #Neuron 2:
        input[0]*weight2[0]+input[1]*weight2[1]+input[2]*weight2[2]+input[3]*weight2[3]+bias2]

print(output)
