from alpine

MAINTAINER Itay Haike

RUN apk add --update python3

RUN apk add git

WORKDIR /home

RUN python3 py.py > OUTPUT_PYTHON.log
CMD ["python3", "py.py"]
