clase  Triangulo :
    def  inicializar ( self , lado1 : int , lado2 : int , lado3 : int ):
        yo . lado1  =  lado1
        yo . lado2  =  lado2
        yo . lado3  =  lado3
    
    def  mayor ( yo ):
        lados  = [ self . lado1 , self . lado2 , self . lado3 ]
        print ( f "El lado mayor es: { max ( lados ) } " )
    
    def  equilatero ( yo ):
        if ( self . lado1  ==  self . lado2  ==  self . lado3 ):
            print ( "Es un triangulo equilatero" )
        otra cosa :
            print ( "NO es un triangulo equilatero" )

    def  imprimir ( auto ):
        print ( f "Lados: { self . lado1 } - { self . lado2 } - { self . lado3 } " )

t1  =  Triángulo ()
t2  =  Triángulo ()
t1 . inicializar ( 20 , 20 , 20 )
t2 . inicializar ( 4 , 20 , 69 )
t1 . imprimir ()
t2 . imprimir ()
t1 . alcalde ()
t2 . alcalde ()
t1 . equilatero ()
t2 . equilatero ()