#
#
# Copyright 2011,2012 Luis Ariel Vega Soliz, Uremix (http://www.uremix.org) and contributors.
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
Created on 28/03/2012

@author: Luis Ariel Vega Soliz
'''
from ctypes import *
from ctypes.wintypes import LPCSTR


'''
WINBASEAPI
__out_opt
HMODULE
WINAPI
GetModuleHandleA(
    __in_opt LPCSTR lpModuleName
    );
'''

GetModuleHandleA = windll.kernel32.GetModuleHandleA
GetModuleHandleA.argtypes = [c_int]
GetModuleHandle = GetModuleHandleA