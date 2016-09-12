#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
import requests

ip = 'http://api.plantix.net'
port = 5010
version = 'v1'
route = 'image_analysis'

image = 'data/iron1.jpg'
json = 'data/example.json'

def main():
    # Header of our requst. Replace <YOUR_API_KEY> with your api key.
    headers = {'api_key': '<YOUR_API_KEY>'}

    # make a dict with the picture and the json
    files = {'picture': open(image,'rb'), 'json':open(json, 'rb')}

    url = 'http://%s:%d/%s/%s' %(ip, port, version, route)
    # post both files to our API
    result = requests.get(url, files=files, headers=headers,timeout=5)

    if result.status_code == 401:
        print 'Authentication failed'
    elif result.status_code == 200:
        # load response that comes in JSON format and print the result
        json_data = result.json()
        for data in json_data['image_analysis']:
            print 'Disease name: %s\n\tProbability: %s%%' %(data['name'], data['similarity'][0])
        print json_data

if __name__ == '__main__':
    main()