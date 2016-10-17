#!/bin/bash
# replace <YOUR_API_KEY> with a valid key
curl -H "api_key: <YOUR_API_KEY>" -F "picture=@../data/Wheat_Leaf_Rust_100059/PEAT_20160609_122425_85d9410f-5452-42da-b471-2d80a4e9d94e.jpg" "http://api.peat-cloud.com/v1/image_analysis"
