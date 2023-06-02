FROM python:3.11.3

WORKDIR /lf_api

COPY ./lf_api /lf_api

RUN pip install --no-cache-dir --upgrade -r requirements.txt
