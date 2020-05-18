# docker build . -t 'sympy'
# docker run -it --rm sympy:latest /bin/bash

# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.11

RUN apt-get update && \
    apt-get install -y \
# text editing
               vim \
# python 3
               python3 \
               python3-pip \
               python3-dev \
# distributed version control
               git \
# download files from the internet
               wget \
# latex
               texlive \
# file compression
               zip \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/local/lib

RUN curl -O https://www.antlr.org/download/antlr-4.8-complete.jar

WORKDIR /opt/

RUN git clone https://github.com/sympy/sympy.git

COPY sympy /opt/sympy/

WORKDIR /opt/sympy
RUN echo "alias python=python3" > /root/.bashrc

RUN python setup.py install

RUN pip3 install antlr4-python3-runtime mpmath
RUN pip3 install ipython
# https://ctan.org/pkg/amsmath?lang=en
RUN wget http://mirrors.ctan.org/macros/latex/required/amsmath.zip
#RUN mv amsmath.zip /opt/
RUN unzip /opt/amsmath.zip

COPY generate_latex_files.py /opt/


