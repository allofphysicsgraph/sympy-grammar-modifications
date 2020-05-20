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
WORKDIR /usr/local/lib

# msg says this is is needed to build the ANTLR grammar
RUN curl -O https://www.antlr.org/download/antlr-4.8-complete.jar

WORKDIR /opt/

# download the sympy source to /opt/
RUN git clone https://github.com/sympy/sympy.git

# layer the local ANTLR modifications on top of the sympy source in /opt/
COPY sympy /opt/sympy/



RUN echo "alias python=python3" > /root/.bashrc
#RUN python3 setup.py install

WORKDIR /opt/
RUN pip3 install antlr4-python3-runtime mpmath

COPY sympy/parsing/latex/_antlr/LaTeX.g4 /opt/sympy/sympy/parsing/latex
COPY sympy/parsing/latex/_antlr/rename.py /opt/sympy/sympy/parsing/latex
COPY sympy/parsing/latex/_antlr/antlr_build.sh /opt/sympy/sympy/parsing/latex

WORKDIR /opt/sympy/sympy/parsing/latex
RUN /bin/bash antlr_build.sh

WORKDIR /opt/
# msg uses ipython for the REPL inside the container
RUN pip3 install ipython

# the purpose of grabbing AMSmath is because bhp thinks the symbols to be parsed exist in the source
# https://ctan.org/pkg/amsmath?lang=en
RUN wget http://mirrors.ctan.org/macros/latex/required/amsmath.zip
#RUN mv amsmath.zip /opt/
RUN unzip /opt/amsmath.zip

COPY generate_latex_files.py /opt/

