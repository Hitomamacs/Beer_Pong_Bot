import cv2
import numpy as np
from Visualizer import Visualizer
class CirlceFinder(Visualizer):
    def __init__(self):
        super().__init__()

    def __get_frame(self, frame_number = 10):
        for i in range(frame_number):
            return self.get_video()


    def circle_identifier(self):
        self.__get_frame()
        gray = self.to_gray_scale(self.frame)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                self.xs.append(x)
                self.ys.append(y)
                cv2.circle(self.frame, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(self.frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

if __name__ == "__main__":
    finder = CirlceFinder()
    finder.circle_identifier()
    cv2.imshow("circles", finder.frame)
    cv2.waitKey(0)