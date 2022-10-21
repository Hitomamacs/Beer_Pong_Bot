import cv2
import numpy as np
from abc import ABC, abstractmethod


class Visual_handler(ABC):
    def __init__(self):
        self.memory_frame = np.zeros((1280, 720, 3), dtype = "uint8")
        self.cam = cv2.VideoCapture(0)
        self.xs = []
        self.ys = []
        self.posList = []
        cv2.namedWindow('mouseRGB')
        cv2.setMouseCallback('mouseRGB', self.onMouse)

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.posList.append((x, y))


    def get_video(self):
        ret, self.frame = self.cam.read()


    def set_video(self, frame):
        self.memory_frame = frame

   

    def get_xs(self):
        return self.xs

    def get_ys(self):
        return self.ys


    def set_xs(self, xs):
        self.xs = xs

    def set_ys(self, ys):
        self.ys = ys




    def to_gray_scale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    def visualize(self, frame, name):
        cv2.imshow(name, frame)
        cv2.waitKey(0)