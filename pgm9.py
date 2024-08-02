import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("rnsitlogo.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,100,200)

kernel=np.ones((5,5),np.float32)/25
texture=cv2.filter2D(gray,-1,kernel)

plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title("Original image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(edges,cmap='gray')
plt.title("Edges")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(texture,cmap='gray')
plt.title("Filtered image")
plt.axis("off")

plt.show()