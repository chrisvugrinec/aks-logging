FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN mkdir -p /var/log/containers/
CMD ["python", "app.py"]
