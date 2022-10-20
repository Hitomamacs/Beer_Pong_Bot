import cv2
import numpy as np
from Visual_handler import Visual_handler
class CirlceFinder(Visual_handler):
    def __init__(self):
        super().__init__()
        self.r = 0
        self.r_list = []
        self.xs = []
        self.ys = []
        self.shifted_xs = []
        self.shifted_ys = []

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
                self.r_list.append(r)
                cv2.circle(self.frame, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(self.frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        self.r = sum(self.r_list)/len(self.r_list)

    def get_circles(self):
        return self.xs, self.ys, self.r

    def find_circles(self):
        self.circle_identifier()
        return self.get_circles()

    def shift_x(self, new_zero):
        self.shifted_xs = [x - new_zero for x in self.xs]

    def shift_y(self, new_zero):
        self.shifted_ys = [y - new_zero for y in self.ys]



if __name__ == "__main__":
    finder = CirlceFinder()
    finder.circle_identifier()
    cv2.imshow("circles", finder.frame)
    cv2.waitKey(0)