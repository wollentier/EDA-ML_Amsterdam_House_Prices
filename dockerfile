
FROM python:3.9.8-slim-buster

#RUN pip install joblib

COPY ./app/src/ .
WORKDIR /app

RUN python -m pip install --upgrade pip

#RUN pip install --upgrade protobuf==3.20.0
#RUN pip install fastapi
#RUN pip install uvicorn
RUN pip install gunicorn
RUN pip install pandas
RUN pip install numpy
RUN pip install plotly
RUN pip install dash
RUN pip install dash_bootstrap_components
#RUN pip install sklearn
#RUN pip install xgboost


#EXPOSE 8000:8000
#EXPOSE 8050
#CMD ["gunicorn", "-b", "0.0.0.0:8050", "--reload", "app:server"]
CMD ["gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "app:server"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]