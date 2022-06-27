import numpy as np
from NeuralNetwork import NeuralNetwork

#Simple Neural Net Project

#going to use sigmoid activation function with 2 layers
#0 to 1; >.5 -> 1; >.5 -> 0
#input----\
#          ---> (Layer 1) -> dot_product -> dot_product_result ------> sum -> layer_1_result -> layer 2 -> sigmoid -> prediction 
#weights--/                                                    bias-/

input_vector = np.array([2, 1.5])

learning_rate = 0.1

neural_network = NeuralNetwork(learning_rate)

print(neural_network.predict(input_vector))