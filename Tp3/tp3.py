import os
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, flowables
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
# Importamos clase de hoja de estilo.
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate('TablaEliminatorias.pdf',pagesize=A4,showBoundary=1)

IMAGEN1 = 'imagenqatar.jpg'
IMAGEN2 = 'copa.jpg'
# Creamos un PageTemplate.
estiloHoja = getSampleStyleSheet()
# Inicializamos la lista Platypus Story.
story = []

def imagenes():
    story.append(Spacer(0, 5))
    # Ahora incluimos una imagen.
    fichero_imagen = IMAGEN1
    imagen_logo = Image(os.path.realpath(fichero_imagen), width=160, height=190)
    story.append(imagen_logo)
    # Ahora incluimos una imagen.
    fichero_imagen2 = IMAGEN2
    imagen_logo2 = Image(os.path.realpath(fichero_imagen2), width=160, height=190)
    story.append(imagen_logo2)

def titulo():
    # Definimos cómo queremos que sea el estilo de la PageTemplate.
    cabecera = estiloHoja['Heading4']
    #  No se  hará un  salto de  página después  de escribir  la cabecera
    # (valor 1 en caso contrario).
    cabecera.pageBreakBefore = 0
    cabecera.keepWithNext = 0
    # Color de la cabecera.
    cabecera.backColor = colors.fidred
    # Incluimos un Flowable, que en este caso es un párrafo.
    parrafo = Paragraph('Clasificacion de la CONMEBOL para la COPA MUNDIAL DE FUTBOL', cabecera)
    # Lo incluimos en el Platypus story.
    story.append(parrafo)

def subtitulo():
    # Dejamos espacio:
    story.append(Spacer(0, 15))

    # Definimos  un párrafo. 
    cadena = ' Posiciones de Eliminatorias Sudamericana de la Copa del Mundo QATAR 2022 '
    # Damos un estilo BodyText al segundo párrafo, que será el texto a escribir. 
    estilo = estiloHoja['BodyText']
    estilo.backColor = colors.fidred
    parrafo2 = Paragraph(cadena, estilo)
    # Y lo incluimos en el story.
    story.append(parrafo2)
    # Dejamos espacio.
    story.append(Spacer(0, 10))

def tabla():
    # Definimos las filas de una tabla.
    fila1 = ['','','Club','PJ','G','E','P','GF','GC','PUNTOS']
    fila2 = ['','1','Brasil','13','11','2','0','27','4','35']
    fila3 = ['','2','Argentina','13','8','5','0','20','6','29']
    fila4 = ['','3','Ecuador','14','7','2','5','23','13','23']
    fila11 = ['','4','Colombia','14','3','8','3','16','17','17']
    fila5 = ['','5','Peru','14','2','2','7','15','20','17']
    fila6 = ['','6','Chile','14','5','4','6','15','16','16']
    fila7 = ['','7','Uruguay','14','4','4','6','14','21','16']
    fila8 = ['','8','Bolivia','14','4','3','7','20','28','15']
    fila9 = ['','9','Paraguay','14','2','7','5','9','18','13']
    fila10 = ['','10','Venezuela','14','2','1','11','9','25','7']

    # Definimos la tabla.
    tabla = Table([fila1,fila2,fila3,fila4,fila11,fila5,fila6,fila7,fila9,fila10])

    # Podemos dar estilo a los elementos de una tabla. En esta ocasión vamos
    # a poner de color verde los paises clasificados y en color naranja el equipo a repechaje
    tabla.setStyle([
    ('TEXTCOLOR',(0,-5),(1,-5),colors.orangered),
    ('TEXTCOLOR',(0,0),(1,4),colors.green)
    ])
    # Y la asignamos al platypus story.
    story.append(tabla)

    # Damos color de fondo a las celdas.
    tabla.setStyle([('BACKGROUND',(1,1),(-1,-1),colors.lightgoldenrodyellow)])

    # Creamos una caja alrededor de las celdas.
    tabla.setStyle([('BOX',(1,1),(-1,-1),0.25,colors.black)])
    # Y ponemos una malla (rejilla) a la tabla.
    tabla.setStyle([('INNERGRID',(1,1),(-1,-1),0.25,colors.black)])


titulo()
imagenes()
subtitulo()
tabla()
# Construimos el Platypus story.

doc.build(story)
