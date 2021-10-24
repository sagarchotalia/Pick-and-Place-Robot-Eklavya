

# Pick and Place Robot using Bin Packing
This project aims to use and simulate an efficient bin packing algorithm to pick and place boxes into bins(containers) in CoppeliaSim.

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Tech Stack](#tech-stack)
  * [File Structure](#file-structure)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installations](#installations)
  * [Execution](#execution)
* [Theory and Approach](#theory-and-approach)
* [Results and Demo](#results-and-demo)
* [Future Work](#future-work)
* [Troubleshooting](#troubleshooting)
* [Contributors](#contributors)
* [Acknowledgements and Resources](#acknowledgements-and-resources)
* [License](#license)


<!-- ABOUT THE PROJECT -->
## About The Project
Bin packing is one of the most interesting problems in combinatorics. It has multiple applications, such as packaging boxes in containers, loading trucks with weight capacity constraints, creating file backups in media and technology mapping in FPGA semiconductor chip design. This project aims to implement a bin packing algorithm that packs variable sized boxes into containers and simulate the same in a CoppeliaSim Scene. 

### Tech Stack
- [CoppeliaSim](https://www.coppeliarobotics.com/downloads)
- [Spyder](https://www.spyder-ide.org/)
- [OpenCV](https://opencv.org/)

### File Structure
```sh

 ┣Algorithms                           # ALgorithms written and tested
 ┃ ┣1D Algorithms                      # 1 Dimensional Bin packing algorithms
 ┃ ┃ ┣BestFitAlgorithm.cpp             
 ┃ ┃ ┣FirstFitAlgorithm.cpp            
 ┃ ┃ ┗NextFitAlgorithm.cpp             
 ┃ ┣2D Algorithms                      # 2 Dimensional Bin packing algorithms
 ┃ ┃ ┗ShelfNextFit.cpp
 ┃ ┗3D Algorithms                      # 3 Dimensional Bin packing algorithms
 ┃ ┃ ┣3DBinPacking.py
 ┃ ┃ ┣3dalgo-dragos.py
 ┃ ┃ ┗3dalgo-pseudo-initial.py         # Pseudocode used to give the general outline of the algorithm
 ┃ ┗Resources                          # Resources referred for Algorithms
 ┃ ┣RectangleBinPack.pdf
 ┃ ┣3D_Bin_Packing_by_erick_dube.pdf
 ┃ ┗master_thesis on_Bin_Packing.pdf
 ┃
 ┣Assets                          # Contains simulation result videos
 ┃
 ┣Script                          # Contains the scripts used to run the scene
 ┃ ┣zmqRemoteApi                  # Contains the ZMQ API client files
 ┃ ┣Scene_Script.py
 ┃ ┣bp3d_greedy.py
 ┃ ┗bp3d.py
 ┃ 
 ┣Simulation_Scene                                # CoppeliaSim Simulation Scenes 
 ┃ ┣EKLAVYA_PICK_PLACE.ttt
 ┃ ┣Simulation_Multiple Boxes.ttt
 ┃ ┣Simulation_four_boxes.ttt
 ┃ ┗scene_ortho_view.ttt
 ┃
 ┣include                              # Essential add-on files needed for ZMQ-API 
 ┃ ┣cbor.lua
 ┃ ┣simAddOnZmq remote API.lua
 ┃ ┗simZMQ.lua
 ┗README.md
```
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Used [CoppeliaSim](https://www.coppeliarobotics.com/downloads) version 4.2.0
* Tested on Windows 10 and MacOS versions 10.14.6 and 10.15.7
* Used [Anaconda](https://www.anaconda.com/products/individual) for Spyder IDE.

### Installations

1. Clone the repo
```sh
git clone https://github.com/sagarchotalia/Pick-and-Place-Robot-Eklavya.git
```
2. For CoppeliaSim v4.2, Clone [ZMQ API repository](https://github.com/CoppeliaRobotics/zmqRemoteApi) in the `CoppeliaSim/programming` folder.

3. Open the `include` folder of this repository. Add the `simAddOnZMQ remote API.lua` file to your main CoppeliaSim directory (for the add-on).

4. Then navigate to the CoppeliaSim/`lua` folder. Paste the scripts `cbor.lua` and `simZMQ.lua` in them.

5. If there are any files with the same name as the above, simply replace them with the files provided in this repository, otherwise the API will show an error.

6. Install [OpenCV](https://pypi.org/project/opencv-python/) in Spyder Terminal.


### Execution
* Open Spyder IDE using either the directly downloaded application or through Anaconda Navigator.
* Open the scene in Coppeliasim. Don't click on the Play icon, the script contains a function that will run the scene for you.
* Run the `Scene_Script.py` script

![Screenshot 2021-10-19 at 12 26 01 PM](https://user-images.githubusercontent.com/72294682/137859058-2378f94c-d46c-4b11-b86c-37fe697f598c.png)

## Theory and Approach
The main idea of the project is that an item comes packaged inside a box on the conveyor belt, and then gets detected by two specific cameras used for vision sensing (one for the length and breadth and the other for the height and length). Then, using this image data captured by the cameras, the three spatial dimensions of the box are determined by using image processing. After this happens, the conveyor stops and the box is picked up by the gantry components and placed at the desired position coordinates as determined by the bin packing algorithm.

In the script, first we connect with the ZeroMQ API at port 23000. Then, the object handles are accessed (this is required in order to manipulate the specific parts of the robot). After that, the simulation needs to be started and then, inside `object_dimensions` function OpenCV functions need to be used to detect the box dimensions as soon as they come into the frame of the camera. Once the dimensions are determined the `bin packing algorithm` is called and the coordinates returned are used so that the robot places the box at the desired position by using the `pick_place` function.

### Flow of Program
![Flowchart](https://user-images.githubusercontent.com/74896007/138588431-37144891-8cab-4aec-ba02-f05c8a8b598b.png)

### Link to Project Report
[Project Report]

<!-- RESULTS AND DEMO -->
## Results and Demo

![Video](https://user-images.githubusercontent.com/74896007/138588492-3158d8be-6ca7-4847-a6d8-546c2d4bc5e3.mp4)

<!-- FUTURE WORK -->
## Future Work
- [ ] Integrate and test the bin packing algorithm with the scene
- [ ] Add the feature of rotation of boxes for more efficient packing

## Troubleshooting


<!-- CONTRIBUTORS -->
## Contributors
* [Ayush Kaura](https://github.com/Ayush-Kaura)
* [Sagar Chotalia](https://github.com/sagarchotalia)


<!-- ACKNOWLEDGEMENTS AND REFERENCES -->
## Acknowledgements and Resources
* [SRA VJTI](https://github.com/SRA-VJTI/Delta2021)
* [Leopoldo Arnesto YouTube](https://www.youtube.com/watch?v=PwGY8PxQOXY&list=PLjzuoBhdtaXOoqkJUqhYQletLLnJP8vjZ)
* [A great 3D Bin Packing Algorithm Implementation](https://github.com/dragostudorache/3D-Bin-Packing-Text-Based-Python-Script)
* [Erick Dube's Research Paper](https://github.com/enzoruiz/3dbinpacking/blob/master/erick_dube_507-034.pdf) along with [Enzo Ruiz's](https://github.com/enzoruiz/3dbinpacking) insightful repository
* Our seniors and mentors [Dhairya Shah](https://github.com/dhairyashah1) and [Karthik Swaminathan](https://github.com/kart1802)


<!-- -->
## License
[MIT License](https://opensource.org/licenses/MIT)




