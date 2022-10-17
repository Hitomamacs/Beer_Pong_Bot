import cv2
import numpy as np
from Visualizer import Visualizer

class BirdEyer(Visualizer):

    def __init__(self, Height, Width):
        capture = cv2.VideoCapture(0)
        self.height = Height
        self.width = Width
        posList = []
        self.video_stream = True
        ##cv2.namedWindow('ClibrationWindow')



    def onMouse(self, event, x, y, flags, param):
        global posList
        if event == cv2.EVENT_LBUTTONDOWN:
            posList.append((x, y))

    def __getCslibration_Point(self):
        pass

    def get_video(self, capture):
        cv2.namedWindow('mouseRGB')
        cv2.setMouseCallback('mouseRGB', self.onMouse)
        if  capture.read() == False:
           capture.open()
        while self.video_stream:
            check, frame = capture.read()
            cv2.imshow("mouseRGB", frame)
            Visualizer.set_video(frame)



if __name__ == "__main__":
    top_down = BirdEyer(1280,1280)
    cap = cv2.VideoCapture(0)
    top_down.get_video(cap)
