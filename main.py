import phonenumbers
import opencage
import folium
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_number, "en")
print("\nCountry in which the phone number is located : {}".format(location))

from phonenumbers import carrier
serviceNumber = phonenumbers.parse(number)
print("Network Carrier in which the phone number is registered : {}".format(carrier.name_for_number(serviceNumber, "en")))

from opencage.geocoder import OpenCageGeocode

key = '95ece0f4dd4b48e9bab9f8f619a21e93'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lag = results[0]['geometry']['lng']

print(lat,lag)

myMap = folium.Map(location=[lat, lag], zoom_start= 9)
folium.Marker([lat, lag], popup=location).add_to(myMap)

myMap.save("mylocation.html")