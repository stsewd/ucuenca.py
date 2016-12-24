# ucuenca.py

[![Build Status](https://travis-ci.org/stsewd/ucuenca.py.svg?branch=master)](https://travis-ci.org/stsewd/ucuenca.py)
[![PyPI version](https://badge.fury.io/py/ucuenca.svg)](https://badge.fury.io/py/ucuenca)

## Descripción

Librería de Python para la API de la [Universidad de Cuenca](http://www.ucuenca.edu.ec/).

## Dependencias

- Python 3.4 o superior.
- El paquete
  [requests](<http://docs.python-requests.org/en/master/user/install/>) debe
  estar instalado.

## Instalación

### Pip

```bash
pip install ucuenca
```

### Manual

```bash
git clone https://github.com/stsewd/ucuenca.py.git
cd ucuenca.py
pip install .
```

## Documentación

### Inicio Rápido

```python
from ucuenca import Ucuenca

uc = Ucuenca()
careers = uc.careers('0104926787')
careers['malla']  # MALLA CONTABILIDAD Y AUDITORIA 2008
careers['fecha_matricula']  # 2013-03-03 09:37:08.0
```

## Contribuir

Pull request son bienvenidos :snake:.
<!-- TODO -->

## Aviso

- Recuerda respetar la privacidad de los demás. No me hago responsable por el
  mal uso de la librería _ucuenca.py_.
- La librería _ucuenca.py_ es una implementación no oficial de la API de la
  Universidad de Cuenca.
- La librería _ucuenca.py_ es de libre distribución, está bajo la licencia [MIT](LICENSE)

