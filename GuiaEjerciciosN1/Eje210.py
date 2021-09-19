'' '
mañana = []
tarde = []
para x en el rango (8):
    si x <= 4:
        val = float (input ("Ingrese los sueldos del turno mañana:"))
        mañana.append (val)
    demás:
        val = float (input ("Ingrese los sueldos del turno tarde:"))
        tarde.append (val)
print ("Sueldos mañana:", mañana, " \ n Sueldos tarde:", tarde)
'' '
ma ñ ana  = []
tarde  = []
cant_ma ñ ana  =  int ( input ( "Ingrese la cantidad de empleados de la mañana:" ))
cant_tarde  =  int ( input ( "Ingrese la cantidad de empleados de la tarde:" ))
para  x  en el  rango ( cant_ma ñ ana ):
    val  =  float ( input ( "Ingrese los sueldos del turno mañana:" ))
    ma ñ ana . añadir ( val )
para  x  en el  rango ( cant_tarde ):
    val  =  float ( input ( "Ingrese los sueldos del turno tarde:" ))
    tarde . añadir ( val )
print ( "Sueldos mañana:" , ma ñ ana , " \ n Sueldos tarde:" , tarde )