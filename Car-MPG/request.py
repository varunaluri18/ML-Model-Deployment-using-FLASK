import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'HP':49, 'VOL':89, 'SP':104.258874, 'WT':28.796})

print(r.json())