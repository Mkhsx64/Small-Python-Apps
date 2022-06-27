import numpy as np
from NeuralNetwork import NeuralNetwork

#Simple Neural Net Project

input_vector = np.array([2, 1.5])

learning_rate = 0.1

neural_network = NeuralNetwork(learning_rate)

print(neural_network.predict(input_vector))