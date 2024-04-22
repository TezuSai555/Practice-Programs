import cv2
import tensorflow
from mtcnn.mtcnn import MTCNN
def detect_mask(face):
    return True 
image1 = cv2.imread('m1.jpg')
detector = MTCNN()
faces = detector.detect_faces(image1)
for face in faces:
    x, y, w, h = face['box']
    cv2.rectangle(image1, (x, y), (x + w, y + h), (255, 0, 0), 2)
    if detect_mask(face):
        label = "Mask"
        color = (0, 255, 0)
    else:
        label = "No Mask"
        color = (0, 0, 255)
    cv2.putText(image1, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
cv2.imshow('Mask Detection', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
