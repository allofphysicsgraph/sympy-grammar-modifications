# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.11

RUN apt-get update && \
    apt-get install -y \
# text editing
               vim \
               python3 \
               python3-pip \
               python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/

RUN git clone https://github.com/sympy/sympy.git
