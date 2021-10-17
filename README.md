

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

--------------------

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

4. Go to the CoppeliaSim application. Right click on it and click on ```Show Package Contents```. Navigate to the ```Programming``` folder and paste the cloned repository in it.

5. *further points to be added*

### Execution
* Open Spyder IDE using either the directly downloaded application or through Anaconda Navigator.
* Open the scene in Coppeliasim. Don't click on the Play icon, the script contains a function that will run the scene for you.
* Run the *scene.py script* (yet to upload)

*Insert GIF/Image of the overall setup*

<!-- RESULTS AND DEMO -->
## Results and Demo
*Add the videos, gifs and other things here*

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
