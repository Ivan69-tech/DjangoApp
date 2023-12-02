import requests
import json


def get_pos():
	r =requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()
	pos = {
	"latitude": r["latitude"],
	"longitude": r["longitude"]
	}
	
	return pos

