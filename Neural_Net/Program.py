import numpy as np

#Simple Neural Net Project

#going to use sigmoid activation function with 2 layers
#0 to 1; >.5 -> 1; >.5 -> 0
#input----\
#          ---> (Layer 1) -> dot_product -> dot_product_result ------> sum -> layer_1_result -> layer 2 -> sigmoid -> prediction 
#weights--/                                                    bias-/

input_vector = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2

prediction = make_prediction(input_vector, weights_1, bias)

print(f"The prediction result is: {prediction}")