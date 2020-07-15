# simuladorComputoDistribuido

## Descripción

Un sistema que simula la ejecución de distintos algoritmos distribuidos.

Por medio de una clase constructora, que se encarga que iniciar las
simulaciones, se instancían procesos que envían y reciben mensajes y están
regidos por las reglas y los algoritmos establecidos en el constructor.

Este sistema está diseñado para trabajar en `MacOS` y `Linux` limitado a la
descarga de las bibliotecas requeridas.

## Estructura general

El sistema de archivos se divide en dos categorías principales: documentos y
código.

### Codigo

El código se encuentra dentro de la carpeta `simulador` y tiene la estructura
para empaquetar proyectos de [python](https://packaging.python.org/tutorials/packaging-projects/).

El trabajo está hecho en Python 3 y trabaja con las siguientes bibliotecas:

- [Simpy](https://simpy.readthedocs.io/en/latest/contents.html)
- [NetworkX](https://networkx.github.io/)

### Documentos

El documento principal es `EstructuraDeSistema.tex` que sirve cómo registro del
diseño del sistema, sus requerimientos, detalles generales y de los avances y
cambios hechos en el mismo. A este archvo se le liga `bibliografia.bib` que
contiene las bibliografías usadas en el curso.

Hay también dos scripts:
- `elimina.sh` que se encarga de eliminar todos los archivos generados del
  repositorio local y
- `bib.sh` que compila el archivo .tex las veces necesarias para generar la
  bibliografía, el índice y las referencias.

## Descarga y Ejecución

**Pendiente**
