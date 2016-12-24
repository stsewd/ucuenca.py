ucuenca.py
==========

|Build Status| |PyPI version|

Descripción
-----------

Librería de Python para la API de la `Universidad de
Cuenca <http://www.ucuenca.edu.ec/>`__.

Dependencias
------------

-  Python 3.4 o superior.
-  El paquete
   `requests <http://docs.python-requests.org/en/master/user/install/>`__
   debe estar instalado.

Instalación
-----------

Pip
~~~

.. code:: bash

    pip install ucuenca

Manual
~~~~~~

.. code:: bash

    git clone https://github.com/stsewd/ucuenca.py.git
    cd ucuenca.py
    pip install .

Documentación
-------------

Inicio Rápido
~~~~~~~~~~~~~

.. code:: python

    from ucuenca import Ucuenca

    uc = Ucuenca()
    careers = uc.careers('0104926787')
    careers['malla']  # MALLA CONTABILIDAD Y AUDITORIA 2008
    careers['fecha_matricula']  # 2013-03-03 09:37:08.0

Contribuir
----------

Pull request son bienvenidos :snake:.

Aviso
-----

-  Recuerda respetar la privacidad de los demás. No me hago responsable
   por el mal uso de la librería *ucuenca.py*.
-  La librería *ucuenca.py* es una implementación no oficial de la API
   de la Universidad de Cuenca.
-  La librería *ucuenca.py* es de libre distribución, está bajo la
   licencia `MIT <LICENSE>`__

.. |Build Status| image:: https://travis-ci.org/stsewd/ucuenca.py.svg?branch=master
   :target: https://travis-ci.org/stsewd/ucuenca.py
.. |PyPI version| image:: https://badge.fury.io/py/ucuenca.svg
   :target: https://badge.fury.io/py/ucuenca
