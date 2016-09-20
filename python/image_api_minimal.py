#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import cv2

import json
import requests

ip = 'api.peat-cloud.com'
version = 'v1'
route = 'image_analysis'

image = 'data/iron1.jpg'

def main():
    # Header of our requst. Replace <YOUR_API_KEY> with your api key.
    headers = {'api_key': '<YOUR_API_KEY>', 'variety': 'TOMATO'}

    # make a dict with the picture
    files = {'picture': open(image,'rb')}

    url = 'http://%s/%s/%s' %(ip, version, route)
    # post both files to our API
    result = requests.get(url, files=files, headers=headers,timeout=50)

    if result.status_code == 401:
        print 'Authentication failed'
    elif result.status_code == 500:
        print 'Internal server error...'
    elif result.status_code == 200:
        # load response that comes in JSON format and print the result
        json_data = result.json()
        for data in json_data['image_analysis']:
            print 'Disease name: %s\n\tProbability: %s%%' %(data['name'], data['similarity'][0])
        print json_data

if __name__ == '__main__':
    main()
