from alpine

MAINTAINER Itay Haike

RUN apk add --update add python3

RUN apk add git

WORKDIR /home

RUN python3 py.py > OUTPUT_PYTHON
