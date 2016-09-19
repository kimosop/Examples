#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import json
import requests

def main():
    #The name of the disease, where we want to get the symptoms from
    disease = 'Striga'
    
    #Replace <YOUR_API_KEY> with your api key
    headers = {'api_key': '<YOUR_API_KEY>'}
    
    #Send request
    url = "http://api.peat-cloud.com/pathogens_spec/disease_name/%s/symptoms" %disease
    req = requests.get(url,headers=headers) 

    #Evaluate response
    if req.status_code == 401:
        print 'Authentication failed'
    elif req.status_code == 200:
        data = req.json()
        print data['data'][0]['symptoms']

if __name__ == '__main__':
    main()