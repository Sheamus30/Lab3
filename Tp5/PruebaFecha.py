#from datetime import datetime
import requests
import numpy as np
import pandas as pd
from tabulate import tabulate 

listaFecha = []
lista = ['argentina','brazil','chile','colombia','ecuador','guyana','paraguay','peru','suriname','uruguay','venezuela','trinidad and tobago']
def ciclo():
    
    for f in range(0,2):
        print("Ingrese el año:")
        anio = input()
        print("Ingrese el mes:")
        mes = input()
        print("Ingrese el dia:")
        dia = input()
        fecha = anio+"-"+mes+"-"+dia
        listaFecha.append(fecha)
    print(listaFecha[0] + " /// " + listaFecha[1])

    for x in lista:
        casesDeaths(x,listaFecha[0],listaFecha[1])


def casesDeaths(data, desde, hasta):
    api_link = f'https://api.covid19api.com/country/{data}/status/deaths?from={desde}T00:00:00Z&to={hasta}T00:00:00Z'
    #print (api_link)
    response = requests.get(api_link)
    respuesta = response.json()
    for item in respuesta:      
        case = item.get("Cases")
    #print(case)
        print(tabulate(lista, headers=['Pais', 'Muertos'], showindex=True))



#    df = pd.DataFrame([[data,case]], columns=['    Pais    ', '     Muertos'])
#    print(df)

        # if cases:   
        #  print(cases)



#URL= 'https://api.covid19api.com/country/argentina/status/deaths?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z'
#api_link = "https://api.covid19api.com/live/country/south-africa/status/confirmed"