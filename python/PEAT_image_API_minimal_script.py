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
headers = {'username':"YOUR USERNAME", "password":"YOUR PASSWORD"}

# make a dict with the picture and the json
files = {"picture": open(image,'rb'),"json":open(json, "rb")}

# post both files to our API
result = requests.get("http://" + ip + ":"+ port + version + route, files=files, headers=headers,timeout=5)

# load response that comes in JSON format
data = json.load(result.text)

# print the result
print result
print data
    
