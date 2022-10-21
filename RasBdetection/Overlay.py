import cv2
import numpy as np

class Overlay():
    def __init__(self):
        self.overlay = np.zeros((720,1280,3), dtype="uint8")



    def draw_line_from_angle(self, x: int, y: int, angle: int, length: int):
        rad = np.deg2rad(angle)
        x2 = x + length * np.cos(rad)
        y2 = y + length * np.sin(rad)
        x2 = np.round(x2).astype(int)
        y2 = np.round(y2).astype(int)
        cv2.line(self.overlay, (x, y), (x2, y2), (0, 0, 255), 2)

    def show_overlay(self):
        cv2.imshow("overlay", self.overlay)
        cv2.waitKey(0)

    def plot_overlay(self, xs: list, ys: list, r:int):
        for x, y in xs, ys:
            cv2.circle(self.overlay, (x, y), r, color=(0, 0, 255), thickness=-1)

    def draw_circles(self, xs: list, ys: list, r: int):
        for x, y in xs, ys:
            cv2.circle(self.overlay, (x, y), r, color=(0, 0, 255), thickness=-1)







if __name__ == "__main__":
    overlay = Overlay()

    overlay.draw_line_from_angle(640, 720, -135, 300)
    cv2.imshow("test", overlay.overlay)
    cv2.waitKey(0)

