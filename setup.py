import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-clave-unica',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='Aplicacion Django para integración con autenticación Clave Única',
    long_description=README,
    url='https://github.com/GatoSnake',
    author='Cristhian Won',
    author_email='cristhian.won@gmail.com',
    long_description_content_type="text/markdown",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'requests>=2.22.0',
        'urllib3>=1.25.3'
    ],
)
