import cv2
import numpy as np
import  matplotlib.pyplot as plt


posList = []
def onMouse(event, x, y, flags, param):
    global posList
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
        
cv2.namedWindow('mouseRGB')        
cv2.setMouseCallback('mouseRGB', onMouse)
posNp = np.array(posList)
        
capture = cv2.VideoCapture(0)
if capture.read() == False:
    capture.open()
checkk = True
while True:
    rendered = np.zeros((1280, 1280, 3), dtype = "uint8")
    check, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            cv2.circle(rendered, (x,y), r, color = (0,0,255), thickness= -1)
    
    
    if (len(posList) == 4) and (checkk == True) :
        for pos in posList:
            frame = cv2.circle(frame, pos, radius=10, color=(0, 0, 255), thickness=-1)
        pts1 = np.float32([[posList[0][0],posList[0][1]], [posList[1][0], posList[1][1]], [posList[2][0], posList[2][1]], [posList[3][0], posList[3][1]]])
        pts2 = np.float32([[0,0],[1280,0], [0, 1280], [1280,1280]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        image = cv2.warpPerspective(frame, matrix, (1280,1280))
        rendered = cv2.warpPerspective(rendered, matrix, (1280,1280))          
        output = image.copy()
        cv2.imshow("persp", image) 
        cv2.imshow("rendered", rendered)          
     
       
    cv2.imshow('mouseRGB', frame)
    key = cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()
