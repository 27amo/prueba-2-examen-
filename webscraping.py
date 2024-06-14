from  bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://www.mercadolibre.com.ec/notebook-lenovo-ideapad-16iau7-storm-gray-tactil-16-intel-core-i7-1255u-16gb-de-ram-512gb-ssd-intel-iris-xe-graphics-g7-96eus-2560x1600px-windows-11-home/p/MEC23051396?pdp_filters=item_id:MEC548990534#is_advertising=true&searchVariation=MEC23051396&position=1&search_layout=grid&type=pad&tracking_id=815bcde2-2762-4e19-b770-0e1fc73d1265&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=YWE1NTU1ZmMtNjQ2Ny00NmRiLWI4N2YtMDM3NDIyMTA5YjFk")

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
