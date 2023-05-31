FROM ubuntu:18.04

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install locales \
    && apt-get -y install tesseract-ocr \
    && apt-get install -y python3 python3-distutils python3-pip \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 --no-cache-dir install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--master", "-p", "4", "-w", "app:app"]