FROM osgeo/gdal:latest

RUN apt-get update
RUN apt-get -y install python3-pip 

RUN python -m pip install satellite-images-nso

COPY src /src

CMD ["python", "/src/main.py"]