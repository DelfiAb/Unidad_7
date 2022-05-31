import requests

url = ""

http_rsp = requests.get(url)

print(http_rsp.text)
print(type(http_rsp.text))
#en tex es dificil editar/trabajarlo ? enotnces lo pasamos a json

print(http_rsp.json())
print(type(http_rsp.json()))

for book in http_rsp.json():
    print(f'Book name: {book["name"]}')
    print(f'Book name: {book["city"]}')