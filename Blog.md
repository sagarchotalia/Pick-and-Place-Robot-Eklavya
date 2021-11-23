# Eklavya: The Journey behind Simulating a Bin-Packing Pick-and-Place Robot

## Introduction
These 6 weeks of Eklavya proved to be a great challenge for Ayush and me, as we struggled to get our concepts down, learn an entirely new software, implement connection with API's, code, resolve some really complex problems, code some more... you get the idea.

All throughout the project, our seniors of [SRA](https://sravjti.in/) helped us out at every turn, resolved the simplest of doubts and issues(perhaps with a sigh), and guided us to completion.
## Why this project?
Eklavya had a selection process, in which there were certain challenging programming tasks we had to implement in order to get selected. Once we were done with them, our seniors provided us with an Excel sheet containing all the available project topics for the taking, and a Google Form that allowed us to choose the top projects we were interested in.

There was also a blank that said "Mention other project topics, if any, that you'd be interested in".

Me and Ayush were separately interested in certain topics, and commonly interested in other ones; so we filled that blank out by our own choices. To make it short, we ended up writing the same (or at least similar) topics; a pick and place robot that could move.

SRA is thorough in their practices. They conducted a final interview before the actual project began, to gauge interest in the topic. In that interview, our seniors offered the project that they'd been working on; the one that had won them [2nd Prize Internationally in the Delta Cup](https://www.youtube.com/watch?v=JBdjbeT3EMY), which was an absolute honour for us.

And thus began our journey.
## Algorithm Writing
We had a dilemma on our hands. It was fine that we didn't know anything about robot simulation, but we had no idea about the topic of Bin Packing itself, we just knew that it meant minimizing the wasted space while packing bins into containers.

And so, for the first two weeks, we were laser-focused on getting the algorithm part done. Bin packing in one dimension is child's play; you just stack up stuff. 

Bin packing in two dimensions requires a bit more thinking. You need to decide where you have to start placing boxes from, in what order you want the boxes to be, and whether they should be rotated or not. This is why we spent a lot of time reading: research papers, resources from all over the web, repositories for the implementation of the same kind of stuff etc. Then, we found out that there are several approcahes to it: you can place them randomly, you can create shelves based on the largest box in a level such as this:

![image](https://user-images.githubusercontent.com/72294682/143036185-c19b0a00-07e0-42b8-ad77-27478aa63056.png)

(I highly suggest you read about first fit, next fit and worst fit algorithms as well)

There are also 2-dimensional guillotine algorithms. The name must remind you of the French King Louis XVI and Queen Marie Antoinette being executed, but worse than that, it must be giving you flashbacks of what life used to be like when you were 15. Ah, bliss.

Moving on.

The main challenge was when we had to implement a 3-Dimensional Bin packing algorithm. Now, the 2D one was difficult enough to implement. The 3D one would have definitely taken us another week or so. Hence, we just decided to use the basic logic of(and heavily modify the code according to the needs of the API used, which is discussed ahead) [this](https://github.com/dragostudorache/3D-Bin-Packing-Text-Based-Python-Script) amazing repository.

Hence, we were done with the algorithm picking. However, the scene proved to be *quite* challenging as well...
## Scene Modification
Our seniors generously provided us a scene in CoppeliaSim, which is a great software for robot simulation and modification, and one that we learnt from scratch.

![image](https://user-images.githubusercontent.com/72294682/143039658-26fbf635-91f1-40af-98f6-5150fae95582.png)

We played around with it a bit, changing the values of the conveyor velocity, trying to get the boxes to be picked, trying to read the box dimensions using a vision sensor and so on.
But, we were facing issues. 

((**name issues here**))

Hence, we saw the implementation of a scene in Inverse Kinematics Mode(or IK Mode). The name is quite intimidating, but honestly, the concept is pretty simple. 
> Inverse Kinematics involves the description of a point in space in order to calculate the joint position and orientation of a robot in order to reach it.

So, we read about the setting up of a scene in IK Mode and implemented it in CoppeliaSim. We faced a few small but surmountable difficulties in our way, but once we were
done with it, it helped us an awful lot with our progress.
## Problems faced with Regular API
Well, we first tried using the regular API that comes with CoppeliaSim. However, that had to be written in Lua, which is a programming language we both were
not familiar with. Writing the API script in Python would offer more documentation with integration of OpenCV, plus we were more familiar with Python.

So, we switched to the Remote API which could be written in Python. Most functions were really useful there, like the ```sim``` functions. We tried writing the script in this version of the API, but we ran into a problem.

The problem was that, our scene was in the IK Mode, however this remote API didn't provide IK functionality. So, we had to switch to a different API, the ZeroMQ API.
## The ZeroMQ API

CoppeliaSim offers several ways to communicate with the actual scene and control the scene elements viz,signals (blocks of data), calling script functions and API functions. 

API functions are really useful as they allow us to perform the above task in a language of our choice like Python or Matlab.
The ZeroMQ (ZMQ) API is one such API supported by CoppeliaSim starting from v4.2. It offers all API functions also available via a CoppeliaSim script: this includes all regular API functions (i.e. sim.* -type functions), but also all API functions provided by plugins (e.g. simOMPL.*, simUI.*, simIK.*, etc.). The ZeroMQ-based remoteAPI can be used in the exact same way as from within a CoppeliaSim script.

One benefit of the ZMQ API is that it supports all regular API which can be written in Python. In our simulation we wanted to implement inverse kinematics in python along with the other functions supported by the remote api, hence we used ZMQ API.
`Follow the set-up instructions for versions 4.2. only.`

### Setting up ZMQ API

- Navigate the folder containing the files for CoppeliaSim.
- Clone the [ZMQ API repository](https://github.com/CoppeliaRobotics/zmqRemoteApi.git) in the ```CoppeliaSim/programming``` folder. 
(Download the repository as zip under the code button present in the github page and extract it to the folder)
- Add the [simAddOnZMQ remote API.lua](https://coppeliarobotics.com/files/tmp/simAddOnZMQ%20remote%20API.lua) file to your main CoppeliaSim folder (for the add-on).
- Navigate to ```CoppeliaSim/lua``` folder. Place [cbor.lua](https://coppeliarobotics.com/files/tmp/cbor.lua) and [simZMQ.lua](https://coppeliarobotics.com/files/tmp/simZMQ.lua) in the folder. Replace any file with the same name.

## Setting up environment for Python Scripts 
- For running the scene using API functions we need to write python scripts. [Spyder](https://www.spyder-ide.org/) is a Python IDE which can be used for the same.
- In the folder where the python scripts are to be written, place the [zmqRemoteApi](https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python/zmqRemoteApi) client files folder of ZMQ API in the same directory. 
It can be done by navigating to ``` CoppeliaSim/programming/zmqRemoteApi/clients/python/``` folder and copying zmqRemoteApi folder into the folder containing the python scripts.
- In the Spyder Terminal run commands 
`pip install pyzmq`
`pip install cbor`
- Once this is done we are ready to write the code to control the simulation scene. 

## Writing Python Scripts for Simulation

### In the Scene 
In the main script(or any other script associated with a scene element), add the line
```sh
simRemoteApi.start(23000) 
```
This is the port at which the API will communicate with the scene(the default port is 23000).

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
Next we access all the objects in scene which we want to affect in the scene. The function returns an integer object handle which can be understood as an id which can be used anywhere to access the particular object (shapes/joints/sensors). 
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

We wrote up these functions and had to trial-run multiple times, changing up the position of some code and variables; sometimes amusing stuff would happen, like a part of the robot would fly off the screen completely.

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

## Resources/References
| Description | Link |
| ------ | ------ |
| Example API Scripts | [zmqRemoteApi](https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python) folder |
| Regular API Functions | [CoppeliaSim Manual ](https://www.coppeliarobotics.com/helpFiles/en/apiFunctions.htm) |
| ZMQ API | [ZMQ Coppelia Manual](https://www.coppeliarobotics.com/helpFiles/en/zmqRemoteApiOverview.htm) |
| CoppeliaSim Forum | [CoppeliaSim Forum](https://forum.coppeliarobotics.com/) |

## Object Detection

To detect the object and determine its dimensions we used two [vision sensors](https://www.coppeliarobotics.com/helpFiles/en/visionSensorPropertiesDialog.htm) (one for determining the x and y dimensions and other for the z dimensions)  and [OpenCV](https://pypi.org/project/opencv-python/) library. 

Remember to install Opencv and NumPy.

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

## Conclusion

There was so much more to Eklavya than what could be summed up in this blog. The technical aspect of it may have been summarized, but our learning experience, the challenges, frustration, disappointment, perseverence and so much more behind the scenes can't be explained fully. 

Eklavya truly was an amazing mentorship program and it got us all skilled in certain aspects; not just the technical ones, but also sticking to deadlines, clearing doubts and issues, and, no matter what, to **_keep learning as much as possible._**
