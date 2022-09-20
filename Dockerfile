from alpine

MAINTAINER ItayHaike@gmail.com
#Install python
RUN apk add --update python3
#Install git
RUN apk add git

WORKDIR /home

COPY . .

CMD ["python3", "py.py" > OUTPUT.log ]
CMD ["python3", "py.py"]
