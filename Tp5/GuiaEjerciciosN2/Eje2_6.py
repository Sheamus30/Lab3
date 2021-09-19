def  cargar ( dic : dict ):
    imprimir ( " \ n INGRESAR UNA ACTIVIDAD" )
    fecha  =  input ( "Ingrese la fecha:" )
    para  x  en  dic :
        si ( x  ==  fecha ):
            dic [ x ]. append (( input ( "Ingrese la hora:" ), input ( "Ingrese la actividad:" )))
            regreso
    dic . actualizar ({ fecha : [( input ( "Ingrese la hora:" ), input ( "Ingrese la actividad:" ))]})

def  imprimir ( dic : dict ):
    imprimir ( " \ n AGENDA MOSTRAR" )
    para  x  en  dic :
        print ( f " \ n Actividades dia { x } :" )
        para  y  en  dic [ x ]:
            print ( f "* Hora: { y [ 0 ] } - Actividad: { y [ 1 ] } " )

def  buscar ( dic : dict ):
    imprimir ( " \ n BUSCAR UNA FECHA" )
    fecha  =  input ( "Ingrese la fecha a buscar:" )
    para  x  en  dic :
        si ( x  ==  fecha ):
            print ( f " \ n Actividades del dia { x } :" )
            para  y  en  dic [ x ]:
                print ( f "* Hora: { y [ 0 ] } - Actividad: { y [ 1 ] } " )
            regreso
    print ( "No se encontro la fecha" )
    

dic  = { "23/08" : [( "14:05" , "tengo que comprar el pan" ), ( "12:06" , "visitar a mi papa" )], "22/04" : [( "13:54" , "Vender ..." )]}
cargar ( dic )
imprimir ( dic )
buscar ( dic )