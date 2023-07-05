import requests
headers = {"accept": "application/json"}
payload = {"key1": "value1"}
response = requests.post("https://httpbin.org/post", headers=headers, data=payload)

print(response.json())

response2 = requests.post("https://httpbin.org/post", headers=headers, json=payload)

print(response2.json())