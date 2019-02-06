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

# cutadapt(for TrimGalore)
RUN pip install --user --upgrade cutadapt

# TrimGalore
RUN wget https://github.com/FelixKrueger/TrimGalore/archive/0.5.0.zip 
RUN unzip 0.5.0.zip && rm 0.5.0.zip
ENV PATH $PATH:/TrimGalore-0.5.0


CMD ["bash"]
VOLUME /mydata



