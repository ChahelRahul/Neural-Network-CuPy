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

layer_outputs=[]
weights=[weight0,weight1,weight2]
biases=[bias0,bias1,bias2]
for neuron_weights,neuron_bias in zip(weights,biases):
    neuron_output=0
    for n_input,weight in zip(input,neuron_weights):
        neuron_output+=n_input*weight
    neuron_output+=neuron_bias
    layer_outputs.append(neuron_output)
print(layer_outputs)