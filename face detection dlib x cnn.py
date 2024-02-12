import cv2
import dlib

image = cv2.imread("people1.png")
#cv2.imshow("people",image)

cnn_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
detections = cnn_detector(image, 1)
#print(detections)

for face in detections:
    l, t, r, b, c = face.rect.left(),face.rect.top(),face.rect.right(),face.rect.bottom(), face.confidence
    #print(c)
    cv2.rectangle(image ,(l,t), (r,b), (255,255,0), 2)
cv2.imshow("people",image)

cv2.waitKey(0)