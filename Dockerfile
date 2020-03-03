
FROM ubuntu:18.04 
MAINTAINER YOHEI_KUMAGAI

# utils
RUN apt-get update
RUN apt-get install -y \ 
           wget \
           tar \
           gcc \
           g++ \
           make \
           zlib1g-dev \
           gzip \
           bzip2 \
           cmake \
           python \
           git \
           unzip \
           cwltool \
           vim \
           sudo \
           --no-install-recommends

# change git config
RUN git config --global http.sslVerify false

# install megahit
WORKDIR /root
RUN git clone https://github.com/voutcn/megahit.git
WORKDIR megahit
RUN git submodule update --init
RUN mkdir build
WORKDIR build
RUN cmake -DUSE_BMI2=OFF -DCMAKE_BUILD_TYPE=release ..
RUN make -j4
ENV PATH $PATH:/root/megahit/build/

# python
WORKDIR /root
RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz --no-check-certificate
RUN tar xzvf Python-3.5.2.tgz

WORKDIR ./Python-3.5.2
RUN ./configure --with-threads
RUN make install

RUN wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
RUN python get-pip.py
WORKDIR /root

# TrimGalore
WORKDIR /root
RUN wget https://github.com/FelixKrueger/TrimGalore/archive/0.5.0.zip --no-check-certificate 
RUN unzip 0.5.0.zip && rm 0.5.0.zip
ENV PATH $PATH:/root/TrimGalore-0.5.0

#FLASh
WORKDIR /root
RUN wget http://ccb.jhu.edu/software/FLASH/FLASH-1.2.11-Linux-x86_64.tar.gz --no-check-certificate
RUN tar -xvf  FLASH-1.2.11-Linux-x86_64.tar.gz
RUN rm FLASH-1.2.11-Linux-x86_64.tar.gz
ENV PATH $PATH:/root/FLASH-1.2.11-Linux-x86_64

# BOWTIE2
WORKDIR /root
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.3/bowtie2-2.3.4.3-linux-x86_64.zip --no-check-certificate
RUN unzip bowtie2-2.3.4.3-linux-x86_64.zip
RUN rm bowtie2-2.3.4.3-linux-x86_64.zip
ENV PATH $PATH:/root/bowtie2-2.3.4.3-linux-x86_64

# install prinseq
WORKDIR /root
RUN wget https://sourceforge.net/projects/prinseq/files/standalone/prinseq-lite-0.20.4.tar.gz --no-check-certificate
RUN tar xzvf prinseq-lite-0.20.4.tar.gz
RUN chmod 777  /root/prinseq-lite-0.20.4/prinseq-lite.pl
ENV PATH $PATH:/root/prinseq-lite-0.20.4

# install pip3
RUN apt-get install -y python-pip python3-pip
ENV PYTHONPATH "${PYTHONPATH}:/usr/local/lib/python3.6/dist-packages"

# cutadapt (for TrimGalore)
WORKDIR /root
RUN pip3 install cutadapt

# install in-house pipeline
WORKDIR /root
RUN pip3 install pathlib
RUN git  clone https://github.com/kmooog/metagenome-pipeline.git 

# Prodigal
WORKDIR /root
RUN git clone https://github.com/hyattpd/Prodigal.git
WORKDIR /root/Prodigal
RUN make install
WORKDIR /root

# add permission
WORKDIR /
RUN chmod 777 root
