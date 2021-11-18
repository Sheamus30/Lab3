# Laboratorio III - TP3
## Consigna:
Investigacion de libreria python ReportLab. Crear entorno virtual para instalar la libreria y hacer un ejemplo practico con dicha libreria.

## ReportLab:
ReportLab es el motor de código abierto ultra robusto y probado en el tiempo para crear documentos PDF complejos basados en datos y gráficos vectoriales personalizados.

## Librerias utilizadas:

reportlab

## Instalación:

pip install reportlab

Se adjunta en el repositorio un archivo Requirements.txt donde se muestra todas las librerias necesarias para la resolucion del trabajo practico.

## Creación de PDF sencillo  

- Importamos los modulos necesarios:

from reportlab.pdfgen import canvas

- Creamos el PDF vacio: 

doc = canvas.Canvas("Hola Mundo.pdf")

- Escribimos una cadena de Texto dentro del documento:

doc.drawString(100, 750, "Hola Mundo!!!")

- Guardamos el documento:

doc.save()


## Webgrafía

- ReportLab Python:	https://pypi.org/project/reportlab/

- ReportLab: https://www.reportlab.com/dev/opensource/

- Recursos Python: https://recursospython.com/guias-y-manuales/crear-documentos-pdf-en-python-con-reportlab/

- Guia completa de ReportLab: https://www.reportlab.com/docs/reportlab-userguide.pdf

- Diario Python: https://pythondiario.com/2017/10/creacion-de-archivos-pdf-con-python-y.html
