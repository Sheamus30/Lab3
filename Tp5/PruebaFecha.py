#from datetime import datetime
from typing import *
import requests
import numpy as np
import pandas as pd
from tabulate import tabulate


listaFecha = []
lista = ['argentina','brazil','chile','colombia','ecuador','guyana','paraguay','peru','suriname','uruguay','venezuela','trinidad and tobago']
lista1 = ['------------']
lista2 = ['------------']
lista3 = ['--------']

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
    cabezera = pd.DataFrame([[lista1,lista2,lista3]], columns=[' Pais  ', '  Muertos', '   Estado'])
    print(cabezera)

    for data in lista:
        api_link = f'https://api.covid19api.com/country/{data}/status/deaths?from={listaFecha[0]}T00:00:00Z&to={listaFecha[1]}T00:00:00Z'
        #print (api_link)
        response = requests.get(api_link)
        respuesta = response.json()
        for item in respuesta:      
            case = item.get("Cases")
            #casesDeaths(x,listaFecha[0],listaFecha[1])
        if ((case > 50 )and(case < 100 )):
            Estado = "Medio" 
        if (case > 100):
            Estado = "Alto"
        if (case < 50):
            Estado = "Bajo"
   
        df = pd.DataFrame([[data,case, Estado]], columns=['        ', '           ','           '])
        print(df)
    


#def casesDeaths(data, desde, hasta):
    #print(case) 
  
    
    
    
    #df = pd.DataFrame([[data,case]], columns=['        ', '           ', '           '])
    #print(df)
    
        # if cases:   
        #  print(cases)


#URL= 'https://api.covid19api.com/country/argentina/status/deaths?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z'
#api_link = "https://api.covid19api.com/live/country/south-africa/status/confirmed"