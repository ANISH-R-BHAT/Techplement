import cv2 
import matplotlib.pyplot as plt 
# Load the pre-trained Haar Cascade classifier for face detection 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 
# Read the input image 
image_path = 'face.jpeg' 
image = cv2.imread(image_path) 
# Convert the image to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Detect faces in the image 
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5) 
# Draw rectangles around detected faces 
for (x, y, w, h) in faces: 
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) 
# Convert BGR image to RGB for displaying with matplotlib 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
# Display the image with detected faces using matplotlib 
plt.imshow(image_rgb) 
plt.title('Detected Faces') 
plt.axis('off')  # Hide axis 
plt.show()