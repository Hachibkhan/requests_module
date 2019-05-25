import requests

import sys

base_url = "http://subeen.com/download/"

info_dt = {"name": "Subeen", "email": "subeen@gmail.com", "country": "Bangladesh"}

url = base_url + "process.php"

response = requests.post(url, data=info_dt)

if response.ok is False:

    sys.exit("Error downloading the file")

with open("cpbbok.pdf", "wb") as f:

    f.write(response.content)

print("Book download complete!")


