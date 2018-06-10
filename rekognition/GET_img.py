import requests

def get_image_from_url(imgurl):
    resp = requests.get(imgurl)
    imgbytes = resp.content
    return imgbytes

def get_image_from_file(filename):
    with open(filename, 'rb') as imgfile:
        return imgfile.read()