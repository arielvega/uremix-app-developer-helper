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
from ctypes import WinError

# ====================
# The problem with long ints: The builtin long->int conversion fails
# for longs with the 31st bit set, because they are technically
# outside the range of a signed 32-bit integer.  However, many times
# we need to be able to pass the Windows API 32-bit quantities with
# this bit set.  So we need a way to convert from an unsigned long
# greater than 1<<31 (0x8000.0000) to its equivalent two's complement
# negative signed integer.
# I won't claim this is the best way, the only other way that comes to
# mind is to convert the number to a string and eval it (ick).
# (int(n>>1)<<1)+int(n&1)
# ====================

def safe_long (n):
    return (int(n>>1)<<1)+int(n&1)

def ErrorIfZero(handle):
    if handle == 0:
        raise WinError()
    else:
        return handle