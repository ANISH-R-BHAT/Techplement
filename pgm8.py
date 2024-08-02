import cv2
import numpy as np
import matplotlib.pyplot as plt

def translate_image(image,dx,dy):
    rows,cols=image.shape[:2]
    translation_matrix=np.float32([[1,0,dx],[0,1,dy]])
    translated_image=cv2.warpAffine(image,translation_matrix,(cols,rows))
    return translated_image

image=cv2.imread("rnsit.jpeg")
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width=image.shape[:2]
center=(width//2,height//2)

rotation_value=int(input("Enter the rotation value between -180 and 180:"))
while rotation_value<-180 or rotation_value>180:
    rotation_value=int(input("Invalid input!"))
scaling_value=int(input("Enter scaling value between 0.1 and 10:"))
while scaling_value<0.1 or scaling_value>10:
    scaling_value=int(input("Invalid input"))
rotated=cv2.getRotationMatrix2D(center=center,angle=rotation_value,scale=1)
rotated_image=cv2.warpAffine(src=image,M=rotated,dsize=(width,height))

scaled=cv2.getRotationMatrix2D(center=center,angle=0,scale=scaling_value)
scaled_image=cv2.warpAffine(src=rotated_image,M=scaled,dsize=(width,height))

w=int(input("Enter x value translation:"))
h=int(input("Enter y value translation:"))
translated_image=translate_image(scaled_image,w,h)
translated_image_rgb=cv2.cvtColor(translated_image,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(translated_image_rgb)
plt.title("Transformed image")
plt.axis("off")

plt.show()