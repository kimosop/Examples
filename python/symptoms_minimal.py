#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
import requests

def main():
    #The name of the disease, where we want to get the symptoms from
    #peat_id of the disease magnesium deficiency
    disease_id = '700004'
    #Replace this with your country code. For example de, in, ...
    language = 'en'
    
    #Replace <YOUR_API_KEY> with your api key
    headers = {'api_key': '<YOUR_API_KEY>'}
    
    #Send request
    url = 'http://api.peat-cloud.com/disease_id/%s/%s' %(disease_id, language)
    req = requests.get(url,headers=headers)
    #Evaluate response
    if req.status_code == 401:
        print 'Authentication failed'
    elif req.status_code == 200:
        print req.text

if __name__ == '__main__':
    main()
