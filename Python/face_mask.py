import cv2

# Load the pre-trained Haar Cascade face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained Haar Cascade face mask detection model
mask_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

# Load the image
image = cv2.imread('mask.jfif')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# For each face detected, check if it has a mask
for (x, y, w, h) in faces:
    # Extract the region of interest (ROI) for the face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    # Detect masks in the ROI
    masks = mask_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the face and mask
    for (mx, my, mw, mh) in masks:
        cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 255, 0), 2)

# Display the result
cv2.imshow('Face Mask Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()