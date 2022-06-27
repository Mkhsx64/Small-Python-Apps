import numpy as np
from NeuralNetwork import NeuralNetwork

#Simple Neural Net Project

#going to use sigmoid activation function with 2 layers
#0 to 1; >.5 -> 1; >.5 -> 0
#input----\
#          ---> (Layer 1) -> dot_product -> dot_product_result ------> sum -> layer_1_result -> layer 2 -> sigmoid -> prediction 
#weights--/                                                    bias-/

input_vector = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])



def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2

prediction = make_prediction(input_vector, weights_1, bias)

print(f"The prediction result is: {prediction}")

#Using a cost function to measure the error; MSE (mean squared error)
target = 0
#Compute difference between the prediction and the target; multiply the result by itself
mse = np.square(prediction - target)

print(f"Prediction: {prediction}; Error: {mse}")

#To know which direction to reduce the error, going to use derivative
derivative = 2 * (prediction - target)

print(f"The derivative is {derivative}")

#updating the weights
weights_1 = weights_1 - derivative

prediction = make_prediction(input_vector, weights_1, bias)

error = (prediction - target) ** 2

print(f"Prediction: {prediction}; Error: {error}")

#Applying the chain rule and using backpropagation



derror_dprediction = 2 * (prediction - target)
layer_1 = np.dot(input_vector, weights_1) + bias
dprediction_dlayer1 = sigmoid_deriv(layer_1)
dlayer1_dbias = 1

derror_dbias = (
    derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
)

