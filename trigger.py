import requests

ngrok_url = 'https://dbf4665e5f39.ngrok.io'
endpoint = f'{ngrok_url}/abc'

r =requests.post(endpoint, json={})
print(r.json()['data'])