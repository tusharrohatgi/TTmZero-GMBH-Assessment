FROM python:3.6.1-alpine



RUN mkdir /code
WORKDIR /code
RUN pip install  allure-pytest
RUN pip install  pytest
RUN pip install  requests
RUN pip install allure-python-commons

COPY . /code/
RUN pytest --alluredir="/code/report"  /code/http_test.py

