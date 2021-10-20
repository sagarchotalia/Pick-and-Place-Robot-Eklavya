

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
* [Results and Demo](#results-and-demo)
* [Future Work](#future-work)
* [Contributors](#contributors)
* [Acknowledgements and Resources](#acknowledgements-and-resources)
* [License](#license)


<!-- ABOUT THE PROJECT -->
## About The Project
Bin packing is one of the most interesting problems in combinatorics. It has multiple applications, such as packaging boxes in containers, loading trucks with weight capacity constraints, creating file backups in media and technology mapping in FPGA semiconductor chip design.

## Tech Stack
- [CoppeliaSim](https://www.coppeliarobotics.com/downloads)
- [Spyder](https://www.spyder-ide.org/)

### File Structure
```sh

 ┣API Scripts                          #Contain the scripts used to run the scene
 ┃ ┣scene.py
 ┃ ┗scene_1.py
 ┣Algorithms                           #The various algorithms we wrote and tested
 ┃ ┣1D Algorithms                      #1 Dimensional bin packing algorithms
 ┃ ┃ ┣BestFitAlgorithm.cpp             
 ┃ ┃ ┣FirstFitAlgorithm.cpp            
 ┃ ┃ ┗NextFitAlgorithm.cpp             
 ┃ ┣2D Algorithms                      #2 Dimensional bin packing algorithms
 ┃ ┃ ┗ShelfNextFit.cpp
 ┃ ┗3D Algorithms                      #3 Dimensional bin packing algorithms
 ┃ ┃ ┣3DBinPacking.py
 ┃ ┃ ┣3dalgo-dragos.py
 ┃ ┃ ┗3dalgo-pseudo-initial.py         #Pseudocode used to give the general outline of the algorithm
 ┣Resources                            #Resources that we referred to throughout the entire project
 ┃ ┣RectangleBinPack.pdf
 ┃ ┣erick_dube_507-034.pdf
 ┃ ┗master_sorset.pdf
 ┣Scene                                #CoppeliaSim scenes containing the Inverse-Kinematic(IK) set up
 ┃ ┣EKLAVYA_PICK_PLACE.ttt
 ┃ ┗coppeliasim_scene.ttt
 ┣include                              #Essential add-on files needed to run the scene
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
* Used [Anaconda Navigator](https://www.anaconda.com/products/individual) for Spyder IDE.

### Installations

1. Clone the repo
```sh
git clone https://github.com/sagarchotalia/Pick-and-Place-Robot-Eklavya.git
```
2. Clone [this repo.](https://github.com/CoppeliaRobotics/zmqRemoteApi)

4. Go to the CoppeliaSim application. Right click on it and click on `Show Package Contents`. Navigate to the `Programming` folder and paste the cloned repository in it.

5. Open the `include` folder of this repository. Add the `simAddOnZMQ remote API.lua` file to your main CoppeliaSim directory(i.e. CoppeliaSim->Show Package Contents->Paste the file there).

6. Then navigate to the CoppeliaSim/`lua` folder. Paste the scripts `cbor.lua` and `simZMQ.lua` in them.

7. If there are any files with the same name as the above, simply replace them with the files provided in this repository, otherwise the API will show an error.


### Execution
* Open Spyder IDE using either the directly downloaded application or through Anaconda Navigator.
* Open the scene in Coppeliasim. Don't click on the Play icon, the script contains a function that will run the scene for you.
* Run the `scene.py` script

![Screenshot 2021-10-19 at 12 26 01 PM](https://user-images.githubusercontent.com/72294682/137859058-2378f94c-d46c-4b11-b86c-37fe697f598c.png)


<!-- RESULTS AND DEMO -->
## Results and Demo
*Add the videos, gifs and other things here*

![gif](https://user-images.githubusercontent.com/72294682/137859720-8dc0fd73-55f4-48ea-990b-08e399e0937e.gif)

<!-- FUTURE WORK -->
## Future Work
- [ ] Integrate and test the bin packing algorithm with the scene
- [ ] Add the feature of rotation of boxes for more efficient packing

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
