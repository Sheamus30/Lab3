def  cargar ( dic : dict ):
    print ( " \ n CARGAR UN PRODUCTO:" )
    dic . update ({ input ( "Ingrese el codigo del producto:" ): [ input ( "Ingrese el nombre del producto:" ), int ( input ( "Ingrese el precio:" )), int ( input ( "Ingrese la cantidad en stock: " ))]})
    # {123456: ["nombre", int, int]}

def  imprimir ( dic : dict ):
    imprimir ( " \ n TODOS LOS PRODUCTOS:" )
    para  clave  en  dic :
        print ( f "Codigo del producto: { clave } - Nombre: { dic [ clave ] [ 0 ] } | Precio: { dic [ clave ] [ 1 ] } | Cantidad de stock: { dic [ clave ] [ 2 ] } " )

def  buscar ( dic : dict ):
    imprimir ( " \ n BUSCAR UN PRODUCTO:" )
    cod  =  input ( "Ingrese el codigo del producto a buscar:" )
    valores  =  dic . elementos ()
    para  x  en  valores :
        si ( cod  ==  x [ 0 ]):
            return ( f "Nombre: { x [ 1 ] [ 0 ] } | Precio: { x [ 1 ] [ 1 ] } | Cantidad de stock: { x [ 1 ] [ 2 ] } " )
    volver  "No se encontro el producto"

def  stock0 ( dic : dict ):
    print ( " \ n PRODUCTOS CON STOCK EN 0:" )
    valores  =  dic . elementos ()
    para  x  en  valores :
        si ( x [ 1 ] [ 2 ] ==  0 ):
            print ( f "Codigo del producto: { x [ 0 ] } - Nombre: { x [ 1 ] [ 0 ] } | Precio: { x [ 1 ] [ 1 ] } | Cantidad de stock: { x [ 1 ] [ 2 ] } " )

dic  = { "123" : [ "Producto1" , 123 , 12 ], "456" : [ "Producto2" , 456 , 0 ]}
cargar ( dic )
imprimir ( dic )
print ( "El producto buscado es:" , buscar ( dic ))
stock0 ( dic )