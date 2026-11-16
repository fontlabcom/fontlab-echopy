# this_file: src/fontlab_echopy/FL.pyi
# Generated from native metadata and independent enrichment inputs.
"""old FL-Python interface for FontGate"""
from __future__ import annotations
from typing import Any
import builtins as _echopy_builtins

class Anchor:
    """===============================================
  Anchor - class to represent Anchor point
===============================================
Integer values are accepted as coordinates

CONSTRUCTOR:
  Anchor() - generic constructor, creates an Anchor with zero coordinates and empty name
  Anchor(Anchor) - copy constructor
  Anchor(string name, integer x, integer y) - creates an Anchor and assigns name and coordinates.

ATTRIBUTES:
  parent (read-only) - anchor's parent object, Glyph
  name (string) - anchor's name as a string
  x (integer) - horizontal position of the anchor
  y (integer) - vertical position of the anchor
  p (Point) - position of the anchor as a Point object

OPERATIONS:

METHODS
  Transform(Matrix m) - applies Matrix transformation to the Anchor(see Matrix().__doc__)
  Layer(int layer_index) - returns position for the "layer_index" master
  SetLayer(int layer_index, Point position) - sets "position" position for the "layer_index" master

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Layer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Anchor.Layer; argument details are not documented."""
        ...

    def SetLayer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Anchor.SetLayer; argument details are not documented."""
        ...

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Anchor.Transform; argument details are not documented."""
        ...

class Canvas:
    """===============================================
  Canvas - class to represent screen paint area and operations
===============================================
This class can perform automatic coordinates transformations, so you can draw in Glyph coordinate space or, if you prefer, in screen coordinates directly
Use constants defined for FontLab module to assign attributes to Canvas object

CONSTRUCTOR:
  ++ Never create Canvas object explicitly - they must be obtained from the FontLab's window classes
  Canvas() - generic constructor, creates an empty Canvas
  Canvas(Canvas) - copy constructor

ATTRIBUTES:
  delta (Point) - horizontal shift during coordinates transformation
  scale (Point(float)) - scaling during coordinates transformation
  width (integer, read-only) - width of the canvas in pixels
  height (integer, read-only) - height of the canvas in pixels
  draw_style (integer, write-only) - sets current drawing mode (copy, XOR, invert etc.)
  pen_color (integer, write-only) - sets current pen color
  pen_style (integer, write-only) - sets current pen style (solid, dashed etc.)
  brush_color (integer, write-only) - sets current brush color
  brush_style (integer, write-only) -  sets current brush style (solid, patterned etc.)
  text_color (integer, write-only) - sets color for a text
  bk_color (integer, write-only) - sets color for a text background
  bk_mode (integer, write-only) - sets background mode for a text output (transparent or opaque)

OPERATIONS:

METHODS
  MoveTo(Point p) | (x, y) - moves current position to p or (x, y) coordinates
  LineTo(Point p) | (x, y) - draws a straight line to the position p or (x, y)
  CurveTo(Point p0, Point p1, Point p2) - draws a 3th-order Bezier curve from the current point to points p0, p1, p2
  SplineTo(Point p0, Point p1) - draws a 2th-order Bezier curve from the current point to points p0, p1
  Ellipse(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - draws a filled ellipse defined by the Rect r, points p0 and p1 or set of coordinates
  Rectangle(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - draws a filled rectangle defined by the Rect r, points p0 and p1 or set of coordinates
  Convert(Point p) - converts coordinates from the source coordinate space to screen coordinates
  UnConvert(Point p) - converts screen coordinates to the currently defined coordinate space
  FitGlyph(Rect r, Glyph g) | (Rect r, Glyph g, WeightVector w) - recalculates parameters of coordinate conversion function to fit glyph g into rectangle r using currently selected options.
  FillGlyph(Glyph g) | (Glyph g, WeightVector w) - fills the glyph g using current coordinate transformation.
  OutlineGlyph(Glyph g) | (Glyph g, WeightVector w) - draws the glyph g outline using current coordinate transformation.
  TextOut(Point p, string s) | (x, y, string s) - draws the string s in the position p or (x, y)
  PutImage(Image i, Point p) | (Image i, Pioint p, int mode) - puts Image i at the selected point

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Convert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.Convert; argument details are not documented."""
        ...

    def CurveTo(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.CurveTo; argument details are not documented."""
        ...

    def Ellipse(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.Ellipse; argument details are not documented."""
        ...

    def FillGlyph(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.FillGlyph; argument details are not documented."""
        ...

    def FitGlyph(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.FitGlyph; argument details are not documented."""
        ...

    def LineTo(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.LineTo; argument details are not documented."""
        ...

    def MoveTo(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.MoveTo; argument details are not documented."""
        ...

    def OutlineGlyph(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.OutlineGlyph; argument details are not documented."""
        ...

    def PutImage(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.PutImage; argument details are not documented."""
        ...

    def Rectangle(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.Rectangle; argument details are not documented."""
        ...

    def SplineTo(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.SplineTo; argument details are not documented."""
        ...

    def TextOut(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.TextOut; argument details are not documented."""
        ...

    def UnConvert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Canvas.UnConvert; argument details are not documented."""
        ...

class CmapTable:
    """===============================================
  CmapTable - class to represent custom 'cmap' table record
===============================================
Refer to OpenType specification for information about constants used for platform, encoding, language and format

CONSTRUCTOR:
  CmapTable() - generic constructor, creates an empty name record
  CmapTable(CmapTable) - copy constructor
  CmapTable((pid, eid, lid, format, type, pagename)) - defines name receiving all values from a tuple
  CmapTable(pid, eid, lid, format, type, pagename) - defines name receiving all values from parameters of constructor

ATTRIBUTES:
  parent (read-only) - parent object, Font
  pid (integer) - platform identifier
  eid (integer) - encoding identifier
  lid (integer) - language identifier
  format (integer) - cmap subtable format (see OpenType specification)
  type (integer) - subtable type (see CMAPTYPE_XXX constants)
  pagename (string) - name of the attached codepage

OPERATIONS:

METHODS

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

class Component:
    """===============================================
  Component - class to represent glyph component
===============================================
Components are defined by the glyph index which they reference, shift of components origin point and scale factor of a component
scale is measured in relation to 1.0, so 100% scale is 1.0 and 60% - 0.6
This class is Multiple Master - compatible

CONSTRUCTOR:
  Component() - generic constructor, creates an empty Component
  Component(Component) - copy constructor
  Component(index) - creates component referencing glyph index with zero shift and 100% scale
  Component(index, Point(integer) delta) - creates component referencing glyph index with delta shift and 100% scale
  Component(index, Point(integer) delta, Point(float) scale) - creates component referencing glyph index with delta shift and scale factor defined by scale

ATTRIBUTES:
  parent (read-only) - parent object, Glyph
  index (integer) - referencing glyph index
  delta (Point(integer)) - shift value
  scale (Point(float)) - scale factor
  deltas [(Point(integer))]- list of shift values for each master
  scales [(Point(float))] - list of scale values for each master

OPERATIONS:

METHODS
  Get() | (Font f) - creates a glyph from component applying delta and scale transformations. Font parameter is not needed when component has a parent
  Paste() - appends component to a parent glyph as a set of outlines. Component must have a parent

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Get(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Component.Get; argument details are not documented."""
        ...

    def Paste(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Component.Paste; argument details are not documented."""
        ...

    def transform(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Component.transform; argument details are not documented."""
        ...

class Dialog:
    """===============================================
  Dialog - class to represent Dialog
===============================================
Note that objects of this class cannot be created explicitly, they are only generated as a result of Glyph().Audit() operation

CONSTRUCTOR:
  Dialog(DialogClass) - generic constructor

ATTRIBUTES:
  title - dialog title
  ok - text on the OK button
  cancel - text on the Cancel button
  position - position of the dialog's origin
  size - dialog size
  rectangle (combination of size and position)

OPERATIONS:

METHODS
  Center()                    - center dialog on screen
  AddControl(integer ControlType, Rect dimension, string identifier, integer ControlStyle)
                              - adds a control to the dialog, see FLdict for
                                Type- and Style-constants
  GetValue(string identifier) - get value from the specified control
  PutValue(string identifier) - put value to the specified control
  Enable(string identifier, integer value)
                              - enable (value=1) or disable (value=0) the specified control
  Show(string identifier, integer value)
                              - show (value=1) or hide (value=0) the specified control
  SetLabel(string identifier, string value)
                              - set the label of the specified control
  GetRect(string identifier)  - get dimension of the specified control as a Rect object
  Repaint(string identifier)  - redraw the specified (custom)control
  Run()                       - run the dialog
  End()|End(integer returnvalue) - end the dialog

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def AddControl(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.AddControl; argument details are not documented."""
        ...

    def Center(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.Center; argument details are not documented."""
        ...

    def Enable(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.Enable; argument details are not documented."""
        ...

    def End(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.End; argument details are not documented."""
        ...

    def GetRect(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.GetRect; argument details are not documented."""
        ...

    def GetValue(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.GetValue; argument details are not documented."""
        ...

    def MoveTo(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.MoveTo; argument details are not documented."""
        ...

    def PutValue(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.PutValue; argument details are not documented."""
        ...

    def Repaint(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.Repaint; argument details are not documented."""
        ...

    def Run(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.Run; argument details are not documented."""
        ...

    def SetLabel(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.SetLabel; argument details are not documented."""
        ...

    def Show(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Dialog.Show; argument details are not documented."""
        ...
    cancel: Any
    ok: Any
    position: Any
    rectangle: Any
    size: Any
    title: Any

class Encoding:
    """Encoding

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def FillUnencoded(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Encoding.FillUnencoded; argument details are not documented."""
        ...

    def FillUnicodes(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Encoding.FillUnicodes; argument details are not documented."""
        ...

    def FindName(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Encoding.FindName; argument details are not documented."""
        ...

    def Load(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Encoding.Load; argument details are not documented."""
        ...

    def Save(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Encoding.Save; argument details are not documented."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Encoding.append; argument details are not documented."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Encoding.insert; argument details are not documented."""
        ...

class EncodingRecord:
    """EncodingRecord

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

class Feature:
    """===============================================
  Feature - class to represent OpenType feature-definition record
===============================================

CONSTRUCTOR:
  Feature() - generic constructor, creates an empty Feature record
  Feature(Feature) - copy constructor
  Feature(string tag) - creates feature, assigns 'tag' and empty value
  Feature(string tag, string value) - creates feature and assigns values to both attributes

ATTRIBUTES:
  parent (read-only) - parent object, Font
  tag (string) - feature's tag
  value (string) - feature's text

OPERATIONS:

METHODS

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

class Features:
    """OT Features array

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Features.append; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Features.clean; argument details are not documented."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Features.insert; argument details are not documented."""
        ...

class Font:
    """===============================================
  Font - base class to represent font
===============================================

CONSTRUCTOR:
  Font() - generic constructor, creates an empty Font  Font(Font) - copy constructor
  Font(string filename) - creates a Font and assigns name of the file from which it was opened

ATTRIBUTES:

  NAMES, COPYRIGHT AND IDENTIFICATION
  family_name(string) - font Family Name
  style_name
  full_name(string) - font Full Name
  font_name(string) - font Font Name
  font_style(integer) - Font Style
  menu_name(string) - font menu name
  weight
  weight_code
  width
  designer
  designer_url
  fontnames[NameRecord] - list of font name records
  copyright(string) - Copyright name field
  notice(string) - Notice field
  note(string) - Font note
  unique_id
  tt_u_id
  tt_version
  trademark
  x_u_id_num
  x_u_id
  vendor
  vendor_url
  version
  year
  version_major
  version_minor
  vp_id
  ms_charset
  ms_id
  panose[integer] - list of Panose values
  collection[collection] - list of glyph indexes in FontLab collection
  pcl_chars_set
  pcl_id

  DIMENSIONS
  upm
  ascender[integer] - list of ascenders, one for each master
  descender[integer] - list of descenders, one for each master
  cap_height[integer] - list of CapHeight records, one for each master
  x_height[integer] - list of xHeight values, one for each master
  default_width
  slant_angle
  italic_angle(float) - Italic Angle
  is_fixed_pitch
  underline_position
  underline_thickness

  ALIGNMENT
  blue_fuzz
  blue_scale
  blue_shift
  blue_values_num(integer) - number of defined blue values
  blue_values[integer[integer]] - two-dimentional array of BlueValues - master index is top-level index
  family_blues_num(integer) - number of FamilyBlues records
  family_blues[integer[integer]] - two-dimentional array of FamilyBlues - master index is top-level index
  family_other_blues_num(integer) - number of FamilyOtherBlues records
  family_other_blues[integer[integer]] - two-dimentional array of FamilyOtherBlues - master index is top-level index
  force_bold[integer] - list of Force Bold values, one for each master
  other_blues_num
  other_blues[integer[integer]] - two-dimentional array of OtherBlues - master index is top-level index
  stem_snap_h_num
  stem_snap_h
  stem_snap_v_num
  stem_snap_v

  OTHER ATTRIBUTES
  classes[string] - list of glyph classes
  ot_classes - OpenType classes data
  classes_text - glyph classes compiled in ot_classes format
  features[Feature] - list of OpenType features
  customdata(string) - font custom data field
  truetypetables[TrueTypeTable] - list of custom TrueType tables
  ttinfo(TTInfo) - loaded TrueType information (mostly hinting-related tables)
  encoding
  glyphs[Glyph] - array of glyphs
  source
  weight_vector
  measurement - position of the measurement line for the font

OPERATIONS:
  len - returns number of glyphs
  [] - accesses glyphs array

METHODS
  New() - clears the font
  Open(string filename) - opens font from VFB format
  Save(string filename) - saves font in VFB format
  Reencode()  FindGlyph(string name) | (Uni unicode) | (integer Unicode) - finds glyph and return its index or -1
  DefineAxis(string Name, string Type, string ShortName) - defines the new Multiple Master axis
  DeleteAxis(axisindex, float position) - removes the axis
  GenerateUnicode() - generates Unicode indexes for all glyphs
  GenerateNames() - generates names for all glyphs
  GenerateGlyph(string glyphname) - generates new glyph using 'glyphname' as a source of information about glyph's composition
  MakeKernFeature([WeightVector vector]) - generates 'kern' feature using font kerning and classes
  MergeFonts(Font source[, flags]) - appends all glyphs from the source font. Check mfXXXX constants for options
  SetClassFlags(int class_index, bool left, bool right) - allows to set 'left' and 'right' properties of the kerning class   SetClassFlags(int class_index, bool lsb, bool rsb, bool width) - allows to set 'lsb', 'rsb' and 'width' properties of the metrics class   GetClassLeft(int class_index) - returns the 'left' property of the class  GetClassRight(int class_index) - returns the 'right' property of the class  GetClassMetricsFlags(int class_index) - returns the tuple containing LSB, RSB and Width flags of the metrics class

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def DefineAxis(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.DefineAxis; argument details are not documented."""
        ...

    def DeleteAxis(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.DeleteAxis; argument details are not documented."""
        ...

    def FindGlyph(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.FindGlyph; argument details are not documented."""
        ...

    def GenerateGlyph(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.GenerateGlyph; argument details are not documented."""
        ...

    def GenerateNames(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.GenerateNames; argument details are not documented."""
        ...

    def GenerateUnicode(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.GenerateUnicode; argument details are not documented."""
        ...

    def GetClassLeft(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.GetClassLeft; argument details are not documented."""
        ...

    def GetClassMetricsFlags(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.GetClassMetricsFlags; argument details are not documented."""
        ...

    def GetClassRight(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.GetClassRight; argument details are not documented."""
        ...

    def MakeKernFeature(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.MakeKernFeature; argument details are not documented."""
        ...

    def MergeFonts(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.MergeFonts; argument details are not documented."""
        ...

    def New(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.New; argument details are not documented."""
        ...

    def Open(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.Open; argument details are not documented."""
        ...

    def OpenAFM(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.OpenAFM; argument details are not documented."""
        ...

    def Save(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.Save; argument details are not documented."""
        ...

    def SaveAFM(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.SaveAFM; argument details are not documented."""
        ...

    def SetClassFlags(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.SetClassFlags; argument details are not documented."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Font.has_key; argument details are not documented."""
        ...

class Glyph:
    """===============================================
  Glyph - class to represent glyph
===============================================

CONSTRUCTOR:
  Glyph() - generic constructor, creates an empty glyph
  Glyph(Glyph) - copy constructor
  Glyph(masterscount) - creates a glyph with 'masterscount' number of masters
  Glyph(masterscount, [Node, ...]) - creates a glyph with 'masterscount' number of masters and assigns a list of nodes

ATTRIBUTES:
  parent (read-only) - Glyph's parent object
  nodes [Node] - list of Nodes
  customdata (string) - custom data defined for this glyph
  note (string) - note defined for this glyph
  mark (integer) - True if glyph is marked
  anchors [Anchor] - list of anchors
  hhints [Hint] - list of horizontal hints
  vhints [Hint] - list of vertical hints
  hlinks [Link] - list of horizontal links
  vlinks [Link] - list of vertical links
  components [Component] - list of componets
  replace_table [Replace] - hint replacing program, list of Replace objects
  kerning [KerningPair] - list of kerning pairs
  layers_number (integer) - number of masters
  flags (integer) - flags set for this glyph
  nodes_number (integer) - number of nodes, same as 'len(Glyph)'
  width (integer) - advance width for the first master
  height (integer) - advance height for the first master
  unicode (integer) - first Unicode index in integer form
  unicodes [integer] - list of Unicode indexes
  name (string) - glyph name
  mask (string) - mask

  STORED TRUETYPE DATA
  advance_width (integer)
  advance_height (integer)
  left_side_bearing (integer)
  top_side_bearing (integer)
  y_pels (integer)
  bounding_box (Rect)
  number_of_contours (integer)
  end_points [integer]
  points [TTPoint]
  instructions [Byte]
  hdmx[Byte]

OPERATIONS:
  len() - returns number of nodes in the glyph
  [] - can be used to access individial nodes
  slice - can be used to access portion of the glyph's nodes array
  + or concatination - can be used to append Glyph, Node or sequence of Nodes
  multiply - second operand must be Matrix, applies matrix transformation to a glyph

METHODS
  Assign (Glyph) - copies all information from the assigned glyph
  Transform(Matrix m) - applies Matrix transformation to the Glyph (see Matrix().__doc__)
  SetLayersNumber(mastersnumber) - changes the number of masters, is applicable only to glyphs that have no parent
  Clear() - removes all nodes
  Add - refer to '+' operator
  Insert (Node | Glyph | [Node]) | (Node | Glyph | [Node], nodeindex) - inserts Node, Glyph or sequence of Nodes at the begining of glyph's nodes or at specified node index
  Present (style) - returns True if a layer or a combination of layers are present in the glyph
  Delete (index) | (index0, index1) - removes node or range of nodes
  ExpandLayer (masterindex) - expands selected master to all other masters
  Shift (Point) | (Point, masterindex) - shifts positions of all nodes at first or specified master
  Scale (Point(float) scale) | (Point(float) scale, Point center) | (Point(float) scale, Point center, masterindex) - scales the glyph
  Layer (masterindex) - returns list of Points for all nodes for the selected master
  Section (masterindex, pointindex, nodetype) - returns list of Points that conform to selected options
  MoveNode(...) - moves the node copying Edit tool behavior (see User manual for details)
  DeleteNode(nodeindex) - removes the node
  InsertNode(nodeindex) | (nodeindex, float time) | (nodeindex, float time, masterindex) - insers new node on a contour
  SELECTION OPERATIONS
  Selection() - returns list of selected nodes
  SelectAll() - selects all nodes
  UnselectAll() - deselects all nodes
  InvertSelection() - selects unselected nodes and deselects selected nodes
  isAnySelected() - returns True if at least one node is selected
  SelectedCount() - returns number of selected nodes
  SelectRect(Rect r) | (Rect r, masterindex) - selects all nodes that are inside the rectangle
  UnselectRect(Rect r) | (Rect r, masterindex) - deselects all nodes that are inside the rectangle
  DeleteSelected() - deletes all selected nodes

  METRICS AND BBOX OPERATIONS
  GetBoundingRect() | (masterindex) - returns Rect - bounding box of the glyph
  GetMetrics() | (masterindex) - returns glyph advance width and advance height in a form of Point
  SetMetrics(Point p) | (Point p, masterindex) - assigns new values to the width and height of the glyph
  GetVSB() | (masterindex) - returns glyph bottom sidebearing position
  SetVSB(value) | (value, masterindex) - assigns new values to the bottom sidebearing of the glyph

  OVERLAP OPERATIONS
  RemoveOverlap() | (masterindex) - removes overlap
  Badd(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Add operation with the glyph or list of nodes
  Bsubtract(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Subtract operation with the glyph or list of nodes
  Bintersect(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Insersect operation with the glyph or list of nodes

  OPERATIONS ON CONTOURS
  GetContoursNumber() - returns number of contours in the glyph
  GetContourBegin(contourindex) - returns index of the first node for a contour
  GetContourLength(contourindex) - returns number of nodes in a contour
  SelectContour(contourindex) - selects all nodes in the contour
  DeleteContour(contourindex) - removes contour
  ReverseContour(contourindex) - reverses contour's direction
  ReorderContour(contourindex, newindex) - reorders contours in the glyph
  isContourClockwise(contourindex) - returns True if direction of contour is clockwise
  SetStartNode(nodeindex) - makes the node a starting node of the contour
  FindContour(nodeindex) - returns number of contour containing the 'nodeindex'

  HINTS OPERATIONS
  RemoveHints(mode) - removes hints and links
  Autohint() | (masterindex) - automatically generates Type 1 hints

  ANCHOR OPERATIONS
  FindAnchor(string name) - finds anchor by name

  TRANSFORMATION ACTIONS
  Decompose() - pastes all components to the glyph outline
  MakeExtremeNodes() | (masterindex) - automatically detects and adds extreme nodes
  Audit() | (masterindex) - performs test of the glyph and returns list of AuditRecord objects
  Iterate(Iterator) - iterates glyph trough iterator class which must unclude following methods: 
     Start(); ClosePath(); StartPath(Node); LineTo(Node); CurveTo(Node); SplineTo(Node); Finish()
  Rotate3D
  Extrude3D(outlinewidth, shift_x, shift_y)
  Shadow(outlinewidth, shift_x, shift_y)
  College(outlinewidth, distance)
  Gradient(outlinewidth, direction, stripes_number, start_y, finish_y)
  Distance(width_x, width_y, cornermode) | (width_x, width_y, cornermode, Glyph dest)
  Interpolate([(nodeindex, Point newposition])
  Warp([Point], float force)
  Rasterize() | Rasterize(Image, [, active layer[, height]]) | Rasterize(Image, [, WeightVector[, height]]) - rasterizes glyph to the Image or to glyph's background. Returns resulting image_rect. Height is relative to font's UPM
         Blend(Glyph source, integer layer1, integer layer2, Point amount) - returns blend of the glyph and source
         JoinAll() - tries to join all open contours
         SaveEPS(string filename) | (string filename, layer) - writes layer into the EPS file named filename
         LoadEPS(string filename) - reads EPS from filename and returns Glyph object. Use Assign method to replace current glyph with the loaded outline
  R([Point], float force)

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Add(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Add; argument details are not documented."""
        ...

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Assign; argument details are not documented."""
        ...

    def Audit(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Audit; argument details are not documented."""
        ...

    def Autohint(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Autohint; argument details are not documented."""
        ...

    def Badd(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Badd; argument details are not documented."""
        ...

    def Bintersect(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Bintersect; argument details are not documented."""
        ...

    def Blend(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Blend; argument details are not documented."""
        ...

    def Bsubtract(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Bsubtract; argument details are not documented."""
        ...

    def Clear(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Clear; argument details are not documented."""
        ...

    def College(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.College; argument details are not documented."""
        ...

    def Decompose(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Decompose; argument details are not documented."""
        ...

    def Delete(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Delete; argument details are not documented."""
        ...

    def DeleteContour(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.DeleteContour; argument details are not documented."""
        ...

    def DeleteNode(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.DeleteNode; argument details are not documented."""
        ...

    def DeleteSelected(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.DeleteSelected; argument details are not documented."""
        ...

    def Distance(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Distance; argument details are not documented."""
        ...

    def EditMask(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.EditMask; argument details are not documented."""
        ...

    def ExchangeMask(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.ExchangeMask; argument details are not documented."""
        ...

    def ExpandLayer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.ExpandLayer; argument details are not documented."""
        ...

    def Extrude3D(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Extrude3D; argument details are not documented."""
        ...

    def FindAnchor(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.FindAnchor; argument details are not documented."""
        ...

    def FindContour(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.FindContour; argument details are not documented."""
        ...

    def GetBoundingRect(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.GetBoundingRect; argument details are not documented."""
        ...

    def GetContourBegin(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.GetContourBegin; argument details are not documented."""
        ...

    def GetContourLength(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.GetContourLength; argument details are not documented."""
        ...

    def GetContoursNumber(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.GetContoursNumber; argument details are not documented."""
        ...

    def GetMetrics(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.GetMetrics; argument details are not documented."""
        ...

    def Gradient(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Gradient; argument details are not documented."""
        ...

    def Insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Insert; argument details are not documented."""
        ...

    def InsertNode(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.InsertNode; argument details are not documented."""
        ...

    def Interpolate(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Interpolate; argument details are not documented."""
        ...

    def InvertSelection(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.InvertSelection; argument details are not documented."""
        ...

    def Iterate(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Iterate; argument details are not documented."""
        ...

    def JoinAll(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.JoinAll; argument details are not documented."""
        ...

    def Layer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Layer; argument details are not documented."""
        ...

    def LoadEPS(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.LoadEPS; argument details are not documented."""
        ...

    def MakeExtremeNodes(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.MakeExtremeNodes; argument details are not documented."""
        ...

    def MoveNode(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.MoveNode; argument details are not documented."""
        ...

    def Present(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Present; argument details are not documented."""
        ...

    def Rasterize(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Rasterize; argument details are not documented."""
        ...

    def RemoveHints(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.RemoveHints; argument details are not documented."""
        ...

    def RemoveOverlap(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.RemoveOverlap; argument details are not documented."""
        ...

    def ReorderContour(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.ReorderContour; argument details are not documented."""
        ...

    def ReverseContour(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.ReverseContour; argument details are not documented."""
        ...

    def Rotate3D(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Rotate3D; argument details are not documented."""
        ...

    def SaveEPS(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SaveEPS; argument details are not documented."""
        ...

    def Scale(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Scale; argument details are not documented."""
        ...

    def Section(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Section; argument details are not documented."""
        ...

    def SelectAll(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SelectAll; argument details are not documented."""
        ...

    def SelectContour(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SelectContour; argument details are not documented."""
        ...

    def SelectRect(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SelectRect; argument details are not documented."""
        ...

    def SelectedCount(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SelectedCount; argument details are not documented."""
        ...

    def Selection(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Selection; argument details are not documented."""
        ...

    def SetLayersNumber(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SetLayersNumber; argument details are not documented."""
        ...

    def SetMetrics(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SetMetrics; argument details are not documented."""
        ...

    def SetStartNode(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.SetStartNode; argument details are not documented."""
        ...

    def Shadow(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Shadow; argument details are not documented."""
        ...

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Shift; argument details are not documented."""
        ...

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Transform; argument details are not documented."""
        ...

    def UnselectAll(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.UnselectAll; argument details are not documented."""
        ...

    def UnselectRect(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.UnselectRect; argument details are not documented."""
        ...

    def Warp(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.Warp; argument details are not documented."""
        ...

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.clear; argument details are not documented."""
        ...

    def isAnySelected(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.isAnySelected; argument details are not documented."""
        ...

    def isContourClockwise(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Glyph.isContourClockwise; argument details are not documented."""
        ...

class Guide:
    """===============================================
  Guide - class to represent guideline
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  Guide() - generic constructor, creates a Guide with zero coordinates
  Guide(Guide) - copy constructor
  Guide(position) - creates a Guide and assigns position
  Guide(position, angle) - creates a Guide and assigns position and width values

ATTRIBUTES:
  parent (read-only) - Guide's parent object, Glyph
  position (integer) - position of the guideline
  width (integer) - width of the guideline
  angle (float) - angle of the guide (degrees)
  positions [(integer)] - list of positions for each master
  widths [(integer)] - list of widths for each master

OPERATIONS:

METHODS
  Transform(Matrix m) - applies Matrix transformation to the Guide (see Matrix().__doc__)
  TransformLayer(Matrix m, layernum) - applies Matrix transformation to the selected layer of the Guide

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Guide.Transform; argument details are not documented."""
        ...

    def TransformLayer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Guide.TransformLayer; argument details are not documented."""
        ...

class Hint:
    """===============================================
  Hint - class to represent hint
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  Hint() - generic constructor, creates a Hint with zero coordinates
  Hint(Hint) - copy constructor
  Hint(position, width) - creates a Hint and assigns position and width values

ATTRIBUTES:
  parent (read-only) - Hint's parent object, Glyph
  position (integer) - position of the hint
  width (integer) - width of the hint
  positions [(integer)] - list of positions for each master
  widths [(integer)] - list of widths for each master

OPERATIONS:

METHODS
  ToLink() - transforms hint to Link (and returns it as a result) using parent as a source of node coordinates. Parent must exist
  Transform(Matrix m) - applies Matrix transformation to the Hint (see Matrix().__doc__)
  TransformLayer(Matrix m, layernum) - applies Matrix transformation to the selected layer of the Hint

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def ToLink(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Hint.ToLink; argument details are not documented."""
        ...

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Hint.Transform; argument details are not documented."""
        ...

    def TransformLayer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Hint.TransformLayer; argument details are not documented."""
        ...

class Image:
    """===============================================
  Image - class to represent bitmap image
===============================================

CONSTRUCTOR:
  Image() - generic constructor, creates a Image with zero coordinates
  Image(Image) - copy constructor
  Image(index1, index2) - creates a Image between nodes index1 and index2

ATTRIBUTES:
  width, height (integer) [read-only] - dimensions of the image
  empty (integer) [read-only] - empty status of the image
  size (integer) [read-only] - size of the image buffer
  data (string)  - image data as string with length
  traceenabled () [read-only] - there is a possibility to trace the image with the Trace command

OPERATIONS:
  Trace (Glyph) - Traces the image with the current option and adds it to the glyph

METHODS
  

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Clear(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.Clear; argument details are not documented."""
        ...

    def Create(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.Create; argument details are not documented."""
        ...

    def GetPixel(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.GetPixel; argument details are not documented."""
        ...

    def HLine(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.HLine; argument details are not documented."""
        ...

    def ImageBlt(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.ImageBlt; argument details are not documented."""
        ...

    def Invert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.Invert; argument details are not documented."""
        ...

    def SetPixel(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.SetPixel; argument details are not documented."""
        ...

    def Trace(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Image.Trace; argument details are not documented."""
        ...

class KerningArray:
    """KerningArray(void)

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.KerningArray.append; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.KerningArray.clean; argument details are not documented."""
        ...

class KerningPair:
    """===============================================
  KerningPair - class to represent kerning pair
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  KerningPair() - generic constructor, creates an empty KerningPair
  KerningPair(KerningPair) - copy constructor
  KerningPair(index) - creates a KerningPair to glyph referenced by index but zero value
  KerningPair(index, value) - creates a KerningPair to glyph referenced by index but and assigns value

ATTRIBUTES:
  parent (read-only) - KerningPair's parent object, Glyph
  key (integer) - index of right glyph of the pair
  value (integer) - value of the pair
  values [(integer)] - list of values for each master

OPERATIONS:

METHODS

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

class Link:
    """===============================================
  Link - class to represent link
===============================================

CONSTRUCTOR:
  Link() - generic constructor, creates a Link with zero coordinates
  Link(Link) - copy constructor
  Link(index1, index2) - creates a Link between nodes index1 and index2

ATTRIBUTES:
  parent (read-only) - Link's parent object, Glyph
  node1, node2 (integer) - indexes of the nodes that are linked

OPERATIONS:

METHODS
  ToHint() - transforms link to Hint (and returns it as a result) using parent as a source of node coordinates. Parent must exist

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def ToHint(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Link.ToHint; argument details are not documented."""
        ...

class Matrix:
    """===============================================
  Matrix - class to represent planar transformations
===============================================
Matrix is used to perform following transformations:
  x1 = x * a + y * b + e
  y1 = x * c + y * d + f

CONSTRUCTOR:
  Matrix() - generic constructor, creates a Matrix that makes no change to coordinates
  Matrix(Matrix) - copy constructor
  Matrix([a, b, c, d, e, f]) - creates a Matrix and assigns coordinates from the list of float numbers
  Matrix(a, b, c, d, e, f) - creates a Matrix and assigns coordinates from float numbers

ATTRIBUTES:
  a, b, c, d, e, f (float) - Matrix parameters

OPERATIONS:
  add - Matrix must be second operand, all parameters are added
  subtract - Matrix must be second operand, all parameters are subtracted
  multiply (with Matrix) - matrixes are multiplied
  multiply (with float number) - all parameters are scaled by the operand

METHODS
  Assign - assigns new values to a Matrix, uses the same syntax as in constructors
  Add(Matrix m) - adds values of the Matrix m to current matrix
  Sub(Matrix m) - subtracts values of the Matrix m from current matrix
  Mul(float s) - mutiplies Matrix's parameters to s value
  Transform(Matrix m) - applies Matrix m transformation to the current Matrix

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Add(self, m: Any) -> Any:
        """Add(Matrix m) - adds values of the Matrix m to current matrix"""
        ...

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        """Assign - assigns new values to a Matrix, uses the same syntax as in constructors"""
        ...

    def Mul(self, s: float) -> Any:
        """Mul(float s) - mutiplies Matrix's parameters to s value"""
        ...

    def Sub(self, m: Any) -> Any:
        """Sub(Matrix m) - subtracts values of the Matrix m from current matrix"""
        ...

    def Transform(self, m: Any) -> Any:
        """Transform(Matrix m) - applies Matrix m transformation to the current Matrix"""
        ...
    a: Any
    b: Any
    c: Any
    d: Any
    e: Any
    f: Any

class Node:
    """===============================================
  Node - class to represent node
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  Node() - generic constructor, creates an empty node
  Node(Node) - copy constructor
  Node(intteger type, Point p) - creates a Node and assigns type and coordinates of the final point

ATTRIBUTES:
  parent (read-only) - Node's parent object
         type (integer) - type of the node, values are: nMOVE, nLINE, nCURVE or nOFF
  count (integer, read-only) - number of points in the node. 3 for curves and 1 for all other types of nodes
  alignment (integer) - type of primitive connection, possible values are: nSHARP, nSMOOTH, nFIXED
  selected (integer) - True if node is selected
  point (Point) - position of the final point of the first master
  points [(Points)] - positions of all points of the first master
  x (integer) - horizontal position of the final point of the node
  y (integer) - vertical position of the final point of the node

OPERATIONS:
  len() - returns number of points in the node, same as count attribute
  [] - can be used to access individial points of the first master
  multiply - second operand must be Matrix, applies matrix transformation to a node

METHODS
  Assign - assigns new values to a Node, refer to constructor for a description of possible options
  SetAllLayers(pointindex, Point p) - assigns position of the point p to all masters of the point number 'pointindex'
  Layer(masterindex) - returns list of points for the master 'masterindex'
  Section(pointindex) - returns list of points for all layers and point number 'pointindex'
  Shift(Point p, masterindex) - shifts position of all points for the master 'masterindex'
  ExpandLayer(masterindex) - copies positions of all points in the master 'masterindex' to other masters
  Transform(Matrix m) - applies Matrix transformation to the Node (see Matrix().__doc__)

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Node.Assign; argument details are not documented."""
        ...

    def ExpandLayer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Node.ExpandLayer; argument details are not documented."""
        ...

    def Layer(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Node.Layer; argument details are not documented."""
        ...

    def Section(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Node.Section; argument details are not documented."""
        ...

    def SetAllLayers(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Node.SetAllLayers; argument details are not documented."""
        ...

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Node.Shift; argument details are not documented."""
        ...

    def Transform(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.Node.Transform; argument details are not documented."""
        ...
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
    """===============================================
  Point - base class to represent point
===============================================
Integer or float values are accepted as coordinates

CONSTRUCTOR:
  Point() - generic constructor, creates a Point with zero coordinates
  Point(Point) - copy constructor
  Point(x, y) - creates a Point and assigns coordinates. x and y may be integer or float

ATTRIBUTES:
  parent (read-only) - Point's parent object
  x (integer or float) - horizontal position of the point
  y (integer or float) - vertical position of the point

OPERATIONS:
  == - compares two points, both coordinates must be equal
  add - Point must be second operand, both coordinates are added
  subtract - Point must be second operand, both coordinates are added
  multiply - second operand may be Point, float or Matrix. If second operand is Point, then result of scalar product is returned

METHODS
  Assign(Point p) | (x, y) - assigns new values to a Point
  Shift(Point p) | (x, y) - shifts Point on a position defined by p or x and y values
  Add(Point p) - same as Shift(Point p)
  Sub(Point p) - subtracts p coordinates from the current Point
  Mul(float s) - mutiplies Point's position to s value
  Transform(Matrix m) - applies Matrix transformation to the Point (see Matrix().__doc__)

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Add(self, p: Any) -> Any:
        """Add(Point p) - same as Shift(Point p)"""
        ...

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        """Assign(Point p) | (x, y) - assigns new values to a Point"""
        ...

    def Mul(self, s: float) -> Any:
        """Mul(float s) - mutiplies Point's position to s value"""
        ...

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        """Shift(Point p) | (x, y) - shifts Point on a position defined by p or x and y values"""
        ...

    def Sub(self, p: Any) -> Any:
        """Sub(Point p) - subtracts p coordinates from the current Point"""
        ...

    def Transform(self, m: Any) -> Any:
        """Transform(Matrix m) - applies Matrix transformation to the Point (see Matrix().__doc__)"""
        ...
    x: Any
    y: Any

class Rect:
    """===============================================
  Rect - base class to represent rectangle
===============================================
Integer or float values are accepted as coordinates

CONSTRUCTOR:
  Rect() - generic constructor, creates a Rect with zero coordinates
  Rect(Rect r) - copy constructor
  Rect(Point p) - creates rectangle with one corner at (0, 0) and another - at coordinates defined by p
  Rect(Point p0, Point p1) - creates rectangle defined by the corner points
  Rect(x0, y0, x1, y1) - creates a rectangle defined by the coordinates of the corner points

ATTRIBUTES:
  ll (Point) - position of the left/bottom corner
  ur (Point) - position of the right/top corner
  x (integer or float) - horizontal position of the left corner
  y (integer or float) - vertical position of the bottom corner
  width (integer or float) - width of the rectangle
  height (integer or float) - height of the rectangle

OPERATIONS:
  add - Point or Rect must be second operand, rectangle is expanded to include this point or rectange
  multiply - second operand must be Matrix. Matrix transformation is applied to the rectangle

METHODS
  Assign(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - assigns new values to a Rect, the same as constructor
  Shift(Point p) | (x, y) - shifts Rect on a position defined by p or x and y values
  Transform(Matrix m) - applies Matrix transformation to the Rect (see Matrix().__doc__)
  Resize(width, height) - resizes rectangle to new width and height
  Include(Rect r) | (Point p) | (x, y)  - expands rectangle to include new rectangle or point
  Check(Rect r) - returns True if r overlaps current rectangle
  Check(Point p) - returns True if p is insude current rectangle
  Validate() - corrents rectangle's orientation

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def Assign(self, *args: Any, **kwargs: Any) -> Any:
        """Assign(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - assigns new values to a Rect, the same as constructor"""
        ...

    def Check(self, *args: Any, **kwargs: Any) -> Any:
        """Check(Rect r) - returns True if r overlaps current rectangle
Check(Point p) - returns True if p is insude current rectangle"""
        ...

    def Include(self, *args: Any, **kwargs: Any) -> Any:
        """Include(Rect r) | (Point p) | (x, y)  - expands rectangle to include new rectangle or point"""
        ...

    def Resize(self, width: Any, height: Any) -> Any:
        """Resize(width, height) - resizes rectangle to new width and height"""
        ...

    def Shift(self, *args: Any, **kwargs: Any) -> Any:
        """Shift(Point p) | (x, y) - shifts Rect on a position defined by p or x and y values"""
        ...

    def Transform(self, m: Any) -> Any:
        """Transform(Matrix m) - applies Matrix transformation to the Rect (see Matrix().__doc__)"""
        ...

    def Validate(self) -> Any:
        """Validate() - corrents rectangle's orientation"""
        ...
    height: Any
    ll: Any
    ur: Any
    width: Any
    x: Any
    y: Any

class TTGasp:
    """TTGasp

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

class TTPoint:
    """===============================================
  TTPoint - class to represent TrueType points
===============================================
All coordinates in TTPoint class are set in 10.6 fixed-point format

CONSTRUCTOR:
  TTPoint() - generic constructor, creates a TTPoint with zero coordinates

ATTRIBUTES:
  x (integer) - x coordinate
  y (integer) - y coordinate
  flag (integer) - point's flag (on-curve or off-curve)

OPERATIONS:

METHODS

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    flag: Any
    x: Any
    y: Any

class TTVdmx:
    """TTVdmx

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

class TrueTypeTable:
    """===============================================
  TrueTypeTable - class to represent custom OpenType table
===============================================

CONSTRUCTOR:
  TrueTypeTable() - generic constructor, creates an empty TrueTypeTable record
  TrueTypeTable(TrueTypeTable) - copy constructor
  TrueTypeTable(string tag) - creates table, assigns 'tag' and empty value
  TrueTypeTable(string tag, string value) - creates TrueType table and assigns values to both attributes
  TrueTypeTable(string tag, string value, integer valuelen) - creates TrueType table and assigns values to both attributes. 'value' may include zeroes

ATTRIBUTES:
  parent (read-only) - parent object, Font
  tag (string) - TrueType table's tag
  value (string) - TrueType table's value

OPERATIONS:

METHODS

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

class Uni:
    """Uni(Int value)

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    value: Any

class VSSGaspArray:
    """VSSGaspArray

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSGaspArray.append; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSGaspArray.clean; argument details are not documented."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSGaspArray.insert; argument details are not documented."""
        ...

class VSSTTPointArray:
    """VSSTTPointArray

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSTTPointArray.append; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSTTPointArray.clean; argument details are not documented."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSTTPointArray.insert; argument details are not documented."""
        ...

class VSSVdmxArray:
    """VSSVdmxArray

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSVdmxArray.append; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSVdmxArray.clean; argument details are not documented."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native FL.VSSVdmxArray.insert; argument details are not documented."""
        ...

class WeightVector:
    """WeightVector

Native bases: object"""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
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
__all__ = ['Anchor', 'BUTTONCONTROL', 'CHECKBOXCONTROL', 'CHOICECONTROL', 'Cancel', 'Canvas', 'CmapTable', 'Component', 'Dialog', 'EDITCONTROL', 'Encoding', 'EncodingRecord', 'Feature', 'Features', 'Font', 'Glyph', 'Guide', 'Hint', 'Image', 'KerningArray', 'KerningPair', 'LISTCONTROL', 'Link', 'Matrix', 'NULLCONTROL', 'Node', 'OK', 'PREVIEWCONTROL', 'Point', 'Rect', 'STATICCONTROL', 'STYLE_BEVELBUTTON', 'STYLE_BUTTON', 'STYLE_CHECKBOX', 'STYLE_CHOICE', 'STYLE_CUSTOM', 'STYLE_EDIT', 'STYLE_FRAME', 'STYLE_LABEL', 'STYLE_LIST', 'TTGasp', 'TTPoint', 'TTVdmx', 'TrueTypeTable', 'Uni', 'VSSGaspArray', 'VSSTTPointArray', 'VSSVdmxArray', 'WS_BORDER', 'WS_CAPTION', 'WS_CHILD', 'WS_CLIPCHILDREN', 'WS_CLIPSIBLINGS', 'WS_DISABLED', 'WS_DLGFRAME', 'WS_GROUP', 'WS_HSCROLL', 'WS_MAXIMIZE', 'WS_MAXIMIZEBOX', 'WS_MINIMIZE', 'WS_MINIMIZEBOX', 'WS_OVERLAPPED', 'WS_OVERLAPPEDWINDOW', 'WS_POPUP', 'WS_POPUPWINDOW', 'WS_SYSMENU', 'WS_TABSTOP ', 'WS_THICKFRAME', 'WS_VISIBLE', 'WS_VSCROLL', 'WeightVector', 'aALIGN', 'aAUTO', 'aIDENT', 'aIDENT2', 'aIDENT3', 'aNEXT', 'aSAME', 'cBRUSH_NULL', 'cBRUSH_SOLID', 'cPEN_DASH', 'cPEN_DOT', 'cPEN_NULL', 'cPEN_SOLID', 'cRECT_3DDOWN', 'cRECT_3DDOWN_FLAT', 'cRECT_3DDOWN_SOLID', 'cRECT_3DUP', 'cRECT_3DUP_FLAT', 'cRECT_3DUP_SOLID', 'cRECT_BLACK_FRAME', 'cRECT_BLACK_SOLID', 'cRECT_BLACK_THICK_FRAME', 'cRECT_ELLIPSE', 'cRECT_FOCUS', 'cRECT_GRAY_FRAME', 'cRECT_GRAY_SOLID', 'cRECT_INVERT', 'cRECT_LTGRAY_SOLID', 'cRECT_RECTANGLE', 'cRECT_SIZE', 'cRECT_WHITE_SOLID', 'cRECT_YELLOW_FRAME', 'cRECT_YELLOW_SOLID', 'cRGB_BLACK', 'cRGB_BLUE', 'cRGB_GRAY', 'cRGB_GREEN', 'cRGB_LTGRAY', 'cRGB_RED', 'cRGB_WHITE', 'cRGB_YELLOW', 'cTO_BOTTOM', 'cTO_CENTER', 'cTO_LEFT', 'cTO_RIGHT', 'cTO_TOP', 'cTO_VCENTER', 'fl', 'ftFONTLAB', 'ftMACTRUETYPE', 'ftMACTRUETYPE_DFONT', 'ftMACTYPE1', 'ftOPENTYPE', 'ftTRUETYPE', 'ftTYPE1', 'ftTYPE1ASCII', 'ftTYPE1ASCII_MM', 'ftTYPE1_MM', 'nCURVE', 'nFIXED', 'nLINE', 'nMOVE', 'nOFF', 'nSHARP', 'nSMOOTH']
