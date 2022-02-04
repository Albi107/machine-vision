import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
from cvzone.FaceMeshModule import FaceMeshDetector




cap = cv2.VideoCapture(0)
detector_1 = FaceDetector(
    minDetectionCon=0.8)  # level of confidence 1 = 100%, 0.3 might not find the faces but other items
arduino = SerialObject()
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, bboxs = detector_1.findFaces(img)
    img, bboxs = detector.findFaceMesh(img, draw=False)

    if bboxs:
        box = bboxs[0]
        pointLeft = box[145]
        pointRight = box[374]
        #cv2.line(img, pointLeft, pointRight, (255, 0, 0), 3)
        #cv2.circle(img, pointLeft,5, (255,0,0), cv2.FILLED)
        #cv2.circle(img, pointRight, 5, (255, 0, 0), cv2.FILLED)
        w,_ = detector.findDistance(pointLeft, pointRight)
        # finding the focal length
        W = 6.3
        d = 50
        f = (w*d)/W
        #print(f)
        # finding the distance
        f = 840
        d = (W*f)/w
        print(d)
        cv2.putText(img, str(d), (20, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        # arduino.sendData([1])
        arduino.sendData([0, 1])

    else:
        # arduino.sendData([0])
        arduino.sendData([1, 0])

    cv2.imshow("Image", img)
    cv2.waitKey(1)
