FROM python:3.11.3

WORKDIR /lf_server

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /lf_server

