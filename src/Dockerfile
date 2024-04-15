FROM python:3.10

ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONBUFFERED=1

RUN apt-get update -y && apt-get install -y \
    ffmpeg \
    libdbus-1-3 \
    libfontconfig1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libglu1 \
    libgtk2.0-dev \
    libopencv-dev \
    libsm6 \
    libx11-xcb-dev \
    libxcb1 \
    libxcb-glx0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-util1 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-xinput0 \
    libxext6 \
    libxi6 \
    libxkbcommon-x11-0 \
    libxrender1 \
    mesa-utils \
    pkg-config \
    python3-opencv \
    x11-common \
    x11-apps

RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
