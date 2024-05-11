FROM ubuntu:latest

RUN apt update
RUN apt install python3-matplotlib -y
RUN apt install build-essential -y
RUN apt install clang -y

WORKDIR /usr/src/app
