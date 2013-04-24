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
Created on 27/03/2012

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

'''
from ctypes import c_long, Structure, c_ulong, c_uint
from ctypes.wintypes import WORD, BYTE, DWORD, LONG, INT




STRICT                  = 1
MAX_PATH                = 260

NULL                    = 0
FALSE                   = 0
TRUE                    = 1


def MAKEWORD(a, b):
    '''
    #define MAKEWORD(a, b)      ((WORD)(((BYTE)(((DWORD_PTR)(a)) & 0xff)) | ((WORD)((BYTE)(((DWORD_PTR)(b)) & 0xff))) << 8))
    '''
    return ((a & 0x000000ff)  | ((b & 0x000000ff) << 8))


def MAKELONG(a, b):
    '''
    #define MAKELONG(a, b)      ((LONG)(((WORD)(((DWORD_PTR)(a)) & 0xffff)) | ((DWORD)((WORD)(((DWORD_PTR)(b)) & 0xffff))) << 16))
    '''
    return ((a & 0x0000ffff) | ((b & 0x0000ffff)<< 16))


def LOWORD(l):
    '''
    #define LOWORD(l)           ((WORD)(((DWORD_PTR)(l)) & 0xffff))
    '''
    return (l & 0x0000ffff)

def HIWORD(l):
    '''
    #define HIWORD(l)           ((WORD)((((DWORD_PTR)(l)) >> 16) & 0xffff))
    '''
    return ((l >> 16) & 0x0000ffff)

def LOBYTE(w):
    '''
    #define LOBYTE(w)           ((BYTE)(((DWORD_PTR)(w)) & 0xff))
    '''
    return (w & 0x000000ff)

def HIBYTE(w):
    '''
    #define HIBYTE(w)           ((BYTE)((((DWORD_PTR)(w)) >> 8) & 0xff))
    '''
    return ((w >> 8) & 0x000000ff)



class RECT(Structure):
    _fields_ = [('left', c_long),
                ('top', c_long),
                ('right', c_long),
                ('bottom', c_long)]

tagRECT = _RECTL = RECTL = RECT

'''
typedef struct tagRECT
{
    LONG    left;
    LONG    top;
    LONG    right;
    LONG    bottom;
} RECT, *PRECT, NEAR *NPRECT, FAR *LPRECT;
'''

class POINT(Structure):
    _fields_ = [('x', c_long),
                ('y', c_long)]

tagPOINT = _POINTL = POINTL = POINT

# mode selections for the device mode function
DM_UPDATE               = 1
DM_COPY                 = 2
DM_PROMPT               = 4
DM_MODIFY               = 8

DM_IN_BUFFER            = DM_MODIFY
DM_IN_PROMPT            = DM_PROMPT
DM_OUT_BUFFER           = DM_COPY
DM_OUT_DEFAULT          = DM_UPDATE

# device capabilities indices
DC_FIELDS               = 1
DC_PAPERS               = 2
DC_PAPERSIZE            = 3
DC_MINEXTENT            = 4
DC_MAXEXTENT            = 5
DC_BINS                 = 6
DC_DUPLEX               = 7
DC_SIZE                 = 8
DC_EXTRA                = 9
DC_VERSION              = 10
DC_DRIVER               = 11
DC_BINNAMES             = 12
DC_ENUMRESOLUTIONS      = 13
DC_FILEDEPENDENCIES     = 14
DC_TRUETYPE             = 15
DC_PAPERNAMES           = 16
DC_ORIENTATION          = 17
DC_COPIES               = 18