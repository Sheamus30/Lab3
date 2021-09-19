def  cargar ( dic : dict ):
    dic . update ({ input ( "Ingrese palabra en ingles:" ): input ( "Ingrese la traduccion al español:" )})

def  mostrar ( dic : dict ):
    print ( "Diccionario:" )
    para  clave  en  dic :
        print ( f "Inglés: { clave } -> Español: { dic [ clave ] } " )

def  buscar ( dic : dict ):
    palabra  =  input ( "Ingrese la palabra en ingles a buscar:" )
    valores  =  dic . elementos ()
    para  x  en  valores :
        si ( x [ 0 ] ==  palabra ):
            return  x [ 1 ]
    volver  "No se encontro la palabra"

dic  = { "hola" : "hola" , "for" : "para" , "get" : "obtener" , "bye" : "chau" }
cargar ( dic )
print ( "La palabra buscada es:" , buscar ( dic ))