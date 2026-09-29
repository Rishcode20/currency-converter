import requests

response = requests.get("https://api.frankfurter.app/latest?from=USD&to=CAD")
print(response.status_code)
print(response.json())