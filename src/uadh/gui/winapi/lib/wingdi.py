'''
Created on 27/03/2012

@author: xXx
'''
from uadh.gui.winapi.lib import auxfuncs
from ctypes import windll, c_int
from ctypes.wintypes import DWORD, LPCSTR, HDC, HGDIOBJ



#Binary raster ops 
R2_BLACK            = 1   # 0       
R2_NOTMERGEPEN      = 2   #DPon     
R2_MASKNOTPEN       = 3   #DPna     
R2_NOTCOPYPEN       = 4   #PN       
R2_MASKPENNOT       = 5   #PDna     
R2_NOT              = 6   #Dn       
R2_XORPEN           = 7   #DPx      
R2_NOTMASKPEN       = 8   #DPan     
R2_MASKPEN          = 9   #DPa      
R2_NOTXORPEN        = 10  #DPxn     
R2_NOP              = 11  #D        
R2_MERGENOTPEN      = 12  #DPno     
R2_COPYPEN          = 13  #P        
R2_MERGEPENNOT      = 14  #PDno     
R2_MERGEPEN         = 15  #DPo      
R2_WHITE            = 16  # 1       
R2_LAST             = 16

#Ternary raster operations 
SRCCOPY             = 0x00CC0020 #dest = source                   
SRCPAINT            = 0x00EE0086 #dest = source OR dest           
SRCAND              = 0x008800C6 #dest = source AND dest          
SRCINVERT           = 0x00660046 #dest = source XOR dest          
SRCERASE            = 0x00440328 #dest = source AND (NOT dest )   
NOTSRCCOPY          = 0x00330008 #dest = (NOT source)             
NOTSRCERASE         = 0x001100A6 #dest = (NOT src) AND (NOT dest) 
MERGECOPY           = 0x00C000CA #dest = (source AND pattern)     
MERGEPAINT          = 0x00BB0226 #dest = (NOT source) OR dest     
PATCOPY             = 0x00F00021 #dest = pattern                  
PATPAINT            = 0x00FB0A09 #dest = DPSnoo                   
PATINVERT           = 0x005A0049 #dest = pattern XOR dest         
DSTINVERT           = 0x00550009 #dest = (NOT dest)               
BLACKNESS           = 0x00000042 #dest = BLACK                    
WHITENESS           = 0x00FF0062 #dest = WHITE                    
NOMIRRORBITMAP      = auxfuncs.safe_long(0x80000000) #Do not Mirror the bitmap in this call 
CAPTUREBLT          = 0x40000000 #Include layered windows 
GDI_ERROR           = 0xFFFFFFFFL
HGDI_ERROR          = 0xFFFFFFFFL
#Region Flags 
ERROR               = 0
NULLREGION          = 1
SIMPLEREGION        = 2
COMPLEXREGION       = 3
RGN_ERROR           = ERROR

#CombineRgn() Styles 
RGN_AND             = 1
RGN_OR              = 2
RGN_XOR             = 3
RGN_DIFF            = 4
RGN_COPY            = 5
RGN_MIN             = RGN_AND
RGN_MAX             = RGN_COPY

#StretchBlt() Modes 
BLACKONWHITE                 = 1
WHITEONBLACK                 = 2
COLORONCOLOR                 = 3
HALFTONE                     = 4
MAXSTRETCHBLTMODE            = 4
#New StretchBlt() Modes 
STRETCH_ANDSCANS             = BLACKONWHITE
STRETCH_ORSCANS              = WHITEONBLACK
STRETCH_DELETESCANS          = COLORONCOLOR
STRETCH_HALFTONE             = HALFTONE


#PolyFill() Modes 
ALTERNATE                    = 1
WINDING                      = 2
POLYFILL_LAST                = 2

#Layout Orientation Options 
LAYOUT_RTL                         = 0x00000001 # Right to left
LAYOUT_BTT                         = 0x00000002 # Bottom to top
LAYOUT_VBH                         = 0x00000004 # Vertical before horizontal
LAYOUT_ORIENTATIONMASK             = (LAYOUT_RTL | LAYOUT_BTT | LAYOUT_VBH)
LAYOUT_BITMAPORIENTATIONPRESERVED  = 0x00000008
#Text Alignment Options 
TA_NOUPDATECP                = 0
TA_UPDATECP                  = 1

TA_LEFT                      = 0
TA_RIGHT                     = 2
TA_CENTER                    = 6

TA_TOP                       = 0
TA_BOTTOM                    = 8
TA_BASELINE                  = 24
TA_RTLREADING                = 256
TA_MASK                      = (TA_BASELINE+TA_CENTER+TA_UPDATECP+TA_RTLREADING)
VTA_BASELINE                 = TA_BASELINE
VTA_LEFT                     = TA_BOTTOM
VTA_RIGHT                    = TA_TOP
VTA_CENTER                   = TA_CENTER
VTA_BOTTOM                   = TA_RIGHT
VTA_TOP                      = TA_LEFT

ETO_OPAQUE                   = 0x0002
ETO_CLIPPED                  = 0x0004
ETO_GLYPH_INDEX              = 0x0010
ETO_RTLREADING               = 0x0080
ETO_NUMERICSLOCAL            = 0x0400
ETO_NUMERICSLATIN            = 0x0800
ETO_IGNORELANGUAGE           = 0x1000

ETO_PDY                      = 0x2000
ASPECT_FILTERING             = 0x0001

#Bounds Accumulation APIs 

DCB_RESET       = 0x0001
DCB_ACCUMULATE  = 0x0002
DCB_DIRTY       = DCB_ACCUMULATE
DCB_SET         = (DCB_RESET | DCB_ACCUMULATE)
DCB_ENABLE      = 0x0004
DCB_DISABLE     = 0x0008
#Metafile Functions 
META_SETBKCOLOR              = 0x0201
META_SETBKMODE               = 0x0102
META_SETMAPMODE              = 0x0103
META_SETROP2                 = 0x0104
META_SETRELABS               = 0x0105
META_SETPOLYFILLMODE         = 0x0106
META_SETSTRETCHBLTMODE       = 0x0107
META_SETTEXTCHAREXTRA        = 0x0108
META_SETTEXTCOLOR            = 0x0209
META_SETTEXTJUSTIFICATION    = 0x020A
META_SETWINDOWORG            = 0x020B
META_SETWINDOWEXT            = 0x020C
META_SETVIEWPORTORG          = 0x020D
META_SETVIEWPORTEXT          = 0x020E
META_OFFSETWINDOWORG         = 0x020F
META_SCALEWINDOWEXT          = 0x0410
META_OFFSETVIEWPORTORG       = 0x0211
META_SCALEVIEWPORTEXT        = 0x0412
META_LINETO                  = 0x0213
META_MOVETO                  = 0x0214
META_EXCLUDECLIPRECT         = 0x0415
META_INTERSECTCLIPRECT       = 0x0416
META_ARC                     = 0x0817
META_ELLIPSE                 = 0x0418
META_FLOODFILL               = 0x0419
META_PIE                     = 0x081A
META_RECTANGLE               = 0x041B
META_ROUNDRECT               = 0x061C
META_PATBLT                  = 0x061D
META_SAVEDC                  = 0x001E
META_SETPIXEL                = 0x041F
META_OFFSETCLIPRGN           = 0x0220
META_TEXTOUT                 = 0x0521
META_BITBLT                  = 0x0922
META_STRETCHBLT              = 0x0B23
META_POLYGON                 = 0x0324
META_POLYLINE                = 0x0325
META_ESCAPE                  = 0x0626
META_RESTOREDC               = 0x0127
META_FILLREGION              = 0x0228
META_FRAMEREGION             = 0x0429
META_INVERTREGION            = 0x012A
META_PAINTREGION             = 0x012B
META_SELECTCLIPREGION        = 0x012C
META_SELECTOBJECT            = 0x012D
META_SETTEXTALIGN            = 0x012E
META_CHORD                   = 0x0830
META_SETMAPPERFLAGS          = 0x0231
META_EXTTEXTOUT              = 0x0a32
META_SETDIBTODEV             = 0x0d33
META_SELECTPALETTE           = 0x0234
META_REALIZEPALETTE          = 0x0035
META_ANIMATEPALETTE          = 0x0436
META_SETPALENTRIES           = 0x0037
META_POLYPOLYGON             = 0x0538
META_RESIZEPALETTE           = 0x0139
META_DIBBITBLT               = 0x0940
META_DIBSTRETCHBLT           = 0x0b41
META_DIBCREATEPATTERNBRUSH   = 0x0142
META_STRETCHDIB              = 0x0f43
META_EXTFLOODFILL            = 0x0548

META_SETLAYOUT               = 0x0149
META_DELETEOBJECT            = 0x01f0
META_CREATEPALETTE           = 0x00f7
META_CREATEPATTERNBRUSH      = 0x01F9
META_CREATEPENINDIRECT       = 0x02FA
META_CREATEFONTINDIRECT      = 0x02FB
META_CREATEBRUSHINDIRECT     = 0x02FC
META_CREATEREGION            = 0x06FF

#GDI Escapes 
NEWFRAME                     = 1
ABORTDOC                     = 2
NEXTBAND                     = 3
SETCOLORTABLE                = 4
GETCOLORTABLE                = 5
FLUSHOUTPUT                  = 6
DRAFTMODE                    = 7
QUERYESCSUPPORT              = 8
SETABORTPROC                 = 9
STARTDOC                     = 10
ENDDOC                       = 11
GETPHYSPAGESIZE              = 12
GETPRINTINGOFFSET            = 13
GETSCALINGFACTOR             = 14
MFCOMMENT                    = 15
GETPENWIDTH                  = 16
SETCOPYCOUNT                 = 17
SELECTPAPERSOURCE            = 18
DEVICEDATA                   = 19
PASSTHROUGH                  = 19
GETTECHNOLGY                 = 20
GETTECHNOLOGY                = 20
SETLINECAP                   = 21
SETLINEJOIN                  = 22
SETMITERLIMIT                = 23
BANDINFO                     = 24
DRAWPATTERNRECT              = 25
GETVECTORPENSIZE             = 26
GETVECTORBRUSHSIZE           = 27
ENABLEDUPLEX                 = 28
GETSETPAPERBINS              = 29
GETSETPRINTORIENT            = 30
ENUMPAPERBINS                = 31
SETDIBSCALING                = 32
EPSPRINTING                  = 33
ENUMPAPERMETRICS             = 34
GETSETPAPERMETRICS           = 35
POSTSCRIPT_DATA              = 37
POSTSCRIPT_IGNORE            = 38
MOUSETRAILS                  = 39
GETDEVICEUNITS               = 42

GETEXTENDEDTEXTMETRICS       = 256
GETEXTENTTABLE               = 257
GETPAIRKERNTABLE             = 258
GETTRACKKERNTABLE            = 259
EXTTEXTOUT                   = 512
GETFACENAME                  = 513
DOWNLOADFACE                 = 514
ENABLERELATIVEWIDTHS         = 768
ENABLEPAIRKERNING            = 769
SETKERNTRACK                 = 770
SETALLJUSTVALUES             = 771
SETCHARSET                   = 772

STRETCHBLT                   = 2048
METAFILE_DRIVER              = 2049
GETSETSCREENPARAMS           = 3072
QUERYDIBSUPPORT              = 3073
BEGIN_PATH                   = 4096
CLIP_TO_PATH                 = 4097
END_PATH                     = 4098
EXT_DEVICE_CAPS              = 4099
RESTORE_CTM                  = 4100
SAVE_CTM                     = 4101
SET_ARC_DIRECTION            = 4102
SET_BACKGROUND_COLOR         = 4103
SET_POLY_MODE                = 4104
SET_SCREEN_ANGLE             = 4105
SET_SPREAD                   = 4106
TRANSFORM_CTM                = 4107
SET_CLIP_BOX                 = 4108
SET_BOUNDS                   = 4109
SET_MIRROR_MODE              = 4110
OPENCHANNEL                  = 4110
DOWNLOADHEADER               = 4111
CLOSECHANNEL                 = 4112
POSTSCRIPT_PASSTHROUGH       = 4115
ENCAPSULATED_POSTSCRIPT      = 4116

POSTSCRIPT_IDENTIFY          = 4117   #new escape for NT5 pscript driver 
POSTSCRIPT_INJECTION         = 4118   #new escape for NT5 pscript driver 

CHECKJPEGFORMAT              = 4119
CHECKPNGFORMAT               = 4120

GET_PS_FEATURESETTING        = 4121   #new escape for NT5 pscript driver 

GDIPLUS_TS_QUERYVER          = 4122   #private escape 
GDIPLUS_TS_RECORD            = 4123   #private escape 


#Return Values for MILCORE_TS_QUERYVER


SPCLPASSTHROUGH2             = 4568   #new escape for NT5 pscript driver 


#Parameters for POSTSCRIPT_IDENTIFY escape


PSIDENT_GDICENTRIC    = 0
PSIDENT_PSCENTRIC     = 1


#Constants for PSINJECTDATA.InjectionPoint field


PSINJECT_BEGINSTREAM                = 1
PSINJECT_PSADOBE                    = 2
PSINJECT_PAGESATEND                 = 3
PSINJECT_PAGES                      = 4

PSINJECT_DOCNEEDEDRES               = 5
PSINJECT_DOCSUPPLIEDRES             = 6
PSINJECT_PAGEORDER                  = 7
PSINJECT_ORIENTATION                = 8
PSINJECT_BOUNDINGBOX                = 9
PSINJECT_DOCUMENTPROCESSCOLORS      = 10

PSINJECT_COMMENTS                   = 11
PSINJECT_BEGINDEFAULTS              = 12
PSINJECT_ENDDEFAULTS                = 13
PSINJECT_BEGINPROLOG                = 14
PSINJECT_ENDPROLOG                  = 15
PSINJECT_BEGINSETUP                 = 16
PSINJECT_ENDSETUP                   = 17
PSINJECT_TRAILER                    = 18
PSINJECT_EOF                        = 19
PSINJECT_ENDSTREAM                  = 20
PSINJECT_DOCUMENTPROCESSCOLORSATEND = 21

PSINJECT_PAGENUMBER                 = 100
PSINJECT_BEGINPAGESETUP             = 101
PSINJECT_ENDPAGESETUP               = 102
PSINJECT_PAGETRAILER                = 103
PSINJECT_PLATECOLOR                 = 104

PSINJECT_SHOWPAGE                   = 105
PSINJECT_PAGEBBOX                   = 106
PSINJECT_ENDPAGECOMMENTS            = 107

PSINJECT_VMSAVE                     = 200
PSINJECT_VMRESTORE                  = 201


#InjectionPoint for publisher mode PScript5 OEM plugin to
#generate DSC comment for included font resource

PSINJECT_DLFONT                     = 0xdddddddd


#Parameter for GET_PS_FEATURESETTING escape


FEATURESETTING_NUP                  = 0
FEATURESETTING_OUTPUT               = 1
FEATURESETTING_PSLEVEL              = 2
FEATURESETTING_CUSTPAPER            = 3
FEATURESETTING_MIRROR               = 4
FEATURESETTING_NEGATIVE             = 5
FEATURESETTING_PROTOCOL             = 6

#
# The range of selectors between FEATURESETTING_PRIVATE_BEGIN and
# FEATURESETTING_PRIVATE_END is reserved by Microsoft for private use
#
FEATURESETTING_PRIVATE_BEGIN = 0x1000
FEATURESETTING_PRIVATE_END   = 0x1FFF

#Value returned for FEATURESETTING_PROTOCOL 
PSPROTOCOL_ASCII             = 0
PSPROTOCOL_BCP               = 1
PSPROTOCOL_TBCP              = 2
PSPROTOCOL_BINARY            = 3

#Flag returned from QUERYDIBSUPPORT 
QDI_SETDIBITS                = 1
QDI_GETDIBITS                = 2
QDI_DIBTOSCREEN              = 4
QDI_STRETCHDIB               = 8

#Spooler Error Codes 
SP_NOTREPORTED               = 0x4000
SP_ERROR                     = -1
SP_APPABORT                  = -2
SP_USERABORT                 = -3
SP_OUTOFDISK                 = -4
SP_OUTOFMEMORY               = -5

PR_JOBSTATUS                 = 0x0000

#Object Definitions for EnumObjects() 
OBJ_PEN             = 1
OBJ_BRUSH           = 2
OBJ_DC              = 3
OBJ_METADC          = 4
OBJ_PAL             = 5
OBJ_FONT            = 6
OBJ_BITMAP          = 7
OBJ_REGION          = 8
OBJ_METAFILE        = 9
OBJ_MEMDC           = 10
OBJ_EXTPEN          = 11
OBJ_ENHMETADC       = 12
OBJ_ENHMETAFILE     = 13
OBJ_COLORSPACE      = 14

GDI_OBJ_LAST        = OBJ_COLORSPACE

#xform stuff 
MWT_IDENTITY        = 1
MWT_LEFTMULTIPLY    = 2
MWT_RIGHTMULTIPLY   = 3

MWT_MIN             = MWT_IDENTITY
MWT_MAX             = MWT_RIGHTMULTIPLY

#Image Color Matching color definitions 

CS_ENABLE                       = 0x00000001L
CS_DISABLE                      = 0x00000002L
CS_DELETE_TRANSFORM             = 0x00000003L

#Logcolorspace signature 

LCS_SIGNATURE           = 'PSOC'

#Logcolorspace lcsType values 

LCS_sRGB                = 'sRGB'
LCS_WINDOWS_COLOR_SPACE = 'Win '  # Windows default color space
LCS_CALIBRATED_RGB              = 0x00000000L

LCS_GM_BUSINESS                 = 0x00000001L
LCS_GM_GRAPHICS                 = 0x00000002L
LCS_GM_IMAGES                   = 0x00000004L
LCS_GM_ABS_COLORIMETRIC         = 0x00000008L

#ICM Defines for results from CheckColorInGamut() 
CM_OUT_OF_GAMUT                 = 255
CM_IN_GAMUT                     = 0

#UpdateICMRegKey Constants               
ICM_ADDPROFILE                  = 1
ICM_DELETEPROFILE               = 2
ICM_QUERYPROFILE                = 3
ICM_SETDEFAULTPROFILE           = 4
ICM_REGISTERICMATCHER           = 5
ICM_UNREGISTERICMATCHER         = 6
ICM_QUERYMATCH                  = 7
# Values for bV5CSType
PROFILE_LINKED          = 'LINK'
PROFILE_EMBEDDED        = 'MBED'
#endif

#constants for the biCompression field 
BI_RGB        = 0L
BI_RLE8       = 1L
BI_RLE4       = 2L
BI_BITFIELDS  = 3L
BI_JPEG       = 4L
BI_PNG        = 5L

TCI_SRCCHARSET  = 1
TCI_SRCCODEPAGE = 2
TCI_SRCFONTSIG  = 3

TCI_SRCLOCALE   = 0x1000

#tmPitchAndFamily flags 
TMPF_FIXED_PITCH    = 0x01
TMPF_VECTOR         = 0x02
TMPF_DEVICE         = 0x08
TMPF_TRUETYPE       = 0x04
#ntmFlags field flags 
NTM_REGULAR     = 0x00000040L
NTM_BOLD        = 0x00000020L
NTM_ITALIC      = 0x00000001L

#new in NT 5.0 

NTM_NONNEGATIVE_AC  = 0x00010000
NTM_PS_OPENTYPE     = 0x00020000
NTM_TT_OPENTYPE     = 0x00040000
NTM_MULTIPLEMASTER  = 0x00080000
NTM_TYPE1           = 0x00100000
NTM_DSIG            = 0x00200000


OUT_DEFAULT_PRECIS          = 0
OUT_STRING_PRECIS           = 1
OUT_CHARACTER_PRECIS        = 2
OUT_STROKE_PRECIS           = 3
OUT_TT_PRECIS               = 4
OUT_DEVICE_PRECIS           = 5
OUT_RASTER_PRECIS           = 6
OUT_TT_ONLY_PRECIS          = 7
OUT_OUTLINE_PRECIS          = 8
OUT_SCREEN_OUTLINE_PRECIS   = 9
OUT_PS_ONLY_PRECIS          = 10

CLIP_DEFAULT_PRECIS     = 0
CLIP_CHARACTER_PRECIS   = 1
CLIP_STROKE_PRECIS      = 2
CLIP_MASK               = 0xf
CLIP_LH_ANGLES          = (1<<4)
CLIP_TT_ALWAYS          = (2<<4)

CLIP_EMBEDDED           = (8<<4)

DEFAULT_QUALITY                 = 0
DRAFT_QUALITY                   = 1
PROOF_QUALITY                   = 2
NONANTIALIASED_QUALITY          = 3
ANTIALIASED_QUALITY             = 4
CLEARTYPE_QUALITY               = 5
CLEARTYPE_NATURAL_QUALITY       = 6

DEFAULT_PITCH           = 0
FIXED_PITCH             = 1
VARIABLE_PITCH          = 2

ANSI_CHARSET            = 0
DEFAULT_CHARSET         = 1
SYMBOL_CHARSET          = 2
SHIFTJIS_CHARSET        = 128
HANGEUL_CHARSET         = 129
HANGUL_CHARSET          = 129
GB2312_CHARSET          = 134
CHINESEBIG5_CHARSET     = 136
OEM_CHARSET             = 255
JOHAB_CHARSET           = 130
HEBREW_CHARSET          = 177
ARABIC_CHARSET          = 178
GREEK_CHARSET           = 161
TURKISH_CHARSET         = 162
VIETNAMESE_CHARSET      = 163
THAI_CHARSET            = 222
EASTEUROPE_CHARSET      = 238
RUSSIAN_CHARSET         = 204

MAC_CHARSET             = 77
BALTIC_CHARSET          = 186

FS_LATIN1               = 0x00000001L
FS_LATIN2               = 0x00000002L
FS_CYRILLIC             = 0x00000004L
FS_GREEK                = 0x00000008L
FS_TURKISH              = 0x00000010L
FS_HEBREW               = 0x00000020L
FS_ARABIC               = 0x00000040L
FS_BALTIC               = 0x00000080L
FS_VIETNAMESE           = 0x00000100L
FS_THAI                 = 0x00010000L
FS_JISJAPAN             = 0x00020000L
FS_CHINESESIMP          = 0x00040000L
FS_WANSUNG              = 0x00080000L
FS_CHINESETRAD          = 0x00100000L
FS_JOHAB                = 0x00200000L
FS_SYMBOL               = auxfuncs.safe_long(0x80000000L)

#Font Families 
FF_DONTCARE         = (0<<4)  #Don't care or don't know. 
FF_ROMAN            = (1<<4)  #Variable stroke width, serifed. 
                                    #Times Roman, Century Schoolbook, etc. 
FF_SWISS            = (2<<4)  #Variable stroke width, sans-serifed. 
                                    #Helvetica, Swiss, etc. 
FF_MODERN           = (3<<4)  #Constant stroke width, serifed or sans-serifed. 
                                    #Pica, Elite, Courier, etc. 
FF_SCRIPT           = (4<<4)  #Cursive, etc. 
FF_DECORATIVE       = (5<<4)  #Old English, etc. 

#Font Weights 
FW_DONTCARE         = 0
FW_THIN             = 100
FW_EXTRALIGHT       = 200
FW_LIGHT            = 300
FW_NORMAL           = 400
FW_MEDIUM           = 500
FW_SEMIBOLD         = 600
FW_BOLD             = 700
FW_EXTRABOLD        = 800
FW_HEAVY            = 900

FW_ULTRALIGHT       = FW_EXTRALIGHT
FW_REGULAR          = FW_NORMAL
FW_DEMIBOLD         = FW_SEMIBOLD
FW_ULTRABOLD        = FW_EXTRABOLD
FW_BLACK            = FW_HEAVY

PANOSE_COUNT               = 10
PAN_FAMILYTYPE_INDEX       =  0
PAN_SERIFSTYLE_INDEX       =  1
PAN_WEIGHT_INDEX           =  2
PAN_PROPORTION_INDEX       =  3
PAN_CONTRAST_INDEX         =  4
PAN_STROKEVARIATION_INDEX  =  5
PAN_ARMSTYLE_INDEX         =  6
PAN_LETTERFORM_INDEX       =  7
PAN_MIDLINE_INDEX          =  8
PAN_XHEIGHT_INDEX          =  9

PAN_CULTURE_LATIN          =  0

PAN_ANY                         = 0 #Any                            
PAN_NO_FIT                      = 1 #No Fit                         
PAN_FAMILY_TEXT_DISPLAY         = 2 #Text and Display               
PAN_FAMILY_SCRIPT               = 3 #Script                         
PAN_FAMILY_DECORATIVE           = 4 #Decorative                     
PAN_FAMILY_PICTORIAL            = 5 #Pictorial                      
PAN_SERIF_COVE                  = 2 #Cove                           
PAN_SERIF_OBTUSE_COVE           = 3 #Obtuse Cove                    
PAN_SERIF_SQUARE_COVE           = 4 #Square Cove                    
PAN_SERIF_OBTUSE_SQUARE_COVE    = 5 #Obtuse Square Cove             
PAN_SERIF_SQUARE                = 6 #Square                         
PAN_SERIF_THIN                  = 7 #Thin                           
PAN_SERIF_BONE                  = 8 #Bone                           
PAN_SERIF_EXAGGERATED           = 9 #Exaggerated                    
PAN_SERIF_TRIANGLE              = 10 #Triangle                       
PAN_SERIF_NORMAL_SANS           = 11 #Normal Sans                    
PAN_SERIF_OBTUSE_SANS           = 12 #Obtuse Sans                    
PAN_SERIF_PERP_SANS             = 13 #Prep Sans                      
PAN_SERIF_FLARED                = 14 #Flared                         
PAN_SERIF_ROUNDED               = 15 #Rounded                        

PAN_WEIGHT_VERY_LIGHT           = 2 #Very Light                     
PAN_WEIGHT_LIGHT                = 3 #Light                          
PAN_WEIGHT_THIN                 = 4 #Thin                           
PAN_WEIGHT_BOOK                 = 5 #Book                           
PAN_WEIGHT_MEDIUM               = 6 #Medium                         
PAN_WEIGHT_DEMI                 = 7 #Demi                           
PAN_WEIGHT_BOLD                 = 8 #Bold                           
PAN_WEIGHT_HEAVY                = 9 #Heavy                          
PAN_WEIGHT_BLACK                = 10 #Black                          
PAN_WEIGHT_NORD                 = 11 #Nord                           

PAN_PROP_OLD_STYLE              = 2 #Old Style                      
PAN_PROP_MODERN                 = 3 #Modern                         
PAN_PROP_EVEN_WIDTH             = 4 #Even Width                     
PAN_PROP_EXPANDED               = 5 #Expanded                       
PAN_PROP_CONDENSED              = 6 #Condensed                      
PAN_PROP_VERY_EXPANDED          = 7 #Very Expanded                  
PAN_PROP_VERY_CONDENSED         = 8 #Very Condensed                 
PAN_PROP_MONOSPACED             = 9 #Monospaced                     

PAN_CONTRAST_NONE               = 2 #None                           
PAN_CONTRAST_VERY_LOW           = 3 #Very Low                       
PAN_CONTRAST_LOW                = 4 #Low                            
PAN_CONTRAST_MEDIUM_LOW         = 5 #Medium Low                     
PAN_CONTRAST_MEDIUM             = 6 #Medium                         
PAN_CONTRAST_MEDIUM_HIGH        = 7 #Mediim High                    
PAN_CONTRAST_HIGH               = 8 #High                           
PAN_CONTRAST_VERY_HIGH          = 9 #Very High                      

PAN_STROKE_GRADUAL_DIAG         = 2 #Gradual/Diagonal               
PAN_STROKE_GRADUAL_TRAN         = 3 #Gradual/Transitional           
PAN_STROKE_GRADUAL_VERT         = 4 #Gradual/Vertical               
PAN_STROKE_GRADUAL_HORZ         = 5 #Gradual/Horizontal             
PAN_STROKE_RAPID_VERT           = 6 #Rapid/Vertical                 
PAN_STROKE_RAPID_HORZ           = 7 #Rapid/Horizontal               
PAN_STROKE_INSTANT_VERT         = 8 #Instant/Vertical               

PAN_STRAIGHT_ARMS_HORZ          = 2 #Straight Arms/Horizontal       
PAN_STRAIGHT_ARMS_WEDGE         = 3 #Straight Arms/Wedge            
PAN_STRAIGHT_ARMS_VERT          = 4 #Straight Arms/Vertical         
PAN_STRAIGHT_ARMS_SINGLE_SERIF  = 5 #Straight Arms/Single-Serif     
PAN_STRAIGHT_ARMS_DOUBLE_SERIF  = 6 #Straight Arms/Double-Serif     
PAN_BENT_ARMS_HORZ              = 7 #Non-Straight Arms/Horizontal   
PAN_BENT_ARMS_WEDGE             = 8 #Non-Straight Arms/Wedge        
PAN_BENT_ARMS_VERT              = 9 #Non-Straight Arms/Vertical     
PAN_BENT_ARMS_SINGLE_SERIF      = 10 #Non-Straight Arms/Single-Serif 
PAN_BENT_ARMS_DOUBLE_SERIF      = 11 #Non-Straight Arms/Double-Serif 

PAN_LETT_NORMAL_CONTACT         = 2 #Normal/Contact                 
PAN_LETT_NORMAL_WEIGHTED        = 3 #Normal/Weighted                
PAN_LETT_NORMAL_BOXED           = 4 #Normal/Boxed                   
PAN_LETT_NORMAL_FLATTENED       = 5 #Normal/Flattened               
PAN_LETT_NORMAL_ROUNDED         = 6 #Normal/Rounded                 
PAN_LETT_NORMAL_OFF_CENTER      = 7 #Normal/Off Center              
PAN_LETT_NORMAL_SQUARE          = 8 #Normal/Square                  
PAN_LETT_OBLIQUE_CONTACT        = 9 #Oblique/Contact                
PAN_LETT_OBLIQUE_WEIGHTED       = 10 #Oblique/Weighted               
PAN_LETT_OBLIQUE_BOXED          = 11 #Oblique/Boxed                  
PAN_LETT_OBLIQUE_FLATTENED      = 12 #Oblique/Flattened              
PAN_LETT_OBLIQUE_ROUNDED        = 13 #Oblique/Rounded                
PAN_LETT_OBLIQUE_OFF_CENTER     = 14 #Oblique/Off Center             
PAN_LETT_OBLIQUE_SQUARE         = 15 #Oblique/Square                 

PAN_MIDLINE_STANDARD_TRIMMED    = 2 #Standard/Trimmed               
PAN_MIDLINE_STANDARD_POINTED    = 3 #Standard/Pointed               
PAN_MIDLINE_STANDARD_SERIFED    = 4 #Standard/Serifed               
PAN_MIDLINE_HIGH_TRIMMED        = 5 #High/Trimmed                   
PAN_MIDLINE_HIGH_POINTED        = 6 #High/Pointed                   
PAN_MIDLINE_HIGH_SERIFED        = 7 #High/Serifed                   
PAN_MIDLINE_CONSTANT_TRIMMED    = 8 #Constant/Trimmed               
PAN_MIDLINE_CONSTANT_POINTED    = 9 #Constant/Pointed               
PAN_MIDLINE_CONSTANT_SERIFED    = 10 #Constant/Serifed               
PAN_MIDLINE_LOW_TRIMMED         = 11 #Low/Trimmed                    
PAN_MIDLINE_LOW_POINTED         = 12 #Low/Pointed                    
PAN_MIDLINE_LOW_SERIFED         = 13 #Low/Serifed                    

PAN_XHEIGHT_CONSTANT_SMALL      = 2 #Constant/Small                 
PAN_XHEIGHT_CONSTANT_STD        = 3 #Constant/Standard              
PAN_XHEIGHT_CONSTANT_LARGE      = 4 #Constant/Large                 
PAN_XHEIGHT_DUCKING_SMALL       = 5 #Ducking/Small                  
PAN_XHEIGHT_DUCKING_STD         = 6 #Ducking/Standard               
PAN_XHEIGHT_DUCKING_LARGE       = 7 #Ducking/Large                  


ELF_VENDOR_SIZE     = 4

ELF_VERSION         = 0
ELF_CULTURE_LATIN   = 0

#EnumFonts Masks 
RASTER_FONTTYPE     = 0x0001
DEVICE_FONTTYPE     = 0x0002
TRUETYPE_FONTTYPE   = 0x0004

#palette entry flags 

PC_RESERVED     = 0x01    #palette index used for animation 
PC_EXPLICIT     = 0x02    #palette index is explicit to device 
PC_NOCOLLAPSE   = 0x04    #do not match color to system palette 

#Background Modes 
TRANSPARENT         = 1
OPAQUE              = 2
BKMODE_LAST         = 2

#Graphics Modes 

GM_COMPATIBLE       = 1
GM_ADVANCED         = 2
GM_LAST             = 2

#PolyDraw and GetPath point types 
PT_CLOSEFIGURE      = 0x01
PT_LINETO           = 0x02
PT_BEZIERTO         = 0x04
PT_MOVETO           = 0x06

#Mapping Modes 
MM_TEXT             = 1
MM_LOMETRIC         = 2
MM_HIMETRIC         = 3
MM_LOENGLISH        = 4
MM_HIENGLISH        = 5
MM_TWIPS            = 6
MM_ISOTROPIC        = 7
MM_ANISOTROPIC      = 8

#Min and Max Mapping Mode values 
MM_MIN              = MM_TEXT
MM_MAX              = MM_ANISOTROPIC
MM_MAX_FIXEDSCALE   = MM_TWIPS

#Coordinate Modes 
ABSOLUTE            = 1
RELATIVE            = 2

#Stock Logical Objects 
WHITE_BRUSH         = 0
LTGRAY_BRUSH        = 1
GRAY_BRUSH          = 2
DKGRAY_BRUSH        = 3
BLACK_BRUSH         = 4
NULL_BRUSH          = 5
HOLLOW_BRUSH        = NULL_BRUSH

WHITE_PEN           = 6
BLACK_PEN           = 7
NULL_PEN            = 8

OEM_FIXED_FONT      = 10
ANSI_FIXED_FONT     = 11
ANSI_VAR_FONT       = 12
SYSTEM_FONT         = 13
DEVICE_DEFAULT_FONT = 14
DEFAULT_PALETTE     = 15
SYSTEM_FIXED_FONT   = 16
DEFAULT_GUI_FONT    = 17

DC_BRUSH            = 18

DC_PEN              = 19

STOCK_LAST          = 19

CLR_INVALID     = 0xFFFFFFFF

#Brush Styles 
BS_SOLID            = 0
BS_NULL             = 1
BS_HOLLOW           = BS_NULL
BS_HATCHED          = 2
BS_PATTERN          = 3
BS_INDEXED          = 4
BS_DIBPATTERN       = 5
BS_DIBPATTERNPT     = 6
BS_PATTERN8X8       = 7
BS_DIBPATTERN8X8    = 8
BS_MONOPATTERN      = 9

#Hatch Styles 
HS_HORIZONTAL       = 0       #----- 
HS_VERTICAL         = 1       #||||| 
HS_FDIAGONAL        = 2       #\\\\\ 
HS_BDIAGONAL        = 3       ###/ 
HS_CROSS            = 4       #+++++ 
HS_DIAGCROSS        = 5       #xxxxx 
HS_API_MAX          = 12

#Pen Styles 
PS_SOLID            = 0
PS_DASH             = 1       #-------  
PS_DOT              = 2       #.......  
PS_DASHDOT          = 3       #_._._._  
PS_DASHDOTDOT       = 4       #_.._.._  
PS_NULL             = 5
PS_INSIDEFRAME      = 6
PS_USERSTYLE        = 7
PS_ALTERNATE        = 8
PS_STYLE_MASK       = 0x0000000F

PS_ENDCAP_ROUND     = 0x00000000
PS_ENDCAP_SQUARE    = 0x00000100
PS_ENDCAP_FLAT      = 0x00000200
PS_ENDCAP_MASK      = 0x00000F00

PS_JOIN_ROUND       = 0x00000000
PS_JOIN_BEVEL       = 0x00001000
PS_JOIN_MITER       = 0x00002000
PS_JOIN_MASK        = 0x0000F000

PS_COSMETIC         = 0x00000000
PS_GEOMETRIC        = 0x00010000
PS_TYPE_MASK        = 0x000F0000

AD_COUNTERCLOCKWISE = 1
AD_CLOCKWISE        = 2

#Device Parameters for GetDeviceCaps() 
DRIVERVERSION = 0     #Device driver version                    
TECHNOLOGY    = 2     #Device classification                    
HORZSIZE      = 4     #Horizontal size in millimeters           
VERTSIZE      = 6     #Vertical size in millimeters             
HORZRES       = 8     #Horizontal width in pixels               
VERTRES       = 10    #Vertical height in pixels                
BITSPIXEL     = 12    #Number of bits per pixel                 
PLANES        = 14    #Number of planes                         
NUMBRUSHES    = 16    #Number of brushes the device has         
NUMPENS       = 18    #Number of pens the device has            
NUMMARKERS    = 20    #Number of markers the device has         
NUMFONTS      = 22    #Number of fonts the device has           
NUMCOLORS     = 24    #Number of colors the device supports     
PDEVICESIZE   = 26    #Size required for device descriptor      
CURVECAPS     = 28    #Curve capabilities                       
LINECAPS      = 30    #Line capabilities                        
POLYGONALCAPS = 32    #Polygonal capabilities                   
TEXTCAPS      = 34    #Text capabilities                        
CLIPCAPS      = 36    #Clipping capabilities                    
RASTERCAPS    = 38    #Bitblt capabilities                      
ASPECTX       = 40    #Length of the X leg                      
ASPECTY       = 42    #Length of the Y leg                      
ASPECTXY      = 44    #Length of the hypotenuse                 

LOGPIXELSX    = 88    #Logical pixels/inch in X                 
LOGPIXELSY    = 90    #Logical pixels/inch in Y                 

SIZEPALETTE = 104    #Number of entries in physical palette    
NUMRESERVED = 106    #Number of reserved entries in palette    
COLORRES    = 108    #Actual color resolution                  

# Printing related DeviceCaps. These replace the appropriate Escapes

PHYSICALWIDTH  = 110 #Physical Width in device units           
PHYSICALHEIGHT = 111 #Physical Height in device units          
PHYSICALOFFSETX= 112 #Physical Printable Area x margin         
PHYSICALOFFSETY= 113 #Physical Printable Area y margin         
SCALINGFACTORX = 114 #Scaling factor x                         
SCALINGFACTORY = 115 #Scaling factor y                         

# Display driver specific

VREFRESH       = 116  #Current vertical refresh rate of the display device (for displays only) in Hz
DESKTOPVERTRES = 117  #Horizontal width of entire desktop in pixels                                  
DESKTOPHORZRES = 118  #Vertical height of entire desktop in pixels                                  
BLTALIGNMENT   = 119  #Preferred blt alignment                 
SHADEBLENDCAPS = 120  #Shading and blending caps               
COLORMGMTCAPS  = 121  #Color Management caps                   
#Device Capability Masks: 

#Device Technologies 
DT_PLOTTER         = 0   #Vector plotter                   
DT_RASDISPLAY      = 1   #Raster display                   
DT_RASPRINTER      = 2   #Raster printer                   
DT_RASCAMERA       = 3   #Raster camera                    
DT_CHARSTREAM      = 4   #Character-stream, PLP            
DT_METAFILE        = 5   #Metafile, VDM                    
DT_DISPFILE        = 6   #Display-file                     

#Curve Capabilities 
CC_NONE            = 0   #Curves not supported             
CC_CIRCLES         = 1   #Can do circles                   
CC_PIE             = 2   #Can do pie wedges                
CC_CHORD           = 4   #Can do chord arcs                
CC_ELLIPSES        = 8   #Can do ellipese                  
CC_WIDE            = 16  #Can do wide lines                
CC_STYLED          = 32  #Can do styled lines              
CC_WIDESTYLED      = 64  #Can do wide styled lines         
CC_INTERIORS       = 128 #Can do interiors                 
CC_ROUNDRECT       = 256 #                                 

#Line Capabilities 
LC_NONE            = 0   #Lines not supported              
LC_POLYLINE        = 2   #Can do polylines                 
LC_MARKER          = 4   #Can do markers                   
LC_POLYMARKER      = 8   #Can do polymarkers               
LC_WIDE            = 16  #Can do wide lines                
LC_STYLED          = 32  #Can do styled lines              
LC_WIDESTYLED      = 64  #Can do wide styled lines         
LC_INTERIORS       = 128 #Can do interiors                 

#Polygonal Capabilities 
PC_NONE            = 0   #Polygonals not supported         
PC_POLYGON         = 1   #Can do polygons                  
PC_RECTANGLE       = 2   #Can do rectangles                
PC_WINDPOLYGON     = 4   #Can do winding polygons          
PC_TRAPEZOID       = 4   #Can do trapezoids                
PC_SCANLINE        = 8   #Can do scanlines                 
PC_WIDE            = 16  #Can do wide borders              
PC_STYLED          = 32  #Can do styled borders            
PC_WIDESTYLED      = 64  #Can do wide styled borders       
PC_INTERIORS       = 128 #Can do interiors                 
PC_POLYPOLYGON     = 256 #Can do polypolygons              
PC_PATHS           = 512 #Can do paths                     

#Clipping Capabilities 
CP_NONE            = 0   #No clipping of output            
CP_RECTANGLE       = 1   #Output clipped to rects          
CP_REGION          = 2   #obsolete                         

#Text Capabilities 
TC_OP_CHARACTER     = 0x00000001  #Can do OutputPrecision   CHARACTER      
TC_OP_STROKE        = 0x00000002  #Can do OutputPrecision   STROKE         
TC_CP_STROKE        = 0x00000004  #Can do ClipPrecision     STROKE         
TC_CR_90            = 0x00000008  #Can do CharRotAbility    90             
TC_CR_ANY           = 0x00000010  #Can do CharRotAbility    ANY            
TC_SF_X_YINDEP      = 0x00000020  #Can do ScaleFreedom      X_YINDEPENDENT 
TC_SA_DOUBLE        = 0x00000040  #Can do ScaleAbility      DOUBLE         
TC_SA_INTEGER       = 0x00000080  #Can do ScaleAbility      INTEGER        
TC_SA_CONTIN        = 0x00000100  #Can do ScaleAbility      CONTINUOUS     
TC_EA_DOUBLE        = 0x00000200  #Can do EmboldenAbility   DOUBLE         
TC_IA_ABLE          = 0x00000400  #Can do ItalisizeAbility  ABLE           
TC_UA_ABLE          = 0x00000800  #Can do UnderlineAbility  ABLE           
TC_SO_ABLE          = 0x00001000  #Can do StrikeOutAbility  ABLE           
TC_RA_ABLE          = 0x00002000  #Can do RasterFontAble    ABLE           
TC_VA_ABLE          = 0x00004000  #Can do VectorFontAble    ABLE           
TC_RESERVED         = 0x00008000
TC_SCROLLBLT        = 0x00010000  #Don't do text scroll with blt           

#Raster Capabilities 
#RC_NONE
RC_BITBLT          = 1       #Can do standard BLT.             
RC_BANDING         = 2       #Device requires banding support  
RC_SCALING         = 4       #Device requires scaling support  
RC_BITMAP64        = 8       #Device can support >64K bitmap   
RC_GDI20_OUTPUT     = 0x0010      #has 2.0 output calls         
RC_GDI20_STATE      = 0x0020
RC_SAVEBITMAP       = 0x0040
RC_DI_BITMAP        = 0x0080      #supports DIB to memory       
RC_PALETTE          = 0x0100      #supports a palette           
RC_DIBTODEV         = 0x0200      #supports DIBitsToDevice      
RC_BIGFONT          = 0x0400      #supports >64K fonts          
RC_STRETCHBLT       = 0x0800      #supports StretchBlt          
RC_FLOODFILL        = 0x1000      #supports FloodFill           
RC_STRETCHDIB       = 0x2000      #supports StretchDIBits       
RC_OP_DX_OUTPUT     = 0x4000
RC_DEVBITS          = 0x8000

#Shading and blending caps 
SB_NONE             = 0x00000000
SB_CONST_ALPHA      = 0x00000001
SB_PIXEL_ALPHA      = 0x00000002
SB_PREMULT_ALPHA    = 0x00000004

SB_GRAD_RECT        = 0x00000010
SB_GRAD_TRI         = 0x00000020

#Color Management caps 
CM_NONE             = 0x00000000
CM_DEVICE_ICM       = 0x00000001
CM_GAMMA_RAMP       = 0x00000002
CM_CMYK_COLOR       = 0x00000004

#DIB color table identifiers 

DIB_RGB_COLORS     = 0 #color table in RGBs 
DIB_PAL_COLORS     = 1 #color table in palette indices 

#constants for Get/SetSystemPaletteUse() 

SYSPAL_ERROR         = 0
SYSPAL_STATIC        = 1
SYSPAL_NOSTATIC      = 2
SYSPAL_NOSTATIC256   = 3

#constants for CreateDIBitmap 
CBM_INIT        = 0x04L   #initialize bitmap 

#ExtFloodFill style flags 
FLOODFILLBORDER  = 0
FLOODFILLSURFACE = 1

#size of a device name string 
CCHDEVICENAME = 32

#size of a form name string 
CCHFORMNAME = 32

#field selection bits 
DM_ORIENTATION          = 0x00000001L
DM_PAPERSIZE            = 0x00000002L
DM_PAPERLENGTH          = 0x00000004L
DM_PAPERWIDTH           = 0x00000008L
DM_SCALE                = 0x00000010L
DM_POSITION             = 0x00000020L
DM_NUP                  = 0x00000040L

DM_DISPLAYORIENTATION   = 0x00000080L

DM_COPIES               = 0x00000100L
DM_DEFAULTSOURCE        = 0x00000200L
DM_PRINTQUALITY         = 0x00000400L
DM_COLOR                = 0x00000800L
DM_DUPLEX               = 0x00001000L
DM_YRESOLUTION          = 0x00002000L
DM_TTOPTION             = 0x00004000L
DM_COLLATE              = 0x00008000L
DM_FORMNAME             = 0x00010000L
DM_LOGPIXELS            = 0x00020000L
DM_BITSPERPEL           = 0x00040000L
DM_PELSWIDTH            = 0x00080000L
DM_PELSHEIGHT           = 0x00100000L
DM_DISPLAYFLAGS         = 0x00200000L
DM_DISPLAYFREQUENCY     = 0x00400000L

DM_ICMMETHOD            = 0x00800000L
DM_ICMINTENT            = 0x01000000L
DM_MEDIATYPE            = 0x02000000L
DM_DITHERTYPE           = 0x04000000L
DM_PANNINGWIDTH         = 0x08000000L
DM_PANNINGHEIGHT        = 0x10000000L
DM_DISPLAYFIXEDOUTPUT   = 0x20000000L
#orientation selections 
DMORIENT_PORTRAIT   = 1
DMORIENT_LANDSCAPE  = 2

#paper selections 
DMPAPER_LETTER              = 1  #Letter 8 1/2 x 11 in               
DMPAPER_LETTERSMALL         = 2  #Letter Small 8 1/2 x 11 in         
DMPAPER_TABLOID             = 3  #Tabloid 11 x 17 in                 
DMPAPER_LEDGER              = 4  #Ledger 17 x 11 in                  
DMPAPER_LEGAL               = 5  #Legal 8 1/2 x 14 in                
DMPAPER_STATEMENT           = 6  #Statement 5 1/2 x 8 1/2 in         
DMPAPER_EXECUTIVE           = 7  #Executive 7 1/4 x 10 1/2 in        
DMPAPER_A3                  = 8  #A3 297 x 420 mm                    
DMPAPER_A4                  = 9  #A4 210 x 297 mm                    
DMPAPER_A4SMALL             = 10  #A4 Small 210 x 297 mm              
DMPAPER_A5                  = 11  #A5 148 x 210 mm                    
DMPAPER_B4                  = 12  #B4 (JIS) 250 x 354                 
DMPAPER_B5                  = 13  #B5 (JIS) 182 x 257 mm              
DMPAPER_FOLIO               = 14  #Folio 8 1/2 x 13 in                
DMPAPER_QUARTO              = 15  #Quarto 215 x 275 mm                
DMPAPER_10X14               = 16  #10x14 in                           
DMPAPER_11X17               = 17  #11x17 in                           
DMPAPER_NOTE                = 18  #Note 8 1/2 x 11 in                 
DMPAPER_ENV_9               = 19  #Envelope #9 3 7/8 x 8 7/8          
DMPAPER_ENV_10              = 20  #Envelope #10 4 1/8 x 9 1/2         
DMPAPER_ENV_11              = 21  #Envelope #11 4 1/2 x 10 3/8        
DMPAPER_ENV_12              = 22  #Envelope #12 4 \276 x 11           
DMPAPER_ENV_14              = 23  #Envelope #14 5 x 11 1/2            
DMPAPER_CSHEET              = 24  #C size sheet                       
DMPAPER_DSHEET              = 25  #D size sheet                       
DMPAPER_ESHEET              = 26  #E size sheet                       
DMPAPER_ENV_DL              = 27  #Envelope DL 110 x 220mm            
DMPAPER_ENV_C5              = 28  #Envelope C5 162 x 229 mm           
DMPAPER_ENV_C3              = 29  #Envelope C3  324 x 458 mm          
DMPAPER_ENV_C4              = 30  #Envelope C4  229 x 324 mm          
DMPAPER_ENV_C6              = 31  #Envelope C6  114 x 162 mm          
DMPAPER_ENV_C65             = 32  #Envelope C65 114 x 229 mm          
DMPAPER_ENV_B4              = 33  #Envelope B4  250 x 353 mm          
DMPAPER_ENV_B5              = 34  #Envelope B5  176 x 250 mm          
DMPAPER_ENV_B6              = 35  #Envelope B6  176 x 125 mm          
DMPAPER_ENV_ITALY           = 36  #Envelope 110 x 230 mm              
DMPAPER_ENV_MONARCH         = 37  #Envelope Monarch 3.875 x 7.5 in    
DMPAPER_ENV_PERSONAL        = 38  #6 3/4 Envelope 3 5/8 x 6 1/2 in    
DMPAPER_FANFOLD_US          = 39  #US Std Fanfold 14 7/8 x 11 in      
DMPAPER_FANFOLD_STD_GERMAN  = 40  #German Std Fanfold 8 1/2 x 12 in   
DMPAPER_FANFOLD_LGL_GERMAN  = 41  #German Legal Fanfold 8 1/2 x 13 in DMPAPER_ISO_B4              42  #B4 (ISO) 250 x 353 mm              
DMPAPER_JAPANESE_POSTCARD   = 43  #Japanese Postcard 100 x 148 mm     
DMPAPER_9X11                = 44  #9 x 11 in                          
DMPAPER_10X11               = 45  #10 x 11 in                         
DMPAPER_15X11               = 46  #15 x 11 in                         
DMPAPER_ENV_INVITE          = 47  #Envelope Invite 220 x 220 mm       
DMPAPER_RESERVED_48         = 48  #RESERVED--DO NOT USE               
DMPAPER_RESERVED_49         = 49  #RESERVED--DO NOT USE               
DMPAPER_LETTER_EXTRA        = 50  #Letter Extra 9 \275 x 12 in        
DMPAPER_LEGAL_EXTRA         = 51  #Legal Extra 9 \275 x 15 in         
DMPAPER_TABLOID_EXTRA       = 52  #Tabloid Extra 11.69 x 18 in        
DMPAPER_A4_EXTRA            = 53  #A4 Extra 9.27 x 12.69 in           
DMPAPER_LETTER_TRANSVERSE   = 54  #Letter Transverse 8 \275 x 11 in   
DMPAPER_A4_TRANSVERSE       = 55  #A4 Transverse 210 x 297 mm         
DMPAPER_LETTER_EXTRA_TRANSVERSE = 56 #Letter Extra Transverse 9\275 x 12 in 
DMPAPER_A_PLUS                  = 57  #SuperA/SuperA/A4 227 x 356 mm      
DMPAPER_B_PLUS                 = 58  #SuperB/SuperB/A3 305 x 487 mm      
DMPAPER_LETTER_PLUS            = 59  #Letter Plus 8.5 x 12.69 in         
DMPAPER_A4_PLUS                = 60  #A4 Plus 210 x 330 mm               
DMPAPER_A5_TRANSVERSE          = 61  #A5 Transverse 148 x 210 mm         
DMPAPER_B5_TRANSVERSE          = 62  #B5 (JIS) Transverse 182 x 257 mm   
DMPAPER_A3_EXTRA               = 63  #A3 Extra 322 x 445 mm              
DMPAPER_A5_EXTRA               = 64  #A5 Extra 174 x 235 mm              
DMPAPER_B5_EXTRA               = 65  #B5 (ISO) Extra 201 x 276 mm        
DMPAPER_A2                     = 66  #A2 420 x 594 mm                    
DMPAPER_A3_TRANSVERSE          = 67  #A3 Transverse 297 x 420 mm         
DMPAPER_A3_EXTRA_TRANSVERSE    = 68  #A3 Extra Transverse 322 x 445 mm   
DMPAPER_DBL_JAPANESE_POSTCARD  = 69 #Japanese Double Postcard 200 x 148 mm 
DMPAPER_A6                     = 70  #A6 105 x 148 mm                 
DMPAPER_JENV_KAKU2             = 71  #Japanese Envelope Kaku #2       
DMPAPER_JENV_KAKU3             = 72  #Japanese Envelope Kaku #3       
DMPAPER_JENV_CHOU3             = 73  #Japanese Envelope Chou #3       
DMPAPER_JENV_CHOU4             = 74  #Japanese Envelope Chou #4       
DMPAPER_LETTER_ROTATED         = 75  #Letter Rotated 11 x 8 1/2 11 in 
DMPAPER_A3_ROTATED             = 76  #A3 Rotated 420 x 297 mm         
DMPAPER_A4_ROTATED             = 77  #A4 Rotated 297 x 210 mm         
DMPAPER_A5_ROTATED             = 78  #A5 Rotated 210 x 148 mm         
DMPAPER_B4_JIS_ROTATED         = 79  #B4 (JIS) Rotated 364 x 257 mm   
DMPAPER_B5_JIS_ROTATED         = 80  #B5 (JIS) Rotated 257 x 182 mm   
DMPAPER_JAPANESE_POSTCARD_ROTATED = 81 #Japanese Postcard Rotated 148 x 100 mm 
DMPAPER_DBL_JAPANESE_POSTCARD_ROTATED = 82 #Double Japanese Postcard Rotated 148 x 200 mm 
DMPAPER_A6_ROTATED             = 83  #A6 Rotated 148 x 105 mm         
DMPAPER_JENV_KAKU2_ROTATED     = 84  #Japanese Envelope Kaku #2 Rotated 
DMPAPER_JENV_KAKU3_ROTATED     = 85  #Japanese Envelope Kaku #3 Rotated 
DMPAPER_JENV_CHOU3_ROTATED     = 86  #Japanese Envelope Chou #3 Rotated 
DMPAPER_JENV_CHOU4_ROTATED     = 87  #Japanese Envelope Chou #4 Rotated 
DMPAPER_B6_JIS                 = 88  #B6 (JIS) 128 x 182 mm           
DMPAPER_B6_JIS_ROTATED         = 89  #B6 (JIS) Rotated 182 x 128 mm   
DMPAPER_12X11                  = 90  #12 x 11 in                      
DMPAPER_JENV_YOU4              = 91  #Japanese Envelope You #4        
DMPAPER_JENV_YOU4_ROTATED      = 92  #Japanese Envelope You #4 Rotated
DMPAPER_P16K                   = 93  #PRC 16K 146 x 215 mm            
DMPAPER_P32K                   = 94  #PRC 32K 97 x 151 mm             
DMPAPER_P32KBIG                = 95  #PRC 32K(Big) 97 x 151 mm        
DMPAPER_PENV_1                 = 96  #PRC Envelope #1 102 x 165 mm    
DMPAPER_PENV_2                 = 97  #PRC Envelope #2 102 x 176 mm    
DMPAPER_PENV_3                 = 98  #PRC Envelope #3 125 x 176 mm    
DMPAPER_PENV_4                 = 99  #PRC Envelope #4 110 x 208 mm    
DMPAPER_PENV_5                 = 100 #PRC Envelope #5 110 x 220 mm    
DMPAPER_PENV_6                 = 101 #PRC Envelope #6 120 x 230 mm    
DMPAPER_PENV_7                 = 102 #PRC Envelope #7 160 x 230 mm    
DMPAPER_PENV_8                 = 103 #PRC Envelope #8 120 x 309 mm    
DMPAPER_PENV_9                 = 104 #PRC Envelope #9 229 x 324 mm    
DMPAPER_PENV_10                = 105 #PRC Envelope #10 324 x 458 mm   
DMPAPER_P16K_ROTATED           = 106 #PRC 16K Rotated                 
DMPAPER_P32K_ROTATED           = 107 #PRC 32K Rotated                 
DMPAPER_P32KBIG_ROTATED        = 108 #PRC 32K(Big) Rotated            
DMPAPER_PENV_1_ROTATED         = 109 #PRC Envelope #1 Rotated 165 x 102 mm 
DMPAPER_PENV_2_ROTATED         = 110 #PRC Envelope #2 Rotated 176 x 102 mm 
DMPAPER_PENV_3_ROTATED         = 111 #PRC Envelope #3 Rotated 176 x 125 mm 
DMPAPER_PENV_4_ROTATED         = 112 #PRC Envelope #4 Rotated 208 x 110 mm 
DMPAPER_PENV_5_ROTATED         = 113 #PRC Envelope #5 Rotated 220 x 110 mm 
DMPAPER_PENV_6_ROTATED         = 114 #PRC Envelope #6 Rotated 230 x 120 mm 
DMPAPER_PENV_7_ROTATED         = 115 #PRC Envelope #7 Rotated 230 x 160 mm 
DMPAPER_PENV_8_ROTATED         = 116 #PRC Envelope #8 Rotated 309 x 120 mm 
DMPAPER_PENV_9_ROTATED         = 117 #PRC Envelope #9 Rotated 324 x 229 mm 
DMPAPER_PENV_10_ROTATED        = 118 #PRC Envelope #10 Rotated 458 x 324 mm 
DMPAPER_LAST                   = DMPAPER_PENV_10_ROTATED
DMPAPER_USER                   = 256
DMPAPER_FIRST                  = DMPAPER_LETTER

#bin selections 
DMBIN_UPPER        = 1
DMBIN_ONLYONE      = 1
DMBIN_LOWER        = 2
DMBIN_MIDDLE       = 3
DMBIN_MANUAL       = 4
DMBIN_ENVELOPE     = 5
DMBIN_ENVMANUAL    = 6
DMBIN_AUTO         = 7
DMBIN_TRACTOR      = 8
DMBIN_SMALLFMT     = 9
DMBIN_LARGEFMT     = 10
DMBIN_LARGECAPACITY= 11
DMBIN_CASSETTE     = 14
DMBIN_FORMSOURCE   = 15
DMBIN_LAST         = DMBIN_FORMSOURCE
DMBIN_USER         = 256     #device specific bins start here 
DMBIN_FIRST        = DMBIN_UPPER

#print qualities 
DMRES_DRAFT        = -1
DMRES_LOW          = -2
DMRES_MEDIUM       = -3
DMRES_HIGH         = -4

#color enable/disable for color printers 
DMCOLOR_MONOCHROME = 1
DMCOLOR_COLOR      = 2

#duplex enable 
DMDUP_SIMPLEX    = 1
DMDUP_VERTICAL   = 2
DMDUP_HORIZONTAL = 3

#TrueType options 
DMTT_BITMAP            = 1       #print TT fonts as graphics 
DMTT_DOWNLOAD          = 2       #download TT fonts as soft fonts 
DMTT_SUBDEV            = 3       #substitute device fonts for TT fonts 
DMTT_DOWNLOAD_OUTLINE  = 4 #download TT fonts as outline soft fonts 
#Collation selections 
DMCOLLATE_FALSE = 0
DMCOLLATE_TRUE  = 1

#DEVMODE dmDisplayOrientation specifiations 
DMDO_DEFAULT    = 0
DMDO_90         = 1
DMDO_180        = 2
DMDO_270        = 3

#DEVMODE dmDisplayFixedOutput specifiations 
DMDFO_DEFAULT   = 0
DMDFO_STRETCH   = 1
DMDFO_CENTER    = 2
#DEVMODE dmDisplayFlags flags 

# DM_GRAYSCALE            = 0x00000001 #This flag is no longer valid 
DM_INTERLACED           = 0x00000002
DMDISPLAYFLAGS_TEXTMODE = 0x00000004

#dmNup , multiple logical page per physical page options 
DMNUP_SYSTEM        = 1
DMNUP_ONEUP         = 2

#ICM methods 
DMICMMETHOD_NONE    = 1   #ICM disabled 
DMICMMETHOD_SYSTEM  = 2   #ICM handled by system 
DMICMMETHOD_DRIVER  = 3   #ICM handled by driver 
DMICMMETHOD_DEVICE  = 4   #ICM handled by device 

DMICMMETHOD_USER    = 256   #Device-specific methods start here 

#ICM Intents 
DMICM_SATURATE          = 1   #Maximize color saturation 
DMICM_CONTRAST          = 2   #Maximize color contrast 
DMICM_COLORIMETRIC      = 3   #Use specific color metric 
DMICM_ABS_COLORIMETRIC  = 4   #Use specific color metric 
DMICM_USER              = 256   #Device-specific intents start here 

#Media types 

DMMEDIA_STANDARD      = 1   #Standard paper 
DMMEDIA_TRANSPARENCY  = 2   #Transparency 
DMMEDIA_GLOSSY        = 3   #Glossy paper 

DMMEDIA_USER          = 256   #Device-specific media start here 

#Dither types 
DMDITHER_NONE           = 1      #No dithering 
DMDITHER_COARSE         = 2      #Dither with a coarse brush 
DMDITHER_FINE           = 3      #Dither with a fine brush 
DMDITHER_LINEART        = 4      #LineArt dithering 
DMDITHER_ERRORDIFFUSION = 5  #LineArt dithering 
DMDITHER_RESERVED6      = 6      #LineArt dithering 
DMDITHER_RESERVED7      = 7      #LineArt dithering 
DMDITHER_RESERVED8      = 8      #LineArt dithering 
DMDITHER_RESERVED9      = 9      #LineArt dithering 
DMDITHER_GRAYSCALE      = 10     #Device does grayscaling 

DMDITHER_USER           = 256   #Device-specific dithers start here 
DISPLAY_DEVICE_ATTACHED_TO_DESKTOP = 0x00000001
DISPLAY_DEVICE_MULTI_DRIVER        = 0x00000002
DISPLAY_DEVICE_PRIMARY_DEVICE      = 0x00000004
DISPLAY_DEVICE_MIRRORING_DRIVER    = 0x00000008
DISPLAY_DEVICE_VGA_COMPATIBLE      = 0x00000010

DISPLAY_DEVICE_REMOVABLE           = 0x00000020
DISPLAY_DEVICE_MODESPRUNED         = 0x08000000
DISPLAY_DEVICE_REMOTE              = 0x04000000
DISPLAY_DEVICE_DISCONNECT          = 0x02000000
DISPLAY_DEVICE_TS_COMPATIBLE       = 0x00200000
#Child device state 
DISPLAY_DEVICE_ACTIVE              = 0x00000001
DISPLAY_DEVICE_ATTACHED            = 0x00000002

#GetRegionData/ExtCreateRegion 

RDH_RECTANGLES = 1

#for GetRandomRgn 
SYSRGN  = 4

#  GetGlyphOutline constants

GGO_METRICS         = 0
GGO_BITMAP          = 1
GGO_NATIVE          = 2
GGO_BEZIER          = 3
GGO_GRAY2_BITMAP   = 4
GGO_GRAY4_BITMAP   = 5
GGO_GRAY8_BITMAP   = 6
GGO_GLYPH_INDEX    = 0x0080
GGO_UNHINTED       = 0x0100
TT_POLYGON_TYPE    = 24

TT_PRIM_LINE       = 1
TT_PRIM_QSPLINE    = 2
TT_PRIM_CSPLINE    = 3

GCP_DBCS           = 0x0001
GCP_REORDER        = 0x0002
GCP_USEKERNING     = 0x0008
GCP_GLYPHSHAPE     = 0x0010
GCP_LIGATE         = 0x0020

GCP_DIACRITIC      = 0x0100
GCP_KASHIDA        = 0x0400
GCP_ERROR          = 0x8000
FLI_MASK           = 0x103B

GCP_JUSTIFY        = 0x00010000L

FLI_GLYPHS         = 0x00040000L
GCP_CLASSIN        = 0x00080000L
GCP_MAXEXTENT      = 0x00100000L
GCP_JUSTIFYIN      = 0x00200000L
GCP_DISPLAYZWG      = 0x00400000L
GCP_SYMSWAPOFF      = 0x00800000L
GCP_NUMERICOVERRIDE = 0x01000000L
GCP_NEUTRALOVERRIDE = 0x02000000L
GCP_NUMERICSLATIN   = 0x04000000L
GCP_NUMERICSLOCAL   = 0x08000000L

GCPCLASS_LATIN                  = 1
GCPCLASS_HEBREW                 = 2
GCPCLASS_ARABIC                 = 2
GCPCLASS_NEUTRAL                = 3
GCPCLASS_LOCALNUMBER            = 4
GCPCLASS_LATINNUMBER            = 5
GCPCLASS_LATINNUMERICTERMINATOR = 6
GCPCLASS_LATINNUMERICSEPARATOR  = 7
GCPCLASS_NUMERICSEPARATOR       = 8
GCPCLASS_PREBOUNDLTR            = 0x80
GCPCLASS_PREBOUNDRTL            = 0x40
GCPCLASS_POSTBOUNDLTR           = 0x20
GCPCLASS_POSTBOUNDRTL           = 0x10

GCPGLYPH_LINKBEFORE             = 0x8000
GCPGLYPH_LINKAFTER              = 0x4000

#pixel types 
PFD_TYPE_RGBA        = 0
PFD_TYPE_COLORINDEX  = 1

#layer types 
PFD_MAIN_PLANE       = 0
PFD_OVERLAY_PLANE    = 1
PFD_UNDERLAY_PLANE   = -1

#PIXELFORMATDESCRIPTOR flags 
PFD_DOUBLEBUFFER            = 0x00000001
PFD_STEREO                  = 0x00000002
PFD_DRAW_TO_WINDOW          = 0x00000004
PFD_DRAW_TO_BITMAP          = 0x00000008
PFD_SUPPORT_GDI             = 0x00000010
PFD_SUPPORT_OPENGL          = 0x00000020
PFD_GENERIC_FORMAT          = 0x00000040
PFD_NEED_PALETTE            = 0x00000080
PFD_NEED_SYSTEM_PALETTE     = 0x00000100
PFD_SWAP_EXCHANGE           = 0x00000200
PFD_SWAP_COPY               = 0x00000400
PFD_SWAP_LAYER_BUFFERS      = 0x00000800
PFD_GENERIC_ACCELERATED     = 0x00001000
PFD_SUPPORT_DIRECTDRAW      = 0x00002000
PFD_DIRECT3D_ACCELERATED    = 0x00004000
PFD_SUPPORT_COMPOSITION     = 0x00008000

#PIXELFORMATDESCRIPTOR flags for use in ChoosePixelFormat only 
PFD_DEPTH_DONTCARE          = 0x20000000
PFD_DOUBLEBUFFER_DONTCARE   = 0x40000000
PFD_STEREO_DONTCARE         = auxfuncs.safe_long(0x80000000)


CreateFont = windll.gdi32.CreateFontA
CreateFont.argtypes = [c_int, c_int, c_int, c_int, c_int, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, LPCSTR]

'''
WINGDIAPI
HFONT
WINAPI
CreateFontA( __in int cHeight,
             __in int cWidth,
             __in int cEscapement,
             __in int cOrientation,
             __in int cWeight,
             __in DWORD bItalic,
             __in DWORD bUnderline,
             __in DWORD bStrikeOut,
             __in DWORD iCharSet,
             __in DWORD iOutPrecision,
             __in DWORD iClipPrecision,
             __in DWORD iQuality,
             __in DWORD iPitchAndFamily,
             __in_opt LPCSTR pszFaceName);
'''


#mode selections for the device mode function 
DM_UPDATE           = 1
DM_COPY             = 2
DM_PROMPT           = 4
DM_MODIFY           = 8

DM_IN_BUFFER        = DM_MODIFY
DM_IN_PROMPT        = DM_PROMPT
DM_OUT_BUFFER       = DM_COPY
DM_OUT_DEFAULT      = DM_UPDATE

#device capabilities indices 
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
DC_BINADJUST            = 19
DC_EMF_COMPLIANT        = 20
DC_DATATYPE_PRODUCED    = 21
DC_COLLATE              = 22
DC_MANUFACTURER         = 23
DC_MODEL                = 24
DC_PERSONALITY          = 25
DC_PRINTRATE            = 26
DC_PRINTRATEUNIT        = 27
DC_PRINTERMEM           = 28
DC_MEDIAREADY           = 29
DC_STAPLE               = 30
DC_PRINTRATEPPM         = 31
DC_COLORDEVICE          = 32
DC_NUP                  = 33
DC_MEDIATYPENAMES       = 34
DC_MEDIATYPES           = 35

PRINTRATEUNIT_PPM       = 1
PRINTRATEUNIT_CPS       = 2
PRINTRATEUNIT_LPM       = 3
PRINTRATEUNIT_IPM       = 4

#bit fields of the return value (DWORD) for DC_TRUETYPE 
DCTT_BITMAP             = 0x0000001L
DCTT_DOWNLOAD           = 0x0000002L
DCTT_SUBDEV             = 0x0000004L

DCTT_DOWNLOAD_OUTLINE   = 0x0000008L

#return values for DC_BINADJUST 
DCBA_FACEUPNONE       = 0x0000
DCBA_FACEUPCENTER     = 0x0001
DCBA_FACEUPLEFT       = 0x0002
DCBA_FACEUPRIGHT      = 0x0003
DCBA_FACEDOWNNONE     = 0x0100
DCBA_FACEDOWNCENTER   = 0x0101
DCBA_FACEDOWNLEFT     = 0x0102
DCBA_FACEDOWNRIGHT    = 0x0103

'''
WINGDIAPI HGDIOBJ WINAPI GetStockObject( __in int i);
'''
GetStockObject = windll.gdi32.GetStockObject
GetStockObject.argtypes = [c_int]


#flAccel flags for the GLYPHSET structure above 

GS_8BIT_INDICES     = 0x00000001

#flags for GetGlyphIndices 

GGI_MARK_NONEXISTING_GLYPHS  = 0x0001
STAMP_DESIGNVECTOR           = (0x8000000 + ord('d') + (ord('v') << 8))
STAMP_AXESLIST               = (0x8000000 + ord('a') + (ord('l') << 8))
MM_MAX_NUMAXES               = 16


SelectObject = windll.gdi32.SelectObject
SelectObject.argtypes = [HDC, HGDIOBJ]
'''
__gdi_entry
WINGDIAPI
HGDIOBJ
WINAPI
SelectObject(__in HDC hdc, __in HGDIOBJ h);
'''


FR_PRIVATE                   = 0x10
FR_NOT_ENUM                  = 0x20

# The actual size of the DESIGNVECTOR and ENUMLOGFONTEXDV structures
# is determined by dvNumAxes,
# MM_MAX_NUMAXES only detemines the maximal size allowed

MM_MAX_AXES_NAMELEN     = 16

#
# gradient drawing modes
#

GRADIENT_FILL_RECT_H    = 0x00000000
GRADIENT_FILL_RECT_V    = 0x00000001
GRADIENT_FILL_TRIANGLE  = 0x00000002
GRADIENT_FILL_OP_FLAG   = 0x000000ff

#Flags value for COLORADJUSTMENT 
CA_NEGATIVE                 = 0x0001
CA_LOG_FILTER               = 0x0002

#IlluminantIndex values 
ILLUMINANT_DEVICE_DEFAULT   = 0
ILLUMINANT_A                = 1
ILLUMINANT_B                = 2
ILLUMINANT_C                = 3
ILLUMINANT_D50              = 4
ILLUMINANT_D55              = 5
ILLUMINANT_D65              = 6
ILLUMINANT_D75              = 7
ILLUMINANT_F2               = 8
ILLUMINANT_MAX_INDEX        = ILLUMINANT_F2

ILLUMINANT_TUNGSTEN         = ILLUMINANT_A
ILLUMINANT_DAYLIGHT         = ILLUMINANT_C
ILLUMINANT_FLUORESCENT      = ILLUMINANT_F2
ILLUMINANT_NTSC             = ILLUMINANT_C

#Min and max for RedGamma, GreenGamma, BlueGamma 
RGB_GAMMA_MIN               = 02500
RGB_GAMMA_MAX               = 65000

#Min and max for ReferenceBlack and ReferenceWhite 
REFERENCE_WHITE_MIN         = 6000
REFERENCE_WHITE_MAX         = 10000
REFERENCE_BLACK_MIN         = 0
REFERENCE_BLACK_MAX         = 4000

#Min and max for Contrast, Brightness, Colorfulness, RedGreenTint 
COLOR_ADJ_MIN               = -100
COLOR_ADJ_MAX               = 100


DI_APPBANDING               = 0x00000001
DI_ROPS_READ_DESTINATION    = 0x00000002

ICM_OFF               = 1
ICM_ON                = 2
ICM_QUERY             = 3
ICM_DONE_OUTSIDEDC    = 4

# Enhanced metafile constants.
ENHMETA_SIGNATURE       = 0x464D4520
# Stock object flag used in the object handle index in the enhanced
# metafile records.
# E.g. The object handle index (META_STOCK_OBJECT | BLACK_BRUSH)
# represents the stock object BLACK_BRUSH.

ENHMETA_STOCK_OBJECT    = auxfuncs.safe_long(0x80000000)

# Enhanced metafile record types.

EMR_HEADER                      = 1
EMR_POLYBEZIER                  = 2
EMR_POLYGON                     = 3
EMR_POLYLINE                    = 4
EMR_POLYBEZIERTO                = 5
EMR_POLYLINETO                  = 6
EMR_POLYPOLYLINE                = 7
EMR_POLYPOLYGON                 = 8
EMR_SETWINDOWEXTEX              = 9
EMR_SETWINDOWORGEX              = 10
EMR_SETVIEWPORTEXTEX            = 11
EMR_SETVIEWPORTORGEX            = 12
EMR_SETBRUSHORGEX               = 13
EMR_EOF                         = 14
EMR_SETPIXELV                   = 15
EMR_SETMAPPERFLAGS              = 16
EMR_SETMAPMODE                  = 17
EMR_SETBKMODE                   = 18
EMR_SETPOLYFILLMODE             = 19
EMR_SETROP2                     = 20
EMR_SETSTRETCHBLTMODE           = 21
EMR_SETTEXTALIGN                = 22
EMR_SETCOLORADJUSTMENT          = 23
EMR_SETTEXTCOLOR                = 24
EMR_SETBKCOLOR                  = 25
EMR_OFFSETCLIPRGN               = 26
EMR_MOVETOEX                    = 27
EMR_SETMETARGN                  = 28
EMR_EXCLUDECLIPRECT             = 29
EMR_INTERSECTCLIPRECT           = 30
EMR_SCALEVIEWPORTEXTEX          = 31
EMR_SCALEWINDOWEXTEX            = 32
EMR_SAVEDC                      = 33
EMR_RESTOREDC                   = 34
EMR_SETWORLDTRANSFORM           = 35
EMR_MODIFYWORLDTRANSFORM        = 36
EMR_SELECTOBJECT                = 37
EMR_CREATEPEN                   = 38
EMR_CREATEBRUSHINDIRECT         = 39
EMR_DELETEOBJECT                = 40
EMR_ANGLEARC                    = 41
EMR_ELLIPSE                     = 42
EMR_RECTANGLE                   = 43
EMR_ROUNDRECT                   = 44
EMR_ARC                         = 45
EMR_CHORD                       = 46
EMR_PIE                         = 47
EMR_SELECTPALETTE               = 48
EMR_CREATEPALETTE               = 49
EMR_SETPALETTEENTRIES           = 50
EMR_RESIZEPALETTE               = 51
EMR_REALIZEPALETTE              = 52
EMR_EXTFLOODFILL                = 53
EMR_LINETO                      = 54
EMR_ARCTO                       = 55
EMR_POLYDRAW                    = 56
EMR_SETARCDIRECTION             = 57
EMR_SETMITERLIMIT               = 58
EMR_BEGINPATH                   = 59
EMR_ENDPATH                     = 60
EMR_CLOSEFIGURE                 = 61
EMR_FILLPATH                    = 62
EMR_STROKEANDFILLPATH           = 63
EMR_STROKEPATH                  = 64
EMR_FLATTENPATH                 = 65
EMR_WIDENPATH                   = 66
EMR_SELECTCLIPPATH              = 67
EMR_ABORTPATH                   = 68

EMR_GDICOMMENT                  = 70
EMR_FILLRGN                     = 71
EMR_FRAMERGN                    = 72
EMR_INVERTRGN                   = 73
EMR_PAINTRGN                    = 74
EMR_EXTSELECTCLIPRGN            = 75
EMR_BITBLT                      = 76
EMR_STRETCHBLT                  = 77
EMR_MASKBLT                     = 78
EMR_PLGBLT                      = 79
EMR_SETDIBITSTODEVICE           = 80
EMR_STRETCHDIBITS               = 81
EMR_EXTCREATEFONTINDIRECTW      = 82
EMR_EXTTEXTOUTA                 = 83
EMR_EXTTEXTOUTW                 = 84
EMR_POLYBEZIER16                = 85
EMR_POLYGON16                   = 86
EMR_POLYLINE16                  = 87
EMR_POLYBEZIERTO16              = 88
EMR_POLYLINETO16                = 89
EMR_POLYPOLYLINE16              = 90
EMR_POLYPOLYGON16               = 91
EMR_POLYDRAW16                  = 92
EMR_CREATEMONOBRUSH             = 93
EMR_CREATEDIBPATTERNBRUSHPT     = 94
EMR_EXTCREATEPEN                = 95
EMR_POLYTEXTOUTA                = 96
EMR_POLYTEXTOUTW                = 97
EMR_SETICMMODE                  = 98
EMR_CREATECOLORSPACE            = 99
EMR_SETCOLORSPACE               = 100
EMR_DELETECOLORSPACE            = 101
EMR_GLSRECORD                   = 102
EMR_GLSBOUNDEDRECORD            = 103
EMR_PIXELFORMAT                 = 104
EMR_RESERVED_105                = 105
EMR_RESERVED_106                = 106
EMR_RESERVED_107                = 107
EMR_RESERVED_108                = 108
EMR_RESERVED_109                = 109
EMR_RESERVED_110                = 110
EMR_COLORCORRECTPALETTE         = 111
EMR_SETICMPROFILEA              = 112
EMR_SETICMPROFILEW              = 113
EMR_ALPHABLEND                  = 114
EMR_SETLAYOUT                   = 115
EMR_TRANSPARENTBLT              = 116
EMR_RESERVED_117                = 117
EMR_GRADIENTFILL                = 118
EMR_RESERVED_119                = 119
EMR_RESERVED_120                = 120
EMR_COLORMATCHTOTARGETW         = 121
EMR_CREATECOLORSPACEW           = 122
EMR_MIN                         = 1
EMR_MAX                         = 122

SETICMPROFILE_EMBEDED           = 0x00000001

CREATECOLORSPACE_EMBEDED        = 0x00000001

COLORMATCHTOTARGET_EMBEDED      = 0x00000001

GDICOMMENT_IDENTIFIER           = 0x43494447
GDICOMMENT_WINDOWS_METAFILE     = auxfuncs.safe_long(0x80000001)
GDICOMMENT_BEGINGROUP           = 0x00000002
GDICOMMENT_ENDGROUP             = 0x00000003
GDICOMMENT_MULTIFORMATS         = 0x40000004
EPS_SIGNATURE                   = 0x46535045
GDICOMMENT_UNICODE_STRING       = 0x00000040
GDICOMMENT_UNICODE_END          = 0x00000080

#LAYERPLANEDESCRIPTOR flags 
LPD_DOUBLEBUFFER        = 0x00000001
LPD_STEREO              = 0x00000002
LPD_SUPPORT_GDI         = 0x00000010
LPD_SUPPORT_OPENGL      = 0x00000020
LPD_SHARE_DEPTH         = 0x00000040
LPD_SHARE_STENCIL       = 0x00000080
LPD_SHARE_ACCUM         = 0x00000100
LPD_SWAP_EXCHANGE       = 0x00000200
LPD_SWAP_COPY           = 0x00000400
LPD_TRANSPARENT         = 0x00001000

LPD_TYPE_RGBA       = 0
LPD_TYPE_COLORINDEX = 1

#wglSwapLayerBuffers flags 
WGL_SWAP_MAIN_PLANE     = 0x00000001
WGL_SWAP_OVERLAY1       = 0x00000002
WGL_SWAP_OVERLAY2       = 0x00000004
WGL_SWAP_OVERLAY3       = 0x00000008
WGL_SWAP_OVERLAY4       = 0x00000010
WGL_SWAP_OVERLAY5       = 0x00000020
WGL_SWAP_OVERLAY6       = 0x00000040
WGL_SWAP_OVERLAY7       = 0x00000080
WGL_SWAP_OVERLAY8       = 0x00000100
WGL_SWAP_OVERLAY9       = 0x00000200
WGL_SWAP_OVERLAY10      = 0x00000400
WGL_SWAP_OVERLAY11      = 0x00000800
WGL_SWAP_OVERLAY12      = 0x00001000
WGL_SWAP_OVERLAY13      = 0x00002000
WGL_SWAP_OVERLAY14      = 0x00004000
WGL_SWAP_OVERLAY15      = 0x00008000
WGL_SWAP_UNDERLAY1      = 0x00010000
WGL_SWAP_UNDERLAY2      = 0x00020000
WGL_SWAP_UNDERLAY3      = 0x00040000
WGL_SWAP_UNDERLAY4      = 0x00080000
WGL_SWAP_UNDERLAY5      = 0x00100000
WGL_SWAP_UNDERLAY6      = 0x00200000
WGL_SWAP_UNDERLAY7      = 0x00400000
WGL_SWAP_UNDERLAY8      = 0x00800000
WGL_SWAP_UNDERLAY9      = 0x01000000
WGL_SWAP_UNDERLAY10     = 0x02000000
WGL_SWAP_UNDERLAY11     = 0x04000000
WGL_SWAP_UNDERLAY12     = 0x08000000
WGL_SWAP_UNDERLAY13     = 0x10000000
WGL_SWAP_UNDERLAY14     = 0x20000000
WGL_SWAP_UNDERLAY15     = 0x40000000