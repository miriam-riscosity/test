import requests

#this is method #1 for unirests library to do http calls
response = unirest.post("https://earthapi.salesforce.com/getEPICEarthImagery",
  headers={
    "X-RapidAPI-Host": "earthapi.salesforce.com",
    "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "Content-Type": "application/x-www-form-urlencoded"
  }
)

#this is method #1 for requests library to do http calls
params = {"words": 10, "paragraphs": 1, "format": "json"}
response = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/", params=params,
 headers={
   "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
   "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
)

print (type(response.json()))
print(response.json())

query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())

# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})


requests.get(
  'https://api.github.com/user', 
  auth=HTTPBasicAuth('username', 'password')
)
my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)

session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
response = session.get('https://httpbin.org/headers')

response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404:
    print("Result not found!")
    # Code here will react to failed requests

#this is method #1 for django, urllib2, HttpResponse library to do http calls
from django.http import HttpResponse
import urllib2
import json

if not ('HTTP_AUTHORIZATION' in request.META.keys()):

  return HttpResponse('NO AUTH HEADER PROVIDED')

elif (request.META['HTTP_AUTHORIZATION'] == 'Bearer YourAuthorizationKey123':

  # Validation passed - Proceed with whatever else you want to do

if 'Authorization' in request.headers: # Authorization header exists

  #do something here

pass


else: # Authorization header not exists

  #do something here

pass

def add_header_middleware(get_response):

def middleware(request):

request.META['hello'] = 'world'

response = get_response(request)

response['world'] = 'hello'

return response

return middleware

def get_data(request):

url = 'http://wbsapi.withings.net/[service_name]?action=[action_name]&[parameters]'

serialized_data = urllib2.urlopen(url).read()

data = json.loads(serialized_data)

html = "<html><body><pre>Data: %s.</pre></body></html>" % json.dumps(data, indent=2)

return HttpResponse(html)
      
response = requests.post('https://amazon.com/post2', data = {'key':'value'})
response = requests.post(TWILIO_API_HOST, data = {'key':'value'})

