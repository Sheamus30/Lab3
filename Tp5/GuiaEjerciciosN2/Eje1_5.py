def  sumar ( nombre : str ):
    return  len ( nombre )

nombre1  =  input ( "Ingrese el primer nombre:" )
nombre2  =  input ( "Ingrese el segundo nombre:" )
cant1  =  sumar ( nombre1 )
cant2  =  sumar ( nombre2 )
si  cant1  >  cant2 :
    print ( f "El nombre ' { nombre1 } ' tiene mas caracteres que ' { nombre2 } '" )
otra cosa :
    print ( f "El nombre { nombre2 } tiene mas caracteres que { nombre1 } " )