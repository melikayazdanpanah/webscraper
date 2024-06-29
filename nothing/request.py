import requests

url ='https://unsplash.com/'
# Making a GET request
response= requests.get(url)
# check status code for response received
# success code - 200
print(response)
# print content of request
print(response.content)
# print request object 
print(response.url) 
# print status code 
print(response.status_code)

if __name__ =="__main__":
    with open("request_output.py" , "w") as f:
              f.write(f"response.content = {repr(response.content)}\n")
              f.write(f"response_url = {repr(response.url)}\n")
              f.write(f"response_status_code = {repr(response.status_code)}\n")