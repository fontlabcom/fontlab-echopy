# this_file: src/fontlab_echopy/fontgate.pyi
# Generated from native metadata and independent enrichment inputs.
"""FontGate Python interface

fgAnchor: Anchor representation
fgAnchors: list of fgAnchor objects
fgAxes: Axes list representation
fgAxis: Axis representation
fgCMaps: list of fgCmapRecord objects
fgCaret: Caret representation
fgCarets: list of fgCaret objects
fgCmapRecord: fgCmapRecord representation
fgCoding: Coding data representation
fgComponent: Component representation
fgComponents: list of fgComponent objects
fgContour: Contour representation
fgContours: list of fgContour objects
fgCuspPoint: CuspPoint representation
fgCuspPoints: list of fgCuspPoint objects
pyfgDataOwnerData: pyfgDataOwnerData objects
fgDesignPosition: Anchor representation
fgDeviceRecord: DeviceRecord representation
fgDeviceRecords: list of fgDeviceRecord objects
fgExtMapUIntToString: fgExtMapUIntToString dictionary
fgFont: Font representation
fgFontHinting: Font Hinting data representation
fgFontInfo: FontInfo data
fgFontInfoDict: Font info dictionaries
fgGaspRecord: GaspRecord representation
fgGaspRecords: list of fgGaspRecord objects
fgGlyph: Glyph representation
fgGlyphsR: fgGlyphsR representation
fgGlyphDict: Glyph dictionaries
fgGlyphIDsSet: GlyphIDs set
fgGlyphs: list of fgGlyph objects
fgGroup: Kerning/Metrics group
fgGroups: Glyph groups list
fgGuide: Guide representation
fgGuides: list of fgGuide objects
fgHint: Hint representation
fgHintCommand: HintCommand representation
fgHintCommands: list of fgHintCommand objects
fgHints: list of fgHint objects
fgKerning: Kerning representation
fgKerningGroups: Dictionary of kerning groups
fgKerningObject: KerningObject representation
fgKerningObjectPair: KerningObjectPair representation
fgLayer: Layer representation
fgLayers: list of fgLayer objects
fgLib: Dictionary with font- or glyph-related data
fgMapBytes: Raw data dictionary
fgExtMapIntTofgShape: fgExtMapIntTofgShape dictionary
fgFlagsDict: bool flags diactionary
fgValuesDict: float values dictionary
fgIntDict: int dictionary
fgStringDict: string dictionary
fgMaster: Anchor representation
fgMasters: list of fgMaster objects
fgMaxP: fgMaxP representation
fgMetricsClass: MetricsClass representation
fgMetricsClasses: list of fgMetricsClass objects
fgNametable: NameTable - unicode->name translation and vice versa
fgNode: Node representation
fgNodes: list of fgNode objects
fgOTLayout: OpenType Layout representation
fgOtInfo: OT Info representation
fgOtValue: OT Value representation
fgPackages: Font packages representation
fgPen: Pen representation
fgExtMapUShortToShort: fgExtMapUShortToShort dictionary
fgShape: Shape representation
fgShapes: list of fgShape objects
fgStem: Stem representation
fgStems: list of fgStem objects
fgTrueTypePoint: TrueType Point representation
fgTrueTypePoints: list of fgTrueTypePoint objects
fgTTInterpreter: TTInterpreter representation
fgVdmxRecord: fgVdmxRecord representation
fgVdmxRecords: list of fgVdmxRecord objects
fgVectorBool: [char] vector
fgVectorChar: [char] vector
fgVectorDouble: [double] vector
fgVectorInt: [int] vector
fgVectorUInt16: [uint16_t] vector
fgVectorUInt32: [uint32t] vector
fgVectorPoint: [fgPoint] vector
fgZone: Zone representation
fgZones: list of fgZone objects
fgOptions: FontGate options
fgOpt_T1Import: fgOpt_T1Import options page
fgOpt_OTImport: fgOpt_OTImport options page
fgOpt_UfoFontImport: fgOpt_UfoFontImport options page
fgOpt_VfbImport: fgOpt_VfbImport options page
fgOpt_VfbExport: fgOpt_VfbExport options page
fgOpt_UfoFontExport: fgOpt_UfoFontExport options page
fgOpt_OTExport: fgOpt_OTExport options page
fgOpt_T1Export: fgOpt_T1Export options page
fgOpt_EOTExport: fgOpt_EOTExport options page
fgOpt_WOFFExport: fgOpt_WOFFExport options page
fgOpt_Font: fgOpt_Font options page
fgOpt_KerningOptions: fgOpt_KerningOptions options page
fgOpt_OTExportFeaFile: fgOpt_OTExportFeaFile options page
fgOpt_TTAutohint: fgOpt_TTAutohint options page
fgOpt_T1Autohint: fgOpt_T1Autohint options page
fgOpt_TTFAutohint: fgOpt_TTFAutohint options page
fgOpt_AutoMetrics: fgOpt_AutoMetrics options page
fgOpt_ExpandKerning: fgOpt_ExpandKerning options page
fgOpt_Optimize: fgOpt_Optimize options page
fgBitmap: Bitmap representation
fgBitmaps: list of  fgBitmap objects
fgBitmapsData: BitmapsData representation
fgBrush: Brush representation
fgColor: Color representation
fgCurve: Curve representation
fgFontGateData: FontGateData representation
fgGlyphData: GlyphData representation
fgExtMapUCharToUChar: fgExtMapUCharToUChar dictionary
fgMatrix: Transformation matrix representation
fgPoint: Point representation
fgPointU: PointU representation
fgRect: Rectangle representation
fgRendered: fgRendered representation
fgTrueTypeData: TrueTypeData representation
fgVector: Vector representation

Supplemental documentation:
Low-level FontLab font data API. fgFont provides glyphs, naming data, features and kerning; fgGlyph provides glyph data. Feature data is exposed by fgFont.features; there is no captured module-level fgFeatures class."""
from __future__ import annotations
from typing import Any

class fgAnchor:
    """Anchor representation

Constructors:
  fgAnchor() - default
  fgAnchor(fgAnchor) - copy
  fgAnchor((x, y), 'name') - create with position=(x, y) and name='name'
  fgAnchor(x, y, 'name') - create with position=(x, y) and name='name'

Native bases: object

Supplemental documentation:
A font-data anchor with `name`, `x` and `y` attributes. `position` exposes its coordinates as an fgPoint. `draw()` sends the anchor to a segment pen; `drawPoints()` uses a point pen. Consult the retained constructors for copying and named coordinate forms.

Source: generated/fontgate.py: fgAnchor captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def copy(self, arg0: fgAnchor) -> Any:
        """copy(fgAnchor) - copy data from another fgAnchor object"""
        ...

    def draw(self, penObject: Any) -> Any:
        """draw(penObject) - draw the object with a segment pen"""
        ...

    def drawPoints(self, penObject: Any) -> Any:
        """drawPoints(penObject) - draw the object with a point pen"""
        ...

    def move(self, dx: Any, dy: Any) -> Any:
        """move(dx, dy) - move anchor by (dx, dy)"""
        ...

    def round(self) -> Any:
        """round() - round anchor coordinates"""
        ...

    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """scale((scale_x, scale_y)[, (center_x, center_y)]) - scale anchor by (scale_x, scale_y) with center=(center_x, center_y) or (0,0) if not defined"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix) - transform anchor coordinates by matrix"""
        ...
    data: Any
    '(uint) - data'
    index: Any
    "(int) - index of object for owner's base layer"
    mark: Any
    '(uint) - mark'
    name: Any
    '(string) - name'
    position: Any
    '(fgPoint) - coordinates as fgPoint'
    x: Any
    '(int/double) - horizontal coordinate'
    y: Any
    '(int/double) - vertical coordinate'

class fgAnchors:
    """list of fgAnchor objects

Native bases: object

Supplemental documentation:
A list of anchor objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgAnchors captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgAxes:
    """Axes list representation

Constructors:
  fgAxes() - default
  fgAxes(fgAxes) - copy

Native bases: object

Supplemental documentation:
An axes list representation with a `masters` attribute holding the masters (fgMasters). It is created as `fgAxes()` or as a copy `fgAxes(fgAxes)`.

Source: generated/fontgate.py: fgAxes captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    masters: Any
    '(fgMasters) - masters'

class fgAxis:
    """Axis representation

Constructors:
  fgAxis('name') - create with name='name'

Native bases: object

Supplemental documentation:
An axis. The captured declaration exposes the attributes `blendMap`, `map`, `name`, `shortName` and `type`. It is created as `fgAxis('name')`, which sets the name.

Source: generated/fontgate.py: fgAxis captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    blendMap: Any
    '(list(Point))'
    map: Any
    '(list(Point))'
    name: Any
    '(string) - name'
    shortName: Any
    '(string) - shortName'
    type: Any
    '(string) - type'

class fgBitmap:
    """Bitmap representation

Constructors:
  fgBitmap() - default
  fgBitmap(fgBitmap) - make orphan copy of another object
  fgBitmap(width, height, bitsPerPixel)
  fgBitmap(width, height, rowBytes, bitsPerPixel, bytesarray)

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear all data"""
        ...

    def clone(self, source: fgBitmap) -> Any:
        """clone(fgBitmap source) - make clone of source bitmap"""
        ...

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(fgBitmap source[, x, y, w, h]) - copy whole source bitmap or part of it with size (w, h) from pos (x, y)"""
        ...

    def copyData(self, *args: Any, **kwargs: Any) -> Any:
        """copy(bytesarray) - assign new bitmap data"""
        ...

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(<same as constructor's arguments>') - allocate new bitmap data"""
        ...

    def downsample(self, arg0: fgBitmap, oversampling: int) -> Any:
        """downsample(fgBitmap, int oversampling)"""
        ...

    def empty(self) -> bool:
        """bool empty() - return true if no data assigned or bitmap size is 0"""
        ...

    def emptyRow(self, y: Any, x0: Any, x1: Any) -> Any:
        """emptyRow(y, x0, x1) - return true if part of row y from x0 till x1 has no non-zero pixels"""
        ...

    def fill(self, color: fgColor) -> Any:
        """fill(fgColor color) - fill entire bitmap by color"""
        ...

    def flipV(self, *args: Any, **kwargs: Any) -> Any:
        """flip bitmap by vertical axis"""
        ...

    def getPixel(self, x: Any, y: Any) -> fgColor:
        """fgColor getPixel(x, y) - get color of pixel (x, y)"""
        ...

    def row(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgBitmap.row; argument details are not documented."""
        ...

    def setPixel(self, x: Any, y: Any, color: fgColor) -> Any:
        """setPixel(x, y, fgColor color) - set color for pixel (x, y)"""
        ...
    bpp: Any
    'bits per pixel'
    bytes: Any
    'bytes per row'
    data: Any
    'bitmap data'
    height: Any
    'bitmap height in pixels'
    size: Any
    'overall bytes count for bitmap storage'
    width: Any
    'bitmap width in pixels'

class fgBitmaps:
    """list of  fgBitmap objects

Native bases: object

Supplemental documentation:
A list of bitmap objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgBitmaps captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgBitmaps.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgBitmaps.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgBitmaps.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgBitmaps.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgBitmaps.insert; argument details are not documented."""
        ...

class fgBitmapsData:
    """BitmapsData representation

Constructors:
  fgBitmapsData() - default
  fgBitmapsData(fgBitmapsData) - copy

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def OK(self) -> bool:
        """bool OK() - return true if status is gdsOK"""
        ...

    def bad(self) -> bool:
        """bool bad() - return true if status isn't gdsOK"""
        ...

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        """fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box"""
        ...

    def copy(self) -> fgBitmapsData:
        """fgBitmapsData copy() - create alone copy of data"""
        ...

    def countPictures(self) -> int:
        """int countPictures() - return pictures count"""
        ...

    def getFontGateData(self, *args: Any, **kwargs: Any) -> Any:
        """getFontGateData() always return 0"""
        ...

    def getType(self) -> Any:
        """string getType() - return 'dtBitmaps'"""
        ...

    def hasBody(self, prepareExport: bool) -> bool:
        """bool hasBody(bool prepareExport) - return true if non-empty body layer is present"""
        ...

    def hasColors(self) -> bool:
        """bool hasColors() - return true if colors is present"""
        ...

    def hasHints(self) -> bool:
        """bool hasHints() - return true if hints is present"""
        ...

    def hasPictures(self) -> bool:
        """bool hasPictures() - return true if pictures is present"""
        ...

    def modified(self) -> bool:
        """bool modified() - always return false"""
        ...

    def setParent(self, arg0: fgGlyph) -> Any:
        """setParent(fgGlyph) - set parent glyph"""
        ...

    def status(self) -> Any:
        """'gdsOK'/'gdsInvalid' status()"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix) - transform data"""
        ...

    def updated(self) -> Any:
        """updated() - mark data as changed, reset internal caches"""
        ...
    bitmaps: Any
    '(fgBitmaps) - list of fgRendered objects'

class fgBrush:
    """Brush representation

Constructors:
  fgBrush() - default
  fgBrush(fgBrush) - copy
  fgBrush(fgColor) - solid brush with selected color and default size (1, 0)
  fgBrush(fgColor, fgPoint) - solid brush with selected color and size

Native bases: object

Supplemental documentation:
A brush. The captured declaration exposes the attributes `kind`, `size` and `solid`, and the methods `asDict`, `asTuple`, `black`, `isBlack`, `isTransparent` and `transparent`. It is created as `fgBrush()`, as a copy `fgBrush(fgBrush)`, as `fgBrush(fgColor)` for a solid brush with the default size (1, 0), or as `fgBrush(fgColor, fgPoint)` for a solid brush with a size.

Source: generated/fontgate.py: fgBrush captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def black(self) -> fgBrush:
        """fgBrush black() - get black solid brush"""
        ...

    def isBlack(self) -> bool:
        """bool isBlack() - return true if brush is black"""
        ...

    def isTransparent(self) -> bool:
        """bool isTransparent() - return true if brush is transparent"""
        ...

    def transparent(self) -> fgBrush:
        """fgBrush transparent() - get transparent solid brush"""
        ...
    kind: Any
    "('Empty'/'Solid'/'Gradient') brush type "
    size: Any
    '(fgPoint) brush size by x and y axis'
    solid: Any
    '(fgColor) brush color '

class fgCMaps:
    """list of fgCmapRecord objects

Native bases: object

Supplemental documentation:
A list of character map objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgCMaps captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCMaps.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCMaps.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCMaps.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCMaps.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCMaps.insert; argument details are not documented."""
        ...

class fgCaret:
    """Caret representation

Constructors:
fgCaret() - default
fgCaret(fgCaret) - copy
fgCaret((fgOtValue/float/int, 'name')) - by coordinate and name

Native bases: object

Supplemental documentation:
A caret with a string `name` and a coordinate `v` (fgOtValue). It is created as `fgCaret()`, as a copy `fgCaret(fgCaret)` or from a coordinate and name as `fgCaret((fgOtValue/float/int, 'name'))`.

Source: generated/fontgate.py: fgCaret captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    name: Any
    '(string) name'
    v: Any
    '(fgOtValue) coordinate'

class fgCarets:
    """list of fgCaret objects

Native bases: object

Supplemental documentation:
A list of caret objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgCarets captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgCmapRecord:
    """fgCmapRecord representation

Native bases: object

Supplemental documentation:
A cmap record. The captured declaration exposes the attributes `eid`, `format`, `lid`, `nid`, `pagename`, `pid` and `type`, and the methods `asDict` and `asTuple`.

Source: generated/fontgate.py: fgCmapRecord captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    eid: Any
    format: Any
    lid: Any
    nid: Any
    pagename: Any
    pid: Any
    type: Any

class fgCoding:
    """Coding data representation

Constructors:
  fgCoding() - default
  fgCoding(fgCoding) - copy
  fgCoding( bool [unicodeRange], bool [codepageRange], fgCMaps cmaps,
         fgEncoding encoding, fgEncoding importedEncoding,
         'encDefault'/'encStandard'/'encCustom')

Native bases: object

Supplemental documentation:
Coding data. The captured declaration exposes the attributes `cmaps`, `codepageRange`, `encoding`, `encodingType`, `importedEncoding` and `unicodeRange`. It is created as `fgCoding()`, as a copy `fgCoding(fgCoding)` or as `fgCoding(bool [unicodeRange], bool [codepageRange], fgCMaps cmaps, fgEncoding encoding, fgEncoding importedEncoding, 'encDefault'/'encStandard'/'encCustom')`.

Source: generated/fontgate.py: fgCoding captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    cmaps: Any
    '(fgCMaps)'
    codepageRange: Any
    '(bool list)'
    encoding: Any
    '(fgEncoding)'
    encodingType: Any
    "('encDefault'/'encStandard'/'encCustom')"
    importedEncoding: Any
    '(fgEncoding)'
    unicodeRange: Any
    '(bool list)'

class fgColor:
    """Color representation

Constructors:  fgColor() - default
  fgColor(fgColor) - copy
  fgColor(float hueValue) - by hue value  fgColor(r, g, b) - by r, g, b, float values from 0 to 1.0
  fgColor(r, g, b, a) - by r, g, b, a float values from 0 to 1.0

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def A(self) -> int:
        """int A() - get alpha value as int (0..255)"""
        ...

    def B(self) -> int:
        """int B() - get blue value as int (0..255)"""
        ...

    def G(self) -> int:
        """int G() - get green value as int (0..255)"""
        ...

    def R(self, *args: Any, **kwargs: Any) -> Any:
        """int B() - get blue value as int (0..255)"""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def black(self) -> fgColor:
        """fgColor black() - get black color"""
        ...

    def fromInt(self, r: Any, g: Any, a: Any=...) -> fgColor:
        """fgColor fromInt(r, g, b[, a=255]) - get color by int rgb(a) values (0..255)"""
        ...

    def fromLab(self, l: Any, a: Any, b: Any) -> fgColor:
        """fgColor fromLab(l, a, b) - get color by float lab values"""
        ...

    def getCMYK(self, *args: Any, **kwargs: Any) -> Any:
        """(c, m, y, k, a) getCMYK([varK = 0.3]) - get color as CMYK+A components"""
        ...

    def gray(self) -> float:
        """float gray() - get color as grayscale level"""
        ...

    def hue(self) -> float:
        """float hue() - get hue value"""
        ...

    def lab(self, *args: Any, **kwargs: Any) -> Any:
        """(l, a, b) lab() - get color as lab float values"""
        ...

    def lightness(self) -> float:
        """float lightness() - get lightness value"""
        ...

    def saturation(self) -> float:
        """float saturation() - get saturation value"""
        ...

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """set((r, g, b[, a])) - set color by tuple with rgb or rgba float values"""
        ...

    def setCMYK(self, *args: Any, **kwargs: Any) -> Any:
        """setCMYK(c, m, y, k[, _a = 1.0]) = set color by CMYK[A] float values"""
        ...

    def setGray(self, *args: Any, **kwargs: Any) -> Any:
        """segGray(float v) - set rgb components to v"""
        ...

    def setHue(self, s: Any=...) -> Any:
        """setHue(h[, s=1.0[, l = 0.5]]) - set by hsl float values"""
        ...

    def transparent(self) -> fgColor:
        """fgColor transparent() - get transparent color"""
        ...

    def xyz(self, *args: Any, **kwargs: Any) -> Any:
        """(x, y, z) xyz() - get color as xyz float values"""
        ...
    a: Any
    '(float 0..1.0) - alpha channel'
    b: Any
    '(float 0..1.0) - blue channel'
    g: Any
    '(float 0..1.0) - green channel'
    r: Any
    '(float 0..1.0) - red channel'

class fgComponent:
    """Component representation

Constructors:
  fgComponent() - default
  fgComponent(fgComponent) - copy
  fgComponent('name', fgMatrix) - by 'name' and transformation matrix fgMatrix

Native bases: object

Supplemental documentation:
A component. The captured declaration exposes the attributes `baseGlyph`, `box`, `hasFullMatrix`, `index`, `matrix`, `offset` and `scale`, and the methods `draw`, `drawPoints` and `move`. `draw` takes a segment pen, `drawPoints` takes a point pen, and `move` takes float dx and dy. It is created as `fgComponent()`, as a copy `fgComponent(fgComponent)` or as `fgComponent('name', fgMatrix)`.

Source: generated/fontgate.py: fgComponent captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def draw(self, object: Any) -> Any:
        """draw(pen object) - draw the object with a segment pen"""
        ...

    def drawPoints(self, object: Any) -> Any:
        """drawPoints(pen object) - draw the object with a point pen"""
        ...

    def move(self, dx: Any, dy: Any) -> Any:
        """move(dx, dy) - move by float dx, dy value"""
        ...
    baseGlyph: Any
    '(string) name of base glyph'
    box: Any
    '(fgRect) - bounding box'
    hasFullMatrix: Any
    index: Any
    "(int) component index in glyph's components list"
    matrix: Any
    '(fgMatrix) - component transform matrix'
    offset: Any
    scale: Any

class fgComponents:
    """list of fgComponent objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgComponents.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgComponents.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgComponents.clean; argument details are not documented."""
        ...

    def decompose(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgComponents.decompose; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgComponents.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def getAsList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgComponents.getAsList; argument details are not documented."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgComponents.insert; argument details are not documented."""
        ...

class fgContour:
    """Contour representation

Constructors:
  fgContour() - default
  fgContour(fgContour) - copy

Native bases: object

Supplemental documentation:
A contour in the fontgate data model. The captured declaration exposes `nodes`, `getNodes`, `getNode`, `countNodes` and `open`. Consult the native declarations for supported calling conventions.

Source: generated/fontgate.py: fgContour captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def appendNode(self, arg0: fgNode) -> Any:
        """appendNode(fgNode) - add node to the end of the contour"""
        ...

    def area(self) -> float:
        """float area()"""
        ...

    def autoClose(self) -> bool:
        """bool autoClose() - bool autoClose() - close contour, return true if changes was made"""
        ...

    def autoInterpolated(self) -> bool:
        """bool autoInterpolated() - interpolate contour nodes, return true if changes was made"""
        ...

    def autoSmooth(self) -> bool:
        """bool autoSmooth() - smooth contour nodes, return true if changes was made"""
        ...

    def boundingBox(self, prepareExport: Any=...) -> fgRect:
        """fgRect boundingBox(fgMatrix[, bool prepareExport = false])"""
        ...

    def clear(self) -> Any:
        """clear() - clear all nodes"""
        ...

    def contains(self, winding: Any=...) -> Any:
        """bool/Nothing contains(fgPoint[, bool winding = false])"""
        ...

    def containsCurvePoint(self) -> bool:
        """bool containsCurvePoint()"""
        ...

    def containsOffPoint(self) -> bool:
        """bool containsOffPoint()"""
        ...

    def countNodes(self) -> int:
        """int countNodes() - get count of nodes"""
        ...

    def deleteNode(self, nodeIndex: int) -> bool:
        """bool deleteNode(int nodeIndex) - delete node"""
        ...

    def draw(self, segmentPen: Any) -> Any:
        """draw(segmentPen) - draw the object with a segment pen"""
        ...

    def drawPoints(self, pointPen: Any) -> Any:
        """drawPoints(pointPen) - draw the object with a point pen"""
        ...

    def empty(self) -> bool:
        """bool empty() - return True if contour haven't any node"""
        ...

    def filterOnPoints(self) -> Any:
        """filterOnPoints()"""
        ...

    def getNode(self, nodeIndex: int) -> fgNode:
        """fgNode getNode(int nodeIndex) - get node by index"""
        ...

    def getNodes(self) -> Any:
        """[ fgNode ] getNodes() - get list of fgNode objects"""
        ...

    def getUFONodesList(self, *args: Any, **kwargs: Any) -> Any:
        """[ ((x, y), 'nodetype', bool smooth, 'name') ] getUFONodesList() -get list of contour nodes as UFO-style tuples"""
        ...

    def insertNode(self, arg0: fgNode, insertTo: int) -> Any:
        """insertNode(fgNode, int insertTo) - insert node into position insertTo"""
        ...

    def isCompatible(self, arg0: fgContour) -> bool:
        """bool isCompatible(fgContour)"""
        ...

    def length(self) -> int:
        """int length() - get count of nodes"""
        ...

    def midPoint(self) -> fgPoint:
        """fgPoint midPoint()"""
        ...

    def reverse(self) -> Any:
        """reverse() - reverse order of contour nodes"""
        ...

    def toCurves(self, *args: Any, **kwargs: Any) -> Any:
        """toCurves([tolerance = 5.])"""
        ...

    def toShortSplines(self, *args: Any, **kwargs: Any) -> Any:
        """toShortSplines([tolerance = 5.[, bool short_splines = true]])"""
        ...

    def transform(self, arg0: fgMatrix) -> fgContour:
        """fgContour transform(fgMatrix)"""
        ...
    name: Any
    '(string) name of contour'
    nodes: Any
    '([fgNode]) contour nodes'
    open: Any
    '(bool) open flag'

class fgContours:
    """list of fgContour objects

Native bases: object

Supplemental documentation:
A list of contour objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgContours captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgContours.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgContours.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgContours.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgContours.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgContours.insert; argument details are not documented."""
        ...

class fgCurve:
    """Curve representation

Constructors:
  fgCurve() - default
  fgCurve(fgCurve) - copy
  fgCurve( [4 x fgPoint] )
  fgCurve( (q0, q1, q2, q3) )
  fgCurve( fgPoint, fgPoint )
  fgCurve( fgPoint, fgPoint, fgPoint )
  fgCurve( fgPoint, fgPoint, fgPoint, fgPoint )
  fgCurve( fgCurve, float t0, float t1 )

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def bbox(self) -> fgRect:
        """fgRect bbox()"""
        ...

    def check(self, flatness: float, length: float, w0: float, w1: float) -> bool:
        """bool check(float flatness, float length, float w0, float w1)"""
        ...

    def coefficients(self, *args: Any, **kwargs: Any) -> Any:
        """(fgPoint a, fgPoint b, fgPoint c, fgPoint d) coefficients()"""
        ...

    def curvature(self, t: float) -> float:
        """float curvature(float t)"""
        ...

    def d1(self, t: float) -> fgPoint:
        """fgPoint d1(float t)"""
        ...

    def d2(self, t: float) -> fgPoint:
        """fgPoint d2(float t)"""
        ...

    def direction(self, time: float) -> fgPoint:
        """fgPoint direction(float time)"""
        ...

    def eseg(self, u: float) -> fgCurve:
        """fgCurve eseg(float u)"""
        ...

    def flat(self, parameter: float=...) -> bool:
        """bool flat(double parameter = almost_zero)"""
        ...

    def getExtrema(self, *args: Any, **kwargs: Any) -> Any:
        """int getExtrema(bool h, [float] )"""
        ...

    def getInflection(self, *args: Any, **kwargs: Any) -> Any:
        """int getInflection( [float] )"""
        ...

    def hasExtrema(self) -> bool:
        """bool hasExtrema()"""
        ...

    def isConvex(self, *args: Any, **kwargs: Any) -> Any:
        """bool isConvex( [float area] )"""
        ...

    def len(self, quality: int) -> float:
        """float len(int quality)"""
        ...

    def maximumDeviation(self) -> float:
        """float maximumDeviation()"""
        ...

    def merge(self, c: fgCurve) -> bool:
        """bool merge(fgCurve c)"""
        ...

    def point(self, time: float) -> fgPoint:
        """fgPoint point(float time)"""
        ...

    def quickLen(self) -> float:
        """float quickLen()"""
        ...

    def render(self, *args: Any, **kwargs: Any) -> Any:
        """int render([fgPoint/fgPointU], int quality)"""
        ...

    def seg(self, stime: float, etime: float) -> fgCurve:
        """fgCurve seg(float stime, float etime)"""
        ...

    def sseg(self, u: float) -> fgCurve:
        """fgCurve sseg(float u)"""
        ...

    def time(self, *args: Any, **kwargs: Any) -> Any:
        """float time(fgPoint[, int quality[, [float min_dist] ]])"""
        ...
    q0: Any
    '(fgPoint)'
    q1: Any
    '(fgPoint)'
    q2: Any
    '(fgPoint)'
    q3: Any
    '(fgPoint)'

class fgCuspPoint:
    """CuspPoint representation

Constructors:
  fgCuspPoint() - default
  fgCuspPoint(fgCuspPoint) - copy

Native bases: object

Supplemental documentation:
A cusp point. The captured declaration exposes the attributes `hlink0`, `hlink1`, `index`, `middleH`, `middleV`, `p`, `vlink0` and `vlink1`. It is created as `fgCuspPoint()` or as a copy `fgCuspPoint(fgCuspPoint)`.

Source: generated/fontgate.py: fgCuspPoint captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def middleH(self) -> bool:
        """bool middleH()"""
        ...

    def middleV(self) -> bool:
        """bool middleV()"""
        ...
    hlink0: Any
    '(int)'
    hlink1: Any
    '(int)'
    index: Any
    '(int)'
    p: Any
    '(fgPoint)'
    vlink0: Any
    '(int)'
    vlink1: Any
    '(int)'

class fgCuspPoints:
    """list of fgCuspPoint objects

Native bases: object

Supplemental documentation:
A list of cusp point objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgCuspPoints captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCuspPoints.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCuspPoints.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCuspPoints.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCuspPoints.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgCuspPoints.insert; argument details are not documented."""
        ...

class fgDesignPosition:
    """Anchor representation

Constructors:
  fgDesignPosition() - default
  fgDesignPosition(fgDesignPosition) - copy
  fgDesignPosition(axisCount) - parametric

Native bases: object

Supplemental documentation:
A design position whose `data` attribute is a list of doubles. It is created as `fgDesignPosition()`, as a copy `fgDesignPosition(fgDesignPosition)` or from an axis count as `fgDesignPosition(axisCount)`.

Source: generated/fontgate.py: fgDesignPosition captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    data: Any
    '(list(double)) - data'

class fgDeviceRecord:
    """DeviceRecord representation

Constructors:
  fgDeviceRecord() - default
  fgDeviceRecord(fgDeviceRecord) - copy
  fgDeviceRecord(tuple( int ppm, int correction) )
  fgDeviceRecord( int ppm, int correction )

Native bases: object

Supplemental documentation:
A device record with int attributes `ppm` and `correction`. It is created as `fgDeviceRecord()`, as a copy `fgDeviceRecord(fgDeviceRecord)`, from a tuple `fgDeviceRecord(tuple(int ppm, int correction))` or as `fgDeviceRecord(int ppm, int correction)`.

Source: generated/fontgate.py: fgDeviceRecord captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    correction: Any
    '(int)'
    ppm: Any
    '(int)'

class fgDeviceRecords:
    """list of fgDeviceRecord objects

Native bases: object

Supplemental documentation:
A list of device record objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgDeviceRecords captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgExtMapIntTofgShape:
    """fgExtMapIntTofgShape dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapIntTofgShape.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapIntTofgShape.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapIntTofgShape.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapIntTofgShape.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapIntTofgShape.value; argument details are not documented."""
        ...

class fgExtMapUCharToUChar:
    """fgExtMapUCharToUChar dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUCharToUChar.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUCharToUChar.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUCharToUChar.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUCharToUChar.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUCharToUChar.value; argument details are not documented."""
        ...

class fgExtMapUIntToString:
    """fgExtMapUIntToString dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUIntToString.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUIntToString.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUIntToString.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUIntToString.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUIntToString.value; argument details are not documented."""
        ...

class fgExtMapUShortToShort:
    """fgExtMapUShortToShort dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUShortToShort.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUShortToShort.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUShortToShort.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUShortToShort.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgExtMapUShortToShort.value; argument details are not documented."""
        ...

class fgFlagsDict:
    """bool flags diactionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgFlagsDict.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgFlagsDict.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgFlagsDict.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgFlagsDict.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgFlagsDict.value; argument details are not documented."""
        ...

class fgFont:
    """Font representation

Constructors:
  fgFont() - create new empty font
  fgFont('font_name') -  - create new empty font with name 'font_name'

Native bases: object

Supplemental documentation:
A font data object. The captured declaration exposes `glyphs`, `info`, `features`, `kerning` and `axes`. Access naming information through `info`; the captured fgFont has no family attribute. Consult each native member declaration for its return type and calling convention.

Source: generated/fontgate.py: fgFont captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addGlyph(self, arg0: fgGlyph) -> fgGlyph:
        """fgGlyph addGlyph(fgGlyph)"""
        ...

    def appendFeatures(self) -> int:
        """int appendFeatures()"""
        ...

    def averageHeight(self) -> float:
        """float averageHeight()"""
        ...

    def averageWidth(self) -> float:
        """float averageWidth()"""
        ...

    def boundingBox(self, arg0: fgMatrix) -> fgRect:
        """fgRect boundingBox(fgMatrix)"""
        ...

    def calculateSafeZones(self, *args: Any, **kwargs: Any) -> Any:
        """?"""
        ...

    def checkMaps(self) -> Any:
        """checkMaps()"""
        ...

    def clearGlyphs(self) -> Any:
        """clearGlyphs() - remove all glyphs"""
        ...

    def clearMaps(self) -> Any:
        """clearMaps() - force clear all font internal caches"""
        ...

    def copyFrom(self, sourceFont: fgFont) -> Any:
        """copyFrom(fgFont sourceFont) - copy all data and glyphs from source font"""
        ...

    def createGlyph(self, clearExisting: Any=...) -> fgGlyph:
        """fgGlyph createGlyph('name'[, int unicode[, bool clearExisting = false]])"""
        ...

    def dropHintingTables(self) -> Any:
        """dropHintingTables()"""
        ...

    def dropLayoutTables(self) -> Any:
        """dropLayoutTables()"""
        ...

    def fixOrdering(self, sortMethod: Any=...) -> bool:
        """bool fixOrdering(float upm[, sortMethod='sortUnicode']) - sort glyphs by selected method. Methods are 'sortNone', 'sortName', 'sortUnicode', 'sortIndex', 'sortIndexReverse'"""
        ...

    def hasColors(self) -> bool:
        """bool hasColors()"""
        ...

    def hasPictures(self) -> bool:
        """bool hasPictures()"""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """bool has_key('name') - return true if font contains glyph with name 'name'"""
        ...

    def items(self) -> Any:
        """[('name', fgGlyph)] items() - returns a list of font's ('name', fgGlyph) tuple pairs"""
        ...

    def keys(self) -> Any:
        """['names'] keys() - return list of names of all glyphs in the font"""
        ...

    def killUnicode(self, unicode: Any) -> Any:
        """killUnicode(unicode) - remove selected unicode from all glyph unicodes lists"""
        ...

    def rebuildMaps(self) -> Any:
        """rebuildMaps() - force clear and rebuild all font internal caches"""
        ...

    def removeGlyph(self, *args: Any, **kwargs: Any) -> Any:
        """bool/Nothing removeGlyph('name'/unicode) - remove glyph selected by 'name' or unicode (int)"""
        ...

    def save(self, save_vfb: Any=...) -> Any:
        """save('path/filename'[, bool save_vfb=false]) - save font in UFO or VFB format"""
        ...

    def scale(self, arg0: float) -> Any:
        """scale(float) - scale font UPM"""
        ...

    def sortGlyphs(self, sortMethod: Any) -> Any:
        """sortGlyphs(sortMethod) - sort glyphs. sortMethod: 'sortNone'/'sortName'/'sortUnicode'/'sortIndex'/'sortIndexReverse'"""
        ...

    def update(self) -> Any:
        """update() - force rebuild font chaches and request font update"""
        ...

    def values(self) -> Any:
        """[fgGlyph] values() - returns list of font's fgGlyph"""
        ...
    axes: Any
    '(fgAxes) axes info'
    coding: Any
    '(fgCoding) encoding info'
    features: Any
    '(fgOTLayout) features data'
    glyphs: Any
    '([fgGlyph]) font glyphs list'
    groups: Any
    '(fgGroups) glyph groups list'
    guides: Any
    '(fgGuides) guides list'
    hinting: Any
    '(fgFontHinting) hinting info'
    hints: Any
    "(fgHints) hints list for font 'Body' layer"
    id: Any
    '(long) package id'
    info: Any
    '(fgFontInfo) font info data'
    kerning: Any
    '(fgKerning) kerning data'
    lib: Any
    '(fgLib) additional font data'
    master: Any
    '(fgLayer) font master layer'
    metricsClasses: Any
    '(fgMetricsClasses) list of metrics classes'
    path: Any
    '(string) path and font file name'
    shapes: Any
    '(fgMapShapes) font shapes map'
    tables: Any
    '(fgMapBytes) raw OT tables data'
    translatedNames: Any
    '([tuples]) raw style->names.translated data'

class fgFontGateData:
    """FontGateData representation

Constructors:
  fgFontGateData() - default
  fgFontGateData(fgFontGateData) - copy

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def OK(self) -> bool:
        """bool OK() - return true if status is gdsOK"""
        ...

    def activeLayer(self) -> fgLayer:
        """fgLayer activeLayer() - get active layer or Nothing if no layers exists"""
        ...

    def addContour(self, arg0: fgContour) -> fgContour:
        """fgContour addContour(fgContour) - add contour into 'Body' layer"""
        ...

    def addShape(self, arg0: fgShape) -> fgShape:
        """fgShape addShape(fgShape) - add shape into 'Body' layer"""
        ...

    def bad(self) -> bool:
        """bool bad() - return true if status isn't gdsOK"""
        ...

    def bodyLayer(self) -> fgLayer:
        """fgLayer bodyLayer() - get layer named 'Body', any existing non-service layer if not found or Nothing if no layers exists"""
        ...

    def bodyLayerStrict(self) -> fgLayer:
        """fgLayer bodyLayerStrict() - get layer named 'Body'. if it's not present, create it on the fly"""
        ...

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        """fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box"""
        ...

    def checkContours(self) -> Any:
        """checkContours() - ckeck for multi-segment contours and split it into one segment's contours"""
        ...

    def copy(self) -> fgFontGateData:
        """fgFontGateData copy() - create alone copy of data"""
        ...

    def countNodesContours(self, *args: Any, **kwargs: Any) -> Any:
        """(nodesCount, contoursCount) countNodesContours() - calculate stats for 'Body' layer if it present, return (0,0) otherwise"""
        ...

    def countPictures(self) -> int:
        """int countPictures() - return pictures count"""
        ...

    def countShapes(self) -> int:
        """int countShapes() - return shapes count"""
        ...

    def findLayer(self, *args: Any, **kwargs: Any) -> Any:
        """fgLayer findLayer('name') - get layer by name, return Nothing if no layer found"""
        ...

    def getFontGateData(self) -> fgFontGateData:
        """fgFontGateData getFontGateData() - return self"""
        ...

    def getType(self) -> Any:
        """string getType() - return 'dtFontGate'"""
        ...

    def hasBody(self, prepareExport: bool) -> bool:
        """bool hasBody(bool prepareExport) - return true if non-empty body layer is present"""
        ...

    def hasColors(self) -> bool:
        """bool hasColors() - return true if colors is present"""
        ...

    def hasHints(self) -> bool:
        """bool hasHints() - return true if hints is present"""
        ...

    def hasPictures(self) -> bool:
        """bool hasPictures() - return true if pictures is present"""
        ...

    def maskLayer(self, createIfMissing: bool) -> fgLayer:
        """fgLayer maskLayer(bool createIfMissing)"""
        ...

    def modified(self) -> bool:
        """bool modified() - return true if data was changed"""
        ...

    def resetBbox(self) -> Any:
        """resetBbox() - reset bbox cache"""
        ...

    def setParent(self, arg0: fgGlyph) -> Any:
        """setParent(fgGlyph) - set parent glyph"""
        ...

    def status(self) -> Any:
        """'gdsOK'/'gdsInvalid' status()"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix) - transform data"""
        ...

    def updated(self) -> Any:
        """updated() - mark data as changed, reset internal caches"""
        ...
    layers: Any
    '(fgLayers) layers list'

class fgFontHinting:
    """Font Hinting data representation

Constructors:
  fgFontHinting() - default
  fgFontHinting(fgFontHinting) - copy

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def generateStemsProgram(self, upm: Any, keepValues: bool) -> Any:
        """generateStemsProgram(Position upm, bool keepValues)"""
        ...

    def getBlueValues(self) -> Any:
        """list( float ) getBlueValues()"""
        ...

    def getFamilyBlues(self) -> Any:
        """list( float ) getFamilyBlues()"""
        ...

    def getFamilyOtherBlues(self, *args: Any, **kwargs: Any) -> Any:
        """list( float ) getFamilyBlues()"""
        ...

    def getOtherBlues(self) -> Any:
        """list( float ) getOtherBlues()"""
        ...

    def getZone(self, index: int, top: bool) -> Any:
        """fgZone/Nothing getZone(int index, bool top)"""
        ...

    def getZonesCount(self, top: bool) -> int:
        """int getZonesCount(bool top)"""
        ...
    blueFuzz: Any
    '(int)'
    blueScale: Any
    '(float)'
    blueShift: Any
    '(int)'
    codePPM: Any
    '(int)'
    cvt: Any
    '( bytesarray )'
    dict: Any
    '( { string : int } )'
    dropoutPPM: Any
    '(int)'
    familyZones: Any
    '(fgZones)'
    flex: Any
    '(bool)'
    forceBold: Any
    '(bool)'
    forceBoldTreshold: Any
    '(float)'
    fpgm: Any
    '( bytesarray )'
    gasp: Any
    '( [ fgGaspRecord ] )'
    hdmx: Any
    '( [ int ] )'
    maxp: Any
    '( fgMaxP )'
    prep: Any
    '( bytesarray )'
    stemH: Any
    '(float)'
    stemSnapLimit: Any
    '(int)'
    stemV: Any
    '(float)'
    stemsH: Any
    '(fgStems)'
    stemsV: Any
    '(fgStems)'
    t1stemsH: Any
    '(fgStems)'
    t1stemsV: Any
    '(fgStems)'
    t1zones: Any
    '(fgZones)'
    vdmx: Any
    '( [ fgVdmxRecord ] )'
    zonePPM: Any
    '(int)'
    zones: Any
    '(fgZones)'

class fgFontInfo:
    """FontInfo data

No constructors - it's the direct member of the fgFont object

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    ascender: Any
    'Ascender value'
    capHeight: Any
    'Cap height value'
    caretOffset: Any
    'Caret offset value'
    copyright: Any
    'Copyright statement'
    descender: Any
    'Descender value'
    dict: Any
    'Other font info tags and data'
    familyName: Any
    'Family name'
    italicAngle: Any
    'Italic angle'
    macintoshFONDFamilyID: Any
    'Family ID number. Corresponds to the ffFamID in the Macintosh FOND resource'
    macintoshFONDName: Any
    'Font name for the Macintosh FOND resource'
    note: Any
    'Arbitrary note about the font'
    openTypeHeadCreated: Any
    'Creation date and time'
    openTypeHeadFlags: Any
    'A list of bit numbers indicating the flags. Corresponds to the OpenType head table flags field'
    openTypeHeadFontDirectionHint: Any
    'Deprecated (Set to 2). Corresponds to the OpenType head table fontDirectionHint field'
    openTypeHeadLowestRecPPEM: Any
    'Smallest readable size in pixels. Corresponds to the OpenType head table lowestRecPPEM field'
    openTypeHeadModified: Any
    'Last modification date and time'
    openTypeHheaAscender: Any
    'Ascender value. Corresponds to the OpenType hhea table Ascender field'
    openTypeHheaCaretOffset: Any
    'Caret offset value. Corresponds to the OpenType hhea table caretOffset field'
    openTypeHheaCaretSlopeRise: Any
    'Caret slope rise value. Corresponds to the OpenType hhea table caretSlopeRise field'
    openTypeHheaCaretSlopeRun: Any
    'Caret slope run value. Corresponds to the OpenType hhea table caretSlopeRun field'
    openTypeHheaDescender: Any
    'Descender value. Corresponds to the OpenType hhea table Descender field'
    openTypeHheaLineGap: Any
    'Line gap value. Corresponds to the OpenType hhea table LineGap field'
    openTypeNameCompatibleFullName: Any
    'Compatible full name. Corresponds to the OpenType name table name ID 18'
    openTypeNameDescription: Any
    'Description of the font. Corresponds to the OpenType name table name ID 10'
    openTypeNameDesigner: Any
    'Designer name. Corresponds to the OpenType name table name ID 9'
    openTypeNameDesignerURL: Any
    'URL for the designer. Corresponds to the OpenType name table name ID 12'
    openTypeNameLicense: Any
    'License text. Corresponds to the OpenType name table name ID 13'
    openTypeNameLicenseURL: Any
    'URL for the license. Corresponds to the OpenType name table name ID 14'
    openTypeNameManufacturer: Any
    'Manufacturer name. Corresponds to the OpenType name table name ID 8'
    openTypeNameManufacturerURL: Any
    'Manufacturer URL. Corresponds to the OpenType name table name ID 11'
    openTypeNamePreferredFamilyName: Any
    'Preferred family name. Corresponds to the OpenType name table name ID 16'
    openTypeNamePreferredSubfamilyName: Any
    'Preferred subfamily name. Corresponds to the OpenType name table name ID 17'
    openTypeNameSampleText: Any
    'Sample text. Corresponds to the OpenType name table name ID 20'
    openTypeNameUniqueID: Any
    'Unique ID string. Corresponds to the OpenType name table name ID 3'
    openTypeNameVersion: Any
    'Version string. Corresponds to the OpenType name table name ID 5'
    openTypeNameWWSFamilyName: Any
    'WWS family name. Corresponds to the OpenType name table name ID 21'
    openTypeNameWWSSubfamilyName: Any
    'WWS Subfamily name. Corresponds to the OpenType name table name ID 22'
    openTypeOS2CodePageRanges: Any
    'A list of bit numbers that are supported code page ranges in the font. Corresponds to the OpenType OS/2 table ulCodePageRange1 and ulCodePageRange2 fields'
    openTypeOS2FamilyClass: Any
    'Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, should be in the range 0-14. The second number, representing the subclass, should be in the range 0-15. Corresponds to the OpenType OS/2 table sFamilyClass field'
    openTypeOS2Panose: Any
    'The list should contain 10 integers that represent the setting for each category in the Panose specification. This corresponds to the OpenType OS/2 table Panose field'
    openTypeOS2Selection: Any
    'A list of bit numbers indicating the bits that should be set in fsSelection. Corresponds to the OpenType OS/2 table selection field'
    openTypeOS2StrikeoutPosition: Any
    'Strikeout position. Corresponds to the OpenType OS/2 table yStrikeoutPosition field'
    openTypeOS2StrikeoutSize: Any
    'Strikeout size. Corresponds to the OpenType OS/2 table yStrikeoutSize field'
    openTypeOS2SubscriptXOffset: Any
    'Subscript x offset. Corresponds to the OpenType OS/2 table ySubscriptXOffset field'
    openTypeOS2SubscriptXSize: Any
    'Subscript horizontal font size. Corresponds to the OpenType OS/2 table ySubscriptXSize field'
    openTypeOS2SubscriptYOffset: Any
    'Subscript y offset. Corresponds to the OpenType OS/2 table ySubscriptYOffset field'
    openTypeOS2SubscriptYSize: Any
    'Subscript vertical font size. Corresponds to the OpenType OS/2 table ySubscriptYSize field'
    openTypeOS2SuperscriptXOffset: Any
    'Superscript x offset. Corresponds to the OpenType OS/2 table ySuperscriptXOffset field'
    openTypeOS2SuperscriptXSize: Any
    'Superscript horizontal font size. Corresponds to the OpenType OS/2 table ySuperscriptXSize field'
    openTypeOS2SuperscriptYOffset: Any
    'Superscript y offset. Corresponds to the OpenType OS/2 table ySuperscriptYOffset field'
    openTypeOS2SuperscriptYSize: Any
    'Superscript vertical font size. Corresponds to the OpenType OS/2 table ySuperscriptYSize field'
    openTypeOS2Type: Any
    'A list of bit numbers indicating the embedding type. Corresponds to the OpenType OS/2 table fsType field'
    openTypeOS2TypoAscender: Any
    'Ascender value. Corresponds to the OpenType OS/2 table sTypoAscender field'
    openTypeOS2TypoDescender: Any
    'Descender value. Corresponds to the OpenType OS/2 table sTypoDescender field'
    openTypeOS2TypoLineGap: Any
    'Line gap value. Corresponds to the OpenType OS/2 table sTypoLineGap field'
    openTypeOS2UnicodeRanges: Any
    'A list of bit numbers that are supported Unicode ranges in the font. Corresponds to the OpenType OS/2 table ulUnicodeRange1, ulUnicodeRange2, ulUnicodeRange3 and ulUnicodeRange4 fields'
    openTypeOS2VendorID: Any
    'Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table achVendID field'
    openTypeOS2WeightClass: Any
    'Weight class value. Must be a positive integer. Corresponds to the OpenType OS/2 table usWeightClass field'
    openTypeOS2WidthClass: Any
    'Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table usWidthClass field'
    openTypeOS2WinAscent: Any
    'Ascender value. Corresponds to the OpenType OS/2 table usWinAscent field'
    openTypeOS2WinDescent: Any
    'Descender value. Corresponds to the OpenType OS/2 table usWinDescent field'
    openTypeVheaCaretOffset: Any
    'Caret offset value. Corresponds to the OpenType vhea table caretOffset field'
    openTypeVheaCaretSlopeRise: Any
    'Caret slope rise value. Corresponds to the OpenType vhea table caretSlopeRise field'
    openTypeVheaCaretSlopeRun: Any
    'Caret slope run value. Corresponds to the OpenType vhea table caretSlopeRun field'
    openTypeVheaVertTypoAscender: Any
    'Ascender value. Corresponds to the OpenType vhea table vertTypoAscender field'
    openTypeVheaVertTypoDescender: Any
    'Descender value. Corresponds to the OpenType vhea table vertTypoDescender field'
    openTypeVheaVertTypoLineGap: Any
    'Line gap value. Corresponds to the OpenType vhea table vertTypoLineGap field'
    postscriptBlueFuzz: Any
    'BlueFuzz value. This corresponds to the Type 1/CFF BlueFuzz field'
    postscriptBlueScale: Any
    'BlueScale value. This corresponds to the Type 1/CFF BlueScale field'
    postscriptBlueShift: Any
    'BlueShift value. This corresponds to the Type 1/CFF BlueShift field'
    postscriptBlueValues: Any
    'A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field'
    postscriptDefaultCharacter: Any
    'The name of the glyph that should be used as the default character in PFM files'
    postscriptDefaultWidthX: Any
    'Default width for glyphs'
    postscriptFamilyBlues: Any
    'A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field'
    postscriptFamilyOtherBlues: Any
    'A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field'
    postscriptFontName: Any
    'Name to be used for the FontName field in Type 1/CFF table'
    postscriptForceBold: Any
    'Indicates how the Type 1/CFF ForceBold field should be set'
    postscriptFullName: Any
    'Name to be used for the FullName field in Type 1/CFF table'
    postscriptIsFixedPitch: Any
    'Indicates if the font is monospaced. A compiler could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF isFixedPitched field'
    postscriptNominalWidthX: Any
    'Nominal width for glyphs'
    postscriptOtherBlues: Any
    'A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field'
    postscriptSlantAngle: Any
    'Artificial slant angle'
    postscriptStemSnapH: Any
    'List of horizontal stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapH field'
    postscriptStemSnapV: Any
    'List of vertical stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapV field'
    postscriptUnderlinePosition: Any
    'Underline position value. Corresponds to the Type 1/CFF/post table UnderlinePosition field'
    postscriptUnderlineThickness: Any
    'Underline thickness value. Corresponds to the Type 1/CFF/post table UnderlineThickness field'
    postscriptUniqueID: Any
    'A unique ID number as defined in the Type 1/CFF specification'
    postscriptWeightName: Any
    'A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the openTypeOS2WeightClass value'
    postscriptWindowsCharacterSet: Any
    'The Windows character set. postscriptWindowsCharacterSet Options. Possible values are 1..20'
    styleMapFamilyName: Any
    'Family name used for bold, italic and bold italic style mapping'
    styleMapStyleName: Any
    "Styling link name. Perrmitted values are 'Regular', 'Italic', 'Bold', 'Bold Italic' (exactly as spelled). No other values are permitted"
    styleName: Any
    'Style name'
    trademark: Any
    'Trademark statement'
    unitsPerEm: Any
    'Units per em'
    versionMajor: Any
    'Major version'
    versionMinor: Any
    'Minor version'
    xHeight: Any
    'x-height value'
    year: Any
    'The year the font was created'

class fgFontInfoDict:
    """Font info dictionaries

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    flags: Any
    hinting: Any
    metrics: Any
    names: Any
    values: Any

class fgGaspRecord:
    """GaspRecord representation

Constructors:  fgGaspRecord() - default
  fgGaspRecord(fgGaspRecord) - copy
  fgGaspRecord(int rangeMaxPPEM, int rangeGaspBehavior) - parametric

Native bases: object

Supplemental documentation:
A gasp record. The captured declaration exposes the attributes `rangeMaxpPPEM` and the behavior constants `DOGRAY`, `GRIDFIT`, `SYMMETRIC_GRIDFIT` and `SYMMETRIC_SMOOTHING`, and the methods `addSymmetry`, `rangeGaspBehavior` and `set`. It is created as `fgGaspRecord()`, as a copy `fgGaspRecord(fgGaspRecord)` or as `fgGaspRecord(int rangeMaxPPEM, int rangeGaspBehavior)`.

Source: generated/fontgate.py: fgGaspRecord captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addSymmetry(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGaspRecord.addSymmetry; argument details are not documented."""
        ...

    def rangeGaspBehavior(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGaspRecord.rangeGaspBehavior; argument details are not documented."""
        ...

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGaspRecord.set; argument details are not documented."""
        ...
    DOGRAY: Any
    '(bool)'
    GRIDFIT: Any
    '(bool)'
    SYMMETRIC_GRIDFIT: Any
    '(bool)'
    SYMMETRIC_SMOOTHING: Any
    '(bool)'
    rangeMaxpPPEM: Any
    '(int)'

class fgGaspRecords:
    """list of fgGaspRecord objects

Native bases: object

Supplemental documentation:
A list of gasp record objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgGaspRecords captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgGlyph:
    """Glyph representation

Constructors:
  fgGlyph() - default
  fgGlyph(fgGlyph) - copy
  fgGlyph('name') - create by name

Native bases: object

Supplemental documentation:
A glyph data object. The captured declaration exposes `name`, `unicode`, `unicodes`, `width`, `anchors` and `components`. Outlines are associated with layer data rather than a contours attribute.

Example::

    print(glyph.name)
    print(glyph.unicode)
    print(glyph.width)

Source: generated/fontgate.py: fgGlyph captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addUnicode(self, unicode: Any) -> Any:
        """addUnicode(unicode) - add unicode to glyph"""
        ...

    def append(self, mtx: Any=...) -> Any:
        """append(fgGlyph[, mtx=fgMatrix()]) - append contours of source glyph to current glyph"""
        ...

    def clear(self, contours: Any=True, components: Any=True, anchors: Any=True, guides: Any=True, hints: Any=True) -> Any:
        """clear(contours=true, components=true, anchors=true, guides=true, hints=true) - clear glyph's data"""
        ...

    def countPictures(self) -> int:
        """int countPictures() - return count of glyph pictures"""
        ...

    def createContour(self) -> fgContour:
        """fgContour createContour() - create new contour"""
        ...

    def createData(self, *args: Any, **kwargs: Any) -> Any:
        """(variable type) createData(GlyphDataType) - create glyph data, specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"""
        ...

    def decompose(self) -> bool:
        """bool decompose() - decompose glyph"""
        ...

    def deleteContour(self, contourIndex: Any) -> Any:
        """deleteContour(contourIndex) - delete contour by index"""
        ...

    def draw(self, *args: Any, **kwargs: Any) -> Any:
        """draw(penObject[, fgMatrix]) - draw contour by penObject (like fgPen) with transform matrix fgMatrix"""
        ...

    def fgData(self) -> Any:
        """fgFontGateData/Nothing fgData() - get dtFontGate data if it's exist"""
        ...

    def fgDataCreate(self) -> fgFontGateData:
        """fgFontGateData fgDataCreate() - get dtFontGate data (create new one if missing)"""
        ...

    def fixComposites(self, fixRotation: Any=False) -> bool:
        """bool fixComposites(fixRotation=false)"""
        ...

    def getData(self, *args: Any, **kwargs: Any) -> Any:
        """(variable type) getData([GlyphDataType='dtFontGate']) - get glyph data, specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"""
        ...

    def getPen(self) -> fgPen:
        """fgPen getPen() - create new pen object"""
        ...

    def hasBody(self) -> bool:
        """bool hasBody() - return True if glyph has contours or picture"""
        ...

    def hasColors(self) -> bool:
        """bool hasColors() - return True if glyph has color pictures"""
        ...

    def hasData(self, GlyphDataType: Any) -> bool:
        """bool hasData(GlyphDataType) - return True if glyph data, specified by GlyphDataType, is exist. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"""
        ...

    def hasHints(self) -> bool:
        """bool hasHints() - return True if glyph has hints"""
        ...

    def hasPictures(self) -> bool:
        """bool hasPictures() - return True if glyph has pictures"""
        ...

    def hasUnicode(self, unicode: Any) -> bool:
        """bool hasUnicode(unicode) - return True if glyph has specified unicode"""
        ...

    def keepData(self, GlyphDataType: Any) -> bool:
        """bool keepData(GlyphDataType) - remove all glyph data, except one specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"""
        ...

    def killData(self, GlyphDataType: Any) -> bool:
        """bool killData(GlyphDataType) - remove glyph data, specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"""
        ...

    def killUnicode(self, unicode: Any) -> Any:
        """killUnicode(unicode) - remove unicode from glyph"""
        ...

    def modified(self, GlyphDataType: Any) -> Any:
        """modified(GlyphDataType) - inform that glyph data GlyphDataType has been modified. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"""
        ...

    def move(self, dx: Any, dy: Any) -> Any:
        """move(dx, dy) - move contour by (dx, dy)"""
        ...

    def removeOverlap(self) -> Any:
        """removeOverlap()"""
        ...

    def setData(self, object: Any) -> Any:
        """setData(GlyphData-like object) - set glyph data"""
        ...

    def setUnicode(self, unicode: Any) -> Any:
        """setUnicode(unicode) - assign unicode to glyph"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix) - transform glyph by fgMatrix data"""
        ...

    def ttData(self) -> Any:
        """fgTrueTypeData/Nothing ttData() - get dtTrueType data if it's exist"""
        ...

    def ttDataCreate(self) -> fgTrueTypeData:
        """fgTrueTypeData ttDataCreate() - get dtTrueType data (create new one if missing)"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    activeLayer: Any
    '(fgLayer) active layer or Nothing if not found'
    anchors: Any
    "([ fgAnchor ]) anchor's list"
    bodyLayer: Any
    "(fgLayer) layer 'Body' or Nothing if not found"
    bodyLayerStrict: Any
    "(fgLayer) layer 'Body' (create one if not found)"
    box: Any
    '(fgRect) glyph bounding box (int values)'
    carets: Any
    "([ fgCaret ]) caret's list"
    components: Any
    "([ fgComponent ]) component's list"
    dict: Any
    "(fgGlyphDict) glyph's data dictionary"
    fbox: Any
    '(fgRect) glyph bounding box (int/float values)'
    guides: Any
    "([ fgGuide ]) guide's list"
    height: Any
    '(float) advancedHeight'
    hints: Any
    "([ fgHint ]) hint's list"
    id: Any
    '(long) glyph ID'
    image: Any
    '(fgBitmap) first glyph image'
    index: Any
    '(int) glyph index '
    kerningLeft: Any
    '(int)'
    kerningRight: Any
    '(int)'
    layer: Any
    "(fgLayer) working layer (if present) or None. Read-only attribute, use layerName='string'|index  to change"
    layerName: Any
    '(string) name of the working layer name'
    layers: Any
    "([ fgLayer ]) layer's list"
    leftMargin: Any
    lib: Any
    "(fgLib) additional glyph's data"
    mark: Any
    "(int) glyph's mark value"
    mask: Any
    '(fgGlyph/Nothing) mask glyph'
    metrics: Any
    '(fgPoint) advancedWidth and advancedHeight'
    name: Any
    '(string) glyph name'
    note: Any
    '(string)'
    otInfo: Any
    '(fgOtInfo)'
    parent: Any
    '(fgFont) parent font for glyph'
    rightMargin: Any
    unicode: Any
    "(int/Nothing) first glyph's unicode or Nothing if unicodes aren't defined"
    unicodes: Any
    "([ int ]) unicode's list"
    vsb: Any
    '(float) vsb'
    width: Any
    '(float) advancedWidth'

class fgGlyphData:
    """GlyphData representation

Constructors:
  fgGlyphData() - default
  fgGlyphData(fgGlyphData) - copy

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def OK(self) -> bool:
        """bool OK() - return true if status is gdsOK"""
        ...

    def bad(self) -> bool:
        """bool bad() - return true if status isn't gdsOK"""
        ...

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        """fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box"""
        ...

    def copy(self) -> fgGlyphData:
        """fgGlyphData copy() - create alone copy of data"""
        ...

    def countPictures(self) -> int:
        """int countPictures() - return pictures count"""
        ...

    def countShapes(self) -> int:
        """int countShapes() - return shapes count"""
        ...

    def getFontGateData(self) -> fgFontGateData:
        """fgFontGateData getFontGateData() - return Nothing"""
        ...

    def getType(self) -> Any:
        """string getType() - return 'dtTrueType'"""
        ...

    def hasBody(self, prepareExport: bool) -> bool:
        """bool hasBody(bool prepareExport) - return true if non-empty body layer is present"""
        ...

    def hasColors(self) -> bool:
        """bool hasColors() - return true if colors is present"""
        ...

    def hasHints(self) -> bool:
        """bool hasHints() - return true if hints is present"""
        ...

    def hasPictures(self) -> bool:
        """bool hasPictures() - return true if pictures is present"""
        ...

    def modified(self) -> bool:
        """bool modified() - return true if data was changed"""
        ...

    def setParent(self, arg0: fgGlyph) -> Any:
        """setParent(fgGlyph) - set parent glyph"""
        ...

    def status(self) -> Any:
        """'gdsOK'/'gdsInvalid' status()"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix) - transform data"""
        ...

    def updated(self) -> Any:
        """updated() - mark data as changed, reset internal caches"""
        ...

class fgGlyphDict:
    """Glyph dictionaries

Native bases: object

Supplemental documentation:
Glyph dictionaries. The captured declaration exposes the attributes `flags`, `lib`, `tags` and `values`.

Source: generated/fontgate.py: fgGlyphDict captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    flags: Any
    lib: Any
    tags: Any
    values: Any

class fgGlyphIDsSet:
    """GlyphIDs set

Constructors:
  fgGlyphIDsSet() - default
  fgGlyphIDsSet(fgGlyphIDsSet) - copy

Native bases: object

Supplemental documentation:
A set of glyph ids. The captured declaration exposes `asList`, `clean`, `contains` (which returns a bool) and `del_`. It is created as `fgGlyphIDsSet()` or as a copy `fgGlyphIDsSet(fgGlyphIDsSet)`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgGlyphIDsSet captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asList(self) -> Any:
        """[ int ] asList() - return set as list"""
        ...

    def clean(self) -> Any:
        """clean() - remove all id's from set"""
        ...

    def contains(self, id: int) -> bool:
        """bool contains(int id) - return True if set contains id"""
        ...

    def del_(self, id: int) -> Any:
        """del(int id) - remove id from set

Native spelling: del; access it through getattr on the native object."""
        ...

class fgGlyphs:
    """list of fgGlyph objects

Native bases: object

Supplemental documentation:
A list of glyph objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgGlyphs captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGlyphs.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGlyphs.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGlyphs.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGlyphs.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGlyphs.insert; argument details are not documented."""
        ...

class fgGlyphsR:
    """fgGlyphsR representation

Constructors:
  fgGlyphsR() - default
  fgGlyphsR(fgGlyphsR) - copy
  fgGlyphsR(fgGlyphs) - create from list(fgGlyph)

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def find(self, *args: Any, **kwargs: Any) -> Any:
        """fgGlyph find(name|unicode)"""
        ...

    def getStats(self, *args: Any, **kwargs: Any) -> Any:
        """(totalGlyphs, avgNodesCount, avgContoursCount) getStats()"""
        ...

    def glyph(self, index: int) -> fgGlyph:
        """fgGlyph glyph(int index)"""
        ...

    def glyphByID(self, ID: int) -> fgGlyph:
        """fgGlyph glyphByID(int ID)"""
        ...

    def index(self, arg0: fgGlyph) -> int:
        """int index(fgGlyph)"""
        ...

    def indexByID(self, *args: Any, **kwargs: Any) -> Any:
        """int index(int ID)"""
        ...

    def rebuildUnicodeMap(self) -> Any:
        """rebuildUnicodeMap()"""
        ...

class fgGroup:
    """Kerning/Metrics group

Constructors:
  fgGroup() - default
  fgGroup(fgGroup) - copy
  fgGroup( tuple('name', list(ids), mode, 'mainglyphname') ) - parametric
           possible values for mode are 'FeaClassGroupMode', 'KernLeftGroupMode', 'KernRightGroupMode', 'KernBothSideGroupMode'

Native bases: object

Supplemental documentation:
A kerning or metrics group with an int `id`, a string `name` and a `mode`. The captured mode values are `'FeaClassGroupMode'`, `'KernLeftGroupMode'`, `'KernRightGroupMode'` and `'KernBothSideGroupMode'`. The captured declaration exposes `isBoth`, `isFeaGroup`, `isLeft` and `isRight`. It is created as `fgGroup()`, as a copy `fgGroup(fgGroup)` or as `fgGroup(('name', [ids], mode, 'mainglyphname'))`.

Source: generated/fontgate.py: fgGroup captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def isBoth(self, *args: Any, **kwargs: Any) -> Any:
        """True if group mode is 'KernBothSideGroupMode'"""
        ...

    def isFeaGroup(self, *args: Any, **kwargs: Any) -> Any:
        """True if group mode is 'FeaClassGroupMode'"""
        ...

    def isLeft(self, *args: Any, **kwargs: Any) -> Any:
        """True if group mode is 'KernLeftGroupMode' or 'KernBothSideGroupMode'"""
        ...

    def isRight(self, *args: Any, **kwargs: Any) -> Any:
        """True if group mode is 'KernRightGroupMode' or 'KernBothSideGroupMode'"""
        ...
    id: Any
    '(int) group id'
    mode: Any
    "('FeaClassGroupMode'/'KernLeftGroupMode'/'KernRightGroupMode'/'KernBothSideGroupMode') group mode"
    name: Any
    '(string) group name'

class fgGroups:
    """Glyph groups list

Constructors:
  fgGroups() - default
  fgGroups(fgDataOwnerData) - parametric

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self) -> Any:
        """dict('name' : fgGroup) asDict()"""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def fromClassRecords(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGroups.fromClassRecords; argument details are not documented."""
        ...

    def fromDict(self, *args: Any, **kwargs: Any) -> Any:
        """fromDict(dict('name':fgGroup))"""
        ...

    def get(self, *args: Any, **kwargs: Any) -> Any:
        """fgGroup get('name')"""
        ...

    def getAsClassRecords(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgGroups.getAsClassRecords; argument details are not documented."""
        ...

    def getCompiled(self) -> Any:
        """string getCompiled()"""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """bool has_key('name')"""
        ...

    def items(self) -> Any:
        """list(tuple('name', fgGroup)) items()"""
        ...

    def keys(self) -> Any:
        """list(names of group) keys()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """bool remove('name')"""
        ...

    def rename(self, *args: Any, **kwargs: Any) -> Any:
        """bool rename('old_name', 'new_name')"""
        ...

    def values(self) -> Any:
        """list(fgGroup) values()"""
        ...

class fgGuide:
    """Guide representation

Constructors:
  fgGuide() - default
  fgGuide(fgGuide) - copy
  fgGuide(float pos[, bool horizontal = false])
  fgGuide(fgPoint p0, fgPoint p1[, name=''[, horizonta=false[, color=fgColor]]])

Native bases: object

Supplemental documentation:
A guide. The captured declaration exposes the attributes `color`, `horizontal`, `index`, `name`, `p0`, `p1`, `position` and `vertical`, and the method `copy`. It is created as `fgGuide()`, as a copy `fgGuide(fgGuide)`, as `fgGuide(float pos[, bool horizontal = false])` or as `fgGuide(fgPoint p0, fgPoint p1[, name=''[, horizonta=false[, color=fgColor]]])`.

Source: generated/fontgate.py: fgGuide captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def copy(self) -> fgGuide:
        """fgGuide copy() - copy object"""
        ...
    color: Any
    '(fgColor)'
    horizontal: Any
    'True if guide is horizontal'
    index: Any
    '(int) index in owner guides list'
    name: Any
    '(string) guide name'
    p0: Any
    '(fgPoint)'
    p1: Any
    '(fgPoint)'
    position: Any
    '(int) y value of p0, p1 if guide is horizontal, x value - if vertical, none if guide nor horizontal/vertical'
    vertical: Any
    'True if guide is vertical'

class fgGuides:
    """list of fgGuide objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

    def remove(self, p0: fgPoint, p1: fgPoint) -> Any:
        """remove(fgPoint p0, fgPoint p1) - remove item if it's points are equal to specified"""
        ...

    def removeHV(self, position: float, horizontal: bool) -> Any:
        """removeHV(float position, bool horizontal)"""
        ...

class fgHint:
    """Hint representation

Constructors:
  fgHint() - default
  fgHint(fgHint) - copy
  fgHint(name= , v= , dv= , point0= , point1= , p0= , p1= , points0= , points1= , horizontal= )

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHint.copy; argument details are not documented."""
        ...
    dv: Any
    '(float)'
    horizontal: Any
    '(bool)'
    index: Any
    "(int) index from owner's hints list"
    name: Any
    '(string) hint name'
    p0: Any
    '(float)'
    p1: Any
    '(float)'
    point0: Any
    '(string)'
    point1: Any
    '(string)'
    points0: Any
    '([int])'
    points1: Any
    '([int])'
    v: Any
    '(float)'

class fgHintCommand:
    """HintCommand representation

Constructors:
  fgHintCommand() - default
  fgHintCommand(fgHintCommand) - copy
  fgHintCommand(code, index) - parametric, possible values for code are 'none'/'hintH'/'hintV'/'replace'

Native bases: object

Supplemental documentation:
A hint command. The captured declaration exposes the attributes `code`, `index`, `pointName` and `subrIndex`. It is created as `fgHintCommand()`, as a copy `fgHintCommand(fgHintCommand)` or as `fgHintCommand(code, index)`, where the possible values for code are 'none'/'hintH'/'hintV'/'replace'.

Source: generated/fontgate.py: fgHintCommand captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    code: Any
    "('none'/'hintH'/'hintV'/'replace') code"
    index: Any
    '(int)'
    pointName: Any
    '(string)'
    subrIndex: Any
    '(int)'

class fgHintCommands:
    """list of fgHintCommand objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHintCommands.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHintCommands.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHintCommands.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHintCommands.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHintCommands.insert; argument details are not documented."""
        ...

class fgHints:
    """list of fgHint objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def getAsDict(self) -> Any:
        """dict(items) getAsDict()"""
        ...

    def getAsList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHints.getAsList; argument details are not documented."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

    def removeByName(self, *args: Any, **kwargs: Any) -> Any:
        """removeByName('name')"""
        ...

    def removeHV(self, v: float, dv: float, horizontal: bool) -> Any:
        """removeHV(float v, float dv, bool horizontal)"""
        ...

    def setFromDict(self, *args: Any, **kwargs: Any) -> Any:
        """setFromDict(dict(items))"""
        ...

    def setFromList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgHints.setFromList; argument details are not documented."""
        ...

class fgIntDict:
    """int dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgIntDict.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgIntDict.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgIntDict.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgIntDict.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgIntDict.value; argument details are not documented."""
        ...

class fgKerning:
    """Kerning representation

Constructors:
  fgKerning(fgDataOwnerData)

Native bases: object

Supplemental documentation:
The kerning table of a font. The captured declaration exposes `get` and `set` for a value addressed by a pair or by a tuple of two names, `has_key`, `keys`, `values`, `items`, `asDict`, `remove` and `clear`, and the group operations `addGroup`, `deleteGroup`, `deleteAllGroups`, `renameGroup` and `hasGroupKerning`. It also exposes `getPlainPairs`, `getPlainPairsDict`, `setPlainPairs`, `scale` and the `groups` attribute.

Source: generated/fontgate.py: fgKerning captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addGroup(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.addGroup; argument details are not documented."""
        ...

    def asDict(self) -> Any:
        """dict(fgKerningObjectPair : float) asDict()"""
        ...

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.clear; argument details are not documented."""
        ...

    def deleteAllGroups(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.deleteAllGroups; argument details are not documented."""
        ...

    def deleteGroup(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.deleteGroup; argument details are not documented."""
        ...

    def get(self, *args: Any, **kwargs: Any) -> Any:
        """float get(fgKerningObjectPair / tuple('name1', 'name2')) - get kerning value"""
        ...

    def getPlainPairs(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.getPlainPairs; argument details are not documented."""
        ...

    def getPlainPairsDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.getPlainPairsDict; argument details are not documented."""
        ...

    def hasGroupKerning(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.hasGroupKerning; argument details are not documented."""
        ...

    def has_key(self, arg0: fgKerningObjectPair) -> bool:
        """bool has_key(fgKerningObjectPair)"""
        ...

    def items(self) -> Any:
        """list( tuple(fgKerningObjectPair, float) ) items()"""
        ...

    def keys(self) -> Any:
        """list(fgKerningObjectPair) keys()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.remove; argument details are not documented."""
        ...

    def renameGroup(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.renameGroup; argument details are not documented."""
        ...

    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.scale; argument details are not documented."""
        ...

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """int set(fgKerningObjectPair / tuple('name1', 'name2'), double) - set kerning value"""
        ...

    def setPlainPairs(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgKerning.setPlainPairs; argument details are not documented."""
        ...

    def values(self) -> Any:
        """list( float ) values()"""
        ...
    groups: Any

class fgKerningGroups:
    """Dictionary of kerning groups

Constructors:
  fgKerningGroups(fgDataOwnerData) - default

Native bases: object

Supplemental documentation:
A dictionary of kerning groups. The captured declaration exposes `has_key`, `keys`, `values`, `items`, `asDict`, `clear`, `remove` and `rename`. Each item is a group name with a list of glyph names and a mode.

Source: generated/fontgate.py: fgKerningGroups captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def clear(self) -> Any:
        """clear() - delete all items"""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """bool has_key('groupName')"""
        ...

    def items(self) -> Any:
        """list( tuple('groupName', tuple( list('glyphName'), mode ) ) items()"""
        ...

    def keys(self) -> Any:
        """list('groupName') keys()"""
        ...

    def remove(self, deleteDependentKerningPairs: Any=...) -> Any:
        """remove('groupName'[, deleteDependentKerningPairs = false])"""
        ...

    def rename(self, *args: Any, **kwargs: Any) -> Any:
        """bool/Nothing rename('oldGroupName', 'newGroupName')"""
        ...

    def values(self) -> Any:
        """list ( tuple( list('glyphName'), mode ) ) values()"""
        ...

class fgKerningObject:
    """KerningObject representation

Constructors:  fgKerningObject() - default
  fgKerningObject(fgKerningObject) - copy
  fgKerningObject('name', mode) - mode must be one of 'glyphMode'/'groupMode'

Native bases: object

Supplemental documentation:
One side of a kerning pair: a glyph or a group. The captured declaration exposes `id` (the glyph or group name) and `mode` (glyphMode or groupMode), with `asDict` and `asTuple`. Consult the retained constructor documentation for the supported creation forms.

Source: generated/fontgate.py: fgKerningObject captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    id: Any
    '(string) glyph or group name'
    mode: Any
    "('glyphMode'/'groupMode')"

class fgKerningObjectPair:
    """KerningObjectPair representation

Constructors:  fgKerningObjectPair() - default
  fgKerningObjectPair(fgKerningObjectPair) - copy
  fgKerningObjectPair( tuple(fgKerningObject, fgKerningObject) )
  fgKerningObjectPair('nameLeft', 'nameRight')
  fgKerningObjectPair(fgKerningObject, fgKerningObject)
  fgKerningObjectPair('nameLeft', 'nameRight', modeLeft, modeRight) - modeLeft, modeRight must be one of 'glyphMode'/'groupMode'

Native bases: object

Supplemental documentation:
A kerning pair made of a `left` and a `right` kerning object, each a glyph or a group, with `asDict` and `asTuple`. Consult the retained constructor documentation for the supported creation forms, which take names, kerning objects or a tuple of two kerning objects.

Source: generated/fontgate.py: fgKerningObjectPair captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    left: Any
    '(fgKerningObject) - left glyph or group'
    right: Any
    '(fgKerningObject) - right glyph or group'

class fgLayer:
    """Layer representation

Constructors:
  fgLayer() - default
  fgLayer(fgLayer) - copy
  fgLayer('name') - create named layer

Math operation:
  fgLayer + fgLayer
  fgLayer - fgLayer

Native bases: object

Supplemental documentation:
A font-data layer exposing `name`, `anchors`, `guides` and `hints`. The captured declarations identify those collections as fgAnchors, fgGuides and fgHints. `countContours()` and `countShapes()` report contour and shape counts; `addContour()` adds an fgContour and returns an fgContour. Consult the member documentation for transformation and bounding-box arguments.

Source: generated/fontgate.py: fgLayer captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addContour(self, arg0: fgContour) -> fgContour:
        """fgContour addContour(fgContour) - add contour to layer"""
        ...

    def boundingBox(self, prepareExport: Any=...) -> Any:
        """fgRect/Nothing boundingBox(fgMatrix[, prepareExport = false])"""
        ...

    def checkContours(self) -> Any:
        """checkContours()"""
        ...

    def countContours(self) -> int:
        """int countContours()"""
        ...

    def countHints(self, horizontal: bool) -> int:
        """int countHints(bool horizontal)"""
        ...

    def countNodes(self) -> int:
        """int countNodes()"""
        ...

    def countPictures(self) -> int:
        """int countPictures()"""
        ...

    def countShapes(self) -> int:
        """int countShapes()"""
        ...

    def findHint(self, arg0: fgHint) -> int:
        """int findHint(fgHint)"""
        ...

    def findNode(self, *args: Any, **kwargs: Any) -> Any:
        """fgNode/Nothing findNode(nodeIndex / 'nodeName') - find name by index or name"""
        ...

    def hasColors(self) -> bool:
        """bool hasColors()"""
        ...

    def hasHints(self) -> bool:
        """bool hasHints()"""
        ...

    def hasPictures(self) -> bool:
        """bool hasPictures()"""
        ...

    def hints2links(self, *args: Any, **kwargs: Any) -> Any:
        """hints2links(double tolerance[, fgCuspPoints])"""
        ...

    def indexToName(self, nodeIndex: int) -> Any:
        """'nodeName' indexToName(int nodeIndex)"""
        ...

    def isCompatible(self, arg0: flLayer) -> Any:
        """bool/Nothing isCompatible(flLayer)"""
        ...

    def nameToIndex(self, *args: Any, **kwargs: Any) -> Any:
        """int nameToIndex('nodeName')"""
        ...

    def prepareNodeNames(self) -> Any:
        """prepareNodeNames()"""
        ...

    def removeHints(self, horizontal: bool) -> Any:
        """removeHints(bool horizontal)"""
        ...

    def transform(self, apply: Any=...) -> Any:
        """transform(const Matrix& mx[, apply = true])"""
        ...
    active: Any
    '(bool)'
    anchors: Any
    '(fgAnchors)'
    guides: Any
    '(fgGuides)'
    hints: Any
    '(fgHints)'
    hintsProgram: Any
    '(fgHintCommands)'
    locked: Any
    '(bool)'
    matrix: Any
    '(fgMatrix)'
    name: Any
    '(string)'
    opacity: Any
    '(float)'
    reference: Any
    '(fgPoint)'
    service: Any
    '(bool)'
    visible: Any
    '(bool)'
    wireframe: Any
    '(bool)'

class fgLayers:
    """list of fgLayer objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLayers.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLayers.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLayers.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLayers.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLayers.insert; argument details are not documented."""
        ...

class fgLib:
    """Dictionary with font- or glyph-related data

Native bases: object

Supplemental documentation:
A dictionary with font- or glyph-related data. The captured declaration exposes the methods `clear`, `get`, `hasKey`, `items`, `keys` and `update`.

Source: generated/fontgate.py: fgLib captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLib.clear; argument details are not documented."""
        ...

    def get(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLib.get; argument details are not documented."""
        ...

    def hasKey(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLib.hasKey; argument details are not documented."""
        ...

    def items(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLib.items; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLib.keys; argument details are not documented."""
        ...

    def update(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgLib.update; argument details are not documented."""
        ...

class fgMapBytes:
    """Raw data dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMapBytes.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMapBytes.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMapBytes.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMapBytes.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMapBytes.value; argument details are not documented."""
        ...

class fgMaster:
    """Anchor representation

Constructors:
  fgMaster() - default
  fgMaster(fgMaster) - copy
  fgMaster('name') - create with name='name'

Native bases: object

Supplemental documentation:
A master. The captured declaration exposes the attributes `name`, `penColor` and `position`. It is created as `fgMaster()`, as a copy `fgMaster(fgMaster)` or as `fgMaster('name')`.

Source: generated/fontgate.py: fgMaster captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    name: Any
    '(string) - name'
    penColor: Any
    '(int) - penColor'
    position: Any
    '(fgDesignPosition)'

class fgMasters:
    """list of fgMaster objects

Native bases: object

Supplemental documentation:
A list of fgMaster objects. The captured declaration exposes `append`, `asList`, `clean`, `del_` and `insert`. The native spelling of `del_` is del, which the capture says to reach through getattr on the native object.

Source: generated/fontgate.py: fgMasters captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgMatrix:
    """Transformation matrix representation

Constructors:
  fgMatrix() - default
  fgMatrix(fgMatrix) - copy
  fgMatrix(float m11, float m12, float m21, float m22, float dx, float dy)

Math operation:
  fgMatrix * fgMatrix
  

Native bases: object

Supplemental documentation:
A transformation matrix with the attributes `m11`, `m12`, `m21`, `m22`, `dx` and `dy`. The captured declaration exposes `asDict`, `asTuple`, `assign`, `determinant`, `invert`, `inverted`, `invertible`, `noMove`, `noRotate`, `noScale`, `scale`, `slant` and `standard`. It is created as `fgMatrix()`, as a copy `fgMatrix(fgMatrix)` or as `fgMatrix(m11, m12, m21, m22, dx, dy)`; two matrices combine with `fgMatrix * fgMatrix`.

Source: generated/fontgate.py: fgMatrix captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def assign(self, m11: Any, m12: Any, m21: Any, m22: Any, dx: Any, dy: Any) -> Any:
        """assign(fgMatrix) or assign(m11, m12, m21, m22, dx, dy)"""
        ...

    def determinant(self) -> float:
        """float determinant()"""
        ...

    def invert(self) -> bool:
        """bool invert()"""
        ...

    def inverted(self) -> fgMatrix:
        """fgMatrix inverted()"""
        ...

    def invertible(self) -> bool:
        """bool invertible()"""
        ...

    def noMove(self) -> bool:
        """bool noMove()"""
        ...

    def noRotate(self) -> bool:
        """bool noRotate()"""
        ...

    def noScale(self) -> bool:
        """bool noScale()"""
        ...

    def scale(self, s: float) -> Any:
        """scale(float s)"""
        ...

    def slant(self) -> Any:
        """slant(float angle) or float slant()"""
        ...

    def standard(self) -> bool:
        """bool standard()"""
        ...
    dx: Any
    dy: Any
    m11: Any
    m12: Any
    m21: Any
    m22: Any

class fgMaxP:
    """fgMaxP representation

Native bases: object

Supplemental documentation:
The maxp table values. The captured declaration exposes the attributes `maxFunctionDefs`, `maxInstructionDefs`, `maxStackElements`, `maxStorage`, `maxTwilightPoints` and `maxZones`, and the methods `asDict` and `asTuple`.

Source: generated/fontgate.py: fgMaxP captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    maxFunctionDefs: Any
    maxInstructionDefs: Any
    maxStackElements: Any
    maxStorage: Any
    maxTwilightPoints: Any
    maxZones: Any

class fgMetricsClass:
    """MetricsClass representation

Constructors:
  fgMetricsClass() - default
  fgMetricsClass(fgMetricsClass) - copy

Native bases: object

Supplemental documentation:
A metrics class. The captured declaration exposes the attributes `glyphs`, `keyGlyphName`, `left`, `name`, `right` and `width`, and the method `hasGlyph`. It is created as `fgMetricsClass()` or as a copy `fgMetricsClass(fgMetricsClass)`.

Source: generated/fontgate.py: fgMetricsClass captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def hasGlyph(self, *args: Any, **kwargs: Any) -> Any:
        """bool hasGlyph(int glyphID/'glyphName')"""
        ...

    def keyGlyphName(self) -> Any:
        """'keyGlyphName' keyGlyphName()"""
        ...
    glyphs: Any
    '(fgGlyphIDsSet)'
    left: Any
    '(bool)'
    name: Any
    '(string)'
    right: Any
    '(bool)'
    width: Any
    '(bool)'

class fgMetricsClasses:
    """list of fgMetricsClass objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMetricsClasses.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMetricsClasses.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMetricsClasses.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMetricsClasses.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgMetricsClasses.insert; argument details are not documented."""
        ...

class fgNametable:
    """NameTable - unicode->name translation and vice versa

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def easyCompare(self, *args: Any, **kwargs: Any) -> Any:
        """bool easyCompare('name0', 'name1')"""
        ...

    def getAlternativeNames(self, *args: Any, **kwargs: Any) -> Any:
        """list( 'altGlyphName' ) getAlternativeNames('glyphName')"""
        ...

    def load(self, path_to_file: Any) -> bool:
        """bool load(string path_to_file)"""
        ...

    def name(self, unicode: int) -> Any:
        """'glyphName' name(int unicode)"""
        ...

    def unc(self, *args: Any, **kwargs: Any) -> Any:
        """int unc('glyphName')"""
        ...
    loaded: Any
    '(bool)'

class fgNode:
    """Node representation

Constructors:
  fgNode() - default
  fgNode(fgNode) - copy
  fgNode('Move'/'On'/'Off'/'Curve', fgPoint[, smooth=false])
  fgNode('Move'/'On'/'Off'/'Curve', fgPoint, 'name'[, smooth=false])

Math operation:
  fgNode + fgNode
  fgNode - fgNode
  fgNode * float

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def isCurve(self) -> bool:
        """bool isCurve()"""
        ...

    def isCurveOff(self) -> bool:
        """bool isCurveOff()"""
        ...

    def isG2(self) -> bool:
        """bool isG2()"""
        ...

    def isInterpolatedX(self) -> bool:
        """bool isInterpolatedX()"""
        ...

    def isInterpolatedY(self) -> bool:
        """bool isInterpolatedY()"""
        ...

    def isOff(self) -> bool:
        """bool isOff()"""
        ...

    def isOn(self) -> bool:
        """bool isOn()"""
        ...

    def isSelected(self) -> bool:
        """bool isSelected()"""
        ...

    def setG2(self, *args: Any, **kwargs: Any) -> Any:
        """setG2([true])"""
        ...

    def setInterpolatedX(self, *args: Any, **kwargs: Any) -> Any:
        """setInterpolatedX([true])"""
        ...

    def setInterpolatedY(self, *args: Any, **kwargs: Any) -> Any:
        """setInterpolatedY([true])"""
        ...

    def setSelected(self, *args: Any, **kwargs: Any) -> Any:
        """setSelected([true])"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix)"""
        ...
    flags: Any
    '(int)'
    kind: Any
    "('Move'/'On'/'Off'/'Curve')"
    name: Any
    '(string)'
    point: Any
    '(fgPoint)'
    smooth: Any
    '(bool)'

class fgNodes:
    """list of fgNode objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgNodes.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgNodes.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgNodes.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgNodes.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgNodes.insert; argument details are not documented."""
        ...

class fgOTLayout:
    """OpenType Layout representation

Constructors:
  fgOTLayout(fgDataOwnerData)
  fgOTLayout(fgFont)

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def clear(self) -> Any:
        """clear() - remove all features"""
        ...

    def get_feature(self, tag: Any) -> Any:
        """string get_feature(string / numeric tag) - get feature text"""
        ...

    def get_prefix(self) -> Any:
        """string get_prefix() - get common part of fea data"""
        ...

    def has_key(self, tag: Any) -> bool:
        """bool has_key(string / numeric tag) - True if feature is present"""
        ...

    def keys(self) -> Any:
        """list(string) keys() - list of feature tags"""
        ...

    def remove(self, tag: Any) -> Any:
        """remove(string / numeric tag) - remove feature"""
        ...

    def set_feature(self, tag: Any, new_content: Any) -> Any:
        """set_feature(string / numeric tag, string new_content) - set feature text"""
        ...

    def set_prefix(self, new_prefix: Any) -> Any:
        """set_prefix(string new_prefix) - set common part of fea data"""
        ...

class fgOpt_AutoMetrics:
    """fgOpt_AutoMetrics options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    close: Any
    left: Any
    right: Any

class fgOpt_EOTExport:
    """fgOpt_EOTExport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    doCompression: Any
    doXORCryptData: Any
    otExport: Any

class fgOpt_ExpandKerning:
    """fgOpt_ExpandKerning options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    applyToAssistance: Any
    codepage: Any
    count: Any
    keep: Any
    limitAction: Any
    limitCmap10: Any
    limitCodepage: Any
    limitCount: Any
    limitFontWindow: Any

class fgOpt_Font:
    """fgOpt_Font options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    autoMetrics: Any
    buildPclt: Any
    detectG2: Any
    detectInterpolation: Any
    expandKerning: Any
    fitAscender: Any
    fitDescender: Any
    optimize: Any
    otExport: Any
    placeDuplicate: Any
    placePaste: Any
    t1Autohint: Any
    t1Export: Any
    ttAutohint: Any

class fgOpt_KerningOptions:
    """fgOpt_KerningOptions options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    saveTheOnlySubtableInKernTable: Any
    useScriptInfoForOneSubtableCutting: Any

class fgOpt_OTExport:
    """fgOpt_OTExport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    CBDT: Any
    COLR: Any
    SVG: Any
    addCharacters: Any
    applyBBoxSavings: Any
    autoWinAscDesc: Any
    autohint: Any
    autohintGlyphs: Any
    autohintingMode: Any
    autotrace: Any
    cff: Any
    cff_adobe: Any
    cff_compress: Any
    cmap10: Any
    copyHDMXData: Any
    decompose: Any
    doAutohinting: Any
    doHintsCompile: Any
    exportCBDT: Any
    exportCOLR: Any
    exportSBIX: Any
    exportSVG: Any
    exportVOLT: Any
    feaFileOptions: Any
    featuresCompile: Any
    featuresRestore: Any
    fixDirection: Any
    fixNames: Any
    fontNames: Any
    generateLTSH: Any
    headBBoxSavings: Any
    kerningOptions: Any
    noReorder: Any
    roundCoordinates: Any
    sbix: Any
    silent_mode: Any
    subrize: Any
    t1autohint: Any
    ttfautohint: Any
    useTTFAutohint: Any
    writeBinaryHinting: Any
    writeBitmaps: Any
    writeDeviceMetrics: Any
    writeGDEF: Any
    writeHintedFont: Any
    writeKernFeature: Any
    writeKernTable: Any
    writeOriginalHinting: Any

class fgOpt_OTExportFeaFile:
    """fgOpt_OTExportFeaFile options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    doWriteGDEF: Any
    inlineLookups: Any
    verbose: Any
    write_body: Any
    write_classes: Any
    write_prefix: Any

class fgOpt_OTImport:
    """fgOpt_OTImport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    convertCurves: Any
    convertNames: Any
    curveConvertPrecision: Any
    featuresDecompile: Any
    featuresStore: Any
    ignoreGlyphs: Any
    namesGrouping: Any
    readKerningFromFeature: Any
    readKerningFromTable: Any
    readMacSpecificNaming: Any
    shortSplines: Any
    storeAAT: Any
    storeOriginalHinting: Any

class fgOpt_Optimize:
    """fgOpt_Optimize options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    align: Any
    reduce: Any

class fgOpt_T1Autohint:
    """fgOpt_T1Autohint options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    hHinting: Any
    hStems: Any
    maxHWidth: Any
    maxVWidth: Any
    minHLen: Any
    minHWidth: Any
    minVLen: Any
    minVWidth: Any
    ratioH: Any
    ratioV: Any
    useAdobeAutohinter: Any
    vHinting: Any
    vStems: Any
    zones: Any

class fgOpt_T1Export:
    """fgOpt_T1Export options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    AFM: Any
    ASCII: Any
    INF: Any
    PFM: Any
    autohint: Any
    cff: Any
    cid: Any
    decompose: Any
    downloadable: Any
    encoding: Any
    fixDirection: Any
    flex: Any
    fsType: Any
    roundCoordinates: Any
    scale1000: Any
    sort: Any
    swapNotice: Any
    unicode: Any
    useOS2: Any

class fgOpt_T1Import:
    """fgOpt_T1Import options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    decompose: Any
    familyGrouping: Any
    ignoreGlyphs: Any
    readMacSpecificNaming: Any
    singleMasterOnly: Any

class fgOpt_TTAutohint:
    """fgOpt_TTAutohint options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    allow3Stems: Any
    allowDeltas: Any
    hHinting: Any
    hintSidebearing: Any
    hintToCenter: Any
    interpolateCusps: Any
    interpolateDoubleLinks: Any
    treshold: Any
    vHinting: Any

class fgOpt_TTFAutohint:
    """fgOpt_TTFAutohint options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    TTFA_info: Any
    adjust_subglyphs: Any
    control_name: Any
    default_script: Any
    dehint: Any
    detailed_info: Any
    dw_cleartype_strong_stem_width: Any
    fallback_script: Any
    fallback_stem_width: Any
    family_suffix: Any
    gdi_cleartype_strong_stem_width: Any
    gray_strong_stem_width: Any
    hint_composites: Any
    hinting_limit: Any
    hinting_range_max: Any
    hinting_range_min: Any
    ignore_restrictions: Any
    increase_x_height: Any
    no_info: Any
    symbol: Any
    windows_compatibility: Any
    x_height_snapping_exceptions_string: Any

class fgOpt_UfoFontExport:
    """fgOpt_UfoFontExport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    base64: Any
    compress: Any
    formatVersion: Any
    writeLayoutTTX: Any

class fgOpt_UfoFontImport:
    """fgOpt_UfoFontImport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    compileFeatures: Any
    fixOrdering: Any
    readLayoutTTX: Any
    removeOverlap: Any

class fgOpt_VfbExport:
    """fgOpt_VfbExport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    saveEncoding: Any

class fgOpt_VfbImport:
    """fgOpt_VfbImport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    autoReplace: Any
    compileFeatures: Any
    fixOrdering: Any
    separateMasters: Any

class fgOpt_WOFFExport:
    """fgOpt_WOFFExport options page

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    otExport: Any

class fgOptions:
    """FontGate options

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    eotexport: Any
    font: Any
    otexport: Any
    otimport: Any
    t1export: Any
    t1import: Any
    ufoexport: Any
    ufoimport: Any
    vfbexport: Any
    vfbimport: Any
    woffexport: Any

class fgOtInfo:
    """OT Info representation

Constructors:
  fgOtInfo() - default
  fgOtInfo(fgOtInfo) - copy

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    glyphClass: Any
    "('Unspecified'/'Simple'/'Ligature'/'Mark'/'Component')"
    markClass: Any
    '(int)'
    otClasses: Any
    '( [ int ] )'

class fgOtValue:
    """OT Value representation

Constructors:
  fgOtValue() - default
  fgOtValue(fgOtValue) - copy
  fgOtValue(float) - by float value
  fgOtValue(int/long) - by int/long value

Math operation:
  fgOtValue + fgOtValue
  fgOtValue - fgOtValue
  fgOtValue * float

Native bases: object

Supplemental documentation:
An OpenType value. The captured declaration exposes the attributes `coordinate`, `deviceTable` and `point_index`. It is created as `fgOtValue()`, as a copy `fgOtValue(fgOtValue)`, from a float as `fgOtValue(float)` or from an int or long as `fgOtValue(int/long)`. The captured math operations are `fgOtValue + fgOtValue`, `fgOtValue - fgOtValue` and `fgOtValue * float`.

Source: generated/fontgate.py: fgOtValue captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    coordinate: Any
    '(float)'
    deviceTable: Any
    '(fgDeviceRecords)'
    point_index: Any
    '(int)'

class fgPackages:
    """Font packages representation

Constructors:
  fgPackages() - default
  fgPackages(fgPackages) - copy
  fgPackages('pathToFontFileOrFolder')

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def add(self, object: Any) -> Any:
        """add(fgFont or fgPackages object) - add font(s)"""
        ...

    def close(self) -> Any:
        """close() - remove all font(s) from list"""
        ...

    def copyFrom(self, arg0: fgPackages) -> Any:
        """copyFrom(fgPackages) - copy all fonts from another fgPackages object"""
        ...

    def create(self) -> Any:
        """create() - add empty font to list and return it's index"""
        ...

    def indexOf(self, arg0: fgFont) -> Any:
        """indexOf(fgFont) - return font index or (-1) if missing in list"""
        ...

    def open(self, path: Any) -> Any:
        """open(path) - open existing font(s) from 'path' location and return first index of created font(s)"""
        ...

    def remove(self, index: int) -> Any:
        """remove(int index) - remove font by index"""
        ...

class fgPen:
    """Pen representation

Constructors:
  fgPen(fgGlyph) - default
  fgPen(fgPen) - copy

Native bases: object

Supplemental documentation:
A pen with a bool `smooth` attribute. The captured declaration exposes `beginPath`, `closePath`, `curveTo`, `curveToOne`, `endPath`, `lineTo`, `moveTo` and `qCurveToOne`. It is created as `fgPen(fgGlyph)` or as a copy `fgPen(fgPen)`.

Source: generated/fontgate.py: fgPen captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def beginPath(self) -> Any:
        """beginPath()"""
        ...

    def closePath(self) -> Any:
        """closePath()"""
        ...

    def curveTo(self, *args: Any, **kwargs: Any) -> Any:
        """curveTo(fgPoint...)"""
        ...

    def curveToOne(self, arg0: fgPoint, arg1: fgPoint, arg2: fgPoint) -> Any:
        """curveToOne(fgPoint, fgPoint, fgPoint)"""
        ...

    def endPath(self) -> Any:
        """endPath()"""
        ...

    def lineTo(self, arg0: fgPoint) -> Any:
        """lineTo(fgPoint)"""
        ...

    def moveTo(self, arg0: fgPoint) -> Any:
        """moveTo(fgPoint)"""
        ...

    def qCurveToOne(self, arg0: fgPoint, arg1: fgPoint) -> Any:
        """qCurveToOne(fgPoint, fgPoint)"""
        ...
    smooth: Any
    '(bool)'

class fgPoint:
    """Point representation

Constructors:
  fgPoint() - default
  fgPoint(fgPoint) - copy
  fgPoint(float x)
  fgPoint(tuple(float x, float y))
  fgPoint(float x, float y)

Math Operations:
  fgPoint + fgPoint
  fgPoint - fgPoint
  fgPoint * fgPoint
  fgPoint * float - vector product
  fgPoint / float
  fgPoint << fgPoint - True if first point is less or equal to second
  fgPoint >> fgPoint - True if first point is greater or equal to second
  fgPoint ^ fgPoint - scalar product

Native bases: object

Supplemental documentation:
A two-dimensional point. The captured declaration exposes the coordinates `x` and `y` and the native vector operations. The captured fgPoint has no point type attribute. Read `x` and `y` or use `asTuple` to inspect coordinates.

Source: generated/fontgate.py: fgPoint captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def angleDiff(self, arg0: fgPoint) -> fgPoint:
        """fgPoint angleDiff(fgPoint)"""
        ...

    def angleSum(self, arg0: fgPoint) -> fgPoint:
        """fgPoint angleSum(fgPoint)"""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def assign(self, x: float, y: float) -> Any:
        """assign(fgPoint) or assign(float x, float y)"""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def close_to(self, d: Any=...) -> bool:
        """bool close_to(fgPoint[, d=0.00001])"""
        ...

    def collinear(self, arg0: fgPoint) -> bool:
        """bool collinear(fgPoint)"""
        ...

    def direction(self) -> fgPoint:
        """fgPoint direction()"""
        ...

    def dist(self, arg0: fgPoint) -> float:
        """float dist(fgPoint)"""
        ...

    def dist2(self, arg0: fgPoint) -> float:
        """float dist2(fgPoint)"""
        ...

    def distance(self, *args: Any, **kwargs: Any) -> Any:
        """float distance(fgPoint[, horizontal=false]"""
        ...

    def doubleScale(self, *args: Any, **kwargs: Any) -> Any:
        """scale(fgPoint) or scale(float sx, float sy)"""
        ...

    def flip(self) -> Any:
        """flip()"""
        ...

    def flipped(self) -> fgPoint:
        """fgPoint flipped()"""
        ...

    def ix(self) -> int:
        """int ix() - integer fast"""
        ...

    def iy(self) -> int:
        """int iy() - integer fast"""
        ...

    def len(self) -> float:
        """float len()"""
        ...

    def len2(self) -> float:
        """float len2()"""
        ...

    def normal(self) -> fgPoint:
        """fgPoint normal()"""
        ...

    def rotate(self, v: fgPoint, c: fgPoint) -> fgPoint:
        """fgPoint rotate(fgPoint v, fgPoint c)"""
        ...

    def round(self, *args: Any, **kwargs: Any) -> Any:
        """fgPoint round([doRound=true])"""
        ...

    def rx(self) -> int:
        """int rx() - integer rounded"""
        ...

    def ry(self) -> int:
        """int ry() - integer rounded"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix)"""
        ...

    def transformed(self, arg0: fgMatrix) -> fgPoint:
        """fgPoint transformed(fgMatrix)"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """float value([horizontal=true])"""
        ...

    def zero(self) -> bool:
        """bool zero()"""
        ...
    x: Any
    '(float)'
    y: Any
    '(float)'

class fgPointU:
    """PointU representation

Constructors:
  fgPointU() - default
  fgPointU(fgPoint) - copy
  fgPointU(fgPointU) - copy
  fgPointU(fgPoint, float u)
  fgPointU(tuple(float x, float y, float u))
  fgPointU(float x, float y, float u)

Math Operations:
  fgPointU + fgPoint/fgPointU
  fgPointU - fgPoint/fgPointU
  fgPointU * fgPoint/fgPointU
  fgPointU * float - vector product
  fgPointU / float
  fgPointU << fgPointU - True if first point is less or equal to second
  fgPointU >> fgPointU - True if first point is greater or equal to second
  fgPointU ^ fgPointU - scalar product

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def angleDiff(self, arg0: fgPoint) -> fgPoint:
        """fgPoint angleDiff(fgPoint)"""
        ...

    def angleSum(self, arg0: fgPoint) -> fgPoint:
        """fgPoint angleSum(fgPoint)"""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def assign(self, x: float, y: float, u: float) -> Any:
        """assign(fgPointU) or assign(float x, float y, float u)"""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def close_to(self, d: Any=...) -> bool:
        """bool close_to(fgPointU[, d=0.00001])"""
        ...

    def collinear(self, arg0: fgPoint) -> bool:
        """bool collinear(fgPoint)"""
        ...

    def direction(self) -> fgPoint:
        """fgPoint direction()"""
        ...

    def dist(self, arg0: fgPoint) -> float:
        """float dist(fgPoint)"""
        ...

    def dist2(self, arg0: fgPoint) -> float:
        """float dist2(fgPoint)"""
        ...

    def distance(self, *args: Any, **kwargs: Any) -> Any:
        """float distance(fgPoint[, horizontal=false]"""
        ...

    def doubleScale(self, *args: Any, **kwargs: Any) -> Any:
        """scale(fgPoint) or scale(float sx, float sy)"""
        ...

    def flip(self) -> Any:
        """flip()"""
        ...

    def flipped(self) -> fgPoint:
        """fgPoint flipped()"""
        ...

    def ix(self) -> int:
        """int ix() - integer fast"""
        ...

    def iy(self) -> int:
        """int iy() - integer fast"""
        ...

    def len(self) -> float:
        """float len()"""
        ...

    def len2(self) -> float:
        """float len2()"""
        ...

    def normal(self) -> fgPoint:
        """fgPoint normal()"""
        ...

    def rotate(self, v: fgPointU, c: fgPoint) -> fgPoint:
        """fgPoint rotate(fgPointU v, fgPoint c)"""
        ...

    def round(self, *args: Any, **kwargs: Any) -> Any:
        """fgPoint round([doRound=true])"""
        ...

    def rx(self) -> int:
        """int rx() - integer rounded"""
        ...

    def ry(self) -> int:
        """int ry() - integer rounded"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix)"""
        ...

    def transformed(self, arg0: fgMatrix) -> fgPoint:
        """fgPoint transformed(fgMatrix)"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """float value([horizontal=true])"""
        ...

    def zero(self) -> bool:
        """bool zero()"""
        ...
    u: Any
    '(float)'
    x: Any
    '(float)'
    y: Any
    '(float)'

class fgRect:
    """Rectangle representation

Constructors:
  fgRect() - default
  fgRect(fgRect) - copy
  fgRect(fgPoint, fgPoint)
  fgRect(fgPoint, fgPoint, bool empty)
  fgRect(float x1, float y1, float x2, float y2)

Math Operations:
  fgRect + fgPoint
  fgRect + fgRect
  fgRect + float
  fgRect - fgPoint
  fgRect - fgRect
  fgRect - float
  fgRect * float
  fgRect / float
  fgRect & fgRect
  fgRect | fgRect

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def adjust(self, x1: float, y1: float, x2: float, y2: float) -> Any:
        """adjust(float x1, float y1, float x2, float y2)"""
        ...

    def adjusted(self, x1: float, y1: float, x2: float, y2: float) -> fgRect:
        """fgRect adjusted(float x1, float y1, float x2, float y2)"""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent Py::Object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent Py::Object as tuple"""
        ...

    def assign(self, arg0: float, arg1: float, arg2: float, fix: Any=...) -> Any:
        """assign(fgPoint, fgPoint[, fix=true]) or assign(float, float, float, float[, fix=true])"""
        ...

    def bottom(self) -> float:
        """float bottom()"""
        ...

    def center(self) -> fgPoint:
        """fgPoint center()"""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def contains(self, *args: Any, **kwargs: Any) -> Any:
        """bool contains(fgPoint) or bool contains(fgRect)"""
        ...

    def containsX(self, arg0: float) -> bool:
        """bool containsX(float)"""
        ...

    def containsY(self, arg0: float) -> bool:
        """bool containsY(float)"""
        ...

    def diagonal(self) -> float:
        """float diagonal()"""
        ...

    def empty(self) -> Any:
        """empty()"""
        ...

    def fix(self) -> Any:
        """fix()"""
        ...

    def fix_x(self) -> Any:
        """fix_x()"""
        ...

    def fix_y(self) -> Any:
        """fix_y()"""
        ...

    def height(self) -> float:
        """float height()"""
        ...

    def intersects(self, arg0: fgRect) -> bool:
        """bool intersects(fgRect)"""
        ...

    def left(self) -> float:
        """float left()"""
        ...

    def move(self, dx: float, dy: float) -> Any:
        """move(float dx, float dy)"""
        ...

    def moved(self, dx: float, dy: float) -> fgRect:
        """fgRect moved(float dx, float dy)"""
        ...

    def right(self) -> float:
        """float right()"""
        ...

    def setBottom(self, arg0: float) -> Any:
        """setBottom(float)"""
        ...

    def setHeight(self, arg0: float) -> Any:
        """setHeight(float)"""
        ...

    def setLeft(self, arg0: float) -> Any:
        """setLeft(float)"""
        ...

    def setRect(self, x: int, y: int, w: int, h: int) -> Any:
        """setRect(int x, int y, int w, int h)"""
        ...

    def setRight(self, arg0: float) -> Any:
        """setRight(float)"""
        ...

    def setSize(self, arg0: fgPoint) -> Any:
        """setSize(fgPoint)"""
        ...

    def setTop(self, arg0: float) -> Any:
        """setTop(float)"""
        ...

    def setWidth(self, arg0: float) -> Any:
        """setWidth(float)"""
        ...

    def size(self) -> fgPoint:
        """fgPoint size()"""
        ...

    def top(self) -> float:
        """float top()"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix)"""
        ...

    def transformed(self, arg0: fgMatrix) -> fgRect:
        """fgRect transformed(fgMatrix)"""
        ...

    def width(self) -> float:
        """float width()"""
        ...

    def zero(self) -> Any:
        """zero()"""
        ...
    _empty: Any
    '(bool) True if Rect is empty'
    ll: Any
    '(fgPoint) lower left point'
    ur: Any
    '(fgPoint) upper right point'

class fgRendered:
    """fgRendered representation

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    bitmap: Any
    metrics: Any
    position: Any
    ppm: Any

class fgShape:
    """Shape representation

Constructors:
  fgShape() - default
  fgShape(fgShape) - copy
  fgShape(fgShape, fgShape, float tx, float ty)
  fgShape(fgShape, fgShape, float tx, float ty, int blend_mode)

Math Operations:
  fgShape + fgShape
  fgShape - fgShape
  fgShape * float

Native bases: object

Supplemental documentation:
A font-data shape whose `contours` attribute holds fgContours. `countContours()` and `countNodes()` report outline counts; `addContour()` adds an fgContour. `matrix` exposes an fgMatrix, while `name` and `opacity` describe the shape.

Source: generated/fontgate.py: fgShape captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addContour(self, arg0: fgContour) -> fgContour:
        """fgContour addContour(fgContour)"""
        ...

    def addShape(self, *args: Any, **kwargs: Any) -> Any:
        """int addShape(fgShape, int mode) ???"""
        ...

    def applyTransform(self) -> Any:
        """applyTransform()"""
        ...

    def area(self) -> float:
        """float area()"""
        ...

    def assignStyle(self, arg0: fgShape) -> Any:
        """assignStyle(fgShape)"""
        ...

    def autoInterpolated(self) -> bool:
        """bool autoInterpolated()"""
        ...

    def autoSmooth(self) -> bool:
        """bool autoSmooth()"""
        ...

    def boundingBox(self, prepareExport: Any=...) -> Any:
        """fgRect/Nothing boundingBox(fgMatrix[, bool prepareExport=false])"""
        ...

    def checkContours(self) -> Any:
        """checkContours()"""
        ...

    def containsOffPoint(self) -> bool:
        """bool containsOffPoint()"""
        ...

    def countContours(self) -> int:
        """int countContours()"""
        ...

    def countNodes(self) -> int:
        """int countNodes()"""
        ...

    def excludeShape(self, *args: Any, **kwargs: Any) -> Any:
        """int excludeShape(fgShape, int mode) ???"""
        ...

    def hasBody(self) -> bool:
        """bool hasBody()"""
        ...

    def hasContours(self) -> bool:
        """bool hasContours()"""
        ...

    def intersectShape(self, *args: Any, **kwargs: Any) -> Any:
        """int intersectShape(fgShape, int mode) ???"""
        ...

    def isCompatible(self, arg0: fgShape) -> Any:
        """bool/Nothing isCompatible(fgShape)"""
        ...

    def removeOverlap(self) -> int:
        """int removeOverlap()"""
        ...

    def reverse(self) -> Any:
        """reverse()"""
        ...

    def sortContours(self) -> Any:
        """sortContours()"""
        ...

    def subtractShape(self, *args: Any, **kwargs: Any) -> Any:
        """int subtractShape(fgShape, int mode) ???"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix)"""
        ...
    angle: Any
    '(float)'
    body: Any
    '(fgBrush)'
    calligraphic: Any
    '(bool)'
    cap_type: Any
    '(int)'
    contours: Any
    '(fgContours)'
    join_type: Any
    '(int)'
    matrix: Any
    '(fgMatrix)'
    name: Any
    '(string)'
    opacity: Any
    '(float)'
    pen: Any
    '(fgBrush)'
    picture: Any
    '(fgBitmap)'
    width: Any
    '(float)'

class fgShapes:
    """list of fgShape objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgShapes.append; argument details are not documented."""
        ...

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgShapes.asList; argument details are not documented."""
        ...

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgShapes.clean; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgShapes.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgShapes.insert; argument details are not documented."""
        ...

class fgStem:
    """Stem representation

Constructors:
  fgStem() - default
  fgStem(fgStem) - copy
  fgStem(float)

Native bases: object

Supplemental documentation:
A stem described by a string `name`, a float `value` and a `program` dict of int to int. The captured declaration exposes `clear`, `fillProgram`, `ppm` and `setProgram`. It is created as `fgStem()`, as a copy `fgStem(fgStem)` or as `fgStem(value)`.

Source: generated/fontgate.py: fgStem captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def fillProgram(self, upm: float) -> Any:
        """list(int) fillProgram(float upm)"""
        ...

    def ppm(self, upm: float, k: int) -> int:
        """int ppm(float upm, int k)"""
        ...

    def setProgram(self, k: int, ppm: int, keepValues: bool) -> Any:
        """setProgram(int k, int ppm, bool keepValues)"""
        ...
    name: Any
    '(string)'
    program: Any
    '( dict(int:int) )'
    value: Any
    '(float)'

class fgStems:
    """list of fgStem objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgStringDict:
    """string dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgStringDict.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgStringDict.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgStringDict.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgStringDict.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgStringDict.value; argument details are not documented."""
        ...

class fgTTInterpreter:
    """TTInterpreter representation

Constructors:
  fgTTInterpreter() - default
  fgTTInterpreter(fgTTInterpreter) - copy

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

class fgTrueTypeData:
    """TrueTypeData representation

Constructors:
  fgTrueTypeData() - default
  fgTrueTypeData(fgTrueTypeData) - copy

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def OK(self) -> bool:
        """bool OK() - return true if status is gdsOK"""
        ...

    def bad(self) -> bool:
        """bool bad() - return true if status isn't gdsOK"""
        ...

    def bottomSideBearing(self) -> int:
        """int bottomSideBearing()"""
        ...

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        """fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box"""
        ...

    def clearImports(self) -> Any:
        """clearImports() - clear instructions and hdmx, set yPels = 1"""
        ...

    def copy(self) -> fgTrueTypeData:
        """fgTrueTypeData copy() - create alone copy of data"""
        ...

    def countPictures(self) -> int:
        """int countPictures() - return pictures count"""
        ...

    def empty(self) -> bool:
        """bool empty() - return true if state == sEmpty or no endpoints present"""
        ...

    def getFontGateData(self) -> fgFontGateData:
        """fgFontGateData getFontGateData() - return Nothing"""
        ...

    def getType(self) -> Any:
        """string getType() - return 'dtTrueType'"""
        ...

    def hasBody(self, prepareExport: bool) -> bool:
        """bool hasBody(bool prepareExport) - return true if non-empty body layer is present"""
        ...

    def hasColors(self) -> bool:
        """bool hasColors() - return true if colors is present"""
        ...

    def hasHints(self) -> bool:
        """bool hasHints() - return true if hints is present"""
        ...

    def hasPictures(self) -> bool:
        """bool hasPictures() - return true if pictures is present"""
        ...

    def modified(self) -> bool:
        """bool modified() - return true if data was changed"""
        ...

    def rightSideBearing(self) -> int:
        """int rightSideBearing()"""
        ...

    def setParent(self, arg0: fgGlyph) -> Any:
        """setParent(fgGlyph) - set parent glyph"""
        ...

    def status(self) -> Any:
        """'gdsOK'/'gdsInvalid' status()"""
        ...

    def transform(self, arg0: fgMatrix) -> Any:
        """transform(fgMatrix) - transform data"""
        ...

    def updateBoundingBox(self) -> Any:
        """updateBoundingBox()"""
        ...

    def updated(self) -> Any:
        """updated() - mark data as changed, reset internal caches"""
        ...

    def valid(self) -> bool:
        """bool valid() - return true if state == sValid | sDecomposed"""
        ...

    def xExtent(self) -> int:
        """int xExtent()"""
        ...

    def yExtent(self) -> int:
        """int yExtent()"""
        ...
    advanceHeight: Any
    '(int)'
    advanceWidth: Any
    '(int)'
    endpoint: Any
    '([int])'
    hdmx: Any
    '(fgHdmx)'
    instructions: Any
    '(fgBuffer)'
    leftSideBearing: Any
    '(int)'
    points: Any
    '(fgTrueTypePoints)'
    pointsMap: Any
    "({ 'name': int value })"
    topSideBearing: Any
    '(int)'
    xMax: Any
    '(int)'
    xMin: Any
    '(int)'
    yMax: Any
    '(int)'
    yMin: Any
    '(int)'
    yPels: Any
    '(int)'

class fgTrueTypePoint:
    """TrueType Point representation

Constructors:
  fgTrueTypePoint() - default
  fgTrueTypePoint(fgTrueTypePoint) - copy
  fgTrueTypePoint(fgPoint)
  fgTrueTypePoint(bool on, int x, int y)

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def assign(self, x: int, y: int) -> Any:
        """assign(int x, int y)"""
        ...

    def onCurve(self, value: Any) -> bool:
        """bool onCurve() or onCurve(bool value)"""
        ...

    def repeat(self, value: Any) -> bool:
        """bool repeat()  or repeat(bool value)"""
        ...

    def touched(self, value: Any) -> bool:
        """bool touched() or touched(bool value)"""
        ...

    def xSame(self, value: Any) -> bool:
        """bool xSame()   or xSame(bool value)"""
        ...

    def xShort(self, value: Any) -> bool:
        """bool xShort()  or xShort(bool value)"""
        ...

    def ySame(self, value: Any) -> bool:
        """bool ySame()   or ySame(bool value)"""
        ...

    def yShort(self, value: Any) -> bool:
        """bool yShort()  or yShort(bool value)"""
        ...
    flag: Any
    '(int)'
    x: Any
    '(int)'
    y: Any
    '(int)'

class fgTrueTypePoints:
    """list of fgTrueTypePoint objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgValuesDict:
    """float values dictionary

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgValuesDict.asDict; argument details are not documented."""
        ...

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgValuesDict.del; argument details are not documented.

Native spelling: del; access it through getattr on the native object."""
        ...

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgValuesDict.has_key; argument details are not documented."""
        ...

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgValuesDict.keys; argument details are not documented."""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontgate.fgValuesDict.value; argument details are not documented."""
        ...

class fgVdmxRecord:
    """fgVdmxRecord representation

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    yMax: Any
    yMin: Any
    yPelHeight: Any

class fgVdmxRecords:
    """list of fgVdmxRecord objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgVector:
    """Vector representation

Constructors:
  fgVector() - default
  fgVector(fgVector) - copy
  fgVector(fgPoint q0[, fgPoint q1]) - from one or two points
  fgVector(fgPoint, float l, float a)

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def angle(self) -> float:
        """float angle()"""
        ...

    def angleTo(self, arg0: fgVector) -> float:
        """float angleTo(fgVector)"""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...

    def bbox(self) -> fgRect:
        """fgRect bbox()"""
        ...

    def center(self) -> fgPoint:
        """fgPoint center()"""
        ...

    def delta(self) -> fgPoint:
        """fgPoint delta()"""
        ...

    def direction(self) -> fgPoint:
        """fgPoint direction()"""
        ...

    def equivalent(self, arg0: fgVector) -> bool:
        """bool equivalent(fgVector)"""
        ...

    def intersect(self, *args: Any, **kwargs: Any) -> Any:
        """fgPoint/None intersect(fgVector) or (fgPoint, t)/None intersect(fgVector, bool get_t)"""
        ...

    def intersectY(self, pos: float) -> Any:
        """float/None intersectY(float pos)"""
        ...

    def len(self) -> float:
        """float len() - distance between q0 and q1"""
        ...

    def parallel(self, arg0: fgVector) -> bool:
        """bool parallel(fgVector)"""
        ...

    def point(self, time: float) -> fgPoint:
        """fgPoint point(float time)"""
        ...

    def time(self, arg0: fgPoint) -> float:
        """float time(fgPoint)"""
        ...
    q0: Any
    '(fgPoint)'
    q1: Any
    '(fgPoint)'

class fgVectorBool:
    """[char] vector

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgVectorChar:
    """[char] vector

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgVectorDouble:
    """[double] vector

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgVectorInt:
    """[int] vector

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgVectorPoint:
    """[fgPoint] vector

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgVectorUInt16:
    """[uint16_t] vector

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgVectorUInt32:
    """[uint32t] vector

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class fgZone:
    """Zone representation

Constructors:
  fgZone() - default
  fgZone(fgZone) - copy

Native bases: object

Supplemental documentation:
A zone described by a string `name`, float `position` and `width`, a bool `top` and a `program` dict of int to int. The captured declaration exposes `clear`, `getIntValues`, `v0` and `v1`. It is created as `fgZone()` or as a copy `fgZone(fgZone)`.

Source: generated/fontgate.py: fgZone captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def getIntValues(self) -> Any:
        """tuple( int y0, int y1 ) getIntValues()"""
        ...

    def v0(self) -> float:
        """float v0()"""
        ...

    def v1(self) -> float:
        """float v1()"""
        ...
    name: Any
    '(string)'
    position: Any
    '(float)'
    program: Any
    '( dict(int:int) )'
    top: Any
    '(bool)'
    width: Any
    '(float)'

class fgZones:
    """list of fgZone objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append(item) or append( list(item) ) - add items to the end of the list"""
        ...

    def asList(self) -> Any:
        """list(items) asList() - get items as list"""
        ...

    def clean(self) -> Any:
        """clean() - delete all items"""
        ...

    def del_(self, index: Any) -> Any:
        """del(index) - delete item by index

Native spelling: del; access it through getattr on the native object."""
        ...

    def insert(self, position: Any, item: Any) -> Any:
        """insert(position, item) - insert item into list at specified position"""
        ...

class pyfgDataOwnerData:
    """pyfgDataOwnerData objects

Native bases: object"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
fgCURVE: int
fgLINE: int
fgMOVE: int
fgOFFCURVE: int
options: fgOptions
__all__ = ['fgAnchor', 'fgAnchors', 'fgAxes', 'fgAxis', 'fgBitmap', 'fgBitmaps', 'fgBitmapsData', 'fgBrush', 'fgCMaps', 'fgCURVE', 'fgCaret', 'fgCarets', 'fgCmapRecord', 'fgCoding', 'fgColor', 'fgComponent', 'fgComponents', 'fgContour', 'fgContours', 'fgCurve', 'fgCuspPoint', 'fgCuspPoints', 'fgDesignPosition', 'fgDeviceRecord', 'fgDeviceRecords', 'fgExtMapIntTofgShape', 'fgExtMapUCharToUChar', 'fgExtMapUIntToString', 'fgExtMapUShortToShort', 'fgFlagsDict', 'fgFont', 'fgFontGateData', 'fgFontHinting', 'fgFontInfo', 'fgFontInfoDict', 'fgGaspRecord', 'fgGaspRecords', 'fgGlyph', 'fgGlyphData', 'fgGlyphDict', 'fgGlyphIDsSet', 'fgGlyphs', 'fgGlyphsR', 'fgGroup', 'fgGroups', 'fgGuide', 'fgGuides', 'fgHint', 'fgHintCommand', 'fgHintCommands', 'fgHints', 'fgIntDict', 'fgKerning', 'fgKerningGroups', 'fgKerningObject', 'fgKerningObjectPair', 'fgLINE', 'fgLayer', 'fgLayers', 'fgLib', 'fgMOVE', 'fgMapBytes', 'fgMaster', 'fgMasters', 'fgMatrix', 'fgMaxP', 'fgMetricsClass', 'fgMetricsClasses', 'fgNametable', 'fgNode', 'fgNodes', 'fgOFFCURVE', 'fgOTLayout', 'fgOpt_AutoMetrics', 'fgOpt_EOTExport', 'fgOpt_ExpandKerning', 'fgOpt_Font', 'fgOpt_KerningOptions', 'fgOpt_OTExport', 'fgOpt_OTExportFeaFile', 'fgOpt_OTImport', 'fgOpt_Optimize', 'fgOpt_T1Autohint', 'fgOpt_T1Export', 'fgOpt_T1Import', 'fgOpt_TTAutohint', 'fgOpt_TTFAutohint', 'fgOpt_UfoFontExport', 'fgOpt_UfoFontImport', 'fgOpt_VfbExport', 'fgOpt_VfbImport', 'fgOpt_WOFFExport', 'fgOptions', 'fgOtInfo', 'fgOtValue', 'fgPackages', 'fgPen', 'fgPoint', 'fgPointU', 'fgRect', 'fgRendered', 'fgShape', 'fgShapes', 'fgStem', 'fgStems', 'fgStringDict', 'fgTTInterpreter', 'fgTrueTypeData', 'fgTrueTypePoint', 'fgTrueTypePoints', 'fgValuesDict', 'fgVdmxRecord', 'fgVdmxRecords', 'fgVector', 'fgVectorBool', 'fgVectorChar', 'fgVectorDouble', 'fgVectorInt', 'fgVectorPoint', 'fgVectorUInt16', 'fgVectorUInt32', 'fgZone', 'fgZones', 'options', 'pyfgDataOwnerData']
