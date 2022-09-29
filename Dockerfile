from alpine

MAINTAINER ItayHaike@gmail.com
#Install python
RUN apk add --update python3

WORKDIR /home

COPY . .

CMD ["python3", "py.py" > OUTPUT.log ]

