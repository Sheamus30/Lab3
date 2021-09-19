lista  = []
alcalde  =  0
cantidad  =  0
para  x  en el  rango ( 5 ):
    val  =  int ( input ( "Ingrese un numero entero:" ))
    lista . añadir ( val )
    si  val  >  mayor :
        mayor  =  val
        cantidad  =  1
    elif  val  ==  mayor :
        cantidad  + =  1
print ( "La lista ingresada es:" , lista , " \ n El mayor numero es:" , mayor , " \ n La cantidad de mayores es:" , cantidad )