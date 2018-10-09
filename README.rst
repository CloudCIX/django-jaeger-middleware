========================
django-jaeger-middleware
========================

Custom middleware to use Jaeger_ inside in Django because the Opentracing lib doesn't work.

Usage
-----
First, install the library;

.. code:: $ python3 -m pip install git+https://github.com/cloudcix/django-jaeger-middleware@master

Next, add the necessary settings to your Django project's settings file;

- ``TRACER_CONFIG``
    - A dictionary containing config for the Jaeger tracer instances.
    - See the docs_ for more information.
- ``TRACER_SERVICE_NAME``
    - The name of the application / project the tracer is being used for.

Lastly, add the middleware to the top of your middleware stack;

.. code:: MIDDLEWARE_CLASSES = [
        'django_jaeger.middleware.DjangoJaegerMiddleware',
    ]

This will wrap the entirety of the request in a span, and also attach the parent span to the request object as ``request.span``.
It will also save the tracer object back into the settings object for use in other parts of the code.
This is so you can create child spans using the jaeger client in your views like so;

.. code:: with settings.TRACER.start_span('child_span', child_of=request.span) as span:
        # Do stuff here

.. _Jaeger: https://www.jaegertracing.io
.. _docs: https://github.com/jaegertracing/jaeger-client-python/blob/master/jaeger_client/config.py
