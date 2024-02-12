import cv2
import dlib

#image = cv2.imread("people.png")
image = cv2.imread("people standing.jpg")
#cv2.imshow("people",image)

face_detector = dlib.get_frontal_face_detector()
detections = face_detector(image, 1)
#print(detections)

for face in detections:
    l, t, r, b = face.left(),face.top(),face.right(),face.bottom()
    cv2.rectangle(image ,(l,t), (r,b), (0,255,0), 2)
cv2.imshow("people",image)



cv2.waitKey(0)