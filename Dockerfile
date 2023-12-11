# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM arm32v7/python:3.10-buster

# RUN apt-get update 
# RUN apt-get install -y python3-numpy
# RUN apt-get install -y python3-pandas

FROM arm32v7/python:3.9-slim


# Allows docker to cache installed dependencies between builds

# RUN apt-get update 
# RUN apt-get install -y python3-pandas
COPY requirements.txt requirements.txt
 
# RUN pip install --upgrade pip setuptools 

RUN pip install --index-url=https://www.piwheels.org/simple --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 5555

# runs the production server
ENTRYPOINT ["python", "graph/manage.py"]
CMD ["runserver", "0.0.0.0:5555"]
