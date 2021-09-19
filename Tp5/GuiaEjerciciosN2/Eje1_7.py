def  carga ():
    lista  = []
    para  x  en el  rango ( 5 ):
        lista . append ( int ( input ( f "Ingrese el valor n ° { x + 1 } :" )))
    volver  lista

def  mostrar ( lista : lista ):
    print ( "La lista es: \ n [" , end = "" )
    para  x  en la  lista :
        si ( x  >  10 ):
            print ( x , end = "" )
    imprimir ( "]" )

lista  =  carga ()
mostrar ( lista )
#mostrar (cargar ())