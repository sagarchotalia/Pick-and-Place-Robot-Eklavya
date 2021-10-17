# -*- coding: utf-8 -*-
# importing modules
import time
import numpy as np
import cv2
from zmqRemoteApi import RemoteAPIClient
from bp3d import Bin, Item, bp3D
# connecting via ZMQ Api at port 23000 
client = RemoteAPIClient('localhost',23000)
# getting simulation handles
sim = client.getObject('sim')
simIK = client.getObject('simIK')
# starting simulation
sim.startSimulation()
# getting object handles 
simBase=sim.getObjectHandle('Gantry_Base') 
simTip=sim.getObjectHandle('Tip')
conveyor_sensor=sim.getObjectHandle('conveyor__sensor')
conveyorhandle=sim.getObjectHandle('efficientConveyor')
otherScriptHandle=sim.getCustomizationScriptAssociatedWithObject(conveyorhandle)
# belt_vel=0.2
# getting handles of dummy points of path to be followed
simTarget=sim.getObjectHandle('Target')
simPoint1=sim.getObjectHandle('Target0')
simPoint2=sim.getObjectHandle('Target2')
simPoint3=sim.getObjectHandle('Target1')
simPoint4=sim.getObjectHandle('Target3')
refPoint=sim.getObjectHandle('Reference')
# getting camera handles
visionSensorHandle_xy = sim.getObjectHandle('Vision_sensor_xy')
visionSensorHandle_yz = sim.getObjectHandle('Vision_sensor_yz')
# object detection counter variables
contour_prev_y_coordinate=-1
no_of_boxes=0
contour_y_coordinate=-1
image_ortho_size_xy=0.45  
image_ortho_size_z=0.50
#setting path points position
position1=sim.getObjectPosition(simPoint1,-1)
quaternion1=sim.getObjectQuaternion(simPoint1,-1)
position2=sim.getObjectPosition(simPoint2,-1)
quaternion2=sim.getObjectQuaternion(simPoint2,-1)
position3=sim.getObjectPosition(simPoint3,-1)
quaternion3=sim.getObjectQuaternion(simPoint3,-1)
position4=sim.getObjectPosition(simPoint4,-1)
quaternion4=sim.getObjectQuaternion(simPoint4,-1)
difference=position4[2]-position3[2]
#bot motion parameters
vel=0.01
accel=0.1
jerk=70
currentVel=[0]*4
currentAccel=[0]*4
maxVel=[vel]*4
maxAccel=[accel]*4
maxJerk=[jerk]*4
targetVel=[0]*4
# bin algo initialisation
box_dim = [0.42,0.22,0.31]
box_dim = [i * 100 for i in box_dim] 
box_dim = [round(x) for x in box_dim]
bin_1 = Bin("Container_Bin_1", box_dim[0], box_dim[1], box_dim[2])
# buffer
buffer=[]

def setTargetPoint(pivot):
    global buffer
    ref_pos=sim.getObjectPosition(refPoint,-1)
    for i in range(3):
        ref_pos[i]+=pivot[i]
    buffer.append(ref_pos)


def object_dimensions(img,resX,resY,img_1, resX_1, resY_1):
    global contour_prev_y_coordinate,no_of_boxes,contour_y_coordinate
    
    img = cv2.cvtColor(np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3),cv2.COLOR_BGR2GRAY)
    _,threshold= cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    img_1 = cv2.cvtColor(np.frombuffer(img_1, dtype=np.uint8).reshape(resY_1, resX_1, 3),cv2.COLOR_BGR2GRAY)
    _,threshold_1= cv2.threshold(img_1,100,255,cv2.THRESH_BINARY)
    contours_1,_ = cv2.findContours(threshold_1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
            (x,contour_y_coordinate,length,width)=cv2.boundingRect(cnt)            
    if(contour_prev_y_coordinate==-1):
        contour_prev_y_coordinate=contour_y_coordinate
        return                
    if(contour_prev_y_coordinate!=0&contour_prev_y_coordinate!=-1):
        contour_prev_y_coordinate=contour_y_coordinate
        return       
    if(contour_y_coordinate>0&contour_prev_y_coordinate==0):
        length=round(((length/resY)*image_ortho_size_xy),2)
        width=round(((width/resX)*(image_ortho_size_xy/2)),2)
        for cnts in contours_1:
                (_,_,depth,ht)=cv2.boundingRect(cnts)
        depth=round(((depth/resX_1)*image_ortho_size_z),2)
        # initialising a box of [length,width,depth]
        box=Item("box"+str(no_of_boxes),length*100,width*100,depth*100)
        pivot=bp3D(bin_1, box) # bp3d algo returns the position where box is placed
        setTargetPoint(pivot)
        del box
        no_of_boxes+=1
        
    contour_prev_y_coordinate=contour_y_coordinate        
            
ikEnv=simIK.createEnvironment()
ikGroup_undamped=simIK.createIkGroup(ikEnv)
simIK.setIkGroupCalculation(ikEnv,ikGroup_undamped,simIK.method_pseudo_inverse,0,6)
ikElement,simToIkMap=simIK.addIkElementFromScene(ikEnv,ikGroup_undamped,simBase,simTip,simTarget,simIK.constraint_pose)

while(True):    
    result=sim.rmlMoveToPosition(simTarget,-1,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,position1,quaternion1,targetVel)
    simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)
    img, resX, resY = sim.getVisionSensorCharImage(visionSensorHandle_xy)
    img_1, resX_1, resY_1 = sim.getVisionSensorCharImage(visionSensorHandle_yz)
    if(len(img)&len(img_1)):
        object_dimensions(img, resX, resY,img_1, resX_1, resY_1)
    
    

    


        
    
    
      
        
        

    
        
