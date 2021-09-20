#from datetime import datetime
import requests

def ciclo():
    lista = ['argentina','brazil','chile','colombia','ecuador','guyana','paraguay','peru','suriname','uruguay','venezuela','trinidad and tobago']
    for x in lista:
        casesDeaths(x)


def casesDeaths(data):
    api_link = f'https://api.covid19api.com/country/{data}/status/deaths?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z'
    print (api_link)
    response = requests.get(api_link)
    respuesta = response.json()
    for item in respuesta:
        case = item.get("Cases")
    print(case)
        # if cases:   
        #  print(cases)

def rangos():
    print("Ingrese el rango Desde (con formato AAAA-MM-DD) ")
    desde = input()
    print("Ingrese el rango Hasta (con formato AAAA-MM-DD)")
    hasta = input()
    print(f"Los rangos ingresados fueron {desde}  - {hasta}")
#URL= 'https://api.covid19api.com/country/argentina/status/deaths?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z'
#api_link = "https://api.covid19api.com/live/country/south-africa/status/confirmed"