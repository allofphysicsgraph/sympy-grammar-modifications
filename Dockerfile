# docker build . -t 'sympy_antlr'
# docker run -it --rm sympy_antlr:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch sympy_antlr:latest /bin/bash
# docker run -it --rm -v `pwd`:/scratch sympy_antlr:latest python3 generate_latex_files.py

# as of 20200520, the build process takes 20 minutes on BHP's mac

# https://github.com/phusion/baseimage-docker
# https://hub.docker.com/r/phusion/baseimage/tags
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
#Java Runtime for Antlr4
               default-jre \
    && rm -rf /var/lib/apt/lists/*
    
RUN echo "alias python=python3" > /root/.bashrc
#RUN python3 setup.py install

RUN ln -s /usr/bin/python3.6 /usr/bin/python

# the purpose of grabbing AMSmath is because bhp thinks the symbols to be parsed exist in the source
# https://ctan.org/pkg/amsmath?lang=en
RUN find /opt -type f 


WORKDIR /opt/
# download the sympy source to /opt/
RUN git clone https://github.com/sympy/sympy.git

# BHP -- this probably isn't necessary since ANTLR is built from source?
WORKDIR /opt/
RUN pip3 install antlr4-python3-runtime==4.7.1 mpmath
# layer the local ANTLR modifications on top of the sympy source in /opt/
COPY sympy/parsing/latex/_antlr/LaTeX.g4 /opt/sympy/sympy/parsing/latex
COPY sympy/parsing/latex/_antlr/rename.py /opt/sympy/sympy/parsing/latex
COPY _parse_latex_antlr.py /opt/sympy/sympy/parsing/latex
COPY sympy/parsing/tests /opt/sympy/sympy/parsing/

WORKDIR /opt/sympy
RUN python3 setup.py install



WORKDIR /opt/
COPY generate_latex_files.py /opt/
RUN mkdir /opt/amsmath
COPY amsmath /opt/amsmath
COPY antlr-4.7.1-complete.jar /usr/local/lib/
COPY data.json /opt/
