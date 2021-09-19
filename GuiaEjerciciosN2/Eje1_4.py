'' '
def perimetro (lado: int):
    volver (lado * 4)
área def (lado: int):
    volver (lado * lado)
def cuadrado (lado: int):
    print ("" "Quiere calcular :)
    1. ¿Área?
    2. ¿Perimetro?
    3. Area y Perimetro? "" ")
    opcion = input ("Ingrese una opcion:")
    si opcion == "1":
        print (f "El area del cuadrado es: {area (lado)}")
    elif opcion == "2":
        print (f "El perimetro del cuadrado es: {perimetro (lado)}")
    elif opcion == "3":
        print (f "El area es: {area (lado)} y perimetro es: {perimetro (lado)}")
    demás:
        print ("Opcion invalida")
cuadrado (5)
'' '

---------------------
def  cuadrado ():
    imprimir ( "1. AREA" )
    imprimir ( "2. PERIMETRO" )
    x  =  int ( input ( "Introduce la opción que desea:" ))
    si  x  ==  1 :
        perimetro ()
    elif  x  ==  2 :
        área ()

def  perimetro ():
    lado  =  int ( input ( "Ingrese el lado del cuadrado:" ))
    p  =  4 * lado
    print ( "El perimetro es:" , p )

def  área ():
    lado  =  int ( input ( "Ingrese el lado del cuadrado:" ))
    a  =  lado * lado
    print ( "El area es:" , a )
cuadrado ()