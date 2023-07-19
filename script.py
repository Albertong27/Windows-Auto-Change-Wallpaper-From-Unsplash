# Another project by Albert
# Please share if you think this is useful
# https://github.com/Albertong27/Windows-Auto-Change-Wallpaper-From-Unsplash

import requests
import json
import urllib.request
import ctypes
import os

API_KEY = '{Put Your API Key Here}'
ENDPOINT = 'https://api.unsplash.com/photos/random?orientation=landscape&query=nature'

response = requests.get(ENDPOINT, headers={'Authorization': 'Client-ID ' + API_KEY})
data = json.loads(response.text)
image_url = data['urls']['raw']
print(image_url)
urllib.request.urlretrieve(image_url, filename='temp.jpg')

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, os.path.abspath('temp.jpg'), 0x01 | 0x02)

