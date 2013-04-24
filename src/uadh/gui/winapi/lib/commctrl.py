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
Created on 31/03/2012

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

'''

from ctypes import Structure, windll, sizeof, c_char_p, c_int, c_wchar_p,\
    c_void_p
from ctypes.wintypes import DWORD, HANDLE, UINT, LPARAM, LPSTR, LPWSTR,\
    HINSTANCE, RECT, HWND, BOOL
from uadh.gui.winapi.lib import winuser
from uadh.gui.winapi.lib.winuser import WM_USER, SC_SIZE, CB_DELETESTRING
from uadh.gui.winapi.lib.auxfuncs import ErrorIfZero

# todos eran (0u - xu)
NM_FIRST                = 0x00000000       # generic to all controls
NM_LAST                 = -99

LVN_FIRST               = -100       # listview
LVN_LAST                = -199

# Property sheet reserved      (0U-200U) -  (0U-299U) - see prsht.h

HDN_FIRST               = -300       # header
HDN_LAST                = -399

TVN_FIRST               = -400       # treeview
TVN_LAST                = -499

TTN_FIRST               = -520       # tooltips
TTN_LAST                = -549

TCN_FIRST               = -550       # tab control
TCN_LAST                = -580

# Shell reserved               (0U-580U) -  (0U-589U)

CDN_FIRST               = -601       # common dialog (new)
CDN_LAST                = -699

TBN_FIRST               = -700       # toolbar
TBN_LAST                = -720

UDN_FIRST               = -721        # updown
UDN_LAST                = -729

DTN_FIRST               = -740       # datetimepick
DTN_LAST                = -745       # DTN_FIRST - 5

MCN_FIRST               = -746       # monthcal
MCN_LAST                = -752       # MCN_FIRST - 6

DTN_FIRST2              = -753       # datetimepick2
DTN_LAST2               = -799

CBEN_FIRST              = -800       # combo box ex
CBEN_LAST               = -830

RBN_FIRST               = -831       # rebar
RBN_LAST                = -859

IPN_FIRST               = -860       # internet address
IPN_LAST                = -879       # internet address

SBN_FIRST               = -880       # status bar
SBN_LAST                = -899

PGN_FIRST               = -900       # Pager Control
PGN_LAST                = -950

WMN_FIRST               = -1000
WMN_LAST                = -1200

BCN_FIRST               = -1250
BCN_LAST                = -1350

#
# Users of this header may define any number of these constants to avoid
# the definitions of each functional group.
#
#    NOTOOLBAR    Customizable bitmap-button toolbar control.
#    NOUPDOWN     Up and Down arrow increment/decrement control.
#    NOSTATUSBAR  Status bar control.
#    NOMENUHELP   APIs to help manage menus, especially with a status bar.
#    NOTRACKBAR   Customizable column-width tracking control.
#    NODRAGLIST   APIs to make a listbox source and sink drag&drop actions.
#    NOPROGRESS   Progress gas gauge.
#    NOHOTKEY     HotKey control
#    NOHEADER     Header bar control.
#    NOIMAGEAPIS  ImageList apis.
#    NOLISTVIEW   ListView control.
#    NOTREEVIEW   TreeView control.
#    NOTABCONTROL Tab control.
#    NOANIMATE    Animate control.
#    NOBUTTON     Button control.
#    NOSTATIC     Static control.
#    NOEDIT       Edit control.
#    NOLISTBOX    Listbox control.
#    NOCOMBOBOX   Combobox control.
#    NOSCROLLBAR  Scrollbar control.
#    NOTASKDIALOG Task Dialog.
#
#=============================================================================


SNDMSG = winuser.SendMessage


InitCommonControls = windll.comctl32.InitCommonControls
'''
WINCOMMCTRLAPI 
void 
WINAPI 
InitCommonControls(void);
'''


class INITCOMMONCONTROLSEX(Structure):
    _fields_ = [ ('dwSize', DWORD),            # size of this structure
                 ('dwICC', DWORD)]             # flags indicating which classes to be initialized
    def __init__(self):
        self.dwSize = sizeof(self)
        self.dwICC = ICC_STANDARD_CLASSES | ICC_WIN95_CLASSES | ICC_TREEVIEW_CLASSES | ICC_TAB_CLASSES
tagINITCOMMONCONTROLSEX = INITCOMMONCONTROLSEX
'''
typedef struct tagINITCOMMONCONTROLSEX {
    DWORD dwSize;             # size of this structure
    DWORD dwICC;              # flags indicating which classes to be initialized
} INITCOMMONCONTROLSEX, *LPINITCOMMONCONTROLSEX;
'''

ICC_LISTVIEW_CLASSES   = 0x00000001 # listview, header
ICC_TREEVIEW_CLASSES   = 0x00000002 # treeview, tooltips
ICC_BAR_CLASSES        = 0x00000004 # toolbar, statusbar, trackbar, tooltips
ICC_TAB_CLASSES        = 0x00000008 # tab, tooltips
ICC_UPDOWN_CLASS       = 0x00000010 # updown
ICC_PROGRESS_CLASS     = 0x00000020 # progress
ICC_HOTKEY_CLASS       = 0x00000040 # hotkey
ICC_ANIMATE_CLASS      = 0x00000080 # animate
ICC_WIN95_CLASSES      = 0x000000FF
ICC_DATE_CLASSES       = 0x00000100 # month picker, date picker, time picker, updown
ICC_USEREX_CLASSES     = 0x00000200 # comboex
ICC_COOL_CLASSES       = 0x00000400 # rebar (coolbar) control
ICC_INTERNET_CLASSES   = 0x00000800
ICC_PAGESCROLLER_CLASS = 0x00001000   # page scroller
ICC_NATIVEFNTCTL_CLASS = 0x00002000   # native font control
ICC_STANDARD_CLASSES   = 0x00004000
ICC_LINK_CLASS         = 0x00008000

InitCommonControlsEx = windll.comctl32.InitCommonControlsEx
'''
WINCOMMCTRLAPI
BOOL
WINAPI
InitCommonControlsEx(__in const INITCOMMONCONTROLSEX *picce);
'''
InitCommonControlsEx.argtypes = [HANDLE]
InitCommonControlsEx.restype = BOOL
#InitCommonControlsEx.restype = ErrorIfZero


ODT_HEADER             = 100
ODT_TAB                = 101
ODT_LISTVIEW           = 102

#====== Ranges for control message IDs =======================================

LVM_FIRST              = 0x1000      # ListView messages
TV_FIRST               = 0x1100      # TreeView messages
HDM_FIRST              = 0x1200      # Header messages
TCM_FIRST              = 0x1300      # Tab control messages
PGM_FIRST              = 0x1400      # Pager control messages
ECM_FIRST              = 0x1500      # Edit control messages
BCM_FIRST              = 0x1600      # Button control messages
CBM_FIRST              = 0x1700      # Combobox control messages
CCM_FIRST              = 0x2000      # Common control shared messages
CCM_LAST               = (CCM_FIRST + 0x200)
CCM_SETBKCOLOR         = (CCM_FIRST + 1) # lParam is bkColor



'''
typedef struct tagCOLORSCHEME {
   DWORD            dwSize;
   COLORREF         clrBtnHighlight;       # highlight color
   COLORREF         clrBtnShadow;          # shadow color
} COLORSCHEME, *LPCOLORSCHEME;
'''

CCM_SETCOLORSCHEME      = (CCM_FIRST + 2) # lParam is color scheme
CCM_GETCOLORSCHEME      = (CCM_FIRST + 3) # fills in COLORSCHEME pointed to by lParam
CCM_GETDROPTARGET       = (CCM_FIRST + 4)
CCM_SETUNICODEFORMAT    = (CCM_FIRST + 5)
CCM_GETUNICODEFORMAT    = (CCM_FIRST + 6)
COMCTL32_VERSION        = 6
CCM_SETVERSION          = (CCM_FIRST + 0x7)
CCM_GETVERSION          = (CCM_FIRST + 0x8)
CCM_SETNOTIFYWINDOW     = (CCM_FIRST + 0x9) # wParam == hwndParent.
CCM_SETWINDOWTHEME      = (CCM_FIRST + 0xb)
CCM_DPISCALE            = (CCM_FIRST + 0xc) # wParam == Awareness
INFOTIPSIZE             = 1024    # for tooltips

    

NM_OUTOFMEMORY          = (NM_FIRST-1)
NM_CLICK                = (NM_FIRST-2)    # uses NMCLICK struct
NM_DBLCLK               = (NM_FIRST-3)
NM_RETURN               = (NM_FIRST-4)
NM_RCLICK               = (NM_FIRST-5)    # uses NMCLICK struct
NM_RDBLCLK              = (NM_FIRST-6)
NM_SETFOCUS             = (NM_FIRST-7)
NM_KILLFOCUS            = (NM_FIRST-8)
NM_CUSTOMDRAW           = (NM_FIRST-12)
NM_HOVER                = (NM_FIRST-13)
NM_NCHITTEST            = (NM_FIRST-14)   # uses NMMOUSE struct
NM_KEYDOWN              = (NM_FIRST-15)   # uses NMKEY struct
NM_RELEASEDCAPTURE      = (NM_FIRST-16)
NM_SETCURSOR            = (NM_FIRST-17)   # uses NMMOUSE struct
NM_CHAR                 = (NM_FIRST-18)   # uses NMCHAR struct
NM_TOOLTIPSCREATED      = (NM_FIRST-19)   # notify of when the tooltips window is create
NM_LDOWN                = (NM_FIRST-20)
NM_RDOWN                = (NM_FIRST-21)
NM_THEMECHANGED         = (NM_FIRST-22)

'''
def CCSIZEOF_STRUCT(structname, member):
    return (((int)((LPBYTE)(&((structname*)0)->member) - ((LPBYTE)((structname*)0)))) + sizeof(((structname*)0)->member))
'''
#define CCSIZEOF_STRUCT(structname, member)  (((int)((LPBYTE)(&((structname*)0)->member) - ((LPBYTE)((structname*)0)))) + sizeof(((structname*)0)->member))

MSGF_COMMCTRL_BEGINDRAG    = 0x4200
MSGF_COMMCTRL_SIZEHEADER   = 0x4201
MSGF_COMMCTRL_DRAGSELECT   = 0x4202
MSGF_COMMCTRL_TOOLBARCUST  = 0x4203



#==================== CUSTOM DRAW ==========================================


# custom draw return flags
# values under 0x00010000 are reserved for global custom draw values.
# above that are for specific controls
CDRF_DODEFAULT         = 0x00000000
CDRF_NEWFONT           = 0x00000002
CDRF_SKIPDEFAULT       = 0x00000004
CDRF_DOERASE           = 0x00000008 # draw the background
CDRF_SKIPPOSTPAINT     = 0x00000100 # don't draw the focus rect
CDRF_NOTIFYPOSTPAINT   = 0x00000010
CDRF_NOTIFYITEMDRAW    = 0x00000020
CDRF_NOTIFYSUBITEMDRAW = 0x00000020  # flags are the same, we can distinguish by context
CDRF_NOTIFYPOSTERASE   = 0x00000040

# drawstage flags
# values under 0x00010000 are reserved for global custom draw values.
# above that are for specific controls
CDDS_PREPAINT          = 0x00000001
CDDS_POSTPAINT         = 0x00000002
CDDS_PREERASE          = 0x00000003
CDDS_POSTERASE         = 0x00000004
# the 0x000010000 bit means it's individual item specific
CDDS_ITEM              = 0x00010000
CDDS_ITEMPREPAINT      = (CDDS_ITEM | CDDS_PREPAINT)
CDDS_ITEMPOSTPAINT     = (CDDS_ITEM | CDDS_POSTPAINT)
CDDS_ITEMPREERASE      = (CDDS_ITEM | CDDS_PREERASE)
CDDS_ITEMPOSTERASE     = (CDDS_ITEM | CDDS_POSTERASE)
CDDS_SUBITEM           = 0x00020000
# itemState flags
CDIS_SELECTED          = 0x0001
CDIS_GRAYED            = 0x0002
CDIS_DISABLED          = 0x0004
CDIS_CHECKED           = 0x0008
CDIS_FOCUS             = 0x0010
CDIS_DEFAULT           = 0x0020
CDIS_HOT               = 0x0040
CDIS_MARKED            = 0x0080
CDIS_INDETERMINATE     = 0x0100
CDIS_SHOWKEYBOARDCUES  = 0x0200


CLR_NONE               = 0xFFFFFFFFL
CLR_DEFAULT            = 0xFF000000L


ILC_MASK               = 0x00000001
ILC_COLOR              = 0x00000000
ILC_COLORDDB           = 0x000000FE
ILC_COLOR4             = 0x00000004
ILC_COLOR8             = 0x00000008
ILC_COLOR16            = 0x00000010
ILC_COLOR24            = 0x00000018
ILC_COLOR32            = 0x00000020
ILC_PALETTE            = 0x00000800      # (not implemented)
ILC_MIRROR             = 0x00002000      # Mirror the icons contained, if the process is mirrored
ILC_PERITEMMIRROR      = 0x00008000      # Causes the mirroring code to mirror each item when inserting a set of images, verses the whole strip

ILD_NORMAL             = 0x00000000
ILD_TRANSPARENT        = 0x00000001
ILD_MASK               = 0x00000010
ILD_IMAGE              = 0x00000020
ILD_ROP                = 0x00000040
ILD_BLEND25            = 0x00000002
ILD_BLEND50            = 0x00000004
ILD_OVERLAYMASK        = 0x00000F00

def INDEXTOOVERLAYMASK(i):
    return (i << 8)

ILD_PRESERVEALPHA      = 0x00001000  # This preserves the alpha channel in dest
ILD_SCALE              = 0x00002000  # Causes the image to be scaled to cx, cy instead of clipped
ILD_DPISCALE           = 0x00004000


ILD_SELECTED           = ILD_BLEND50
ILD_FOCUS              = ILD_BLEND25
ILD_BLEND              = ILD_BLEND50
CLR_HILIGHT            = CLR_DEFAULT

ILS_NORMAL             = 0x00000000
ILS_GLOW               = 0x00000001
ILS_SHADOW             = 0x00000002
ILS_SATURATE           = 0x00000004
ILS_ALPHA              = 0x00000008


ILCF_MOVE   = (0x00000000)
ILCF_SWAP   = (0x00000001)


# begin_r_commctrl
HDS_HORZ               = 0x0000
HDS_BUTTONS            = 0x0002
HDS_HOTTRACK           = 0x0004
HDS_HIDDEN             = 0x0008
HDS_DRAGDROP           = 0x0040
HDS_FULLDRAG           = 0x0080
HDS_FILTERBAR          = 0x0100
HDS_FLAT               = 0x0200
# end_r_commctrl


HDFT_ISSTRING      = 0x0000      # HD_ITEM.pvFilter points to a HD_TEXTFILTER
HDFT_ISNUMBER      = 0x0001      # HD_ITEM.pvFilter points to a INT
HDFT_ISDATE        = 0x0002      # HD_ITEM.pvFilter points to a DWORD (dos date)

HDFT_HASNOVALUE    = 0x8000      # clear the filter, by setting this bit



HDI_WIDTH              = 0x0001
HDI_HEIGHT             = HDI_WIDTH
HDI_TEXT               = 0x0002
HDI_FORMAT             = 0x0004
HDI_LPARAM             = 0x0008
HDI_BITMAP             = 0x0010
HDI_IMAGE              = 0x0020
HDI_DI_SETITEM         = 0x0040
HDI_ORDER              = 0x0080
HDI_FILTER             = 0x0100


# HDF_ flags are shared with the listview control (LVCFMT_ flags)

HDF_LEFT               = 0x0000 # Same as LVCFMT_LEFT
HDF_RIGHT              = 0x0001 # Same as LVCFMT_RIGHT
HDF_CENTER             = 0x0002 # Same as LVCFMT_CENTER
HDF_JUSTIFYMASK        = 0x0003 # Same as LVCFMT_JUSTIFYMASK
HDF_RTLREADING         = 0x0004 # Same as LVCFMT_LEFT

HDF_BITMAP             = 0x2000
HDF_STRING             = 0x4000
HDF_OWNERDRAW          = 0x8000 # Same as LVCFMT_COL_HAS_IMAGES
HDF_IMAGE              = 0x0800 # Same as LVCFMT_IMAGE
HDF_BITMAP_ON_RIGHT    = 0x1000 # Same as LVCFMT_BITMAP_ON_RIGHT
HDF_SORTUP             = 0x0400
HDF_SORTDOWN           = 0x0200


HDM_GETITEMCOUNT        = (HDM_FIRST + 0)

HDM_INSERTITEMA         = (HDM_FIRST + 1)
HDM_INSERTITEMW         = (HDM_FIRST + 10)
HDM_INSERTITEM          = HDM_INSERTITEMW
HDM_DELETEITEM          = (HDM_FIRST + 2)
HDM_GETITEMA            = (HDM_FIRST + 3)
HDM_GETITEMW            = (HDM_FIRST + 11)
HDM_GETITEM             = HDM_GETITEMW
HDM_SETITEMA            = (HDM_FIRST + 4)
HDM_SETITEMW            = (HDM_FIRST + 12)
HDM_SETITEM             = HDM_SETITEMW


HDM_LAYOUT              = (HDM_FIRST + 5)

HHT_NOWHERE            = 0x0001
HHT_ONHEADER           = 0x0002
HHT_ONDIVIDER          = 0x0004
HHT_ONDIVOPEN          = 0x0008
HHT_ONFILTER           = 0x0010
HHT_ONFILTERBUTTON     = 0x0020
HHT_ABOVE              = 0x0100
HHT_BELOW              = 0x0200
HHT_TORIGHT            = 0x0400
HHT_TOLEFT             = 0x0800

HDSIL_NORMAL           = 0
HDSIL_STATE            = 1

HDM_HITTEST             = (HDM_FIRST + 6)

HDM_GETITEMRECT         = (HDM_FIRST + 7)

HDM_SETIMAGELIST        = (HDM_FIRST + 8)

HDM_GETIMAGELIST        = (HDM_FIRST + 9)

HDM_ORDERTOINDEX        = (HDM_FIRST + 15)

HDM_CREATEDRAGIMAGE     = (HDM_FIRST + 16)  # wparam = which item (by index)

HDM_GETORDERARRAY       = (HDM_FIRST + 17)

HDM_SETORDERARRAY       = (HDM_FIRST + 18)


# lparam = int array of size HDM_GETITEMCOUNT
# the array specifies the order that all items should be displayed.
# e.g.  { 2, 0, 1}
# says the index 2 item should be shown in the 0ths position
#      index 0 should be shown in the 1st position
#      index 1 should be shown in the 2nd position


HDM_SETHOTDIVIDER            = (HDM_FIRST + 19)


HDM_SETBITMAPMARGIN          = (HDM_FIRST + 20)

HDM_GETBITMAPMARGIN          = (HDM_FIRST + 21)

HDM_SETUNICODEFORMAT         = CCM_SETUNICODEFORMAT

HDM_GETUNICODEFORMAT         = CCM_GETUNICODEFORMAT

HDM_SETFILTERCHANGETIMEOUT   = (HDM_FIRST+22)

HDM_EDITFILTER               = (HDM_FIRST+23)

# Clear filter takes -1 as a column value to indicate that all
# the filter should be cleared.  When this happens you will
# only receive a single filter changed notification.

HDM_CLEARFILTER              = (HDM_FIRST+24)


HDN_ITEMCHANGINGA       = (HDN_FIRST-0)
HDN_ITEMCHANGINGW       = (HDN_FIRST-20)
HDN_ITEMCHANGEDA        = (HDN_FIRST-1)
HDN_ITEMCHANGEDW        = (HDN_FIRST-21)
HDN_ITEMCLICKA          = (HDN_FIRST-2)
HDN_ITEMCLICKW          = (HDN_FIRST-22)
HDN_ITEMDBLCLICKA       = (HDN_FIRST-3)
HDN_ITEMDBLCLICKW       = (HDN_FIRST-23)
HDN_DIVIDERDBLCLICKA    = (HDN_FIRST-5)
HDN_DIVIDERDBLCLICKW    = (HDN_FIRST-25)
HDN_BEGINTRACKA         = (HDN_FIRST-6)
HDN_BEGINTRACKW         = (HDN_FIRST-26)
HDN_ENDTRACKA           = (HDN_FIRST-7)
HDN_ENDTRACKW           = (HDN_FIRST-27)
HDN_TRACKA              = (HDN_FIRST-8)
HDN_TRACKW              = (HDN_FIRST-28)
HDN_GETDISPINFOA        = (HDN_FIRST-9)
HDN_GETDISPINFOW        = (HDN_FIRST-29)
HDN_BEGINDRAG           = (HDN_FIRST-10)
HDN_ENDDRAG             = (HDN_FIRST-11)
HDN_FILTERCHANGE        = (HDN_FIRST-12)
HDN_FILTERBTNCLICK      = (HDN_FIRST-13)
HDN_ITEMCHANGING        =  HDN_ITEMCHANGINGW
HDN_ITEMCHANGED         =  HDN_ITEMCHANGEDW
HDN_ITEMCLICK           =  HDN_ITEMCLICKW
HDN_ITEMDBLCLICK        =  HDN_ITEMDBLCLICKW
HDN_DIVIDERDBLCLICK     =  HDN_DIVIDERDBLCLICKW
HDN_BEGINTRACK          =  HDN_BEGINTRACKW
HDN_ENDTRACK            =  HDN_ENDTRACKW
HDN_TRACK               =  HDN_TRACKW
HDN_GETDISPINFO         =  HDN_GETDISPINFOW


TOOLBARCLASSNAMEW       = "ToolbarWindow32"
TOOLBARCLASSNAMEA       = TOOLBARCLASSNAMEW
TOOLBARCLASSNAME        = TOOLBARCLASSNAMEW


CMB_MASKED             = 0x02
TBSTATE_CHECKED        = 0x01
TBSTATE_PRESSED        = 0x02
TBSTATE_ENABLED        = 0x04
TBSTATE_HIDDEN         = 0x08
TBSTATE_INDETERMINATE  = 0x10
TBSTATE_WRAP           = 0x20
TBSTATE_ELLIPSES       = 0x40
TBSTATE_MARKED         = 0x80


# begin_r_commctrl

TBSTYLE_BUTTON          = 0x0000  # obsolete; use BTNS_BUTTON instead
TBSTYLE_SEP             = 0x0001  # obsolete; use BTNS_SEP instead
TBSTYLE_CHECK           = 0x0002  # obsolete; use BTNS_CHECK instead
TBSTYLE_GROUP           = 0x0004  # obsolete; use BTNS_GROUP instead
TBSTYLE_CHECKGROUP      = (TBSTYLE_GROUP | TBSTYLE_CHECK)     # obsolete; use BTNS_CHECKGROUP instead
TBSTYLE_DROPDOWN        = 0x0008  # obsolete; use BTNS_DROPDOWN instead
TBSTYLE_AUTOSIZE        = 0x0010  # obsolete; use BTNS_AUTOSIZE instead
TBSTYLE_NOPREFIX        = 0x0020  # obsolete; use BTNS_NOPREFIX instead
TBSTYLE_TOOLTIPS        = 0x0100
TBSTYLE_WRAPABLE        = 0x0200
TBSTYLE_ALTDRAG         = 0x0400
TBSTYLE_FLAT            = 0x0800
TBSTYLE_LIST            = 0x1000
TBSTYLE_CUSTOMERASE     = 0x2000
TBSTYLE_REGISTERDROP    = 0x4000
TBSTYLE_TRANSPARENT     = 0x8000
# end_r_commctrl
TBSTYLE_EX_DRAWDDARROWS = 0x00000001

# begin_r_commctrl
BTNS_BUTTON         = TBSTYLE_BUTTON      # 0x0000
BTNS_SEP            = TBSTYLE_SEP         # 0x0001
BTNS_CHECK          = TBSTYLE_CHECK       # 0x0002
BTNS_GROUP          = TBSTYLE_GROUP       # 0x0004
BTNS_CHECKGROUP     = TBSTYLE_CHECKGROUP  # (TBSTYLE_GROUP | TBSTYLE_CHECK)
BTNS_DROPDOWN       = TBSTYLE_DROPDOWN    # 0x0008
BTNS_AUTOSIZE       = TBSTYLE_AUTOSIZE    # 0x0010; automatically calculate the cx of the button
BTNS_NOPREFIX       = TBSTYLE_NOPREFIX    # 0x0020; this button should not have accel prefix
BTNS_SHOWTEXT       = 0x0040              # ignored unless TBSTYLE_EX_MIXEDBUTTONS is set
BTNS_WHOLEDROPDOWN  = 0x0080          # draw drop-down arrow, but without split arrow section

# end_r_commctrl

TBSTYLE_EX_MIXEDBUTTONS            = 0x00000008
TBSTYLE_EX_HIDECLIPPEDBUTTONS      = 0x00000010  # don't show partially obscured buttons
TBSTYLE_EX_DOUBLEBUFFER            = 0x00000080 # Double Buffer the toolbar


# Toolbar custom draw return flags
TBCDRF_NOEDGES             = 0x00010000  # Don't draw button edges
TBCDRF_HILITEHOTTRACK      = 0x00020000  # Use color of the button bk when hottracked
TBCDRF_NOOFFSET            = 0x00040000  # Don't offset button if pressed
TBCDRF_NOMARK              = 0x00080000  # Don't draw default highlight of image/text for TBSTATE_MARKED
TBCDRF_NOETCHEDEFFECT      = 0x00100000  # Don't draw etched effect for disabled items
TBCDRF_BLENDICON           = 0x00200000  # Use ILD_BLEND50 on the icon image
TBCDRF_NOBACKGROUND        = 0x00400000  # Use ILD_BLEND50 on the icon image

TB_ENABLEBUTTON            = (WM_USER + 1)
TB_CHECKBUTTON             = (WM_USER + 2)
TB_PRESSBUTTON             = (WM_USER + 3)
TB_HIDEBUTTON              = (WM_USER + 4)
TB_INDETERMINATE           = (WM_USER + 5)
TB_MARKBUTTON              = (WM_USER + 6)
TB_ISBUTTONENABLED         = (WM_USER + 9)
TB_ISBUTTONCHECKED         = (WM_USER + 10)
TB_ISBUTTONPRESSED         = (WM_USER + 11)
TB_ISBUTTONHIDDEN          = (WM_USER + 12)
TB_ISBUTTONINDETERMINATE   = (WM_USER + 13)
TB_ISBUTTONHIGHLIGHTED     = (WM_USER + 14)
TB_SETSTATE                = (WM_USER + 17)
TB_GETSTATE                = (WM_USER + 18)
TB_ADDBITMAP               = (WM_USER + 19)

HINST_COMMCTRL             = HINSTANCE(-1)
IDB_STD_SMALL_COLOR        = 0
IDB_STD_LARGE_COLOR        = 1
IDB_VIEW_SMALL_COLOR       = 4
IDB_VIEW_LARGE_COLOR       = 5
IDB_HIST_SMALL_COLOR       = 8
IDB_HIST_LARGE_COLOR       = 9


# icon indexes for standard bitmap

STD_CUT                 = 0
STD_COPY                = 1
STD_PASTE               = 2
STD_UNDO                = 3
STD_REDOW               = 4
STD_DELETE              = 5
STD_FILENEW             = 6
STD_FILEOPEN            = 7
STD_FILESAVE            = 8
STD_PRINTPRE            = 9
STD_PROPERTIES          = 10
STD_HELP                = 11
STD_FIND                = 12
STD_REPLACE             = 13
STD_PRINT               = 14

# icon indexes for standard view bitmap

VIEW_LARGEICONS         = 0
VIEW_SMALLICONS         = 1
VIEW_LIST               = 2
VIEW_DETAILS            = 3
VIEW_SORTNAME           = 4
VIEW_SORTSIZE           = 5
VIEW_SORTDATE           = 6
VIEW_SORTTYPE           = 7
VIEW_PARENTFOLDER       = 8
VIEW_NETCONNECT         = 9
VIEW_NETDISCONNECT      = 10
VIEW_NEWFOLDER          = 11
VIEW_VIEWMENU           = 12


HIST_BACK               = 0
HIST_FORWARD            = 1
HIST_FAVORITES          = 2
HIST_ADDTOFAVORITES     = 3
HIST_VIEWTREE           = 4


TB_ADDBUTTONSA          = (WM_USER + 20)
TB_INSERTBUTTONA        = (WM_USER + 21)
TB_ADDBUTTONS           = (WM_USER + 20)
TB_INSERTBUTTON         = (WM_USER + 21)
TB_DELETEBUTTON         = (WM_USER + 22)
TB_GETBUTTON            = (WM_USER + 23)
TB_BUTTONCOUNT          = (WM_USER + 24)
TB_COMMANDTOINDEX       = (WM_USER + 25)



TB_SAVERESTOREA         = (WM_USER + 26)
TB_SAVERESTOREW         = (WM_USER + 76)
TB_CUSTOMIZE            = (WM_USER + 27)
TB_ADDSTRINGA           = (WM_USER + 28)
TB_ADDSTRINGW           = (WM_USER + 77)
TB_GETITEMRECT          = (WM_USER + 29)
TB_BUTTONSTRUCTSIZE     = (WM_USER + 30)
TB_SETBUTTONSIZE        = (WM_USER + 31)
TB_SETBITMAPSIZE        = (WM_USER + 32)
TB_AUTOSIZE             = (WM_USER + 33)
TB_GETTOOLTIPS          = (WM_USER + 35)
TB_SETTOOLTIPS          = (WM_USER + 36)
TB_SETPARENT            = (WM_USER + 37)
TB_SETROWS              = (WM_USER + 39)
TB_GETROWS              = (WM_USER + 40)
TB_SETCMDID             = (WM_USER + 42)
TB_CHANGEBITMAP         = (WM_USER + 43)
TB_GETBITMAP            = (WM_USER + 44)
TB_GETBUTTONTEXTA       = (WM_USER + 45)
TB_GETBUTTONTEXTW       = (WM_USER + 75)
TB_REPLACEBITMAP        = (WM_USER + 46)
TB_SETINDENT            = (WM_USER + 47)
TB_SETIMAGELIST         = (WM_USER + 48)
TB_GETIMAGELIST         = (WM_USER + 49)
TB_LOADIMAGES           = (WM_USER + 50)
TB_GETRECT              = (WM_USER + 51) # wParam is the Cmd instead of index
TB_SETHOTIMAGELIST      = (WM_USER + 52)
TB_GETHOTIMAGELIST      = (WM_USER + 53)
TB_SETDISABLEDIMAGELIST = (WM_USER + 54)
TB_GETDISABLEDIMAGELIST = (WM_USER + 55)
TB_SETSTYLE             = (WM_USER + 56)
TB_GETSTYLE             = (WM_USER + 57)
TB_GETBUTTONSIZE        = (WM_USER + 58)
TB_SETBUTTONWIDTH       = (WM_USER + 59)
TB_SETMAXTEXTROWS       = (WM_USER + 60)
TB_GETTEXTROWS          = (WM_USER + 61)
TB_GETBUTTONTEXT        = TB_GETBUTTONTEXTW
TB_SAVERESTORE          = TB_SAVERESTOREW
TB_ADDSTRING            = TB_ADDSTRINGW
TB_GETOBJECT            = (WM_USER + 62)  # wParam == IID, lParam void **ppv
TB_GETHOTITEM           = (WM_USER + 71)
TB_SETHOTITEM           = (WM_USER + 72)  # wParam == iHotItem
TB_SETANCHORHIGHLIGHT   = (WM_USER + 73)  # wParam == TRUE/FALSE
TB_GETANCHORHIGHLIGHT   = (WM_USER + 74)
TB_MAPACCELERATORA      = (WM_USER + 78)  # wParam == ch, lParam int * pidBtn


TBIMHT_AFTER            = 0x00000001 # TRUE = insert After iButton, otherwise before
TBIMHT_BACKGROUND       = 0x00000002 # TRUE iff missed buttons completely

TB_GETINSERTMARK        = (WM_USER + 79)  # lParam == LPTBINSERTMARK
TB_SETINSERTMARK        = (WM_USER + 80)  # lParam == LPTBINSERTMARK
TB_INSERTMARKHITTEST    = (WM_USER + 81)  # wParam == LPPOINT lParam == LPTBINSERTMARK
TB_MOVEBUTTON           = (WM_USER + 82)
TB_GETMAXSIZE           = (WM_USER + 83)  # lParam == LPSIZE
TB_SETEXTENDEDSTYLE     = (WM_USER + 84)  # For TBSTYLE_EX_*
TB_GETEXTENDEDSTYLE     = (WM_USER + 85)  # For TBSTYLE_EX_*
TB_GETPADDING           = (WM_USER + 86)
TB_SETPADDING           = (WM_USER + 87)
TB_SETINSERTMARKCOLOR   = (WM_USER + 88)
TB_GETINSERTMARKCOLOR   = (WM_USER + 89)


TB_SETCOLORSCHEME       = CCM_SETCOLORSCHEME  # lParam is color scheme
TB_GETCOLORSCHEME       = CCM_GETCOLORSCHEME      # fills in COLORSCHEME pointed to by lParam

TB_SETUNICODEFORMAT     = CCM_SETUNICODEFORMAT
TB_GETUNICODEFORMAT     = CCM_GETUNICODEFORMAT

TB_MAPACCELERATORW      = (WM_USER + 90)  # wParam == ch, lParam int * pidBtn
TB_MAPACCELERATOR       = TB_MAPACCELERATORW


TBBF_LARGE             = 0x0001

TB_GETBITMAPFLAGS       = (WM_USER + 41)

TBIF_IMAGE             = 0x00000001
TBIF_TEXT              = 0x00000002
TBIF_STATE             = 0x00000004
TBIF_STYLE             = 0x00000008
TBIF_LPARAM            = 0x00000010
TBIF_COMMAND           = 0x00000020
TBIF_SIZE              = 0x00000040
TBIF_BYINDEX           = 0x80000000 # this specifies that the wparam in Get/SetButtonInfo is an index, not id


# BUTTONINFO APIs do NOT support the string pool.
TB_GETBUTTONINFOW        = (WM_USER + 63)
TB_SETBUTTONINFOW        = (WM_USER + 64)
TB_GETBUTTONINFOA        = (WM_USER + 65)
TB_SETBUTTONINFOA        = (WM_USER + 66)
TB_GETBUTTONINFO         = TB_GETBUTTONINFOW
TB_SETBUTTONINFO         = TB_SETBUTTONINFOW
TB_INSERTBUTTONW         = (WM_USER + 67)
TB_ADDBUTTONSW           = (WM_USER + 68)

TB_HITTEST               = (WM_USER + 69)

# New post Win95/NT4 for InsertButton and AddButton.  if iString member
# is a pointer to a string, it will be handled as a string like listview
# (although LPSTR_TEXTCALLBACK is not supported).
TB_INSERTBUTTON         = TB_INSERTBUTTONW
TB_ADDBUTTONS           = TB_ADDBUTTONSW


TB_SETDRAWTEXTFLAGS     = (WM_USER + 70)  # wParam == mask lParam == bit values


TB_GETSTRINGW           = (WM_USER + 91)
TB_GETSTRINGA           = (WM_USER + 92)
TB_GETSTRING            = TB_GETSTRINGW

TB_SETHOTITEM2          = (WM_USER + 94)  # wParam == iHotItem,  lParam = dwFlags
TB_SETLISTGAP           = (WM_USER + 96)
TB_GETIMAGELISTCOUNT    = (WM_USER + 98)
TB_GETIDEALSIZE         = (WM_USER + 99)  # wParam == fHeight, lParam = psize
# before using WM_USER + 103, recycle old space above = (WM_USER + 97)



TBMF_PAD               = 0x00000001
TBMF_BARPAD            = 0x00000002
TBMF_BUTTONSPACING     = 0x00000004

TB_GETMETRICS           = (WM_USER + 101)
TB_SETMETRICS           = (WM_USER + 102)

TB_SETWINDOWTHEME       = CCM_SETWINDOWTHEME

TBN_GETBUTTONINFOA      = (TBN_FIRST-0)
TBN_BEGINDRAG           = (TBN_FIRST-1)
TBN_ENDDRAG             = (TBN_FIRST-2)
TBN_BEGINADJUST         = (TBN_FIRST-3)
TBN_ENDADJUST           = (TBN_FIRST-4)
TBN_RESET               = (TBN_FIRST-5)
TBN_QUERYINSERT         = (TBN_FIRST-6)
TBN_QUERYDELETE         = (TBN_FIRST-7)
TBN_TOOLBARCHANGE       = (TBN_FIRST-8)
TBN_CUSTHELP            = (TBN_FIRST-9)
TBN_DROPDOWN            = (TBN_FIRST - 10)
TBN_GETOBJECT           = (TBN_FIRST - 12)

# Hot item change flags
HICF_OTHER           = 0x00000000
HICF_MOUSE           = 0x00000001          # Triggered by mouse
HICF_ARROWKEYS       = 0x00000002          # Triggered by arrow keys
HICF_ACCELERATOR     = 0x00000004          # Triggered by accelerator
HICF_DUPACCEL        = 0x00000008          # This accelerator is not unique
HICF_ENTERING        = 0x00000010          # idOld is invalid
HICF_LEAVING         = 0x00000020          # idNew is invalid
HICF_RESELECT        = 0x00000040          # hot item reselected
HICF_LMOUSE          = 0x00000080          # left mouse button selected
HICF_TOGGLEDROPDOWN  = 0x00000100          # Toggle button's dropdown state


TBN_HOTITEMCHANGE       = (TBN_FIRST - 13)
TBN_DRAGOUT             = (TBN_FIRST - 14) # this is sent when the user clicks down on a button then drags off the button
TBN_DELETINGBUTTON      = (TBN_FIRST - 15) # uses TBNOTIFY
TBN_GETDISPINFOA        = (TBN_FIRST - 16) # This is sent when the  toolbar needs  some display information
TBN_GETDISPINFOW        = (TBN_FIRST - 17) # This is sent when the  toolbar needs  some display information
TBN_GETINFOTIPA         = (TBN_FIRST - 18)
TBN_GETINFOTIPW         = (TBN_FIRST - 19)
TBN_GETBUTTONINFOW      = (TBN_FIRST - 20)
TBN_RESTORE             = (TBN_FIRST - 21)
TBN_SAVE                = (TBN_FIRST - 22)
TBN_INITCUSTOMIZE       = (TBN_FIRST - 23)
TBNRF_HIDEHELP          = 0x00000001
TBNRF_ENDCUSTOMIZE      = 0x00000002
TBN_WRAPHOTITEM         = (TBN_FIRST - 24)
TBN_DUPACCELERATOR      = (TBN_FIRST - 25)
TBN_WRAPACCELERATOR     = (TBN_FIRST - 26)
TBN_DRAGOVER            = (TBN_FIRST - 27)
TBN_MAPACCELERATOR      = (TBN_FIRST - 28)


TBNF_IMAGE             = 0x00000001
TBNF_TEXT              = 0x00000002
TBNF_DI_SETITEM        = 0x10000000

# Return codes for TBN_DROPDOWN
TBDDRET_DEFAULT         = 0
TBDDRET_NODEFAULT       = 1
TBDDRET_TREATPRESSED    = 2       # Treat as a standard press button



#====== REBAR CONTROL ========================================================


REBARCLASSNAMEW          = "ReBarWindow32"
REBARCLASSNAMEA          = REBARCLASSNAMEW
REBARCLASSNAME           = REBARCLASSNAMEW

RBIM_IMAGELIST  = 0x00000001

# begin_r_commctrl

RBS_TOOLTIPS                 = 0x00000100
RBS_VARHEIGHT                = 0x00000200
RBS_BANDBORDERS              = 0x00000400
RBS_FIXEDORDER               = 0x00000800
RBS_REGISTERDROP             = 0x00001000
RBS_AUTOSIZE                 = 0x00002000
RBS_VERTICALGRIPPER          = 0x00004000  # this always has the vertical gripper (default for horizontal mode)
RBS_DBLCLKTOGGLE             = 0x00008000
# end_r_commctrl

RBBS_BREAK            = 0x00000001  # break to new line
RBBS_FIXEDSIZE        = 0x00000002  # band can't be sized
RBBS_CHILDEDGE        = 0x00000004  # edge around top & bottom of child window
RBBS_HIDDEN           = 0x00000008  # don't show
RBBS_NOVERT           = 0x00000010  # don't show when vertical
RBBS_FIXEDBMP         = 0x00000020  # bitmap doesn't move during band resize
RBBS_VARIABLEHEIGHT   = 0x00000040  # allow autosizing of this child vertically
RBBS_GRIPPERALWAYS    = 0x00000080  # always show the gripper
RBBS_NOGRIPPER        = 0x00000100  # never show the gripper
RBBS_USECHEVRON       = 0x00000200  # display drop-down button for this band if it's sized smaller than ideal width
RBBS_HIDETITLE        = 0x00000400  # keep band title hidden
RBBS_TOPALIGN         = 0x00000800  # keep band in top row


RBBIM_STYLE        = 0x00000001
RBBIM_COLORS       = 0x00000002
RBBIM_TEXT         = 0x00000004
RBBIM_IMAGE        = 0x00000008
RBBIM_CHILD        = 0x00000010
RBBIM_CHILDSIZE    = 0x00000020
RBBIM_SIZE         = 0x00000040
RBBIM_BACKGROUND   = 0x00000080
RBBIM_ID           = 0x00000100
RBBIM_IDEALSIZE    = 0x00000200
RBBIM_LPARAM       = 0x00000400
RBBIM_HEADERSIZE   = 0x00000800  # control the size of the header


RB_INSERTBANDA        = (WM_USER +  1)
RB_DELETEBAND         = (WM_USER +  2)
RB_GETBARINFO         = (WM_USER +  3)
RB_SETBARINFO         = (WM_USER +  4)
RB_GETBANDINFO        = (WM_USER +  5)
RB_SETBANDINFOA       = (WM_USER +  6)
RB_SETPARENT          = (WM_USER +  7)
RB_HITTEST            = (WM_USER +  8)
RB_GETRECT            = (WM_USER +  9)
RB_INSERTBANDW        = (WM_USER +  10)
RB_SETBANDINFOW       = (WM_USER +  11)
RB_GETBANDCOUNT       = (WM_USER +  12)
RB_GETROWCOUNT        = (WM_USER +  13)
RB_GETROWHEIGHT       = (WM_USER +  14)
RB_IDTOINDEX          = (WM_USER +  16) # wParam == id
RB_GETTOOLTIPS        = (WM_USER +  17)
RB_SETTOOLTIPS        = (WM_USER +  18)
RB_SETBKCOLOR         = (WM_USER +  19) # sets the default BK color
RB_GETBKCOLOR         = (WM_USER +  20) # defaults to CLR_NONE
RB_SETTEXTCOLOR       = (WM_USER +  21)
RB_GETTEXTCOLOR       = (WM_USER +  22) # defaults to 0x00000000
RBSTR_CHANGERECT      = 0x0001   # flags for RB_SIZETORECT
RB_SIZETORECT         = (WM_USER +  23) # resize the rebar/break bands and such to this rect (lparam)
RB_SETCOLORSCHEME     = CCM_SETCOLORSCHEME  # lParam is color scheme
RB_GETCOLORSCHEME     = CCM_GETCOLORSCHEME  # fills in COLORSCHEME pointed to by lParam

RB_INSERTBAND    = RB_INSERTBANDW
RB_SETBANDINFO   = RB_SETBANDINFOW

# for manual drag control
# lparam == cursor pos
        # -1 means do it yourself.
        # -2 means use what you had saved before
RB_BEGINDRAG         = (WM_USER + 24)
RB_ENDDRAG           = (WM_USER + 25)
RB_DRAGMOVE          = (WM_USER + 26)
RB_GETBARHEIGHT      = (WM_USER + 27)
RB_GETBANDINFOW      = (WM_USER + 28)
RB_GETBANDINFOA      = (WM_USER + 29)
RB_GETBANDINFO       = RB_GETBANDINFOW


RB_MINIMIZEBAND      = (WM_USER + 30)
RB_MAXIMIZEBAND      = (WM_USER + 31)

RB_GETDROPTARGET     = (CCM_GETDROPTARGET)

RB_GETBANDBORDERS    = (WM_USER + 34)  # returns in lparam = lprc the amount of edges added to band wparam

RB_SHOWBAND          = (WM_USER + 35)      # show/hide band
RB_SETPALETTE        = (WM_USER + 37)
RB_GETPALETTE        = (WM_USER + 38)
RB_MOVEBAND          = (WM_USER + 39)

RB_SETUNICODEFORMAT     = CCM_SETUNICODEFORMAT
RB_GETUNICODEFORMAT     = CCM_GETUNICODEFORMAT


RB_GETBANDMARGINS       = (WM_USER + 40)
RB_SETWINDOWTHEME       = CCM_SETWINDOWTHEME

RB_PUSHCHEVRON      = (WM_USER + 43)

RBN_HEIGHTCHANGE    = (RBN_FIRST - 0)
RBN_GETOBJECT       = (RBN_FIRST - 1)
RBN_LAYOUTCHANGED   = (RBN_FIRST - 2)
RBN_AUTOSIZE        = (RBN_FIRST - 3)
RBN_BEGINDRAG       = (RBN_FIRST - 4)
RBN_ENDDRAG         = (RBN_FIRST - 5)
RBN_DELETINGBAND    = (RBN_FIRST - 6)     # Uses NMREBAR
RBN_DELETEDBAND     = (RBN_FIRST - 7)     # Uses NMREBAR
RBN_CHILDSIZE       = (RBN_FIRST - 8)
RBN_CHEVRONPUSHED   = (RBN_FIRST - 10)


RBN_MINMAX          = (RBN_FIRST - 21)


RBN_AUTOBREAK       = (RBN_FIRST - 22)


# Mask flags for NMREBAR
RBNM_ID        = 0x00000001
RBNM_STYLE     = 0x00000002
RBNM_LPARAM    = 0x00000004

RBAB_AUTOSIZE  = 0x0001   # These are not flags and are all mutually exclusive
RBAB_ADDBAND   = 0x0002



RBHT_NOWHERE   = 0x0001
RBHT_CAPTION   = 0x0002
RBHT_CLIENT    = 0x0003
RBHT_GRABBER   = 0x0004
RBHT_CHEVRON   = 0x0008


#====== TOOLTIPS CONTROL =====================================================

TOOLTIPS_CLASSW          = "tooltips_class32"
TOOLTIPS_CLASSA          = TOOLTIPS_CLASSW

#ifdef UNICODE
TOOLTIPS_CLASS           = TOOLTIPS_CLASSW

#define TTTOOLINFOA_V1_SIZE CCSIZEOF_STRUCT(TTTOOLINFOA, lpszText)
#define TTTOOLINFOW_V1_SIZE CCSIZEOF_STRUCT(TTTOOLINFOW, lpszText)
TTTOOLINFOA_V2_SIZE = 44
#define TTTOOLINFOW_V2_SIZE CCSIZEOF_STRUCT(TTTOOLINFOW, lParam)
#define TTTOOLINFOA_V3_SIZE CCSIZEOF_STRUCT(TTTOOLINFOA, lpReserved)
#define TTTOOLINFOW_V3_SIZE CCSIZEOF_STRUCT(TTTOOLINFOW, lpReserved)

class TOOLINFO(Structure):
    _fields_ = [('cbSize', UINT),
                ('uFlags', UINT),
                ('hwnd', HWND),
                ('uId', c_int),
                ('rect', RECT),
                ('hinst', HINSTANCE),
                ('lpszText', LPWSTR),
                ('lParam', LPARAM),
                ('lpReserved', c_void_p)]

    def __init__(self):
        self.cbSize = 48#sizeof(TOOLINFO)
        self.uFlags = TTF_CENTERTIP

'''
typedef struct tagTOOLINFOA {
    UINT cbSize;
    UINT uFlags;
    HWND hwnd;
    UINT_PTR uId;
    RECT rect;
    HINSTANCE hinst;
    LPSTR lpszText;
    LPARAM lParam;
    void *lpReserved;
} TTTOOLINFOA, NEAR *PTOOLINFOA, *LPTTTOOLINFOA;
'''


# begin_r_commctrl

TTS_ALWAYSTIP          = 0x01
TTS_NOPREFIX           = 0x02
TTS_NOANIMATE          = 0x10
TTS_NOFADE             = 0x20
TTS_BALLOON            = 0x40
TTS_CLOSE              = 0x80

# end_r_commctrl

TTF_IDISHWND           = 0x0001

# Use this to center around trackpoint in trackmode
# -OR- to center around tool in normal mode.
# Use TTF_ABSOLUTE to place the tip exactly at the track coords when
# in tracking mode.  TTF_ABSOLUTE can be used in conjunction with TTF_CENTERTIP
# to center the tip absolutely about the track point.

TTF_CENTERTIP          = 0x0002
TTF_RTLREADING         = 0x0004
TTF_SUBCLASS           = 0x0010
TTF_TRACK              = 0x0020
TTF_ABSOLUTE           = 0x0080
TTF_TRANSPARENT        = 0x0100
TTF_PARSELINKS         = 0x1000
TTF_DI_SETITEM         = 0x8000       # valid only on the TTN_NEEDTEXT callback


TTDT_AUTOMATIC          = 0
TTDT_RESHOW             = 1
TTDT_AUTOPOP            = 2
TTDT_INITIAL            = 3

# ToolTip Icons (Set with TTM_SETTITLE)
TTI_NONE                = 0
TTI_INFO                = 1
TTI_WARNING             = 2
TTI_ERROR               = 3


# Tool Tip Messages
TTM_ACTIVATE            = (WM_USER + 1)
TTM_SETDELAYTIME        = (WM_USER + 3)
TTM_ADDTOOLA            = (WM_USER + 4)
TTM_ADDTOOLW            = (WM_USER + 50)
TTM_DELTOOLA            = (WM_USER + 5)
TTM_DELTOOLW            = (WM_USER + 51)
TTM_NEWTOOLRECTA        = (WM_USER + 6)
TTM_NEWTOOLRECTW        = (WM_USER + 52)
TTM_RELAYEVENT          = (WM_USER + 7) # Win7: wParam = GetMessageExtraInfo() when relaying WM_MOUSEMOVE
TTM_GETTOOLINFOA        = (WM_USER + 8)
TTM_GETTOOLINFOW        = (WM_USER + 53)
TTM_SETTOOLINFOA        = (WM_USER + 9)
TTM_SETTOOLINFOW        = (WM_USER + 54)
TTM_HITTESTA            = (WM_USER +10)
TTM_HITTESTW            = (WM_USER +55)
TTM_GETTEXTA            = (WM_USER +11)
TTM_GETTEXTW            = (WM_USER +56)
TTM_UPDATETIPTEXTA      = (WM_USER +12)
TTM_UPDATETIPTEXTW      = (WM_USER +57)
TTM_GETTOOLCOUNT        = (WM_USER +13)
TTM_ENUMTOOLSA          = (WM_USER +14)
TTM_ENUMTOOLSW          = (WM_USER +58)
TTM_GETCURRENTTOOLA     = (WM_USER + 15)
TTM_GETCURRENTTOOLW     = (WM_USER + 59)
TTM_WINDOWFROMPOINT     = (WM_USER + 16)
TTM_TRACKACTIVATE       = (WM_USER + 17)  # wParam = TRUE/FALSE start end  lparam = LPTOOLINFO
TTM_TRACKPOSITION       = (WM_USER + 18)  # lParam = dwPos
TTM_SETTIPBKCOLOR       = (WM_USER + 19)
TTM_SETTIPTEXTCOLOR     = (WM_USER + 20)
TTM_GETDELAYTIME        = (WM_USER + 21)
TTM_GETTIPBKCOLOR       = (WM_USER + 22)
TTM_GETTIPTEXTCOLOR     = (WM_USER + 23)
TTM_SETMAXTIPWIDTH      = (WM_USER + 24)
TTM_GETMAXTIPWIDTH      = (WM_USER + 25)
TTM_SETMARGIN           = (WM_USER + 26)  # lParam = lprc
TTM_GETMARGIN           = (WM_USER + 27)  # lParam = lprc
TTM_POP                 = (WM_USER + 28)
TTM_UPDATE              = (WM_USER + 29)
TTM_GETBUBBLESIZE       = (WM_USER + 30)
TTM_ADJUSTRECT          = (WM_USER + 31)
TTM_SETTITLEA           = (WM_USER + 32)  # wParam = TTI_*, lParam = char* szTitle
TTM_SETTITLEW           = (WM_USER + 33)  # wParam = TTI_*, lParam = wchar* szTitle
TTM_POPUP               = (WM_USER + 34)
TTM_GETTITLE            = (WM_USER + 35) # wParam = 0, lParam = TTGETTITLE*


TTM_ADDTOOL             = TTM_ADDTOOLW
TTM_DELTOOL             = TTM_DELTOOLW
TTM_NEWTOOLRECT         = TTM_NEWTOOLRECTW
TTM_GETTOOLINFO         = TTM_GETTOOLINFOW
TTM_SETTOOLINFO         = TTM_SETTOOLINFOW
TTM_HITTEST             = TTM_HITTESTW
TTM_GETTEXT             = TTM_GETTEXTW
TTM_UPDATETIPTEXT       = TTM_UPDATETIPTEXTW
TTM_ENUMTOOLS           = TTM_ENUMTOOLSW
TTM_GETCURRENTTOOL      = TTM_GETCURRENTTOOLW
TTM_SETTITLE            = TTM_SETTITLEW

TTN_GETDISPINFOA        = (TTN_FIRST - 0)
TTN_GETDISPINFOW        = (TTN_FIRST - 10)
TTN_SHOW                = (TTN_FIRST - 1)
TTN_POP                 = (TTN_FIRST - 2)
TTN_LINKCLICK           = (TTN_FIRST - 3)
TTN_GETDISPINFO         = TTN_GETDISPINFOW
TTN_NEEDTEXT            = TTN_GETDISPINFO
TTN_NEEDTEXTA           = TTN_GETDISPINFOA
TTN_NEEDTEXTW           = TTN_GETDISPINFOW

#====== STATUS BAR CONTROL ===================================================

# begin_r_commctrl

SBARS_SIZEGRIP         = 0x0100
SBARS_TOOLTIPS         = 0x0800
# this is a status bar flag, preference to SBARS_TOOLTIPS
SBT_TOOLTIPS           = 0x0800



STATUSCLASSNAMEW        = "msctls_statusbar32"
STATUSCLASSNAMEA        = STATUSCLASSNAMEW
STATUSCLASSNAME         = STATUSCLASSNAMEW

SB_SETTEXTA             = (WM_USER+1)
SB_SETTEXTW             = (WM_USER+11)
SB_GETTEXTA             = (WM_USER+2)
SB_GETTEXTW             = (WM_USER+13)
SB_GETTEXTLENGTHA       = (WM_USER+3)
SB_GETTEXTLENGTHW       = (WM_USER+12)
SB_GETTEXT              = SB_GETTEXTW
SB_SETTEXT              = SB_SETTEXTW
SB_GETTEXTLENGTH        = SB_GETTEXTLENGTHW

SB_SETPARTS             = (WM_USER+4)
SB_GETPARTS             = (WM_USER+6)
SB_GETBORDERS           = (WM_USER+7)
SB_SETMINHEIGHT         = (WM_USER+8)
SB_SIMPLE               = (WM_USER+9)
SB_GETRECT              = (WM_USER+10)
SB_ISSIMPLE             = (WM_USER+14)
SB_SETICON              = (WM_USER+15)
SB_SETTIPTEXTA          = (WM_USER+16)
SB_SETTIPTEXTW          = (WM_USER+17)
SB_GETTIPTEXTA          = (WM_USER+18)
SB_GETTIPTEXTW          = (WM_USER+19)
SB_SETTIPTEXT           = SB_SETTIPTEXTW
SB_GETTIPTEXT           = SB_GETTIPTEXTW
SB_GETICON              = (WM_USER+20)
SB_SETUNICODEFORMAT     = CCM_SETUNICODEFORMAT
SB_GETUNICODEFORMAT     = CCM_GETUNICODEFORMAT
SBT_OWNERDRAW           = 0x1000
SBT_NOBORDERS           = 0x0100
SBT_POPOUT              = 0x0200
SBT_RTLREADING          = 0x0400
SBT_NOTABPARSING        = 0x0800

SB_SETBKCOLOR           = CCM_SETBKCOLOR      # lParam = bkColor

# status bar notifications
SBN_SIMPLEMODECHANGE    = (SBN_FIRST - 0)

# refers to the data saved for simple mode
SB_SIMPLEID = 0x00ff

#====== MENU HELP ============================================================

MINSYSCOMMAND   = SC_SIZE

#====== TRACKBAR CONTROL =====================================================

TRACKBAR_CLASSA         = "msctls_trackbar32"
TRACKBAR_CLASSW         = TRACKBAR_CLASSA
TRACKBAR_CLASS          = TRACKBAR_CLASSW


# begin_r_commctrl

TBS_AUTOTICKS          = 0x0001
TBS_VERT               = 0x0002
TBS_HORZ               = 0x0000
TBS_TOP                = 0x0004
TBS_BOTTOM             = 0x0000
TBS_LEFT               = 0x0004
TBS_RIGHT              = 0x0000
TBS_BOTH               = 0x0008
TBS_NOTICKS            = 0x0010
TBS_ENABLESELRANGE     = 0x0020
TBS_FIXEDLENGTH        = 0x0040
TBS_NOTHUMB            = 0x0080
TBS_TOOLTIPS           = 0x0100
TBS_REVERSED           = 0x0200  # Accessibility hint: the smaller number (usually the min value) means "high" and the larger number (usually the max value) means "low"
TBS_DOWNISLEFT         = 0x0400  # Down=Left and Up=Right (default is Down=Right and Up=Left)


# end_r_commctrl

TBM_GETPOS              = (WM_USER)
TBM_GETRANGEMIN         = (WM_USER+1)
TBM_GETRANGEMAX         = (WM_USER+2)
TBM_GETTIC              = (WM_USER+3)
TBM_SETTIC              = (WM_USER+4)
TBM_SETPOS              = (WM_USER+5)
TBM_SETRANGE            = (WM_USER+6)
TBM_SETRANGEMIN         = (WM_USER+7)
TBM_SETRANGEMAX         = (WM_USER+8)
TBM_CLEARTICS           = (WM_USER+9)
TBM_SETSEL              = (WM_USER+10)
TBM_SETSELSTART         = (WM_USER+11)
TBM_SETSELEND           = (WM_USER+12)
TBM_GETPTICS            = (WM_USER+14)
TBM_GETTICPOS           = (WM_USER+15)
TBM_GETNUMTICS          = (WM_USER+16)
TBM_GETSELSTART         = (WM_USER+17)
TBM_GETSELEND           = (WM_USER+18)
TBM_CLEARSEL            = (WM_USER+19)
TBM_SETTICFREQ          = (WM_USER+20)
TBM_SETPAGESIZE         = (WM_USER+21)
TBM_GETPAGESIZE         = (WM_USER+22)
TBM_SETLINESIZE         = (WM_USER+23)
TBM_GETLINESIZE         = (WM_USER+24)
TBM_GETTHUMBRECT        = (WM_USER+25)
TBM_GETCHANNELRECT      = (WM_USER+26)
TBM_SETTHUMBLENGTH      = (WM_USER+27)
TBM_GETTHUMBLENGTH      = (WM_USER+28)
TBM_SETTOOLTIPS         = (WM_USER+29)
TBM_GETTOOLTIPS         = (WM_USER+30)
TBM_SETTIPSIDE          = (WM_USER+31)
# TrackBar Tip Side flags
TBTS_TOP                = 0
TBTS_LEFT               = 1
TBTS_BOTTOM             = 2
TBTS_RIGHT              = 3

TBM_SETBUDDY            = (WM_USER+32) # wparam = BOOL fLeft; (or right)
TBM_GETBUDDY            = (WM_USER+33) # wparam = BOOL fLeft; (or right)
TBM_SETPOSNOTIFY        = (WM_USER+34)
TBM_SETUNICODEFORMAT    = CCM_SETUNICODEFORMAT
TBM_GETUNICODEFORMAT    = CCM_GETUNICODEFORMAT


TB_LINEUP               = 0
TB_LINEDOWN             = 1
TB_PAGEUP               = 2
TB_PAGEDOWN             = 3
TB_THUMBPOSITION        = 4
TB_THUMBTRACK           = 5
TB_TOP                  = 6
TB_BOTTOM               = 7
TB_ENDTRACK             = 8

# custom draw item specs
TBCD_TICS      = 0x0001
TBCD_THUMB     = 0x0002
TBCD_CHANNEL   = 0x0003

#====== DRAG LIST CONTROL ====================================================

DL_BEGINDRAG            = (WM_USER+133)
DL_DRAGGING             = (WM_USER+134)
DL_DROPPED              = (WM_USER+135)
DL_CANCELDRAG           = (WM_USER+136)

DL_CURSORSET            = 0
DL_STOPCURSOR           = 1
DL_COPYCURSOR           = 2
DL_MOVECURSOR           = 3

DRAGLISTMSGSTRING       = "commctrl_DragListMsg"

#====== UPDOWN CONTROL =======================================================

UPDOWN_CLASSA           = "msctls_updown32"
UPDOWN_CLASSW           = UPDOWN_CLASSA
UPDOWN_CLASS            = UPDOWN_CLASSW

UD_MAXVAL              = 0x7fff
UD_MINVAL              = (-UD_MAXVAL)

# begin_r_commctrl

UDS_WRAP               = 0x0001
UDS_SETBUDDYINT        = 0x0002
UDS_ALIGNRIGHT         = 0x0004
UDS_ALIGNLEFT          = 0x0008
UDS_AUTOBUDDY          = 0x0010
UDS_ARROWKEYS          = 0x0020
UDS_HORZ               = 0x0040
UDS_NOTHOUSANDS        = 0x0080
UDS_HOTTRACK           = 0x0100

# end_r_commctrl

UDM_SETRANGE            = (WM_USER+101)
UDM_GETRANGE            = (WM_USER+102)
UDM_SETPOS              = (WM_USER+103)
UDM_GETPOS              = (WM_USER+104)
UDM_SETBUDDY            = (WM_USER+105)
UDM_GETBUDDY            = (WM_USER+106)
UDM_SETACCEL            = (WM_USER+107)
UDM_GETACCEL            = (WM_USER+108)
UDM_SETBASE             = (WM_USER+109)
UDM_GETBASE             = (WM_USER+110)
UDM_SETRANGE32          = (WM_USER+111)
UDM_GETRANGE32          = (WM_USER+112) # wParam & lParam are LPINT
UDM_SETUNICODEFORMAT    = CCM_SETUNICODEFORMAT
UDM_GETUNICODEFORMAT    = CCM_GETUNICODEFORMAT
UDM_SETPOS32            = (WM_USER+113)
UDM_GETPOS32            = (WM_USER+114)

UDN_DELTAPOS            = (UDN_FIRST - 1)

#====== PROGRESS CONTROL =====================================================

PROGRESS_CLASSA         = "msctls_progress32"
PROGRESS_CLASSW         = PROGRESS_CLASSA
PROGRESS_CLASS          = PROGRESS_CLASSW

# begin_r_commctrl

PBS_SMOOTH             = 0x01
PBS_VERTICAL           = 0x04

# end_r_commctrl

PBM_SETRANGE            = (WM_USER+1)
PBM_SETPOS              = (WM_USER+2)
PBM_DELTAPOS            = (WM_USER+3)
PBM_SETSTEP             = (WM_USER+4)
PBM_STEPIT              = (WM_USER+5)
PBM_SETRANGE32          = (WM_USER+6)  # lParam = high, wParam = low

PBM_GETRANGE            = (WM_USER+7)  # wParam = return (TRUE ? low : high). lParam = PPBRANGE or NULL
PBM_GETPOS              = (WM_USER+8)
PBM_SETBARCOLOR         = (WM_USER+9)             # lParam = bar color
PBM_SETBKCOLOR          = CCM_SETBKCOLOR  # lParam = bkColor

# begin_r_commctrl

PBS_MARQUEE            = 0x08

# end_r_commctrl

PBM_SETMARQUEE          = (WM_USER+10)

#====== HOTKEY CONTROL =======================================================

HOTKEYF_SHIFT          = 0x01
HOTKEYF_CONTROL        = 0x02
HOTKEYF_ALT            = 0x04
HOTKEYF_EXT            = 0x08

HKCOMB_NONE            = 0x0001
HKCOMB_S               = 0x0002
HKCOMB_C               = 0x0004
HKCOMB_A               = 0x0008
HKCOMB_SC              = 0x0010
HKCOMB_SA              = 0x0020
HKCOMB_CA              = 0x0040
HKCOMB_SCA             = 0x0080


HKM_SETHOTKEY           = (WM_USER+1)
HKM_GETHOTKEY           = (WM_USER+2)
HKM_SETRULES            = (WM_USER+3)

HOTKEY_CLASSA           = "msctls_hotkey32"
HOTKEY_CLASSW           = HOTKEY_CLASSA
HOTKEY_CLASS            = HOTKEY_CLASSW

#====== COMMON CONTROL STYLES ================================================

CCS_TOP                = 0x00000001L
CCS_NOMOVEY            = 0x00000002L
CCS_BOTTOM             = 0x00000003L
CCS_NORESIZE           = 0x00000004L
CCS_NOPARENTALIGN      = 0x00000008L
CCS_ADJUSTABLE         = 0x00000020L
CCS_NODIVIDER          = 0x00000040L
CCS_VERT               = 0x00000080L
CCS_LEFT               = (CCS_VERT | CCS_TOP)
CCS_RIGHT              = (CCS_VERT | CCS_BOTTOM)
CCS_NOMOVEX            = (CCS_VERT | CCS_NOMOVEY)

# end_r_commctrl

#====== SysLink control =========================================


INVALID_LINK_INDEX  = (-1)
MAX_LINKID_TEXT     = 48
L_MAX_URL_LENGTH    = (2048 + 32 + len(":#"))

WC_LINK             = "SysLink"

# begin_r_commctrl

LWS_TRANSPARENT    = 0x0001
LWS_IGNORERETURN   = 0x0002

# end_r_commctrl

LIF_ITEMINDEX   = 0x00000001
LIF_STATE       = 0x00000002
LIF_ITEMID      = 0x00000004
LIF_URL         = 0x00000008

LIS_FOCUSED        = 0x00000001
LIS_ENABLED        = 0x00000002
LIS_VISITED        = 0x00000004

#  LinkWindow messages
LM_HITTEST         = (WM_USER+0x300)  # wParam: n/a, lparam: PLHITTESTINFO, ret: BOOL
LM_GETIDEALHEIGHT  = (WM_USER+0x301)  # wParam: cxMaxWidth, lparam: n/a, ret: cy
LM_SETITEM         = (WM_USER+0x302)  # wParam: n/a, lparam: LITEM*, ret: BOOL
LM_GETITEM         = (WM_USER+0x303)  # wParam: n/a, lparam: LITEM*, ret: BOOL
LM_GETIDEALSIZE    = (LM_GETIDEALHEIGHT)  # wParam: cxMaxWidth, lparam: SIZE*, ret: cy


#====== End SysLink control =========================================


#====== LISTVIEW CONTROL =====================================================

WC_LISTVIEWA            = "SysListView32"
WC_LISTVIEWW            = WC_LISTVIEWA
WC_LISTVIEW             = WC_LISTVIEWW

# begin_r_commctrl

LVS_ICON               = 0x0000
LVS_REPORT             = 0x0001
LVS_SMALLICON          = 0x0002
LVS_LIST               = 0x0003
LVS_TYPEMASK           = 0x0003
LVS_SINGLESEL          = 0x0004
LVS_SHOWSELALWAYS      = 0x0008
LVS_SORTASCENDING      = 0x0010
LVS_SORTDESCENDING     = 0x0020
LVS_SHAREIMAGELISTS    = 0x0040
LVS_NOLABELWRAP        = 0x0080
LVS_AUTOARRANGE        = 0x0100
LVS_EDITLABELS         = 0x0200
LVS_OWNERDATA          = 0x1000
LVS_NOSCROLL           = 0x2000

LVS_TYPESTYLEMASK      = 0xfc00

LVS_ALIGNTOP           = 0x0000
LVS_ALIGNLEFT          = 0x0800
LVS_ALIGNMASK          = 0x0c00

LVS_OWNERDRAWFIXED     = 0x0400
LVS_NOCOLUMNHEADER     = 0x4000
LVS_NOSORTHEADER       = 0x8000

# end_r_commctrl

LVM_SETUNICODEFORMAT     = CCM_SETUNICODEFORMAT

LVM_GETUNICODEFORMAT     = CCM_GETUNICODEFORMAT

LVM_GETBKCOLOR          = (LVM_FIRST + 0)

LVM_SETBKCOLOR          = (LVM_FIRST + 1)

LVM_GETIMAGELIST        = (LVM_FIRST + 2)

LVSIL_NORMAL            = 0
LVSIL_SMALL             = 1
LVSIL_STATE             = 2
LVSIL_GROUPHEADER       = 3

LVM_SETIMAGELIST        = (LVM_FIRST + 3)

LVM_GETITEMCOUNT        = (LVM_FIRST + 4)

LVIF_TEXT              = 0x00000001
LVIF_IMAGE             = 0x00000002
LVIF_PARAM             = 0x00000004
LVIF_STATE             = 0x00000008
LVIF_INDENT            = 0x00000010
LVIF_NORECOMPUTE       = 0x00000800
LVIF_GROUPID           = 0x00000100
LVIF_COLUMNS           = 0x00000200

LVIS_FOCUSED           = 0x0001
LVIS_SELECTED          = 0x0002
LVIS_CUT               = 0x0004
LVIS_DROPHILITED       = 0x0008
LVIS_GLOW              = 0x0010
LVIS_ACTIVATING        = 0x0020

LVIS_OVERLAYMASK       = 0x0F00
LVIS_STATEIMAGEMASK    = 0xF000

def INDEXTOSTATEIMAGEMASK(i):
    return (i << 12)

I_INDENTCALLBACK        = (-1)
I_GROUPIDCALLBACK       = (-1)
I_GROUPIDNONE           = (-2)

I_IMAGECALLBACK         = (-1)

I_IMAGENONE             = (-2)


I_COLUMNSCALLBACK       = -1

LVM_GETITEMA            = (LVM_FIRST + 5)
LVM_GETITEMW            = (LVM_FIRST + 75)
LVM_GETITEM             = LVM_GETITEMW

LVM_SETITEMA            = (LVM_FIRST + 6)
LVM_SETITEMW            = (LVM_FIRST + 76)
LVM_SETITEM             = LVM_SETITEMW

LVM_INSERTITEMA         = (LVM_FIRST + 7)
LVM_INSERTITEMW         = (LVM_FIRST + 77)
#ifdef UNICODE
LVM_INSERTITEM          = LVM_INSERTITEMW


LVM_DELETEITEM          = (LVM_FIRST + 8)


LVM_DELETEALLITEMS      = (LVM_FIRST + 9)

LVM_GETCALLBACKMASK     = (LVM_FIRST + 10)

LVM_SETCALLBACKMASK     = (LVM_FIRST + 11)


LVNI_ALL               = 0x0000

LVNI_FOCUSED           = 0x0001
LVNI_SELECTED          = 0x0002
LVNI_CUT               = 0x0004
LVNI_DROPHILITED       = 0x0008
LVNI_STATEMASK         = (LVNI_FOCUSED | LVNI_SELECTED | LVNI_CUT | LVNI_DROPHILITED)

LVNI_VISIBLEORDER      = 0x0010
LVNI_PREVIOUS          = 0x0020
LVNI_VISIBLEONLY       = 0x0040
LVNI_SAMEGROUPONLY     = 0x0080

LVNI_ABOVE             = 0x0100
LVNI_BELOW             = 0x0200
LVNI_TOLEFT            = 0x0400
LVNI_TORIGHT           = 0x0800
LVNI_DIRECTIONMASK     = (LVNI_ABOVE | LVNI_BELOW | LVNI_TOLEFT | LVNI_TORIGHT)


LVFI_PARAM             = 0x0001
LVFI_STRING            = 0x0002
LVFI_SUBSTRING         = 0x0004  # Same as LVFI_PARTIAL
LVFI_PARTIAL           = 0x0008
LVFI_WRAP              = 0x0020
LVFI_NEARESTXY         = 0x0040

LVM_FINDITEMA           = (LVM_FIRST + 13)
LVM_FINDITEMW           = (LVM_FIRST + 83)
LVM_FINDITEM            = LVM_FINDITEMW

LVIR_BOUNDS             = 0
LVIR_ICON               = 1
LVIR_LABEL              = 2
LVIR_SELECTBOUNDS       = 3


LVM_GETITEMRECT         = (LVM_FIRST + 14)

LVM_SETITEMPOSITION     = (LVM_FIRST + 15)

LVM_GETITEMPOSITION     = (LVM_FIRST + 16)

LVM_GETSTRINGWIDTHA     = (LVM_FIRST + 17)
LVM_GETSTRINGWIDTHW     = (LVM_FIRST + 87)
LVM_GETSTRINGWIDTH      = LVM_GETSTRINGWIDTHW


LVHT_NOWHERE           = 0x00000001
LVHT_ONITEMICON        = 0x00000002
LVHT_ONITEMLABEL       = 0x00000004
LVHT_ONITEMSTATEICON   = 0x00000008
LVHT_ONITEM            = (LVHT_ONITEMICON | LVHT_ONITEMLABEL | LVHT_ONITEMSTATEICON)

LVHT_ABOVE             = 0x00000008
LVHT_BELOW             = 0x00000010
LVHT_TORIGHT           = 0x00000020
LVHT_TOLEFT            = 0x00000040


LVHT_EX_GROUP_HEADER      = 0x10000000
LVHT_EX_GROUP_FOOTER      = 0x20000000
LVHT_EX_GROUP_COLLAPSE    = 0x40000000
LVHT_EX_GROUP_BACKGROUND  = 0x80000000
LVHT_EX_GROUP_STATEICON   = 0x01000000
LVHT_EX_GROUP_SUBSETLINK  = 0x02000000
LVHT_EX_GROUP             = (LVHT_EX_GROUP_BACKGROUND | LVHT_EX_GROUP_COLLAPSE | LVHT_EX_GROUP_FOOTER | LVHT_EX_GROUP_HEADER | LVHT_EX_GROUP_STATEICON | LVHT_EX_GROUP_SUBSETLINK)
LVHT_EX_ONCONTENTS        = 0x04000000 # On item AND not on the background
LVHT_EX_FOOTER            = 0x08000000

LVM_HITTEST             = (LVM_FIRST + 18)

LVM_ENSUREVISIBLE       = (LVM_FIRST + 19)

LVM_SCROLL              = (LVM_FIRST + 20)

LVM_REDRAWITEMS         = (LVM_FIRST + 21)

LVA_DEFAULT            = 0x0000
LVA_ALIGNLEFT          = 0x0001
LVA_ALIGNTOP           = 0x0002
LVA_SNAPTOGRID         = 0x0005


LVM_ARRANGE             = (LVM_FIRST + 22)

LVM_EDITLABELA          = (LVM_FIRST + 23)
LVM_EDITLABELW          = (LVM_FIRST + 118)
LVM_EDITLABEL           = LVM_EDITLABELW

LVCF_FMT               = 0x0001
LVCF_WIDTH             = 0x0002
LVCF_TEXT              = 0x0004
LVCF_SUBITEM           = 0x0008
LVCF_IMAGE             = 0x0010
LVCF_ORDER             = 0x0020

# LVCFMT_ flags up to FFFF are shared with the header control (HDF_ flags).
# Flags above FFFF are listview-specific.

LVCFMT_LEFT                = 0x0000 # Same as HDF_LEFT
LVCFMT_RIGHT               = 0x0001 # Same as HDF_RIGHT
LVCFMT_CENTER              = 0x0002 # Same as HDF_CENTER
LVCFMT_JUSTIFYMASK         = 0x0003 # Same as HDF_JUSTIFYMASK
LVCFMT_IMAGE               = 0x0800 # Same as HDF_IMAGE
LVCFMT_BITMAP_ON_RIGHT     = 0x1000 # Same as HDF_BITMAP_ON_RIGHT
LVCFMT_COL_HAS_IMAGES      = 0x8000 # Same as HDF_OWNERDRAW


LVM_GETCOLUMNA          = (LVM_FIRST + 25)
LVM_GETCOLUMNW          = (LVM_FIRST + 95)
LVM_GETCOLUMN           = LVM_GETCOLUMNW

LVM_SETCOLUMNA          = (LVM_FIRST + 26)
LVM_SETCOLUMNW          = (LVM_FIRST + 96)
LVM_SETCOLUMN           = LVM_SETCOLUMNW

LVM_INSERTCOLUMNA       = (LVM_FIRST + 27)
LVM_INSERTCOLUMNW       = (LVM_FIRST + 97)
#   define  LVM_INSERTCOLUMN    = LVM_INSERTCOLUMNW

LVM_DELETECOLUMN        = (LVM_FIRST + 28)

LVM_GETCOLUMNWIDTH      = (LVM_FIRST + 29)

LVSCW_AUTOSIZE              = -1
LVSCW_AUTOSIZE_USEHEADER    = -2
LVM_SETCOLUMNWIDTH          = (LVM_FIRST + 30)

LVM_GETHEADER               = (LVM_FIRST + 31)

LVM_CREATEDRAGIMAGE     = (LVM_FIRST + 33)

LVM_GETVIEWRECT         = (LVM_FIRST + 34)

LVM_GETTEXTCOLOR        = (LVM_FIRST + 35)

LVM_SETTEXTCOLOR        = (LVM_FIRST + 36)

LVM_GETTEXTBKCOLOR      = (LVM_FIRST + 37)

LVM_SETTEXTBKCOLOR      = (LVM_FIRST + 38)

LVM_GETTOPINDEX         = (LVM_FIRST + 39)

LVM_GETCOUNTPERPAGE     = (LVM_FIRST + 40)

LVM_GETORIGIN           = (LVM_FIRST + 41)

LVM_UPDATE              = (LVM_FIRST + 42)

LVM_SETITEMSTATE        = (LVM_FIRST + 43)

LVM_GETITEMSTATE        = (LVM_FIRST + 44)

LVM_GETITEMTEXTA        = (LVM_FIRST + 45)
LVM_GETITEMTEXTW        = (LVM_FIRST + 115)
LVM_GETITEMTEXT         = LVM_GETITEMTEXTW

LVM_SETITEMTEXTA        = (LVM_FIRST + 46)
LVM_SETITEMTEXTW        = (LVM_FIRST + 116)
LVM_SETITEMTEXT         = LVM_SETITEMTEXTW

# these flags only apply to LVS_OWNERDATA listviews in report or list mode
LVSICF_NOINVALIDATEALL = 0x00000001
LVSICF_NOSCROLL        = 0x00000002

LVM_SORTITEMS           = (LVM_FIRST + 48)

LVM_SETITEMPOSITION32   = (LVM_FIRST + 49)

LVM_GETSELECTEDCOUNT    = (LVM_FIRST + 50)

LVM_GETITEMSPACING      = (LVM_FIRST + 51)

LVM_GETISEARCHSTRINGA   = (LVM_FIRST + 52)
LVM_GETISEARCHSTRINGW   = (LVM_FIRST + 117)
LVM_GETISEARCHSTRING    = LVM_GETISEARCHSTRINGW

LVM_SETICONSPACING      = (LVM_FIRST + 53)
# -1 for cx and cy means we'll use the default (system settings)
# 0 for cx or cy means use the current setting (allows you to change just one param)

LVM_SETEXTENDEDLISTVIEWSTYLE = (LVM_FIRST + 54)   # optional wParam == mask

LVM_GETEXTENDEDLISTVIEWSTYLE = (LVM_FIRST + 55)

LVS_EX_GRIDLINES         = 0x00000001
LVS_EX_SUBITEMIMAGES     = 0x00000002
LVS_EX_CHECKBOXES        = 0x00000004
LVS_EX_TRACKSELECT       = 0x00000008
LVS_EX_HEADERDRAGDROP    = 0x00000010
LVS_EX_FULLROWSELECT     = 0x00000020 # applies to report mode only
LVS_EX_ONECLICKACTIVATE  = 0x00000040
LVS_EX_TWOCLICKACTIVATE  = 0x00000080
LVS_EX_FLATSB            = 0x00000100
LVS_EX_REGIONAL          = 0x00000200
LVS_EX_INFOTIP           = 0x00000400 # listview does InfoTips for you
LVS_EX_UNDERLINEHOT      = 0x00000800
LVS_EX_UNDERLINECOLD     = 0x00001000
LVS_EX_MULTIWORKAREAS    = 0x00002000
LVS_EX_LABELTIP          = 0x00004000 # listview unfolds partly hidden labels if it does not have infotip text
LVS_EX_BORDERSELECT      = 0x00008000 # border selection style instead of highlight
LVS_EX_DOUBLEBUFFER      = 0x00010000
LVS_EX_HIDELABELS        = 0x00020000
LVS_EX_SINGLEROW         = 0x00040000
LVS_EX_SNAPTOGRID        = 0x00080000  # Icons automatically snap to grid.
LVS_EX_SIMPLESELECT      = 0x00100000  # Also changes overlay rendering to top right for icon mode.


LVM_GETSUBITEMRECT        = (LVM_FIRST + 56)

LVM_SUBITEMHITTEST        = (LVM_FIRST + 57)

LVM_SETCOLUMNORDERARRAY   = (LVM_FIRST + 58)

LVM_GETCOLUMNORDERARRAY   = (LVM_FIRST + 59)

LVM_SETHOTITEM            = (LVM_FIRST + 60)

LVM_GETHOTITEM            = (LVM_FIRST + 61)

LVM_SETHOTCURSOR          = (LVM_FIRST + 62)

LVM_GETHOTCURSOR          = (LVM_FIRST + 63)

LVM_APPROXIMATEVIEWRECT   = (LVM_FIRST + 64)

LV_MAX_WORKAREAS          = 16
LVM_SETWORKAREAS          = (LVM_FIRST + 65)

LVM_GETWORKAREAS          = (LVM_FIRST + 70)

LVM_GETNUMBEROFWORKAREAS  = (LVM_FIRST + 73)

LVM_GETSELECTIONMARK     = (LVM_FIRST + 66)

LVM_SETSELECTIONMARK     = (LVM_FIRST + 67)

LVM_SETHOVERTIME         = (LVM_FIRST + 71)

LVM_GETHOVERTIME         = (LVM_FIRST + 72)

LVM_SETTOOLTIPS          = (LVM_FIRST + 74)

LVM_GETTOOLTIPS          = (LVM_FIRST + 78)

LVM_SORTITEMSEX          = (LVM_FIRST + 81)


LVBKIF_SOURCE_NONE          = 0x00000000
LVBKIF_SOURCE_HBITMAP       = 0x00000001
LVBKIF_SOURCE_URL           = 0x00000002
LVBKIF_SOURCE_MASK          = 0x00000003
LVBKIF_STYLE_NORMAL         = 0x00000000
LVBKIF_STYLE_TILE           = 0x00000010
LVBKIF_STYLE_MASK           = 0x00000010
LVBKIF_FLAG_TILEOFFSET      = 0x00000100
LVBKIF_TYPE_WATERMARK       = 0x10000000
LVBKIF_FLAG_ALPHABLEND      = 0x20000000
LVM_SETBKIMAGEA             = (LVM_FIRST + 68)
LVM_SETBKIMAGEW             = (LVM_FIRST + 138)
LVM_GETBKIMAGEA             = (LVM_FIRST + 69)
LVM_GETBKIMAGEW             = (LVM_FIRST + 139)
LVM_SETSELECTEDCOLUMN       = (LVM_FIRST + 140)

LV_VIEW_ICON           = 0x0000
LV_VIEW_DETAILS        = 0x0001
LV_VIEW_SMALLICON      = 0x0002
LV_VIEW_LIST           = 0x0003
LV_VIEW_TILE           = 0x0004
LV_VIEW_MAX            = 0x0004
LVM_SETVIEW            = (LVM_FIRST + 142)


LVM_GETVIEW            = (LVM_FIRST + 143)

LVGF_NONE          = 0x00000000
LVGF_HEADER        = 0x00000001
LVGF_FOOTER        = 0x00000002
LVGF_STATE         = 0x00000004
LVGF_ALIGN         = 0x00000008
LVGF_GROUPID       = 0x00000010

LVGS_NORMAL            = 0x00000000
LVGS_COLLAPSED         = 0x00000001
LVGS_HIDDEN            = 0x00000002
LVGS_NOHEADER          = 0x00000004
LVGS_COLLAPSIBLE       = 0x00000008
LVGS_FOCUSED           = 0x00000010
LVGS_SELECTED          = 0x00000020
LVGS_SUBSETED          = 0x00000040
LVGS_SUBSETLINKFOCUSED = 0x00000080

LVGA_HEADER_LEFT   = 0x00000001
LVGA_HEADER_CENTER = 0x00000002
LVGA_HEADER_RIGHT  = 0x00000004  # Don't forget to validate exclusivity
LVGA_FOOTER_LEFT   = 0x00000008
LVGA_FOOTER_CENTER = 0x00000010
LVGA_FOOTER_RIGHT  = 0x00000020  # Don't forget to validate exclusivity

LVM_INSERTGROUP              = (LVM_FIRST + 145)

LVM_SETGROUPINFO             = (LVM_FIRST + 147)

LVM_GETGROUPINFO             = (LVM_FIRST + 149)

LVM_REMOVEGROUP              = (LVM_FIRST + 150)

LVM_MOVEGROUP                = (LVM_FIRST + 151)

LVM_GETGROUPCOUNT            = (LVM_FIRST + 152)

LVM_GETGROUPINFOBYINDEX      = (LVM_FIRST + 153)

LVM_MOVEITEMTOGROUP          = (LVM_FIRST + 154)

LVGGR_GROUP         = 0 # Entire expanded group
LVGGR_HEADER        = 1 # Header only (collapsed group)
LVGGR_LABEL         = 2 # Label only
LVGGR_SUBSETLINK    = 3 # subset link only

LVM_GETGROUPRECT               = (LVM_FIRST + 98)

LVGMF_NONE         = 0x00000000
LVGMF_BORDERSIZE   = 0x00000001
LVGMF_BORDERCOLOR  = 0x00000002
LVGMF_TEXTCOLOR    = 0x00000004

LVM_SETGROUPMETRICS         = (LVM_FIRST + 155)

LVM_GETGROUPMETRICS         = (LVM_FIRST + 156)

LVM_ENABLEGROUPVIEW         = (LVM_FIRST + 157)

LVM_SORTGROUPS              = (LVM_FIRST + 158)

LVM_INSERTGROUPSORTED       = (LVM_FIRST + 159)

LVM_REMOVEALLGROUPS         = (LVM_FIRST + 160)

LVM_HASGROUP                = (LVM_FIRST + 161)

LVM_GETGROUPSTATE           = (LVM_FIRST + 92)

LVM_GETFOCUSEDGROUP         = (LVM_FIRST + 93)

LVTVIF_AUTOSIZE      = 0x00000000
LVTVIF_FIXEDWIDTH    = 0x00000001
LVTVIF_FIXEDHEIGHT   = 0x00000002
LVTVIF_FIXEDSIZE     = 0x00000003

LVTVIM_TILESIZE      = 0x00000001
LVTVIM_COLUMNS       = 0x00000002
LVTVIM_LABELMARGIN   = 0x00000004

LVM_SETTILEVIEWINFO                 = (LVM_FIRST + 162)

LVM_GETTILEVIEWINFO                 = (LVM_FIRST + 163)

LVM_SETTILEINFO                     = (LVM_FIRST + 164)

LVM_GETTILEINFO                     = (LVM_FIRST + 165)

LVIM_AFTER                          = 0x00000001 # TRUE = insert After iItem, otherwise before

LVM_SETINSERTMARK                   = (LVM_FIRST + 166)

LVM_GETINSERTMARK                   = (LVM_FIRST + 167)

LVM_INSERTMARKHITTEST               = (LVM_FIRST + 168)

LVM_GETINSERTMARKRECT               = (LVM_FIRST + 169)

LVM_SETINSERTMARKCOLOR              = (LVM_FIRST + 170)

LVM_GETINSERTMARKCOLOR               = (LVM_FIRST + 171)

LVM_SETINFOTIP          = (LVM_FIRST + 173)

LVM_GETSELECTEDCOLUMN   = (LVM_FIRST + 174)

LVM_ISGROUPVIEWENABLED  = (LVM_FIRST + 175)

LVM_GETOUTLINECOLOR     = (LVM_FIRST + 176)

LVM_SETOUTLINECOLOR     = (LVM_FIRST + 177)

LVM_CANCELEDITLABEL     = (LVM_FIRST + 179)

# These next to methods make it easy to identify an item that can be repositioned
# within listview. For example: Many developers use the lParam to store an identifier that is
# unique. Unfortunatly, in order to find this item, they have to iterate through all of the items
# in the listview. Listview will maintain a unique identifier.  The upper bound is the size of a DWORD.
LVM_MAPINDEXTOID       = (LVM_FIRST + 180)

LVM_MAPIDTOINDEX       = (LVM_FIRST + 181)

LVM_ISITEMVISIBLE      = (LVM_FIRST + 182)

LVM_GETEMPTYTEXT       = (LVM_FIRST + 204)

LVM_GETFOOTERRECT      = (LVM_FIRST + 205)

# footer flags
LVFF_ITEMCOUNT         = 0x00000001

LVM_GETFOOTERINFO      = (LVM_FIRST + 206)

LVM_GETFOOTERITEMRECT  = (LVM_FIRST + 207)

# footer item flags
LVFIF_TEXT              = 0x00000001
LVFIF_STATE             = 0x00000002

# footer item state
LVFIS_FOCUSED           = 0x0001


LVM_GETFOOTERITEM       = (LVM_FIRST + 208)

LVM_GETITEMINDEXRECT    = (LVM_FIRST + 209)

LVM_SETITEMINDEXSTATE   = (LVM_FIRST + 210)

LVM_GETNEXTITEMINDEX    = (LVM_FIRST + 211)

# key flags stored in uKeyFlags
LVKF_ALT      = 0x0001
LVKF_CONTROL  = 0x0002
LVKF_SHIFT    = 0x0004


# dwItemType
LVCDI_ITEM        = 0x00000000
LVCDI_GROUP       = 0x00000001
LVCDI_ITEMSLIST   = 0x00000002

# ListView custom draw return values
LVCDRF_NOSELECT            = 0x00010000
LVCDRF_NOGROUPFRAME        = 0x00020000

LVN_ITEMCHANGING        = (LVN_FIRST-0)
LVN_ITEMCHANGED         = (LVN_FIRST-1)
LVN_INSERTITEM          = (LVN_FIRST-2)
LVN_DELETEITEM          = (LVN_FIRST-3)
LVN_DELETEALLITEMS      = (LVN_FIRST-4)
LVN_BEGINLABELEDITA     = (LVN_FIRST-5)
LVN_BEGINLABELEDITW     = (LVN_FIRST-75)
LVN_ENDLABELEDITA       = (LVN_FIRST-6)
LVN_ENDLABELEDITW       = (LVN_FIRST-76)
LVN_COLUMNCLICK         = (LVN_FIRST-8)
LVN_BEGINDRAG           = (LVN_FIRST-9)
LVN_BEGINRDRAG          = (LVN_FIRST-11)
LVN_ODCACHEHINT         = (LVN_FIRST-13)
LVN_ODFINDITEMA         = (LVN_FIRST-52)
LVN_ODFINDITEMW         = (LVN_FIRST-79)

LVN_ITEMACTIVATE        = (LVN_FIRST-14)
LVN_ODSTATECHANGED      = (LVN_FIRST-15)
LVN_ODFINDITEM          = LVN_ODFINDITEMW


LVN_HOTTRACK            = (LVN_FIRST-21)

LVN_GETDISPINFOA        = (LVN_FIRST-50)
LVN_GETDISPINFOW        = (LVN_FIRST-77)
LVN_SETDISPINFOA        = (LVN_FIRST-51)
LVN_SETDISPINFOW        = (LVN_FIRST-78)
LVN_BEGINLABELEDIT      = LVN_BEGINLABELEDITW
LVN_ENDLABELEDIT        = LVN_ENDLABELEDITW
LVN_GETDISPINFO         = LVN_GETDISPINFOW
LVN_SETDISPINFO         = LVN_SETDISPINFOW

LVIF_DI_SETITEM        = 0x1000

LVN_KEYDOWN             = (LVN_FIRST-55)

LVN_MARQUEEBEGIN        = (LVN_FIRST-56)

# NMLVGETINFOTIPA.dwFlag values

LVGIT_UNFOLDED = 0x0001

LVN_GETINFOTIPA          = (LVN_FIRST-57)
LVN_GETINFOTIPW          = (LVN_FIRST-58)
LVN_GETINFOTIP           = LVN_GETINFOTIPW


#
#  LVN_INCREMENTALSEARCH gives the app the opportunity to customize
#  incremental search.  For example, if the items are numeric,
#  the app can do numerical search instead of string search.
#
#  ListView notifies the app with NMLVFINDITEM.
#  The app sets pnmfi->lvfi.lParam to the result of the incremental search,
#  or to LVNSCH_DEFAULT if ListView should do the default search,
#  or to LVNSCH_ERROR to fail the search and just beep,
#  or to LVNSCH_IGNORE to stop all ListView processing.
#
#  The return value is not used.

LVNSCH_DEFAULT  = -1
LVNSCH_ERROR    = -2
LVNSCH_IGNORE   = -3

LVN_INCREMENTALSEARCHA   = (LVN_FIRST-62)
LVN_INCREMENTALSEARCHW   = (LVN_FIRST-63)
LVN_INCREMENTALSEARCH    = LVN_INCREMENTALSEARCHW

LVN_BEGINSCROLL          = (LVN_FIRST-80)
LVN_ENDSCROLL            = (LVN_FIRST-81)

LVN_LINKCLICK           = (LVN_FIRST-84)


EMF_CENTERED           = 0x00000001  # render markup centered in the listview area


LVN_GETEMPTYMARKUP      = (LVN_FIRST-87)

#====== TREEVIEW CONTROL =====================================================

WC_TREEVIEWA            = "SysTreeView32"
WC_TREEVIEWW            = WC_TREEVIEWA
WC_TREEVIEW             = WC_TREEVIEWW

# begin_r_commctrl

TVS_HASBUTTONS         = 0x0001
TVS_HASLINES           = 0x0002
TVS_LINESATROOT        = 0x0004
TVS_EDITLABELS         = 0x0008
TVS_DISABLEDRAGDROP    = 0x0010
TVS_SHOWSELALWAYS      = 0x0020
TVS_RTLREADING         = 0x0040

TVS_NOTOOLTIPS         = 0x0080
TVS_CHECKBOXES         = 0x0100
TVS_TRACKSELECT        = 0x0200
TVS_SINGLEEXPAND       = 0x0400
TVS_INFOTIP            = 0x0800
TVS_FULLROWSELECT      = 0x1000
TVS_NOSCROLL           = 0x2000
TVS_NONEVENHEIGHT      = 0x4000
TVS_NOHSCROLL          = 0x8000  # TVS_NOSCROLL overrides this

TVIF_TEXT              = 0x0001
TVIF_IMAGE             = 0x0002
TVIF_PARAM             = 0x0004
TVIF_STATE             = 0x0008
TVIF_HANDLE            = 0x0010
TVIF_SELECTEDIMAGE     = 0x0020
TVIF_CHILDREN          = 0x0040
TVIF_INTEGRAL          = 0x0080

TVIS_SELECTED          = 0x0002
TVIS_CUT               = 0x0004
TVIS_DROPHILITED       = 0x0008
TVIS_BOLD              = 0x0010
TVIS_EXPANDED          = 0x0020
TVIS_EXPANDEDONCE      = 0x0040
TVIS_EXPANDPARTIAL     = 0x0080
TVIS_OVERLAYMASK       = 0x0F00
TVIS_STATEIMAGEMASK    = 0xF000
TVIS_USERMASK          = 0xF000
TVIS_EX_ALL            = 0x0002

TVM_INSERTITEMA         = (TV_FIRST + 0)
TVM_INSERTITEMW         = (TV_FIRST + 50)
TVM_INSERTITEM          = TVM_INSERTITEMW

TVM_DELETEITEM          = (TV_FIRST + 1)

TVM_EXPAND              = (TV_FIRST + 2)

TVE_COLLAPSE           = 0x0001
TVE_EXPAND             = 0x0002
TVE_TOGGLE             = 0x0003
TVE_EXPANDPARTIAL      = 0x4000
TVE_COLLAPSERESET      = 0x8000

TVM_GETITEMRECT         = (TV_FIRST + 4)

TVM_GETCOUNT            = (TV_FIRST + 5)

TVM_GETINDENT           = (TV_FIRST + 6)

TVM_SETINDENT           = (TV_FIRST + 7)

TVM_GETIMAGELIST        = (TV_FIRST + 8)

TVSIL_NORMAL            = 0
TVSIL_STATE             = 2

TVM_SETIMAGELIST        = (TV_FIRST + 9)

TVM_GETNEXTITEM         = (TV_FIRST + 10)

TVGN_ROOT              = 0x0000
TVGN_NEXT              = 0x0001
TVGN_PREVIOUS          = 0x0002
TVGN_PARENT            = 0x0003
TVGN_CHILD             = 0x0004
TVGN_FIRSTVISIBLE      = 0x0005
TVGN_NEXTVISIBLE       = 0x0006
TVGN_PREVIOUSVISIBLE   = 0x0007
TVGN_DROPHILITE        = 0x0008
TVGN_CARET             = 0x0009
TVGN_LASTVISIBLE       = 0x000A
TVSI_NOSINGLEEXPAND    = 0x8000 # Should not conflict with TVGN flags.

TVM_SELECTITEM          = (TV_FIRST + 11)

TVM_GETITEMA            = (TV_FIRST + 12)
TVM_GETITEMW            = (TV_FIRST + 62)
TVM_GETITEM             = TVM_GETITEMW

TVM_SETITEMA            = (TV_FIRST + 13)
TVM_SETITEMW            = (TV_FIRST + 63)
TVM_SETITEM             = TVM_SETITEMW

TVM_EDITLABELA          = (TV_FIRST + 14)
TVM_EDITLABELW          = (TV_FIRST + 65)
TVM_EDITLABEL           = TVM_EDITLABELW

TVM_GETEDITCONTROL      = (TV_FIRST + 15)

TVM_GETVISIBLECOUNT     = (TV_FIRST + 16)

TVM_HITTEST             = (TV_FIRST + 17)

TVHT_NOWHERE           = 0x0001
TVHT_ONITEMICON        = 0x0002
TVHT_ONITEMLABEL       = 0x0004
TVHT_ONITEMINDENT      = 0x0008
TVHT_ONITEMBUTTON      = 0x0010
TVHT_ONITEMRIGHT       = 0x0020
TVHT_ONITEMSTATEICON   = 0x0040

TVHT_ABOVE             = 0x0100
TVHT_BELOW             = 0x0200
TVHT_TORIGHT           = 0x0400
TVHT_TOLEFT            = 0x0800
TVHT_ONITEM            = (TVHT_ONITEMICON | TVHT_ONITEMLABEL | TVHT_ONITEMSTATEICON)


TVM_CREATEDRAGIMAGE     = (TV_FIRST + 18)

TVM_SORTCHILDREN        = (TV_FIRST + 19)

TVM_ENSUREVISIBLE       = (TV_FIRST + 20)

TVM_SORTCHILDRENCB      = (TV_FIRST + 21)

TVM_ENDEDITLABELNOW     = (TV_FIRST + 22)

TVM_GETISEARCHSTRINGA   = (TV_FIRST + 23)
TVM_GETISEARCHSTRINGW   = (TV_FIRST + 64)
TVM_GETISEARCHSTRING    = TVM_GETISEARCHSTRINGW

TVM_SETTOOLTIPS         = (TV_FIRST + 24)

TVM_GETTOOLTIPS         = (TV_FIRST + 25)

TVM_SETINSERTMARK       = (TV_FIRST + 26)

TVM_SETUNICODEFORMAT    = CCM_SETUNICODEFORMAT

TVM_GETUNICODEFORMAT    = CCM_GETUNICODEFORMAT

TVM_SETITEMHEIGHT              = (TV_FIRST + 27)

TVM_SETBKCOLOR                 = (TV_FIRST + 29)

TVM_SETTEXTCOLOR               = (TV_FIRST + 30)

TVM_GETBKCOLOR                 = (TV_FIRST + 31)

TVM_GETTEXTCOLOR               = (TV_FIRST + 32)

TVM_SETSCROLLTIME              = (TV_FIRST + 33)

TVM_GETSCROLLTIME              = (TV_FIRST + 34)

TVM_SETINSERTMARKCOLOR         = (TV_FIRST + 37)

TVM_GETINSERTMARKCOLOR         = (TV_FIRST + 38)

TVM_GETITEMSTATE               = (TV_FIRST + 39)

TVM_SETLINECOLOR               = (TV_FIRST + 40)

TVM_GETLINECOLOR               = (TV_FIRST + 41)

TVM_MAPACCIDTOHTREEITEM        = (TV_FIRST + 42)

TVM_MAPHTREEITEMTOACCID        = (TV_FIRST + 43)

TVM_SETEXTENDEDSTYLE           = (TV_FIRST + 44)

TVM_GETEXTENDEDSTYLE           = (TV_FIRST + 45)

TVM_SETAUTOSCROLLINFO          = (TV_FIRST + 59)

TVN_SELCHANGINGA        = (TVN_FIRST-1)
TVN_SELCHANGINGW        = (TVN_FIRST-50)
TVN_SELCHANGEDA         = (TVN_FIRST-2)
TVN_SELCHANGEDW         = (TVN_FIRST-51)

TVC_UNKNOWN            = 0x0000
TVC_BYMOUSE            = 0x0001
TVC_BYKEYBOARD         = 0x0002

TVN_GETDISPINFOA        = (TVN_FIRST-3)
TVN_GETDISPINFOW        = (TVN_FIRST-52)
TVN_SETDISPINFOA        = (TVN_FIRST-4)
TVN_SETDISPINFOW        = (TVN_FIRST-53)

TVIF_DI_SETITEM        = 0x1000


TVN_ITEMEXPANDINGA      = (TVN_FIRST-5)
TVN_ITEMEXPANDINGW      = (TVN_FIRST-54)
TVN_ITEMEXPANDEDA       = (TVN_FIRST-6)
TVN_ITEMEXPANDEDW       = (TVN_FIRST-55)
TVN_BEGINDRAGA          = (TVN_FIRST-7)
TVN_BEGINDRAGW          = (TVN_FIRST-56)
TVN_BEGINRDRAGA         = (TVN_FIRST-8)
TVN_BEGINRDRAGW         = (TVN_FIRST-57)
TVN_DELETEITEMA         = (TVN_FIRST-9)
TVN_DELETEITEMW         = (TVN_FIRST-58)
TVN_BEGINLABELEDITA     = (TVN_FIRST-10)
TVN_BEGINLABELEDITW     = (TVN_FIRST-59)
TVN_ENDLABELEDITA       = (TVN_FIRST-11)
TVN_ENDLABELEDITW       = (TVN_FIRST-60)
TVN_KEYDOWN             = (TVN_FIRST-12)
TVN_GETINFOTIPA         = (TVN_FIRST-13)
TVN_GETINFOTIPW         = (TVN_FIRST-14)
TVN_SINGLEEXPAND        = (TVN_FIRST-15)

TVNRET_DEFAULT          = 0
TVNRET_SKIPOLD          = 1
TVNRET_SKIPNEW          = 2

TVN_GETINFOTIP          = TVN_GETINFOTIPW

# treeview's customdraw return meaning don't draw images.  valid on CDRF_NOTIFYITEMPREPAINT
TVCDRF_NOIMAGES        = 0x00010000

##########  ComboBoxEx ################

WC_COMBOBOXEXW         = "ComboBoxEx32"
WC_COMBOBOXEXA         = WC_COMBOBOXEXW
WC_COMBOBOXEX          = WC_COMBOBOXEXW

CBEIF_TEXT             = 0x00000001
CBEIF_IMAGE            = 0x00000002
CBEIF_SELECTEDIMAGE    = 0x00000004
CBEIF_OVERLAY          = 0x00000008
CBEIF_INDENT           = 0x00000010
CBEIF_LPARAM           = 0x00000020

CBEIF_DI_SETITEM       = 0x10000000

CBEM_INSERTITEMA        = (WM_USER + 1)
CBEM_SETIMAGELIST       = (WM_USER + 2)
CBEM_GETIMAGELIST       = (WM_USER + 3)
CBEM_GETITEMA           = (WM_USER + 4)
CBEM_SETITEMA           = (WM_USER + 5)
CBEM_DELETEITEM         = CB_DELETESTRING
CBEM_GETCOMBOCONTROL    = (WM_USER + 6)
CBEM_GETEDITCONTROL     = (WM_USER + 7)
CBEM_SETEXSTYLE         = (WM_USER + 8)  # use  SETEXTENDEDSTYLE instead
CBEM_SETEXTENDEDSTYLE   = (WM_USER + 14)   # lparam == new style, wParam (optional) == mask
CBEM_GETEXSTYLE         = (WM_USER + 9) # use GETEXTENDEDSTYLE instead
CBEM_GETEXTENDEDSTYLE   = (WM_USER + 9)
CBEM_SETUNICODEFORMAT   = CCM_SETUNICODEFORMAT
CBEM_GETUNICODEFORMAT   = CCM_GETUNICODEFORMAT

CBEM_HASEDITCHANGED     = (WM_USER + 10)
CBEM_INSERTITEMW        = (WM_USER + 11)
CBEM_SETITEMW           = (WM_USER + 12)
CBEM_GETITEMW           = (WM_USER + 13)
CBEM_INSERTITEM         = CBEM_INSERTITEMW
CBEM_SETITEM            = CBEM_SETITEMW
CBEM_GETITEM            = CBEM_GETITEMW


CBEM_SETWINDOWTHEME     = CCM_SETWINDOWTHEME

CBES_EX_NOEDITIMAGE         = 0x00000001
CBES_EX_NOEDITIMAGEINDENT   = 0x00000002
CBES_EX_PATHWORDBREAKPROC   = 0x00000004
CBES_EX_NOSIZELIMIT         = 0x00000008

CBEN_GETDISPINFO         = (CBEN_FIRST - 0)


CBEN_GETDISPINFOA        = (CBEN_FIRST - 0)
CBEN_INSERTITEM          = (CBEN_FIRST - 1)
CBEN_DELETEITEM          = (CBEN_FIRST - 2)
CBEN_BEGINEDIT           = (CBEN_FIRST - 4)
CBEN_ENDEDITA            = (CBEN_FIRST - 5)
CBEN_ENDEDITW            = (CBEN_FIRST - 6)
CBEN_GETDISPINFOW        = (CBEN_FIRST - 7)
CBEN_DRAGBEGINA          = (CBEN_FIRST - 8)
CBEN_DRAGBEGINW          = (CBEN_FIRST - 9)
CBEN_DRAGBEGIN           = CBEN_DRAGBEGINW


CBEN_ENDEDIT             = CBEN_ENDEDITW

CBENF_KILLFOCUS          = 1
CBENF_RETURN             = 2
CBENF_ESCAPE             = 3
CBENF_DROPDOWN           = 4


#====== TAB CONTROL ==========================================================

WC_TABCONTROLA          = "SysTabControl32"
WC_TABCONTROLW          = WC_TABCONTROLA
WC_TABCONTROL           = WC_TABCONTROLW


# begin_r_commctrl

#if (_WIN32_IE >= 0x0300)
TCS_SCROLLOPPOSITE     = 0x0001   # assumes multiline tab
TCS_BOTTOM             = 0x0002
TCS_RIGHT              = 0x0002
TCS_MULTISELECT        = 0x0004  # allow multi-select in button mode
TCS_FLATBUTTONS        = 0x0008
TCS_FORCEICONLEFT      = 0x0010
TCS_FORCELABELLEFT     = 0x0020
TCS_HOTTRACK           = 0x0040
TCS_VERTICAL           = 0x0080
TCS_TABS               = 0x0000
TCS_BUTTONS            = 0x0100
TCS_SINGLELINE         = 0x0000
TCS_MULTILINE          = 0x0200
TCS_RIGHTJUSTIFY       = 0x0000
TCS_FIXEDWIDTH         = 0x0400
TCS_RAGGEDRIGHT        = 0x0800
TCS_FOCUSONBUTTONDOWN  = 0x1000
TCS_OWNERDRAWFIXED     = 0x2000
TCS_TOOLTIPS           = 0x4000
TCS_FOCUSNEVER         = 0x8000

# end_r_commctrl

#if (_WIN32_IE >= 0x0400)
# EX styles for use with TCM_SETEXTENDEDSTYLE
TCS_EX_FLATSEPARATORS  = 0x00000001
TCS_EX_REGISTERDROP    = 0x00000002


TCM_GETIMAGELIST        = (TCM_FIRST + 2)

TCM_SETIMAGELIST        = (TCM_FIRST + 3)

TCM_GETITEMCOUNT        = (TCM_FIRST + 4)

TCIF_TEXT              = 0x0001
TCIF_IMAGE             = 0x0002
TCIF_RTLREADING        = 0x0004
TCIF_PARAM             = 0x0008
TCIF_STATE             = 0x0010


TCIS_BUTTONPRESSED     = 0x0001
TCIS_HIGHLIGHTED       = 0x0002

class TCITEM(Structure):
    _fields__ = [ ('mask', UINT),
                 ('dwState', DWORD),
                 ('dwStateMask', DWORD),
                 ('pszText', LPWSTR),
                 ('cchTextMax',c_int),
                 ('iImage', c_int),
                 ('lParam',LPARAM)]

TC_ITEM = TCITEM

TCM_GETITEMA            = (TCM_FIRST + 5)
TCM_GETITEMW            = (TCM_FIRST + 60)
TCM_GETITEM             = TCM_GETITEMW


def TabCtrl_GetItem(hwnd, iItem, pitem):
    return SNDMSG(hwnd, TCM_GETITEM, iItem, pitem)

TCM_SETITEMA            = (TCM_FIRST + 6)
TCM_SETITEMW            = (TCM_FIRST + 61)
TCM_SETITEM             = TCM_SETITEMW

def TabCtrl_SetItem(hwnd, index, pitem):
    return SNDMSG(hwnd, TCM_SETITEM, index, pitem)

TCM_INSERTITEMA         = (TCM_FIRST + 7)
TCM_INSERTITEMW         = (TCM_FIRST + 62)
TCM_INSERTITEM          = TCM_INSERTITEMW

def TabCtrl_InsertItem(hwnd, index, pitem):
    return SNDMSG(hwnd, TCM_INSERTITEM, index, pitem)

TCM_DELETEITEM          = (TCM_FIRST + 8)

TCM_DELETEALLITEMS      = (TCM_FIRST + 9)

TCM_GETITEMRECT         = (TCM_FIRST + 10)

def TabCtrl_GetItemRect(hwnd, i, prc):
    return SNDMSG(hwnd, TCM_GETITEMRECT, i, prc)

TCM_GETCURSEL           = (TCM_FIRST + 11)

TCM_SETCURSEL           = (TCM_FIRST + 12)

TCHT_NOWHERE           = 0x0001
TCHT_ONITEMICON        = 0x0002
TCHT_ONITEMLABEL       = 0x0004
TCHT_ONITEM            = (TCHT_ONITEMICON | TCHT_ONITEMLABEL)

TCM_HITTEST             = (TCM_FIRST + 13)

TCM_SETITEMEXTRA        = (TCM_FIRST + 14)

TCM_ADJUSTRECT          = (TCM_FIRST + 40)

TCM_SETITEMSIZE         = (TCM_FIRST + 41)

TCM_REMOVEIMAGE         = (TCM_FIRST + 42)

TCM_SETPADDING          = (TCM_FIRST + 43)

TCM_GETROWCOUNT         = (TCM_FIRST + 44)

TCM_GETTOOLTIPS         = (TCM_FIRST + 45)

TCM_SETTOOLTIPS         = (TCM_FIRST + 46)

TCM_GETCURFOCUS         = (TCM_FIRST + 47)

TCM_SETCURFOCUS         = (TCM_FIRST + 48)

TCM_SETMINTABWIDTH      = (TCM_FIRST + 49)

TCM_DESELECTALL         = (TCM_FIRST + 50)

TCM_HIGHLIGHTITEM       = (TCM_FIRST + 51)

TCM_SETEXTENDEDSTYLE    = (TCM_FIRST + 52)  # optional wParam == mask

TCM_GETEXTENDEDSTYLE    = (TCM_FIRST + 53)

TCM_SETUNICODEFORMAT    = CCM_SETUNICODEFORMAT

TCM_GETUNICODEFORMAT    = CCM_GETUNICODEFORMAT

TCN_KEYDOWN             = (TCN_FIRST - 0)

TCN_SELCHANGE           = (TCN_FIRST - 1)
TCN_SELCHANGING         = (TCN_FIRST - 2)
TCN_GETOBJECT           = (TCN_FIRST - 3)
TCN_FOCUSCHANGE         = (TCN_FIRST - 4)


#====== ANIMATE CONTROL ======================================================

ANIMATE_CLASSW          = "SysAnimate32"
ANIMATE_CLASSA          = ANIMATE_CLASSW
ANIMATE_CLASS           = ANIMATE_CLASSW

# begin_r_commctrl

ACS_CENTER             = 0x0001
ACS_TRANSPARENT        = 0x0002
ACS_AUTOPLAY           = 0x0004
ACS_TIMER              = 0x0008  # don't use threads... use timers

# end_r_commctrl

ACM_OPENA               = (WM_USER+100)
ACM_OPENW               = (WM_USER+103)
ACM_OPEN                = ACM_OPENW

ACM_PLAY                = (WM_USER+101)
ACM_STOP                = (WM_USER+102)
ACM_ISPLAYING           = (WM_USER+104)

ACN_START               = 1
ACN_STOP                = 2

#====== MONTHCAL CONTROL ======================================================

MONTHCAL_CLASSW          = "SysMonthCal32"
MONTHCAL_CLASSA          = MONTHCAL_CLASSW
MONTHCAL_CLASS           = MONTHCAL_CLASSW

MCM_FIRST          = 0x1000

# BOOL MonthCal_GetCurSel(HWND hmc, LPSYSTEMTIME pst)
#   returns FALSE if MCS_MULTISELECT
#   returns TRUE and sets *pst to the currently selected date otherwise
MCM_GETCURSEL       = (MCM_FIRST + 1)

# ====================== Button Control =============================


# Button Class Name
WC_BUTTONA              = "Button"
WC_BUTTONW              = WC_BUTTONA
WC_BUTTON               = WC_BUTTONW

BUTTON_IMAGELIST_ALIGN_LEFT     = 0
BUTTON_IMAGELIST_ALIGN_RIGHT    = 1
BUTTON_IMAGELIST_ALIGN_TOP      = 2
BUTTON_IMAGELIST_ALIGN_BOTTOM   = 3
BUTTON_IMAGELIST_ALIGN_CENTER   = 4       # Doesn't draw text

BCM_GETIDEALSIZE        = (BCM_FIRST + 0x0001)

BCM_SETIMAGELIST        = (BCM_FIRST + 0x0002)

BCM_GETIMAGELIST        = (BCM_FIRST + 0x0003)

BCM_SETTEXTMARGIN       = (BCM_FIRST + 0x0004)

BCM_GETTEXTMARGIN       = (BCM_FIRST + 0x0005)

BCN_HOTITEMCHANGE       = (BCN_FIRST + 0x0001)

BST_HOT           = 0x0200

# ====================== Static Control =============================


# Static Class Name
WC_STATICA              = "Static"
WC_STATICW              = WC_STATICA
WC_STATIC               = WC_STATICW

# =====================  End Static Control =========================

# ====================== Edit Control =============================

# Edit Class Name
WC_EDITA                = "Edit"
WC_EDITW                = WC_EDITA
WC_EDIT                 = WC_EDITW

EM_SETCUEBANNER     = (ECM_FIRST + 1)     # Set the cue banner with the lParm = LPCWSTR

EM_GETCUEBANNER     = (ECM_FIRST + 2)     # Set the cue banner with the lParm = LPCWSTR

EM_SHOWBALLOONTIP   = (ECM_FIRST + 3)     # Show a balloon tip associated to the edit control

EM_HIDEBALLOONTIP   = (ECM_FIRST + 4)     # Hide any balloon tip associated with the edit control

# =====================  End Edit Control =========================

# ====================== Listbox Control =============================

# Listbox Class Name
WC_LISTBOXA             = "ListBox"
WC_LISTBOXW             = WC_LISTBOXA
WC_LISTBOX              = WC_LISTBOXW


# =====================  End Listbox Control =========================

# ====================== Combobox Control =============================
# Combobox Class Name
WC_COMBOBOXA            = "ComboBox"
WC_COMBOBOXW            = WC_COMBOBOXA
WC_COMBOBOX             = WC_COMBOBOXW

# custom combobox control messages
CB_SETMINVISIBLE        = (CBM_FIRST + 1)
CB_GETMINVISIBLE        = (CBM_FIRST + 2)
CB_SETCUEBANNER         = (CBM_FIRST + 3)
CB_GETCUEBANNER         = (CBM_FIRST + 4)


# =====================  End Combobox Control =========================

# ====================== Scrollbar Control ============================
WC_SCROLLBARA            = "ScrollBar"
WC_SCROLLBARW            = WC_SCROLLBARA
WC_SCROLLBAR             = WC_SCROLLBARW
# ===================== End Scrollbar Control =========================

# ===================== Task Dialog =========================

#
#====== Dynamic Array routines ==========================================
#
# Note that the STL and other libraries have similar functionality.
# The routines here are specific to Windows and may not be as convenient
# or fully functional as those in other libraries.
#

DA_LAST         = (0x7FFFFFFF)
DA_ERR          = (-1)

# Merge two DPAs.  This takes two (optionally) presorted arrays and merges
# the source array into the dest.  DPA_Merge uses the provided callbacks
# to perform comparison and merge operations.  The merge callback is
# called when two elements (one in each list) match according to the
# compare function.  This allows portions of an element in one list to
# be merged with the respective element in the second list.
#
# The first DPA (hdpaDest) is the output array.
#
# Merge options:
#
#    DPAM_SORTED       The arrays are already sorted; don't sort
#    DPAM_UNION        The resulting array is the union of all elements
#                      in both arrays (DPAMM_INSERT may be sent for
#                      this merge option.)
#    DPAM_INTERSECT    Only elements in the source array that intersect
#                      with the dest array are merged.  (DPAMM_DELETE
#                      may be sent for this merge option.)
#    DPAM_NORMAL       Like DPAM_INTERSECT except the dest array
#                      also maintains its original, additional elements.
#
DPAM_SORTED            = 0x00000001
DPAM_NORMAL            = 0x00000002
DPAM_UNION             = 0x00000004
DPAM_INTERSECT         = 0x00000008


# Messages for merge callback
DPAMM_MERGE     = 1
DPAMM_DELETE    = 2
DPAMM_INSERT    = 3

#
# Search array.  If DPAS_SORTED, then array is assumed to be sorted
# according to pfnCompare, and binary search algorithm is used.
# Otherwise, linear search is used.
#
# Searching starts at iStart (0 to start search at beginning).
#
# DPAS_INSERTBEFORE/AFTER govern what happens if an exact match is not
# found.  If neither are specified, this function returns -1 if no exact
# match is found.  Otherwise, the index of the item before or after the
# closest (including exact) match is returned.
#
# Search option flags
#
DPAS_SORTED            = 0x0001
DPAS_INSERTBEFORE      = 0x0002
DPAS_INSERTAFTER       = 0x0004

#
# If the messages for TrackMouseEvent have not been defined then define them
# now.
#
#ifndef WM_MOUSEHOVER
WM_MOUSEHOVER                  = 0x02A1
WM_MOUSELEAVE                  = 0x02A3

WSB_PROP_CYVSCROLL = 0x00000001L
WSB_PROP_CXHSCROLL = 0x00000002L
WSB_PROP_CYHSCROLL = 0x00000004L
WSB_PROP_CXVSCROLL = 0x00000008L
WSB_PROP_CXHTHUMB  = 0x00000010L
WSB_PROP_CYVTHUMB  = 0x00000020L
WSB_PROP_VBKGCOLOR = 0x00000040L
WSB_PROP_HBKGCOLOR = 0x00000080L
WSB_PROP_VSTYLE    = 0x00000100L
WSB_PROP_HSTYLE    = 0x00000200L
WSB_PROP_WINSTYLE  = 0x00000400L
WSB_PROP_PALETTE   = 0x00000800L
WSB_PROP_MASK      = 0x00000FFFL

FSB_FLAT_MODE           = 2
FSB_ENCARTA_MODE        = 1
FSB_REGULAR_MODE        = 0


