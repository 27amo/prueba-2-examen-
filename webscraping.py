from  bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://listado.mercadolibre.com.ec/laptops#D[A:laptops%20]")

soup = BeautifulSoup(url.content,"html.parser")


resultado = soup.find("span",{"class","andes-money-amount__fraction"})

print(resultado)

precioActual_text = resultado.text

print(precioActual_text)

precioActual = float(precioActual_text)

print(precioActual)

precioDeseado = 500

print(precioDeseado)

if precioDeseado >= precioActual:
    print("Esta oferta es para ti")
else:
    print("no hay nada para ti")
