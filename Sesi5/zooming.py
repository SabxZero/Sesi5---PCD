import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomPLus(image,factor) :
    height, width = image.shape[:2]
    new_height = int(height/factor)
    new_width = int(width/factor)
    imgzoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_Y = int(y * factor)
            ori_X = int(x * factor)

            ori_Y = min(ori_Y, height - 1)
            ori_X = min(ori_X, width - 1)

            imgzoom[y,x] = image[ori_Y,ori_X]

    return imgzoom

image = img.imread('Pewdiepie1.jpg')
skala = 2.0

imgzoom = zoomPLus(image,skala)
img.imwrite('Pewdiepie1.jpg',imgzoom)
plt.subplot(1,2,1)
plt.imshow(image)

plt.subplot(1,2,2)
plt.imshow(imgzoom)
plt.show()
image = img.imwrite("zooming.jpeg", imgzoom)