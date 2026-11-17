# this_file: generated/FL.py
# Generated from native API metadata; edit enrichment inputs, then merge.
'old FL-Python interface for FontGate'
from __future__ import annotations
from typing import Any
import builtins as _echopy_builtins
from fontlab_echopy._runtime import bind as _bind, unavailable as _unavailable

class Anchor:
    '===============================================\n  Anchor - class to represent Anchor point\n===============================================\nInteger values are accepted as coordinates\n\nCONSTRUCTOR:\n  Anchor() - generic constructor, creates an Anchor with zero coordinates and empty name\n  Anchor(Anchor) - copy constructor\n  Anchor(string name, integer x, integer y) - creates an Anchor and assigns name and coordinates.\n\nATTRIBUTES:\n  parent (read-only) - anchor\'s parent object, Glyph\n  name (string) - anchor\'s name as a string\n  x (integer) - horizontal position of the anchor\n  y (integer) - vertical position of the anchor\n  p (Point) - position of the anchor as a Point object\n\nOPERATIONS:\n\nMETHODS\n  Transform(Matrix m) - applies Matrix transformation to the Anchor(see Matrix().__doc__)\n  Layer(int layer_index) - returns position for the "layer_index" master\n  SetLayer(int layer_index, Point position) - sets "position" position for the "layer_index" master\n\nNative bases: object\n\nCaptured native MRO: Anchor, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Anchor.__init__')

    def Layer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Anchor.Layer; argument details are not documented.'
        _unavailable('FL.Anchor.Layer')

    def SetLayer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Anchor.SetLayer; argument details are not documented.'
        _unavailable('FL.Anchor.SetLayer')

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Anchor.Transform; argument details are not documented.'
        _unavailable('FL.Anchor.Transform')


class Canvas:
    "===============================================\n  Canvas - class to represent screen paint area and operations\n===============================================\nThis class can perform automatic coordinates transformations, so you can draw in Glyph coordinate space or, if you prefer, in screen coordinates directly\nUse constants defined for FontLab module to assign attributes to Canvas object\n\nCONSTRUCTOR:\n  ++ Never create Canvas object explicitly - they must be obtained from the FontLab's window classes\n  Canvas() - generic constructor, creates an empty Canvas\n  Canvas(Canvas) - copy constructor\n\nATTRIBUTES:\n  delta (Point) - horizontal shift during coordinates transformation\n  scale (Point(float)) - scaling during coordinates transformation\n  width (integer, read-only) - width of the canvas in pixels\n  height (integer, read-only) - height of the canvas in pixels\n  draw_style (integer, write-only) - sets current drawing mode (copy, XOR, invert etc.)\n  pen_color (integer, write-only) - sets current pen color\n  pen_style (integer, write-only) - sets current pen style (solid, dashed etc.)\n  brush_color (integer, write-only) - sets current brush color\n  brush_style (integer, write-only) -  sets current brush style (solid, patterned etc.)\n  text_color (integer, write-only) - sets color for a text\n  bk_color (integer, write-only) - sets color for a text background\n  bk_mode (integer, write-only) - sets background mode for a text output (transparent or opaque)\n\nOPERATIONS:\n\nMETHODS\n  MoveTo(Point p) | (x, y) - moves current position to p or (x, y) coordinates\n  LineTo(Point p) | (x, y) - draws a straight line to the position p or (x, y)\n  CurveTo(Point p0, Point p1, Point p2) - draws a 3th-order Bezier curve from the current point to points p0, p1, p2\n  SplineTo(Point p0, Point p1) - draws a 2th-order Bezier curve from the current point to points p0, p1\n  Ellipse(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - draws a filled ellipse defined by the Rect r, points p0 and p1 or set of coordinates\n  Rectangle(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - draws a filled rectangle defined by the Rect r, points p0 and p1 or set of coordinates\n  Convert(Point p) - converts coordinates from the source coordinate space to screen coordinates\n  UnConvert(Point p) - converts screen coordinates to the currently defined coordinate space\n  FitGlyph(Rect r, Glyph g) | (Rect r, Glyph g, WeightVector w) - recalculates parameters of coordinate conversion function to fit glyph g into rectangle r using currently selected options.\n  FillGlyph(Glyph g) | (Glyph g, WeightVector w) - fills the glyph g using current coordinate transformation.\n  OutlineGlyph(Glyph g) | (Glyph g, WeightVector w) - draws the glyph g outline using current coordinate transformation.\n  TextOut(Point p, string s) | (x, y, string s) - draws the string s in the position p or (x, y)\n  PutImage(Image i, Point p) | (Image i, Pioint p, int mode) - puts Image i at the selected point\n\nNative bases: object\n\nCaptured native MRO: Canvas, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Canvas.__init__')

    def Convert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.Convert; argument details are not documented.'
        _unavailable('FL.Canvas.Convert')

    def CurveTo(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.CurveTo; argument details are not documented.'
        _unavailable('FL.Canvas.CurveTo')

    def Ellipse(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.Ellipse; argument details are not documented.'
        _unavailable('FL.Canvas.Ellipse')

    def FillGlyph(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.FillGlyph; argument details are not documented.'
        _unavailable('FL.Canvas.FillGlyph')

    def FitGlyph(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.FitGlyph; argument details are not documented.'
        _unavailable('FL.Canvas.FitGlyph')

    def LineTo(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.LineTo; argument details are not documented.'
        _unavailable('FL.Canvas.LineTo')

    def MoveTo(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.MoveTo; argument details are not documented.'
        _unavailable('FL.Canvas.MoveTo')

    def OutlineGlyph(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.OutlineGlyph; argument details are not documented.'
        _unavailable('FL.Canvas.OutlineGlyph')

    def PutImage(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.PutImage; argument details are not documented.'
        _unavailable('FL.Canvas.PutImage')

    def Rectangle(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.Rectangle; argument details are not documented.'
        _unavailable('FL.Canvas.Rectangle')

    def SplineTo(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.SplineTo; argument details are not documented.'
        _unavailable('FL.Canvas.SplineTo')

    def TextOut(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.TextOut; argument details are not documented.'
        _unavailable('FL.Canvas.TextOut')

    def UnConvert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Canvas.UnConvert; argument details are not documented.'
        _unavailable('FL.Canvas.UnConvert')


class CmapTable:
    "===============================================\n  CmapTable - class to represent custom 'cmap' table record\n===============================================\nRefer to OpenType specification for information about constants used for platform, encoding, language and format\n\nCONSTRUCTOR:\n  CmapTable() - generic constructor, creates an empty name record\n  CmapTable(CmapTable) - copy constructor\n  CmapTable((pid, eid, lid, format, type, pagename)) - defines name receiving all values from a tuple\n  CmapTable(pid, eid, lid, format, type, pagename) - defines name receiving all values from parameters of constructor\n\nATTRIBUTES:\n  parent (read-only) - parent object, Font\n  pid (integer) - platform identifier\n  eid (integer) - encoding identifier\n  lid (integer) - language identifier\n  format (integer) - cmap subtable format (see OpenType specification)\n  type (integer) - subtable type (see CMAPTYPE_XXX constants)\n  pagename (string) - name of the attached codepage\n\nOPERATIONS:\n\nMETHODS\n\nNative bases: object\n\nCaptured native MRO: CmapTable, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.CmapTable.__init__')


class Component:
    '===============================================\n  Component - class to represent glyph component\n===============================================\nComponents are defined by the glyph index which they reference, shift of components origin point and scale factor of a component\nscale is measured in relation to 1.0, so 100% scale is 1.0 and 60% - 0.6\nThis class is Multiple Master - compatible\n\nCONSTRUCTOR:\n  Component() - generic constructor, creates an empty Component\n  Component(Component) - copy constructor\n  Component(index) - creates component referencing glyph index with zero shift and 100% scale\n  Component(index, Point(integer) delta) - creates component referencing glyph index with delta shift and 100% scale\n  Component(index, Point(integer) delta, Point(float) scale) - creates component referencing glyph index with delta shift and scale factor defined by scale\n\nATTRIBUTES:\n  parent (read-only) - parent object, Glyph\n  index (integer) - referencing glyph index\n  delta (Point(integer)) - shift value\n  scale (Point(float)) - scale factor\n  deltas [(Point(integer))]- list of shift values for each master\n  scales [(Point(float))] - list of scale values for each master\n\nOPERATIONS:\n\nMETHODS\n  Get() | (Font f) - creates a glyph from component applying delta and scale transformations. Font parameter is not needed when component has a parent\n  Paste() - appends component to a parent glyph as a set of outlines. Component must have a parent\n\nNative bases: object\n\nCaptured native MRO: Component, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Component.__init__')

    def Get(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Component.Get; argument details are not documented.'
        _unavailable('FL.Component.Get')

    def Paste(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Component.Paste; argument details are not documented.'
        _unavailable('FL.Component.Paste')

    def transform(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Component.transform; argument details are not documented.'
        _unavailable('FL.Component.transform')


class Dialog:
    "===============================================\n  Dialog - class to represent Dialog\n===============================================\nNote that objects of this class cannot be created explicitly, they are only generated as a result of Glyph().Audit() operation\n\nCONSTRUCTOR:\n  Dialog(DialogClass) - generic constructor\n\nATTRIBUTES:\n  title - dialog title\n  ok - text on the OK button\n  cancel - text on the Cancel button\n  position - position of the dialog's origin\n  size - dialog size\n  rectangle (combination of size and position)\n\nOPERATIONS:\n\nMETHODS\n  Center()                    - center dialog on screen\n  AddControl(integer ControlType, Rect dimension, string identifier, integer ControlStyle)\n                              - adds a control to the dialog, see FLdict for\n                                Type- and Style-constants\n  GetValue(string identifier) - get value from the specified control\n  PutValue(string identifier) - put value to the specified control\n  Enable(string identifier, integer value)\n                              - enable (value=1) or disable (value=0) the specified control\n  Show(string identifier, integer value)\n                              - show (value=1) or hide (value=0) the specified control\n  SetLabel(string identifier, string value)\n                              - set the label of the specified control\n  GetRect(string identifier)  - get dimension of the specified control as a Rect object\n  Repaint(string identifier)  - redraw the specified (custom)control\n  Run()                       - run the dialog\n  End()|End(integer returnvalue) - end the dialog\n\nNative bases: object\n\nCaptured native MRO: Dialog, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Dialog.__init__')

    def AddControl(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.AddControl; argument details are not documented.'
        _unavailable('FL.Dialog.AddControl')

    def Center(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.Center; argument details are not documented.'
        _unavailable('FL.Dialog.Center')

    def Enable(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.Enable; argument details are not documented.'
        _unavailable('FL.Dialog.Enable')

    def End(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.End; argument details are not documented.'
        _unavailable('FL.Dialog.End')

    def GetRect(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.GetRect; argument details are not documented.'
        _unavailable('FL.Dialog.GetRect')

    def GetValue(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.GetValue; argument details are not documented.'
        _unavailable('FL.Dialog.GetValue')

    def MoveTo(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.MoveTo; argument details are not documented.'
        _unavailable('FL.Dialog.MoveTo')

    def PutValue(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.PutValue; argument details are not documented.'
        _unavailable('FL.Dialog.PutValue')

    def Repaint(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.Repaint; argument details are not documented.'
        _unavailable('FL.Dialog.Repaint')

    def Run(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.Run; argument details are not documented.'
        _unavailable('FL.Dialog.Run')

    def SetLabel(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.SetLabel; argument details are not documented.'
        _unavailable('FL.Dialog.SetLabel')

    def Show(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Dialog.Show; argument details are not documented.'
        _unavailable('FL.Dialog.Show')

    cancel: Any
    ok: Any
    position: Any
    rectangle: Any
    size: Any
    title: Any

class Encoding:
    'Encoding\n\nNative bases: object\n\nCaptured native MRO: Encoding, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Encoding.__init__')

    def FillUnencoded(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Encoding.FillUnencoded; argument details are not documented.'
        _unavailable('FL.Encoding.FillUnencoded')

    def FillUnicodes(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Encoding.FillUnicodes; argument details are not documented.'
        _unavailable('FL.Encoding.FillUnicodes')

    def FindName(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Encoding.FindName; argument details are not documented.'
        _unavailable('FL.Encoding.FindName')

    def Load(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Encoding.Load; argument details are not documented.'
        _unavailable('FL.Encoding.Load')

    def Save(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Encoding.Save; argument details are not documented.'
        _unavailable('FL.Encoding.Save')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Encoding.append; argument details are not documented.'
        _unavailable('FL.Encoding.append')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Encoding.insert; argument details are not documented.'
        _unavailable('FL.Encoding.insert')


class EncodingRecord:
    'EncodingRecord\n\nNative bases: object\n\nCaptured native MRO: EncodingRecord, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.EncodingRecord.__init__')


class Feature:
    "===============================================\n  Feature - class to represent OpenType feature-definition record\n===============================================\n\nCONSTRUCTOR:\n  Feature() - generic constructor, creates an empty Feature record\n  Feature(Feature) - copy constructor\n  Feature(string tag) - creates feature, assigns 'tag' and empty value\n  Feature(string tag, string value) - creates feature and assigns values to both attributes\n\nATTRIBUTES:\n  parent (read-only) - parent object, Font\n  tag (string) - feature's tag\n  value (string) - feature's text\n\nOPERATIONS:\n\nMETHODS\n\nNative bases: object\n\nCaptured native MRO: Feature, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Feature.__init__')


class Features:
    'OT Features array\n\nNative bases: object\n\nCaptured native MRO: Features, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Features.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Features.append; argument details are not documented.'
        _unavailable('FL.Features.append')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Features.clean; argument details are not documented.'
        _unavailable('FL.Features.clean')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Features.insert; argument details are not documented.'
        _unavailable('FL.Features.insert')


class Font:
    "===============================================\n  Font - base class to represent font\n===============================================\n\nCONSTRUCTOR:\n  Font() - generic constructor, creates an empty Font  Font(Font) - copy constructor\n  Font(string filename) - creates a Font and assigns name of the file from which it was opened\n\nATTRIBUTES:\n\n  NAMES, COPYRIGHT AND IDENTIFICATION\n  family_name(string) - font Family Name\n  style_name\n  full_name(string) - font Full Name\n  font_name(string) - font Font Name\n  font_style(integer) - Font Style\n  menu_name(string) - font menu name\n  weight\n  weight_code\n  width\n  designer\n  designer_url\n  fontnames[NameRecord] - list of font name records\n  copyright(string) - Copyright name field\n  notice(string) - Notice field\n  note(string) - Font note\n  unique_id\n  tt_u_id\n  tt_version\n  trademark\n  x_u_id_num\n  x_u_id\n  vendor\n  vendor_url\n  version\n  year\n  version_major\n  version_minor\n  vp_id\n  ms_charset\n  ms_id\n  panose[integer] - list of Panose values\n  collection[collection] - list of glyph indexes in FontLab collection\n  pcl_chars_set\n  pcl_id\n\n  DIMENSIONS\n  upm\n  ascender[integer] - list of ascenders, one for each master\n  descender[integer] - list of descenders, one for each master\n  cap_height[integer] - list of CapHeight records, one for each master\n  x_height[integer] - list of xHeight values, one for each master\n  default_width\n  slant_angle\n  italic_angle(float) - Italic Angle\n  is_fixed_pitch\n  underline_position\n  underline_thickness\n\n  ALIGNMENT\n  blue_fuzz\n  blue_scale\n  blue_shift\n  blue_values_num(integer) - number of defined blue values\n  blue_values[integer[integer]] - two-dimentional array of BlueValues - master index is top-level index\n  family_blues_num(integer) - number of FamilyBlues records\n  family_blues[integer[integer]] - two-dimentional array of FamilyBlues - master index is top-level index\n  family_other_blues_num(integer) - number of FamilyOtherBlues records\n  family_other_blues[integer[integer]] - two-dimentional array of FamilyOtherBlues - master index is top-level index\n  force_bold[integer] - list of Force Bold values, one for each master\n  other_blues_num\n  other_blues[integer[integer]] - two-dimentional array of OtherBlues - master index is top-level index\n  stem_snap_h_num\n  stem_snap_h\n  stem_snap_v_num\n  stem_snap_v\n\n  OTHER ATTRIBUTES\n  classes[string] - list of glyph classes\n  ot_classes - OpenType classes data\n  classes_text - glyph classes compiled in ot_classes format\n  features[Feature] - list of OpenType features\n  customdata(string) - font custom data field\n  truetypetables[TrueTypeTable] - list of custom TrueType tables\n  ttinfo(TTInfo) - loaded TrueType information (mostly hinting-related tables)\n  encoding\n  glyphs[Glyph] - array of glyphs\n  source\n  weight_vector\n  measurement - position of the measurement line for the font\n\nOPERATIONS:\n  len - returns number of glyphs\n  [] - accesses glyphs array\n\nMETHODS\n  New() - clears the font\n  Open(string filename) - opens font from VFB format\n  Save(string filename) - saves font in VFB format\n  Reencode()  FindGlyph(string name) | (Uni unicode) | (integer Unicode) - finds glyph and return its index or -1\n  DefineAxis(string Name, string Type, string ShortName) - defines the new Multiple Master axis\n  DeleteAxis(axisindex, float position) - removes the axis\n  GenerateUnicode() - generates Unicode indexes for all glyphs\n  GenerateNames() - generates names for all glyphs\n  GenerateGlyph(string glyphname) - generates new glyph using 'glyphname' as a source of information about glyph's composition\n  MakeKernFeature([WeightVector vector]) - generates 'kern' feature using font kerning and classes\n  MergeFonts(Font source[, flags]) - appends all glyphs from the source font. Check mfXXXX constants for options\n  SetClassFlags(int class_index, bool left, bool right) - allows to set 'left' and 'right' properties of the kerning class   SetClassFlags(int class_index, bool lsb, bool rsb, bool width) - allows to set 'lsb', 'rsb' and 'width' properties of the metrics class   GetClassLeft(int class_index) - returns the 'left' property of the class  GetClassRight(int class_index) - returns the 'right' property of the class  GetClassMetricsFlags(int class_index) - returns the tuple containing LSB, RSB and Width flags of the metrics class\n\nNative bases: object\n\nCaptured native MRO: Font, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Font.__init__')

    def DefineAxis(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.DefineAxis; argument details are not documented.'
        _unavailable('FL.Font.DefineAxis')

    def DeleteAxis(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.DeleteAxis; argument details are not documented.'
        _unavailable('FL.Font.DeleteAxis')

    def FindGlyph(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.FindGlyph; argument details are not documented.'
        _unavailable('FL.Font.FindGlyph')

    def GenerateGlyph(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.GenerateGlyph; argument details are not documented.'
        _unavailable('FL.Font.GenerateGlyph')

    def GenerateNames(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.GenerateNames; argument details are not documented.'
        _unavailable('FL.Font.GenerateNames')

    def GenerateUnicode(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.GenerateUnicode; argument details are not documented.'
        _unavailable('FL.Font.GenerateUnicode')

    def GetClassLeft(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.GetClassLeft; argument details are not documented.'
        _unavailable('FL.Font.GetClassLeft')

    def GetClassMetricsFlags(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.GetClassMetricsFlags; argument details are not documented.'
        _unavailable('FL.Font.GetClassMetricsFlags')

    def GetClassRight(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.GetClassRight; argument details are not documented.'
        _unavailable('FL.Font.GetClassRight')

    def MakeKernFeature(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.MakeKernFeature; argument details are not documented.'
        _unavailable('FL.Font.MakeKernFeature')

    def MergeFonts(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.MergeFonts; argument details are not documented.'
        _unavailable('FL.Font.MergeFonts')

    def New(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.New; argument details are not documented.'
        _unavailable('FL.Font.New')

    def Open(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.Open; argument details are not documented.'
        _unavailable('FL.Font.Open')

    def OpenAFM(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.OpenAFM; argument details are not documented.'
        _unavailable('FL.Font.OpenAFM')

    def Save(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.Save; argument details are not documented.'
        _unavailable('FL.Font.Save')

    def SaveAFM(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.SaveAFM; argument details are not documented.'
        _unavailable('FL.Font.SaveAFM')

    def SetClassFlags(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.SetClassFlags; argument details are not documented.'
        _unavailable('FL.Font.SetClassFlags')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Font.has_key; argument details are not documented.'
        _unavailable('FL.Font.has_key')


class Glyph:
    "===============================================\n  Glyph - class to represent glyph\n===============================================\n\nCONSTRUCTOR:\n  Glyph() - generic constructor, creates an empty glyph\n  Glyph(Glyph) - copy constructor\n  Glyph(masterscount) - creates a glyph with 'masterscount' number of masters\n  Glyph(masterscount, [Node, ...]) - creates a glyph with 'masterscount' number of masters and assigns a list of nodes\n\nATTRIBUTES:\n  parent (read-only) - Glyph's parent object\n  nodes [Node] - list of Nodes\n  customdata (string) - custom data defined for this glyph\n  note (string) - note defined for this glyph\n  mark (integer) - True if glyph is marked\n  anchors [Anchor] - list of anchors\n  hhints [Hint] - list of horizontal hints\n  vhints [Hint] - list of vertical hints\n  hlinks [Link] - list of horizontal links\n  vlinks [Link] - list of vertical links\n  components [Component] - list of componets\n  replace_table [Replace] - hint replacing program, list of Replace objects\n  kerning [KerningPair] - list of kerning pairs\n  layers_number (integer) - number of masters\n  flags (integer) - flags set for this glyph\n  nodes_number (integer) - number of nodes, same as 'len(Glyph)'\n  width (integer) - advance width for the first master\n  height (integer) - advance height for the first master\n  unicode (integer) - first Unicode index in integer form\n  unicodes [integer] - list of Unicode indexes\n  name (string) - glyph name\n  mask (string) - mask\n\n  STORED TRUETYPE DATA\n  advance_width (integer)\n  advance_height (integer)\n  left_side_bearing (integer)\n  top_side_bearing (integer)\n  y_pels (integer)\n  bounding_box (Rect)\n  number_of_contours (integer)\n  end_points [integer]\n  points [TTPoint]\n  instructions [Byte]\n  hdmx[Byte]\n\nOPERATIONS:\n  len() - returns number of nodes in the glyph\n  [] - can be used to access individial nodes\n  slice - can be used to access portion of the glyph's nodes array\n  + or concatination - can be used to append Glyph, Node or sequence of Nodes\n  multiply - second operand must be Matrix, applies matrix transformation to a glyph\n\nMETHODS\n  Assign (Glyph) - copies all information from the assigned glyph\n  Transform(Matrix m) - applies Matrix transformation to the Glyph (see Matrix().__doc__)\n  SetLayersNumber(mastersnumber) - changes the number of masters, is applicable only to glyphs that have no parent\n  Clear() - removes all nodes\n  Add - refer to '+' operator\n  Insert (Node | Glyph | [Node]) | (Node | Glyph | [Node], nodeindex) - inserts Node, Glyph or sequence of Nodes at the begining of glyph's nodes or at specified node index\n  Present (style) - returns True if a layer or a combination of layers are present in the glyph\n  Delete (index) | (index0, index1) - removes node or range of nodes\n  ExpandLayer (masterindex) - expands selected master to all other masters\n  Shift (Point) | (Point, masterindex) - shifts positions of all nodes at first or specified master\n  Scale (Point(float) scale) | (Point(float) scale, Point center) | (Point(float) scale, Point center, masterindex) - scales the glyph\n  Layer (masterindex) - returns list of Points for all nodes for the selected master\n  Section (masterindex, pointindex, nodetype) - returns list of Points that conform to selected options\n  MoveNode(...) - moves the node copying Edit tool behavior (see User manual for details)\n  DeleteNode(nodeindex) - removes the node\n  InsertNode(nodeindex) | (nodeindex, float time) | (nodeindex, float time, masterindex) - insers new node on a contour\n  SELECTION OPERATIONS\n  Selection() - returns list of selected nodes\n  SelectAll() - selects all nodes\n  UnselectAll() - deselects all nodes\n  InvertSelection() - selects unselected nodes and deselects selected nodes\n  isAnySelected() - returns True if at least one node is selected\n  SelectedCount() - returns number of selected nodes\n  SelectRect(Rect r) | (Rect r, masterindex) - selects all nodes that are inside the rectangle\n  UnselectRect(Rect r) | (Rect r, masterindex) - deselects all nodes that are inside the rectangle\n  DeleteSelected() - deletes all selected nodes\n\n  METRICS AND BBOX OPERATIONS\n  GetBoundingRect() | (masterindex) - returns Rect - bounding box of the glyph\n  GetMetrics() | (masterindex) - returns glyph advance width and advance height in a form of Point\n  SetMetrics(Point p) | (Point p, masterindex) - assigns new values to the width and height of the glyph\n  GetVSB() | (masterindex) - returns glyph bottom sidebearing position\n  SetVSB(value) | (value, masterindex) - assigns new values to the bottom sidebearing of the glyph\n\n  OVERLAP OPERATIONS\n  RemoveOverlap() | (masterindex) - removes overlap\n  Badd(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Add operation with the glyph or list of nodes\n  Bsubtract(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Subtract operation with the glyph or list of nodes\n  Bintersect(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Insersect operation with the glyph or list of nodes\n\n  OPERATIONS ON CONTOURS\n  GetContoursNumber() - returns number of contours in the glyph\n  GetContourBegin(contourindex) - returns index of the first node for a contour\n  GetContourLength(contourindex) - returns number of nodes in a contour\n  SelectContour(contourindex) - selects all nodes in the contour\n  DeleteContour(contourindex) - removes contour\n  ReverseContour(contourindex) - reverses contour's direction\n  ReorderContour(contourindex, newindex) - reorders contours in the glyph\n  isContourClockwise(contourindex) - returns True if direction of contour is clockwise\n  SetStartNode(nodeindex) - makes the node a starting node of the contour\n  FindContour(nodeindex) - returns number of contour containing the 'nodeindex'\n\n  HINTS OPERATIONS\n  RemoveHints(mode) - removes hints and links\n  Autohint() | (masterindex) - automatically generates Type 1 hints\n\n  ANCHOR OPERATIONS\n  FindAnchor(string name) - finds anchor by name\n\n  TRANSFORMATION ACTIONS\n  Decompose() - pastes all components to the glyph outline\n  MakeExtremeNodes() | (masterindex) - automatically detects and adds extreme nodes\n  Audit() | (masterindex) - performs test of the glyph and returns list of AuditRecord objects\n  Iterate(Iterator) - iterates glyph trough iterator class which must unclude following methods: \n     Start(); ClosePath(); StartPath(Node); LineTo(Node); CurveTo(Node); SplineTo(Node); Finish()\n  Rotate3D\n  Extrude3D(outlinewidth, shift_x, shift_y)\n  Shadow(outlinewidth, shift_x, shift_y)\n  College(outlinewidth, distance)\n  Gradient(outlinewidth, direction, stripes_number, start_y, finish_y)\n  Distance(width_x, width_y, cornermode) | (width_x, width_y, cornermode, Glyph dest)\n  Interpolate([(nodeindex, Point newposition])\n  Warp([Point], float force)\n  Rasterize() | Rasterize(Image, [, active layer[, height]]) | Rasterize(Image, [, WeightVector[, height]]) - rasterizes glyph to the Image or to glyph's background. Returns resulting image_rect. Height is relative to font's UPM\n         Blend(Glyph source, integer layer1, integer layer2, Point amount) - returns blend of the glyph and source\n         JoinAll() - tries to join all open contours\n         SaveEPS(string filename) | (string filename, layer) - writes layer into the EPS file named filename\n         LoadEPS(string filename) - reads EPS from filename and returns Glyph object. Use Assign method to replace current glyph with the loaded outline\n  R([Point], float force)\n\nNative bases: object\n\nCaptured native MRO: Glyph, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Glyph.__init__')

    def Add(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Add; argument details are not documented.'
        _unavailable('FL.Glyph.Add')

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Assign; argument details are not documented.'
        _unavailable('FL.Glyph.Assign')

    def Audit(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Audit; argument details are not documented.'
        _unavailable('FL.Glyph.Audit')

    def Autohint(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Autohint; argument details are not documented.'
        _unavailable('FL.Glyph.Autohint')

    def Badd(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Badd; argument details are not documented.'
        _unavailable('FL.Glyph.Badd')

    def Bintersect(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Bintersect; argument details are not documented.'
        _unavailable('FL.Glyph.Bintersect')

    def Blend(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Blend; argument details are not documented.'
        _unavailable('FL.Glyph.Blend')

    def Bsubtract(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Bsubtract; argument details are not documented.'
        _unavailable('FL.Glyph.Bsubtract')

    def Clear(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Clear; argument details are not documented.'
        _unavailable('FL.Glyph.Clear')

    def College(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.College; argument details are not documented.'
        _unavailable('FL.Glyph.College')

    def Decompose(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Decompose; argument details are not documented.'
        _unavailable('FL.Glyph.Decompose')

    def Delete(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Delete; argument details are not documented.'
        _unavailable('FL.Glyph.Delete')

    def DeleteContour(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.DeleteContour; argument details are not documented.'
        _unavailable('FL.Glyph.DeleteContour')

    def DeleteNode(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.DeleteNode; argument details are not documented.'
        _unavailable('FL.Glyph.DeleteNode')

    def DeleteSelected(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.DeleteSelected; argument details are not documented.'
        _unavailable('FL.Glyph.DeleteSelected')

    def Distance(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Distance; argument details are not documented.'
        _unavailable('FL.Glyph.Distance')

    def EditMask(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.EditMask; argument details are not documented.'
        _unavailable('FL.Glyph.EditMask')

    def ExchangeMask(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.ExchangeMask; argument details are not documented.'
        _unavailable('FL.Glyph.ExchangeMask')

    def ExpandLayer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.ExpandLayer; argument details are not documented.'
        _unavailable('FL.Glyph.ExpandLayer')

    def Extrude3D(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Extrude3D; argument details are not documented.'
        _unavailable('FL.Glyph.Extrude3D')

    def FindAnchor(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.FindAnchor; argument details are not documented.'
        _unavailable('FL.Glyph.FindAnchor')

    def FindContour(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.FindContour; argument details are not documented.'
        _unavailable('FL.Glyph.FindContour')

    def GetBoundingRect(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.GetBoundingRect; argument details are not documented.'
        _unavailable('FL.Glyph.GetBoundingRect')

    def GetContourBegin(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.GetContourBegin; argument details are not documented.'
        _unavailable('FL.Glyph.GetContourBegin')

    def GetContourLength(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.GetContourLength; argument details are not documented.'
        _unavailable('FL.Glyph.GetContourLength')

    def GetContoursNumber(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.GetContoursNumber; argument details are not documented.'
        _unavailable('FL.Glyph.GetContoursNumber')

    def GetMetrics(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.GetMetrics; argument details are not documented.'
        _unavailable('FL.Glyph.GetMetrics')

    def Gradient(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Gradient; argument details are not documented.'
        _unavailable('FL.Glyph.Gradient')

    def Insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Insert; argument details are not documented.'
        _unavailable('FL.Glyph.Insert')

    def InsertNode(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.InsertNode; argument details are not documented.'
        _unavailable('FL.Glyph.InsertNode')

    def Interpolate(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Interpolate; argument details are not documented.'
        _unavailable('FL.Glyph.Interpolate')

    def InvertSelection(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.InvertSelection; argument details are not documented.'
        _unavailable('FL.Glyph.InvertSelection')

    def Iterate(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Iterate; argument details are not documented.'
        _unavailable('FL.Glyph.Iterate')

    def JoinAll(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.JoinAll; argument details are not documented.'
        _unavailable('FL.Glyph.JoinAll')

    def Layer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Layer; argument details are not documented.'
        _unavailable('FL.Glyph.Layer')

    def LoadEPS(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.LoadEPS; argument details are not documented.'
        _unavailable('FL.Glyph.LoadEPS')

    def MakeExtremeNodes(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.MakeExtremeNodes; argument details are not documented.'
        _unavailable('FL.Glyph.MakeExtremeNodes')

    def MoveNode(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.MoveNode; argument details are not documented.'
        _unavailable('FL.Glyph.MoveNode')

    def Present(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Present; argument details are not documented.'
        _unavailable('FL.Glyph.Present')

    def Rasterize(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Rasterize; argument details are not documented.'
        _unavailable('FL.Glyph.Rasterize')

    def RemoveHints(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.RemoveHints; argument details are not documented.'
        _unavailable('FL.Glyph.RemoveHints')

    def RemoveOverlap(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.RemoveOverlap; argument details are not documented.'
        _unavailable('FL.Glyph.RemoveOverlap')

    def ReorderContour(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.ReorderContour; argument details are not documented.'
        _unavailable('FL.Glyph.ReorderContour')

    def ReverseContour(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.ReverseContour; argument details are not documented.'
        _unavailable('FL.Glyph.ReverseContour')

    def Rotate3D(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Rotate3D; argument details are not documented.'
        _unavailable('FL.Glyph.Rotate3D')

    def SaveEPS(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SaveEPS; argument details are not documented.'
        _unavailable('FL.Glyph.SaveEPS')

    def Scale(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Scale; argument details are not documented.'
        _unavailable('FL.Glyph.Scale')

    def Section(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Section; argument details are not documented.'
        _unavailable('FL.Glyph.Section')

    def SelectAll(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SelectAll; argument details are not documented.'
        _unavailable('FL.Glyph.SelectAll')

    def SelectContour(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SelectContour; argument details are not documented.'
        _unavailable('FL.Glyph.SelectContour')

    def SelectRect(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SelectRect; argument details are not documented.'
        _unavailable('FL.Glyph.SelectRect')

    def SelectedCount(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SelectedCount; argument details are not documented.'
        _unavailable('FL.Glyph.SelectedCount')

    def Selection(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Selection; argument details are not documented.'
        _unavailable('FL.Glyph.Selection')

    def SetLayersNumber(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SetLayersNumber; argument details are not documented.'
        _unavailable('FL.Glyph.SetLayersNumber')

    def SetMetrics(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SetMetrics; argument details are not documented.'
        _unavailable('FL.Glyph.SetMetrics')

    def SetStartNode(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.SetStartNode; argument details are not documented.'
        _unavailable('FL.Glyph.SetStartNode')

    def Shadow(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Shadow; argument details are not documented.'
        _unavailable('FL.Glyph.Shadow')

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Shift; argument details are not documented.'
        _unavailable('FL.Glyph.Shift')

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Transform; argument details are not documented.'
        _unavailable('FL.Glyph.Transform')

    def UnselectAll(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.UnselectAll; argument details are not documented.'
        _unavailable('FL.Glyph.UnselectAll')

    def UnselectRect(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.UnselectRect; argument details are not documented.'
        _unavailable('FL.Glyph.UnselectRect')

    def Warp(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.Warp; argument details are not documented.'
        _unavailable('FL.Glyph.Warp')

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.clear; argument details are not documented.'
        _unavailable('FL.Glyph.clear')

    def isAnySelected(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.isAnySelected; argument details are not documented.'
        _unavailable('FL.Glyph.isAnySelected')

    def isContourClockwise(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Glyph.isContourClockwise; argument details are not documented.'
        _unavailable('FL.Glyph.isContourClockwise')


class Guide:
    "===============================================\n  Guide - class to represent guideline\n===============================================\nThis class is Multiple Master - compatible\n\nCONSTRUCTOR:\n  Guide() - generic constructor, creates a Guide with zero coordinates\n  Guide(Guide) - copy constructor\n  Guide(position) - creates a Guide and assigns position\n  Guide(position, angle) - creates a Guide and assigns position and width values\n\nATTRIBUTES:\n  parent (read-only) - Guide's parent object, Glyph\n  position (integer) - position of the guideline\n  width (integer) - width of the guideline\n  angle (float) - angle of the guide (degrees)\n  positions [(integer)] - list of positions for each master\n  widths [(integer)] - list of widths for each master\n\nOPERATIONS:\n\nMETHODS\n  Transform(Matrix m) - applies Matrix transformation to the Guide (see Matrix().__doc__)\n  TransformLayer(Matrix m, layernum) - applies Matrix transformation to the selected layer of the Guide\n\nNative bases: object\n\nCaptured native MRO: Guide, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Guide.__init__')

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Guide.Transform; argument details are not documented.'
        _unavailable('FL.Guide.Transform')

    def TransformLayer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Guide.TransformLayer; argument details are not documented.'
        _unavailable('FL.Guide.TransformLayer')


class Hint:
    "===============================================\n  Hint - class to represent hint\n===============================================\nThis class is Multiple Master - compatible\n\nCONSTRUCTOR:\n  Hint() - generic constructor, creates a Hint with zero coordinates\n  Hint(Hint) - copy constructor\n  Hint(position, width) - creates a Hint and assigns position and width values\n\nATTRIBUTES:\n  parent (read-only) - Hint's parent object, Glyph\n  position (integer) - position of the hint\n  width (integer) - width of the hint\n  positions [(integer)] - list of positions for each master\n  widths [(integer)] - list of widths for each master\n\nOPERATIONS:\n\nMETHODS\n  ToLink() - transforms hint to Link (and returns it as a result) using parent as a source of node coordinates. Parent must exist\n  Transform(Matrix m) - applies Matrix transformation to the Hint (see Matrix().__doc__)\n  TransformLayer(Matrix m, layernum) - applies Matrix transformation to the selected layer of the Hint\n\nNative bases: object\n\nCaptured native MRO: Hint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Hint.__init__')

    def ToLink(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Hint.ToLink; argument details are not documented.'
        _unavailable('FL.Hint.ToLink')

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Hint.Transform; argument details are not documented.'
        _unavailable('FL.Hint.Transform')

    def TransformLayer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Hint.TransformLayer; argument details are not documented.'
        _unavailable('FL.Hint.TransformLayer')


class Image:
    '===============================================\n  Image - class to represent bitmap image\n===============================================\n\nCONSTRUCTOR:\n  Image() - generic constructor, creates a Image with zero coordinates\n  Image(Image) - copy constructor\n  Image(index1, index2) - creates a Image between nodes index1 and index2\n\nATTRIBUTES:\n  width, height (integer) [read-only] - dimensions of the image\n  empty (integer) [read-only] - empty status of the image\n  size (integer) [read-only] - size of the image buffer\n  data (string)  - image data as string with length\n  traceenabled () [read-only] - there is a possibility to trace the image with the Trace command\n\nOPERATIONS:\n  Trace (Glyph) - Traces the image with the current option and adds it to the glyph\n\nMETHODS\n  \n\nNative bases: object\n\nCaptured native MRO: Image, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Image.__init__')

    def Clear(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.Clear; argument details are not documented.'
        _unavailable('FL.Image.Clear')

    def Create(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.Create; argument details are not documented.'
        _unavailable('FL.Image.Create')

    def GetPixel(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.GetPixel; argument details are not documented.'
        _unavailable('FL.Image.GetPixel')

    def HLine(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.HLine; argument details are not documented.'
        _unavailable('FL.Image.HLine')

    def ImageBlt(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.ImageBlt; argument details are not documented.'
        _unavailable('FL.Image.ImageBlt')

    def Invert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.Invert; argument details are not documented.'
        _unavailable('FL.Image.Invert')

    def SetPixel(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.SetPixel; argument details are not documented.'
        _unavailable('FL.Image.SetPixel')

    def Trace(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Image.Trace; argument details are not documented.'
        _unavailable('FL.Image.Trace')


class KerningArray:
    'KerningArray(void)\n\nNative bases: object\n\nCaptured native MRO: KerningArray, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.KerningArray.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.KerningArray.append; argument details are not documented.'
        _unavailable('FL.KerningArray.append')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.KerningArray.clean; argument details are not documented.'
        _unavailable('FL.KerningArray.clean')


class KerningPair:
    "===============================================\n  KerningPair - class to represent kerning pair\n===============================================\nThis class is Multiple Master - compatible\n\nCONSTRUCTOR:\n  KerningPair() - generic constructor, creates an empty KerningPair\n  KerningPair(KerningPair) - copy constructor\n  KerningPair(index) - creates a KerningPair to glyph referenced by index but zero value\n  KerningPair(index, value) - creates a KerningPair to glyph referenced by index but and assigns value\n\nATTRIBUTES:\n  parent (read-only) - KerningPair's parent object, Glyph\n  key (integer) - index of right glyph of the pair\n  value (integer) - value of the pair\n  values [(integer)] - list of values for each master\n\nOPERATIONS:\n\nMETHODS\n\nNative bases: object\n\nCaptured native MRO: KerningPair, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.KerningPair.__init__')


class Link:
    "===============================================\n  Link - class to represent link\n===============================================\n\nCONSTRUCTOR:\n  Link() - generic constructor, creates a Link with zero coordinates\n  Link(Link) - copy constructor\n  Link(index1, index2) - creates a Link between nodes index1 and index2\n\nATTRIBUTES:\n  parent (read-only) - Link's parent object, Glyph\n  node1, node2 (integer) - indexes of the nodes that are linked\n\nOPERATIONS:\n\nMETHODS\n  ToHint() - transforms link to Hint (and returns it as a result) using parent as a source of node coordinates. Parent must exist\n\nNative bases: object\n\nCaptured native MRO: Link, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Link.__init__')

    def ToHint(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Link.ToHint; argument details are not documented.'
        _unavailable('FL.Link.ToHint')


class Matrix:
    "===============================================\n  Matrix - class to represent planar transformations\n===============================================\nMatrix is used to perform following transformations:\n  x1 = x * a + y * b + e\n  y1 = x * c + y * d + f\n\nCONSTRUCTOR:\n  Matrix() - generic constructor, creates a Matrix that makes no change to coordinates\n  Matrix(Matrix) - copy constructor\n  Matrix([a, b, c, d, e, f]) - creates a Matrix and assigns coordinates from the list of float numbers\n  Matrix(a, b, c, d, e, f) - creates a Matrix and assigns coordinates from float numbers\n\nATTRIBUTES:\n  a, b, c, d, e, f (float) - Matrix parameters\n\nOPERATIONS:\n  add - Matrix must be second operand, all parameters are added\n  subtract - Matrix must be second operand, all parameters are subtracted\n  multiply (with Matrix) - matrixes are multiplied\n  multiply (with float number) - all parameters are scaled by the operand\n\nMETHODS\n  Assign - assigns new values to a Matrix, uses the same syntax as in constructors\n  Add(Matrix m) - adds values of the Matrix m to current matrix\n  Sub(Matrix m) - subtracts values of the Matrix m from current matrix\n  Mul(float s) - mutiplies Matrix's parameters to s value\n  Transform(Matrix m) - applies Matrix m transformation to the current Matrix\n\nNative bases: object\n\nCaptured native MRO: Matrix, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Matrix.__init__')

    def Add(self, m: Any) -> Any:
        'Add(Matrix m) - adds values of the Matrix m to current matrix'
        _unavailable('FL.Matrix.Add')

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        'Assign - assigns new values to a Matrix, uses the same syntax as in constructors'
        _unavailable('FL.Matrix.Assign')

    def Mul(self, s: float) -> Any:
        "Mul(float s) - mutiplies Matrix's parameters to s value"
        _unavailable('FL.Matrix.Mul')

    def Sub(self, m: Any) -> Any:
        'Sub(Matrix m) - subtracts values of the Matrix m from current matrix'
        _unavailable('FL.Matrix.Sub')

    def Transform(self, m: Any) -> Any:
        'Transform(Matrix m) - applies Matrix m transformation to the current Matrix'
        _unavailable('FL.Matrix.Transform')

    a: Any
    b: Any
    c: Any
    d: Any
    e: Any
    f: Any

class Node:
    "===============================================\n  Node - class to represent node\n===============================================\nThis class is Multiple Master - compatible\n\nCONSTRUCTOR:\n  Node() - generic constructor, creates an empty node\n  Node(Node) - copy constructor\n  Node(intteger type, Point p) - creates a Node and assigns type and coordinates of the final point\n\nATTRIBUTES:\n  parent (read-only) - Node's parent object\n         type (integer) - type of the node, values are: nMOVE, nLINE, nCURVE or nOFF\n  count (integer, read-only) - number of points in the node. 3 for curves and 1 for all other types of nodes\n  alignment (integer) - type of primitive connection, possible values are: nSHARP, nSMOOTH, nFIXED\n  selected (integer) - True if node is selected\n  point (Point) - position of the final point of the first master\n  points [(Points)] - positions of all points of the first master\n  x (integer) - horizontal position of the final point of the node\n  y (integer) - vertical position of the final point of the node\n\nOPERATIONS:\n  len() - returns number of points in the node, same as count attribute\n  [] - can be used to access individial points of the first master\n  multiply - second operand must be Matrix, applies matrix transformation to a node\n\nMETHODS\n  Assign - assigns new values to a Node, refer to constructor for a description of possible options\n  SetAllLayers(pointindex, Point p) - assigns position of the point p to all masters of the point number 'pointindex'\n  Layer(masterindex) - returns list of points for the master 'masterindex'\n  Section(pointindex) - returns list of points for all layers and point number 'pointindex'\n  Shift(Point p, masterindex) - shifts position of all points for the master 'masterindex'\n  ExpandLayer(masterindex) - copies positions of all points in the master 'masterindex' to other masters\n  Transform(Matrix m) - applies Matrix transformation to the Node (see Matrix().__doc__)\n\nNative bases: object\n\nCaptured native MRO: Node, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Node.__init__')

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Node.Assign; argument details are not documented.'
        _unavailable('FL.Node.Assign')

    def ExpandLayer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Node.ExpandLayer; argument details are not documented.'
        _unavailable('FL.Node.ExpandLayer')

    def Layer(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Node.Layer; argument details are not documented.'
        _unavailable('FL.Node.Layer')

    def Section(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Node.Section; argument details are not documented.'
        _unavailable('FL.Node.Section')

    def SetAllLayers(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Node.SetAllLayers; argument details are not documented.'
        _unavailable('FL.Node.SetAllLayers')

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Node.Shift; argument details are not documented.'
        _unavailable('FL.Node.Shift')

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.Node.Transform; argument details are not documented.'
        _unavailable('FL.Node.Transform')

    alignment: Any
    count: Any
    open: Any
    parent: Any
    point: Any
    points: Any
    selected: Any
    type: Any
    x: Any
    y: Any

class Point:
    "===============================================\n  Point - base class to represent point\n===============================================\nInteger or float values are accepted as coordinates\n\nCONSTRUCTOR:\n  Point() - generic constructor, creates a Point with zero coordinates\n  Point(Point) - copy constructor\n  Point(x, y) - creates a Point and assigns coordinates. x and y may be integer or float\n\nATTRIBUTES:\n  parent (read-only) - Point's parent object\n  x (integer or float) - horizontal position of the point\n  y (integer or float) - vertical position of the point\n\nOPERATIONS:\n  == - compares two points, both coordinates must be equal\n  add - Point must be second operand, both coordinates are added\n  subtract - Point must be second operand, both coordinates are added\n  multiply - second operand may be Point, float or Matrix. If second operand is Point, then result of scalar product is returned\n\nMETHODS\n  Assign(Point p) | (x, y) - assigns new values to a Point\n  Shift(Point p) | (x, y) - shifts Point on a position defined by p or x and y values\n  Add(Point p) - same as Shift(Point p)\n  Sub(Point p) - subtracts p coordinates from the current Point\n  Mul(float s) - mutiplies Point's position to s value\n  Transform(Matrix m) - applies Matrix transformation to the Point (see Matrix().__doc__)\n\nNative bases: object\n\nCaptured native MRO: Point, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Point.__init__')

    def Add(self, p: Any) -> Any:
        'Add(Point p) - same as Shift(Point p)'
        _unavailable('FL.Point.Add')

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        'Assign(Point p) | (x, y) - assigns new values to a Point'
        _unavailable('FL.Point.Assign')

    def Mul(self, s: float) -> Any:
        "Mul(float s) - mutiplies Point's position to s value"
        _unavailable('FL.Point.Mul')

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        'Shift(Point p) | (x, y) - shifts Point on a position defined by p or x and y values'
        _unavailable('FL.Point.Shift')

    def Sub(self, p: Any) -> Any:
        'Sub(Point p) - subtracts p coordinates from the current Point'
        _unavailable('FL.Point.Sub')

    def Transform(self, m: Any) -> Any:
        'Transform(Matrix m) - applies Matrix transformation to the Point (see Matrix().__doc__)'
        _unavailable('FL.Point.Transform')

    x: Any
    y: Any

class Rect:
    "===============================================\n  Rect - base class to represent rectangle\n===============================================\nInteger or float values are accepted as coordinates\n\nCONSTRUCTOR:\n  Rect() - generic constructor, creates a Rect with zero coordinates\n  Rect(Rect r) - copy constructor\n  Rect(Point p) - creates rectangle with one corner at (0, 0) and another - at coordinates defined by p\n  Rect(Point p0, Point p1) - creates rectangle defined by the corner points\n  Rect(x0, y0, x1, y1) - creates a rectangle defined by the coordinates of the corner points\n\nATTRIBUTES:\n  ll (Point) - position of the left/bottom corner\n  ur (Point) - position of the right/top corner\n  x (integer or float) - horizontal position of the left corner\n  y (integer or float) - vertical position of the bottom corner\n  width (integer or float) - width of the rectangle\n  height (integer or float) - height of the rectangle\n\nOPERATIONS:\n  add - Point or Rect must be second operand, rectangle is expanded to include this point or rectange\n  multiply - second operand must be Matrix. Matrix transformation is applied to the rectangle\n\nMETHODS\n  Assign(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - assigns new values to a Rect, the same as constructor\n  Shift(Point p) | (x, y) - shifts Rect on a position defined by p or x and y values\n  Transform(Matrix m) - applies Matrix transformation to the Rect (see Matrix().__doc__)\n  Resize(width, height) - resizes rectangle to new width and height\n  Include(Rect r) | (Point p) | (x, y)  - expands rectangle to include new rectangle or point\n  Check(Rect r) - returns True if r overlaps current rectangle\n  Check(Point p) - returns True if p is insude current rectangle\n  Validate() - corrents rectangle's orientation\n\nNative bases: object\n\nCaptured native MRO: Rect, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Rect.__init__')

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        'Assign(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - assigns new values to a Rect, the same as constructor'
        _unavailable('FL.Rect.Assign')

    def Check(self, *args: Any, **kwargs: Any) -> Any:
        'Check(Rect r) - returns True if r overlaps current rectangle\nCheck(Point p) - returns True if p is insude current rectangle'
        _unavailable('FL.Rect.Check')

    def Include(self, *args: Any, **kwargs: Any) -> Any:
        'Include(Rect r) | (Point p) | (x, y)  - expands rectangle to include new rectangle or point'
        _unavailable('FL.Rect.Include')

    def Resize(self, width: Any, height: Any) -> Any:
        'Resize(width, height) - resizes rectangle to new width and height'
        _unavailable('FL.Rect.Resize')

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        'Shift(Point p) | (x, y) - shifts Rect on a position defined by p or x and y values'
        _unavailable('FL.Rect.Shift')

    def Transform(self, m: Any) -> Any:
        'Transform(Matrix m) - applies Matrix transformation to the Rect (see Matrix().__doc__)'
        _unavailable('FL.Rect.Transform')

    def Validate(self) -> Any:
        "Validate() - corrents rectangle's orientation"
        _unavailable('FL.Rect.Validate')

    height: Any
    ll: Any
    ur: Any
    width: Any
    x: Any
    y: Any

class TTGasp:
    'TTGasp\n\nNative bases: object\n\nCaptured native MRO: TTGasp, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.TTGasp.__init__')


class TTPoint:
    "===============================================\n  TTPoint - class to represent TrueType points\n===============================================\nAll coordinates in TTPoint class are set in 10.6 fixed-point format\n\nCONSTRUCTOR:\n  TTPoint() - generic constructor, creates a TTPoint with zero coordinates\n\nATTRIBUTES:\n  x (integer) - x coordinate\n  y (integer) - y coordinate\n  flag (integer) - point's flag (on-curve or off-curve)\n\nOPERATIONS:\n\nMETHODS\n\nNative bases: object\n\nCaptured native MRO: TTPoint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.TTPoint.__init__')

    flag: Any
    x: Any
    y: Any

class TTVdmx:
    'TTVdmx\n\nNative bases: object\n\nCaptured native MRO: TTVdmx, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.TTVdmx.__init__')


class TrueTypeTable:
    "===============================================\n  TrueTypeTable - class to represent custom OpenType table\n===============================================\n\nCONSTRUCTOR:\n  TrueTypeTable() - generic constructor, creates an empty TrueTypeTable record\n  TrueTypeTable(TrueTypeTable) - copy constructor\n  TrueTypeTable(string tag) - creates table, assigns 'tag' and empty value\n  TrueTypeTable(string tag, string value) - creates TrueType table and assigns values to both attributes\n  TrueTypeTable(string tag, string value, integer valuelen) - creates TrueType table and assigns values to both attributes. 'value' may include zeroes\n\nATTRIBUTES:\n  parent (read-only) - parent object, Font\n  tag (string) - TrueType table's tag\n  value (string) - TrueType table's value\n\nOPERATIONS:\n\nMETHODS\n\nNative bases: object\n\nCaptured native MRO: TrueTypeTable, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.TrueTypeTable.__init__')


class Uni:
    'Uni(Int value)\n\nNative bases: object\n\nCaptured native MRO: Uni, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.Uni.__init__')

    value: Any

class VSSGaspArray:
    'VSSGaspArray\n\nNative bases: object\n\nCaptured native MRO: VSSGaspArray, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.VSSGaspArray.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSGaspArray.append; argument details are not documented.'
        _unavailable('FL.VSSGaspArray.append')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSGaspArray.clean; argument details are not documented.'
        _unavailable('FL.VSSGaspArray.clean')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSGaspArray.insert; argument details are not documented.'
        _unavailable('FL.VSSGaspArray.insert')


class VSSTTPointArray:
    'VSSTTPointArray\n\nNative bases: object\n\nCaptured native MRO: VSSTTPointArray, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.VSSTTPointArray.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSTTPointArray.append; argument details are not documented.'
        _unavailable('FL.VSSTTPointArray.append')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSTTPointArray.clean; argument details are not documented.'
        _unavailable('FL.VSSTTPointArray.clean')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSTTPointArray.insert; argument details are not documented.'
        _unavailable('FL.VSSTTPointArray.insert')


class VSSVdmxArray:
    'VSSVdmxArray\n\nNative bases: object\n\nCaptured native MRO: VSSVdmxArray, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.VSSVdmxArray.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSVdmxArray.append; argument details are not documented.'
        _unavailable('FL.VSSVdmxArray.append')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSVdmxArray.clean; argument details are not documented.'
        _unavailable('FL.VSSVdmxArray.clean')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native FL.VSSVdmxArray.insert; argument details are not documented.'
        _unavailable('FL.VSSVdmxArray.insert')


class WeightVector:
    'WeightVector\n\nNative bases: object\n\nCaptured native MRO: WeightVector, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('FL.WeightVector.__init__')


BUTTONCONTROL: int
CHECKBOXCONTROL: int
CHOICECONTROL: int
Cancel: int
EDITCONTROL: int
LISTCONTROL: int
NULLCONTROL: int
OK: int
PREVIEWCONTROL: int
STATICCONTROL: int
STYLE_BEVELBUTTON: int
STYLE_BUTTON: int
STYLE_CHECKBOX: int
STYLE_CHOICE: int
STYLE_CUSTOM: int
STYLE_EDIT: int
STYLE_FRAME: int
STYLE_LABEL: int
STYLE_LIST: int
WS_BORDER: int
WS_CAPTION: int
WS_CHILD: int
WS_CLIPCHILDREN: int
WS_CLIPSIBLINGS: int
WS_DISABLED: int
WS_DLGFRAME: int
WS_GROUP: int
WS_HSCROLL: int
WS_MAXIMIZE: int
WS_MAXIMIZEBOX: int
WS_MINIMIZE: int
WS_MINIMIZEBOX: int
WS_OVERLAPPED: int
WS_OVERLAPPEDWINDOW: int
WS_POPUP: int
WS_POPUPWINDOW: int
WS_SYSMENU: int
WS_TABSTOP_: int
WS_THICKFRAME: int
WS_VISIBLE: int
WS_VSCROLL: int
aALIGN: int
aAUTO: int
aIDENT: int
aIDENT2: int
aIDENT3: int
aNEXT: int
aSAME: int
cBRUSH_NULL: int
cBRUSH_SOLID: int
cPEN_DASH: int
cPEN_DOT: int
cPEN_NULL: int
cPEN_SOLID: int
cRECT_3DDOWN: int
cRECT_3DDOWN_FLAT: int
cRECT_3DDOWN_SOLID: int
cRECT_3DUP: int
cRECT_3DUP_FLAT: int
cRECT_3DUP_SOLID: int
cRECT_BLACK_FRAME: int
cRECT_BLACK_SOLID: int
cRECT_BLACK_THICK_FRAME: int
cRECT_ELLIPSE: int
cRECT_FOCUS: int
cRECT_GRAY_FRAME: int
cRECT_GRAY_SOLID: int
cRECT_INVERT: int
cRECT_LTGRAY_SOLID: int
cRECT_RECTANGLE: int
cRECT_SIZE: int
cRECT_WHITE_SOLID: int
cRECT_YELLOW_FRAME: int
cRECT_YELLOW_SOLID: int
cRGB_BLACK: int
cRGB_BLUE: int
cRGB_GRAY: int
cRGB_GREEN: int
cRGB_LTGRAY: int
cRGB_RED: int
cRGB_WHITE: int
cRGB_YELLOW: int
cTO_BOTTOM: int
cTO_CENTER: int
cTO_LEFT: int
cTO_RIGHT: int
cTO_TOP: int
cTO_VCENTER: int
fl: Any
ftFONTLAB: int
ftMACTRUETYPE: int
ftMACTRUETYPE_DFONT: int
ftMACTYPE1: int
ftOPENTYPE: int
ftTRUETYPE: int
ftTYPE1: int
ftTYPE1ASCII: int
ftTYPE1ASCII_MM: int
ftTYPE1_MM: int
nCURVE: int
nFIXED: int
nLINE: int
nMOVE: int
nOFF: int
nSHARP: int
nSMOOTH: int

__echopy_source_aliases__ = {'WS_TABSTOP ': 'WS_TABSTOP_'}
__all__ = ['Anchor', 'BUTTONCONTROL', 'CHECKBOXCONTROL', 'CHOICECONTROL', 'Cancel', 'Canvas', 'CmapTable', 'Component', 'Dialog', 'EDITCONTROL', 'Encoding', 'EncodingRecord', 'Feature', 'Features', 'Font', 'Glyph', 'Guide', 'Hint', 'Image', 'KerningArray', 'KerningPair', 'LISTCONTROL', 'Link', 'Matrix', 'NULLCONTROL', 'Node', 'OK', 'PREVIEWCONTROL', 'Point', 'Rect', 'STATICCONTROL', 'STYLE_BEVELBUTTON', 'STYLE_BUTTON', 'STYLE_CHECKBOX', 'STYLE_CHOICE', 'STYLE_CUSTOM', 'STYLE_EDIT', 'STYLE_FRAME', 'STYLE_LABEL', 'STYLE_LIST', 'TTGasp', 'TTPoint', 'TTVdmx', 'TrueTypeTable', 'Uni', 'VSSGaspArray', 'VSSTTPointArray', 'VSSVdmxArray', 'WS_BORDER', 'WS_CAPTION', 'WS_CHILD', 'WS_CLIPCHILDREN', 'WS_CLIPSIBLINGS', 'WS_DISABLED', 'WS_DLGFRAME', 'WS_GROUP', 'WS_HSCROLL', 'WS_MAXIMIZE', 'WS_MAXIMIZEBOX', 'WS_MINIMIZE', 'WS_MINIMIZEBOX', 'WS_OVERLAPPED', 'WS_OVERLAPPEDWINDOW', 'WS_POPUP', 'WS_POPUPWINDOW', 'WS_SYSMENU', 'WS_TABSTOP ', 'WS_THICKFRAME', 'WS_VISIBLE', 'WS_VSCROLL', 'WeightVector', 'aALIGN', 'aAUTO', 'aIDENT', 'aIDENT2', 'aIDENT3', 'aNEXT', 'aSAME', 'cBRUSH_NULL', 'cBRUSH_SOLID', 'cPEN_DASH', 'cPEN_DOT', 'cPEN_NULL', 'cPEN_SOLID', 'cRECT_3DDOWN', 'cRECT_3DDOWN_FLAT', 'cRECT_3DDOWN_SOLID', 'cRECT_3DUP', 'cRECT_3DUP_FLAT', 'cRECT_3DUP_SOLID', 'cRECT_BLACK_FRAME', 'cRECT_BLACK_SOLID', 'cRECT_BLACK_THICK_FRAME', 'cRECT_ELLIPSE', 'cRECT_FOCUS', 'cRECT_GRAY_FRAME', 'cRECT_GRAY_SOLID', 'cRECT_INVERT', 'cRECT_LTGRAY_SOLID', 'cRECT_RECTANGLE', 'cRECT_SIZE', 'cRECT_WHITE_SOLID', 'cRECT_YELLOW_FRAME', 'cRECT_YELLOW_SOLID', 'cRGB_BLACK', 'cRGB_BLUE', 'cRGB_GRAY', 'cRGB_GREEN', 'cRGB_LTGRAY', 'cRGB_RED', 'cRGB_WHITE', 'cRGB_YELLOW', 'cTO_BOTTOM', 'cTO_CENTER', 'cTO_LEFT', 'cTO_RIGHT', 'cTO_TOP', 'cTO_VCENTER', 'fl', 'ftFONTLAB', 'ftMACTRUETYPE', 'ftMACTRUETYPE_DFONT', 'ftMACTYPE1', 'ftOPENTYPE', 'ftTRUETYPE', 'ftTYPE1', 'ftTYPE1ASCII', 'ftTYPE1ASCII_MM', 'ftTYPE1_MM', 'nCURVE', 'nFIXED', 'nLINE', 'nMOVE', 'nOFF', 'nSHARP', 'nSMOOTH']
_bind(globals(), 'FL', __echopy_source_aliases__)
