listas  = []
mayor  =  0.0
para  x  en el  rango ( 5 ):
    val  =  float ( input ( "Ingrese un sueldo:" ))
    si  val  >  mayor :
        mayor  =  val
        listas . añadir ( val )
    otra cosa :
        listas . insertar ( 0 , val )
print ( "La lista ingresada es:" , listas , " \ n El mayor numero es:" , mayor )