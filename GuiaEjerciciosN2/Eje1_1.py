def  carga ():
    num1  =  int ( input ( "ingrese el primer valor:" ))
    num2  =  int ( input ( "ingrese el segundo valor:" ))
    return ( num1 , num2 )

def  suma ( num1 , num2 ):
    return ( num1 + num2 )

def  mensaje ():
    print ( "Chau bro, nos vemos" )

valores  =  carga ()
print ( "El valor de la suma:" , suma ( valores [ 0 ], valores [ 1 ]))
mensaje ()