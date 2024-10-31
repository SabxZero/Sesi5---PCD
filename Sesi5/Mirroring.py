import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'Pewdiepie1.jpg'
image = img.imread(path)

height, width = image.shape[:2]
horizontal = np.zeros_like(image)
vertikal = np.zeros_like(image)

for y in range(height):
    for x in range(width) :
        horizontal[y,x] = image[y, width - 1 - x]

for y in range(height):
    for x in range(width):
        vertikal[y,x] = image[height - 1-y,x]

plt.figure(figsize=(10,5))

plt.subplot (1,3,1)
plt.imshow(image)

plt.subplot(1,3,2)
plt.imshow(horizontal)

plt.subplot(1,3,3)
plt.imshow(vertikal)

plt.show()
image = img.imwrite("Mirroring(horizontal).jpeg", horizontal)
image1 = img.imwrite("Mirroring(vertikal).jpeg", vertikal)