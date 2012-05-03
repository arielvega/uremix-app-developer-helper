'''
Created on 27/03/2012

@author: xXx
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