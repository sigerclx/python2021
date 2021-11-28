from pygeocoder import Geocoder
from urllib.parse import quote_plus
# if __name__ == '__main__':
#     address ='207 N. Defiance St,Archbold,OH'
#     print(Geocoder.geocode(address)[0].coordnates)

address ='207 N. Defiance St,Archbold,OH'
base ='123'
path = '{}?address={}&sen={}'.format(base,address,'hello')
print(path)