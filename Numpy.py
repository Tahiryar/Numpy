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
