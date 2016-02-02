textlocal
=========

For sending and receiving text messages (SMS & MMS) from textlocal.com.


Installation
------------

.. code-block:: bash

    pip install textlocal

Sending Messages
~~~~~~~~~~~~~~~~


.. code-block:: python

    from textlocal import Textlocal
    from textlocal.messages import SMS


    textlocal = Textlocal(api_key='your api key', from='you')
    message = SMS('440123456789', 'message')
    textlocal.send(message)
