# -*- coding: utf-8 -*-
#importing modules
import time
import numpy as np
import cv2
from zmqRemoteApi import RemoteAPIClient

client = RemoteAPIClient('localhost',23000)
sim = client.getObject('sim')
simIK = client.getObject('simIK')

sim.startSimulation()

simTarget=sim.getObjectHandle('Target')
simBase=sim.getObjectHandle('Gantry_Base')
simTip=sim.getObjectHandle('Tip')
simPoint1=sim.getObjectHandle('Target0')
simPoint2=sim.getObjectHandle('Target2')
simPoint3=sim.getObjectHandle('Target1')
simPoint4=sim.getObjectHandle('Target3')

conveyor_sensor=sim.getObjectHandle('conveyor__sensor')
conveyorhandle=sim.getObjectHandle('efficientConveyor')

otherScriptHandle=sim.getCustomizationScriptAssociatedWithObject(conveyorhandle)

visionSensorHandle_xy = sim.getObjectHandle('Vision_sensor_xy')
visionSensorHandle_yz = sim.getObjectHandle('Vision_sensor_yz')


belt_vel=0.2
prev_y=-1
counter=0
y=-1  

position1=sim.getObjectPosition(simPoint1,-1)
quaternion1=sim.getObjectQuaternion(simPoint1,-1)

position2=sim.getObjectPosition(simPoint2,-1)
quaternion2=sim.getObjectQuaternion(simPoint2,-1)

position3=sim.getObjectPosition(simPoint3,-1)
quaternion3=sim.getObjectQuaternion(simPoint3,-1)

position4=sim.getObjectPosition(simPoint4,-1)
quaternion4=sim.getObjectQuaternion(simPoint4,-1)

vel=0.005
accel=0.1
jerk=70
currentVel=[0]*4
currentAccel=[0]*4
maxVel=[vel]*4
maxAccel=[accel]*4
maxJerk=[jerk]*4
targetVel=[0]*4

def pick_place(detectedObjectHandle):
    result1=sim.rmlMoveToPosition(simTarget,-1,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,position2,quaternion2,targetVel)
    simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)
    sim.setObjectInt32Parameter(detectedObjectHandle,sim.shapeintparam_static,1)
    sim.resetDynamicObject(detectedObjectHandle)
    
    sim.setObjectParent(detectedObjectHandle,simTip,True)
    
    result=sim.rmlMoveToPosition(simTarget,-1,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,position1,quaternion1,targetVel)
    simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)
    
    result2=sim.rmlMoveToPosition(simTarget,-1,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,position3,quaternion3,targetVel)
    simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)
    
    result3=sim.rmlMoveToPosition(simTarget,-1,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,position4,quaternion4,targetVel)
    simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)
    
    sim.setObjectInt32Parameter(detectedObjectHandle,sim.shapeintparam_static,0)
    sim.setObjectParent(detectedObjectHandle,-1,True)  

def object_dimensions(img,resX,resY):
    global y,prev_y,counter
    img = cv2.cvtColor(np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3),cv2.COLOR_BGR2GRAY)
    _,threshold= cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
            (x,y,w,h)=cv2.boundingRect(cnt)            
    if(prev_y==-1):
        prev_y=y
        return                
    if(prev_y!=0&prev_y!=-1):
        prev_y=y
        return       
    if(y>0&prev_y==0):
        print("[", w, h,"]")
        print("box")
        counter+=1
        print(counter)        
    prev_y=y        
            
ikEnv=simIK.createEnvironment()
ikGroup_undamped=simIK.createIkGroup(ikEnv)
simIK.setIkGroupCalculation(ikEnv,ikGroup_undamped,simIK.method_pseudo_inverse,0,6)
ikElement,simToIkMap=simIK.addIkElementFromScene(ikEnv,ikGroup_undamped,simBase,simTip,simTarget,simIK.constraint_pose)

while(True):    
    result=sim.rmlMoveToPosition(simTarget,-1,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,position1,quaternion1,targetVel)
    simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)
    img, resX, resY = sim.getVisionSensorCharImage(visionSensorHandle_xy)
    if(len(img)):
        object_dimensions(img, resX, resY)
    reading=sim.handleProximitySensor(conveyor_sensor)
    if(reading!=0):        
        sim.setScriptVariable('vel',otherScriptHandle,0.0)
        reading,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.handleProximitySensor(conveyor_sensor)
        pick_place(detectedObjectHandle)
    


        
    
    
      
        
        

    
        
