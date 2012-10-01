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
Created on 27/03/2012

@author: Luis Ariel Vega Soliz
'''

from ctypes import *
from uadh.gui.mfc.lib.winuser import WM_USER


# AppBar stuff

ABM_NEW           = 0x00000000
ABM_REMOVE        = 0x00000001
ABM_QUERYPOS      = 0x00000002
ABM_SETPOS        = 0x00000003
ABM_GETSTATE      = 0x00000004
ABM_GETTASKBARPOS = 0x00000005
ABM_ACTIVATE      = 0x00000006  # lParam == TRUE/FALSE means activate/deactivate
ABM_GETAUTOHIDEBAR = 0x00000007
ABM_SETAUTOHIDEBAR = 0x00000008  # this can fail at any time.  MUST check the result
                                        # lParam = TRUE/FALSE  Set/Unset
                                        # uEdge = what edge
ABM_WINDOWPOSCHANGED = 0x0000009


ABM_SETSTATE         = 0x0000000a

# these are put in the wparam of callback messages
ABN_STATECHANGE    = 0x0000000
ABN_POSCHANGED     = 0x0000001
ABN_FULLSCREENAPP  = 0x0000002
ABN_WINDOWARRANGE  = 0x0000003 # lParam == TRUE means hide

# flags for get state
ABS_AUTOHIDE    = 0x0000001
ABS_ALWAYSONTOP = 0x0000002

ABE_LEFT        = 0
ABE_TOP         = 1
ABE_RIGHT       = 2
ABE_BOTTOM      = 3

# Shell File Operations

FO_MOVE                    = 0x0001
FO_COPY                    = 0x0002
FO_DELETE                  = 0x0003
FO_RENAME                  = 0x0004

# SHFILEOPSTRUCT.fFlags and IFileOperation::SetOperationFlags() flag values

FOF_MULTIDESTFILES         = 0x0001
FOF_CONFIRMMOUSE           = 0x0002
FOF_SILENT                 = 0x0004  # don't display progress UI (confirm prompts may be displayed still)
FOF_RENAMEONCOLLISION      = 0x0008  # automatically rename the source files to avoid the collisions
FOF_NOCONFIRMATION         = 0x0010  # don't display confirmation UI, assume "yes" for cases that can be bypassed, "no" for those that can not
FOF_WANTMAPPINGHANDLE      = 0x0020  # Fill in SHFILEOPSTRUCT.hNameMappings. Must be freed using SHFreeNameMappings
FOF_ALLOWUNDO              = 0x0040  # enable undo including Recycle behavior for IFileOperation::Delete()
FOF_FILESONLY              = 0x0080  # only operate on the files (non folders), both files and folders are assumed without this
FOF_SIMPLEPROGRESS         = 0x0100  # means don't show names of files
FOF_NOCONFIRMMKDIR         = 0x0200  # don't dispplay confirmatino UI before making any needed directories, assume "Yes" in these cases
FOF_NOERRORUI              = 0x0400  # don't put up error UI, other UI may be displayed, progress, confirmations


FOF_NOCOPYSECURITYATTRIBS  = 0x0800  # dont copy file security attributes (ACLs)
FOF_NORECURSION            = 0x1000  # don't recurse into directories for operations that would recurse
FOF_NO_CONNECTED_ELEMENTS  = 0x2000  # don't operate on connected elements ("xxx_files" folders that go with .htm files)
FOF_WANTNUKEWARNING        = 0x4000  # during delete operation, warn if nuking instead of recycling (partially overrides FOF_NOCONFIRMATION)


FOF_NORECURSEREPARSE       = 0x8000  # deprecated; the operations engine always does the right thing on FolderLink objects (symlinks, reparse points, folder shortcuts)

FOF_NO_UI                  = (FOF_SILENT | FOF_NOCONFIRMATION | FOF_NOERRORUI | FOF_NOCONFIRMMKDIR) # don't display any UI at all

PO_DELETE       = 0x0013  # printer is being deleted
PO_RENAME       = 0x0014  # printer is being renamed
PO_PORTCHANGE   = 0x0020  # port this printer connected to is being changed
                                # if this id is set, the strings received by
                                # the copyhook are a doubly-null terminated
                                # list of strings.  The first is the printer
                                # name and the second is the printer port.
PO_REN_PORT     = 0x0034  # PO_RENAME and PO_PORTCHANGE at same time.


# ShellExecute() and ShellExecuteEx() error codes

# regular WinExec() codes
SE_ERR_FNF              = 2       # file not found
SE_ERR_PNF              = 3       # path not found
SE_ERR_ACCESSDENIED     = 5       # access denied
SE_ERR_OOM              = 8       # out of memory
SE_ERR_DLLNOTFOUND      = 32

# error values for ShellExecute() beyond the regular WinExec() codes
SE_ERR_SHARE                    = 26
SE_ERR_ASSOCINCOMPLETE          = 27
SE_ERR_DDETIMEOUT               = 28
SE_ERR_DDEFAIL                  = 29
SE_ERR_DDEBUSY                  = 30
SE_ERR_NOASSOC                  = 31

# Note CLASSKEY overrides CLASSNAME
SEE_MASK_DEFAULT           = 0x00000000
SEE_MASK_CLASSNAME         = 0x00000001   # SHELLEXECUTEINFO.lpClass is valid
SEE_MASK_CLASSKEY          = 0x00000003   # SHELLEXECUTEINFO.hkeyClass is valid
# Note SEE_MASK_INVOKEIDLIST(0xC) implies SEE_MASK_IDLIST(0x04)
SEE_MASK_IDLIST            = 0x00000004   # SHELLEXECUTEINFO.lpIDList is valid
SEE_MASK_INVOKEIDLIST      = 0x0000000c   # enable IContextMenu based verbs


SEE_MASK_ICON              = 0x00000010   # not used
SEE_MASK_HOTKEY            = 0x00000020   # SHELLEXECUTEINFO.dwHotKey is valid
SEE_MASK_NOCLOSEPROCESS    = 0x00000040   # SHELLEXECUTEINFO.hProcess
SEE_MASK_CONNECTNETDRV     = 0x00000080   # enables re-connecting disconnected network drives
SEE_MASK_NOASYNC           = 0x00000100   # block on the call until the invoke has completed, use for callers that exit after calling ShellExecuteEx()
SEE_MASK_FLAG_DDEWAIT      = SEE_MASK_NOASYNC # Use SEE_MASK_NOASYNC instead of SEE_MASK_FLAG_DDEWAIT as it more accuratly describes the behavior
SEE_MASK_DOENVSUBST        = 0x00000200   # indicates that SHELLEXECUTEINFO.lpFile contains env vars that should be expanded
SEE_MASK_FLAG_NO_UI        = 0x00000400   # disable UI including error messages
SEE_MASK_UNICODE           = 0x00004000
SEE_MASK_NO_CONSOLE        = 0x00008000
SEE_MASK_ASYNCOK           = 0x00100000

SEE_MASK_HMONITOR          = 0x00200000   # SHELLEXECUTEINFO.hMonitor

SEE_MASK_NOQUERYCLASSSTORE = 0x01000000
SEE_MASK_WAITFORINPUTIDLE  = 0x02000000


SEE_MASK_FLAG_LOG_USAGE    = 0x04000000


# flags for SHEmptyRecycleBin

SHERB_NOCONFIRMATION    = 0x00000001
SHERB_NOPROGRESSUI      = 0x00000002
SHERB_NOSOUND           = 0x00000004

NIN_SELECT          = (WM_USER + 0)
NINF_KEY            = 0x1
NIN_KEYSELECT       = (NIN_SELECT | NINF_KEY)

NIN_BALLOONSHOW         = (WM_USER + 2)
NIN_BALLOONHIDE         = (WM_USER + 3)
NIN_BALLOONTIMEOUT      = (WM_USER + 4)
NIN_BALLOONUSERCLICK    = (WM_USER + 5)


NIM_ADD         = 0x00000000
NIM_MODIFY      = 0x00000001
NIM_DELETE      = 0x00000002

NIM_SETFOCUS    = 0x00000003
NIM_SETVERSION  = 0x00000004


# set NOTIFYICONDATA.uVersion with 0, 3 or 4
# please read the documentation on the behavior difference that the different versions imply
NOTIFYICON_VERSION      = 3

NIF_MESSAGE     = 0x00000001
NIF_ICON        = 0x00000002
NIF_TIP         = 0x00000004


NIF_STATE       = 0x00000008
NIF_INFO        = 0x00000010


NIF_GUID        = 0x00000020

NIS_HIDDEN              = 0x00000001
NIS_SHAREDICON          = 0x00000002
# says this is the source of a shared icon

# Notify Icon Infotip flags
NIIF_NONE       = 0x00000000
# icon flags are mutually exclusive
# and take only the lowest 2 bits
NIIF_INFO       = 0x00000001
NIIF_WARNING    = 0x00000002
NIIF_ERROR      = 0x00000003

NIIF_USER       = 0x00000004

NIIF_ICON_MASK  = 0x0000000F

NIIF_NOSOUND    = 0x00000010

SHGFI_ICON              = 0x000000100     # get icon
SHGFI_DISPLAYNAME       = 0x000000200     # get display name
SHGFI_TYPENAME          = 0x000000400     # get type name
SHGFI_ATTRIBUTES        = 0x000000800     # get attributes
SHGFI_ICONLOCATION      = 0x000001000     # get icon location
SHGFI_EXETYPE           = 0x000002000     # return exe type
SHGFI_SYSICONINDEX      = 0x000004000     # get system icon index
SHGFI_LINKOVERLAY       = 0x000008000     # put a link overlay on icon
SHGFI_SELECTED          = 0x000010000     # show icon in selected state


SHGFI_ATTR_SPECIFIED    = 0x000020000     # get only specified attributes

SHGFI_LARGEICON         = 0x000000000     # get large icon
SHGFI_SMALLICON         = 0x000000001     # get small icon
SHGFI_OPENICON          = 0x000000002     # get open icon
SHGFI_SHELLICONSIZE     = 0x000000004     # get shell size icon
SHGFI_PIDL              = 0x000000008     # pszPath is a pidl
SHGFI_USEFILEATTRIBUTES = 0x000000010     # use passed dwFileAttribute


SHGFI_ADDOVERLAYS       = 0x000000020     # apply the appropriate overlays
SHGFI_OVERLAYINDEX      = 0x000000040     # Get the index of the overlay


SHGNLI_PIDL             = 0x000000001     # pszLinkTo is a pidl
SHGNLI_PREFIXNAME       = 0x000000002     # Make name "Shortcut to xxx"
SHGNLI_NOUNIQUE         = 0x000000004     # don't do the unique name generation


SHGNLI_NOLNK            = 0x000000008     # don't add ".lnk" extension

SHGNLI_NOLOCNAME        = 0x000000010     # use non localized (parsing) name from the target

PRINTACTION_OPEN                = 0        # pszBuf1:<PrinterName>
PRINTACTION_PROPERTIES          = 1        # pszBuf1:<PrinterName>, pszBuf2:optional <PageName>
PRINTACTION_NETINSTALL          = 2        # pszBuf1:<NetPrinterName>
PRINTACTION_NETINSTALLLINK      = 3        # pszBuf1:<NetPrinterName>, pszBuf2:<path to store link>
PRINTACTION_TESTPAGE            = 4        # pszBuf1:<PrinterName>
PRINTACTION_OPENNETPRN          = 5        # pszBuf1:<NetPrinterName>
PRINTACTION_DOCUMENTDEFAULTS    = 6      # pszBuf1:<PrinterName>
PRINTACTION_SERVERPROPERTIES    = 7      # pszBuf1:<Server> or <NetPrinterName>

OFFLINE_STATUS_LOCAL        = 0x0001  # If open, it's open locally
OFFLINE_STATUS_REMOTE       = 0x0002  # If open, it's open remotely
OFFLINE_STATUS_INCOMPLETE   = 0x0004  # The local copy is currently imcomplete.
                                            # The file will not be available offline
                                            # until it has been synchronized.


SHIL_LARGE          = 0   # normally 32x32
SHIL_SMALL          = 1   # normally 16x16
SHIL_EXTRALARGE     = 2
SHIL_SYSSMALL       = 3   # like SHIL_SMALL, but tracks system small icon metric correctly


SHIL_LAST           = SHIL_SYSSMALL