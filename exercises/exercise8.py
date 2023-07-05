import requests
headers = {"accept": "application/json"}
response = requests.get("https://httpbin.org/get", headers=headers)

print(response.status_code) # 200 OK