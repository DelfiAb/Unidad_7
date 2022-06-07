import requests

#url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php"
#url_rsp = requests.get(url, params={"i": "Gin"})
#en vez de poner url podria haber pegado directo el link, y no usar el val de arriba
#print(url_rsp.json()) #para ver si funciona el link pruebo así
#url_rsp = requests.get(url, params={"i": "Gin"})
#url_json = url_rsp.json()
#print(url_rsp)

base_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
http_rsp = requests.get(base_url, params={"s": "margarita"})
rsp_json = http_rsp.json()

print(rsp_json)
print(type(rsp_json))
print(rsp_json["drinks"][0]["idDrink"])

class Drinks:

    def __init__(self, tittle, strAlcohol, strInstructions) -> None:
        self.tittle = tittle
        self.strAlcohol = strAlcohol
        self.strInstructions = strInstructions

    def __str__(self) -> str:
        return f"{self.tittle}, {self.strAlcohol}, {self.strInstructions}"

print(Drinks("Caipi", "Caipiroshka", "asdfg"))

#OTRA FORMA MAS "LINDA" DE HACERLO:
drink_type = input("Drink >>")
req_params = {"s": drink_type}
http_resp = requests.get(base_url, params = req_params)

print(http_resp.jsonn())