FROM tensorflow/tensorflow:1.5.0-py3

COPY requirements.txt /

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC

RUN apt update && apt install -y libsm6 libxext6 libxrender-dev

RUN apt install python3 -y

RUN apt install python3-pip -y

RUN pip3 install pytest

RUN apt install make -y

RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

RUN make extract-data
RUN make train-model

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 webserver:app
