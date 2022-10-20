import cv2
import numpy as np

class Overlay():
    def __init__(self):
        self.overlay = np.zeros((1280,720,3), dtype="uint8")

    def plot_overlay(self, xs: list, ys: list, r:int):
        for x, y in xs, ys:
            cv2.circle(self.overlay, (x, y), r, color=(0, 0, 255), thickness=-1)
