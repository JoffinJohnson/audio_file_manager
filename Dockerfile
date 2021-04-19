#init a base image (alphine is the small of linux destro)
FROM python:3.8-alpine
#deffine the present working directory
WORKDIR /docker-flask-test
#copy contents to working directory
#ADD . /docker-flask-test
COPY . /docker-flask-test
#run pip install, all dependencies for the flask application
RUN pip install -r requirements.txt
#define command to stat the container
CMD ["python","app.py"]