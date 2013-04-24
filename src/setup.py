#
#
# Copyright 2011,2013 Luis Ariel Vega Soliz, Uremix (http://www.uremix.org) and contributors.
#
#
# This file is part of UADH (Uremix App Developer Helper).
#
#    UADH is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    UADH is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with UADH.  If not, see <http://www.gnu.org/licenses/>.
#
#


'''
Created on 26/10/2011

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

'''

from setuptools import setup, find_packages  
  
setup(name='uremix-app-developer-helper',
      version='0.3.1',
      description='Un conjunto de procedimientos de ayuda para el desarrollo de aplicaciones en Uremix (http://uremix.org)',
      author='Luis Ariel Vega Soliz',
      author_email='vsoliz.ariel@gmail.com',
      url='https://github.com/arielvega/uremix-app-developer-helper',
      license='GPL v3',
      packages = find_packages(),
      install_requires = ['python-configobj', 'python-gtk2']
)
