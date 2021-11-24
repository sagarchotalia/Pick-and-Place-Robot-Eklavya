# Eklavya: The Journey behind Simulating a Bin-Packing Pick-and-Place Robot

## Introduction
These 6 weeks of Eklavya proved to be a great challenge for Ayush and me, as we struggled to get our concepts down, learn an entirely new software, implement connection with API's, code, resolve some really complex problems, code some more... you get the idea.

All throughout the project, our seniors of [SRA](https://sravjti.in/) helped us out at every turn, resolved the simplest of doubts and issues(perhaps with a sigh), and guided us to completion.
## Why this project?
Our seniors provided us with an Excel sheet containing all the available project topics for the taking, and a Google Form that allowed us to choose the top projects we were interested in, and provide suggestions for any other topics we were interested in. To make it short, me and Ayush ended up writing the same (or at least similar) topics in the suggestion; a moving pick and place robot. We were quite interested in how to implement something like this.

SRA conducted a final interview before the actual project began, to gauge interest in the topic. In that interview, our seniors offered the project that they'd been working on; the one that had won them [2nd Prize Internationally in the Delta Cup](https://www.youtube.com/watch?v=JBdjbeT3EMY), which was an absolute honour for us.

And thus began our journey.
## Algorithm Writing
We had a dilemma on our hands. It was fine that we didn't know anything about robot simulation, but we had no idea about the topic of Bin Packing itself, we just knew that it meant minimizing the wasted space while packing bins into containers.

And so, for the first two weeks, we were focused on getting the algorithm part done.

Bin packing in two dimensions requires a bit of thinking. You need to decide where you have to start placing boxes from, in what order you want the boxes to be, and whether they should be rotated or not. We spent a lot of time reading: research papers, resources from all over the web, repositories for the implementation of the same kind of stuff etc. Then, we found out that there are several approcahes to it: you can place them randomly, you can create shelves based on the largest box in a level such as this:

![image](https://user-images.githubusercontent.com/72294682/143036185-c19b0a00-07e0-42b8-ad77-27478aa63056.png)

(I highly suggest reading about first fit, next fit and worst fit algorithms as well)

There are also 2-dimensional guillotine algorithms which are quite interesting(The name must remind you of the French King Louis XVI and Queen Marie Antoinette being executed, but worse than that, it must be giving you flashbacks of what life used to be like when you were 15 and your biggest problem in life was Social Studies. Ah, bliss.).

Moving on.

The Bin Packing Algorithm is a NP hard problem. Thus heuristic algorithms represent the best approach to perform bin packing with reasonable efficiency.
The 3D algorithm of the same would have definitely taken us another week or so to properly implement. Hence, we just decided to use the basic logic of(and change the code according to the needs of the API used, which is discussed ahead) [this](https://github.com/dragostudorache/3D-Bin-Packing-Text-Based-Python-Script) amazing repository.

Hence, we were done with the algorithm picking. However, the scene proved to be *quite* challenging as well...
## Scene Modification
Our seniors generously provided us a scene in CoppeliaSim, which is a great software for robot simulation and modification, and one that we learnt from scratch.

![image](https://user-images.githubusercontent.com/72294682/143039658-26fbf635-91f1-40af-98f6-5150fae95582.png)

We played around with it a bit, changing the values of the conveyor velocity, trying to get the boxes to be picked, trying to read the box dimensions using a vision sensor and so on.
But, we were facing issues. 

The thing is, if you have a robot or any object in CoppeliaSim, and you don't have to control it precisely, then you're all good. *However*, if you're going to need the tip of the robot to be at a certain position, or move from its default position to a certain point, or anything similar to that, what you'll need to implement is Inverse Kinematics. The name is quite intimidating, but honestly, the concept is pretty simple. Simply put,
> Inverse Kinematics involves the description of a point in space in order to calculate the joint position and orientation of a robot in order to reach it.

As you may have guessed, when you're given just a point in space with nothing else but the constraints of the joints, the calculations required to actually figure out the angles and joint coordinates get pretty complex(Googling those formulae does not help).

So, we read about the setting up of a scene in IK Mode and implemented it in CoppeliaSim. Implementing this solved most of our issues and helped us to control the scene.
## Let's talk API

In order to move the robot parts to a certain point, we need to communicate with the scene first. This is done via Application Programming Interfaces(API's). CoppeliaSim offers support for various API's.

We first tried writing the script using the regular API pre-included. However, that had to be written in Lua, which is a programming language we both were not familiar with. Writing the API script in Python would offer more documentation with integration of OpenCV, plus we were more familiar with Python.

So, we switched to the Remote API which could be written in Python. Most functions were really useful there, like the ```sim``` functions. We tried writing the script in this version of the API, but we ran into a problem.

The problem was that, our scene was in the IK Mode, however this remote API didn't provide IK functionality. So, we had to switch to a different API, the ZeroMQ API.
## The ZeroMQ API

CoppeliaSim offers several ways to communicate with the actual scene and control the scene elements viz, signals (blocks of data), calling script functions and API functions. 

API functions are really useful as they allow us to perform the above task in a language of our choice like Python or Matlab.
The ZeroMQ (ZMQ) API is one such API supported by CoppeliaSim starting from v4.2. It gives us all the regular API functions(i.e. sim.* -type functions), along with all API functions provided by plugins (e.g. simOMPL.* , simUI.* , simIK.* , etc.). 

In our simulation, we wanted to implement inverse kinematics in python along with the other functions supported by the remote api, hence we used ZMQ API.

### Setting up ZMQ API

In order to use the ZMQ API, we must download certain files and add them to the CoppeliaSim package contents. The instructions on how to do this are mentioned in detail on the [CoppeliaRobotics website](https://www.coppeliarobotics.com/helpFiles/en/zmqRemoteApiOverview.htm)

Next, we need an environment where we can write the actual scripts that will connect to the scene. For our purposes, [Spyder](https://www.spyder-ide.org/) is more than sufficient. After this, run these commands in the Spyder Terminal:

`pip install pyzmq`

`pip install cbor`
- Once this is done we are ready to write the code to control the simulation scene. 

## Writing Python Scripts for Simulation

### In the Scene 
Add the line
```sh
simRemoteApi.start(23000) 
```
in the main script. This is the port at which the API will communicate with the scene(the default port is 23000).

### In the Python Script
##### For establishing communication 

We need to import remoteApiClient and connect via ZMQ API at port 23000
```sh 
from zmqRemoteApi import RemoteAPIClient
client_id = RemoteAPIClient('localhost',23000)
``` 
NOTE: If the client_id = -1, it means that the communication is unsuccessful.
##### Getting Simulation Handles
For every namespace or functionality you need , get the simulation handles
```sh 
sim = client.getObject('sim') # all sim.* type of functions and constants
simIK = client.getObject('simIK') #all simIK.* type of functions and constants
```
##### Getting Object Handles
Next we access all the objects in scene which we want to affect in the scene. The function returns an integer object handle which can be understood as an ID, which can be used anywhere to access the particular object (shapes/joints/sensors). 
```sh
object_handle_name=sim.getObjectHandle('scene_element_name')
```
##### Starting the Simulation
```sh 
sim.startSimulation() 
``` 
If the value returned is:
- -1: This means that there's an error.
- 0: This means that the operation could not be performed.
- greater than 0: Success! 
##### Working with Joints
There are various functions associated with joints like velocity, force and position control. For example, 
```sh
sim.setJointTargetVelocity(int objectHandle,float targetVelocity)
```
sets the target velocity of a non-spherical joint in torque-force mode
(motor enabled and position control disabled).

We wrote up these functions and had to trial-run multiple times, changing up the position of some code and variables; sometimes amusing stuff would happen, like a part of the robot would fly off the screen completely. You just have to try modifying the code and check the scene variables until you figure out what the issues are.

##### Working with vision sensors

```sh 
img, resX, resY = sim.getVisionSensorCharImage(visionSensorHandle)
img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
```
`img` returned is a 1 dimensional array, needs to be resized using NumPy.

##### Closing the Simulation 
```sh 
sim.closeSimulation()
```
The return value is : 
- -1 in case of an error, 
- 0 if the operation could not be performed, and
- greater than 0 in case of success.

## Object Detection

To detect the object and determine its dimensions we used two [vision sensors](https://www.coppeliarobotics.com/helpFiles/en/visionSensorPropertiesDialog.htm) (one for determining the x and y dimensions and other for the z dimensions)  and [OpenCV](https://pypi.org/project/opencv-python/) library.

The image is provided continuously by the vision sensors. 

```sh
img, resX, resY = sim.getVisionSensorCharImage(visionSensorHandle_xy) 
```

Upon receiving an image, it is converted to gray scale and [binary thresholding](https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html) is applied. Then the boundary in the image is calculated, this done by contours. Contours can be explained simply as a curve joining all the continuous points (along the boundary), having the same color or intensity. A bounding rectangle is created for the contour that is created. 
```py
img = cv2.cvtColor(np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3),cv2.COLOR_BGR2GRAY)
 _,threshold= cv2.threshold(img,100,255,cv2.THRESH_BINARY)
 contours,_ = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/74896007/143065811-730f9cfb-f6e5-4e99-8cee-d01a92c6f4ee.png">
</p>

Whenever the points of the bounding rectangle of the box  are not at the exact boundary of the image captured by the camera , at that instance the dimensions of the rectangle are stored in pixels. This is to validate if the box is completely under the frame. The length, width and depth that are stored in pixels are converted to actual dimensions in metres by using the conversion factor. 

```py
  if(contour_y_coordinate>0&contour_prev_y_coordinate==0):
        length=round(((length/resY)*image_ortho_size_xy),2)
        width=round(((width/resX)*(image_ortho_size_xy/2)),2)
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/74896007/143063396-fee7accd-dff2-41ca-889e-acb29ff61e47.jpg">
</p>

## Motion of the Robot
Now, the objects are getting detected, the API is working fine, etc. Let's talk motion of the bot. In order to move the bot, CoppeliaSim has a Motion Library called RML, that offers API functions. We ended up using the function `sim.rmlMoveToPosition` in order to move an object from one position to another.

Our basic logic was this:

![image](https://user-images.githubusercontent.com/72294682/143230070-332ad1bf-9d40-4496-a4b3-183278318d72.png)

When the vision sensor detects a box at point 1, 
1. Move the tip of the robot to point 1.
2. Pick the box up and move to point 2.
3. Move the tip with the box to point 3.
4. Place the box down at point 4.

The coordinates of point 4, which is actually inside the box, are determined using the Bin Packing Algorithm.


## Resources and References
Here are some of the resources we used for this project.
| Description | Link |
| ------ | ------ |
| Example API Scripts | [zmqRemoteApi](https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python) folder |
| Regular API Functions | [CoppeliaSim Manual ](https://www.coppeliarobotics.com/helpFiles/en/apiFunctions.htm) |
| ZMQ API | [ZMQ Coppelia Manual](https://www.coppeliarobotics.com/helpFiles/en/zmqRemoteApiOverview.htm) |
| CoppeliaSim Forum | [CoppeliaSim Forum](https://forum.coppeliarobotics.com/) |
| Research Papers | [Research Papers](https://github.com/sagarchotalia/Pick-and-Place-Robot-Eklavya/tree/main/Algorithm/Resources)|

## Conclusion

There was so much more to Eklavya than what could be summed up in this blog. The technical aspect of it may have been summarized, but our learning experience, the challenges, frustration, disappointment, perseverence and so much more behind the scenes can't be explained fully. 

Eklavya truly was an amazing mentorship program and it got us all skilled in certain aspects; not just the technical ones, but also sticking to deadlines, clearing doubts and issues, and, no matter what, to **_keep learning as much as possible._**
