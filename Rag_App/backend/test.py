import requests

query_url = "http://127.0.0.1:8080/query"
data = {"query": "what subjects does agastya malik have?"}
response = requests.post(query_url, json=data)
print(response.json())
