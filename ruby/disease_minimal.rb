require 'net/http'
require 'json'

PLANT_NAME = 'TOMATO'

#Replace this with your country code. For example de, in, ...
LANGUAGE = 'en'

#Replace <YOUR_API_KEY> with your api key
API_KEY = '<YOUR_API_KEY>'

def send_request
    uri = URI('http://api.peat-cloud.com/diseases/%s/%s' % [PLANT_NAME, LANGUAGE])
    http = Net::HTTP.new(uri.host, uri.port)
    req = Net::HTTP::Get.new(uri.path, initheader = {'Content-Type' => 'application/json', 'api_key' => API_KEY})

    res = http.request(req)
    puts "response #{res.body}"
rescue => e
    puts "failed #{e}"
end

send_request()
