from paisesSudamerica import *
import requests
import pandas as pd

listaFecha = []
lista1 = ['-------']
lista2 = ['--------']
lista3 = ['-------']

def run():

    for f in range(0,2):

        print("Ingrese el año:")
        anio = int(input())
        while ((anio < 2020 )or(anio > 2021 )):
            print("Debe colocar un anio entre 2020 y 2021")
            anio = int(input("Ingrese el año: "))

        print("Ingrese el mes:")
        mes = int(input())
        while ((mes < 1 )or(mes > 12 )):
            print("Debe colocar un mes entre 01 y 12")
            mes = int(input("Ingrese el mes: "))

        print("Ingrese el dia:")
        dia = int(input())
        while ((dia < 1 )or(dia > 31 )):
            print("Debe colocar un dia entre 01 y 31")
            dia = int(input("Ingrese el dia: "))
            

        fecha = str(anio)+"-"+str(mes)+"-"+str(dia)
        listaFecha.append(fecha)
    print(" Fecha Ingresada: " + listaFecha[0] + " /// " + listaFecha[1]) 
    cabezera = pd.DataFrame([[lista1,lista2,lista3]], columns=['Pais', 'Muertos', 'Estado'])
    print(cabezera)

    for data in listaPaises:
        api_link = f'https://api.covid19api.com/country/{data}/status/deaths?from={listaFecha[0]}T00:00:00Z&to={listaFecha[1]}T00:00:00Z'
        response = requests.get(api_link)
        respuesta = response.json()
        for item in respuesta:      
            case = item.get("Cases")
            sigla = item.get("CountryCode")
        if ((case > 15000 )and(case < 50000 )):
            Estado = "Amarillo" 
        if (case > 50000):
            Estado = "Rojo"
        if (case < 15000):
            Estado = "Verde"
   
        df = pd.DataFrame([[sigla,case, Estado]], columns=['        ', '           ','           '])
        print(df)

    