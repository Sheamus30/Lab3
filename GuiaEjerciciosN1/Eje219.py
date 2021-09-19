lista = [[ 4 , 12 , 5 , 66 ], [ 14 , 6 , 25 ], [ 3 , 4 , 5 , 67 , 89 , 23 , 1 ], [ 78 , 56 ]]
print ( "Lista antes:" , lista )
para  x  en  rango ( len ( lista )):
    para  j  en  rango ( len ( lista [ x ])):
        si  lista [ x ] [ j ] >  10 :
            lista [ x ] [ j ] =  0
print ( "Lista despues:" , lista )