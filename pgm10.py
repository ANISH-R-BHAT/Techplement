import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("rnsit.jpeg",cv2.IMREAD_GRAYSCALE)

gaussian_blur=cv2.GaussianBlur(image,(5,5),0)

bilateral_blur=cv2.bilateralFilter(image,9,75,75)

plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.imshow(image,cmap="gray")
plt.title("Original image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(gaussian_blur,cmap="gray")
plt.title("Gaussian blur")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(bilateral_blur,cmap="gray")
plt.title("Bilateral blur")
plt.axis("off")

plt.show()