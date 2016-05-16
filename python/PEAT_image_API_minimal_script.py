#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
import requests

ip = "api.plantix.net"
port = "80"
version = "/v1"
route = "/image_analysis"

image = "data/iron1.jpg"
json = "data/example.json"

# make a header with your username and password
headers = {'username':"YOUR_PASSWORD", "password":"YOUR USERNAME"}

# make a dict with the picture and the json
files = {"picture": open(image,'rb'),"json":open(json, "rb")}

# post both files to our API
result = requests.get("http://" + ip + ":"+ port + version + route, files=files, headers=headers,timeout=5)

# load response that comes in JSON format
data = result.json()

# print the response code and
print result
print data
    
