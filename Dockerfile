# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim-buster 

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt

RUN sudo apt-get -y install cmake
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 5555

# runs the production server
ENTRYPOINT ["python", "graph/manage.py"]
CMD ["runserver", "0.0.0.0:5555"]
