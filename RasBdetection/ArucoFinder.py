import cv2
import numpy as np
from Visual_handler import Visual_handler

class ArucoFinder(Visual_handler):
    def __init__(self):
        super().__init__()
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
        self.marker = np.zeros((300,300,1), dtype="uint8")
        self.center = (0,0)

    def draw_marker(self,  id):
        cv2.aruco.drawMarker(self.aruco_dict, id, 300, self.marker, 1)


    def detect_marker(self, frame):
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, self.aruco_dict)
        return corners, ids, rejectedImgPoints

    def draw_detected_marker(self, frame, corners, ids):
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        return frame

    def draw_axis(self, frame, corners, ids):
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, self.cam_matrix, self.dist_coeffs)
        frame = cv2.aruco.drawAxis(frame, self.cam_matrix, self.dist_coeffs, rvec, tvec, 0.1)
        return frame

    def draw_all(self, frame):
        corners, ids, rejectedImgPoints = self.detect_marker(frame)
        frame = self.draw_detected_marker(frame, corners, ids)
        frame = self.draw_axis(frame, corners, ids)
        return frame

    def marker_distance(self, corners):
        if corners:
            x = corners[0][0][0][0]
            y = corners[0][0][0][1]
            return np.sqrt(x**2 + y**2)
        else:
            return 0

    def get_marker_distance(self, frame):
        corners, ids, rejectedImgPoints = self.detect_marker(frame)
        return self.marker_distance(corners)

    def find_center(self, aruco1, aruco2):
        self.center = ((aruco1[0][0][0][0] + aruco2[0][0][0][0])/2, (aruco1[0][0][0][1] + aruco2[0][0][0][1])/2)


    def get_center(self):
        return self.center

    def get_marker(self):
        return self.marker


if __name__ == "__main__":
    finder = ArucoFinder()
    finder.draw_marker(1)


