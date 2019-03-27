FROM centos:latest 
MAINTAINER YOHEI_KUMAGAI

# utils
RUN yum -y install \ 
           kernel-devel \
           kernel-headers \
           gcc-c++ \
           patch \
           libyaml-devel \
           libffi-devel \
           autoconf \
           automake \
           make \
           libtool \
           bison \
           tk-devel \
           zip \
           wget \
           tar \
           gcc \
           zlib \
           unzip \
           zlib-devel \
           bzip2 \
           bzip2-devel \
           readline \
           readline-devel \
           sqlite \
           sqlite-devel \
           openssl \
           openssl-devel \
           git \
           gdbm-devel \
           python-devel

# install cmake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0.tar.gz
RUN tar xzvf cmake-3.14.0.tar.gz
RUN cd cmake-3.14.0
RUN ./bootstrap
RUN make
RUN make install

# update gcc

RUN yum install centos-release-scl -y
RUN yum install scl-utils -y
RUN yum install devtoolset-7-gcc devtoolset-7-gcc-c++ devtoolset-7-binutils -y
RUN scl enable devtoolset-7 bash


# python
WORKDIR /root
RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
RUN tar xzvf Python-3.5.2.tgz

WORKDIR ./Python-3.5.2
RUN ./configure --with-threads
RUN make install

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
WORKDIR /root

# cutadapt(for TrimGalore)
RUN pip install --user --upgrade cutadapt

# TrimGalore
RUN wget https://github.com/FelixKrueger/TrimGalore/archive/0.5.0.zip 
RUN unzip 0.5.0.zip && rm 0.5.0.zip
ENV PATH $PATH:/TrimGalore-0.5.0

#FLASh
RUN wget http://ccb.jhu.edu/software/FLASH/FLASH-1.2.11-Linux-x86_64.tar.gz
RUN tar -xvf  FLASH-1.2.11-Linux-x86_64.tar.gz
RUN rm FLASH-1.2.11-Linux-x86_64.tar.gz
ENV PATH $PATH:/FLASH-1.2.11-Linux-x86_64

# BOWTIE2
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.3/bowtie2-2.3.4.3-linux-x86_64.zip
RUN unzip bowtie2-2.3.4.3-linux-x86_64.zip
RUN rm bowtie2-2.3.4.3-linux-x86_64.zip
ENV PATH $PATH:/bowtie2-2.3.4.3-linux-x86_64

# MEGAHIT ## G++のインストールが必要っぽいが一旦飛ばす
#RUN git clone https://github.com/voutcn/megahit.git
#WORKDIR ./megahit
#make
#WORKDIR ./

#WORKDIR ./
#CMD ["bash"]
#VOLUME /mydata

# install megahit
RUN git clone https://github.com/voutcn/megahit.git
RUN cd megahit
RUN git submodule update --init
RUN mkdir build && cd build
RUN cmake -DUSE_BMI2=OFF -DCMAKE_BUILD_TYPE=release ..
RUN make -j4


