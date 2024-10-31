import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'Pewdiepie1.jpg'
image = img.imread(path)

height, width = image.shape[:2]

combined = np.zeros_like(image)

for y in range(height):
    for x in range(width):
        combined[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(combined)

plt.show()