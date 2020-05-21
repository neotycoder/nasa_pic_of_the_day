import requests
import wget
import ssl

# API URL for NASA APOD API REQUESTS

url="https://api.nasa.gov/planetary/apod?api_key=<enter your api key here>"

# make a GET request
response = requests.get(url)

# As a test, check the response
print(response)

# Let's put the response into JSON
apod_json = response.json()

# Let's see what the json format looks like:

print(apod_json)

# Let's get just the URL
apod_url = apod_json['url']

print("url: {}".format(apod_url))

# I've added the following ssl call to avoid certificate issues. 
ssl._create_default_https_context = ssl._create_unverified_context
# Perform the download
wget.download(apod_url)

# Added the following to print out the filename:
print("The file has been downloaded: {}".format(apod_url))
