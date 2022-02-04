import numpy as np
import cv2
from PIL import ImageGrab
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.SerialModule import SerialObject
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

detector_1 = FaceDetector(minDetectionCon=0.75)  # level of confidence 1 = 100%, 0.3 might not find the faces but other items
arduino = SerialObject()
detector = FaceMeshDetector()#maxFaces=1)
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
# vid = cv2.VideoWriter('record.avi', fourcc, 8, (500,490))
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        img = ImageGrab.grab(bbox=(50, 10, 700, 700))  # x, y, w, h (50, 10, 700, 700)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        frame, bboxs = detector_1.findFaces(frame)
        frame, bboxs = detector.findFaceMesh(frame)
        results = pose.process(frame)
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        if bboxs:
            # arduino.sendData([1])
            arduino.sendData([0, 1])
            #cv2.putText(frame, "Human face", (20, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        else:
            # arduino.sendData([0])
            arduino.sendData([1, 0])

        # vid.write(img_np)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

vid.release()
cv2.destroyAllWindows()
