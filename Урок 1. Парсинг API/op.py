import requests
import json

url = "http://openlibrary.org/search.json"

subject = "Artificial intelligence"

params = {
    "subject" : subject,
    "limit": 10
}
response = requests.get(url,params = params)

if response.status_code == 200:
    print("Успешный запрос API!")
else:
    print("Запрос API отклонен c кодом состояния:", response.status_code)    
