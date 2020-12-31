import os
import satellite_images_nso.api.nso_georegion as nso

YOUR_USER_NAME_HERE = os.getenv("NSOUsername")
YOUR_PASSWORD_HERE = os.getenv("NSOPassword")
path_geojson = "/src/examples/example.geojson"
# The first parameter is the path to the geojson, the second the map where the cropped satellite data will be installed
georegion = nso.nso_georegion(path_geojson,"/data",\
                              YOUR_USER_NAME_HERE,\
                             YOUR_PASSWORD_HERE)

# This method fetches all the download links to all the satelliet images which contain region in the geojson.
links = georegion.retrieve_download_links()
print(links)

# Execute
georegion.execute_link("https://api.satellietdataportaal.nl/v1/download/SV_RD_11bit_RGBI_200cm/20200915_112331_SV1-04")