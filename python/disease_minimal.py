#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
import requests

def main():
    #First we need the name of the plant, from which we want to know all known diseases
    plant_name = 'tomato'

    #Replace <YOUR_API_KEY> with your api key
    headers = {'api_key': '<YOUR_API_KEY>'}
    url = 'http://api.peat-cloud.com/diseases/%s' %plant_name
    req = requests.get(url, headers=headers) 

    #Evaluate response
    if req.status_code == 401:
        print 'Authentication failed'
    elif req.status_code == 200:
        data = req.text 
        print data 

if __name__ == '__main__':
    main()