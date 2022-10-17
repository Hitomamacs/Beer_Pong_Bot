import cv2
import numpy as np
from abc import ABC, abstractmethod


class Visualizer(ABC):
    def __init__(self):
        self.memory_frame = np.zeros((720, 1280, 3), dtype = "uint8")
        self.cam = cv2.VideoCapture(0)
        self.xs = []
        self.ys = []
        cv2.namedWindow('mouseRGB')
        cv2.setMouseCallback('mouseRGB', self.onMouse)

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.posList.append((x, y))


    def get_video(self):
        ret, self.frame = self.cam.read()





    def to_gray_scale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    def visualize(self, frame, name):
        cv2.imshow(name, frame)
        cv2.waitKey(0)