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

***Nota:** Si tienes instalado python2 y python3 en tu sistema,
asegúrate de usar el comando ``pip3`` en lugar de ``pip`` en las
siguientes instrucciones.*

Usando `pip <https://pip.pypa.io/en/stable/quickstart/>`__ (recomendada)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En una terminal (ventana de comandos), ejecuta:

.. code:: bash

    pip install ucuenca

De manera manual
~~~~~~~~~~~~~~~~

En una terminal (ventana de comandos), ejecuta:

.. code:: bash

    git clone https://github.com/stsewd/ucuenca.py.git
    cd ucuenca.py
    pip install .

Inicio Rápido
-------------

Para empezar a usar la librería, instala *ucuenca.py*, crea un objeto
Ucuenca y haz uso de sus métodos.

.. code:: python

    from ucuenca import Ucuenca

    uc = Ucuenca()
    # Un estudiante puede cursar varias carreras,
    # obtenemos una sola.
    careers = uc.careers('0104926787')[0]
    careers['malla']  # MALLA CONTABILIDAD Y AUDITORIA 2008
    careers['fecha_matricula']  # 2013-03-03 09:37:08.0

Documentación
-------------

Por ahora, para ver la documentación se puede hacer uso de la función de
python
`*help* <https://docs.python.org/3/library/functions.html#help>`__.

.. code:: python

    from ucuenca import Ucuenca

    help(Ucuenca)

Contribuir
----------

Si encuentras un error, tienes ideas de cómo mejorar el proyecto,
házmelo saber creando un
`issue <https://github.com/stsewd/ucuenca.py/issues/new>`__.

`Pull
requests <https://help.github.com/articles/about-pull-requests/>`__ son
bienvenidos :snake:.

Aviso
-----

-  Recuerda respetar la privacidad de los demás. No me hago responsable
   por el mal uso de la librería *ucuenca.py*.
-  La librería *ucuenca.py* es una implementación no oficial de la API
   de la Universidad de Cuenca.
-  La librería *ucuenca.py* es de libre distribución, está bajo la
   licencia `MIT <LICENSE>`__.
-  Los ejemplos mostrados aquí son los mismos usados en la página de la
   API.

.. |Build Status| image:: https://travis-ci.org/stsewd/ucuenca.py.svg?branch=master
   :target: https://travis-ci.org/stsewd/ucuenca.py
.. |PyPI version| image:: https://badge.fury.io/py/ucuenca.svg
   :target: https://badge.fury.io/py/ucuenca
