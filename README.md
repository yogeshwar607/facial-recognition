# STUDIOS

AI based utility for facial recognition in disguise and crowd

### Docker Steps

1. To build Docker image, run `docker build -f src/Dockerfile -t face_recognizer src/`.
2. To capture images, run `docker run -it face_recognizer "create_input_images.py"`.
3. To run the face recognizer, run `docker run -it face_recognizer`.

### Steps to Install -

1. Open your project `../Documents/STUDIOS` in VSCode
2. Tap Extensions from left panel in VSCode, install -
   1. Docx Viewer/Reader
   2. vscode-pdf
   3. OR instead install "Office Viewer(Markdown Editor)" for all type of file viewing
   4. Jupyter
3. Open terminal and install necessary libraries -
   1. Install Python from [here](https://www.python.org/downloads/release/python-31011/). Follow the instructions after file download.
   2. To check if Python is downloaded correctly run - `python3 --version`
   3. Install Python Package Installer - `pip3 install --upgrade pip`
   4. Check if it installed by running - `pip3 --version`
   5. Install Conda environment manager from [here](https://docs.conda.io/en/latest/miniconda.html)
      - Download required miniconda
      - In terminal, run - `bash ../Downloads/Miniconda3-latest-MacOSX-x86_64.sh`
      - Reload the terminal once, check if conda is installed by `conda --version`
      - Set conda base to inactivate on launch - `conda config --set auto_activate_base false`
   6. Create new conda environment with python 3.10 - `conda create -n face_env python=3.10`
   7. Activate the newly created environment - `conda activate face_env`
   8. Install tensorflow in MacOS using - `SYSTEM_VERSION_COMPAT=0 pip install tensorflow-macos tensorflow-metal`
   9. Check tensorflow version - `python3 -c "import tensorflow as tf; print(tf.__version__)"`
   10. Install all other libs by `pip install -r requirements.txt`
4. Before running a cell in Jupyter notebook select interpreter for Jupyter -
   1. Form your VSCode Command Palette (Shift+Command+P), search and then choose

      ``Jupyter: Select Interpreter to Start Jupyter Server``
   2. You should then select the python version that is associated to your conda environment (face_env).


To build

docker build -f src/Dockerfile -t face_recognizer src/


To train new face

xhost + && docker run -it --rm --privileged --pid=host -e "DISPLAY=$DISPLAY" -e "QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --volume "$(pwd)/src/images:/usr/src/app/images:rw" --device="/dev/video0:/dev/video0" --device="/dev/video1:/dev/video1" face_recognizer "create_input_images.py"


To recognise trained face

xhost + && docker run -it --rm --privileged --pid=host -e "DISPLAY=$DISPLAY" -e "QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --volume "$(pwd)/src/images:/usr/src/app/images:rw" --device="/dev/video0:/dev/video0" --device="/dev/video1:/dev/video1" face_recognizer "main.py"
# ai-camera-detection
