require 'net/http'
require 'uri'
require 'json'
require 'mime/types'

IP = "api.peat-cloud.com"
VERSION = "v1"
ROUTE = "image_analysis"
URL = "http://#{IP}/#{VERSION}/#{ROUTE}"

#Replace <YOUR_API_KEY> with your api key
API_KEY = "<YOUR_API_KEY>"

BOUNDARY = "%d" %Time.now.to_f.ceil

FILE = "../data/tomato_nutrient/healthy_640x480.png"

def send_request
    uri = URI(URL)
    http = Net::HTTP.new(uri.host, uri.port)


    req = Net::HTTP::Post.new(uri.path, initheader = {"Content-Type" => "multipart/form-data; boundary=#{BOUNDARY}", "api_key" => API_KEY})

	post_body = []

	# Add the file Data
	post_body << "--#{BOUNDARY}\r\n"
	post_body << "Content-Disposition: form-data; name=\"picture\"; filename=\"#{File.basename(FILE)}\"\r\n"
	post_body << "Content-Type: #{MIME::Types.type_for(FILE)}\r\n\r\n"
	post_body << File.read(FILE)
	post_body << "\r\n--#{BOUNDARY}--\r\n"
	req.body = post_body.join

    print req.body

    res = http.request(req)
    puts "response #{res.body}"
rescue => e
    puts "failed #{e}"
end

send_request()
