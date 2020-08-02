#set base image (host os)
FROM python:3.8

#set the working dir in the container
WORKDIR /code

#copy the dependencies file to the working dir 
COPY requirements.txt .

# install dependendencies
RUN pip install -r requirements.txt

# copy source code to the working dir 
COPY src/ .

# command to run on container start 
CMD [ "python" ,"./app.py" ]
