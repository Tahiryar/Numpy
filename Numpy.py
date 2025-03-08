import numpy as np
from PIL import Image

arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)


matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)

# Image Load Karna NumPy se

# Image ko Load Karna
img = Image.open("image.jpg")
img_array = np.array(img)

print("Image Shape:", img_array.shape)  # Height x Width x Channels


# Input Features (5 Features)
X = np.random.rand(10, 5)  # 10 Samples, 5 Features Each

# Weights aur Bias
W = np.random.rand(5, 3)  # 5 Inputs se 3 Neurons ko connect kar raha hai
B = np.random.rand(3)

# Neural Network ka Forward Pass
output = np.dot(X, W) + B

print("Neural Network Output:\n", output)
