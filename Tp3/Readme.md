# Laboratorio III - TP3
## Consigna:
Investigacion de libreria python ReportLab. Crear entorno virtual para instalar la libreria y hacer un ejemplo practico con dicha libreria.

## ReportLab:
ReportLab es el motor de código abierto ultra robusto y probado en el tiempo para crear documentos PDF complejos basados en datos y gráficos vectoriales personalizados.

## Librerias utilizadas:
Pillow

reportlab

## Instalación:

pip install reportlab

Se adjunta en el repositorio un archivo Requirements.txt donde se muestra todas las librerias necesarias para la resolucion del trabajo practico.

## Utilizacion de PLATYPUS
Se crea un documento a partir de la clase DocTemplate y se le pasa una lista de Flowables mediante el método build. Para ello se construye un Platypus story, que consiste en una secuencia de elementos básicos Flowables, que son formateados.
- DocTemplates - La plantilla del documento. El contenedor último de un documento.
- PageTemplates - Las especificaciones para diseñar páginas de varias clases.
- Frames - Las especificaciones de regiones en la páginas que pueden contener texto ó gráficos.
- Flowables - Elementos de texto ó gráficos que están incrustados en el documento (párrafos, tablas, imágenes, pero no pies de página, por ejemplo).

## Webgrafía

- ReportLab Python:	https://pypi.org/project/reportlab/

- ReportLab: https://www.reportlab.com/dev/opensource/

- Recursos Python: https://recursospython.com/guias-y-manuales/crear-documentos-pdf-en-python-con-reportlab/

- Guia completa de ReportLab: https://www.reportlab.com/docs/reportlab-userguide.pdf

- Diario Python: https://pythondiario.com/2017/10/creacion-de-archivos-pdf-con-python-y.html
