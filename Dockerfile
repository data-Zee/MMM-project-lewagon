FROM python:3.10.6-buster

WORKDIR /prod

COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY MMM-project-lewagon MMM-project-lewagon
COPY setup.py setup.py
RUN pip install .

# CMD uvicorn MMM-project-lewagon.api.fast:app --host 0.0.0.0 --port $PORT
