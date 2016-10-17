#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
import requests


ip = "api.peat-cloud.com"
version = "v1"
route = "image_analysis"
url = "http://%s/%s/%s" % (ip, version, route)


def single_processing():
    # Header of our requst. Replace <YOUR_API_KEY> with your api key.
    headers = {"api_key": "<YOUR_API_KEY>"}

    # make a dict with the picture
    image = os.path.join("data", "tomato_nutrient", "iron1.jpg")
    files = {"picture": open(image, "rb")}

    # post both files to our API
    result = requests.get(url, files=files, headers=headers, timeout=10)

    if result.status_code == 401:
        print "Authentication failed"
    elif result.status_code == 500:
        print "Internal server error..."
    elif result.status_code == 200:
        # load response that comes in JSON format and print the result
        json_data = result.json()
        for data in json_data["image_analysis"]:
            print "Disease name: %s\n\tProbability: %s%%" % (data["name"], data["similarity"])
    print ""
    return


def batch_processing(directory):
    '''
    this example is a bit more sophisticated than the simple single_processing function,
    it needs a base folder as argument
    and will iterate over every image in all subfolders of this directory
    '''

    # Header of our requst. Replace <YOUR_API_KEY> with your api key.
    headers = {"api_key": "<YOUR_API_KEY>"}

    # get a list of all the subfolders
    folderlist = [x[0] for x in os.walk(directory)]

    # iterate over all folder in a given directory
    for folder in folderlist:
        filelist = [i for i in os.listdir(folder) if i.endswith(".jpg")]

        # iterate over all files in a given subfolder
        for f in filelist:
            filepath = os.path.join(folder, f)
            files = {"picture": open(filepath, "rb")}
            result = requests.get(url, files=files, headers=headers, timeout=10)

            # all data comes in json format
            json_data = result.json()

            # just printing
            print "filename:", f
            print "input from folder:", folder
            print "image API result:", json_data["image_analysis"][0]["name"], \
                  json_data["image_analysis"][0]["similarity"], "peat_id", \
                  json_data["image_analysis"][0]["peat_id"], "\n"
    return


if __name__ == "__main__":
    single_processing()
    batch_processing("data")
