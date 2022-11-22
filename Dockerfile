FROM ubuntu
RUN apt-get update && apt-get install -y software-properties-common gcc && \
add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install --upgrade pip
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt
CMD python -u /app/src/run.py
# Sample commands to push the docker image file to docker hub.
# docker build -t gabrieldeoliveiraest/projetofinal2_web:latest -f Dockerfile .
# docker login -u "gabrieldeoliveiraest" -p "password" docker.io
# docker push gabrieldeoliveiraest/projetofinal2_web:latest
