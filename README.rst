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
This span object will continue an existing span if one exists.
It will also create ``settings.TRACER`` which is a pointer to the tracer instance, which will be necessary for creating intermediate spans.

To add child spans to http requests to the same django system (to prevent new spans from being created for intermediate requests), you have to add headers to the request like this;

.. code:: request = request
    headers = {}
    settings.TRACER.inject(request.span, opentracing.Format.TEXT_MAP, headers):
    for k, v in headers.items():
        request.add_header(k, v)
    # Make your request

If you want to create a child span for something that doesn't go through your Django project (for example, for a database request), you can do the following;

.. code:: with settings.TRACER.start_span('child_span', child_of=request.span) as span:
        # Do stuff here

.. _Jaeger: https://www.jaegertracing.io
.. _docs: https://github.com/jaegertracing/jaeger-client-python/blob/master/jaeger_client/config.py
