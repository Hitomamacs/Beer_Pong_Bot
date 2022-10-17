import cv2
import numpy as np
from Visualizer import Visualizer
class BirdEyer2(Visualizer):

    def __init__(self, Width, Height):
        self.height = Height
        self.width = Width
        self.posList = []
        self.video_stream = True
        self. frame = np.zeros((Width, Height, 3), dtype = "uint8")

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.posList.append((x, y))


    def _get_calibration_point(self, frame):
        if len(self.posList) == 4:
            for pos in self.posList:
                frame = cv2.circle(frame, pos, radius=10, color=(0, 0, 255), thickness=-1)


    def get_video(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow('mouseRGB')
        cv2.setMouseCallback('mouseRGB', self.onMouse)
        while self.video_stream:
            ret, frame = cam.read()
            self._get_calibration_point(frame)
            self.visualize(frame, "mouseRGB")
            Visualizer.set_video(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    top_down = BirdEyer2(1280,1280)
    top_down.get_video()