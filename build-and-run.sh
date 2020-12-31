docker build . -t satellite-images-nso #--no-cache
# docker run -it --entrypoint bash satellite-images-nso
docker run --env-file .env --mount type=bind,src="${PWD}/data",dst=/data satellite-images-nso 