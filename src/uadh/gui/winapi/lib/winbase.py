'''
Created on 28/03/2012

@author: xXx
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