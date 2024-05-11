FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install build-essential -y
RUN apt install clang -y
RUN apt install gnuplot -y
RUN apt install python3-numpy -y


WORKDIR /usr/src/app
