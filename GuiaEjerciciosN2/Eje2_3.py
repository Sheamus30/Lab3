def  mostrar ( dic : dict ):
    print ( "Todos los articulos:" )
    para  clave  en  dic :
        print ( f "Nombre: { clave } - Precio: $ { dic [ clave ] } " )

def  superior ( dic : dict ):
    print ( "Articulos mayores a 100:" )
    para  clave  en  dic :
        si ( dic [ tecla ] >  100 ):
            print ( f "Nombre: { clave } - Precio: $ { dic [ clave ] } " )

dic  = { "Fideos" : 120 , "Manzana" : 67 , "Lechuga" : 150 , "Tomates" : 101 , "Chocolate" : 32 }
mostrar ( dic )
superior ( dic )