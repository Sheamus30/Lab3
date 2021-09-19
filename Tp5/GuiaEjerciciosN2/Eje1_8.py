def  carga ():
    lista  = []
    para  x  en el  rango ( 5 ):
        lista . append ([ input ( f "Ingrese el nombre de la { x + 1 } ° persona:" ), int ( input ( "Ingrese la edad de la persona:" ))])
    volver  lista

def  imprimir ( lista : lista ):
    suma  =  0
    print ( "Las personas mayores de edad:" )
    para  x  en el  rango ( 5 ):
        suma  + =  lista [ x ] [ 1 ]
        si ( lista [ x ] [ 1 ] > =  18 ):
            print ( f "Nombre: { lista [ x ] [ 0 ] } - Edad: { lista [ x ] [ 1 ] } " )
    print ( "La edad promedio es:" , suma / 5 )

lista  =  carga ()
imprimir ( lista )