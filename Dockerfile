FROM ubuntu
MAINTAINER YOHEI_KUMAGAI
RUN apt-get update && apt-get install -y wget
RUN apt-get install unzip
RUN wget https://github.com/FelixKrueger/TrimGalore/archive/0.5.0.zip 
RUN unzip 0.5.0.zip && rm 0.5.0.zip
ENV PATH $PATH:/TrimGalore-0.5.0
CMD ["bash"]




