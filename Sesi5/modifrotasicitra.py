import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateimage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    height, width = image.shape[:2]
    new_height = int(abs(height * cos_deg) + abs(width * sin_deg))
    new_width = int(abs(height * sin_deg) + abs(width * cos_deg))
    outputimage = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    centerY, centerX = new_height // 2, new_width // 2

    for y in range(height):
        for x in range(width):
            newX = int(cos_deg * x - sin_deg * y) + centerX
            newY = int(sin_deg * x + cos_deg * y) + centerY
            
            if 0 <= newX < new_width and 0 <= newY < new_height:
                outputimage[newY, newX] = image[y, x]

    return outputimage

image = img.imread('pewdiepie1.jpg')

rotated_image = rotateimage(image, 45)

plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)

plt.show()