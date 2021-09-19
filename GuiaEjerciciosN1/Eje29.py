lista  = []
para  x  en el  rango ( 5 ):
    val  =  float ( input ( "Ingrese las alturas:" ))
    lista . añadir ( val )
promedio  =  suma ( lista ) / 5
bajas = 0
altos = 0
para  x  en la  lista :
    si  x < promedio :
        bajas  + =  1
    elif  x > = promedio :
        altos  + =  1
print ( "Las alturas ingresadas son:" , lista , " \ n El promedio es:" , promedio , " \ n Las personas mayores al promedio son:" , altos , " \ n Las personas menores al promedio son:" , bajas )
