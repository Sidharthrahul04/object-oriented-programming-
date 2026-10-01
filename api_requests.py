import requests

#get
params={"id":1
        }
headers={'Authentication':'XYZ-123'
        }
try:
    response=requests.get("https://jsonplaceholder.typicode.com/todos/1",params=params,headers=headers,timeout=10)
    print(response.status_code)
    response.raise_for_status()
    data=response.json()
    print(data["title"])
except requests.RequestException as e:
    print(e)

#response.status_code

#post
json={"id":1
        }
headers={'Authentication':'XYZ-123'
        }
try:
    response=requests.post("https://jsonplaceholder.typicode.com/todos/1",json=json,headers=headers)
    # print(response)
    response.raise_for_status()
except requests.RequestException as e:
    print(e)






# Endpoint → where you're sending the request.

# params → extra information added to the URL to specify/filter what you want.

# json → structured data sent in the request body, commonly with POST.

# API key → a credential that an API may require to identify/authorize your requests.

# And API documentation → the instruction manual telling you which endpoint, parameters, headers, authentication, and request format that particular API expects.