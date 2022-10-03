# Beer_Pong_Bot

## Overview:
The main idea is to build an autonomous robot to play  the game of [BeerPong](https://en.wikipedia.org/wiki/Beer_pong).
We can divide the project in 3 main stages:
1. [Hardware design](#hardware)
2. [Software design](#software)
3. Testing
---

## Hardware
We'll gonna use a 2 axis robot. All of the pieces are gonna be 3d Printed. A rotary table with a stepper motor will be used to control the movement along one of the axis. The mechanism to throw the ball will be implemented using 2 dc motors controlled by an arduino. These mtors will be placed adjacent to the cannon and will transfer the angular velocity to the ball. The cannon will also have an auto-reloding mechanism for throwing more balls successively. We are gonna use a microcontroller for taking car of low level logic and the actuation part, while for the part of object detection and Video stream processing we will use a device similar to a raspberry pi or a jetson nano (**still to be decided**). A small camera is also part of our equipment ant it will be used to identify the cups and see if the ball finished inside one of them.
To map the enviroment and to do some pose estimation we will use some Aruco Markers positioned near the edges of the table and one on top of the main cannon

### DC Motor Controller:

A low level logic will be implemented using an Arduino uno to control the motors (both the steppers and the dc motors). The DC motors will be controlled using the PWM signal of the  Arduino digital pins. This signal will be the input of a H-Bridge, in particular a L298N that will be our motor Controller. Since the curve of the velocity of the motor does not respond in a linear way we have two options:
1. Close loop sysyem
2. Open loop system
In the open loop system we have two options. THe first is to map in the old fashion way, using a directed and uniform map, the duty cycle of the pwm signal and the speed of the motor (for exemple 255 will correspond to the max speed of the motor while 0 wil be mapped to the motor being in an idle state). The second option is to measure the tuple (Pwm, dist).Then calculate the angular speed of the wheels and so the velocity imprinted to the ball. We can fit a function and so obtain the couple (PWM, Ball Speed) that we will later use to calculate the parabolic trajectory of the ball.
The second option is to use a close loop system were we can measure the speed of the motors/wheels using an infrared light sensor and some reflecting tape and backpropagate this signal in a PID controller. 
Probably we will implement the open loop system being more simple and at the same time really effective.
In the following scheme a summary of the motor logic:
[![](https://mermaid.ink/img/pako:eNp1jz1rw0AMhv-K0NRAQmlGD4XELV1qMPZQaJxB9SnJwd3JyOdCiPPfe27cQodqEPp4H31csBXDmOFRqTvBa9UESLbZVdR3H6x6Lu0eVqvHsaA-st7Xjj55hO3dRs1gg0BhW5VWQlRxjnVxG7CdGBjLtwJqewzkYMx3hURRyH-1-5s2_55fqqQbDKe-9xQMRAEv067nGXz4o684_ku8zMR6JiaPS_SsnqxJ316mSoPxxJ4bzFJo-ECDiw024ZqkNESpz6HFLOrASxw6Q5GfLKWNHrMDuT5VOwrvIj_59Qvnq27w)](https://mermaid.live/edit#pako:eNp1jz1rw0AMhv-K0NRAQmlGD4XELV1qMPZQaJxB9SnJwd3JyOdCiPPfe27cQodqEPp4H31csBXDmOFRqTvBa9UESLbZVdR3H6x6Lu0eVqvHsaA-st7Xjj55hO3dRs1gg0BhW5VWQlRxjnVxG7CdGBjLtwJqewzkYMx3hURRyH-1-5s2_55fqqQbDKe-9xQMRAEv067nGXz4o684_ku8zMR6JiaPS_SsnqxJ316mSoPxxJ4bzFJo-ECDiw024ZqkNESpz6HFLOrASxw6Q5GfLKWNHrMDuT5VOwrvIj_59Qvnq27w)

---

### Stepper motors:
We will use two stepper motors to control the movement of our Robot. Both the motor will be connected to two simple drivers that will fed the Arduino Uno. We decided to use a 2-axis setup so that we can compensate a non-optimal strength/speed control



## Software
The main OS of all the sytem probably will be ROS (or a linux distro for the rasberry pi **ROS is the final Decision**) [Ros Playlist](https://www.youtube.com/watch?v=2lIV3dRvHmQ). The  image processing Pipeline is explained in the following graph.

---
[![](https://mermaid.ink/img/pako:eNp1UUFqwzAQ_MqiUwvJB3woJHZaSgmEJj3ZOSjWOhGNtGIlxYQof69Ut9BLdRKjmdmd0U30pFBU4sjSnWDXdBbyWbTvKBUsOPYERvInst_DfP6UNuR10GSBhuk5wfKhJmKlrQwI26sPaB4nm5f2zdJoIcjDGaHRBq3P2n0xgjVKHxkVjDqcMsVh-t9pWYZD2iAPxAaWmhXgFeGicYRUtzty0JRRBdhPmrpomvbl4_UvkGqygSJDgwH7EiXBqq2j8_Cb7Ye-mtjGxbyNtMcc4YBh1Bb66AChl9bmItJzu6YLQt7WOeRvsZgJg2ykVrnaW0E6EU5osBNVviocZDyHTnT2nqkyBtpebS-qwBFnIjqVC2i0zJ9iRDXIs8f7FwwKj4o)](https://mermaid.live/edit#pako:eNp1UUFqwzAQ_MqiUwvJB3woJHZaSgmEJj3ZOSjWOhGNtGIlxYQof69Ut9BLdRKjmdmd0U30pFBU4sjSnWDXdBbyWbTvKBUsOPYERvInst_DfP6UNuR10GSBhuk5wfKhJmKlrQwI26sPaB4nm5f2zdJoIcjDGaHRBq3P2n0xgjVKHxkVjDqcMsVh-t9pWYZD2iAPxAaWmhXgFeGicYRUtzty0JRRBdhPmrpomvbl4_UvkGqygSJDgwH7EiXBqq2j8_Cb7Ye-mtjGxbyNtMcc4YBh1Bb66AChl9bmItJzu6YLQt7WOeRvsZgJg2ykVrnaW0E6EU5osBNVviocZDyHTnT2nqkyBtpebS-qwBFnIjqVC2i0zJ9iRDXIs8f7FwwKj4o)
We will probably introduce an IMU for measuring the inclination on the y axis and having better results even if the table is tilted. To calibrate the spinning wheels we will use an Euristic. We will test the motors at different speeds and measure the distance that the ball travels. Then we will search a linear correlation betwin the distance the ball travels and the rpms of the motor. Doing this we will have the possibility to chose precisely the speed of the motor according to the distance of the cup that we want to center



## TO DO List:
 - [X] 3D print all parts
 - [ ] Assemble 3D Printed parts
 - [ ] Make simple electronics Work
 - [ ] Test rasberry pi and arduino camera with aruco markers
 - [ ] Study ROS and work with it
 - [ ] Implement Aruco markers distance detection
 - [ ] Cups/Circle Detection
 - [ ] Compute distance between cup and cannon
 - [ ] Workaround math equation to determine how much the turn-table motors need to turn.
 - [ ] Math for partabolic trajectory (strenght and y motor)
 - [ ] Logic to decide at which cup the bot aims
 - [ ] Testing and fine tuning



## Useuful links
1. [Orientation using QR](https://temugeb.github.io/python/computer_vision/2021/06/15/QR-Code_Orientation.html)
2. [Qr code position Estimation](https://github.com/envyen/qr-pose-estimation)
3. [Aruco markers vs QR](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)
4. [Warp Perspective for bird eye view](https://answers.opencv.org/question/232957/apply-getperspectivetransform-and-warpperspective-for-bird-eye-view-python/)
5. [More on bird eye View](https://nikolasent.github.io/opencv/2017/05/07/Bird's-Eye-View-Transformation.html)
6. [Identify Circkes](https://www.delftstack.com/howto/python/opencv-hough-circles/#:~:text=Use%20the%20HoughCircles()%20Function,present%20in%20a%20grayscale%20image.)
7. [Aruco Markers dimension](https://www.youtube.com/watch?v=lbgl2u6KrDU)
8. [Flex camera cable](https://www.amazon.it/dp/B071213Q35/ref=sspa_dk_detail_4?pd_rd_i=B071213Q35&pd_rd_w=dgF6h&content-id=amzn1.sym.7d53b420-4ab4-47bf-9f3c-0af37b169282&pf_rd_p=7d53b420-4ab4-47bf-9f3c-0af37b169282&pf_rd_r=8DEK2B3MZ7S97MGT476Q&pd_rd_wg=PT7Ur&pd_rd_r=9b181f0d-3bd7-4426-ab04-5aaabbb91dc3&s=lighting&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&smid=A1X7QLRQH87QA3&th=1)
9. [Cameras Comparison](https://www.androidcentral.com/best-raspberry-pi-camera)
