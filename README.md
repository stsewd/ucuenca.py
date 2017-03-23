# ucuenca.py

[![Build Status](https://travis-ci.org/stsewd/ucuenca.py.svg?branch=master)](https://travis-ci.org/stsewd/ucuenca.py)
[![PyPI version](https://badge.fury.io/py/ucuenca.svg)](https://badge.fury.io/py/ucuenca)
[![codecov](https://codecov.io/gh/stsewd/ucuenca.py/branch/master/graph/badge.svg)](https://codecov.io/gh/stsewd/ucuenca.py)

## Descripción

Librería de Python para la API de la [Universidad de Cuenca](http://www.ucuenca.edu.ec/).

## Dependencias

- Python 3.4 o superior.
- El paquete
  [requests](<http://docs.python-requests.org/en/master/user/install/>) debe
  estar instalado.

## Instalación

_**Nota:** Si tienes instalado python2 y python3 en tu sistema, asegúrate de usar el comando `pip3` en lugar de `pip` en las siguientes instrucciones._

### Usando [pip](<https://pip.pypa.io/en/stable/quickstart/>) (recomendada)

En una terminal (ventana de comandos), ejecuta:

```bash
pip install ucuenca
```

### De manera manual

En una terminal (ventana de comandos), ejecuta:

```bash
git clone https://github.com/stsewd/ucuenca.py.git
cd ucuenca.py
pip install .
```

## Inicio Rápido

Para empezar a usar la librería, instala _ucuenca.py_, crea un objeto Ucuenca y haz uso de sus métodos.

```python
from ucuenca import Ucuenca

uc = Ucuenca()
# Un estudiante puede cursar varias carreras,
# obtenemos una sola.
careers = uc.careers('0104926787')[0]
careers['malla']  # MALLA CONTABILIDAD Y AUDITORIA 2008
careers['fecha_matricula']  # 2013-03-03 09:37:08.0
```

## Documentación

Por ahora, para ver la documentación se puede hacer uso de la función de python [_help_](<https://docs.python.org/3/library/functions.html#help>).

```python
from ucuenca import Ucuenca

help(Ucuenca)
```

Adicionalmente, existen varios ejemplos del uso de la librería en el directorio [`examples`](examples/).

## Contribuir

Si encuentras un error, tienes ideas de cómo mejorar el proyecto, házmelo saber creando un [issue](<https://github.com/stsewd/ucuenca.py/issues/new>).

[Pull requests](<https://help.github.com/articles/about-pull-requests/>) son bienvenidos :snake:.

## Aviso

- Recuerda respetar la privacidad de los demás. No me hago responsable por el
  mal uso de la librería _ucuenca.py_.
- La librería _ucuenca.py_ es una implementación no oficial de la API de la
  Universidad de Cuenca.
- La librería _ucuenca.py_ es de libre distribución, está bajo la licencia [MIT](LICENSE).
- Los ejemplos mostrados aquí son los mismos usados en la página de la API.
