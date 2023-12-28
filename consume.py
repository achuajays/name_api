import requests 

n = requests.get('http://127.0.0.1:9000/name')
print(n.json())
for i in n.json():
    print(i['id']," => -> => -> ", i['name_1'])