FROM ubuntu:18.04

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV DEBIAN_FRONTEND noninteractive

# Various Python and C/build deps
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    libc-dev \
    cmake \
    git \
    unzip \
    pkg-config \
    python-dev \
    python-opencv \
    libopencv-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libgtk2.0-dev \
    python-numpy \
    python-pycurl \
    libatlas-base-dev \
    gfortran \
    webp \
    qt5-default \
    libvtk6-dev \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    python3 \
    python3-pip \
    python-dev

RUN pip3 install numpy matplotlib

# Install Open CV - Warning, this takes absolutely forever
RUN mkdir -p ~/opencv && cd ~/opencv && \
    wget https://github.com/Itseez/opencv/archive/3.4.0.zip && \
    unzip 3.4.0.zip && \
    rm 3.4.0.zip && \
    mv opencv-3.4.0 OpenCV && \
    cd OpenCV && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=ON -D CUDA_ARCH_BIN="6.2" -D CUDA_ARCH_PTX="" \
    -D WITH_CUBLAS=ON -D ENABLE_FAST_MATH=ON -D CUDA_FAST_MATH=ON \
    -D ENABLE_NEON=ON -D WITH_LIBV4L=ON -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF -D BUILD_EXAMPLES=OFF -D BUILD_opencv_python3=yes \
    -D WITH_QT=ON -D WITH_OPENGL=ON .. && \
    make -j4 && \
    make install && \
    ldconfig