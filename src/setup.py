'''
Created on 26/10/2011

@author: ariel
'''

from setuptools import setup, find_packages  
  
setup(name='uremix-app-developer-helper',
      version='0.1',
      description='Un conjunto de procedimientos de ayuda para el desarrollo de aplicaciones en Uremix',
      author='Luis Ariel Vega Soliz',
      author_email='vsoliz.ariel@gmail.com',
      url='https://github.com/arielvega/uremix-app-developer-helper',
      license='GPL v3',
      py_modules=['mobile'],
      packages = find_packages(),
      install_requires = ['python-configobj', 'python-gtk2']
)
