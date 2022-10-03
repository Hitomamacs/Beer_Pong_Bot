# Beer_Pong_Bot

## Overview:
The main idea is to build an autonomous robot to play  the game of [BeerPong](https://en.wikipedia.org/wiki/Beer_pong).
We can divide the project in 3 main stages:
1. Hardware design
2. Software design
3. Testing
---

### Hardware:
We'll gonna use a 2 axis robot. All of the pieces are gonna be 3d Printed. A rotary table with a stepper motor will be used to control the movement along one of the axis. The mechanism to throw the ball will be implemented using 2 dc motors controlled by an arduino. These mtors will be placed adjacent to the cannon and will transfer the angular velocity to the ball. The cannon will also have an auto-reloding mechanism for throwing more balls successively. We are gonna use a microcontroller for taking car of low level logic and the actuation part while for the part of object detection and processing the Video stream we will use a device similar to a raspberry pi or a jetson nano (**still to be decided**). A small camera is also part of our equipment ant it will be used to identify the cups and see if the ball finished inside one of them.
To map the enviroment and to do some pose estimation we will use some Aruco Markers positioned near the edges of the table and one on top of the main cannon

### Sofware:
The main OS of all the sytem probably will be ROS or a linux distro for the rasberry pi. The  image processing Pipeline is explained in the following graph.

---
[![](https://mermaid.ink/img/pako:eNp1UUFqwzAQ_MqiUwvJB3woJHZaSgmEJj3ZOSjWOhGNtGIlxYQof69Ut9BLdRKjmdmd0U30pFBU4sjSnWDXdBbyWbTvKBUsOPYERvInst_DfP6UNuR10GSBhuk5wfKhJmKlrQwI26sPaB4nm5f2zdJoIcjDGaHRBq3P2n0xgjVKHxkVjDqcMsVh-t9pWYZD2iAPxAaWmhXgFeGicYRUtzty0JRRBdhPmrpomvbl4_UvkGqygSJDgwH7EiXBqq2j8_Cb7Ye-mtjGxbyNtMcc4YBh1Bb66AChl9bmItJzu6YLQt7WOeRvsZgJg2ykVrnaW0E6EU5osBNVviocZDyHTnT2nqkyBtpebS-qwBFnIjqVC2i0zJ9iRDXIs8f7FwwKj4o)](https://mermaid.live/edit#pako:eNp1UUFqwzAQ_MqiUwvJB3woJHZaSgmEJj3ZOSjWOhGNtGIlxYQof69Ut9BLdRKjmdmd0U30pFBU4sjSnWDXdBbyWbTvKBUsOPYERvInst_DfP6UNuR10GSBhuk5wfKhJmKlrQwI26sPaB4nm5f2zdJoIcjDGaHRBq3P2n0xgjVKHxkVjDqcMsVh-t9pWYZD2iAPxAaWmhXgFeGicYRUtzty0JRRBdhPmrpomvbl4_UvkGqygSJDgwH7EiXBqq2j8_Cb7Ye-mtjGxbyNtMcc4YBh1Bb66AChl9bmItJzu6YLQt7WOeRvsZgJg2ykVrnaW0E6EU5osBNVviocZDyHTnT2nqkyBtpebS-qwBFnIjqVC2i0zJ9iRDXIs8f7FwwKj4o)
We will probably introduce an IMU for measuring the inclination on the y axis and having better results even if the table is tilted. To calibrate the spinning wheels we will use an Euristic. We will test the motors at different speeds and measure the distance that the ball travels. Then we will search a linear correlation betwin the distance the ball travels and the rpms of the motor. Doing this we will have the possibility to chose precisely the speed of the motor according to the distance of the cup that we want to center



## TO DO List:
 



## Useuful links
1. [Orientation using QR](https://temugeb.github.io/python/computer_vision/2021/06/15/QR-Code_Orientation.html)
2. [Qr code position Estimation](https://github.com/envyen/qr-pose-estimation)
3. [Aruco markers vs QR](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)
4. [Warp Perspective for bird eye view](https://answers.opencv.org/question/232957/apply-getperspectivetransform-and-warpperspective-for-bird-eye-view-python/)
5. [More on bird eye View](https://nikolasent.github.io/opencv/2017/05/07/Bird's-Eye-View-Transformation.html)
6. [Identify Circkes](https://www.delftstack.com/howto/python/opencv-hough-circles/#:~:text=Use%20the%20HoughCircles()%20Function,present%20in%20a%20grayscale%20image.)
