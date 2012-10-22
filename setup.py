from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-expirefield',
    version='0.0.1',
    author='Jarrell Waggoner',
    author_email='malloc47@gmail.com',
    packages=find_packages(),
    url='https://github.com/malloc47/django-expirefield',
    license='LICENSE.txt',
    description='ExpireField for django models that will remove fields at regular intervals',
    install_requires=[
        "Django >= 1.4.0",
    ],
    download_url='https://github.com/malloc47/expirefield/tarball/master'
)
