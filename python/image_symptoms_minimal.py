#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
import requests

IP = 'api.peat-cloud.com' #127.0.0.1:5000'  #'api.peat-cloud.com'

# Header of our requst. Replace <YOUR_API_KEY> with your api key.
HEADER = {'api_key': '<YOUR_API_KEY>'}

def single_processing():
    
    version = 'v1'
    route = 'image_analysis'
    url = 'http://%s/%s/%s' % (IP, version, route)

    # make a dict with the picture
    image = os.path.join('..', 'data', 'tomato_nutrient', 'iron1.png')
    files = {'picture': open(image, 'rb')}

    # post both files to our API
    result = requests.get(url, files=files, headers=HEADER, timeout=200000)

    if result.status_code == 401:
        print 'Authentication failed'
    elif result.status_code == 500:
        print 'Internal server error...'
    elif result.status_code == 200:
        # load response that comes in JSON format and print the result
        json_data = result.json()
        print json_data['image_analysis']
        for data in json_data['image_analysis']:
            print 'Disease name: %s\n\tProbability: %s%%' % (data['name'], data['similarity'])

    return json_data['image_analysis'][0]['name']


def request_symptoms(d_name):

    #Send request
    url = 'http://%s/pathogens_spec/disease_name/%s/symptoms' %(IP, d_name)
    req = requests.get(url,headers=HEADER) 

    #Evaluate response
    if req.status_code == 401:
        print 'Authentication failed'
    elif req.status_code == 200:
        data = req.json()
        print 'Symptoms:\n\t%s' %data['data'][0]['symptoms']

if __name__ == '__main__':
    disease_name = single_processing()
    request_symptoms(disease_name)