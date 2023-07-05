import requests
headers = {"accept": "application/json"}
response = requests.post("https://httpbin.org/get", headers=headers)

print(response.status_code) ##405 Method Not Allowed