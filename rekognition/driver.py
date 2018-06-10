import boto3
import GET_img
import json
from pprint import pprint

def get_labels(thumbImg, client):

	img_size = GET_img.get_image_from_url(thumbImg)

	labels = []

	try:
		resp = client.detect_labels(Image={'Bytes': img_size}, MinConfidence=60.0)

		for label in resp['Labels']:
			labels.append(label['Name'])

	except :
		return labels

	return labels


with open('data.json') as f:
	data = json.load(f)

with open("cre") as f:
	for line in f:
		if line[0] == 'A':
			ACCESS_KEY = line
		else:
			SECRET_KEY = line

ACCESS_KEY = ACCESS_KEY[:len(ACCESS_KEY) - 1]

client = boto3.client('rekognition', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

form = []

for iterator in range(0, len(data["data"]["hits"])):

	unit = {}

	mageId = data["data"]["hits"][iterator]["mageId"]
	thumbImg = data["data"]["hits"][iterator]["thumbImg"]

	if len(thumbImg) == 0:
		continue
	labels = get_labels(thumbImg, client)
	
	unit["mageId"] = mageId
	unit["tag"]	= labels

	form.append(unit)

pprint(form)

# [
# 	{
# 		mageID: 
# 		tags: [a, b, c, ...]
# 	}
# 	...
# ]
