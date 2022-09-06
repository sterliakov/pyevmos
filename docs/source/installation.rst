Installation
============

You can install ``evmos`` with ``pip``:

.. code-block:: bash

    pip install -U evmos

Installing from source:

.. code-block:: bash

    git clone https://github.com/sterliakov/pyevmos/
    cd pyevmos
    pip install .


Supported extras:

- ``test``: install test dependencies (``pip install evmos[test]``)
- ``dev``: install development dependencies (``pip install evmos[dev]``). Currently this includes only ``protobuf`` compiler for rebuilding ``proto/autogen`` folder content.
- ``docs``: dependencies for building documentation (``pip install evmos[docs]``)
