from alpine

MAINTAINER Itay Haike

RUN apk add --update python3

RUN apk add git

WORKDIR /home

CMD ["python3", "py.py" > OUTPUT.log
CMD ["python3", "py.py"]
