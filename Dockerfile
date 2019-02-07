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
wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.3/bowtie2-2.3.4.3-source.zip
RUN unzip bowtie2-2.3.4.3-source.zip
RUN rm bowtie2-2.3.4.3-source.zip


CMD ["bash"]
VOLUME /mydata



