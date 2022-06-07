import random
import requests       #sirve para hablar con apps en internet


url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"

http_rsp = requests.get(url)  #aca le digo q obtenga la info del link con el "get"

#print(http_rsp.text)
#print(type(http_rsp.text))   #pasar la rta a texto plano (str)
    #-->en tex es dificil editar/trabajarlo ? enotnces lo pasamos a json

#print(http_rsp.json())
#print(type(http_rsp.json()))
'''for book in http_rsp.json():
    print(f'Book name: {book["name"]}')
    print(f'Book name: {book["city"]}')'''

####################################################
class Novela:
    def __init__(self, titulo, origen) -> None:
        self.__id = random.randint(0, 1000000)
        self.titulo = titulo
        self.origen = origen

    def __str__(self):
        return f"Novela\n" \
               f"\tTitulo: {self.titulo}\n" \
               f"\tOrigen: {self.origen}\n"
####################################################

novelas_response = http_rsp.json()
novelas = []

for novela in novelas_response:
    novelas.append(Novela(novela["name"], novela["city"]))
    #aca appendea a cada novela q esta en el link a la lista "novela" usando la class Novela

print(novelas)

def user_menu():
    print("Menu Novelas")
    while True:
        print("1) Listar novelas")
        print("2) Agregar novela")
        print("3) salir")

        option = input(">> ")

        if option == "1":
            for novela in novelas:
                print(novela)

        elif option == "2":
            print("Nueva novela:")
            titulo = input("Titulo:")
            origen = input("Origen:")

            nueva_novela = Novela(titulo, origen)
            novelas.append(nueva_novela)

        elif option == "3":
            break

        else:
            print("Ingrese una opcion valida")

user_menu() #function call