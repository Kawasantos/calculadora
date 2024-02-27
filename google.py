import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='SUA_CHAVE_DE_API_AQUI')

# Geocodificação de um endereço
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Resultado
print(geocode_result)