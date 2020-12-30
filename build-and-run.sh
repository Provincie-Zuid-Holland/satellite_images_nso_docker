docker build . -t satellite-images-nso --no-cache
docker run -it --entrypoint bash satellite-images-nso