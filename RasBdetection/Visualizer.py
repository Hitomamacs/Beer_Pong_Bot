import cv2
import numpy as np
from abc import ABC, abstractmethod


class Visualizer(ABC):
    Width = 1280
    Height = 1280
    frame1 = np.zeros((Width, Height, 3), dtype = "uint8")

    @staticmethod
    def set_video(new_frame):
        frame1 = new_frame

    def to_gray_scale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    def visualize(self, frame, name):
        cv2.imshow(name, frame)