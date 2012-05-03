'''
Created on 26/03/2012

@author: xXx
'''

from ctypes import *


from uadh.gui.winapi.lib import auxfuncs, windef
from ctypes.wintypes import RECT, POINT, HWND, HMENU, DWORD, HANDLE, BOOL, HDC,\
    UINT, WPARAM, LPARAM, HINSTANCE, HICON, WORD, INT
from uadh.gui.winapi.lib.windef import TRUE
from uadh.gui.winapi.lib.auxfuncs import ErrorIfZero

WNDPROC = WINFUNCTYPE(c_long, c_int, c_uint, c_int, c_int)

'''
typedef LRESULT (CALLBACK* WNDPROC)(HWND, UINT, WPARAM, LPARAM);
'''

# Scroll Bar Constants

SB_HORZ           = 0
SB_VERT           = 1
SB_CTL            = 2
SB_BOTH           = 3


# Scroll Bar Commands

SB_LINEUP         = 0
SB_LINELEFT       = 0
SB_LINEDOWN       = 1
SB_LINERIGHT      = 1
SB_PAGEUP         = 2
SB_PAGELEFT       = 2
SB_PAGEDOWN       = 3
SB_PAGERIGHT      = 3
SB_THUMBPOSITION  = 4
SB_THUMBTRACK     = 5
SB_TOP            = 6
SB_LEFT           = 6
SB_BOTTOM         = 7
SB_RIGHT          = 7
SB_ENDSCROLL      = 8


# ShowWindow() Commands

SW_HIDE            = 0
SW_SHOWNORMAL      = 1
SW_NORMAL          = 1
SW_SHOWMINIMIZED   = 2
SW_SHOWMAXIMIZED   = 3
SW_MAXIMIZE        = 3
SW_SHOWNOACTIVATE  = 4
SW_SHOW            = 5
SW_MINIMIZE        = 6
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA          = 8
SW_RESTORE         = 9
SW_SHOWDEFAULT     = 10
SW_FORCEMINIMIZE   = 11
SW_MAX             = 11



# Old ShowWindow() Commands

HIDE_WINDOW         = 0
SHOW_OPENWINDOW     = 1
SHOW_ICONWINDOW     = 2
SHOW_FULLSCREEN     = 3
SHOW_OPENNOACTIVATE = 4


# Identifiers for the WM_SHOWWINDOW message

SW_PARENTCLOSING    = 1
SW_OTHERZOOM        = 2
SW_PARENTOPENING    = 3
SW_OTHERUNZOOM      = 4


# AnimateWindow() Commands

AW_HOR_POSITIVE           = 0x00000001
AW_HOR_NEGATIVE           = 0x00000002
AW_VER_POSITIVE           = 0x00000004
AW_VER_NEGATIVE           = 0x00000008
AW_CENTER                 = 0x00000010
AW_HIDE                   = 0x00010000
AW_ACTIVATE               = 0x00020000
AW_SLIDE                  = 0x00040000
AW_BLEND                  = 0x00080000


# WM_KEYUP/DOWN/CHAR HIWORD(lParam) flags

KF_EXTENDED     = 0x0100
KF_DLGMODE      = 0x0800
KF_MENUMODE     = 0x1000
KF_ALTDOWN      = 0x2000
KF_REPEAT       = 0x4000
KF_UP           = 0x8000



# Virtual Keys, Standard Set

VK_LBUTTON      = 0x01
VK_RBUTTON      = 0x02
VK_CANCEL       = 0x03
VK_MBUTTON      = 0x04     #NOT contiguous with L & RBUTTON
VK_XBUTTON1     = 0x05     #NOT contiguous with L & RBUTTON
VK_XBUTTON2     = 0x06     #NOT contiguous with L & RBUTTON



# 0x07 : unassigned


VK_BACK         = 0x08
VK_TAB          = 0x09


# 0x0A - 0x0B : reserved


VK_CLEAR        = 0x0C
VK_RETURN       = 0x0D

VK_SHIFT        = 0x10
VK_CONTROL      = 0x11
VK_MENU         = 0x12
VK_PAUSE        = 0x13
VK_CAPITAL      = 0x14

VK_KANA         = 0x15
VK_HANGEUL      = 0x15   #old name - should be here for compatibility
VK_HANGUL       = 0x15
VK_JUNJA        = 0x17
VK_FINAL        = 0x18
VK_HANJA        = 0x19
VK_KANJI        = 0x19

VK_ESCAPE       = 0x1B

VK_CONVERT      = 0x1C
VK_NONCONVERT   = 0x1D
VK_ACCEPT       = 0x1E
VK_MODECHANGE   = 0x1F

VK_SPACE        = 0x20
VK_PRIOR        = 0x21
VK_NEXT         = 0x22
VK_END          = 0x23
VK_HOME         = 0x24
VK_LEFT         = 0x25
VK_UP           = 0x26
VK_RIGHT        = 0x27
VK_DOWN         = 0x28
VK_SELECT       = 0x29
VK_PRINT        = 0x2A
VK_EXECUTE      = 0x2B
VK_SNAPSHOT     = 0x2C
VK_INSERT       = 0x2D
VK_DELETE       = 0x2E
VK_HELP         = 0x2F


# VK_0 - VK_9 are the same as ASCII '0' - '9' (0x30 - 0x39)
# 0x40 : unassigned
# VK_A - VK_Z are the same as ASCII 'A' - 'Z' (0x41 - 0x5A)


VK_LWIN         = 0x5B
VK_RWIN         = 0x5C
VK_APPS         = 0x5D


# 0x5E : reserved


VK_SLEEP        = 0x5F

VK_NUMPAD0      = 0x60
VK_NUMPAD1      = 0x61
VK_NUMPAD2      = 0x62
VK_NUMPAD3      = 0x63
VK_NUMPAD4      = 0x64
VK_NUMPAD5      = 0x65
VK_NUMPAD6      = 0x66
VK_NUMPAD7      = 0x67
VK_NUMPAD8      = 0x68
VK_NUMPAD9      = 0x69
VK_MULTIPLY     = 0x6A
VK_ADD          = 0x6B
VK_SEPARATOR    = 0x6C
VK_SUBTRACT     = 0x6D
VK_DECIMAL      = 0x6E
VK_DIVIDE       = 0x6F
VK_F1           = 0x70
VK_F2           = 0x71
VK_F3           = 0x72
VK_F4           = 0x73
VK_F5           = 0x74
VK_F6           = 0x75
VK_F7           = 0x76
VK_F8           = 0x77
VK_F9           = 0x78
VK_F10          = 0x79
VK_F11          = 0x7A
VK_F12          = 0x7B
VK_F13          = 0x7C
VK_F14          = 0x7D
VK_F15          = 0x7E
VK_F16          = 0x7F
VK_F17          = 0x80
VK_F18          = 0x81
VK_F19          = 0x82
VK_F20          = 0x83
VK_F21          = 0x84
VK_F22          = 0x85
VK_F23          = 0x86
VK_F24          = 0x87


# 0x88 - 0x8F : unassigned


VK_NUMLOCK      = 0x90
VK_SCROLL       = 0x91


# NEC PC-9800 kbd definitions

VK_OEM_NEC_EQUAL= 0x92   # '=' key on numpad


# Fujitsu/OASYS kbd definitions

VK_OEM_FJ_JISHO   = 0x92   # 'Dictionary' key
VK_OEM_FJ_MASSHOU = 0x93   # 'Unregister word' key
VK_OEM_FJ_TOUROKU = 0x94   # 'Register word' key
VK_OEM_FJ_LOYA    = 0x95   # 'Left OYAYUBI' key
VK_OEM_FJ_ROYA    = 0x96   # 'Right OYAYUBI' key


# 0x97 - 0x9F : unassigned



# VK_L* & VK_R* - left and right Alt, Ctrl and Shift virtual keys.
# Used only as parameters to GetAsyncKeyState() and GetKeyState().
# No other API or message will distinguish left and right keys in this way.

VK_LSHIFT       = 0xA0
VK_RSHIFT       = 0xA1
VK_LCONTROL     = 0xA2
VK_RCONTROL     = 0xA3
VK_LMENU        = 0xA4
VK_RMENU        = 0xA5

VK_BROWSER_BACK      = 0xA6
VK_BROWSER_FORWARD   = 0xA7
VK_BROWSER_REFRESH   = 0xA8
VK_BROWSER_STOP      = 0xA9
VK_BROWSER_SEARCH    = 0xAA
VK_BROWSER_FAVORITES = 0xAB
VK_BROWSER_HOME      = 0xAC

VK_VOLUME_MUTE       = 0xAD
VK_VOLUME_DOWN       = 0xAE
VK_VOLUME_UP         = 0xAF
VK_MEDIA_NEXT_TRACK  = 0xB0
VK_MEDIA_PREV_TRACK  = 0xB1
VK_MEDIA_STOP        = 0xB2
VK_MEDIA_PLAY_PAUSE  = 0xB3
VK_LAUNCH_MAIL       = 0xB4
VK_LAUNCH_MEDIA_SELECT = 0xB5
VK_LAUNCH_APP1       = 0xB6
VK_LAUNCH_APP2       = 0xB7


# 0xB8 - 0xB9 : reserved


VK_OEM_1        = 0xBA   # ';:' for US
VK_OEM_PLUS     = 0xBB   # '+' any country
VK_OEM_COMMA    = 0xBC   # ',' any country
VK_OEM_MINUS    = 0xBD   # '-' any country
VK_OEM_PERIOD   = 0xBE   # '.' any country
VK_OEM_2        = 0xBF   # '/?' for US
VK_OEM_3        = 0xC0   # '`~' for US


# 0xC1 - 0xD7 : reserved



# 0xD8 - 0xDA : unassigned


VK_OEM_4        = 0xDB  #  '[{' for US
VK_OEM_5        = 0xDC  #  '\|' for US
VK_OEM_6        = 0xDD  #  ']}' for US
VK_OEM_7        = 0xDE  #  ''"' for US
VK_OEM_8        = 0xDF


# 0xE0 : reserved



# Various extended or enhanced keyboards

VK_OEM_AX       = 0xE1  #  'AX' key on Japanese AX kbd
VK_OEM_102      = 0xE2  #  "<>" or "\|" on RT 102-key kbd.
VK_ICO_HELP     = 0xE3  #  Help key on ICO
VK_ICO_00       = 0xE4  #  00 key on ICO

VK_PROCESSKEY   = 0xE5

VK_ICO_CLEAR    = 0xE6

VK_PACKET       = 0xE7


# 0xE8 : unassigned



# Nokia/Ericsson definitions

VK_OEM_RESET    = 0xE9
VK_OEM_JUMP     = 0xEA
VK_OEM_PA1      = 0xEB
VK_OEM_PA2      = 0xEC
VK_OEM_PA3      = 0xED
VK_OEM_WSCTRL   = 0xEE
VK_OEM_CUSEL    = 0xEF
VK_OEM_ATTN     = 0xF0
VK_OEM_FINISH   = 0xF1
VK_OEM_COPY     = 0xF2
VK_OEM_AUTO     = 0xF3
VK_OEM_ENLW     = 0xF4
VK_OEM_BACKTAB  = 0xF5

VK_ATTN         = 0xF6
VK_CRSEL        = 0xF7
VK_EXSEL        = 0xF8
VK_EREOF        = 0xF9
VK_PLAY         = 0xFA
VK_ZOOM         = 0xFB
VK_NONAME       = 0xFC
VK_PA1          = 0xFD
VK_OEM_CLEAR    = 0xFE


# 0xFF : reserved

 
 

# SetWindowsHook() codes

WH_MIN              = (-1)
WH_MSGFILTER        = (-1)
WH_JOURNALRECORD    = 0
WH_JOURNALPLAYBACK  = 1
WH_KEYBOARD         = 2
WH_GETMESSAGE       = 3
WH_CALLWNDPROC      = 4
WH_CBT              = 5
WH_SYSMSGFILTER     = 6
WH_MOUSE            = 7

WH_HARDWARE         = 8

WH_DEBUG            = 9
WH_SHELL            = 10
WH_FOREGROUNDIDLE   = 11

WH_CALLWNDPROCRET   = 12

WH_KEYBOARD_LL      = 13
WH_MOUSE_LL         = 14

WH_MAX              = 14

WH_MINHOOK          = WH_MIN
WH_MAXHOOK          = WH_MAX


# Hook Codes

HC_ACTION           = 0
HC_GETNEXT          = 1
HC_SKIP             = 2
HC_NOREMOVE         = 3
HC_NOREM            = HC_NOREMOVE
HC_SYSMODALON       = 4
HC_SYSMODALOFF      = 5


# CBT Hook Codes

HCBT_MOVESIZE       = 0
HCBT_MINMAX         = 1
HCBT_QS             = 2
HCBT_CREATEWND      = 3
HCBT_DESTROYWND     = 4
HCBT_ACTIVATE       = 5
HCBT_CLICKSKIPPED   = 6
HCBT_KEYSKIPPED     = 7
HCBT_SYSCOMMAND     = 8
HCBT_SETFOCUS       = 9


# codes passed in WPARAM for WM_WTSSESSION_CHANGE


WTS_CONSOLE_CONNECT              = 0x1
WTS_CONSOLE_DISCONNECT           = 0x2
WTS_REMOTE_CONNECT               = 0x3
WTS_REMOTE_DISCONNECT            = 0x4
WTS_SESSION_LOGON                = 0x5
WTS_SESSION_LOGOFF               = 0x6
WTS_SESSION_LOCK                 = 0x7
WTS_SESSION_UNLOCK               = 0x8
WTS_SESSION_REMOTE_CONTROL       = 0x9




# WH_MSGFILTER Filter Proc Codes

MSGF_DIALOGBOX      = 0
MSGF_MESSAGEBOX     = 1
MSGF_MENU           = 2
MSGF_SCROLLBAR      = 5
MSGF_NEXTWINDOW     = 6
MSGF_MAX            = 8                       # unused
MSGF_USER           = 4096


# Shell support

HSHELL_WINDOWCREATED        = 1
HSHELL_WINDOWDESTROYED      = 2
HSHELL_ACTIVATESHELLWINDOW  = 3

HSHELL_WINDOWACTIVATED      = 4
HSHELL_GETMINRECT           = 5
HSHELL_REDRAW               = 6
HSHELL_TASKMAN              = 7
HSHELL_LANGUAGE             = 8
HSHELL_SYSMENU              = 9
HSHELL_ENDTASK              = 10

HSHELL_ACCESSIBILITYSTATE   = 11
HSHELL_APPCOMMAND           = 12

HSHELL_WINDOWREPLACED       = 13
HSHELL_WINDOWREPLACING      = 14

HSHELL_HIGHBIT            = 0x8000
HSHELL_FLASH              = (HSHELL_REDRAW|HSHELL_HIGHBIT)
HSHELL_RUDEAPPACTIVATED   = (HSHELL_WINDOWACTIVATED|HSHELL_HIGHBIT)

# cmd for HSHELL_APPCOMMAND and WM_APPCOMMAND
APPCOMMAND_BROWSER_BACKWARD       = 1
APPCOMMAND_BROWSER_FORWARD        = 2
APPCOMMAND_BROWSER_REFRESH        = 3
APPCOMMAND_BROWSER_STOP           = 4
APPCOMMAND_BROWSER_SEARCH         = 5
APPCOMMAND_BROWSER_FAVORITES      = 6
APPCOMMAND_BROWSER_HOME           = 7
APPCOMMAND_VOLUME_MUTE            = 8
APPCOMMAND_VOLUME_DOWN            = 9
APPCOMMAND_VOLUME_UP              = 10
APPCOMMAND_MEDIA_NEXTTRACK        = 11
APPCOMMAND_MEDIA_PREVIOUSTRACK    = 12
APPCOMMAND_MEDIA_STOP             = 13
APPCOMMAND_MEDIA_PLAY_PAUSE       = 14
APPCOMMAND_LAUNCH_MAIL            = 15
APPCOMMAND_LAUNCH_MEDIA_SELECT    = 16
APPCOMMAND_LAUNCH_APP1            = 17
APPCOMMAND_LAUNCH_APP2            = 18
APPCOMMAND_BASS_DOWN              = 19
APPCOMMAND_BASS_BOOST             = 20
APPCOMMAND_BASS_UP                = 21
APPCOMMAND_TREBLE_DOWN            = 22
APPCOMMAND_TREBLE_UP              = 23
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 24
APPCOMMAND_MICROPHONE_VOLUME_DOWN = 25
APPCOMMAND_MICROPHONE_VOLUME_UP   = 26
APPCOMMAND_HELP                   = 27
APPCOMMAND_FIND                   = 28
APPCOMMAND_NEW                    = 29
APPCOMMAND_OPEN                   = 30
APPCOMMAND_CLOSE                  = 31
APPCOMMAND_SAVE                   = 32
APPCOMMAND_PRINT                  = 33
APPCOMMAND_UNDO                   = 34
APPCOMMAND_REDO                   = 35
APPCOMMAND_COPY                   = 36
APPCOMMAND_CUT                    = 37
APPCOMMAND_PASTE                  = 38
APPCOMMAND_REPLY_TO_MAIL          = 39
APPCOMMAND_FORWARD_MAIL           = 40
APPCOMMAND_SEND_MAIL              = 41
APPCOMMAND_SPELL_CHECK            = 42
APPCOMMAND_DICTATE_OR_COMMAND_CONTROL_TOGGLE    = 43
APPCOMMAND_MIC_ON_OFF_TOGGLE      = 44
APPCOMMAND_CORRECTION_LIST        = 45
APPCOMMAND_MEDIA_PLAY             = 46
APPCOMMAND_MEDIA_PAUSE            = 47
APPCOMMAND_MEDIA_RECORD           = 48
APPCOMMAND_MEDIA_FAST_FORWARD     = 49
APPCOMMAND_MEDIA_REWIND           = 50
APPCOMMAND_MEDIA_CHANNEL_UP       = 51
APPCOMMAND_MEDIA_CHANNEL_DOWN     = 52
APPCOMMAND_DELETE                 = 53
APPCOMMAND_DWM_FLIP3D             = 54

FAPPCOMMAND_MOUSE = 0x8000
FAPPCOMMAND_KEY   = 0
FAPPCOMMAND_OEM = 0x1000
FAPPCOMMAND_MASK = 0xF000


# Low level hook flags


LLKHF_EXTENDED     = (KF_EXTENDED >> 8)
LLKHF_INJECTED     = 0x00000010
LLKHF_ALTDOWN      = (KF_ALTDOWN >> 8)
LLKHF_UP           = (KF_UP >> 8)

LLMHF_INJECTED     = 0x00000001


# Keyboard Layout API

HKL_PREV            = 0
HKL_NEXT            = 1


KLF_ACTIVATE      = 0x00000001
KLF_SUBSTITUTE_OK = 0x00000002
KLF_REORDER       = 0x00000008

KLF_REPLACELANG   = 0x00000010
KLF_NOTELLSHELL   = 0x00000080

KLF_SETFORPROCESS = 0x00000100

KLF_SHIFTLOCK     = 0x00010000
KLF_RESET         = 0x40000000


# Bits in wParam of WM_INPUTLANGCHANGEREQUEST message

INPUTLANGCHANGE_SYSCHARSET = 0x0001
INPUTLANGCHANGE_FORWARD    = 0x0002
INPUTLANGCHANGE_BACKWARD   = 0x0004



# Size of KeyboardLayoutName (number of characters), including nul terminator

KL_NAMELENGTH = 9


# Desktop-specific access flags

DESKTOP_READOBJECTS       = 0x0001L
DESKTOP_CREATEWINDOW      = 0x0002L
DESKTOP_CREATEMENU        = 0x0004L
DESKTOP_HOOKCONTROL       = 0x0008L
DESKTOP_JOURNALRECORD     = 0x0010L
DESKTOP_JOURNALPLAYBACK   = 0x0020L
DESKTOP_ENUMERATE         = 0x0040L
DESKTOP_WRITEOBJECTS      = 0x0080L
DESKTOP_SWITCHDESKTOP     = 0x0100L


# Desktop-specific control flags

DF_ALLOWOTHERACCOUNTHOOK  = 0x0001L


# Windowstation-specific access flags

WINSTA_ENUMDESKTOPS       = 0x0001L
WINSTA_READATTRIBUTES     = 0x0002L
WINSTA_ACCESSCLIPBOARD    = 0x0004L
WINSTA_CREATEDESKTOP      = 0x0008L
WINSTA_WRITEATTRIBUTES    = 0x0010L
WINSTA_ACCESSGLOBALATOMS  = 0x0020L
WINSTA_EXITWINDOWS        = 0x0040L
WINSTA_ENUMERATE          = 0x0100L
WINSTA_READSCREEN         = 0x0200L

WINSTA_ALL_ACCESS         = (
                             WINSTA_ENUMDESKTOPS      |
                             WINSTA_READATTRIBUTES    |
                             WINSTA_ACCESSCLIPBOARD   |
                             WINSTA_CREATEDESKTOP     |
                             WINSTA_WRITEATTRIBUTES   |
                             WINSTA_ACCESSGLOBALATOMS |
                             WINSTA_EXITWINDOWS       |
                             WINSTA_ENUMERATE         |
                             WINSTA_READSCREEN
                             )


# Windowstation creation flags.

CWF_CREATE_ONLY        = 0x00000001


# Windowstation-specific attribute flags

WSF_VISIBLE            = 0x0001L

UOI_FLAGS       = 1
UOI_NAME        = 2
UOI_TYPE        = 3
UOI_USER_SID    = 4
UOI_HEAPSIZE    = 5
UOI_IO          = 6

class WNDCLASSEX(Structure):
    _fields_ = [('cbSize', UINT),
                ('style', UINT),
                ('lpfnWndProc', WNDPROC),
                ('cbClsExtra', c_int),
                ('cbWndExtra', c_int),
                ('hInstance', HINSTANCE),
                ('hIcon', HICON),
                ('hCursor', c_int),
                ('hbrBackground', c_int),
                ('lpszMenuName', c_char_p),
                ('lpszClassName', c_char_p),
                ('hIconSm', HICON)]
'''
typedef struct tagWNDCLASSEXA {
    UINT        cbSize;
    /* Win 3.x */
    UINT        style;
    WNDPROC     lpfnWndProc;
    int         cbClsExtra;
    int         cbWndExtra;
    HINSTANCE   hInstance;
    HICON       hIcon;
    HCURSOR     hCursor;
    HBRUSH      hbrBackground;
    LPCSTR      lpszMenuName;
    LPCSTR      lpszClassName;
    /* Win 4.0 */
    HICON       hIconSm;
} WNDCLASSEXA, *PWNDCLASSEXA, NEAR *NPWNDCLASSEXA, FAR *LPWNDCLASSEXA;
'''

class WNDCLASS(Structure):
    _fields_ = [('style', c_uint),
                ('lpfnWndProc', WNDPROC),
                ('cbClsExtra', c_int),
                ('cbWndExtra', c_int),
                ('hInstance', c_int),
                ('hIcon', c_int),
                ('hCursor', c_int),
                ('hbrBackground', c_int),
                ('lpszMenuName', c_char_p),
                ('lpszClassName', c_char_p)]

'''
typedef struct tagWNDCLASSW {
    UINT        style;
    WNDPROC     lpfnWndProc;
    int         cbClsExtra;
    int         cbWndExtra;
    HINSTANCE   hInstance;
    HICON       hIcon;
    HCURSOR     hCursor;
    HBRUSH      hbrBackground;
    LPCWSTR     lpszMenuName;
    LPCWSTR     lpszClassName;
} WNDCLASSW, *PWNDCLASSW, NEAR *NPWNDCLASSW, FAR *LPWNDCLASSW;
'''

# Message structure

class MSG(Structure):
    _fields_ = [('hwnd', c_int),
                ('message', c_uint),
                ('wParam', c_int),
                ('lParam', c_int),
                ('time', c_int),
                ('pt', POINT)]

tagMSG = MSG


#define POINTTOPOINTS(pt)      (MAKELONG((short)((pt).x), (short)((pt).y)))

def MAKEWPARAM(l, h):
    '''#define MAKEWPARAM(l, h)      ((WPARAM)(DWORD)MAKELONG(l, h))'''
    r = WPARAM(DWORD( windef.MAKELONG(l, h)))
    return r.value


def MAKELPARAM(l, h):
    '''#define MAKELPARAM(l, h)      ((LPARAM)(DWORD)MAKELONG(l, h))'''
    n = windef.MAKELONG(l, h)
    #return LPARAM(n.value)
    return n



#define MAKELRESULT(l, h)     ((LRESULT)(DWORD)MAKELONG(l, h))

# Window field offsets for GetWindowLong()

GWL_WNDPROC         = (-4)
GWL_HINSTANCE       = (-6)
GWL_HWNDPARENT      = (-8)
GWL_STYLE           = (-16)
GWL_EXSTYLE         = (-20)
GWL_USERDATA        = (-21)
GWL_ID              = (-12)

GWLP_WNDPROC        = (-4)
GWLP_HINSTANCE      = (-6)
GWLP_HWNDPARENT     = (-8)
GWLP_USERDATA       = (-21)
GWLP_ID             = (-12)


# Class field offsets for GetClassLong()

GCL_MENUNAME        = -8
GCL_HBRBACKGROUND   = -10
GCL_HCURSOR         = -12
GCL_HICON           = -14
GCL_HMODULE         = -16
GCL_CBWNDEXTRA      = -18
GCL_CBCLSEXTRA      = -20
GCL_WNDPROC         = -24
GCL_STYLE           = -26
GCW_ATOM            = -32

GCL_HICONSM         = -34

GCLP_MENUNAME       = -8
GCLP_HBRBACKGROUND  = -10
GCLP_HCURSOR        = -12
GCLP_HICON          = -14
GCLP_HMODULE        = -16
GCLP_WNDPROC        = -24
GCLP_HICONSM        = -34


# Window Messages


WM_NULL                       = 0x0000
WM_CREATE                     = 0x0001
WM_DESTROY                    = 0x0002
WM_MOVE                       = 0x0003
WM_SIZE                       = 0x0005

WM_ACTIVATE                   = 0x0006

# WM_ACTIVATE state values

WA_INACTIVE     = 0
WA_ACTIVE       = 1
WA_CLICKACTIVE  = 2

WM_SETFOCUS                   = 0x0007
WM_KILLFOCUS                  = 0x0008
WM_ENABLE                     = 0x000A
WM_SETREDRAW                  = 0x000B
WM_SETTEXT                    = 0x000C
WM_GETTEXT                    = 0x000D
WM_GETTEXTLENGTH              = 0x000E
WM_PAINT                      = 0x000F
WM_CLOSE                      = 0x0010

WM_QUERYENDSESSION            = 0x0011
WM_QUERYOPEN                  = 0x0013
WM_ENDSESSION                 = 0x0016

WM_QUIT                       = 0x0012
WM_ERASEBKGND                 = 0x0014
WM_SYSCOLORCHANGE             = 0x0015
WM_SHOWWINDOW                 = 0x0018
WM_WININICHANGE               = 0x001A

WM_SETTINGCHANGE              = WM_WININICHANGE

WM_DEVMODECHANGE              = 0x001B
WM_ACTIVATEAPP                = 0x001C
WM_FONTCHANGE                 = 0x001D
WM_TIMECHANGE                 = 0x001E
WM_CANCELMODE                 = 0x001F
WM_SETCURSOR                  = 0x0020
WM_MOUSEACTIVATE              = 0x0021
WM_CHILDACTIVATE              = 0x0022
WM_QUEUESYNC                  = 0x0023

WM_GETMINMAXINFO              = 0x0024

WM_PAINTICON                  = 0x0026
WM_ICONERASEBKGND             = 0x0027
WM_NEXTDLGCTL                 = 0x0028
WM_SPOOLERSTATUS              = 0x002A
WM_DRAWITEM                   = 0x002B
WM_MEASUREITEM                = 0x002C
WM_DELETEITEM                 = 0x002D
WM_VKEYTOITEM                 = 0x002E
WM_CHARTOITEM                 = 0x002F
WM_SETFONT                    = 0x0030
WM_GETFONT                    = 0x0031
WM_SETHOTKEY                  = 0x0032
WM_GETHOTKEY                  = 0x0033
WM_QUERYDRAGICON              = 0x0037
WM_COMPAREITEM                = 0x0039

WM_GETOBJECT                  = 0x003D

WM_COMPACTING                 = 0x0041
WM_COMMNOTIFY                 = 0x0044   # no longer suported
WM_WINDOWPOSCHANGING          = 0x0046
WM_WINDOWPOSCHANGED           = 0x0047

WM_POWER                      = 0x0048

# wParam for WM_POWER window message and DRV_POWER driver notification

PWR_OK              = 1
PWR_FAIL            = (-1)
PWR_SUSPENDREQUEST  = 1
PWR_SUSPENDRESUME   = 2
PWR_CRITICALRESUME  = 3

WM_COPYDATA                   = 0x004A
WM_CANCELJOURNAL              = 0x004B

WM_NOTIFY                     = 0x004E
WM_INPUTLANGCHANGEREQUEST     = 0x0050
WM_INPUTLANGCHANGE            = 0x0051
WM_TCARD                      = 0x0052
WM_HELP                       = 0x0053
WM_USERCHANGED                = 0x0054
WM_NOTIFYFORMAT               = 0x0055

NFR_ANSI                             = 1
NFR_UNICODE                          = 2
NF_QUERY                             = 3
NF_REQUERY                           = 4

WM_CONTEXTMENU                = 0x007B
WM_STYLECHANGING              = 0x007C
WM_STYLECHANGED               = 0x007D
WM_DISPLAYCHANGE              = 0x007E
WM_GETICON                    = 0x007F
WM_SETICON                    = 0x0080

WM_NCCREATE                   = 0x0081
WM_NCDESTROY                  = 0x0082
WM_NCCALCSIZE                 = 0x0083
WM_NCHITTEST                  = 0x0084
WM_NCPAINT                    = 0x0085
WM_NCACTIVATE                 = 0x0086
WM_GETDLGCODE                 = 0x0087

WM_SYNCPAINT                  = 0x0088

WM_NCMOUSEMOVE                = 0x00A0
WM_NCLBUTTONDOWN              = 0x00A1
WM_NCLBUTTONUP                = 0x00A2
WM_NCLBUTTONDBLCLK            = 0x00A3
WM_NCRBUTTONDOWN              = 0x00A4
WM_NCRBUTTONUP                = 0x00A5
WM_NCRBUTTONDBLCLK            = 0x00A6
WM_NCMBUTTONDOWN              = 0x00A7
WM_NCMBUTTONUP                = 0x00A8
WM_NCMBUTTONDBLCLK            = 0x00A9

WM_NCXBUTTONDOWN              = 0x00AB
WM_NCXBUTTONUP                = 0x00AC
WM_NCXBUTTONDBLCLK            = 0x00AD

WM_INPUT_DEVICE_CHANGE        = 0x00FE

WM_INPUT                      = 0x00FF

WM_KEYFIRST                   = 0x0100
WM_KEYDOWN                    = 0x0100
WM_KEYUP                      = 0x0101
WM_CHAR                       = 0x0102
WM_DEADCHAR                   = 0x0103
WM_SYSKEYDOWN                 = 0x0104
WM_SYSKEYUP                   = 0x0105
WM_SYSCHAR                    = 0x0106
WM_SYSDEADCHAR                = 0x0107

WM_UNICHAR                    = 0x0109
WM_KEYLAST                    = 0x0109
UNICODE_NOCHAR                = 0xFFFF

WM_IME_STARTCOMPOSITION       = 0x010D
WM_IME_ENDCOMPOSITION         = 0x010E
WM_IME_COMPOSITION            = 0x010F
WM_IME_KEYLAST                = 0x010F

WM_INITDIALOG                 = 0x0110
WM_COMMAND                    = 0x0111
WM_SYSCOMMAND                 = 0x0112
WM_TIMER                      = 0x0113
WM_HSCROLL                    = 0x0114
WM_VSCROLL                    = 0x0115
WM_INITMENU                   = 0x0116
WM_INITMENUPOPUP              = 0x0117

WM_MENUSELECT                 = 0x011F
WM_MENUCHAR                   = 0x0120
WM_ENTERIDLE                  = 0x0121

WM_MENURBUTTONUP              = 0x0122
WM_MENUDRAG                   = 0x0123
WM_MENUGETOBJECT              = 0x0124
WM_UNINITMENUPOPUP            = 0x0125
WM_MENUCOMMAND                = 0x0126

WM_CHANGEUISTATE              = 0x0127
WM_UPDATEUISTATE              = 0x0128
WM_QUERYUISTATE               = 0x0129


# LOWORD(wParam) values in WM_*UISTATE*

UIS_SET                         = 1
UIS_CLEAR                       = 2
UIS_INITIALIZE                  = 3


# HIWORD(wParam) values in WM_*UISTATE*

UISF_HIDEFOCUS                = 0x1
UISF_HIDEACCEL                = 0x2

UISF_ACTIVE                   = 0x4

WM_CTLCOLORMSGBOX             = 0x0132
WM_CTLCOLOREDIT               = 0x0133
WM_CTLCOLORLISTBOX            = 0x0134
WM_CTLCOLORBTN                = 0x0135
WM_CTLCOLORDLG                = 0x0136
WM_CTLCOLORSCROLLBAR          = 0x0137
WM_CTLCOLORSTATIC             = 0x0138
MN_GETHMENU                   = 0x01E1

WM_MOUSEFIRST                 = 0x0200
WM_MOUSEMOVE                  = 0x0200
WM_LBUTTONDOWN                = 0x0201
WM_LBUTTONUP                  = 0x0202
WM_LBUTTONDBLCLK              = 0x0203
WM_RBUTTONDOWN                = 0x0204
WM_RBUTTONUP                  = 0x0205
WM_RBUTTONDBLCLK              = 0x0206
WM_MBUTTONDOWN                = 0x0207
WM_MBUTTONUP                  = 0x0208
WM_MBUTTONDBLCLK              = 0x0209

WM_MOUSEWHEEL                 = 0x020A

WM_XBUTTONDOWN                = 0x020B
WM_XBUTTONUP                  = 0x020C
WM_XBUTTONDBLCLK              = 0x020D

WM_MOUSELAST                  = 0x020D

# Value for rolling one detent
WHEEL_DELTA                     = 120

#WHEEL_PAGESCROLL                = (UINT_MAX)

# XButton values are WORD flags
XBUTTON1    = 0x0001
XBUTTON2    = 0x0002
# Were there to be an XBUTTON3, its value would be 0x0004

WM_PARENTNOTIFY               = 0x0210
WM_ENTERMENULOOP              = 0x0211
WM_EXITMENULOOP               = 0x0212


WM_NEXTMENU                   = 0x0213
WM_SIZING                     = 0x0214
WM_CAPTURECHANGED             = 0x0215
WM_MOVING                     = 0x0216

WM_POWERBROADCAST             = 0x0218

PBT_APMQUERYSUSPEND           = 0x0000
PBT_APMQUERYSTANDBY           = 0x0001

PBT_APMQUERYSUSPENDFAILED     = 0x0002
PBT_APMQUERYSTANDBYFAILED     = 0x0003

PBT_APMSUSPEND                = 0x0004
PBT_APMSTANDBY                = 0x0005

PBT_APMRESUMECRITICAL         = 0x0006
PBT_APMRESUMESUSPEND          = 0x0007
PBT_APMRESUMESTANDBY          = 0x0008

PBTF_APMRESUMEFROMFAILURE     = 0x00000001

PBT_APMBATTERYLOW             = 0x0009
PBT_APMPOWERSTATUSCHANGE      = 0x000A

PBT_APMOEMEVENT               = 0x000B


PBT_APMRESUMEAUTOMATIC        = 0x0012

WM_DEVICECHANGE               = 0x0219

WM_MDICREATE                  = 0x0220
WM_MDIDESTROY                 = 0x0221
WM_MDIACTIVATE                = 0x0222
WM_MDIRESTORE                 = 0x0223
WM_MDINEXT                    = 0x0224
WM_MDIMAXIMIZE                = 0x0225
WM_MDITILE                    = 0x0226
WM_MDICASCADE                 = 0x0227
WM_MDIICONARRANGE             = 0x0228
WM_MDIGETACTIVE               = 0x0229


WM_MDISETMENU                 = 0x0230
WM_ENTERSIZEMOVE              = 0x0231
WM_EXITSIZEMOVE               = 0x0232
WM_DROPFILES                  = 0x0233
WM_MDIREFRESHMENU             = 0x0234

WM_IME_SETCONTEXT             = 0x0281
WM_IME_NOTIFY                 = 0x0282
WM_IME_CONTROL                = 0x0283
WM_IME_COMPOSITIONFULL        = 0x0284
WM_IME_SELECT                 = 0x0285
WM_IME_CHAR                   = 0x0286

WM_IME_REQUEST                = 0x0288

WM_IME_KEYDOWN                = 0x0290
WM_IME_KEYUP                  = 0x0291

WM_MOUSEHOVER                 = 0x02A1
WM_MOUSELEAVE                 = 0x02A3


WM_NCMOUSEHOVER               = 0x02A0
WM_NCMOUSELEAVE               = 0x02A2


WM_WTSSESSION_CHANGE          = 0x02B1

WM_TABLET_FIRST               = 0x02c0
WM_TABLET_LAST                = 0x02df


WM_CUT                        = 0x0300
WM_COPY                       = 0x0301
WM_PASTE                      = 0x0302
WM_CLEAR                      = 0x0303
WM_UNDO                       = 0x0304
WM_RENDERFORMAT               = 0x0305
WM_RENDERALLFORMATS           = 0x0306
WM_DESTROYCLIPBOARD           = 0x0307
WM_DRAWCLIPBOARD              = 0x0308
WM_PAINTCLIPBOARD             = 0x0309
WM_VSCROLLCLIPBOARD           = 0x030A
WM_SIZECLIPBOARD              = 0x030B
WM_ASKCBFORMATNAME            = 0x030C
WM_CHANGECBCHAIN              = 0x030D
WM_HSCROLLCLIPBOARD           = 0x030E
WM_QUERYNEWPALETTE            = 0x030F
WM_PALETTEISCHANGING          = 0x0310
WM_PALETTECHANGED             = 0x0311
WM_HOTKEY                     = 0x0312

WM_PRINT                      = 0x0317
WM_PRINTCLIENT                = 0x0318

WM_APPCOMMAND                 = 0x0319

WM_THEMECHANGED               = 0x031A

WM_CLIPBOARDUPDATE            = 0x031D

WM_HANDHELDFIRST              = 0x0358
WM_HANDHELDLAST               = 0x035F

WM_AFXFIRST                   = 0x0360
WM_AFXLAST                    = 0x037F

WM_PENWINFIRST                = 0x0380
WM_PENWINLAST                 = 0x038F


WM_APP                        = 0x8000


# NOTE: All Message Numbers below 0x0400 are RESERVED.

# Private Window Messages Start Here:

WM_USER                       = 0x0400

# wParam for WM_SIZING message 
WMSZ_LEFT           = 1
WMSZ_RIGHT          = 2
WMSZ_TOP            = 3
WMSZ_TOPLEFT        = 4
WMSZ_TOPRIGHT       = 5
WMSZ_BOTTOM         = 6
WMSZ_BOTTOMLEFT     = 7
WMSZ_BOTTOMRIGHT    = 8


# WM_NCHITTEST and MOUSEHOOKSTRUCT Mouse Position Codes

HTERROR             = (-2)
HTTRANSPARENT       = (-1)
HTNOWHERE           = 0
HTCLIENT            = 1
HTCAPTION           = 2
HTSYSMENU           = 3
HTGROWBOX           = 4
HTSIZE              = HTGROWBOX
HTMENU              = 5
HTHSCROLL           = 6
HTVSCROLL           = 7
HTMINBUTTON         = 8
HTMAXBUTTON         = 9
HTLEFT              = 10
HTRIGHT             = 11
HTTOP               = 12
HTTOPLEFT           = 13
HTTOPRIGHT          = 14
HTBOTTOM            = 15
HTBOTTOMLEFT        = 16
HTBOTTOMRIGHT       = 17
HTBORDER            = 18
HTREDUCE            = HTMINBUTTON
HTZOOM              = HTMAXBUTTON
HTSIZEFIRST         = HTLEFT
HTSIZELAST          = HTBOTTOMRIGHT

HTOBJECT            = 19
HTCLOSE             = 20
HTHELP              = 21


# SendMessageTimeout values

SMTO_NORMAL       = 0x0000
SMTO_BLOCK        = 0x0001
SMTO_ABORTIFHUNG  = 0x0002

SMTO_NOTIMEOUTIFNOTHUNG = 0x0008


# WM_MOUSEACTIVATE Return Codes

MA_ACTIVATE         = 1
MA_ACTIVATEANDEAT   = 2
MA_NOACTIVATE       = 3
MA_NOACTIVATEANDEAT = 4


# WM_SETICON / WM_GETICON Type Codes

ICON_SMALL          = 0
ICON_BIG            = 1

ICON_SMALL2         = 2


# WM_SIZE message wParam values

SIZE_RESTORED       = 0
SIZE_MINIMIZED      = 1
SIZE_MAXIMIZED      = 2
SIZE_MAXSHOW        = 3
SIZE_MAXHIDE        = 4


# Obsolete constant names

SIZENORMAL          = SIZE_RESTORED
SIZEICONIC          = SIZE_MINIMIZED
SIZEFULLSCREEN      = SIZE_MAXIMIZED
SIZEZOOMSHOW        = SIZE_MAXSHOW
SIZEZOOMHIDE        = SIZE_MAXHIDE


# WM_NCCALCSIZE "window valid rect" return values

WVR_ALIGNTOP      = 0x0010
WVR_ALIGNLEFT     = 0x0020
WVR_ALIGNBOTTOM   = 0x0040
WVR_ALIGNRIGHT    = 0x0080
WVR_HREDRAW       = 0x0100
WVR_VREDRAW       = 0x0200
WVR_REDRAW        = (WVR_HREDRAW | WVR_VREDRAW)
WVR_VALIDRECTS    = 0x0400



# Key State Masks for Mouse Messages

MK_LBUTTON        = 0x0001
MK_RBUTTON        = 0x0002
MK_SHIFT          = 0x0004
MK_CONTROL        = 0x0008
MK_MBUTTON        = 0x0010

MK_XBUTTON1       = 0x0020
MK_XBUTTON2       = 0x0040

TME_HOVER     = 0x00000001
TME_LEAVE     = 0x00000002


TME_NONCLIENT = 0x00000010

TME_QUERY     = 0x40000000
TME_CANCEL    = auxfuncs.safe_long(0x80000000)


HOVER_DEFAULT = 0xFFFFFFFF


# Window Styles

# Window style constants are 32 bits - the first 16 flags are reserved
# for generic window styles - styles that might apply to any window,
# regardless of type.  The lower 16 are window-type-specific.

# Window style constants.

WS_OVERLAPPED     = 0x00000000L
WS_POPUP          = auxfuncs.safe_long(0x80000000L)
WS_CHILD          = 0x40000000L
WS_MINIMIZE       = 0x20000000L
WS_VISIBLE        = 0x10000000L
WS_DISABLED       = 0x08000000L
WS_CLIPSIBLINGS   = 0x04000000L
WS_CLIPCHILDREN   = 0x02000000L
WS_MAXIMIZE       = 0x01000000L
WS_CAPTION        = 0x00C00000L      # WS_BORDER | WS_DLGFRAME 
WS_BORDER         = 0x00800000L
WS_DLGFRAME       = 0x00400000L
WS_VSCROLL        = 0x00200000L
WS_HSCROLL        = 0x00100000L
WS_SYSMENU        = 0x00080000L
WS_THICKFRAME     = 0x00040000L
WS_GROUP          = 0x00020000L
WS_TABSTOP        = 0x00010000L

WS_MINIMIZEBOX    = 0x00020000L
WS_MAXIMIZEBOX    = 0x00010000L


WS_TILED            = WS_OVERLAPPED
WS_ICONIC           = WS_MINIMIZE
WS_SIZEBOX          = WS_THICKFRAME


# Common Window Styles

WS_OVERLAPPEDWINDOW = (
                       WS_OVERLAPPED  |
                       WS_CAPTION     |
                       WS_SYSMENU     |
                       WS_THICKFRAME  |
                       WS_MINIMIZEBOX |
                       WS_MAXIMIZEBOX
                       )

WS_POPUPWINDOW      = (WS_POPUP | WS_BORDER | WS_SYSMENU)

WS_CHILDWINDOW      = (WS_CHILD)

WS_TILEDWINDOW      = WS_OVERLAPPEDWINDOW


# Extended Window Styles

WS_EX_DLGMODALFRAME   = 0x00000001L
WS_EX_NOPARENTNOTIFY  = 0x00000004L
WS_EX_TOPMOST         = 0x00000008L
WS_EX_ACCEPTFILES     = 0x00000010L
WS_EX_TRANSPARENT     = 0x00000020L

WS_EX_MDICHILD        = 0x00000040L
WS_EX_TOOLWINDOW      = 0x00000080L
WS_EX_WINDOWEDGE      = 0x00000100L
WS_EX_CLIENTEDGE      = 0x00000200L
WS_EX_CONTEXTHELP     = 0x00000400L

WS_EX_RIGHT           = 0x00001000L
WS_EX_LEFT            = 0x00000000L
WS_EX_RTLREADING      = 0x00002000L
WS_EX_LTRREADING      = 0x00000000L
WS_EX_LEFTSCROLLBAR   = 0x00004000L
WS_EX_RIGHTSCROLLBAR  = 0x00000000L

WS_EX_CONTROLPARENT   = 0x00010000L
WS_EX_STATICEDGE      = 0x00020000L
WS_EX_APPWINDOW       = 0x00040000L


WS_EX_OVERLAPPEDWINDOW  = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
WS_EX_PALETTEWINDOW     = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)

WS_EX_LAYERED         = 0x00080000

WS_EX_NOINHERITLAYOUT = 0x00100000L # Disable inheritence of mirroring by children
WS_EX_LAYOUTRTL       = 0x00400000L # Right to left mirroring

WS_EX_COMPOSITED      = 0x02000000L

WS_EX_NOACTIVATE      = 0x08000000L


# Class styles

CS_VREDRAW        = 0x0001
CS_HREDRAW        = 0x0002
CS_DBLCLKS        = 0x0008
CS_OWNDC          = 0x0020
CS_CLASSDC        = 0x0040
CS_PARENTDC       = 0x0080
CS_NOCLOSE        = 0x0200
CS_SAVEBITS       = 0x0800
CS_BYTEALIGNCLIENT= 0x1000
CS_BYTEALIGNWINDOW= 0x2000
CS_GLOBALCLASS    = 0x4000

CS_IME            = 0x00010000

CS_DROPSHADOW     = 0x00020000

PRF_CHECKVISIBLE  = 0x00000001L
PRF_NONCLIENT     = 0x00000002L
PRF_CLIENT        = 0x00000004L
PRF_ERASEBKGND    = 0x00000008L
PRF_CHILDREN      = 0x00000010L
PRF_OWNED         = 0x00000020L

# 3D border styles
BDR_RAISEDOUTER = 0x0001
BDR_SUNKENOUTER = 0x0002
BDR_RAISEDINNER = 0x0004
BDR_SUNKENINNER = 0x0008

BDR_OUTER       = (BDR_RAISEDOUTER | BDR_SUNKENOUTER)
BDR_INNER       = (BDR_RAISEDINNER | BDR_SUNKENINNER)
BDR_RAISED      = (BDR_RAISEDOUTER | BDR_RAISEDINNER)
BDR_SUNKEN      = (BDR_SUNKENOUTER | BDR_SUNKENINNER)


EDGE_RAISED     = (BDR_RAISEDOUTER | BDR_RAISEDINNER)
EDGE_SUNKEN     = (BDR_SUNKENOUTER | BDR_SUNKENINNER)
EDGE_ETCHED     = (BDR_SUNKENOUTER | BDR_RAISEDINNER)
EDGE_BUMP       = (BDR_RAISEDOUTER | BDR_SUNKENINNER)

# Border flags
BF_LEFT       = 0x0001
BF_TOP        = 0x0002
BF_RIGHT      = 0x0004
BF_BOTTOM     = 0x0008

BF_TOPLEFT      = (BF_TOP | BF_LEFT)
BF_TOPRIGHT     = (BF_TOP | BF_RIGHT)
BF_BOTTOMLEFT   = (BF_BOTTOM | BF_LEFT)
BF_BOTTOMRIGHT  = (BF_BOTTOM | BF_RIGHT)
BF_RECT         = (BF_LEFT | BF_TOP | BF_RIGHT | BF_BOTTOM)

BF_DIAGONAL   = 0x0010

# For diagonal lines, the BF_RECT flags specify the end point of the
# vector bounded by the rectangle parameter.
BF_DIAGONAL_ENDTOPRIGHT     = (BF_DIAGONAL | BF_TOP | BF_RIGHT)
BF_DIAGONAL_ENDTOPLEFT      = (BF_DIAGONAL | BF_TOP | BF_LEFT)
BF_DIAGONAL_ENDBOTTOMLEFT   = (BF_DIAGONAL | BF_BOTTOM | BF_LEFT)
BF_DIAGONAL_ENDBOTTOMRIGHT  = (BF_DIAGONAL | BF_BOTTOM | BF_RIGHT)


BF_MIDDLE     = 0x0800   #Fill in the middle
BF_SOFT       = 0x1000   #For softer buttons
BF_ADJUST     = 0x2000   #Calculate the space left over
BF_FLAT       = 0x4000   #For flat rather than 3D borders
BF_MONO       = 0x8000   #For monochrome borders

# flags for DrawFrameControl

DFC_CAPTION           = 1
DFC_MENU              = 2
DFC_SCROLL            = 3
DFC_BUTTON            = 4
DFC_POPUPMENU         = 5

DFCS_CAPTIONCLOSE     = 0x0000
DFCS_CAPTIONMIN       = 0x0001
DFCS_CAPTIONMAX       = 0x0002
DFCS_CAPTIONRESTORE   = 0x0003
DFCS_CAPTIONHELP      = 0x0004

DFCS_MENUARROW        = 0x0000
DFCS_MENUCHECK        = 0x0001
DFCS_MENUBULLET       = 0x0002
DFCS_MENUARROWRIGHT   = 0x0004
DFCS_SCROLLUP         = 0x0000
DFCS_SCROLLDOWN       = 0x0001
DFCS_SCROLLLEFT       = 0x0002
DFCS_SCROLLRIGHT      = 0x0003
DFCS_SCROLLCOMBOBOX   = 0x0005
DFCS_SCROLLSIZEGRIP   = 0x0008
DFCS_SCROLLSIZEGRIPRIGHT = 0x0010

DFCS_BUTTONCHECK      = 0x0000
DFCS_BUTTONRADIOIMAGE = 0x0001
DFCS_BUTTONRADIOMASK  = 0x0002
DFCS_BUTTONRADIO      = 0x0004
DFCS_BUTTON3STATE     = 0x0008
DFCS_BUTTONPUSH       = 0x0010

DFCS_INACTIVE         = 0x0100
DFCS_PUSHED           = 0x0200
DFCS_CHECKED          = 0x0400

DFCS_TRANSPARENT      = 0x0800
DFCS_HOT              = 0x1000

DFCS_ADJUSTRECT       = 0x2000
DFCS_FLAT             = 0x4000
DFCS_MONO             = 0x8000


# flags for DrawCaption
DC_ACTIVE         = 0x0001
DC_SMALLCAP       = 0x0002
DC_ICON           = 0x0004
DC_TEXT           = 0x0008
DC_INBUTTON       = 0x0010

DC_GRADIENT       = 0x0020

DC_BUTTONS        = 0x1000

IDANI_OPEN          = 1
IDANI_CAPTION       = 3


# Predefined Clipboard Formats

CF_TEXT             = 1
CF_BITMAP           = 2
CF_METAFILEPICT     = 3
CF_SYLK             = 4
CF_DIF              = 5
CF_TIFF             = 6
CF_OEMTEXT          = 7
CF_DIB              = 8
CF_PALETTE          = 9
CF_PENDATA          = 10
CF_RIFF             = 11
CF_WAVE             = 12
CF_UNICODETEXT      = 13
CF_ENHMETAFILE      = 14

CF_HDROP            = 15
CF_LOCALE           = 16
CF_DIBV5            = 17
CF_MAX              = 18

CF_OWNERDISPLAY   = 0x0080
CF_DSPTEXT        = 0x0081
CF_DSPBITMAP      = 0x0082
CF_DSPMETAFILEPICT= 0x0083
CF_DSPENHMETAFILE = 0x008E


# "Private" formats don't get GlobalFree()'d

CF_PRIVATEFIRST   = 0x0200
CF_PRIVATELAST    = 0x02FF


# "GDIOBJ" formats do get DeleteObject()'d

CF_GDIOBJFIRST    = 0x0300
CF_GDIOBJLAST     = 0x03FF


# Defines for the fVirt field of the Accelerator table structure.

FVIRTKEY  = TRUE           #Assumed to be == TRUE
FNOINVERT = 0x02
FSHIFT    = 0x04
FCONTROL  = 0x08
FALT      = 0x10


class PAINTSTRUCT(Structure):
    _fields_ = [('hdc', c_int),
                ('fErase', c_int),
                ('rcPaint', RECT),
                ('fRestore', c_int),
                ('fIncUpdate', c_int),
                ('rgbReserved', c_char * 32)]

'''
typedef struct tagPAINTSTRUCT {
    HDC         hdc;
    BOOL        fErase;
    RECT        rcPaint;
    BOOL        fRestore;
    BOOL        fIncUpdate;
    BYTE        rgbReserved[32];
} PAINTSTRUCT, *PPAINTSTRUCT, *NPPAINTSTRUCT, *LPPAINTSTRUCT;
'''


WPF_SETMINPOSITION        = 0x0001
WPF_RESTORETOMAXIMIZED    = 0x0002
WPF_ASYNCWINDOWPLACEMENT  = 0x0004

# Owner draw control types

ODT_MENU        = 1
ODT_LISTBOX     = 2
ODT_COMBOBOX    = 3
ODT_BUTTON      = 4
ODT_STATIC      = 5


# Owner draw actions

ODA_DRAWENTIRE  = 0x0001
ODA_SELECT      = 0x0002
ODA_FOCUS       = 0x0004

# Owner draw state

ODS_SELECTED    = 0x0001
ODS_GRAYED      = 0x0002
ODS_DISABLED    = 0x0004
ODS_CHECKED     = 0x0008
ODS_FOCUS       = 0x0010

ODS_DEFAULT         = 0x0020
ODS_COMBOBOXEDIT    = 0x1000

ODS_HOTLIGHT        = 0x0040
ODS_INACTIVE        = 0x0080

ODS_NOACCEL         = 0x0100
ODS_NOFOCUSRECT     = 0x0200


class DRAWITEMSTRUCT(Structure):
    _fields_ =[('CtlType',UINT),
               ('CtlID',UINT),
               ('itemID',UINT),
               ('itemAction',UINT),
               ('itemState',UINT),
               ('hwndItem',HWND),
               ('hDC',HDC),
               ('rcItem',RECT),
               ('itemData',DWORD)]

tagDRAWITEMSTRUCT = DRAWITEMSTRUCT
'''
DRAWITEMSTRUCT {
    UINT        CtlType;
    UINT        CtlID;
    UINT        itemID;
    UINT        itemAction;
    UINT        itemState;
    HWND        hwndItem;
    HDC         hDC;
    RECT        rcItem;
    ULONG_PTR   itemData;
} DRAWITEMSTRUCT, NEAR *PDRAWITEMSTRUCT, FAR *LPDRAWITEMSTRUCT;
'''

'''
WINUSERAPI
BOOL
WINAPI
GetMessageA(
    __out LPMSG lpMsg,
    __in_opt HWND hWnd,
    __in UINT wMsgFilterMin,
    __in UINT wMsgFilterMax);
'''

GetMessageA = windll.user32.GetMessageA
GetMessage = GetMessageA


'''
WINUSERAPI
BOOL
WINAPI
TranslateMessage(
    __in CONST MSG *lpMsg);
'''

TranslateMessage = windll.user32.TranslateMessage

'''
WINUSERAPI
LRESULT
WINAPI
DispatchMessageA(
    __in CONST MSG *lpMsg);
'''

DispatchMessageA = windll.user32.DispatchMessageA
DispatchMessage = DispatchMessageA


# Queue status flags for GetQueueStatus() and MsgWaitForMultipleObjects()

QS_KEY            = 0x0001
QS_MOUSEMOVE      = 0x0002
QS_MOUSEBUTTON    = 0x0004
QS_POSTMESSAGE    = 0x0008
QS_TIMER          = 0x0010
QS_PAINT          = 0x0020
QS_SENDMESSAGE    = 0x0040
QS_HOTKEY         = 0x0080
QS_ALLPOSTMESSAGE = 0x0100

QS_RAWINPUT       = 0x0400

QS_MOUSE          = (QS_MOUSEMOVE | QS_MOUSEBUTTON)


QS_INPUT          = (QS_MOUSE | QS_KEY | QS_RAWINPUT)
QS_ALLEVENTS      = (QS_INPUT | QS_POSTMESSAGE | QS_TIMER | QS_PAINT | QS_HOTKEY)

QS_ALLINPUT       = (QS_INPUT | QS_POSTMESSAGE | QS_TIMER | QS_PAINT | QS_HOTKEY | QS_SENDMESSAGE)
                            
USER_TIMER_MAXIMUM = 0x7FFFFFFF
USER_TIMER_MINIMUM = 0x0000000A


EnableWindow = windll.user32.EnableWindow
'''
WINUSERAPI
BOOL
WINAPI
EnableWindow(
    __in HWND hWnd,
    __in BOOL bEnable);
'''
EnableWindow.argtypes = [HWND, BOOL]

IsWindowEnabled = windll.user32.IsWindowEnabled 
'''
WINUSERAPI
BOOL
WINAPI
IsWindowEnabled(
    __in HWND hWnd);
'''
IsWindowEnabled.argtypes = [HWND]


# Owner draw control types

ODT_MENU        = 1
ODT_LISTBOX     = 2
ODT_COMBOBOX    = 3
ODT_BUTTON      = 4
ODT_STATIC      = 5


# Owner draw actions

ODA_DRAWENTIRE= 0x0001
ODA_SELECT    = 0x0002
ODA_FOCUS     = 0x0004


# Owner draw state

ODS_SELECTED  = 0x0001
ODS_GRAYED    = 0x0002
ODS_DISABLED  = 0x0004
ODS_CHECKED   = 0x0008
ODS_FOCUS     = 0x0010

ODS_DEFAULT       = 0x0020
ODS_COMBOBOXEDIT  = 0x1000

ODS_HOTLIGHT      = 0x0040
ODS_INACTIVE      = 0x0080

ODS_NOACCEL       = 0x0100
ODS_NOFOCUSRECT   = 0x0200


# PeekMessage() Options

PM_NOREMOVE       = 0x0000
PM_REMOVE         = 0x0001
PM_NOYIELD        = 0x0002

PM_QS_INPUT         = (QS_INPUT << 16)
PM_QS_POSTMESSAGE   = ((QS_POSTMESSAGE | QS_HOTKEY | QS_TIMER) << 16)
PM_QS_PAINT         = (QS_PAINT << 16)
PM_QS_SENDMESSAGE   = (QS_SENDMESSAGE << 16)

MOD_ALT       = 0x0001
MOD_CONTROL   = 0x0002
MOD_SHIFT     = 0x0004
MOD_WIN       = 0x0008

IDHOT_SNAPWINDOW        = (-1)    # SHIFT-PRINTSCRN 
IDHOT_SNAPDESKTOP       = (-2)    # PRINTSCRN       

ENDSESSION_LOGOFF  = auxfuncs.safe_long(0x80000000)

ENDSESSION_CRITICAL = 0x40000000

ENDSESSION_CLOSEAPP = 0x00000001

EWX_LOGOFF         = 0
EWX_SHUTDOWN      = 0x00000001
EWX_REBOOT        = 0x00000002
EWX_FORCE         = 0x00000004
EWX_POWEROFF      = 0x00000008
EWX_FORCEIFHUNG   = 0x00000010
EWX_QUICKRESOLVE  = 0x00000020



SendMessageA = windll.user32.SendMessageA
#SendMessageA.argtypes = [HWND, UINT, WPARAM, LPARAM]
SendMessage = SendMessageA

'''
WINUSERAPI
LRESULT
WINAPI
SendMessageA(
    __in HWND hWnd,
    __in UINT Msg,
    __in WPARAM wParam,
    __in LPARAM lParam);
'''

# Broadcast Special Message Recipient list
BSM_ALLCOMPONENTS     = 0x00000000
BSM_VXDS              = 0x00000001
BSM_NETDRIVER         = 0x00000002
BSM_INSTALLABLEDRIVERS= 0x00000004
BSM_APPLICATIONS      = 0x00000008
BSM_ALLDESKTOPS       = 0x00000010

# Broadcast Special Message Flags
BSF_QUERY             = 0x00000001
BSF_IGNORECURRENTTASK = 0x00000002
BSF_FLUSHDISK         = 0x00000004
BSF_NOHANG            = 0x00000008
BSF_POSTMESSAGE       = 0x00000010
BSF_FORCEIFHUNG       = 0x00000020
BSF_NOTIMEOUTIFNOTHUNG= 0x00000040

BSF_ALLOWSFW          = 0x00000080
BSF_SENDNOTIFYMESSAGE = 0x00000100

BSF_RETURNHDESK       = 0x00000200
BSF_LUID              = 0x00000400

BROADCAST_QUERY_DENY       = 0x424D5144  # Return this value to deny a query.

DEVICE_NOTIFY_WINDOW_HANDLE        = 0x00000000
DEVICE_NOTIFY_SERVICE_HANDLE       = 0x00000001
DEVICE_NOTIFY_ALL_INTERFACE_CLASSES= 0x00000004

HWND_BROADCAST = 0xffff
HWND_MESSAGE   = -3


'''
WINUSERAPI
LRESULT
WINAPI
DefWindowProcA(
    __in HWND hWnd,
    __in UINT Msg,
    __in WPARAM wParam,
    __in LPARAM lParam);
'''
DefWindowProcA = windll.user32.DefWindowProcA
DefWindowProcA.argtypes = [HWND, UINT, WPARAM, LPARAM]


'''
WINUSERAPI
VOID
WINAPI
PostQuitMessage(
    __in int nExitCode);
'''
PostQuitMessage = windll.user32.PostQuitMessage
PostQuitMessage.argtypes = [c_int]


# InSendMessageEx return value

ISMEX_NOSEND    = 0x00000000
ISMEX_SEND      = 0x00000001
ISMEX_NOTIFY    = 0x00000002
ISMEX_CALLBACK  = 0x00000004
ISMEX_REPLIED   = 0x00000008


'''
WINUSERAPI
ATOM
WINAPI
RegisterClassA(
    __in CONST WNDCLASSA *lpWndClass);
'''
RegisterClassA = windll.user32.RegisterClassA
RegisterClassA.argtypes = [HANDLE]
RegisterClass = RegisterClassA


CW_USEDEFAULT       = auxfuncs.safe_long(0x80000000)


# Special value for CreateWindow, et al.

HWND_DESKTOP       = 0

'''
HWND CreateWindowEx(

    DWORD dwExStyle,    // extended window style
    LPCTSTR lpClassName,    // pointer to registered class name
    LPCTSTR lpWindowName,    // pointer to window name
    DWORD dwStyle,    // window style
    int x,    // horizontal position of window
    int y,    // vertical position of window
    int nWidth,    // window width
    int nHeight,    // window height
    HWND hWndParent,    // handle to parent or owner window
    HMENU hMenu,    // handle to menu, or child-window identifier
    HINSTANCE hInstance,    // handle to application instance
    LPVOID lpParam     // pointer to window-creation data
   );
'''
CreateWindowEx = windll.user32.CreateWindowExA
CreateWindowEx.argtypes = [DWORD, c_char_p, c_char_p, DWORD, c_int, c_int, c_int, c_int, HWND, HMENU, HINSTANCE, c_int]
CreateWindowEx.restype = ErrorIfZero

def CreateWindowA(lpClassName, lpWindowName, dwStyle, x, y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam):
    return CreateWindowEx(0L, lpClassName, lpWindowName, dwStyle, x, y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam)

CreateWindow = CreateWindowA


'''
WINUSERAPI
BOOL
WINAPI
IsWindow(
    __in_opt HWND hWnd);
'''
IsWindow = windll.user32.IsWindow
IsWindow.argtypes = [HWND]


'''
WINUSERAPI
BOOL
WINAPI
IsMenu(
    __in HMENU hMenu);
'''
IsMenu = windll.user32.IsMenu
IsMenu.argtypes = [HMENU]


'''
WINUSERAPI
BOOL
WINAPI
IsChild(
    __in HWND hWndParent,
    __in HWND hWnd);
'''
IsChild = windll.user32.IsChild
IsChild.argtypes = [HWND, HWND]


'''
WINUSERAPI
BOOL
WINAPI
DestroyWindow(
    __in HWND hWnd);
'''
DestroyWindow = windll.user32.DestroyWindow
DestroyWindow.argtypes = [HWND]


'''
WINUSERAPI
BOOL
WINAPI
ShowWindow(
    __in HWND hWnd,
    __in int nCmdShow);
'''
ShowWindow = windll.user32.ShowWindow
ShowWindow.argtypes = [HWND, c_int]


'''
WINUSERAPI
BOOL
WINAPI
AnimateWindow(
    __in HWND hWnd,
    __in DWORD dwTime,
    __in DWORD dwFlags);
'''
AnimateWindow = windll.user32.AnimateWindow
AnimateWindow.argtypes = [HWND, DWORD, DWORD]


PW_CLIENTONLY         = 0x00000001

LWA_COLORKEY          = 0x00000001
LWA_ALPHA             = 0x00000002


ULW_COLORKEY          = 0x00000001
ULW_ALPHA             = 0x00000002
ULW_OPAQUE            = 0x00000004

ULW_EX_NORESIZE       = 0x00000008


FLASHW_STOP       = 0
FLASHW_CAPTION    = 0x00000001
FLASHW_TRAY       = 0x00000002
FLASHW_ALL        = (FLASHW_CAPTION | FLASHW_TRAY)
FLASHW_TIMER      = 0x00000004
FLASHW_TIMERNOFG  = 0x0000000C

'''
WINUSERAPI
BOOL
WINAPI
ShowOwnedPopups(
    __in  HWND hWnd,
    __in  BOOL fShow);
'''


'''
WINUSERAPI
BOOL
WINAPI
OpenIcon(
    __in  HWND hWnd);
'''

'''
WINUSERAPI
BOOL
WINAPI
CloseWindow(
    __in  HWND hWnd);
'''


MoveWindow = windll.user32.MoveWindow
'''
WINUSERAPI
BOOL
WINAPI
MoveWindow(
    __in HWND hWnd,
    __in int X,
    __in int Y,
    __in int nWidth,
    __in int nHeight,
    __in BOOL bRepaint);
'''
MoveWindow.argtypes = [HWND, c_int, c_int, c_int, c_int, BOOL]

SetWindowPos = windll.user32.SetWindowPos
'''
WINUSERAPI
BOOL
WINAPI
SetWindowPos(
    __in HWND hWnd,
    __in_opt HWND hWndInsertAfter,
    __in int X,
    __in int Y,
    __in int cx,
    __in int cy,
    __in UINT uFlags);
'''
SetWindowPos.argtypes = [HWND, HWND, c_int, c_int, c_int, c_int, UINT]

'''
WINUSERAPI
BOOL
WINAPI
GetWindowPlacement(
    __in HWND hWnd,
    __inout WINDOWPLACEMENT *lpwndpl);
'''
'''
WINUSERAPI
BOOL
WINAPI
SetWindowPlacement(
    __in HWND hWnd,
    __in CONST WINDOWPLACEMENT *lpwndpl);
'''
'''
WINUSERAPI
BOOL
WINAPI
IsWindowVisible(
    __in HWND hWnd);
'''
'''
WINUSERAPI
BOOL
WINAPI
IsIconic(
    __in HWND hWnd);
'''
'''
WINUSERAPI
BOOL
WINAPI
AnyPopup(
    VOID);
'''
'''
WINUSERAPI
BOOL
WINAPI
BringWindowToTop(
    __in HWND hWnd);
'''
'''
WINUSERAPI
BOOL
WINAPI
IsZoomed(
    __in HWND hWnd);
'''
# SetWindowPos Flags

SWP_NOSIZE        = 0x0001
SWP_NOMOVE        = 0x0002
SWP_NOZORDER      = 0x0004
SWP_NOREDRAW      = 0x0008
SWP_NOACTIVATE    = 0x0010
SWP_FRAMECHANGED  = 0x0020   #The frame changed: send WM_NCCALCSIZE
SWP_SHOWWINDOW    = 0x0040
SWP_HIDEWINDOW    = 0x0080
SWP_NOCOPYBITS    = 0x0100
SWP_NOOWNERZORDER = 0x0200   #Don't do owner Z ordering
SWP_NOSENDCHANGING= 0x0400   #Don't send WM_WINDOWPOSCHANGING

SWP_DRAWFRAME       = SWP_FRAMECHANGED
SWP_NOREPOSITION    = SWP_NOOWNERZORDER

SWP_DEFERERASE     = 0x2000
SWP_ASYNCWINDOWPOS = 0x4000


HWND_TOP        = 0
HWND_BOTTOM     = 1
HWND_TOPMOST    = -1
HWND_NOTOPMOST  = -2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP     = 0x0002


KEYEVENTF_UNICODE   = 0x0004
KEYEVENTF_SCANCODE  = 0x0008

MOUSEEVENTF_MOVE      = 0x0001  #mouse move
MOUSEEVENTF_LEFTDOWN  = 0x0002  #left button down
MOUSEEVENTF_LEFTUP    = 0x0004  #left button up
MOUSEEVENTF_RIGHTDOWN = 0x0008  #right button down
MOUSEEVENTF_RIGHTUP   = 0x0010  #right button up
MOUSEEVENTF_MIDDLEDOWN= 0x0020  #middle button down
MOUSEEVENTF_MIDDLEUP  = 0x0040  #middle button up
MOUSEEVENTF_XDOWN     = 0x0080  #x button down
MOUSEEVENTF_XUP       = 0x0100  #x button down
MOUSEEVENTF_WHEEL     = 0x0800  #wheel button rolled

MOUSEEVENTF_VIRTUALDESK = 0x4000  #map to entire virtual desktop
MOUSEEVENTF_ABSOLUTE  = 0x8000  #absolute move

MAPVK_VK_TO_VSC     = (0)
MAPVK_VSC_TO_VK     = (1)
MAPVK_VK_TO_CHAR    = (2)
MAPVK_VSC_TO_VK_EX  = (3)


# GetSystemMetrics() codes


SM_CXSCREEN             = 0
SM_CYSCREEN             = 1
SM_CXVSCROLL            = 2
SM_CYHSCROLL            = 3
SM_CYCAPTION            = 4
SM_CXBORDER             = 5
SM_CYBORDER             = 6
SM_CXDLGFRAME           = 7
SM_CYDLGFRAME           = 8
SM_CYVTHUMB             = 9
SM_CXHTHUMB             = 10
SM_CXICON               = 11
SM_CYICON               = 12
SM_CXCURSOR             = 13
SM_CYCURSOR             = 14
SM_CYMENU               = 15
SM_CXFULLSCREEN         = 16
SM_CYFULLSCREEN         = 17
SM_CYKANJIWINDOW        = 18
SM_MOUSEPRESENT         = 19
SM_CYVSCROLL            = 20
SM_CXHSCROLL            = 21
SM_DEBUG                = 22
SM_SWAPBUTTON           = 23
SM_RESERVED1            = 24
SM_RESERVED2            = 25
SM_RESERVED3            = 26
SM_RESERVED4            = 27
SM_CXMIN                = 28
SM_CYMIN                = 29
SM_CXSIZE               = 30
SM_CYSIZE               = 31
SM_CXFRAME              = 32
SM_CYFRAME              = 33
SM_CXMINTRACK           = 34
SM_CYMINTRACK           = 35
SM_CXDOUBLECLK          = 36
SM_CYDOUBLECLK          = 37
SM_CXICONSPACING        = 38
SM_CYICONSPACING        = 39
SM_MENUDROPALIGNMENT    = 40
SM_PENWINDOWS           = 41
SM_DBCSENABLED          = 42
SM_CMOUSEBUTTONS        = 43


SM_CXFIXEDFRAME         = SM_CXDLGFRAME   #;win40 name change
SM_CYFIXEDFRAME         = SM_CYDLGFRAME   #;win40 name change
SM_CXSIZEFRAME          = SM_CXFRAME      #;win40 name change
SM_CYSIZEFRAME          = SM_CYFRAME      #;win40 name change

SM_SECURE               = 44
SM_CXEDGE               = 45
SM_CYEDGE               = 46
SM_CXMINSPACING         = 47
SM_CYMINSPACING         = 48
SM_CXSMICON             = 49
SM_CYSMICON             = 50
SM_CYSMCAPTION          = 51
SM_CXSMSIZE             = 52
SM_CYSMSIZE             = 53
SM_CXMENUSIZE           = 54
SM_CYMENUSIZE           = 55
SM_ARRANGE              = 56
SM_CXMINIMIZED          = 57
SM_CYMINIMIZED          = 58
SM_CXMAXTRACK           = 59
SM_CYMAXTRACK           = 60
SM_CXMAXIMIZED          = 61
SM_CYMAXIMIZED          = 62
SM_NETWORK              = 63
SM_CLEANBOOT            = 67
SM_CXDRAG               = 68
SM_CYDRAG               = 69

SM_SHOWSOUNDS           = 70

SM_CXMENUCHECK          = 71   # Use instead of GetMenuCheckMarkDimensions()!
SM_CYMENUCHECK          = 72
SM_SLOWMACHINE          = 73
SM_MIDEASTENABLED       = 74

SM_MOUSEWHEELPRESENT    = 75

SM_XVIRTUALSCREEN       = 76
SM_YVIRTUALSCREEN       = 77
SM_CXVIRTUALSCREEN      = 78
SM_CYVIRTUALSCREEN      = 79
SM_CMONITORS            = 80
SM_SAMEDISPLAYFORMAT    = 81

SM_IMMENABLED           = 82

SM_CXFOCUSBORDER        = 83
SM_CYFOCUSBORDER        = 84

SM_TABLETPC             = 86
SM_MEDIACENTER          = 87
SM_STARTER              = 88
SM_SERVERR2             = 89

SM_REMOTESESSION      = 0x1000

SM_SHUTTINGDOWN       = 0x2000

SM_REMOTECONTROL      = 0x2001

SM_CARETBLINKINGENABLED = 0x2002

PMB_ACTIVE    = 0x00000001

# return codes for WM_MENUCHAR
MNC_IGNORE  = 0
MNC_CLOSE   = 1
MNC_EXECUTE = 2
MNC_SELECT  = 3

MNS_NOCHECK       = auxfuncs.safe_long(0x80000000)
MNS_MODELESS      = 0x40000000
MNS_DRAGDROP      = 0x20000000
MNS_AUTODISMISS   = 0x10000000
MNS_NOTIFYBYPOS   = 0x08000000
MNS_CHECKORBMP    = 0x04000000

MIM_MAXHEIGHT             = 0x00000001
MIM_BACKGROUND            = 0x00000002
MIM_HELPID                = 0x00000004
MIM_MENUDATA              = 0x00000008
MIM_STYLE                 = 0x00000010
MIM_APPLYTOSUBMENUS       = auxfuncs.safe_long(0x80000000)


# WM_MENUDRAG return values.

MND_CONTINUE       = 0
MND_ENDMENU        = 1


# MENUGETOBJECTINFO dwFlags values

MNGOF_TOPGAP       = 0x00000001
MNGOF_BOTTOMGAP    = 0x00000002


# WM_MENUGETOBJECT return values

MNGO_NOINTERFACE   = 0x00000000
MNGO_NOERROR       = 0x00000001

MIIM_STATE     = 0x00000001
MIIM_ID        = 0x00000002
MIIM_SUBMENU   = 0x00000004
MIIM_CHECKMARKS= 0x00000008
MIIM_TYPE      = 0x00000010
MIIM_DATA      = 0x00000020

MIIM_STRING    = 0x00000040
MIIM_BITMAP    = 0x00000080
MIIM_FTYPE     = 0x00000100

HBMMENU_CALLBACK            = -1
HBMMENU_SYSTEM              = 1
HBMMENU_MBAR_RESTORE        = 2
HBMMENU_MBAR_MINIMIZE       = 3
HBMMENU_MBAR_CLOSE          = 5
HBMMENU_MBAR_CLOSE_D        = 6
HBMMENU_MBAR_MINIMIZE_D     = 7
HBMMENU_POPUP_CLOSE         = 8
HBMMENU_POPUP_RESTORE       = 9
HBMMENU_POPUP_MAXIMIZE      = 10
HBMMENU_POPUP_MINIMIZE      = 11


# Flags for TrackPopupMenu

TPM_LEFTBUTTON      = 0x0000L
TPM_RIGHTBUTTON     = 0x0002L
TPM_LEFTALIGN       = 0x0000L
TPM_CENTERALIGN     = 0x0004L
TPM_RIGHTALIGN      = 0x0008L
TPM_TOPALIGN        = 0x0000L
TPM_VCENTERALIGN    = 0x0010L
TPM_BOTTOMALIGN     = 0x0020L
TPM_HORIZONTAL      = 0x0000L     # Horz alignment matters more
TPM_VERTICAL        = 0x0040L     # Vert alignment matters more
TPM_NONOTIFY        = 0x0080L     # Don't send any notification msgs
TPM_RETURNCMD       = 0x0100L
TPM_RECURSE         = 0x0001L
TPM_HORPOSANIMATION = 0x0400L
TPM_HORNEGANIMATION = 0x0800L
TPM_VERPOSANIMATION = 0x1000L
TPM_VERNEGANIMATION = 0x2000L
TPM_NOANIMATION     = 0x4000L
TPM_LAYOUTRTL       = 0x8000L

DOF_EXECUTABLE    = 0x8001      # wFmt flags
DOF_DOCUMENT      = 0x8002
DOF_DIRECTORY     = 0x8003
DOF_MULTIPLE      = 0x8004
DOF_PROGMAN       = 0x0001
DOF_SHELLDATA     = 0x0002

DO_DROPFILE       = 0x454C4946L
DO_PRINTFILE      = 0x544E5250L


# DrawText() Format Flags

DT_TOP                    = 0x00000000
DT_LEFT                   = 0x00000000
DT_CENTER                 = 0x00000001
DT_RIGHT                  = 0x00000002
DT_VCENTER                = 0x00000004
DT_BOTTOM                 = 0x00000008
DT_WORDBREAK              = 0x00000010
DT_SINGLELINE             = 0x00000020
DT_EXPANDTABS             = 0x00000040
DT_TABSTOP                = 0x00000080
DT_NOCLIP                 = 0x00000100
DT_EXTERNALLEADING        = 0x00000200
DT_CALCRECT               = 0x00000400
DT_NOPREFIX               = 0x00000800
DT_INTERNAL               = 0x00001000

DT_EDITCONTROL            = 0x00002000
DT_PATH_ELLIPSIS          = 0x00004000
DT_END_ELLIPSIS           = 0x00008000
DT_MODIFYSTRING           = 0x00010000
DT_RTLREADING             = 0x00020000
DT_WORD_ELLIPSIS          = 0x00040000

DT_NOFULLWIDTHCHARBREAK   = 0x00080000

DT_HIDEPREFIX             = 0x00100000
DT_PREFIXONLY             = 0x00200000


'''
WINUSERAPI
int
WINAPI
DrawTextA(
    __in HDC hdc,
    __inout_ecount_opt(cchText) LPCSTR lpchText,
    __in int cchText,
    __inout LPRECT lprc,
    __in UINT format);
'''

DrawTextA = windll.user32.DrawTextA
DrawTextA.argtypes = [HDC, HANDLE, c_int, HANDLE, UINT]
DrawText = DrawTextA


# Monolithic state-drawing routine
# Image type
DST_COMPLEX   = 0x0000
DST_TEXT      = 0x0001
DST_PREFIXTEXT= 0x0002
DST_ICON      = 0x0003
DST_BITMAP    = 0x0004

# State type
DSS_NORMAL    = 0x0000
DSS_UNION     = 0x0010  # Gray string appearance
DSS_DISABLED  = 0x0020
DSS_MONO      = 0x0080

DSS_HIDEPREFIX = 0x0200
DSS_PREFIXONLY = 0x0400

DSS_RIGHT     = 0x8000


'''
WINUSERAPI
BOOL
WINAPI
UpdateWindow(
    __in HWND hWnd);
'''

UpdateWindow = windll.user32.UpdateWindow
UpdateWindow.argtypes = [HWND]

'''
WINUSERAPI
HWND
WINAPI
SetActiveWindow(
    __in HWND hWnd);
'''

SetActiveWindow = windll.user32.SetActiveWindow
SetActiveWindow.argtypes = [HWND]

# GetDCEx() flags

DCX_WINDOW         = 0x00000001L
DCX_CACHE          = 0x00000002L
DCX_NORESETATTRS   = 0x00000004L
DCX_CLIPCHILDREN   = 0x00000008L
DCX_CLIPSIBLINGS   = 0x00000010L
DCX_PARENTCLIP     = 0x00000020L
DCX_EXCLUDERGN     = 0x00000040L
DCX_INTERSECTRGN   = 0x00000080L
DCX_EXCLUDEUPDATE  = 0x00000100L
DCX_INTERSECTUPDATE= 0x00000200L
DCX_LOCKWINDOWUPDATE = 0x00000400L
DCX_VALIDATE       = 0x00200000L


'''
WINUSERAPI
HDC
WINAPI
BeginPaint(
    __in HWND hWnd,
    __out LPPAINTSTRUCT lpPaint);
'''
BeginPaint = windll.user32.BeginPaint
BeginPaint.argtypes = [HWND, HANDLE]


'''
WINUSERAPI
BOOL
WINAPI
EndPaint(
    __in HWND hWnd,
    __in CONST PAINTSTRUCT *lpPaint);
'''
EndPaint = windll.user32.EndPaint
EndPaint.argtypes = [HWND, HANDLE]

# RedrawWindow() flags

RDW_INVALIDATE        = 0x0001
RDW_INTERNALPAINT     = 0x0002
RDW_ERASE             = 0x0004

RDW_VALIDATE          = 0x0008
RDW_NOINTERNALPAINT   = 0x0010
RDW_NOERASE           = 0x0020

RDW_NOCHILDREN        = 0x0040
RDW_ALLCHILDREN       = 0x0080

RDW_UPDATENOW         = 0x0100
RDW_ERASENOW          = 0x0200

RDW_FRAME             = 0x0400
RDW_NOFRAME           = 0x0800

SW_SCROLLCHILDREN = 0x0001   #Scroll children within *lprcScroll.
SW_INVALIDATE     = 0x0002   #Invalidate after scrolling
SW_ERASE          = 0x0004   #If SW_INVALIDATE, don't send WM_ERASEBACKGROUND

SW_SMOOTHSCROLL   = 0x0010   #Use smooth scrolling



'''
WINUSERAPI
int
WINAPI
SetScrollPos(
    __in HWND hWnd,
    __in int nBar,
    __in int nPos,
    __in BOOL bRedraw);

WINUSERAPI
int
WINAPI
GetScrollPos(
    __in HWND hWnd,
    __in int nBar);

WINUSERAPI
BOOL
WINAPI
SetScrollRange(
    __in HWND hWnd,
    __in int nBar,
    __in int nMinPos,
    __in int nMaxPos,
    __in BOOL bRedraw);

WINUSERAPI
BOOL
WINAPI
GetScrollRange(
    __in HWND hWnd,
    __in int nBar,
    __out LPINT lpMinPos,
    __out LPINT lpMaxPos);
'''

ShowScrollBar = windll.user32.ShowScrollBar
ShowScrollBar.argtypes = [HWND, c_int, BOOL]

'''
WINUSERAPI
BOOL
WINAPI
ShowScrollBar(
    __in HWND hWnd,
    __in int wBar,
    __in BOOL bShow);
'''

'''
WINUSERAPI
BOOL
WINAPI
EnableScrollBar(
    __in HWND hWnd,
    __in UINT wSBflags,
    __in UINT wArrows);
'''



# EnableScrollBar() flags

ESB_ENABLE_BOTH   = 0x0000
ESB_DISABLE_BOTH  = 0x0003

ESB_DISABLE_LEFT  = 0x0001
ESB_DISABLE_RIGHT = 0x0002

ESB_DISABLE_UP    = 0x0001
ESB_DISABLE_DOWN  = 0x0002

ESB_DISABLE_LTUP  = ESB_DISABLE_LEFT
ESB_DISABLE_RTDN  = ESB_DISABLE_RIGHT


'''
WINUSERAPI
BOOL
WINAPI
SetWindowTextA(
    __in HWND hWnd,
    __in_opt LPCSTR lpString);
'''
SetWindowTextA = windll.user32.SetWindowTextA
SetWindowTextA.argtypes = [HWND, HANDLE]
SetWindowText = SetWindowTextA


'''
WINUSERAPI
int
WINAPI
GetWindowTextA(
    __in HWND hWnd,
    __out_ecount(nMaxCount) LPSTR lpString,
    __in int nMaxCount);
'''
GetWindowTextA = windll.user32.GetWindowTextA
GetWindowTextA.argtypes = [HWND, HANDLE, c_int]
GetWindowText = GetWindowTextA


'''
WINUSERAPI
int
WINAPI
GetWindowTextLengthA(
    __in HWND hWnd);
'''
GetWindowTextLengthA = windll.user32.GetWindowTextLengthA
GetWindowTextLengthA.argtypes = [HWND]
GetWindowTextLength = GetWindowTextLengthA


'''
WINUSERAPI
BOOL
WINAPI
GetClientRect(
    __in HWND hWnd,
    __out LPRECT lpRect);
'''
GetClientRect = windll.user32.GetClientRect
GetClientRect.argtypes = [HWND, HANDLE]


'''
WINUSERAPI
BOOL
WINAPI
GetWindowRect(
    __in HWND hWnd,
    __out LPRECT lpRect);
'''
GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = [HWND, HANDLE]

'''
WINUSERAPI
BOOL
WINAPI
AdjustWindowRect(
    __inout LPRECT lpRect,
    __in DWORD dwStyle,
    __in BOOL bMenu);
'''
AdjustWindowRect = windll.user32.AdjustWindowRect
AdjustWindowRect.argtypes = [HANDLE, DWORD, BOOL]


HELPINFO_WINDOW  = 0x0001
HELPINFO_MENUITEM= 0x0002


# MessageBox() Flags

MB_OK                     = 0x00000000L
MB_OKCANCEL               = 0x00000001L
MB_ABORTRETRYIGNORE       = 0x00000002L
MB_YESNOCANCEL            = 0x00000003L
MB_YESNO                  = 0x00000004L
MB_RETRYCANCEL            = 0x00000005L

MB_CANCELTRYCONTINUE      = 0x00000006L

MB_ICONHAND               = 0x00000010L
MB_ICONQUESTION           = 0x00000020L
MB_ICONEXCLAMATION        = 0x00000030L
MB_ICONASTERISK           = 0x00000040L

MB_USERICON               = 0x00000080L
MB_ICONWARNING            = MB_ICONEXCLAMATION
MB_ICONERROR              = MB_ICONHAND

MB_ICONINFORMATION        = MB_ICONASTERISK
MB_ICONSTOP               = MB_ICONHAND

MB_DEFBUTTON1             = 0x00000000L
MB_DEFBUTTON2             = 0x00000100L
MB_DEFBUTTON3             = 0x00000200L

MB_DEFBUTTON4             = 0x00000300L

MB_APPLMODAL              = 0x00000000L
MB_SYSTEMMODAL            = 0x00001000L
MB_TASKMODAL              = 0x00002000L

MB_HELP                   = 0x00004000L # Help Button

MB_NOFOCUS                = 0x00008000L
MB_SETFOREGROUND          = 0x00010000L
MB_DEFAULT_DESKTOP_ONLY   = 0x00020000L

MB_TOPMOST                = 0x00040000L
MB_RIGHT                  = 0x00080000L
MB_RTLREADING             = 0x00100000L

MB_SERVICE_NOTIFICATION        = 0x00200000L

MB_SERVICE_NOTIFICATION_NT3X   = 0x00040000L

MB_TYPEMASK               = 0x0000000FL
MB_ICONMASK               = 0x000000F0L
MB_DEFMASK                = 0x00000F00L
MB_MODEMASK               = 0x00003000L
MB_MISCMASK               = 0x0000C000L

CWP_ALL           = 0x0000
CWP_SKIPINVISIBLE = 0x0001
CWP_SKIPDISABLED  = 0x0002
CWP_SKIPTRANSPARENT = 0x0004


# Color Types

CTLCOLOR_MSGBOX         = 0
CTLCOLOR_EDIT           = 1
CTLCOLOR_LISTBOX        = 2
CTLCOLOR_BTN            = 3
CTLCOLOR_DLG            = 4
CTLCOLOR_SCROLLBAR      = 5
CTLCOLOR_STATIC         = 6
CTLCOLOR_MAX            = 7

COLOR_SCROLLBAR         = 0
COLOR_BACKGROUND        = 1
COLOR_ACTIVECAPTION     = 2
COLOR_INACTIVECAPTION   = 3
COLOR_MENU              = 4
COLOR_WINDOW            = 5
COLOR_WINDOWFRAME       = 6
COLOR_MENUTEXT          = 7
COLOR_WINDOWTEXT        = 8
COLOR_CAPTIONTEXT       = 9
COLOR_ACTIVEBORDER      = 10
COLOR_INACTIVEBORDER    = 11
COLOR_APPWORKSPACE      = 12
COLOR_HIGHLIGHT         = 13
COLOR_HIGHLIGHTTEXT     = 14
COLOR_BTNFACE           = 15
COLOR_BTNSHADOW         = 16
COLOR_GRAYTEXT          = 17
COLOR_BTNTEXT           = 18
COLOR_INACTIVECAPTIONTEXT = 19
COLOR_BTNHIGHLIGHT      = 20

COLOR_3DDKSHADOW        = 21
COLOR_3DLIGHT           = 22
COLOR_INFOTEXT          = 23
COLOR_INFOBK            = 24

COLOR_HOTLIGHT          = 26
COLOR_GRADIENTACTIVECAPTION = 27
COLOR_GRADIENTINACTIVECAPTION = 28

COLOR_MENUHILIGHT       = 29
COLOR_MENUBAR           = 30

COLOR_DESKTOP           = COLOR_BACKGROUND
COLOR_3DFACE            = COLOR_BTNFACE
COLOR_3DSHADOW          = COLOR_BTNSHADOW
COLOR_3DHIGHLIGHT       = COLOR_BTNHIGHLIGHT
COLOR_3DHILIGHT         = COLOR_BTNHIGHLIGHT
COLOR_BTNHILIGHT        = COLOR_BTNHIGHLIGHT




'''
WINUSERAPI
LONG
WINAPI
GetWindowLongA(
    __in HWND hWnd,
    __in int nIndex);
'''
GetWindowLongA = windll.user32.GetWindowLongA
GetWindowLongA.argtypes = [HWND, c_int]
GetWindowLong = GetWindowLongA 

'''
WINUSERAPI
HWND
WINAPI
GetParent(
    __in HWND hWnd);
'''
GetParent = windll.user32.GetParent
GetParent.argtypes = [HWND]

'''
WINUSERAPI
HWND
WINAPI
SetParent(
    __in HWND hWndChild,
    __in_opt HWND hWndNewParent);
'''
SetParent = windll.user32.SetParent
SetParent.argtypes = [HWND, HWND]

# GetWindow() Constants

GW_HWNDFIRST        = 0
GW_HWNDLAST         = 1
GW_HWNDNEXT         = 2
GW_HWNDPREV         = 3
GW_OWNER            = 4
GW_CHILD            = 5

GW_ENABLEDPOPUP     = 6
GW_MAX              = 6

# ;win40  -- A lot of MF_* flags have been renamed as MFT_* and MFS_* flags

# Menu flags for Add/Check/EnableMenuItem()

MF_INSERT         = 0x00000000L
MF_CHANGE         = 0x00000080L
MF_APPEND         = 0x00000100L
MF_DELETE         = 0x00000200L
MF_REMOVE         = 0x00001000L

MF_BYCOMMAND      = 0x00000000L
MF_BYPOSITION     = 0x00000400L

MF_SEPARATOR      = 0x00000800L

MF_ENABLED        = 0x00000000L
MF_GRAYED         = 0x00000001L
MF_DISABLED       = 0x00000002L

MF_UNCHECKED      = 0x00000000L
MF_CHECKED        = 0x00000008L
MF_USECHECKBITMAPS= 0x00000200L

MF_STRING         = 0x00000000L
MF_BITMAP         = 0x00000004L
MF_OWNERDRAW      = 0x00000100L

MF_POPUP          = 0x00000010L
MF_MENUBARBREAK   = 0x00000020L
MF_MENUBREAK      = 0x00000040L

MF_UNHILITE       = 0x00000000L
MF_HILITE         = 0x00000080L

MF_DEFAULT        = 0x00001000L

MF_SYSMENU        = 0x00002000L
MF_HELP           = 0x00004000L

MF_RIGHTJUSTIFY   = 0x00004000L

MF_MOUSESELECT    = 0x00008000L

MF_END            = 0x00000080L   #Obsolete -- only used by old RES files

MFT_STRING        = MF_STRING
MFT_BITMAP        = MF_BITMAP
MFT_MENUBARBREAK  = MF_MENUBARBREAK
MFT_MENUBREAK     = MF_MENUBREAK
MFT_OWNERDRAW     = MF_OWNERDRAW
MFT_RADIOCHECK    = 0x00000200L
MFT_SEPARATOR     = MF_SEPARATOR
MFT_RIGHTORDER    = 0x00002000L
MFT_RIGHTJUSTIFY  = MF_RIGHTJUSTIFY

# Menu flags for Add/Check/EnableMenuItem()
MFS_GRAYED        = 0x00000003L
MFS_DISABLED      = MFS_GRAYED
MFS_CHECKED       = MF_CHECKED
MFS_HILITE        = MF_HILITE
MFS_ENABLED       = MF_ENABLED
MFS_UNCHECKED     = MF_UNCHECKED
MFS_UNHILITE      = MF_UNHILITE
MFS_DEFAULT       = MF_DEFAULT


# System Menu Command Values

SC_SIZE       = 0xF000
SC_MOVE       = 0xF010
SC_MINIMIZE   = 0xF020
SC_MAXIMIZE   = 0xF030
SC_NEXTWINDOW = 0xF040
SC_PREVWINDOW = 0xF050
SC_CLOSE      = 0xF060
SC_VSCROLL    = 0xF070
SC_HSCROLL    = 0xF080
SC_MOUSEMENU  = 0xF090
SC_KEYMENU    = 0xF100
SC_ARRANGE    = 0xF110
SC_RESTORE    = 0xF120
SC_TASKLIST   = 0xF130
SC_SCREENSAVE = 0xF140
SC_HOTKEY     = 0xF150

SC_DEFAULT    = 0xF160
SC_MONITORPOWER  = 0xF170
SC_CONTEXTHELP= 0xF180
SC_SEPARATOR  = 0xF00F


# Obsolete names

SC_ICON         = SC_MINIMIZE
SC_ZOOM         = SC_MAXIMIZE

'''
WINUSERAPI
HCURSOR
WINAPI
LoadCursorA(
    __in_opt HINSTANCE hInstance,
    __in LPCSTR lpCursorName);
'''
LoadCursorA = windll.user32.LoadCursorA
LoadCursorA.argtypes = [HINSTANCE, c_int]
LoadCursor = LoadCursorA


# Standard Cursor IDs

IDC_ARROW         = 32512
IDC_IBEAM         = 32513
IDC_WAIT          = 32514
IDC_CROSS         = 32515
IDC_UPARROW       = 32516
IDC_SIZE          = 32640   #OBSOLETE: use IDC_SIZEALL
IDC_ICON          = 32641   #OBSOLETE: use IDC_ARROW
IDC_SIZENWSE      = 32642
IDC_SIZENESW      = 32643
IDC_SIZEWE        = 32644
IDC_SIZENS        = 32645
IDC_SIZEALL        = 32646
IDC_NO             = 32648 #not in win3.1
IDC_HAND           = 32649
IDC_APPSTARTING    = 32650 #not in win3.1
IDC_HELP           = 32651


'''
WINUSERAPI
HICON
WINAPI
LoadIconA(
    __in_opt HINSTANCE hInstance,
    __in LPCSTR lpIconName);
'''
LoadIconA = windll.user32.LoadIconA
LoadIconA.argtypes = [HINSTANCE, c_int]




IMAGE_BITMAP        = 0
IMAGE_ICON          = 1
IMAGE_CURSOR        = 2
IMAGE_ENHMETAFILE   = 3

LR_DEFAULTCOLOR   = 0x00000000
LR_MONOCHROME     = 0x00000001
LR_COLOR          = 0x00000002
LR_COPYRETURNORG  = 0x00000004
LR_COPYDELETEORG  = 0x00000008
LR_LOADFROMFILE   = 0x00000010
LR_LOADTRANSPARENT= 0x00000020
LR_DEFAULTSIZE    = 0x00000040
LR_VGACOLOR       = 0x00000080
LR_LOADMAP3DCOLORS= 0x00001000
LR_CREATEDIBSECTION  = 0x00002000
LR_COPYFROMRESOURCE  = 0x00004000
LR_SHARED         = 0x00008000

DI_MASK       = 0x0001
DI_IMAGE      = 0x0002
DI_NORMAL     = 0x0003
DI_COMPAT     = 0x0004
DI_DEFAULTSIZE= 0x0008


DI_NOMIRROR   = 0x0010

RES_ICON     = 1
RES_CURSOR   = 2



# OEM Resource Ordinal Numbers

OBM_CLOSE           = 32754
OBM_UPARROW         = 32753
OBM_DNARROW         = 32752
OBM_RGARROW         = 32751
OBM_LFARROW         = 32750
OBM_REDUCE          = 32749
OBM_ZOOM            = 32748
OBM_RESTORE         = 32747
OBM_REDUCED         = 32746
OBM_ZOOMD           = 32745
OBM_RESTORED        = 32744
OBM_UPARROWD        = 32743
OBM_DNARROWD        = 32742
OBM_RGARROWD        = 32741
OBM_LFARROWD        = 32740
OBM_MNARROW         = 32739
OBM_COMBO           = 32738
OBM_UPARROWI        = 32737
OBM_DNARROWI        = 32736
OBM_RGARROWI        = 32735
OBM_LFARROWI        = 32734

OBM_OLD_CLOSE       = 32767
OBM_SIZE            = 32766
OBM_OLD_UPARROW     = 32765
OBM_OLD_DNARROW     = 32764
OBM_OLD_RGARROW     = 32763
OBM_OLD_LFARROW     = 32762
OBM_BTSIZE          = 32761
OBM_CHECK           = 32760
OBM_CHECKBOXES      = 32759
OBM_BTNCORNERS      = 32758
OBM_OLD_REDUCE      = 32757
OBM_OLD_ZOOM        = 32756
OBM_OLD_RESTORE     = 32755


OCR_NORMAL          = 32512
OCR_IBEAM           = 32513
OCR_WAIT            = 32514
OCR_CROSS           = 32515
OCR_UP              = 32516
OCR_SIZE            = 32640    #OBSOLETE: use OCR_SIZEALL
OCR_ICON            = 32641    #OBSOLETE: use OCR_NORMAL
OCR_SIZENWSE        = 32642
OCR_SIZENESW        = 32643
OCR_SIZEWE          = 32644
OCR_SIZENS          = 32645
OCR_SIZEALL         = 32646
OCR_ICOCUR          = 32647    #OBSOLETE: use OIC_WINLOGO
OCR_NO              = 32648

OCR_HAND            = 32649


OCR_APPSTARTING     = 32650



OIC_SAMPLE          = 32512
OIC_HAND            = 32513
OIC_QUES            = 32514
OIC_BANG            = 32515
OIC_NOTE            = 32516

OIC_WINLOGO         = 32517
OIC_WARNING         = OIC_BANG
OIC_ERROR           = OIC_HAND
OIC_INFORMATION     = OIC_NOTE


ORD_LANGDRIVER    = 1      #The ordinal number for the entry point of language drivers.
                               



# Standard Icon IDs

 
IDI_APPLICATION     = 32512
IDI_HAND            = 32513
IDI_QUESTION        = 32514
IDI_EXCLAMATION     = 32515
IDI_ASTERISK        = 32516

IDI_WINLOGO         = 32517

IDI_WARNING     = IDI_EXCLAMATION
IDI_ERROR       = IDI_HAND
IDI_INFORMATION = IDI_ASTERISK


# Dialog Box Command IDs

IDOK                = 1
IDCANCEL            = 2
IDABORT             = 3
IDRETRY             = 4
IDIGNORE            = 5
IDYES               = 6
IDNO                = 7

IDCLOSE         = 8
IDHELP          = 9

IDTRYAGAIN      = 10
IDCONTINUE      = 11

IDTIMEOUT = 32000


# Edit Control Styles

ES_LEFT           = 0x0000L
ES_CENTER         = 0x0001L
ES_RIGHT          = 0x0002L
ES_MULTILINE      = 0x0004L
ES_UPPERCASE      = 0x0008L
ES_LOWERCASE      = 0x0010L
ES_PASSWORD       = 0x0020L
ES_AUTOVSCROLL    = 0x0040L
ES_AUTOHSCROLL    = 0x0080L
ES_NOHIDESEL      = 0x0100L
ES_OEMCONVERT     = 0x0400L
ES_READONLY       = 0x0800L
ES_WANTRETURN     = 0x1000L

ES_NUMBER         = 0x2000L


# Edit Control Notification Codes

EN_SETFOCUS       = 0x0100
EN_KILLFOCUS      = 0x0200
EN_CHANGE         = 0x0300
EN_UPDATE         = 0x0400
EN_ERRSPACE       = 0x0500
EN_MAXTEXT        = 0x0501
EN_HSCROLL        = 0x0601
EN_VSCROLL        = 0x0602

EN_ALIGN_LTR_EC   = 0x0700
EN_ALIGN_RTL_EC   = 0x0701


EC_LEFTMARGIN     = 0x0001
EC_RIGHTMARGIN    = 0x0002
EC_USEFONTINFO    = 0xffff

# wParam of EM_GET/SETIMESTATUS 
EMSIS_COMPOSITIONSTRING      = 0x0001

# lParam for EMSIS_COMPOSITIONSTRING 
EIMES_GETCOMPSTRATONCE       = 0x0001
EIMES_CANCELCOMPSTRINFOCUS   = 0x0002
EIMES_COMPLETECOMPSTRKILLFOCUS = 0x0004


# Edit Control Messages

EM_GETSEL             = 0x00B0
EM_SETSEL             = 0x00B1
EM_GETRECT            = 0x00B2
EM_SETRECT            = 0x00B3
EM_SETRECTNP          = 0x00B4
EM_SCROLL             = 0x00B5
EM_LINESCROLL         = 0x00B6
EM_SCROLLCARET        = 0x00B7
EM_GETMODIFY          = 0x00B8
EM_SETMODIFY          = 0x00B9
EM_GETLINECOUNT       = 0x00BA
EM_LINEINDEX          = 0x00BB
EM_SETHANDLE          = 0x00BC
EM_GETHANDLE          = 0x00BD
EM_GETTHUMB           = 0x00BE
EM_LINELENGTH         = 0x00C1
EM_REPLACESEL         = 0x00C2
EM_GETLINE            = 0x00C4
EM_LIMITTEXT          = 0x00C5
EM_CANUNDO            = 0x00C6
EM_UNDO               = 0x00C7
EM_FMTLINES           = 0x00C8
EM_LINEFROMCHAR       = 0x00C9
EM_SETTABSTOPS        = 0x00CB
EM_SETPASSWORDCHAR    = 0x00CC
EM_EMPTYUNDOBUFFER    = 0x00CD
EM_GETFIRSTVISIBLELINE= 0x00CE
EM_SETREADONLY        = 0x00CF
EM_SETWORDBREAKPROC   = 0x00D0
EM_GETWORDBREAKPROC   = 0x00D1
EM_GETPASSWORDCHAR    = 0x00D2

EM_SETMARGINS         = 0x00D3
EM_GETMARGINS         = 0x00D4
EM_SETLIMITTEXT       = EM_LIMITTEXT   # ;win40 Name change
EM_GETLIMITTEXT       = 0x00D5
EM_POSFROMCHAR        = 0x00D6
EM_CHARFROMPOS        = 0x00D7

EM_SETIMESTATUS       = 0x00D8
EM_GETIMESTATUS       = 0x00D9


# EDITWORDBREAKPROC code values

WB_LEFT            = 0
WB_RIGHT           = 1
WB_ISDELIMITER     = 2



# Button Control Styles

BS_PUSHBUTTON     = 0x00000000L
BS_DEFPUSHBUTTON  = 0x00000001L
BS_CHECKBOX       = 0x00000002L
BS_AUTOCHECKBOX   = 0x00000003L
BS_RADIOBUTTON    = 0x00000004L
BS_3STATE         = 0x00000005L
BS_AUTO3STATE     = 0x00000006L
BS_GROUPBOX       = 0x00000007L
BS_USERBUTTON     = 0x00000008L
BS_AUTORADIOBUTTON= 0x00000009L
BS_PUSHBOX        = 0x0000000AL
BS_OWNERDRAW      = 0x0000000BL
BS_TYPEMASK       = 0x0000000FL
BS_LEFTTEXT       = 0x00000020L
BS_TEXT           = 0x00000000L
BS_ICON           = 0x00000040L
BS_BITMAP         = 0x00000080L
BS_LEFT           = 0x00000100L
BS_RIGHT          = 0x00000200L
BS_CENTER         = 0x00000300L
BS_TOP            = 0x00000400L
BS_BOTTOM         = 0x00000800L
BS_VCENTER        = 0x00000C00L
BS_PUSHLIKE       = 0x00001000L
BS_MULTILINE      = 0x00002000L
BS_NOTIFY         = 0x00004000L
BS_FLAT           = 0x00008000L
BS_RIGHTBUTTON    = BS_LEFTTEXT


# User Button Notification Codes

BN_CLICKED          = 0
BN_PAINT            = 1
BN_HILITE           = 2
BN_UNHILITE         = 3
BN_DISABLE          = 4
BN_DOUBLECLICKED    = 5
BN_PUSHED           = BN_HILITE
BN_UNPUSHED         = BN_UNHILITE
BN_DBLCLK           = BN_DOUBLECLICKED
BN_SETFOCUS         = 6
BN_KILLFOCUS        = 7


# Button Control Messages

BM_GETCHECK      = 0x00F0
BM_SETCHECK      = 0x00F1
BM_GETSTATE      = 0x00F2
BM_SETSTATE      = 0x00F3
BM_SETSTYLE      = 0x00F4
BM_CLICK         = 0x00F5
BM_GETIMAGE      = 0x00F6
BM_SETIMAGE      = 0x00F7

BST_UNCHECKED    = 0x0000
BST_CHECKED      = 0x0001
BST_INDETERMINATE= 0x0002
BST_PUSHED       = 0x0004
BST_FOCUS        = 0x0008


# Static Control Constants

SS_LEFT           = 0x00000000L
SS_CENTER         = 0x00000001L
SS_RIGHT          = 0x00000002L
SS_ICON           = 0x00000003L
SS_BLACKRECT      = 0x00000004L
SS_GRAYRECT       = 0x00000005L
SS_WHITERECT      = 0x00000006L
SS_BLACKFRAME     = 0x00000007L
SS_GRAYFRAME      = 0x00000008L
SS_WHITEFRAME     = 0x00000009L
SS_USERITEM       = 0x0000000AL
SS_SIMPLE         = 0x0000000BL
SS_LEFTNOWORDWRAP = 0x0000000CL
SS_OWNERDRAW      = 0x0000000DL
SS_BITMAP         = 0x0000000EL
SS_ENHMETAFILE    = 0x0000000FL
SS_ETCHEDHORZ     = 0x00000010L
SS_ETCHEDVERT     = 0x00000011L
SS_ETCHEDFRAME    = 0x00000012L
SS_TYPEMASK       = 0x0000001FL
SS_REALSIZECONTROL= 0x00000040L
SS_NOPREFIX       = 0x00000080L  #Don't do "&" character translation
SS_NOTIFY         = 0x00000100L
SS_CENTERIMAGE    = 0x00000200L
SS_RIGHTJUST      = 0x00000400L
SS_REALSIZEIMAGE  = 0x00000800L
SS_SUNKEN         = 0x00001000L
SS_EDITCONTROL    = 0x00002000L
SS_ENDELLIPSIS    = 0x00004000L
SS_PATHELLIPSIS   = 0x00008000L
SS_WORDELLIPSIS   = 0x0000C000L
SS_ELLIPSISMASK   = 0x0000C000L



# Static Control Mesages

STM_SETICON       = 0x0170
STM_GETICON       = 0x0171
STM_SETIMAGE      = 0x0172
STM_GETIMAGE      = 0x0173
STN_CLICKED       = 0
STN_DBLCLK        = 1
STN_ENABLE        = 2
STN_DISABLE       = 3

STM_MSGMAX        = 0x0174


# Dialog window class

#WC_DIALOG       (MAKEINTATOM(0x8002))


# Get/SetWindowWord/Long offsets for use with WC_DIALOG windows

DWL_MSGRESULT   = 0
DWL_DLGPROC     = 4
DWL_USER        = 8

DWLP_MSGRESULT  = 0
###DWLP_DLGPROC    = DWLP_MSGRESULT + sizeof(LRESULT)
###DWLP_USER       = DWLP_DLGPROC + sizeof(DLGPROC)



# DlgDirList, DlgDirListComboBox flags values

DDL_READWRITE     = 0x0000
DDL_READONLY      = 0x0001
DDL_HIDDEN        = 0x0002
DDL_SYSTEM        = 0x0004
DDL_DIRECTORY     = 0x0010
DDL_ARCHIVE       = 0x0020

DDL_POSTMSGS      = 0x2000
DDL_DRIVES        = 0x4000
DDL_EXCLUSIVE     = 0x8000



# Dialog Styles

DS_ABSALIGN       = 0x01L
DS_SYSMODAL       = 0x02L
DS_LOCALEDIT      = 0x20L    #Edit items get Local storage.
DS_SETFONT        = 0x40L   # User specified font for Dlg controls
DS_MODALFRAME     = 0x80L   # Can be combined with WS_CAPTION 
DS_NOIDLEMSG      = 0x100L  # WM_ENTERIDLE message will not be sent
DS_SETFOREGROUND  = 0x200L  # not in win3.1
DS_3DLOOK         = 0x0004L
DS_FIXEDSYS       = 0x0008L
DS_NOFAILCREATE   = 0x0010L
DS_CONTROL        = 0x0400L
DS_CENTER         = 0x0800L
DS_CENTERMOUSE    = 0x1000L
DS_CONTEXTHELP    = 0x2000L

DS_SHELLFONT        = (DS_SETFONT | DS_FIXEDSYS)

DM_GETDEFID         = (WM_USER+0)
DM_SETDEFID         = (WM_USER+1)


DM_REPOSITION       = (WM_USER+2)


# Returned in HIWORD() of DM_GETDEFID result if msg is supported

DC_HASDEFID       = 0x534B



# Dialog Codes

DLGC_WANTARROWS   = 0x0001      # Control wants arrow keys        
DLGC_WANTTAB      = 0x0002      # Control wants tab keys          
DLGC_WANTALLKEYS  = 0x0004      # Control wants all keys          
DLGC_WANTMESSAGE  = 0x0004      # Pass message to control         
DLGC_HASSETSEL    = 0x0008      # Understands EM_SETSEL message   
DLGC_DEFPUSHBUTTON= 0x0010      # Default pushbutton              
DLGC_UNDEFPUSHBUTTON = 0x0020    #  Non-default pushbutton          
DLGC_RADIOBUTTON  = 0x0040       #Radio button                    
DLGC_WANTCHARS    = 0x0080       #Want WM_CHAR messages           
DLGC_STATIC       = 0x0100       #Static item: don't include      
DLGC_BUTTON       = 0x2000       #Button item: can be checked     

LB_CTLCODE         =  0L


# Listbox Return Values

LB_OKAY             = 0
LB_ERR              = (-1)
LB_ERRSPACE         = (-2)


# The idStaticPath parameter to DlgDirList can have the following values
#  ORed if the list box should show other details of the files along with
#  the name of the files;

#                                   all other details also will be returned



# Listbox Notification Codes

LBN_ERRSPACE        = (-2)
LBN_SELCHANGE       = 1
LBN_DBLCLK          = 2
LBN_SELCANCEL       = 3
LBN_SETFOCUS        = 4
LBN_KILLFOCUS       = 5



# Listbox messages

LB_ADDSTRING          = 0x0180
LB_INSERTSTRING       = 0x0181
LB_DELETESTRING       = 0x0182
LB_SELITEMRANGEEX     = 0x0183
LB_RESETCONTENT       = 0x0184
LB_SETSEL             = 0x0185
LB_SETCURSEL          = 0x0186
LB_GETSEL             = 0x0187
LB_GETCURSEL          = 0x0188
LB_GETTEXT            = 0x0189
LB_GETTEXTLEN         = 0x018A
LB_GETCOUNT           = 0x018B
LB_SELECTSTRING       = 0x018C
LB_DIR                = 0x018D
LB_GETTOPINDEX        = 0x018E
LB_FINDSTRING         = 0x018F
LB_GETSELCOUNT        = 0x0190
LB_GETSELITEMS        = 0x0191
LB_SETTABSTOPS        = 0x0192
LB_GETHORIZONTALEXTENT= 0x0193
LB_SETHORIZONTALEXTENT= 0x0194
LB_SETCOLUMNWIDTH     = 0x0195
LB_ADDFILE            = 0x0196
LB_SETTOPINDEX        = 0x0197
LB_GETITEMRECT        = 0x0198
LB_GETITEMDATA        = 0x0199
LB_SETITEMDATA        = 0x019A
LB_SELITEMRANGE       = 0x019B
LB_SETANCHORINDEX     = 0x019C
LB_GETANCHORINDEX     = 0x019D
LB_SETCARETINDEX      = 0x019E
LB_GETCARETINDEX      = 0x019F
LB_SETITEMHEIGHT      = 0x01A0
LB_GETITEMHEIGHT      = 0x01A1
LB_FINDSTRINGEXACT    = 0x01A2
LB_SETLOCALE          = 0x01A5
LB_GETLOCALE          = 0x01A6
LB_SETCOUNT           = 0x01A7

LB_INITSTORAGE        = 0x01A8
LB_ITEMFROMPOINT      = 0x01A9

LB_GETLISTBOXINFO     = 0x01B2

LB_MSGMAX             = 0x01B3



# Listbox Styles

LBS_NOTIFY          = 0x0001L
LBS_SORT            = 0x0002L
LBS_NOREDRAW        = 0x0004L
LBS_MULTIPLESEL     = 0x0008L
LBS_OWNERDRAWFIXED  = 0x0010L
LBS_OWNERDRAWVARIABLE  = 0x0020L
LBS_HASSTRINGS      = 0x0040L
LBS_USETABSTOPS     = 0x0080L
LBS_NOINTEGRALHEIGHT= 0x0100L
LBS_MULTICOLUMN     = 0x0200L
LBS_WANTKEYBOARDINPUT  = 0x0400L
LBS_EXTENDEDSEL     = 0x0800L
LBS_DISABLENOSCROLL = 0x1000L
LBS_NODATA          = 0x2000L

LBS_NOSEL           = 0x4000L

LBS_COMBOBOX        = 0x8000L

LBS_STANDARD        = (LBS_NOTIFY | LBS_SORT | WS_VSCROLL | WS_BORDER)



# Combo Box return Values

CB_OKAY             = 0
CB_ERR              = (-1)
CB_ERRSPACE         = (-2)



# Combo Box Notification Codes

CBN_ERRSPACE        = (-1)
CBN_SELCHANGE       = 1
CBN_DBLCLK          = 2
CBN_SETFOCUS        = 3
CBN_KILLFOCUS       = 4
CBN_EDITCHANGE      = 5
CBN_EDITUPDATE      = 6
CBN_DROPDOWN        = 7
CBN_CLOSEUP         = 8
CBN_SELENDOK        = 9
CBN_SELENDCANCEL    = 10



# Combo Box styles

CBS_SIMPLE          = 0x0001L
CBS_DROPDOWN        = 0x0002L
CBS_DROPDOWNLIST    = 0x0003L
CBS_OWNERDRAWFIXED  = 0x0010L
CBS_OWNERDRAWVARIABLE  = 0x0020L
CBS_AUTOHSCROLL     = 0x0040L
CBS_OEMCONVERT      = 0x0080L
CBS_SORT            = 0x0100L
CBS_HASSTRINGS      = 0x0200L
CBS_NOINTEGRALHEIGHT= 0x0400L
CBS_DISABLENOSCROLL = 0x0800L

CBS_UPPERCASE       = 0x2000L
CBS_LOWERCASE       = 0x4000L



# Combo Box messages

CB_GETEDITSEL             = 0x0140
CB_LIMITTEXT              = 0x0141
CB_SETEDITSEL             = 0x0142
CB_ADDSTRING              = 0x0143
CB_DELETESTRING           = 0x0144
CB_DIR                    = 0x0145
CB_GETCOUNT               = 0x0146
CB_GETCURSEL              = 0x0147
CB_GETLBTEXT              = 0x0148
CB_GETLBTEXTLEN           = 0x0149
CB_INSERTSTRING           = 0x014A
CB_RESETCONTENT           = 0x014B
CB_FINDSTRING             = 0x014C
CB_SELECTSTRING           = 0x014D
CB_SETCURSEL              = 0x014E
CB_SHOWDROPDOWN           = 0x014F
CB_GETITEMDATA            = 0x0150
CB_SETITEMDATA            = 0x0151
CB_GETDROPPEDCONTROLRECT  = 0x0152
CB_SETITEMHEIGHT          = 0x0153
CB_GETITEMHEIGHT          = 0x0154
CB_SETEXTENDEDUI          = 0x0155
CB_GETEXTENDEDUI          = 0x0156
CB_GETDROPPEDSTATE        = 0x0157
CB_FINDSTRINGEXACT        = 0x0158
CB_SETLOCALE              = 0x0159
CB_GETLOCALE              = 0x015A

CB_GETTOPINDEX            = 0x015b
CB_SETTOPINDEX            = 0x015c
CB_GETHORIZONTALEXTENT    = 0x015d
CB_SETHORIZONTALEXTENT    = 0x015e
CB_GETDROPPEDWIDTH        = 0x015f
CB_SETDROPPEDWIDTH        = 0x0160
CB_INITSTORAGE            = 0x0161


CB_GETCOMBOBOXINFO        = 0x0164

CB_MSGMAX                 = 0x0165



# Scroll Bar Styles

SBS_HORZ                  = 0x0000L
SBS_VERT                  = 0x0001L
SBS_TOPALIGN              = 0x0002L
SBS_LEFTALIGN             = 0x0002L
SBS_BOTTOMALIGN           = 0x0004L
SBS_RIGHTALIGN            = 0x0004L
SBS_SIZEBOXTOPLEFTALIGN   = 0x0002L
SBS_SIZEBOXBOTTOMRIGHTALIGN  = 0x0004L
SBS_SIZEBOX               = 0x0008L
SBS_SIZEGRIP              = 0x0010L


# Scroll bar messages

#ifndef NOWINMESSAGES
SBM_SETPOS                = 0x00E0 #not in win3.1
SBM_GETPOS                = 0x00E1 #not in win3.1
SBM_SETRANGE              = 0x00E2 #not in win3.1
SBM_SETRANGEREDRAW        = 0x00E6 #not in win3.1
SBM_GETRANGE              = 0x00E3 #not in win3.1
SBM_ENABLE_ARROWS         = 0x00E4 #not in win3.1

SBM_SETSCROLLINFO         = 0x00E9
SBM_GETSCROLLINFO         = 0x00EA

SBM_GETSCROLLBARINFO      = 0x00EB



SIF_RANGE         = 0x0001
SIF_PAGE          = 0x0002
SIF_POS           = 0x0004
SIF_DISABLENOSCROLL  = 0x0008
SIF_TRACKPOS      = 0x0010
SIF_ALL           = (SIF_RANGE | SIF_PAGE | SIF_POS | SIF_TRACKPOS)


# MDI client style bits

MDIS_ALLCHILDSTYLES  = 0x0001


# wParam Flags for WM_MDITILE and WM_MDICASCADE messages.

MDITILE_VERTICAL     = 0x0000 #not in win3.1
MDITILE_HORIZONTAL   = 0x0001 #not in win3.1
MDITILE_SKIPDISABLED = 0x0002 #not in win3.1

MDITILE_ZORDER       = 0x0004



# Commands to pass to WinHelp()

HELP_CONTEXT    = 0x0001L   #Display topic in ulTopic
HELP_QUIT       = 0x0002L   #Terminate help
HELP_INDEX      = 0x0003L   #Display index
HELP_CONTENTS   = 0x0003L
HELP_HELPONHELP = 0x0004L   #Display help on using help
HELP_SETINDEX   = 0x0005L   #Set current Index for multi index help
HELP_SETCONTENTS= 0x0005L
HELP_CONTEXTPOPUP = 0x0008L
HELP_FORCEFILE  = 0x0009L
HELP_KEY        = 0x0101L  # Display topic for keyword in offabData
HELP_COMMAND    = 0x0102L
HELP_PARTIALKEY = 0x0105L
HELP_MULTIKEY   = 0x0201L
HELP_SETWINPOS  = 0x0203L
HELP_CONTEXTMENU= 0x000a
HELP_FINDER     = 0x000b
HELP_WM_HELP    = 0x000c
HELP_SETPOPUP_POS = 0x000d

HELP_TCARD            = 0x8000
HELP_TCARD_DATA       = 0x0010
HELP_TCARD_OTHER_CALLER = 0x0011

# These are in winhelp.h in Win95.
IDH_NO_HELP                     = 28440
IDH_MISSING_CONTEXT             = 28441 # Control doesn't have matching help context
IDH_GENERIC_HELP_BUTTON         = 28442 # Property sheet help button
IDH_OK                          = 28443
IDH_CANCEL                      = 28444
IDH_HELP                        = 28445


GR_GDIOBJECTS       = 0       # Count of GDI objects
GR_USEROBJECTS      = 1       # Count of USER objects



# Parameter for SystemParametersInfo.


SPI_GETBEEP               = 0x0001
SPI_SETBEEP               = 0x0002
SPI_GETMOUSE              = 0x0003
SPI_SETMOUSE              = 0x0004
SPI_GETBORDER             = 0x0005
SPI_SETBORDER             = 0x0006
SPI_GETKEYBOARDSPEED      = 0x000A
SPI_SETKEYBOARDSPEED      = 0x000B
SPI_LANGDRIVER            = 0x000C
SPI_ICONHORIZONTALSPACING = 0x000D
SPI_GETSCREENSAVETIMEOUT  = 0x000E
SPI_SETSCREENSAVETIMEOUT  = 0x000F
SPI_GETSCREENSAVEACTIVE   = 0x0010
SPI_SETSCREENSAVEACTIVE   = 0x0011
SPI_GETGRIDGRANULARITY    = 0x0012
SPI_SETGRIDGRANULARITY    = 0x0013
SPI_SETDESKWALLPAPER      = 0x0014
SPI_SETDESKPATTERN        = 0x0015
SPI_GETKEYBOARDDELAY      = 0x0016
SPI_SETKEYBOARDDELAY      = 0x0017
SPI_ICONVERTICALSPACING   = 0x0018
SPI_GETICONTITLEWRAP      = 0x0019
SPI_SETICONTITLEWRAP      = 0x001A
SPI_GETMENUDROPALIGNMENT  = 0x001B
SPI_SETMENUDROPALIGNMENT  = 0x001C
SPI_SETDOUBLECLKWIDTH     = 0x001D
SPI_SETDOUBLECLKHEIGHT    = 0x001E
SPI_GETICONTITLELOGFONT   = 0x001F
SPI_SETDOUBLECLICKTIME    = 0x0020
SPI_SETMOUSEBUTTONSWAP    = 0x0021
SPI_SETICONTITLELOGFONT   = 0x0022
SPI_GETFASTTASKSWITCH     = 0x0023
SPI_SETFASTTASKSWITCH     = 0x0024
SPI_SETDRAGFULLWINDOWS    = 0x0025
SPI_GETDRAGFULLWINDOWS    = 0x0026
SPI_GETNONCLIENTMETRICS   = 0x0029
SPI_SETNONCLIENTMETRICS   = 0x002A
SPI_GETMINIMIZEDMETRICS   = 0x002B
SPI_SETMINIMIZEDMETRICS   = 0x002C
SPI_GETICONMETRICS        = 0x002D
SPI_SETICONMETRICS        = 0x002E
SPI_SETWORKAREA           = 0x002F
SPI_GETWORKAREA           = 0x0030
SPI_SETPENWINDOWS         = 0x0031

SPI_GETHIGHCONTRAST       = 0x0042
SPI_SETHIGHCONTRAST       = 0x0043
SPI_GETKEYBOARDPREF       = 0x0044
SPI_SETKEYBOARDPREF       = 0x0045
SPI_GETSCREENREADER       = 0x0046
SPI_SETSCREENREADER       = 0x0047
SPI_GETANIMATION          = 0x0048
SPI_SETANIMATION          = 0x0049
SPI_GETFONTSMOOTHING      = 0x004A
SPI_SETFONTSMOOTHING      = 0x004B
SPI_SETDRAGWIDTH          = 0x004C
SPI_SETDRAGHEIGHT         = 0x004D
SPI_SETHANDHELD           = 0x004E
SPI_GETLOWPOWERTIMEOUT    = 0x004F
SPI_GETPOWEROFFTIMEOUT    = 0x0050
SPI_SETLOWPOWERTIMEOUT    = 0x0051
SPI_SETPOWEROFFTIMEOUT    = 0x0052
SPI_GETLOWPOWERACTIVE     = 0x0053
SPI_GETPOWEROFFACTIVE     = 0x0054
SPI_SETLOWPOWERACTIVE     = 0x0055
SPI_SETPOWEROFFACTIVE     = 0x0056
SPI_SETCURSORS            = 0x0057
SPI_SETICONS              = 0x0058
SPI_GETDEFAULTINPUTLANG   = 0x0059
SPI_SETDEFAULTINPUTLANG   = 0x005A
SPI_SETLANGTOGGLE         = 0x005B
SPI_GETWINDOWSEXTENSION   = 0x005C
SPI_SETMOUSETRAILS        = 0x005D
SPI_GETMOUSETRAILS        = 0x005E
SPI_SETSCREENSAVERRUNNING = 0x0061
SPI_SCREENSAVERRUNNING    = SPI_SETSCREENSAVERRUNNING

SPI_GETFILTERKEYS        = 0x0032
SPI_SETFILTERKEYS        = 0x0033
SPI_GETTOGGLEKEYS        = 0x0034
SPI_SETTOGGLEKEYS        = 0x0035
SPI_GETMOUSEKEYS         = 0x0036
SPI_SETMOUSEKEYS         = 0x0037
SPI_GETSHOWSOUNDS        = 0x0038
SPI_SETSHOWSOUNDS        = 0x0039
SPI_GETSTICKYKEYS        = 0x003A
SPI_SETSTICKYKEYS        = 0x003B
SPI_GETACCESSTIMEOUT     = 0x003C
SPI_SETACCESSTIMEOUT     = 0x003D

SPI_GETSERIALKEYS        = 0x003E
SPI_SETSERIALKEYS        = 0x003F

SPI_GETSOUNDSENTRY       = 0x0040
SPI_SETSOUNDSENTRY       = 0x0041


SPI_GETSNAPTODEFBUTTON   = 0x005F
SPI_SETSNAPTODEFBUTTON   = 0x0060


SPI_GETMOUSEHOVERWIDTH   = 0x0062
SPI_SETMOUSEHOVERWIDTH   = 0x0063
SPI_GETMOUSEHOVERHEIGHT  = 0x0064
SPI_SETMOUSEHOVERHEIGHT  = 0x0065
SPI_GETMOUSEHOVERTIME    = 0x0066
SPI_SETMOUSEHOVERTIME    = 0x0067
SPI_GETWHEELSCROLLLINES  = 0x0068
SPI_SETWHEELSCROLLLINES  = 0x0069
SPI_GETMENUSHOWDELAY     = 0x006A
SPI_SETMENUSHOWDELAY     = 0x006B

SPI_GETSHOWIMEUI        = 0x006E
SPI_SETSHOWIMEUI        = 0x006F

SPI_GETMOUSESPEED       = 0x0070
SPI_SETMOUSESPEED       = 0x0071
SPI_GETSCREENSAVERRUNNING = 0x0072
SPI_GETDESKWALLPAPER    = 0x0073


SPI_GETACTIVEWINDOWTRACKING       = 0x1000
SPI_SETACTIVEWINDOWTRACKING       = 0x1001
SPI_GETMENUANIMATION              = 0x1002
SPI_SETMENUANIMATION              = 0x1003
SPI_GETCOMBOBOXANIMATION          = 0x1004
SPI_SETCOMBOBOXANIMATION          = 0x1005
SPI_GETLISTBOXSMOOTHSCROLLING     = 0x1006
SPI_SETLISTBOXSMOOTHSCROLLING     = 0x1007
SPI_GETGRADIENTCAPTIONS           = 0x1008
SPI_SETGRADIENTCAPTIONS           = 0x1009
SPI_GETKEYBOARDCUES               = 0x100A
SPI_SETKEYBOARDCUES               = 0x100B
SPI_GETMENUUNDERLINES             = SPI_GETKEYBOARDCUES
SPI_SETMENUUNDERLINES             = SPI_SETKEYBOARDCUES
SPI_GETACTIVEWNDTRKZORDER         = 0x100C
SPI_SETACTIVEWNDTRKZORDER         = 0x100D
SPI_GETHOTTRACKING                = 0x100E
SPI_SETHOTTRACKING                = 0x100F
SPI_GETMENUFADE                   = 0x1012
SPI_SETMENUFADE                   = 0x1013
SPI_GETSELECTIONFADE              = 0x1014
SPI_SETSELECTIONFADE              = 0x1015
SPI_GETTOOLTIPANIMATION           = 0x1016
SPI_SETTOOLTIPANIMATION           = 0x1017
SPI_GETTOOLTIPFADE                = 0x1018
SPI_SETTOOLTIPFADE                = 0x1019
SPI_GETCURSORSHADOW               = 0x101A
SPI_SETCURSORSHADOW               = 0x101B


SPI_GETMOUSESONAR                 = 0x101C
SPI_SETMOUSESONAR                 = 0x101D
SPI_GETMOUSECLICKLOCK             = 0x101E
SPI_SETMOUSECLICKLOCK             = 0x101F
SPI_GETMOUSEVANISH                = 0x1020
SPI_SETMOUSEVANISH                = 0x1021
SPI_GETFLATMENU                   = 0x1022
SPI_SETFLATMENU                   = 0x1023
SPI_GETDROPSHADOW                 = 0x1024
SPI_SETDROPSHADOW                 = 0x1025
SPI_GETBLOCKSENDINPUTRESETS       = 0x1026
SPI_SETBLOCKSENDINPUTRESETS       = 0x1027

SPI_GETUIEFFECTS                  = 0x103E
SPI_SETUIEFFECTS                  = 0x103F

SPI_GETFOREGROUNDLOCKTIMEOUT      = 0x2000
SPI_SETFOREGROUNDLOCKTIMEOUT      = 0x2001
SPI_GETACTIVEWNDTRKTIMEOUT        = 0x2002
SPI_SETACTIVEWNDTRKTIMEOUT        = 0x2003
SPI_GETFOREGROUNDFLASHCOUNT       = 0x2004
SPI_SETFOREGROUNDFLASHCOUNT       = 0x2005
SPI_GETCARETWIDTH                 = 0x2006
SPI_SETCARETWIDTH                 = 0x2007

SPI_GETMOUSECLICKLOCKTIME         = 0x2008
SPI_SETMOUSECLICKLOCKTIME         = 0x2009
SPI_GETFONTSMOOTHINGTYPE          = 0x200A
SPI_SETFONTSMOOTHINGTYPE          = 0x200B

# constants for SPI_GETFONTSMOOTHINGTYPE and SPI_SETFONTSMOOTHINGTYPE:
FE_FONTSMOOTHINGSTANDARD          = 0x0001
FE_FONTSMOOTHINGCLEARTYPE         = 0x0002

SPI_GETFONTSMOOTHINGCONTRAST         = 0x200C
SPI_SETFONTSMOOTHINGCONTRAST         = 0x200D

SPI_GETFOCUSBORDERWIDTH           = 0x200E
SPI_SETFOCUSBORDERWIDTH           = 0x200F
SPI_GETFOCUSBORDERHEIGHT          = 0x2010
SPI_SETFOCUSBORDERHEIGHT          = 0x2011

SPI_GETFONTSMOOTHINGORIENTATION         = 0x2012
SPI_SETFONTSMOOTHINGORIENTATION         = 0x2013

# constants for SPI_GETFONTSMOOTHINGORIENTATION and SPI_SETFONTSMOOTHINGORIENTATION:
FE_FONTSMOOTHINGORIENTATIONBGR = 0x0000
FE_FONTSMOOTHINGORIENTATIONRGB = 0x0001


# Flags

SPIF_UPDATEINIFILE  = 0x0001
SPIF_SENDWININICHANGE = 0x0002
SPIF_SENDCHANGE       = SPIF_SENDWININICHANGE


METRICS_USEDEFAULT  = -1



ARW_BOTTOMLEFT            = 0x0000L
ARW_BOTTOMRIGHT           = 0x0001L
ARW_TOPLEFT               = 0x0002L
ARW_TOPRIGHT              = 0x0003L
ARW_STARTMASK             = 0x0003L
ARW_STARTRIGHT            = 0x0001L
ARW_STARTTOP              = 0x0002L

ARW_LEFT                  = 0x0000L
ARW_RIGHT                 = 0x0000L
ARW_UP                    = 0x0004L
ARW_DOWN                  = 0x0004L
ARW_HIDE                  = 0x0008L


# flags for SERIALKEYS dwFlags field
SERKF_SERIALKEYSON= 0x00000001
SERKF_AVAILABLE   = 0x00000002
SERKF_INDICATOR   = 0x00000004


# flags for HIGHCONTRAST dwFlags field
HCF_HIGHCONTRASTON= 0x00000001
HCF_AVAILABLE     = 0x00000002
HCF_HOTKEYACTIVE  = 0x00000004
HCF_CONFIRMHOTKEY = 0x00000008
HCF_HOTKEYSOUND   = 0x00000010
HCF_INDICATOR     = 0x00000020
HCF_HOTKEYAVAILABLE = 0x00000040
HCF_LOGONDESKTOP  = 0x00000100
HCF_DEFAULTDESKTOP= 0x00000200

# Flags for ChangeDisplaySettings
CDS_UPDATEREGISTRY         = 0x00000001
CDS_TEST                   = 0x00000002
CDS_FULLSCREEN             = 0x00000004
CDS_GLOBAL                 = 0x00000008
CDS_SET_PRIMARY            = 0x00000010
CDS_VIDEOPARAMETERS        = 0x00000020


CDS_RESET                  = 0x40000000
CDS_RESET_EX               = 0x20000000
CDS_NORESET                = 0x10000000


# Return values for ChangeDisplaySettings
DISP_CHANGE_SUCCESSFUL       = 0
DISP_CHANGE_RESTART          = 1
DISP_CHANGE_FAILED           = -1
DISP_CHANGE_BADMODE          = -2
DISP_CHANGE_NOTUPDATED       = -3
DISP_CHANGE_BADFLAGS         = -4
DISP_CHANGE_BADPARAM         = -5
DISP_CHANGE_BADDUALVIEW      = -6

# Flags for EnumDisplaySettingsEx
EDS_RAWMODE                 = 0x00000002
EDS_ROTATEDMODE             = 0x00000004


# Flags for EnumDisplayDevices
EDD_GET_DEVICE_INTERFACE_NAME = 0x00000001




# FILTERKEYS dwFlags field

FKF_FILTERKEYSON  = 0x00000001
FKF_AVAILABLE     = 0x00000002
FKF_HOTKEYACTIVE  = 0x00000004
FKF_CONFIRMHOTKEY = 0x00000008
FKF_HOTKEYSOUND   = 0x00000010
FKF_INDICATOR     = 0x00000020
FKF_CLICKON       = 0x00000040



# STICKYKEYS dwFlags field

SKF_STICKYKEYSON  = 0x00000001
SKF_AVAILABLE     = 0x00000002
SKF_HOTKEYACTIVE  = 0x00000004
SKF_CONFIRMHOTKEY = 0x00000008
SKF_HOTKEYSOUND   = 0x00000010
SKF_INDICATOR     = 0x00000020
SKF_AUDIBLEFEEDBACK  = 0x00000040
SKF_TRISTATE      = 0x00000080
SKF_TWOKEYSOFF    = 0x00000100


SKF_LALTLATCHED     = 0x10000000
SKF_LCTLLATCHED     = 0x04000000
SKF_LSHIFTLATCHED   = 0x01000000
SKF_RALTLATCHED     = 0x20000000
SKF_RCTLLATCHED     = 0x08000000
SKF_RSHIFTLATCHED   = 0x02000000
SKF_LWINLATCHED     = 0x40000000
SKF_RWINLATCHED     = auxfuncs.safe_long(0x80000000)
SKF_LALTLOCKED      = 0x00100000
SKF_LCTLLOCKED      = 0x00040000
SKF_LSHIFTLOCKED    = 0x00010000
SKF_RALTLOCKED      = 0x00200000
SKF_RCTLLOCKED      = 0x00080000
SKF_RSHIFTLOCKED    = 0x00020000
SKF_LWINLOCKED      = 0x00400000
SKF_RWINLOCKED      = 0x00800000


# MOUSEKEYS dwFlags field

MKF_MOUSEKEYSON   = 0x00000001
MKF_AVAILABLE     = 0x00000002
MKF_HOTKEYACTIVE  = 0x00000004
MKF_CONFIRMHOTKEY = 0x00000008
MKF_HOTKEYSOUND   = 0x00000010
MKF_INDICATOR     = 0x00000020
MKF_MODIFIERS     = 0x00000040
MKF_REPLACENUMBERS= 0x00000080

MKF_LEFTBUTTONSEL = 0x10000000
MKF_RIGHTBUTTONSEL= 0x20000000
MKF_LEFTBUTTONDOWN= 0x01000000
MKF_RIGHTBUTTONDOWN = 0x02000000
MKF_MOUSEMODE     = auxfuncs.safe_long(0x80000000)



# ACCESSTIMEOUT dwFlags field

ATF_TIMEOUTON     = 0x00000001
ATF_ONOFFFEEDBACK = 0x00000002

# values for SOUNDSENTRY iFSGrafEffect field
SSGF_NONE       = 0
SSGF_DISPLAY    = 3

# values for SOUNDSENTRY iFSTextEffect field
SSTF_NONE       = 0
SSTF_CHARS      = 1
SSTF_BORDER     = 2
SSTF_DISPLAY    = 3

# values for SOUNDSENTRY iWindowsEffect field
SSWF_NONE     = 0
SSWF_TITLE    = 1
SSWF_WINDOW   = 2
SSWF_DISPLAY  = 3
SSWF_CUSTOM   = 4


# SOUNDSENTRY dwFlags field

SSF_SOUNDSENTRYON = 0x00000001
SSF_AVAILABLE     = 0x00000002
SSF_INDICATOR     = 0x00000004


# TOGGLEKEYS dwFlags field

TKF_TOGGLEKEYSON  = 0x00000001
TKF_AVAILABLE     = 0x00000002
TKF_HOTKEYACTIVE  = 0x00000004
TKF_CONFIRMHOTKEY = 0x00000008
TKF_HOTKEYSOUND   = 0x00000010
TKF_INDICATOR     = 0x00000020



# SetLastErrorEx() types.


SLE_ERROR     = 0x00000001
SLE_MINORERROR= 0x00000002
SLE_WARNING   = 0x00000003


# Multimonitor API.


MONITOR_DEFAULTTONULL     = 0x00000000
MONITOR_DEFAULTTOPRIMARY  = 0x00000001
MONITOR_DEFAULTTONEAREST  = 0x00000002

MONITORINFOF_PRIMARY      = 0x00000001


# dwFlags for SetWinEventHook

WINEVENT_OUTOFCONTEXT = 0x0000  #// Events are ASYNC
WINEVENT_SKIPOWNTHREAD= 0x0001  #// Don't call back for events on installer's thread
WINEVENT_SKIPOWNPROCESS = 0x0002  #// Don't call back for events on installer's process
WINEVENT_INCONTEXT    = 0x0004  #// Events are SYNC, this causes your dll to be injected into every process


# Common object IDs (cookies, only for sending WM_GETOBJECT to get at the
# thing in question).  Positive IDs are reserved for apps (app specific),
# negative IDs are system things and are global, 0 means "just little old
# me".

CHILDID_SELF        = 0
INDEXID_OBJECT      = 0
INDEXID_CONTAINER   = 0


# Reserved IDs for system objects

OBJID_WINDOW        = 0x00000000L
OBJID_SYSMENU       = 0xFFFFFFFFL
OBJID_TITLEBAR      = 0xFFFFFFFEL
OBJID_MENU          = 0xFFFFFFFDL
OBJID_CLIENT        = 0xFFFFFFFCL
OBJID_VSCROLL       = 0xFFFFFFFBL
OBJID_HSCROLL       = 0xFFFFFFFAL
OBJID_SIZEGRIP      = 0xFFFFFFF9L
OBJID_CARET         = 0xFFFFFFF8L
OBJID_CURSOR        = 0xFFFFFFF7L
OBJID_ALERT         = 0xFFFFFFF6L
OBJID_SOUND         = 0xFFFFFFF5L
OBJID_QUERYCLASSNAMEIDX = 0xFFFFFFF4L
OBJID_NATIVEOM      = 0xFFFFFFF0L


# EVENT DEFINITION

EVENT_MIN         = 0x00000001
EVENT_MAX         = 0x7FFFFFFF


#  EVENT_SYSTEM_SOUND
#  Sent when a sound is played.  Currently nothing is generating this, we
#  this event when a system sound (for menus, etc) is played.  Apps
#  generate this, if accessible, when a private sound is played.  For
#  example, if Mail plays a "New Mail" sound.

#  System Sounds:
#  (Generated by PlaySoundEvent in USER itself)
#      hwnd            is NULL
#      idObject        is OBJID_SOUND
#      idChild         is sound child ID if one
#  App Sounds:
#  (PlaySoundEvent won't generate notification; up to app)
#      hwnd + idObject gets interface pointer to Sound object
#      idChild identifies the sound in question
#  are going to be cleaning up the SOUNDSENTRY feature in the control panel
#  and will use this at that time.  Applications implementing WinEvents
#  are perfectly welcome to use it.  Clients of IAccessible* will simply
#  turn around and get back a non-visual object that describes the sound.

EVENT_SYSTEM_SOUND            = 0x0001


# EVENT_SYSTEM_ALERT
# System Alerts:
# (Generated by MessageBox() calls for example)
#      hwnd            is hwndMessageBox
#      idObject        is OBJID_ALERT
# App Alerts:
# (Generated whenever)
#      hwnd+idObject gets interface pointer to Alert

EVENT_SYSTEM_ALERT            = 0x0002


# EVENT_SYSTEM_FOREGROUND
# Sent when the foreground (active) window changes, even if it is changing
# to another window in the same thread as the previous one.
#      hwnd            is hwndNewForeground
#      idObject        is OBJID_WINDOW
#      idChild    is INDEXID_OBJECT

EVENT_SYSTEM_FOREGROUND       = 0x0003


# Menu
#      hwnd            is window (top level window or popup menu window)
#      idObject        is ID of control (OBJID_MENU, OBJID_SYSMENU, OBJID_SELF for popup)
#      idChild         is CHILDID_SELF

# EVENT_SYSTEM_MENUSTART
# EVENT_SYSTEM_MENUEND
# For MENUSTART, hwnd+idObject+idChild refers to the control with the menu bar,
#  or the control bringing up the context menu.

# Sent when entering into and leaving from menu mode (system, app bar, and
# track popups).

EVENT_SYSTEM_MENUSTART        = 0x0004
EVENT_SYSTEM_MENUEND          = 0x0005


# EVENT_SYSTEM_MENUPOPUPSTART
# EVENT_SYSTEM_MENUPOPUPEND
# Sent when a menu popup comes up and just before it is taken down.  Note
# that for a call to TrackPopupMenu(), a client will see EVENT_SYSTEM_MENUSTART
# followed almost immediately by EVENT_SYSTEM_MENUPOPUPSTART for the popup
# being shown.

# For MENUPOPUP, hwnd+idObject+idChild refers to the NEW popup coming up, not the
# parent item which is hierarchical.  You can get the parent menu/popup by
# asking for the accParent object.

EVENT_SYSTEM_MENUPOPUPSTART   = 0x0006
EVENT_SYSTEM_MENUPOPUPEND     = 0x0007



# EVENT_SYSTEM_CAPTURESTART
# EVENT_SYSTEM_CAPTUREEND
# Sent when a window takes the capture and releases the capture.

EVENT_SYSTEM_CAPTURESTART     = 0x0008
EVENT_SYSTEM_CAPTUREEND       = 0x0009


# Move Size
# EVENT_SYSTEM_MOVESIZESTART
# EVENT_SYSTEM_MOVESIZEEND
# Sent when a window enters and leaves move-size dragging mode.

EVENT_SYSTEM_MOVESIZESTART    = 0x000A
EVENT_SYSTEM_MOVESIZEEND      = 0x000B


# Context Help
# EVENT_SYSTEM_CONTEXTHELPSTART
# EVENT_SYSTEM_CONTEXTHELPEND
# Sent when a window enters and leaves context sensitive help mode.

EVENT_SYSTEM_CONTEXTHELPSTART = 0x000C
EVENT_SYSTEM_CONTEXTHELPEND   = 0x000D


# Drag & Drop
# EVENT_SYSTEM_DRAGDROPSTART
# EVENT_SYSTEM_DRAGDROPEND
# Send the START notification just before going into drag&drop loop.  Send
# the END notification just after canceling out.
# Note that it is up to apps and OLE to generate this, since the system
# doesn't know.  Like EVENT_SYSTEM_SOUND, it will be a while before this
# is prevalent.

EVENT_SYSTEM_DRAGDROPSTART    = 0x000E
EVENT_SYSTEM_DRAGDROPEND      = 0x000F


# Dialog
# Send the START notification right after the dialog is completely
#  initialized and visible.  Send the END right before the dialog
#  is hidden and goes away.
# EVENT_SYSTEM_DIALOGSTART
# EVENT_SYSTEM_DIALOGEND

EVENT_SYSTEM_DIALOGSTART      = 0x0010
EVENT_SYSTEM_DIALOGEND        = 0x0011


# EVENT_SYSTEM_SCROLLING
# EVENT_SYSTEM_SCROLLINGSTART
# EVENT_SYSTEM_SCROLLINGEND
# Sent when beginning and ending the tracking of a scrollbar in a window,
# and also for scrollbar controls.

EVENT_SYSTEM_SCROLLINGSTART   = 0x0012
EVENT_SYSTEM_SCROLLINGEND     = 0x0013


# Alt-Tab Window
# Send the START notification right after the switch window is initialized
# and visible.  Send the END right before it is hidden and goes away.
# EVENT_SYSTEM_SWITCHSTART
# EVENT_SYSTEM_SWITCHEND

EVENT_SYSTEM_SWITCHSTART      = 0x0014
EVENT_SYSTEM_SWITCHEND        = 0x0015


# EVENT_SYSTEM_MINIMIZESTART
# EVENT_SYSTEM_MINIMIZEEND
# Sent when a window minimizes and just before it restores.

EVENT_SYSTEM_MINIMIZESTART    = 0x0016
EVENT_SYSTEM_MINIMIZEEND      = 0x0017


EVENT_CONSOLE_CARET           = 0x4001
EVENT_CONSOLE_UPDATE_REGION   = 0x4002
EVENT_CONSOLE_UPDATE_SIMPLE   = 0x4003
EVENT_CONSOLE_UPDATE_SCROLL   = 0x4004
EVENT_CONSOLE_LAYOUT          = 0x4005
EVENT_CONSOLE_START_APPLICATION = 0x4006
EVENT_CONSOLE_END_APPLICATION = 0x4007

CONSOLE_APPLICATION_16BIT     = 0x0001


# Flags for EVENT_CONSOLE_CARET

CONSOLE_CARET_SELECTION       = 0x0001
CONSOLE_CARET_VISIBLE         = 0x0002



# Object events

# The system AND apps generate these.  The system generates these for
# real windows.  Apps generate these for objects within their window which
# act like a separate control, e.g. an item in a list view.

# When the system generate them, dwParam2 is always WMOBJID_SELF.  When
# apps generate them, apps put the has-meaning-to-the-app-only ID value
# in dwParam2.
# For all events, if you want detailed accessibility information, callers
# should
#     # Call AccessibleObjectFromWindow() with the hwnd, idObject parameters
#          of the event, and IID_IAccessible as the REFIID, to get back an
#          IAccessible* to talk to
#     # Initialize and fill in a VARIANT as VT_I4 with lVal the idChild
#          parameter of the event.
#     # If idChild isn't zero, call get_accChild() in the container to see
#          if the child is an object in its own right.  If so, you will get
#          back an IDispatch* object for the child.  You should release the
#          parent, and call QueryInterface() on the child object to get its
#          IAccessible*.  Then you talk directly to the child.  Otherwise,
#          if get_accChild() returns you nothing, you should continue to
#          use the child VARIANT.  You will ask the container for the properties
#          of the child identified by the VARIANT.  In other words, the
#          child in this case is accessible but not a full-blown object.
#          Like a button on a titlebar which is 'small' and has no children.



# For all EVENT_OBJECT events,
#      hwnd is the dude to Send the WM_GETOBJECT message to (unless NULL,
#          see above for system things)
#      idObject is the ID of the object that can resolve any queries a
#          client might have.  It's a way to deal with windowless controls,
#          controls that are just drawn on the screen in some larger parent
#          window (like SDM), or standard frame elements of a window.
#      idChild is the piece inside of the object that is affected.  This
#          allows clients to access things that are too small to have full
#          blown objects in their own right.  Like the thumb of a scrollbar.
#          The hwnd/idObject pair gets you to the container, the dude you
#          probably want to talk to most of the time anyway.  The idChild
#          can then be passed into the acc properties to get the name/value
#          of it as needed.

# Example #1:
#      System propagating a listbox selection change
#      EVENT_OBJECT_SELECTION
#          hwnd == listbox hwnd
#          idObject == OBJID_WINDOW
#          idChild == new selected item, or CHILDID_SELF if
#              nothing now selected within container.
#      Word '97 propagating a listbox selection change
#          hwnd == SDM window
#          idObject == SDM ID to get at listbox 'control'
#          idChild == new selected item, or CHILDID_SELF if
#              nothing

# Example #2:
#      System propagating a menu item selection on the menu bar
#      EVENT_OBJECT_SELECTION
#          hwnd == top level window
#          idObject == OBJID_MENU
#          idChild == ID of child menu bar item selected

# Example #3:
#      System propagating a dropdown coming off of said menu bar item
#      EVENT_OBJECT_CREATE
#          hwnd == popup item
#          idObject == OBJID_WINDOW
#          idChild == CHILDID_SELF

# Example #4:

# For EVENT_OBJECT_REORDER, the object referred to by hwnd/idObject is the
# PARENT container in which the zorder is occurring.  This is because if
# one child is zordering, all of them are changing their relative zorder.

EVENT_OBJECT_CREATE               = 0x8000  #// hwnd + ID + idChild is created item
EVENT_OBJECT_DESTROY              = 0x8001  #// hwnd + ID + idChild is destroyed item
EVENT_OBJECT_SHOW                 = 0x8002  #// hwnd + ID + idChild is shown item
EVENT_OBJECT_HIDE                 = 0x8003  #// hwnd + ID + idChild is hidden item
EVENT_OBJECT_REORDER              = 0x8004  #// hwnd + ID + idChild is parent of zordering children

# NOTE:
# Minimize the number of notifications!

# When you are hiding a parent object, obviously all child objects are no
# longer visible on screen.  They still have the same "visible" status,
# but are not truly visible.  Hence do not send HIDE notifications for the
# children also.  One implies all.  The same goes for SHOW.



EVENT_OBJECT_FOCUS                = 0x8005  #// hwnd + ID + idChild is focused item
EVENT_OBJECT_SELECTION            = 0x8006  #// hwnd + ID + idChild is selected item (if only one), or idChild is OBJID_WINDOW if complex
EVENT_OBJECT_SELECTIONADD         = 0x8007  #// hwnd + ID + idChild is item added
EVENT_OBJECT_SELECTIONREMOVE      = 0x8008  #// hwnd + ID + idChild is item removed
EVENT_OBJECT_SELECTIONWITHIN      = 0x8009  #// hwnd + ID + idChild is parent of changed selected items


# NOTES:
# There is only one "focused" child item in a parent.  This is the place
# keystrokes are going at a given moment.  Hence only send a notification
# about where the NEW focus is going.  A NEW item getting the focus already
# implies that the OLD item is losing it.

# SELECTION however can be multiple.  Hence the different SELECTION
# notifications.  Here's when to use each:

# (1) Send a SELECTION notification in the simple single selection
#     case (like the focus) when the item with the selection is
#     merely moving to a different item within a container.  hwnd + ID
#     is the container control, idChildItem is the new child with the
#     selection.

# (2) Send a SELECTIONADD notification when a new item has simply been added
#     to the selection within a container.  This is appropriate when the
#     number of newly selected items is very small.  hwnd + ID is the
#     container control, idChildItem is the new child added to the selection.

# (3) Send a SELECTIONREMOVE notification when a new item has simply been
#     removed from the selection within a container.  This is appropriate
#     when the number of newly selected items is very small, just like
#     SELECTIONADD.  hwnd + ID is the container control, idChildItem is the
#     new child removed from the selection.

# (4) Send a SELECTIONWITHIN notification when the selected items within a
#     control have changed substantially.  Rather than propagate a large
#     number of changes to reflect removal for some items, addition of
#     others, just tell somebody who cares that a lot happened.  It will
#     be faster an easier for somebody watching to just turn around and
#     query the container control what the new bunch of selected items
#     are.


EVENT_OBJECT_STATECHANGE          = 0x800A  #// hwnd + ID + idChild is item w/ state change

# Examples of when to send an EVENT_OBJECT_STATECHANGE include
#     # It is being enabled/disabled (USER does for windows)
#     # It is being pressed/released (USER does for buttons)
#     # It is being checked/unchecked (USER does for radio/check buttons)

EVENT_OBJECT_LOCATIONCHANGE       = 0x800B  #// hwnd + ID + idChild is moved/sized item


# Note:
# A LOCATIONCHANGE is not sent for every child object when the parent
# changes shape/moves.  Send one notification for the topmost object
# that is changing.  For example, if the user resizes a top level window,
# USER will generate a LOCATIONCHANGE for it, but not for the menu bar,
# title bar, scrollbars, etc.  that are also changing shape/moving.

# In other words, it only generates LOCATIONCHANGE notifications for
# real windows that are moving/sizing.  It will not generate a LOCATIONCHANGE
# for every non-floating child window when the parent moves (the children are
# logically moving also on screen, but not relative to the parent).

# Now, if the app itself resizes child windows as a result of being
# sized, USER will generate LOCATIONCHANGEs for those dudes also because
# it doesn't know better.

# Note also that USER will generate LOCATIONCHANGE notifications for two
# non-window sys objects:
#      (1) System caret
#      (2) Cursor


EVENT_OBJECT_NAMECHANGE           = 0x800C  #// hwnd + ID + idChild is item w/ name change
EVENT_OBJECT_DESCRIPTIONCHANGE    = 0x800D  #// hwnd + ID + idChild is item w/ desc change
EVENT_OBJECT_VALUECHANGE          = 0x800E  #// hwnd + ID + idChild is item w/ value change
EVENT_OBJECT_PARENTCHANGE         = 0x800F  #// hwnd + ID + idChild is item w/ new parent
EVENT_OBJECT_HELPCHANGE           = 0x8010 # // hwnd + ID + idChild is item w/ help change
EVENT_OBJECT_DEFACTIONCHANGE      = 0x8011  #// hwnd + ID + idChild is item w/ def action change
EVENT_OBJECT_ACCELERATORCHANGE    = 0x8012  #// hwnd + ID + idChild is item w/ keybd accel change



# Child IDs




# System Sounds (idChild of system SOUND notification)

SOUND_SYSTEM_STARTUP            = 1
SOUND_SYSTEM_SHUTDOWN           = 2
SOUND_SYSTEM_BEEP               = 3
SOUND_SYSTEM_ERROR              = 4
SOUND_SYSTEM_QUESTION           = 5
SOUND_SYSTEM_WARNING            = 6
SOUND_SYSTEM_INFORMATION        = 7
SOUND_SYSTEM_MAXIMIZE           = 8
SOUND_SYSTEM_MINIMIZE           = 9
SOUND_SYSTEM_RESTOREUP          = 10
SOUND_SYSTEM_RESTOREDOWN        = 11
SOUND_SYSTEM_APPSTART           = 12
SOUND_SYSTEM_FAULT              = 13
SOUND_SYSTEM_APPEND             = 14
SOUND_SYSTEM_MENUCOMMAND        = 15
SOUND_SYSTEM_MENUPOPUP          = 16
CSOUND_SYSTEM                   = 16


# System Alerts (indexChild of system ALERT notification)

ALERT_SYSTEM_INFORMATIONAL      = 1       #// MB_INFORMATION
ALERT_SYSTEM_WARNING            = 2       #// MB_WARNING
ALERT_SYSTEM_ERROR              = 3       #// MB_ERROR
ALERT_SYSTEM_QUERY              = 4       #// MB_QUESTION
ALERT_SYSTEM_CRITICAL           = 5       #// HardSysErrBox
CALERT_SYSTEM                   = 6

GUI_CARETBLINKING = 0x00000001
GUI_INMOVESIZE    = 0x00000002
GUI_INMENUMODE    = 0x00000004
GUI_SYSTEMMENUMODE= 0x00000008
GUI_POPUPMENUMODE = 0x00000010
GUI_16BITTASK     = 0x00000020

STATE_SYSTEM_UNAVAILABLE      = 0x00000001  #// Disabled
STATE_SYSTEM_SELECTED         = 0x00000002
STATE_SYSTEM_FOCUSED          = 0x00000004
STATE_SYSTEM_PRESSED          = 0x00000008
STATE_SYSTEM_CHECKED          = 0x00000010
STATE_SYSTEM_MIXED            = 0x00000020  #// 3-state checkbox or toolbar button
STATE_SYSTEM_INDETERMINATE    =  STATE_SYSTEM_MIXED
STATE_SYSTEM_READONLY         = 0x00000040
STATE_SYSTEM_HOTTRACKED       = 0x00000080
STATE_SYSTEM_DEFAULT          = 0x00000100
STATE_SYSTEM_EXPANDED         = 0x00000200
STATE_SYSTEM_COLLAPSED        = 0x00000400
STATE_SYSTEM_BUSY             = 0x00000800
STATE_SYSTEM_FLOATING         = 0x00001000  #// Children "owned" not "contained" by parent
STATE_SYSTEM_MARQUEED         = 0x00002000
STATE_SYSTEM_ANIMATED         = 0x00004000
STATE_SYSTEM_INVISIBLE        = 0x00008000
STATE_SYSTEM_OFFSCREEN        = 0x00010000
STATE_SYSTEM_SIZEABLE         = 0x00020000
STATE_SYSTEM_MOVEABLE         = 0x00040000
STATE_SYSTEM_SELFVOICING      = 0x00080000
STATE_SYSTEM_FOCUSABLE        = 0x00100000
STATE_SYSTEM_SELECTABLE       = 0x00200000
STATE_SYSTEM_LINKED           = 0x00400000
STATE_SYSTEM_TRAVERSED        = 0x00800000
STATE_SYSTEM_MULTISELECTABLE  = 0x01000000  #// Supports multiple selection
STATE_SYSTEM_EXTSELECTABLE    = 0x02000000  #// Supports extended selection
STATE_SYSTEM_ALERT_LOW        = 0x04000000  #// This information is of low priority
STATE_SYSTEM_ALERT_MEDIUM     = 0x08000000  #// This information is of medium priority
STATE_SYSTEM_ALERT_HIGH       = 0x10000000  #// This information is of high priority
STATE_SYSTEM_PROTECTED        = 0x20000000  #// access to this is restricted
STATE_SYSTEM_VALID            = 0x3FFFFFFF

CCHILDREN_TITLEBAR              = 5
CCHILDREN_SCROLLBAR             = 5


CURSOR_SHOWING   = 0x00000001

WS_ACTIVECAPTION  = 0x0001



# The "real" ancestor window

GA_PARENT       = 1
GA_ROOT         = 2
GA_ROOTOWNER    = 3


# WM_INPUT wParam



# Use this macro to get the input code from wParam.

#GET_RAWINPUT_CODE_WPARAM(wParam)    ((wParam) & 0xff)


# The input is in the regular message flow,
# the app is required to call DefWindowProc
# so that the system can perform clean ups.

RIM_INPUT      =  0


# The input is sink only. The app is expected
# to behave nicely.

RIM_INPUTSINK   = 1



# Type of the raw input

RIM_TYPEMOUSE       = 0
RIM_TYPEKEYBOARD    = 1
RIM_TYPEHID         = 2



# Define the mouse button state indicators.


RI_MOUSE_LEFT_BUTTON_DOWN = 0x0001  #// Left Button changed to down.
RI_MOUSE_LEFT_BUTTON_UP   = 0x0002  #// Left Button changed to up.
RI_MOUSE_RIGHT_BUTTON_DOWN= 0x0004  #// Right Button changed to down.
RI_MOUSE_RIGHT_BUTTON_UP  = 0x0008  #// Right Button changed to up.
RI_MOUSE_MIDDLE_BUTTON_DOWN = 0x0010  #// Middle Button changed to down.
RI_MOUSE_MIDDLE_BUTTON_UP = 0x0020  #// Middle Button changed to up.

RI_MOUSE_BUTTON_1_DOWN      = RI_MOUSE_LEFT_BUTTON_DOWN
RI_MOUSE_BUTTON_1_UP        = RI_MOUSE_LEFT_BUTTON_UP
RI_MOUSE_BUTTON_2_DOWN      = RI_MOUSE_RIGHT_BUTTON_DOWN
RI_MOUSE_BUTTON_2_UP        = RI_MOUSE_RIGHT_BUTTON_UP
RI_MOUSE_BUTTON_3_DOWN      = RI_MOUSE_MIDDLE_BUTTON_DOWN
RI_MOUSE_BUTTON_3_UP        = RI_MOUSE_MIDDLE_BUTTON_UP

RI_MOUSE_BUTTON_4_DOWN    = 0x0040
RI_MOUSE_BUTTON_4_UP      = 0x0080
RI_MOUSE_BUTTON_5_DOWN    = 0x0100
RI_MOUSE_BUTTON_5_UP      = 0x0200


# If usButtonFlags has RI_MOUSE_WHEEL, the wheel delta is stored in usButtonData.
# Take it as a signed value.

RI_MOUSE_WHEEL            = 0x0400


# Define the mouse indicator flags.

MOUSE_MOVE_RELATIVE         = 0
MOUSE_MOVE_ABSOLUTE         = 1
MOUSE_VIRTUAL_DESKTOP  = 0x02  #// the coordinates are mapped to the virtual desktop
MOUSE_ATTRIBUTES_CHANGED = 0x04  #// requery for mouse attributes



# Define the keyboard overrun MakeCode.


KEYBOARD_OVERRUN_MAKE_CODE  = 0xFF


# Define the keyboard input data Flags.

RI_KEY_MAKE             = 0
RI_KEY_BREAK            = 1
RI_KEY_E0               = 2
RI_KEY_E1               = 4
RI_KEY_TERMSRV_SET_LED  = 8
RI_KEY_TERMSRV_SHADOW = 0x10


# Flags for GetRawInputData


RID_INPUT             = 0x10000003
RID_HEADER            = 0x10000005



# Raw Input Device Information

RIDI_PREPARSEDDATA    = 0x20000005
RIDI_DEVICENAME       = 0x20000007  #// the return valus is the character length, not the byte size
RIDI_DEVICEINFO       = 0x2000000b

RIDEV_REMOVE          = 0x00000001
RIDEV_EXCLUDE         = 0x00000010
RIDEV_PAGEONLY        = 0x00000020
RIDEV_NOLEGACY        = 0x00000030
RIDEV_INPUTSINK       = 0x00000100
RIDEV_CAPTUREMOUSE    = 0x00000200  #// effective when mouse nolegacy is specified, otherwise it would be an error
RIDEV_NOHOTKEYS       = 0x00000200  #// effective for keyboard.
RIDEV_APPKEYS         = 0x00000400  #// effective for keyboard.


RIDEV_EXINPUTSINK     = 0x00001000
RIDEV_DEVNOTIFY       = 0x00002000

RIDEV_EXMODEMASK      = 0x000000F0

MAX_STR_BLOCKREASON = 256


