import math
import cv2
import numpy as np

class AngleFinder():

    def __init__(self, ball_velocity):
        self.shifted_xs = []
        self.shifted_ys = []
        self.ball_velocity = ball_velocity
        self.distance = 0

    def compute_distance(self, x_length, y_length):
        return math.sqrt(x_length**2 + y_length**2)

    def set_xs(self, xs):
        self.shifted_xs = xs

    def set_ys(self, ys):
        self.shifted_ys = ys

    def find_x_angle(self, x, y):
        return math.atan(y/x)

    def find_y_angle(self, gravity = 9.81, ):
        return math.asin((gravity*self.distance)/self.ball_velocity**2)/2