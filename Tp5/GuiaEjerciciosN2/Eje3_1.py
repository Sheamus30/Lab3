clase  Alumno ():
    def  inicializar ( self , nombre : str , nota : int ):
        yo . nombre  =  nombre
        yo . nota  =  nota
    
    def  regular ( uno mismo ):
        si ( self . nota  > =  4 ):
            print ( f "El alumno { self . nombre } esta regular con una nota de { self . nota } " )
        otra cosa :
            print ( f "El alumno { self . nombre } no esta regular con una nota de { self . nota } " )
    
    def  imprimir ( auto ):
        print ( f "Nombre: { self . nombre } - Nota: { self . nota } " )

a1  =  Alumno ()
a2  =  Alumno ()
a1 . inicializar ( "Matias" , 5 )
a2 . inicializar ( "Lucas" , 3 )
a1 . imprimir ()
a2 . imprimir ()
a1 . regular ()
a2 . regular ()