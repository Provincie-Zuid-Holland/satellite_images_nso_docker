# satellite_images_nso_docker
Environment to run `satellite_images_nso` python package in (based on GDAL).

# TL;DR - Interactive bash
```console
docker run -it --entrypoint bash dockerhubpzh/satellite_images_nso_docker
python
```
```python
YOUR_USER_NAME_HERE = ""
YOUR_PASSWORD_HERE = ""
import satellite_images_nso.api.nso_georegion as nso
path_geojson = "/src/examples/example.geojson"
# The first parameter is the path to the geojson, the second the map where the cropped satellite data will be installed
georegion = nso.nso_georegion(path_geojson,"/src/output/",\
                              YOUR_USER_NAME_HERE,\
                             YOUR_PASSWORD_HERE)

# This method fetches all the download links to all the satelliet images which contain region in the geojson.
links = georegion.retrieve_download_links()
print(links)
```


# DockerHub
https://hub.docker.com/r/dockerhubpzh/satellite_images_nso_docker