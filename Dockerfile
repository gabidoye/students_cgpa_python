#Deriving the latest base image
FROM python:3.10


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/gpa_app

#to COPY the remote file at working directory in container
COPY . . 
# Now the structure looks like this '/usr/app/src/test.py'

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt



#ENTRYPOINT instruction should be used to run the software
#contained by your image, along with any arguments.

ENTRYPOINT [ "python", "./entry.py"]