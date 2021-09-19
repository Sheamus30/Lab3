def  mostrar ( dic : dict ):
    para  clave  en  dic :
        print ( f "Nombre: { clave } - Habitantes: { dic [ clave ] } " )

dic  = { "Argentina" : 45 , "Alemania" : 32 , "EEUU" : 120 , "Perú" : 65 , "España" : 73 }
mostrar ( dic )