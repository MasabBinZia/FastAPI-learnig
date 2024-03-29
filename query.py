import requests

res = requests.get('http://127.0.0.1:8000/items/100/?q=101')
print("Text", res.text)
print("JSON", res.json())
print("Status Code", res.status_code)


