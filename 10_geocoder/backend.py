import pandas as pd
from geopy.geocoders import Nominatim


def add_lat_lon(local_filename):
    data = pd.read_csv(local_filename)
    data.columns = map(str.lower, data.columns)
    try:
        addresses = data['address']
    except KeyError:
        print('Neither address nor Address is a column in uploaded csv')
        return False

    geolocator = Nominatim()
    lats, longs = [], []
    for address in addresses:
        location = geolocator.geocode(address)
        if location is None:
            lats.append('N/A')
            longs.append('N/A')
        else:
            lats.append(location.latitude)
            longs.append(location.longitude)

    data['latitude'] = lats
    data['longitude'] = longs
    data.to_csv(local_filename, index=False)

    return True
