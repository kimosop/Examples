#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
import requests
import json

# Path to our api.
IP = 'api.peat-cloud.com'
VERSION = 'v1'
ROUTE = 'image_analysis'
URL = 'http://%s/%s/%s' % (IP, VERSION, ROUTE)

# Header of our requst. Replace <YOUR_API_KEY> with your api key.
HEADER = {'api_key': '<YOUR_API_KEY>'}

ROOT_FOLDER = '../data/batch_example'
JSON_META_FILENAME = 'meta_data.json'


def send_request(filepath, header):
    files = {'picture': open(filepath, 'rb')}
    response = requests.get(URL, files=files, headers=header, timeout=10)
    return response.json()


def save_json(json_data, filepath):
    json_filename = '%s.json' % filepath[:-4]
    with open(json_filename, 'w') as outfile:
        json.dump(json_data, outfile, indent=4, sort_keys=True)


def load_json(json_file, folder):
    json_data = {}
    if json_file:
        with open(os.path.join(folder, json_file[0])) as data_file:
            json_data = json.load(data_file, parse_float=str, parse_int=str)
    return json_data


def batch_processing(directory):
    '''
        this example is a bit more sophisticated than the simple single_processing function,
        it needs a base folder as argument
        and will iterate over every image in all subfolders of this directory
    '''

    # get a list of all the subfolders
    folder_list = [x[0] for x in os.walk(directory)]
    # iterate over all folder in a given directory
    for folder in folder_list:
        file_list = [i for i in os.listdir(folder) if i.endswith('.jpg') or i.endswith('.png')]

        # Find the json metadata file in the folder
        json_file = [i for i in os.listdir(folder) if i == JSON_META_FILENAME]
        json_meta_data = load_json(json_file, folder)
        # Merge the header with the metadata json.
        new_header = json_meta_data.copy()
        new_header.update(HEADER)
        # iterate over all files in a given subfolder
        for f in file_list:
            filepath = os.path.join(folder, f)

            # Send request
            json_data = send_request(filepath, new_header)

            # Save the image results into a json
            save_json(json_data, filepath)

            # just printing
            print 'filename:', f
            print 'input from folder:', folder
            print 'image API result:\n\tName: %s\n\tSimilarity: %f\n\tpeat_id: %d' % \
                (json_data['image_analysis'][0]['name'],
                 json_data['image_analysis'][0]['similarity'],
                 json_data['image_analysis'][0]['peat_id'])


if __name__ == '__main__':
    batch_processing(ROOT_FOLDER)
