importar al  azar

clase  Dado :
    valor : int
    def  tirar ( yo ):
        yo . valor  =  aleatorio . randint ( 1 , 6 )
    def  imprimir ( auto ):
        print ( f "El valor del dado es: { self . valor } " )
    def  retornar_valor ( yo ):
        volver a  sí mismo . valor

clase  JuegoDeDados :
    dado1 : Dado ()
    dado2 : Dado ()
    dado3 : Dado ()
    def  __init__ ( self , dado1 : Dado (), dado2 : Dado (), dado3 : Dado ()):
        yo . dado1  =  dado1
        yo . dado2  =  dado2
        yo . dado3  =  dado3
    
    def  jugar ( yo ):
        yo . dado1 . tirar ()
        yo . dado2 . tirar ()
        yo . dado3 . tirar ()
        yo . dado1 . imprimir ()
        yo . dado2 . imprimir ()
        yo . dado3 . imprimir ()
        if ( self . dado1 . retornar_valor () ==  self . dado2 . retornar_valor () ==  self . dado3 . retornar_valor ()):
            imprimir ( "Gano" )
        otra cosa :
            imprimir ( "Perdio" )

d1  =  Dado ()
d2  =  Dado ()
d3  =  Dado ()

juego1  =  JuegoDeDados ( d1 , d2 , d3 )
juego1 . jugar ()