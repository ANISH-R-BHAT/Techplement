import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# Read the image 
image = cv2.imread('shapes.jpg') 
# Convert the image to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Apply Gaussian blur to reduce noise 
blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
= 
# Apply adaptive thresholding with adjusted parameters 
thresh 
cv2.adaptiveThreshold(blurred, 
cv2.THRESH_BINARY_INV, 15, 4) 
255, 
cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
# Find the contours 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
# Draw the contours on the original image 
cv2.drawContours(image, contours, -1, (0, 255, 0), 2) 
# Convert BGR image to RGB for displaying with matplotlib 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
# Display the image with contours using matplotlib 
plt.imshow(image_rgb) 
plt.title('Contours') 
plt.axis('off')  # Hide axis 
plt.show()