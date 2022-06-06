import phonenumbers
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print("Country in which the phone number is located : \n{}".format(geocoder.description_for_number(ch_number, "en")))

from phonenumbers import carrier
serviceNumber = phonenumbers.parse(number, "RO")
print("\nNetwork Carrier in which the phone number is registered : \n{}".format(carrier.name_for_number(serviceNumber, "en")))