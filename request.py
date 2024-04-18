import requests

# Making a GET request
r = requests.get('https://unsplash.com/')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)
# print request object 
print(r.url) 
# print status code 
print(r.status_code)