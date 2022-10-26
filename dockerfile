
FROM python:3.10-slim-buster

COPY ./app/ .
COPY ./app/src/ .

RUN python -m pip install --upgrade pip

RUN pip install pandas
RUN pip install numpy
RUN pip install plotly
RUN pip install dash
RUN pip install dash_bootstrap_components
RUN pip install sklearn
RUN pip install xgboost

EXPOSE 8050:8050
CMD ["python", "/main.py"]
