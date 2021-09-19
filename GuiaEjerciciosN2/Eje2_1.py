def  carga ():
    lista  = []
    para  x  en el  rango ( 5 ):
        lista . append (( input ( "Ingrese el nombre del país:" ), int ( input ( "Ingrese la cantidad de habitantes que tiene:" ))))
    volver  lista

def  imprimir ( lista : lista ):
    print ( "Los paises ingresados ​​son:" )
    para  x  en la  lista :
        print ( f "Nombre: { x [ 0 ] } - Habitantes: { x [ 1 ] } " )

def  mayor ( lista : lista ):
    mayor  = ( 0 , 0 )
    para  x  en la  lista :
        si ( x [ 1 ] >  alcalde [ 1 ]):
            alcalde  =  x
    print ( f "El país con mayor cantidad de habitantes es { mayor [ 0 ] } con { mayor [ 1 ] } habitantes" )

lista  =  carga ()
imprimir ( lista )
alcalde ( lista )