import glob
from PIL import Image, ImageFile, ExifTags
import json
from geopy.geocoders import ArcGIS
ImageFile.LOAD_TRUNCATED_IMAGES = True


GEO_KEY = 34853
ROT_KEY = 274
COUNTRIES = {"ESP": "Spain", "GBR": "United Kingdom", "FRA": "France", "USA": "United States"}


def get_coords(geo):
    lat_dms = geo[2]
    lat = lat_dms[0][0] / lat_dms[0][1]
    lat += lat_dms[1][0] / lat_dms[1][1] / 60.0
    lat += lat_dms[2][0] / lat_dms[2][1] / 3600.
    if geo[1] == 'S':
        lat *= -1

    lon_dms = geo[4]
    lon = lon_dms[0][0] / lon_dms[0][1]
    lon += lon_dms[1][0] / lon_dms[1][1] / 60.0
    lon += lon_dms[2][0] / lon_dms[2][1] / 3600.
    if geo[3] == 'W':
        lon *= -1

    return lat, lon


def downsample(im, exif, file):
    scale = max(max(im.size) / 800, 1)
    dest_im = im.resize(tuple(int(dim / scale) for dim in im.size))
    dest_im = rotate_image(dest_im, exif)
    dest_file = file.replace("source", "downsampled")
    dest_im.save(dest_file)
    return dest_file


def rotate_image(image, exif):
    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    return image


def update_world_json(visited):
    with open('world.json', 'r', encoding="utf-8-sig") as f:
        data = json.load(f)

    for point in data['features']:
        if point['properties']['NAME'] in visited:
            point['properties']['visited'] = True
        else:
            point['properties']['visited'] = False

    json_str = json.dumps(data)
    with open("world.json", 'w') as jf:
        jf.write(json_str)


json_str = []
visited = []
geo = ArcGIS()
for file in glob.glob(r"pics\source\*"):
    im = Image.open(file)
    exif = im._getexif()
    if exif is not None:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation': break
        geo_data = exif[GEO_KEY]
        if 2 in geo_data.keys():
            coords = get_coords(geo_data)  # get lat, lon
            down_file = downsample(im, exif, file)  # make sure image is not more than 800px in a direction
            json_str.append({"lat": coords[0], "lon": coords[1], "file": down_file})  # add to image json
            country = COUNTRIES[geo.reverse(coords).address.split(',')[-1].strip()]  # get long form of country
            if country not in visited:  # add to visited countries if not already there
                visited.append(country)

        else:
            print(f"No coordinates for {file}")
    else:
        print(f"No metadata for {file}")

update_world_json(visited)  # update world json with current visits

with open("image_data.json", "w") as jf:  # save image json
    jf.write(json.dumps(json_str))
