import pandas
from geopy.geocoders import ArcGIS


df = pandas.read_csv("supermarkets.csv")
nom = ArcGIS()

df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]
df["Coordinates"] = df["Address"].apply(nom.geocode)
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x is not None else None)
df.drop("Coordinates", 1, inplace=True)
print(df)
print()
print(df["Latitude"])
print(df["Longitude"])

# nom = ArcGIS()
# n = nom.geocode("3995 23rd St, San Francisco, CA 94114")



