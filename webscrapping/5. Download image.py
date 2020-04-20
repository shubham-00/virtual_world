import urllib.request

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Glatt_-_Glattbrugg_IMG_6869.jpg/1200px-Glatt_-_Glattbrugg_IMG_6869.jpg'

urllib.request.urlretrieve(url, 'image.jpg')

