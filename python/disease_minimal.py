#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
import requests

def main():
    #First we need the name of the plant, from which we want to know all known diseases
    plant_name = 'TOMATO'
    #Replace this with your country code. For example de, in, ...
    language = 'en'
    #Replace <YOUR_API_KEY> with your api key
    headers = {'api_key': '<YOUR_API_KEY>'}
    url = 'http://api.peat-cloud.com/diseases/%s/%s' %(plant_name, language)
    req = requests.get(url, headers=headers) 
    #Evaluate response
    if req.status_code == 401:
        print req.text
    elif req.status_code == 200:
        data = req.text 
        print data 

if __name__ == '__main__':
    main()
