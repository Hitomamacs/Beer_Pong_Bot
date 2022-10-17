#TODO two scripts one publish visualization another one publish useful data
import cv2
import numpy as np
from Visualizer import Visualizer
class BirdEyer2(Visualizer):

    def __init__(self):
        super().__init__()
        self.posList = []
        self.video_stream = True
        self. frame = np.zeros((720, 1280, 3), dtype = "uint8")
        self.matrix = np.zeros((3,3), dtype= "uint8")
        self.top_down_frame = np.zeros((720, 1280, 3), dtype = "uint8")

    def get_calibration_point(self):
        while (len(self.posList) < 4):
            frame = self.get_video()
            cv2.imshow("mouseRGB", self.frame)
            cv2.waitKey(0)
        if len(self.posList) == 4:
            for pos in self.posList:
                frame = cv2.circle(self.frame, pos, radius=10, color=(0, 0, 255), thickness=-1)
                cv2.imshow("mouseRGB", self.frame)


    def transform(self):
        pts1 = np.float32(
            [[self.posList[0][0], self.posList[0][1]], [self.posList[1][0], self.posList[1][1]], [self.posList[2][0], self.posList[2][1]],
             [self.posList[3][0], self.posList[3][1]]])
        pts2 = np.float32([[0, 0], [720, 0], [0, 1280], [720, 1280]])
        self.matrix = cv2.getPerspectiveTransform(pts1, pts2)
        self.top_down_frame = cv2.warpPerspective(self.frame, self.matrix, (720, 1280))
        return self.top_down_frame




if __name__ == "__main__":
    top_down = BirdEyer2()
    top_down.get_calibration_point()
    a = top_down.transform()
    cv2.imshow("test", a)
    cv2.waitKey(0)



