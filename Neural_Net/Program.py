import numpy as np

#checking out numpy functions
#grading check

# CURVE_CENTER = 80
# grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])
# def curve(grades):
#     average = grades.mean()
#     change = CURVE_CENTER - average
#     new_grades = grades + change
#     return print(np.clip(new_grades, grades, 100))

# curve(grades)

#messing with input vectors with vanilla python to understand
#dot product

input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

# #Computing dot product of input_vector and weights_1
# first_indexes_mult = input_vector[0] * weights_1[0]
# second_indexes_mult = input_vector[1] * weights_1[1]
# dot_product_1 = first_indexes_mult + second_indexes_mult

# print(f"The dot product is: {dot_product_1}")

#now using NumPy

dot_product_1 = np.dot(input_vector, weights_1)

print(f"The dot product is: {dot_product_1}")

#going to use sigmoid activation function with 2 layers
#0 to 1; >.5 -> 1; >.5 -> 0
#input----\
#          ---> (Layer 1) -> dot_product -> dot_product_result ------> sum -> layer_1_result -> layer 2 -> sigmoid -> prediction 
#weights--/                                                    bias-/
