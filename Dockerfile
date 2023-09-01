FROM python:3.10.6-buster

WORKDIR /prod

COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY mmmproject mmmproject
COPY pipelines pipelines
COPY setup.py setup.py
#COPY mmm-lewagon-project-75c770847cb8.json mmm-lewagon-project-75c770847cb8.json
RUN pip install .
#RUN mkdir models

CMD uvicorn mmmproject.api.main:app --host 0.0.0.0 --port $PORT
