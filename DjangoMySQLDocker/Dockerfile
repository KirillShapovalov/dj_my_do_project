FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /dj_my_do
WORKDIR /dj_my_do
ADD requirements.txt /dj_my_do/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /dj_my_do/
