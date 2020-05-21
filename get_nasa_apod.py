import requests
import wget
import ssl
import shutil
import os

# API URL for NASA APOD API REQUESTS


url="https://api.nasa.gov/planetary/apod?api_key=<PUT YOUR API KEY HERE>"

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

# Let's copy this to a specific location. For me, what I want to do is store this in a specific directory. I eventually want my OS to cycle through these as background pics. 

# But first we need to split on the '/' symbol in the url. What I want to do is get the last value which is the file name in the url. 

split_on_slash = apod_url.split('/')

# Let's get the length of the split_on_slash variable
length_of_split_on_slash = len(split_on_slash) - 1

# Now let's just get the file name:
imagefile = split_on_slash[length_of_split_on_slash]

# Let's print out just the file name:

print("The image filename: {}".format(imagefile))

# Now that we have verified that the file name, let's copy this over to your target pictures directory.

path_cwd = "./{}".format(imagefile)
target_dir = "<some directory path>/{}".format(imagefile)

# Copy the file over
shutil.copyfile(path_cwd, target_dir)

# Let's check if the file reached it's destination

cmd = "ls -l {}".format(target_dir)
stream = os.popen(cmd)
print(stream.read())
