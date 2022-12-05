FROM ubuntu
RUN apt-get update && apt-get install -y software-properties-common gcc && \
add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN ln -s /usr/bin/python3 /usr/bin/python
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN python3 -m pip install -r requirements.txt
#1. Sample commands to push the docker image file to docker hub.
## docker build -t gabrieldeoliveiraest/projetofinal2_web:latest -f Dockerfile .
## docker login -u "gabrieldeoliveiraest" -p "password" docker.io
## docker push gabrieldeoliveiraest/projetofinal2_web:latest
#2. Sample commands to build cross-platform images
## docker buildx create --use
## docker buildx build --platform linux/amd64,linux/arm64 --push -t vishnuchalla007/docker-se:latest .