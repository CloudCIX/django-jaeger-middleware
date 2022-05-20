from setuptools import setup

__version__ = '1.0.1'

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='django-jaeger-middleware',
    version=__version__,
    url='https://github.com/cloudcix/django-jaeger-middleware',
    download_url='https://github.com/cloudcix/django-jaeger-middleware/releases/',
    license='MIT',
    author='cloudcix',
    author_email='developers@cix.ie',
    description='Django middleware to handle tracing requests using Jaeger Python Client.',
    long_description=long_description,
    packages=['django_jaeger'],
    install_requires=[
        'django==2.2.28',
        'jaeger-client',
        'opentracing',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
