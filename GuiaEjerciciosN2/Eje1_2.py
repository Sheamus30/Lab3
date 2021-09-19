def  suma ( num1 , num2 ):
    return ( num1 + num2 )

def  carga ():
    num1  =  int ( input ( "ingrese el primer valor:" ))
    num2  =  int ( input ( "ingrese el segundo valor:" ))
    return ( num1 , num2 )

para  x  en el  rango ( 5 ):
    imprimir ( "----------------------------------------" )
    valores  =  carga ()
    print ( "El valor de la suma:" , suma ( valores [ 0 ], valores [ 1 ]))