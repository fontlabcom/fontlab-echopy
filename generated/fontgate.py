# this_file: generated/fontgate.py
# Generated from native API metadata; edit enrichment inputs, then merge.
'FontGate Python interface\n\nfgAnchor: Anchor representation\nfgAnchors: list of fgAnchor objects\nfgAxes: Axes list representation\nfgAxis: Axis representation\nfgCMaps: list of fgCmapRecord objects\nfgCaret: Caret representation\nfgCarets: list of fgCaret objects\nfgCmapRecord: fgCmapRecord representation\nfgCoding: Coding data representation\nfgComponent: Component representation\nfgComponents: list of fgComponent objects\nfgContour: Contour representation\nfgContours: list of fgContour objects\nfgCuspPoint: CuspPoint representation\nfgCuspPoints: list of fgCuspPoint objects\npyfgDataOwnerData: pyfgDataOwnerData objects\nfgDesignPosition: Anchor representation\nfgDeviceRecord: DeviceRecord representation\nfgDeviceRecords: list of fgDeviceRecord objects\nfgExtMapUIntToString: fgExtMapUIntToString dictionary\nfgFont: Font representation\nfgFontHinting: Font Hinting data representation\nfgFontInfo: FontInfo data\nfgFontInfoDict: Font info dictionaries\nfgGaspRecord: GaspRecord representation\nfgGaspRecords: list of fgGaspRecord objects\nfgGlyph: Glyph representation\nfgGlyphsR: fgGlyphsR representation\nfgGlyphDict: Glyph dictionaries\nfgGlyphIDsSet: GlyphIDs set\nfgGlyphs: list of fgGlyph objects\nfgGroup: Kerning/Metrics group\nfgGroups: Glyph groups list\nfgGuide: Guide representation\nfgGuides: list of fgGuide objects\nfgHint: Hint representation\nfgHintCommand: HintCommand representation\nfgHintCommands: list of fgHintCommand objects\nfgHints: list of fgHint objects\nfgKerning: Kerning representation\nfgKerningGroups: Dictionary of kerning groups\nfgKerningObject: KerningObject representation\nfgKerningObjectPair: KerningObjectPair representation\nfgLayer: Layer representation\nfgLayers: list of fgLayer objects\nfgLib: Dictionary with font- or glyph-related data\nfgMapBytes: Raw data dictionary\nfgExtMapIntTofgShape: fgExtMapIntTofgShape dictionary\nfgFlagsDict: bool flags diactionary\nfgValuesDict: float values dictionary\nfgIntDict: int dictionary\nfgStringDict: string dictionary\nfgMaster: Anchor representation\nfgMasters: list of fgMaster objects\nfgMaxP: fgMaxP representation\nfgMetricsClass: MetricsClass representation\nfgMetricsClasses: list of fgMetricsClass objects\nfgNametable: NameTable - unicode->name translation and vice versa\nfgNode: Node representation\nfgNodes: list of fgNode objects\nfgOTLayout: OpenType Layout representation\nfgOtInfo: OT Info representation\nfgOtValue: OT Value representation\nfgPackages: Font packages representation\nfgPen: Pen representation\nfgExtMapUShortToShort: fgExtMapUShortToShort dictionary\nfgShape: Shape representation\nfgShapes: list of fgShape objects\nfgStem: Stem representation\nfgStems: list of fgStem objects\nfgTrueTypePoint: TrueType Point representation\nfgTrueTypePoints: list of fgTrueTypePoint objects\nfgTTInterpreter: TTInterpreter representation\nfgVdmxRecord: fgVdmxRecord representation\nfgVdmxRecords: list of fgVdmxRecord objects\nfgVectorBool: [char] vector\nfgVectorChar: [char] vector\nfgVectorDouble: [double] vector\nfgVectorInt: [int] vector\nfgVectorUInt16: [uint16_t] vector\nfgVectorUInt32: [uint32t] vector\nfgVectorPoint: [fgPoint] vector\nfgZone: Zone representation\nfgZones: list of fgZone objects\nfgOptions: FontGate options\nfgOpt_T1Import: fgOpt_T1Import options page\nfgOpt_OTImport: fgOpt_OTImport options page\nfgOpt_UfoFontImport: fgOpt_UfoFontImport options page\nfgOpt_VfbImport: fgOpt_VfbImport options page\nfgOpt_VfbExport: fgOpt_VfbExport options page\nfgOpt_UfoFontExport: fgOpt_UfoFontExport options page\nfgOpt_OTExport: fgOpt_OTExport options page\nfgOpt_T1Export: fgOpt_T1Export options page\nfgOpt_EOTExport: fgOpt_EOTExport options page\nfgOpt_WOFFExport: fgOpt_WOFFExport options page\nfgOpt_Font: fgOpt_Font options page\nfgOpt_KerningOptions: fgOpt_KerningOptions options page\nfgOpt_OTExportFeaFile: fgOpt_OTExportFeaFile options page\nfgOpt_TTAutohint: fgOpt_TTAutohint options page\nfgOpt_T1Autohint: fgOpt_T1Autohint options page\nfgOpt_TTFAutohint: fgOpt_TTFAutohint options page\nfgOpt_AutoMetrics: fgOpt_AutoMetrics options page\nfgOpt_ExpandKerning: fgOpt_ExpandKerning options page\nfgOpt_Optimize: fgOpt_Optimize options page\nfgBitmap: Bitmap representation\nfgBitmaps: list of  fgBitmap objects\nfgBitmapsData: BitmapsData representation\nfgCapParams: fgCapParams representation\nfgBrush: Brush representation\nfgColor: Color representation\nfgCurve: Curve representation\nfgFontGateData: FontGateData representation\nfgGlyphData: GlyphData representation\nfgExtMapUCharToUChar: fgExtMapUCharToUChar dictionary\nfgMatrix: Transformation matrix representation\nfgPoint: Point representation\nfgPointU: PointU representation\nfgRect: Rectangle representation\nfgRendered: fgRendered representation\nfgTrueTypeData: TrueTypeData representation\nfgVector: Vector representation'
from __future__ import annotations
from typing import Any
import builtins as _echopy_builtins
from fontlab_echopy._runtime import bind as _bind, unavailable as _unavailable

class fgAnchor:
    "Anchor representation\n\nConstructors:\n  fgAnchor() - default\n  fgAnchor(fgAnchor) - copy\n  fgAnchor((x, y), 'name') - create with position=(x, y) and name='name'\n  fgAnchor(x, y, 'name') - create with position=(x, y) and name='name'\n\nNative bases: object\n\nCaptured native MRO: fgAnchor, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgAnchor.__init__')

    def copy(self, arg0: fgAnchor) -> Any:
        'copy(fgAnchor) - copy data from another fgAnchor object'
        _unavailable('fontgate.fgAnchor.copy')

    def draw(self, penObject: Any) -> Any:
        'draw(penObject) - draw the object with a segment pen'
        _unavailable('fontgate.fgAnchor.draw')

    def drawPoints(self, penObject: Any) -> Any:
        'drawPoints(penObject) - draw the object with a point pen'
        _unavailable('fontgate.fgAnchor.drawPoints')

    def move(self, dx: Any, dy: Any) -> Any:
        'move(dx, dy) - move anchor by (dx, dy)'
        _unavailable('fontgate.fgAnchor.move')

    def round(self) -> Any:
        'round() - round anchor coordinates'
        _unavailable('fontgate.fgAnchor.round')

    def scale(self, *args: Any, **kwargs: Any) -> Any:
        'scale((scale_x, scale_y)[, (center_x, center_y)]) - scale anchor by (scale_x, scale_y) with center=(center_x, center_y) or (0,0) if not defined'
        _unavailable('fontgate.fgAnchor.scale')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix) - transform anchor coordinates by matrix'
        _unavailable('fontgate.fgAnchor.transform')

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
    'list of fgAnchor objects\n\nNative bases: object\n\nCaptured native MRO: fgAnchors, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgAnchors.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgAnchors.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgAnchors.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgAnchors.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgAnchors.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgAnchors.insert')


class fgAxes:
    'Axes list representation\n\nConstructors:\n  fgAxes() - default\n  fgAxes(fgAxes) - copy\n\nNative bases: object\n\nCaptured native MRO: fgAxes, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgAxes.__init__')

    masters: Any
    '(fgMasters) - masters'

class fgAxis:
    "Axis representation\n\nConstructors:\n  fgAxis('name') - create with name='name'\n\nNative bases: object\n\nCaptured native MRO: fgAxis, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgAxis.__init__')

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
    'Bitmap representation\n\nConstructors:\n  fgBitmap() - default\n  fgBitmap(fgBitmap) - make orphan copy of another object\n  fgBitmap(width, height, bitsPerPixel)\n  fgBitmap(width, height, rowBytes, bitsPerPixel, bytesarray)\n\nNative bases: object\n\nCaptured native MRO: fgBitmap, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgBitmap.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgBitmap.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgBitmap.asTuple')

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        'clear all data'
        _unavailable('fontgate.fgBitmap.clear')

    def clone(self, source: fgBitmap) -> Any:
        'clone(fgBitmap source) - make clone of source bitmap'
        _unavailable('fontgate.fgBitmap.clone')

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        'copy(fgBitmap source[, x, y, w, h]) - copy whole source bitmap or part of it with size (w, h) from pos (x, y)'
        _unavailable('fontgate.fgBitmap.copy')

    def copyData(self, *args: Any, **kwargs: Any) -> Any:
        'copy(bytesarray) - assign new bitmap data'
        _unavailable('fontgate.fgBitmap.copyData')

    def create(self, *args: Any, **kwargs: Any) -> Any:
        "create(<same as constructor's arguments>') - allocate new bitmap data"
        _unavailable('fontgate.fgBitmap.create')

    def downsample(self, arg0: fgBitmap, oversampling: int) -> Any:
        'downsample(fgBitmap, int oversampling)'
        _unavailable('fontgate.fgBitmap.downsample')

    def empty(self) -> bool:
        'bool empty() - return true if no data assigned or bitmap size is 0'
        _unavailable('fontgate.fgBitmap.empty')

    def emptyRow(self, y: Any, x0: Any, x1: Any) -> Any:
        'emptyRow(y, x0, x1) - return true if part of row y from x0 till x1 has no non-zero pixels'
        _unavailable('fontgate.fgBitmap.emptyRow')

    def fill(self, color: fgColor) -> Any:
        'fill(fgColor color) - fill entire bitmap by color'
        _unavailable('fontgate.fgBitmap.fill')

    def flipV(self, *args: Any, **kwargs: Any) -> Any:
        'flip bitmap by vertical axis'
        _unavailable('fontgate.fgBitmap.flipV')

    def getPixel(self, x: Any, y: Any) -> fgColor:
        'fgColor getPixel(x, y) - get color of pixel (x, y)'
        _unavailable('fontgate.fgBitmap.getPixel')

    def row(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgBitmap.row; argument details are not documented.'
        _unavailable('fontgate.fgBitmap.row')

    def setPixel(self, x: Any, y: Any, color: fgColor) -> Any:
        'setPixel(x, y, fgColor color) - set color for pixel (x, y)'
        _unavailable('fontgate.fgBitmap.setPixel')

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
    'list of  fgBitmap objects\n\nNative bases: object\n\nCaptured native MRO: fgBitmaps, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgBitmaps.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgBitmaps.append; argument details are not documented.'
        _unavailable('fontgate.fgBitmaps.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgBitmaps.asList; argument details are not documented.'
        _unavailable('fontgate.fgBitmaps.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgBitmaps.clean; argument details are not documented.'
        _unavailable('fontgate.fgBitmaps.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgBitmaps.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgBitmaps.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgBitmaps.insert; argument details are not documented.'
        _unavailable('fontgate.fgBitmaps.insert')


class fgBitmapsData:
    'BitmapsData representation\n\nConstructors:\n  fgBitmapsData() - default\n  fgBitmapsData(fgBitmapsData) - copy\n\nNative bases: object\n\nCaptured native MRO: fgBitmapsData, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgBitmapsData.__init__')

    def OK(self) -> bool:
        'bool OK() - return true if status is gdsOK'
        _unavailable('fontgate.fgBitmapsData.OK')

    def bad(self) -> bool:
        "bool bad() - return true if status isn't gdsOK"
        _unavailable('fontgate.fgBitmapsData.bad')

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        'fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box'
        _unavailable('fontgate.fgBitmapsData.boundingBox')

    def copy(self) -> fgBitmapsData:
        'fgBitmapsData copy() - create alone copy of data'
        _unavailable('fontgate.fgBitmapsData.copy')

    def countPictures(self) -> int:
        'int countPictures() - return pictures count'
        _unavailable('fontgate.fgBitmapsData.countPictures')

    def getFontGateData(self, *args: Any, **kwargs: Any) -> Any:
        'getFontGateData() always return 0'
        _unavailable('fontgate.fgBitmapsData.getFontGateData')

    def getType(self) -> Any:
        "string getType() - return 'dtBitmaps'"
        _unavailable('fontgate.fgBitmapsData.getType')

    def hasBody(self, prepareExport: bool) -> bool:
        'bool hasBody(bool prepareExport) - return true if non-empty body layer is present'
        _unavailable('fontgate.fgBitmapsData.hasBody')

    def hasColors(self) -> bool:
        'bool hasColors() - return true if colors is present'
        _unavailable('fontgate.fgBitmapsData.hasColors')

    def hasHints(self) -> bool:
        'bool hasHints() - return true if hints is present'
        _unavailable('fontgate.fgBitmapsData.hasHints')

    def hasPictures(self) -> bool:
        'bool hasPictures() - return true if pictures is present'
        _unavailable('fontgate.fgBitmapsData.hasPictures')

    def modified(self) -> bool:
        'bool modified() - always return false'
        _unavailable('fontgate.fgBitmapsData.modified')

    def setParent(self, arg0: fgGlyph) -> Any:
        'setParent(fgGlyph) - set parent glyph'
        _unavailable('fontgate.fgBitmapsData.setParent')

    def status(self) -> Any:
        "'gdsOK'/'gdsInvalid' status()"
        _unavailable('fontgate.fgBitmapsData.status')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix) - transform data'
        _unavailable('fontgate.fgBitmapsData.transform')

    def updated(self) -> Any:
        'updated() - mark data as changed, reset internal caches'
        _unavailable('fontgate.fgBitmapsData.updated')

    bitmaps: Any
    '(fgBitmaps) - list of fgRendered objects'

class fgBrush:
    'Brush representation\n\nConstructors:\n  fgBrush() - default\n  fgBrush(fgBrush) - copy\n  fgBrush(fgColor) - solid brush with selected color and default size (1, 0)\n  fgBrush(fgColor, fgPoint) - solid brush with selected color and size\n\nNative bases: object\n\nCaptured native MRO: fgBrush, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgBrush.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgBrush.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgBrush.asTuple')

    @_echopy_builtins.staticmethod
    def black() -> fgBrush:
        'fgBrush black() - get black solid brush'
        _unavailable('fontgate.fgBrush.black')

    def isBlack(self) -> bool:
        'bool isBlack() - return true if brush is black'
        _unavailable('fontgate.fgBrush.isBlack')

    def isTransparent(self) -> bool:
        'bool isTransparent() - return true if brush is transparent'
        _unavailable('fontgate.fgBrush.isTransparent')

    @_echopy_builtins.staticmethod
    def transparent() -> fgBrush:
        'fgBrush transparent() - get transparent solid brush'
        _unavailable('fontgate.fgBrush.transparent')

    cap0: Any
    'fgCapParams start cap (copy; assign back after editing)'
    cap1: Any
    'fgCapParams end cap (copy; assign back after editing)'
    contrast: Any
    '(float) stroke contrast, 1.0 = none'
    join_type: Any
    '(int) 0 = bevel, 1 = round, 2 = miter'
    kind: Any
    "('Empty'/'Solid'/'Gradient') brush type "
    miter_limit: Any
    '(float) miter limit'
    proportion: Any
    '(float) nib proportion, 0..1 (0.5 = round/square nib)'
    remove_overlap: Any
    '(bool) remove overlap of the expanded stroke'
    rotation: Any
    '(float) nib rotation in degrees'
    solid: Any
    '(fgColor) brush color '
    thickness: Any
    '(float) stroke thickness'
    tolerance: Any
    '(float) stroke approximation tolerance'

class fgCMaps:
    'list of fgCmapRecord objects\n\nNative bases: object\n\nCaptured native MRO: fgCMaps, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCMaps.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCMaps.append; argument details are not documented.'
        _unavailable('fontgate.fgCMaps.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCMaps.asList; argument details are not documented.'
        _unavailable('fontgate.fgCMaps.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCMaps.clean; argument details are not documented.'
        _unavailable('fontgate.fgCMaps.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCMaps.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgCMaps.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCMaps.insert; argument details are not documented.'
        _unavailable('fontgate.fgCMaps.insert')


class fgCapParams:
    'fgCapParams representation\n\nNative bases: object\n\nCaptured native MRO: fgCapParams, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCapParams.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgCapParams.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgCapParams.asTuple')

    curvature: Any
    offset: Any
    rotation: Any
    shaping: Any
    type: Any

class fgCaret:
    "Caret representation\n\nConstructors:\nfgCaret() - default\nfgCaret(fgCaret) - copy\nfgCaret((fgOtValue/float/int, 'name')) - by coordinate and name\n\nNative bases: object\n\nCaptured native MRO: fgCaret, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCaret.__init__')

    name: Any
    '(string) name'
    v: Any
    '(fgOtValue) coordinate'

class fgCarets:
    'list of fgCaret objects\n\nNative bases: object\n\nCaptured native MRO: fgCarets, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCarets.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgCarets.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgCarets.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgCarets.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgCarets.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgCarets.insert')


class fgCmapRecord:
    'fgCmapRecord representation\n\nNative bases: object\n\nCaptured native MRO: fgCmapRecord, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCmapRecord.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgCmapRecord.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgCmapRecord.asTuple')

    eid: Any
    format: Any
    lid: Any
    nid: Any
    pagename: Any
    pid: Any
    type: Any

class fgCoding:
    "Coding data representation\n\nConstructors:\n  fgCoding() - default\n  fgCoding(fgCoding) - copy\n  fgCoding( bool [unicodeRange], bool [codepageRange], fgCMaps cmaps,\n         fgEncoding encoding, fgEncoding importedEncoding,\n         'encDefault'/'encStandard'/'encCustom')\n\nNative bases: object\n\nCaptured native MRO: fgCoding, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCoding.__init__')

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
    'Color representation\n\nConstructors:  fgColor() - default\n  fgColor(fgColor) - copy\n  fgColor(float hueValue) - by hue value  fgColor(r, g, b) - by r, g, b, float values from 0 to 1.0\n  fgColor(r, g, b, a) - by r, g, b, a float values from 0 to 1.0\n\nNative bases: object\n\nCaptured native MRO: fgColor, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgColor.__init__')

    def A(self) -> int:
        'int A() - get alpha value as int (0..255)'
        _unavailable('fontgate.fgColor.A')

    def B(self) -> int:
        'int B() - get blue value as int (0..255)'
        _unavailable('fontgate.fgColor.B')

    def G(self) -> int:
        'int G() - get green value as int (0..255)'
        _unavailable('fontgate.fgColor.G')

    def R(self, *args: Any, **kwargs: Any) -> Any:
        'int B() - get blue value as int (0..255)'
        _unavailable('fontgate.fgColor.R')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgColor.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgColor.asTuple')

    @_echopy_builtins.staticmethod
    def black() -> fgColor:
        'fgColor black() - get black color'
        _unavailable('fontgate.fgColor.black')

    @_echopy_builtins.staticmethod
    def fromInt(r: Any, g: Any, a: Any = ...) -> fgColor:
        'fgColor fromInt(r, g, b[, a=255]) - get color by int rgb(a) values (0..255)'
        _unavailable('fontgate.fgColor.fromInt')

    @_echopy_builtins.staticmethod
    def fromLab(l: Any, a: Any, b: Any) -> fgColor:
        'fgColor fromLab(l, a, b) - get color by float lab values'
        _unavailable('fontgate.fgColor.fromLab')

    def getCMYK(self, *args: Any, **kwargs: Any) -> Any:
        '(c, m, y, k, a) getCMYK([varK = 0.3]) - get color as CMYK+A components'
        _unavailable('fontgate.fgColor.getCMYK')

    def gray(self) -> float:
        'float gray() - get color as grayscale level'
        _unavailable('fontgate.fgColor.gray')

    def hue(self) -> float:
        'float hue() - get hue value'
        _unavailable('fontgate.fgColor.hue')

    def lab(self, *args: Any, **kwargs: Any) -> Any:
        '(l, a, b) lab() - get color as lab float values'
        _unavailable('fontgate.fgColor.lab')

    def lightness(self) -> float:
        'float lightness() - get lightness value'
        _unavailable('fontgate.fgColor.lightness')

    def saturation(self) -> float:
        'float saturation() - get saturation value'
        _unavailable('fontgate.fgColor.saturation')

    def set(self, *args: Any, **kwargs: Any) -> Any:
        'set((r, g, b[, a])) - set color by tuple with rgb or rgba float values'
        _unavailable('fontgate.fgColor.set')

    def setCMYK(self, *args: Any, **kwargs: Any) -> Any:
        'setCMYK(c, m, y, k[, _a = 1.0]) = set color by CMYK[A] float values'
        _unavailable('fontgate.fgColor.setCMYK')

    def setGray(self, *args: Any, **kwargs: Any) -> Any:
        'segGray(float v) - set rgb components to v'
        _unavailable('fontgate.fgColor.setGray')

    def setHue(self, s: Any = ...) -> Any:
        'setHue(h[, s=1.0[, l = 0.5]]) - set by hsl float values'
        _unavailable('fontgate.fgColor.setHue')

    @_echopy_builtins.staticmethod
    def transparent() -> fgColor:
        'fgColor transparent() - get transparent color'
        _unavailable('fontgate.fgColor.transparent')

    def xyz(self, *args: Any, **kwargs: Any) -> Any:
        '(x, y, z) xyz() - get color as xyz float values'
        _unavailable('fontgate.fgColor.xyz')

    a: Any
    '(float 0..1.0) - alpha channel'
    b: Any
    '(float 0..1.0) - blue channel'
    g: Any
    '(float 0..1.0) - green channel'
    r: Any
    '(float 0..1.0) - red channel'

class fgComponent:
    "Component representation\n\nConstructors:\n  fgComponent() - default\n  fgComponent(fgComponent) - copy\n  fgComponent('name', fgMatrix) - by 'name' and transformation matrix fgMatrix\n\nNative bases: object\n\nCaptured native MRO: fgComponent, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgComponent.__init__')

    def draw(self, object: Any) -> Any:
        'draw(pen object) - draw the object with a segment pen'
        _unavailable('fontgate.fgComponent.draw')

    def drawPoints(self, object: Any) -> Any:
        'drawPoints(pen object) - draw the object with a point pen'
        _unavailable('fontgate.fgComponent.drawPoints')

    def move(self, dx: Any, dy: Any) -> Any:
        'move(dx, dy) - move by float dx, dy value'
        _unavailable('fontgate.fgComponent.move')

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
    'list of fgComponent objects\n\nNative bases: object\n\nCaptured native MRO: fgComponents, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgComponents.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgComponents.append; argument details are not documented.'
        _unavailable('fontgate.fgComponents.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgComponents.asList; argument details are not documented.'
        _unavailable('fontgate.fgComponents.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgComponents.clean; argument details are not documented.'
        _unavailable('fontgate.fgComponents.clean')

    def decompose(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgComponents.decompose; argument details are not documented.'
        _unavailable('fontgate.fgComponents.decompose')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgComponents.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgComponents.del')

    def getAsList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgComponents.getAsList; argument details are not documented.'
        _unavailable('fontgate.fgComponents.getAsList')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgComponents.insert; argument details are not documented.'
        _unavailable('fontgate.fgComponents.insert')


class fgContour:
    'Contour representation\n\nConstructors:\n  fgContour() - default\n  fgContour(fgContour) - copy\n\nNative bases: object\n\nCaptured native MRO: fgContour, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgContour.__init__')

    def appendNode(self, arg0: fgNode) -> Any:
        'appendNode(fgNode) - add node to the end of the contour'
        _unavailable('fontgate.fgContour.appendNode')

    def area(self) -> float:
        'float area()'
        _unavailable('fontgate.fgContour.area')

    def autoClose(self) -> bool:
        'bool autoClose() - bool autoClose() - close contour, return true if changes was made'
        _unavailable('fontgate.fgContour.autoClose')

    def autoInterpolated(self) -> bool:
        'bool autoInterpolated() - interpolate contour nodes, return true if changes was made'
        _unavailable('fontgate.fgContour.autoInterpolated')

    def autoSmooth(self) -> bool:
        'bool autoSmooth() - smooth contour nodes, return true if changes was made'
        _unavailable('fontgate.fgContour.autoSmooth')

    def boundingBox(self, prepareExport: Any = ...) -> fgRect:
        'fgRect boundingBox(fgMatrix[, bool prepareExport = false])'
        _unavailable('fontgate.fgContour.boundingBox')

    def clear(self) -> Any:
        'clear() - clear all nodes'
        _unavailable('fontgate.fgContour.clear')

    def contains(self, winding: Any = ...) -> Any:
        'bool/Nothing contains(fgPoint[, bool winding = false])'
        _unavailable('fontgate.fgContour.contains')

    def containsCurvePoint(self) -> bool:
        'bool containsCurvePoint()'
        _unavailable('fontgate.fgContour.containsCurvePoint')

    def containsOffPoint(self) -> bool:
        'bool containsOffPoint()'
        _unavailable('fontgate.fgContour.containsOffPoint')

    def countNodes(self) -> int:
        'int countNodes() - get count of nodes'
        _unavailable('fontgate.fgContour.countNodes')

    def deleteNode(self, nodeIndex: int) -> bool:
        'bool deleteNode(int nodeIndex) - delete node'
        _unavailable('fontgate.fgContour.deleteNode')

    def draw(self, segmentPen: Any) -> Any:
        'draw(segmentPen) - draw the object with a segment pen'
        _unavailable('fontgate.fgContour.draw')

    def drawPoints(self, pointPen: Any) -> Any:
        'drawPoints(pointPen) - draw the object with a point pen'
        _unavailable('fontgate.fgContour.drawPoints')

    def empty(self) -> bool:
        "bool empty() - return True if contour haven't any node"
        _unavailable('fontgate.fgContour.empty')

    def filterOnPoints(self) -> Any:
        'filterOnPoints()'
        _unavailable('fontgate.fgContour.filterOnPoints')

    def getNode(self, nodeIndex: int) -> fgNode:
        'fgNode getNode(int nodeIndex) - get node by index'
        _unavailable('fontgate.fgContour.getNode')

    def getNodes(self) -> Any:
        '[ fgNode ] getNodes() - get list of fgNode objects'
        _unavailable('fontgate.fgContour.getNodes')

    def getUFONodesList(self, *args: Any, **kwargs: Any) -> Any:
        "[ ((x, y), 'nodetype', bool smooth, 'name') ] getUFONodesList() -get list of contour nodes as UFO-style tuples"
        _unavailable('fontgate.fgContour.getUFONodesList')

    def insertNode(self, arg0: fgNode, insertTo: int) -> Any:
        'insertNode(fgNode, int insertTo) - insert node into position insertTo'
        _unavailable('fontgate.fgContour.insertNode')

    def isCompatible(self, arg0: fgContour) -> bool:
        'bool isCompatible(fgContour)'
        _unavailable('fontgate.fgContour.isCompatible')

    def length(self) -> int:
        'int length() - get count of nodes'
        _unavailable('fontgate.fgContour.length')

    def midPoint(self) -> fgPoint:
        'fgPoint midPoint()'
        _unavailable('fontgate.fgContour.midPoint')

    def reverse(self) -> Any:
        'reverse() - reverse order of contour nodes'
        _unavailable('fontgate.fgContour.reverse')

    def toCurves(self, *args: Any, **kwargs: Any) -> Any:
        'toCurves([tolerance = 5.])'
        _unavailable('fontgate.fgContour.toCurves')

    def toShortSplines(self, *args: Any, **kwargs: Any) -> Any:
        'toShortSplines([tolerance = 5.[, bool short_splines = true]])'
        _unavailable('fontgate.fgContour.toShortSplines')

    def transform(self, arg0: fgMatrix) -> fgContour:
        'fgContour transform(fgMatrix)'
        _unavailable('fontgate.fgContour.transform')

    name: Any
    '(string) name of contour'
    nodes: Any
    '([fgNode]) contour nodes'
    open: Any
    '(bool) open flag'

class fgContours:
    'list of fgContour objects\n\nNative bases: object\n\nCaptured native MRO: fgContours, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgContours.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgContours.append; argument details are not documented.'
        _unavailable('fontgate.fgContours.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgContours.asList; argument details are not documented.'
        _unavailable('fontgate.fgContours.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgContours.clean; argument details are not documented.'
        _unavailable('fontgate.fgContours.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgContours.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgContours.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgContours.insert; argument details are not documented.'
        _unavailable('fontgate.fgContours.insert')


class fgCurve:
    'Curve representation\n\nConstructors:\n  fgCurve() - default\n  fgCurve(fgCurve) - copy\n  fgCurve( [4 x fgPoint] )\n  fgCurve( (q0, q1, q2, q3) )\n  fgCurve( fgPoint, fgPoint )\n  fgCurve( fgPoint, fgPoint, fgPoint )\n  fgCurve( fgPoint, fgPoint, fgPoint, fgPoint )\n  fgCurve( fgCurve, float t0, float t1 )\n\nNative bases: object\n\nCaptured native MRO: fgCurve, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCurve.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgCurve.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgCurve.asTuple')

    def bbox(self) -> fgRect:
        'fgRect bbox()'
        _unavailable('fontgate.fgCurve.bbox')

    def check(self, flatness: float, length: float, w0: float, w1: float) -> bool:
        'bool check(float flatness, float length, float w0, float w1)'
        _unavailable('fontgate.fgCurve.check')

    def coefficients(self, *args: Any, **kwargs: Any) -> Any:
        '(fgPoint a, fgPoint b, fgPoint c, fgPoint d) coefficients()'
        _unavailable('fontgate.fgCurve.coefficients')

    def curvature(self, t: float) -> float:
        'float curvature(float t)'
        _unavailable('fontgate.fgCurve.curvature')

    def d1(self, t: float) -> fgPoint:
        'fgPoint d1(float t)'
        _unavailable('fontgate.fgCurve.d1')

    def d2(self, t: float) -> fgPoint:
        'fgPoint d2(float t)'
        _unavailable('fontgate.fgCurve.d2')

    def direction(self, time: float) -> fgPoint:
        'fgPoint direction(float time)'
        _unavailable('fontgate.fgCurve.direction')

    def eseg(self, u: float) -> fgCurve:
        'fgCurve eseg(float u)'
        _unavailable('fontgate.fgCurve.eseg')

    def flat(self, parameter: float = ...) -> bool:
        'bool flat(double parameter = almost_zero)'
        _unavailable('fontgate.fgCurve.flat')

    def getExtrema(self, *args: Any, **kwargs: Any) -> Any:
        'int getExtrema(bool h, [float] )'
        _unavailable('fontgate.fgCurve.getExtrema')

    def getInflection(self, *args: Any, **kwargs: Any) -> Any:
        'int getInflection( [float] )'
        _unavailable('fontgate.fgCurve.getInflection')

    def hasExtrema(self) -> bool:
        'bool hasExtrema()'
        _unavailable('fontgate.fgCurve.hasExtrema')

    def isConvex(self, *args: Any, **kwargs: Any) -> Any:
        'bool isConvex( [float area] )'
        _unavailable('fontgate.fgCurve.isConvex')

    def len(self, quality: int) -> float:
        'float len(int quality)'
        _unavailable('fontgate.fgCurve.len')

    def maximumDeviation(self) -> float:
        'float maximumDeviation()'
        _unavailable('fontgate.fgCurve.maximumDeviation')

    def merge(self, c: fgCurve) -> bool:
        'bool merge(fgCurve c)'
        _unavailable('fontgate.fgCurve.merge')

    def point(self, time: float) -> fgPoint:
        'fgPoint point(float time)'
        _unavailable('fontgate.fgCurve.point')

    def quickLen(self) -> float:
        'float quickLen()'
        _unavailable('fontgate.fgCurve.quickLen')

    def render(self, *args: Any, **kwargs: Any) -> Any:
        'int render([fgPoint/fgPointU], int quality)'
        _unavailable('fontgate.fgCurve.render')

    def seg(self, stime: float, etime: float) -> fgCurve:
        'fgCurve seg(float stime, float etime)'
        _unavailable('fontgate.fgCurve.seg')

    def sseg(self, u: float) -> fgCurve:
        'fgCurve sseg(float u)'
        _unavailable('fontgate.fgCurve.sseg')

    def time(self, *args: Any, **kwargs: Any) -> Any:
        'float time(fgPoint[, int quality[, [float min_dist] ]])'
        _unavailable('fontgate.fgCurve.time')

    q0: Any
    '(fgPoint)'
    q1: Any
    '(fgPoint)'
    q2: Any
    '(fgPoint)'
    q3: Any
    '(fgPoint)'

class fgCuspPoint:
    'CuspPoint representation\n\nConstructors:\n  fgCuspPoint() - default\n  fgCuspPoint(fgCuspPoint) - copy\n\nNative bases: object\n\nCaptured native MRO: fgCuspPoint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCuspPoint.__init__')

    def middleH(self) -> bool:
        'bool middleH()'
        _unavailable('fontgate.fgCuspPoint.middleH')

    def middleV(self) -> bool:
        'bool middleV()'
        _unavailable('fontgate.fgCuspPoint.middleV')

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
    'list of fgCuspPoint objects\n\nNative bases: object\n\nCaptured native MRO: fgCuspPoints, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgCuspPoints.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCuspPoints.append; argument details are not documented.'
        _unavailable('fontgate.fgCuspPoints.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCuspPoints.asList; argument details are not documented.'
        _unavailable('fontgate.fgCuspPoints.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCuspPoints.clean; argument details are not documented.'
        _unavailable('fontgate.fgCuspPoints.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCuspPoints.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgCuspPoints.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgCuspPoints.insert; argument details are not documented.'
        _unavailable('fontgate.fgCuspPoints.insert')


class fgDesignPosition:
    'Anchor representation\n\nConstructors:\n  fgDesignPosition() - default\n  fgDesignPosition(fgDesignPosition) - copy\n  fgDesignPosition(axisCount) - parametric\n\nNative bases: object\n\nCaptured native MRO: fgDesignPosition, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgDesignPosition.__init__')

    data: Any
    '(list(double)) - data'

class fgDeviceRecord:
    'DeviceRecord representation\n\nConstructors:\n  fgDeviceRecord() - default\n  fgDeviceRecord(fgDeviceRecord) - copy\n  fgDeviceRecord(tuple( int ppm, int correction) )\n  fgDeviceRecord( int ppm, int correction )\n\nNative bases: object\n\nCaptured native MRO: fgDeviceRecord, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgDeviceRecord.__init__')

    correction: Any
    '(int)'
    ppm: Any
    '(int)'

class fgDeviceRecords:
    'list of fgDeviceRecord objects\n\nNative bases: object\n\nCaptured native MRO: fgDeviceRecords, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgDeviceRecords.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgDeviceRecords.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgDeviceRecords.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgDeviceRecords.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgDeviceRecords.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgDeviceRecords.insert')


class fgExtMapIntTofgShape:
    'fgExtMapIntTofgShape dictionary\n\nNative bases: object\n\nCaptured native MRO: fgExtMapIntTofgShape, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgExtMapIntTofgShape.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapIntTofgShape.asDict; argument details are not documented.'
        _unavailable('fontgate.fgExtMapIntTofgShape.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapIntTofgShape.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgExtMapIntTofgShape.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapIntTofgShape.has_key; argument details are not documented.'
        _unavailable('fontgate.fgExtMapIntTofgShape.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapIntTofgShape.keys; argument details are not documented.'
        _unavailable('fontgate.fgExtMapIntTofgShape.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapIntTofgShape.value; argument details are not documented.'
        _unavailable('fontgate.fgExtMapIntTofgShape.value')


class fgExtMapUCharToUChar:
    'fgExtMapUCharToUChar dictionary\n\nNative bases: object\n\nCaptured native MRO: fgExtMapUCharToUChar, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgExtMapUCharToUChar.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUCharToUChar.asDict; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUCharToUChar.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUCharToUChar.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgExtMapUCharToUChar.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUCharToUChar.has_key; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUCharToUChar.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUCharToUChar.keys; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUCharToUChar.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUCharToUChar.value; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUCharToUChar.value')


class fgExtMapUIntToString:
    'fgExtMapUIntToString dictionary\n\nNative bases: object\n\nCaptured native MRO: fgExtMapUIntToString, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgExtMapUIntToString.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUIntToString.asDict; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUIntToString.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUIntToString.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgExtMapUIntToString.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUIntToString.has_key; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUIntToString.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUIntToString.keys; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUIntToString.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUIntToString.value; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUIntToString.value')


class fgExtMapUShortToShort:
    'fgExtMapUShortToShort dictionary\n\nNative bases: object\n\nCaptured native MRO: fgExtMapUShortToShort, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgExtMapUShortToShort.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUShortToShort.asDict; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUShortToShort.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUShortToShort.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgExtMapUShortToShort.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUShortToShort.has_key; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUShortToShort.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUShortToShort.keys; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUShortToShort.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgExtMapUShortToShort.value; argument details are not documented.'
        _unavailable('fontgate.fgExtMapUShortToShort.value')


class fgFlagsDict:
    'bool flags diactionary\n\nNative bases: object\n\nCaptured native MRO: fgFlagsDict, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgFlagsDict.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgFlagsDict.asDict; argument details are not documented.'
        _unavailable('fontgate.fgFlagsDict.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgFlagsDict.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgFlagsDict.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgFlagsDict.has_key; argument details are not documented.'
        _unavailable('fontgate.fgFlagsDict.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgFlagsDict.keys; argument details are not documented.'
        _unavailable('fontgate.fgFlagsDict.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgFlagsDict.value; argument details are not documented.'
        _unavailable('fontgate.fgFlagsDict.value')


class fgFont:
    "Font representation\n\nConstructors:\n  fgFont() - create new empty font\n  fgFont('font_name') -  - create new empty font with name 'font_name'\n\nNative bases: object\n\nCaptured native MRO: fgFont, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgFont.__init__')

    def addGlyph(self, arg0: fgGlyph) -> fgGlyph:
        'fgGlyph addGlyph(fgGlyph)'
        _unavailable('fontgate.fgFont.addGlyph')

    def appendFeatures(self) -> int:
        'int appendFeatures()'
        _unavailable('fontgate.fgFont.appendFeatures')

    def averageHeight(self) -> float:
        'float averageHeight()'
        _unavailable('fontgate.fgFont.averageHeight')

    def averageWidth(self) -> float:
        'float averageWidth()'
        _unavailable('fontgate.fgFont.averageWidth')

    def boundingBox(self, arg0: fgMatrix) -> fgRect:
        'fgRect boundingBox(fgMatrix)'
        _unavailable('fontgate.fgFont.boundingBox')

    def calculateSafeZones(self, *args: Any, **kwargs: Any) -> Any:
        '?'
        _unavailable('fontgate.fgFont.calculateSafeZones')

    def checkMaps(self) -> Any:
        'checkMaps()'
        _unavailable('fontgate.fgFont.checkMaps')

    def clearGlyphs(self) -> Any:
        'clearGlyphs() - remove all glyphs'
        _unavailable('fontgate.fgFont.clearGlyphs')

    def clearMaps(self) -> Any:
        'clearMaps() - force clear all font internal caches'
        _unavailable('fontgate.fgFont.clearMaps')

    def copyFrom(self, sourceFont: fgFont) -> Any:
        'copyFrom(fgFont sourceFont) - copy all data and glyphs from source font'
        _unavailable('fontgate.fgFont.copyFrom')

    def createGlyph(self, clearExisting: Any = ...) -> fgGlyph:
        "fgGlyph createGlyph('name'[, int unicode[, bool clearExisting = false]])"
        _unavailable('fontgate.fgFont.createGlyph')

    def dropHintingTables(self) -> Any:
        'dropHintingTables()'
        _unavailable('fontgate.fgFont.dropHintingTables')

    def dropLayoutTables(self) -> Any:
        'dropLayoutTables()'
        _unavailable('fontgate.fgFont.dropLayoutTables')

    def fixOrdering(self, sortMethod: Any = ...) -> bool:
        "bool fixOrdering(float upm[, sortMethod='sortUnicode']) - sort glyphs by selected method. Methods are 'sortNone', 'sortName', 'sortUnicode', 'sortIndex', 'sortIndexReverse'"
        _unavailable('fontgate.fgFont.fixOrdering')

    def hasColors(self) -> bool:
        'bool hasColors()'
        _unavailable('fontgate.fgFont.hasColors')

    def hasPictures(self) -> bool:
        'bool hasPictures()'
        _unavailable('fontgate.fgFont.hasPictures')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        "bool has_key('name') - return true if font contains glyph with name 'name'"
        _unavailable('fontgate.fgFont.has_key')

    def items(self) -> Any:
        "[('name', fgGlyph)] items() - returns a list of font's ('name', fgGlyph) tuple pairs"
        _unavailable('fontgate.fgFont.items')

    def keys(self) -> Any:
        "['names'] keys() - return list of names of all glyphs in the font"
        _unavailable('fontgate.fgFont.keys')

    def killUnicode(self, unicode: Any) -> Any:
        'killUnicode(unicode) - remove selected unicode from all glyph unicodes lists'
        _unavailable('fontgate.fgFont.killUnicode')

    def rebuildMaps(self) -> Any:
        'rebuildMaps() - force clear and rebuild all font internal caches'
        _unavailable('fontgate.fgFont.rebuildMaps')

    def removeGlyph(self, *args: Any, **kwargs: Any) -> Any:
        "bool/Nothing removeGlyph('name'/unicode) - remove glyph selected by 'name' or unicode (int)"
        _unavailable('fontgate.fgFont.removeGlyph')

    def save(self, save_vfb: Any = ...) -> Any:
        "save('path/filename'[, bool save_vfb=false]) - save font in UFO or VFB format"
        _unavailable('fontgate.fgFont.save')

    def scale(self, arg0: float) -> Any:
        'scale(float) - scale font UPM'
        _unavailable('fontgate.fgFont.scale')

    def sortGlyphs(self, sortMethod: Any) -> Any:
        "sortGlyphs(sortMethod) - sort glyphs. sortMethod: 'sortNone'/'sortName'/'sortUnicode'/'sortIndex'/'sortIndexReverse'"
        _unavailable('fontgate.fgFont.sortGlyphs')

    def update(self) -> Any:
        'update() - force rebuild font chaches and request font update'
        _unavailable('fontgate.fgFont.update')

    def values(self) -> Any:
        "[fgGlyph] values() - returns list of font's fgGlyph"
        _unavailable('fontgate.fgFont.values')

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
    'FontGateData representation\n\nConstructors:\n  fgFontGateData() - default\n  fgFontGateData(fgFontGateData) - copy\n\nNative bases: object\n\nCaptured native MRO: fgFontGateData, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgFontGateData.__init__')

    def OK(self) -> bool:
        'bool OK() - return true if status is gdsOK'
        _unavailable('fontgate.fgFontGateData.OK')

    def activeLayer(self) -> fgLayer:
        'fgLayer activeLayer() - get active layer or Nothing if no layers exists'
        _unavailable('fontgate.fgFontGateData.activeLayer')

    def addContour(self, arg0: fgContour) -> fgContour:
        "fgContour addContour(fgContour) - add contour into 'Body' layer"
        _unavailable('fontgate.fgFontGateData.addContour')

    def addShape(self, arg0: fgShape) -> fgShape:
        "fgShape addShape(fgShape) - add shape into 'Body' layer"
        _unavailable('fontgate.fgFontGateData.addShape')

    def bad(self) -> bool:
        "bool bad() - return true if status isn't gdsOK"
        _unavailable('fontgate.fgFontGateData.bad')

    def bodyLayer(self) -> fgLayer:
        "fgLayer bodyLayer() - get layer named 'Body', any existing non-service layer if not found or Nothing if no layers exists"
        _unavailable('fontgate.fgFontGateData.bodyLayer')

    def bodyLayerStrict(self) -> fgLayer:
        "fgLayer bodyLayerStrict() - get layer named 'Body'. if it's not present, create it on the fly"
        _unavailable('fontgate.fgFontGateData.bodyLayerStrict')

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        'fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box'
        _unavailable('fontgate.fgFontGateData.boundingBox')

    def checkContours(self) -> Any:
        "checkContours() - ckeck for multi-segment contours and split it into one segment's contours"
        _unavailable('fontgate.fgFontGateData.checkContours')

    def copy(self) -> fgFontGateData:
        'fgFontGateData copy() - create alone copy of data'
        _unavailable('fontgate.fgFontGateData.copy')

    def countNodesContours(self, *args: Any, **kwargs: Any) -> Any:
        "(nodesCount, contoursCount) countNodesContours() - calculate stats for 'Body' layer if it present, return (0,0) otherwise"
        _unavailable('fontgate.fgFontGateData.countNodesContours')

    def countPictures(self) -> int:
        'int countPictures() - return pictures count'
        _unavailable('fontgate.fgFontGateData.countPictures')

    def countShapes(self) -> int:
        'int countShapes() - return shapes count'
        _unavailable('fontgate.fgFontGateData.countShapes')

    def findLayer(self, *args: Any, **kwargs: Any) -> Any:
        "fgLayer findLayer('name') - get layer by name, return Nothing if no layer found"
        _unavailable('fontgate.fgFontGateData.findLayer')

    def getFontGateData(self) -> fgFontGateData:
        'fgFontGateData getFontGateData() - return self'
        _unavailable('fontgate.fgFontGateData.getFontGateData')

    def getType(self) -> Any:
        "string getType() - return 'dtFontGate'"
        _unavailable('fontgate.fgFontGateData.getType')

    def hasBody(self, prepareExport: bool) -> bool:
        'bool hasBody(bool prepareExport) - return true if non-empty body layer is present'
        _unavailable('fontgate.fgFontGateData.hasBody')

    def hasColors(self) -> bool:
        'bool hasColors() - return true if colors is present'
        _unavailable('fontgate.fgFontGateData.hasColors')

    def hasHints(self) -> bool:
        'bool hasHints() - return true if hints is present'
        _unavailable('fontgate.fgFontGateData.hasHints')

    def hasPictures(self) -> bool:
        'bool hasPictures() - return true if pictures is present'
        _unavailable('fontgate.fgFontGateData.hasPictures')

    def maskLayer(self, createIfMissing: bool) -> fgLayer:
        'fgLayer maskLayer(bool createIfMissing)'
        _unavailable('fontgate.fgFontGateData.maskLayer')

    def modified(self) -> bool:
        'bool modified() - return true if data was changed'
        _unavailable('fontgate.fgFontGateData.modified')

    def resetBbox(self) -> Any:
        'resetBbox() - reset bbox cache'
        _unavailable('fontgate.fgFontGateData.resetBbox')

    def setParent(self, arg0: fgGlyph) -> Any:
        'setParent(fgGlyph) - set parent glyph'
        _unavailable('fontgate.fgFontGateData.setParent')

    def status(self) -> Any:
        "'gdsOK'/'gdsInvalid' status()"
        _unavailable('fontgate.fgFontGateData.status')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix) - transform data'
        _unavailable('fontgate.fgFontGateData.transform')

    def updated(self) -> Any:
        'updated() - mark data as changed, reset internal caches'
        _unavailable('fontgate.fgFontGateData.updated')

    layers: Any
    '(fgLayers) layers list'

class fgFontHinting:
    'Font Hinting data representation\n\nConstructors:\n  fgFontHinting() - default\n  fgFontHinting(fgFontHinting) - copy\n\nNative bases: object\n\nCaptured native MRO: fgFontHinting, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgFontHinting.__init__')

    def generateStemsProgram(self, upm: Any, keepValues: bool) -> Any:
        'generateStemsProgram(Position upm, bool keepValues)'
        _unavailable('fontgate.fgFontHinting.generateStemsProgram')

    def getBlueValues(self) -> Any:
        'list( float ) getBlueValues()'
        _unavailable('fontgate.fgFontHinting.getBlueValues')

    def getFamilyBlues(self) -> Any:
        'list( float ) getFamilyBlues()'
        _unavailable('fontgate.fgFontHinting.getFamilyBlues')

    def getFamilyOtherBlues(self, *args: Any, **kwargs: Any) -> Any:
        'list( float ) getFamilyBlues()'
        _unavailable('fontgate.fgFontHinting.getFamilyOtherBlues')

    def getOtherBlues(self) -> Any:
        'list( float ) getOtherBlues()'
        _unavailable('fontgate.fgFontHinting.getOtherBlues')

    def getZone(self, index: int, top: bool) -> Any:
        'fgZone/Nothing getZone(int index, bool top)'
        _unavailable('fontgate.fgFontHinting.getZone')

    def getZonesCount(self, top: bool) -> int:
        'int getZonesCount(bool top)'
        _unavailable('fontgate.fgFontHinting.getZonesCount')

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
    "FontInfo data\n\nNo constructors - it's the direct member of the fgFont object\n\nNative bases: object\n\nCaptured native MRO: fgFontInfo, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgFontInfo.__init__')

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
    'Font info dictionaries\n\nNative bases: object\n\nCaptured native MRO: fgFontInfoDict, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgFontInfoDict.__init__')

    flags: Any
    hinting: Any
    metrics: Any
    names: Any
    values: Any

class fgGaspRecord:
    'GaspRecord representation\n\nConstructors:  fgGaspRecord() - default\n  fgGaspRecord(fgGaspRecord) - copy\n  fgGaspRecord(int rangeMaxPPEM, int rangeGaspBehavior) - parametric\n\nNative bases: object\n\nCaptured native MRO: fgGaspRecord, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGaspRecord.__init__')

    def addSymmetry(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGaspRecord.addSymmetry; argument details are not documented.'
        _unavailable('fontgate.fgGaspRecord.addSymmetry')

    def rangeGaspBehavior(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGaspRecord.rangeGaspBehavior; argument details are not documented.'
        _unavailable('fontgate.fgGaspRecord.rangeGaspBehavior')

    def set(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGaspRecord.set; argument details are not documented.'
        _unavailable('fontgate.fgGaspRecord.set')

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
    'list of fgGaspRecord objects\n\nNative bases: object\n\nCaptured native MRO: fgGaspRecords, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGaspRecords.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgGaspRecords.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgGaspRecords.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgGaspRecords.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgGaspRecords.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgGaspRecords.insert')


class fgGlyph:
    "Glyph representation\n\nConstructors:\n  fgGlyph() - default\n  fgGlyph(fgGlyph) - copy\n  fgGlyph('name') - create by name\n\nNative bases: object\n\nCaptured native MRO: fgGlyph, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGlyph.__init__')

    def addUnicode(self, unicode: Any) -> Any:
        'addUnicode(unicode) - add unicode to glyph'
        _unavailable('fontgate.fgGlyph.addUnicode')

    def append(self, mtx: Any = ...) -> Any:
        'append(fgGlyph[, mtx=fgMatrix()]) - append contours of source glyph to current glyph'
        _unavailable('fontgate.fgGlyph.append')

    def clear(self, contours: Any = True, components: Any = True, anchors: Any = True, guides: Any = True, hints: Any = True) -> Any:
        "clear(contours=true, components=true, anchors=true, guides=true, hints=true) - clear glyph's data"
        _unavailable('fontgate.fgGlyph.clear')

    def countPictures(self) -> int:
        'int countPictures() - return count of glyph pictures'
        _unavailable('fontgate.fgGlyph.countPictures')

    def createContour(self) -> fgContour:
        'fgContour createContour() - create new contour'
        _unavailable('fontgate.fgGlyph.createContour')

    def createData(self, *args: Any, **kwargs: Any) -> Any:
        "(variable type) createData(GlyphDataType) - create glyph data, specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"
        _unavailable('fontgate.fgGlyph.createData')

    def decompose(self) -> bool:
        'bool decompose() - decompose glyph'
        _unavailable('fontgate.fgGlyph.decompose')

    def deleteContour(self, contourIndex: Any) -> Any:
        'deleteContour(contourIndex) - delete contour by index'
        _unavailable('fontgate.fgGlyph.deleteContour')

    def draw(self, *args: Any, **kwargs: Any) -> Any:
        'draw(penObject[, fgMatrix]) - draw contour by penObject (like fgPen) with transform matrix fgMatrix'
        _unavailable('fontgate.fgGlyph.draw')

    def fgData(self) -> Any:
        "fgFontGateData/Nothing fgData() - get dtFontGate data if it's exist"
        _unavailable('fontgate.fgGlyph.fgData')

    def fgDataCreate(self) -> fgFontGateData:
        'fgFontGateData fgDataCreate() - get dtFontGate data (create new one if missing)'
        _unavailable('fontgate.fgGlyph.fgDataCreate')

    def fixComposites(self, fixRotation: Any = False) -> bool:
        'bool fixComposites(fixRotation=false)'
        _unavailable('fontgate.fgGlyph.fixComposites')

    def getData(self, *args: Any, **kwargs: Any) -> Any:
        "(variable type) getData([GlyphDataType='dtFontGate']) - get glyph data, specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"
        _unavailable('fontgate.fgGlyph.getData')

    def getPen(self) -> fgPen:
        'fgPen getPen() - create new pen object'
        _unavailable('fontgate.fgGlyph.getPen')

    def hasBody(self) -> bool:
        'bool hasBody() - return True if glyph has contours or picture'
        _unavailable('fontgate.fgGlyph.hasBody')

    def hasColors(self) -> bool:
        'bool hasColors() - return True if glyph has color pictures'
        _unavailable('fontgate.fgGlyph.hasColors')

    def hasData(self, GlyphDataType: Any) -> bool:
        "bool hasData(GlyphDataType) - return True if glyph data, specified by GlyphDataType, is exist. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"
        _unavailable('fontgate.fgGlyph.hasData')

    def hasHints(self) -> bool:
        'bool hasHints() - return True if glyph has hints'
        _unavailable('fontgate.fgGlyph.hasHints')

    def hasPictures(self) -> bool:
        'bool hasPictures() - return True if glyph has pictures'
        _unavailable('fontgate.fgGlyph.hasPictures')

    def hasUnicode(self, unicode: Any) -> bool:
        'bool hasUnicode(unicode) - return True if glyph has specified unicode'
        _unavailable('fontgate.fgGlyph.hasUnicode')

    def keepData(self, GlyphDataType: Any) -> bool:
        "bool keepData(GlyphDataType) - remove all glyph data, except one specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"
        _unavailable('fontgate.fgGlyph.keepData')

    def killData(self, GlyphDataType: Any) -> bool:
        "bool killData(GlyphDataType) - remove glyph data, specified by GlyphDataType. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"
        _unavailable('fontgate.fgGlyph.killData')

    def killUnicode(self, unicode: Any) -> Any:
        'killUnicode(unicode) - remove unicode from glyph'
        _unavailable('fontgate.fgGlyph.killUnicode')

    def modified(self, GlyphDataType: Any) -> Any:
        "modified(GlyphDataType) - inform that glyph data GlyphDataType has been modified. Possible values are 'dtNone', 'dtFontGate', 'dtTrueType', 'dtType1', 'dtCFF', 'dtProteus', 'dtBitmaps'"
        _unavailable('fontgate.fgGlyph.modified')

    def move(self, dx: Any, dy: Any) -> Any:
        'move(dx, dy) - move contour by (dx, dy)'
        _unavailable('fontgate.fgGlyph.move')

    def removeOverlap(self) -> Any:
        'removeOverlap()'
        _unavailable('fontgate.fgGlyph.removeOverlap')

    def setData(self, object: Any) -> Any:
        'setData(GlyphData-like object) - set glyph data'
        _unavailable('fontgate.fgGlyph.setData')

    def setUnicode(self, unicode: Any) -> Any:
        'setUnicode(unicode) - assign unicode to glyph'
        _unavailable('fontgate.fgGlyph.setUnicode')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix) - transform glyph by fgMatrix data'
        _unavailable('fontgate.fgGlyph.transform')

    def ttData(self) -> Any:
        "fgTrueTypeData/Nothing ttData() - get dtTrueType data if it's exist"
        _unavailable('fontgate.fgGlyph.ttData')

    def ttDataCreate(self) -> fgTrueTypeData:
        'fgTrueTypeData ttDataCreate() - get dtTrueType data (create new one if missing)'
        _unavailable('fontgate.fgGlyph.ttDataCreate')

    def update(self) -> Any:
        'update()'
        _unavailable('fontgate.fgGlyph.update')

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
    'GlyphData representation\n\nConstructors:\n  fgGlyphData() - default\n  fgGlyphData(fgGlyphData) - copy\n\nNative bases: object\n\nCaptured native MRO: fgGlyphData, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGlyphData.__init__')

    def OK(self) -> bool:
        'bool OK() - return true if status is gdsOK'
        _unavailable('fontgate.fgGlyphData.OK')

    def bad(self) -> bool:
        "bool bad() - return true if status isn't gdsOK"
        _unavailable('fontgate.fgGlyphData.bad')

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        'fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box'
        _unavailable('fontgate.fgGlyphData.boundingBox')

    def copy(self) -> fgGlyphData:
        'fgGlyphData copy() - create alone copy of data'
        _unavailable('fontgate.fgGlyphData.copy')

    def countPictures(self) -> int:
        'int countPictures() - return pictures count'
        _unavailable('fontgate.fgGlyphData.countPictures')

    def countShapes(self) -> int:
        'int countShapes() - return shapes count'
        _unavailable('fontgate.fgGlyphData.countShapes')

    def getFontGateData(self) -> fgFontGateData:
        'fgFontGateData getFontGateData() - return Nothing'
        _unavailable('fontgate.fgGlyphData.getFontGateData')

    def getType(self) -> Any:
        "string getType() - return 'dtTrueType'"
        _unavailable('fontgate.fgGlyphData.getType')

    def hasBody(self, prepareExport: bool) -> bool:
        'bool hasBody(bool prepareExport) - return true if non-empty body layer is present'
        _unavailable('fontgate.fgGlyphData.hasBody')

    def hasColors(self) -> bool:
        'bool hasColors() - return true if colors is present'
        _unavailable('fontgate.fgGlyphData.hasColors')

    def hasHints(self) -> bool:
        'bool hasHints() - return true if hints is present'
        _unavailable('fontgate.fgGlyphData.hasHints')

    def hasPictures(self) -> bool:
        'bool hasPictures() - return true if pictures is present'
        _unavailable('fontgate.fgGlyphData.hasPictures')

    def modified(self) -> bool:
        'bool modified() - return true if data was changed'
        _unavailable('fontgate.fgGlyphData.modified')

    def setParent(self, arg0: fgGlyph) -> Any:
        'setParent(fgGlyph) - set parent glyph'
        _unavailable('fontgate.fgGlyphData.setParent')

    def status(self) -> Any:
        "'gdsOK'/'gdsInvalid' status()"
        _unavailable('fontgate.fgGlyphData.status')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix) - transform data'
        _unavailable('fontgate.fgGlyphData.transform')

    def updated(self) -> Any:
        'updated() - mark data as changed, reset internal caches'
        _unavailable('fontgate.fgGlyphData.updated')


class fgGlyphDict:
    'Glyph dictionaries\n\nNative bases: object\n\nCaptured native MRO: fgGlyphDict, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGlyphDict.__init__')

    flags: Any
    lib: Any
    tags: Any
    values: Any

class fgGlyphIDsSet:
    'GlyphIDs set\n\nConstructors:\n  fgGlyphIDsSet() - default\n  fgGlyphIDsSet(fgGlyphIDsSet) - copy\n\nNative bases: object\n\nCaptured native MRO: fgGlyphIDsSet, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGlyphIDsSet.__init__')

    def asList(self) -> Any:
        '[ int ] asList() - return set as list'
        _unavailable('fontgate.fgGlyphIDsSet.asList')

    def clean(self) -> Any:
        "clean() - remove all id's from set"
        _unavailable('fontgate.fgGlyphIDsSet.clean')

    def contains(self, id: int) -> bool:
        'bool contains(int id) - return True if set contains id'
        _unavailable('fontgate.fgGlyphIDsSet.contains')

    def del_(self, id: int) -> Any:
        'del(int id) - remove id from set\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgGlyphIDsSet.del')


class fgGlyphs:
    'list of fgGlyph objects\n\nNative bases: object\n\nCaptured native MRO: fgGlyphs, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGlyphs.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGlyphs.append; argument details are not documented.'
        _unavailable('fontgate.fgGlyphs.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGlyphs.asList; argument details are not documented.'
        _unavailable('fontgate.fgGlyphs.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGlyphs.clean; argument details are not documented.'
        _unavailable('fontgate.fgGlyphs.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGlyphs.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgGlyphs.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGlyphs.insert; argument details are not documented.'
        _unavailable('fontgate.fgGlyphs.insert')


class fgGlyphsR:
    'fgGlyphsR representation\n\nConstructors:\n  fgGlyphsR() - default\n  fgGlyphsR(fgGlyphsR) - copy\n  fgGlyphsR(fgGlyphs) - create from list(fgGlyph)\n\nNative bases: object\n\nCaptured native MRO: fgGlyphsR, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGlyphsR.__init__')

    def find(self, *args: Any, **kwargs: Any) -> Any:
        'fgGlyph find(name|unicode)'
        _unavailable('fontgate.fgGlyphsR.find')

    def getStats(self, *args: Any, **kwargs: Any) -> Any:
        '(totalGlyphs, avgNodesCount, avgContoursCount) getStats()'
        _unavailable('fontgate.fgGlyphsR.getStats')

    def glyph(self, index: int) -> fgGlyph:
        'fgGlyph glyph(int index)'
        _unavailable('fontgate.fgGlyphsR.glyph')

    def glyphByID(self, ID: int) -> fgGlyph:
        'fgGlyph glyphByID(int ID)'
        _unavailable('fontgate.fgGlyphsR.glyphByID')

    def index(self, arg0: fgGlyph) -> int:
        'int index(fgGlyph)'
        _unavailable('fontgate.fgGlyphsR.index')

    def indexByID(self, *args: Any, **kwargs: Any) -> Any:
        'int index(int ID)'
        _unavailable('fontgate.fgGlyphsR.indexByID')

    def rebuildUnicodeMap(self) -> Any:
        'rebuildUnicodeMap()'
        _unavailable('fontgate.fgGlyphsR.rebuildUnicodeMap')


class fgGroup:
    "Kerning/Metrics group\n\nConstructors:\n  fgGroup() - default\n  fgGroup(fgGroup) - copy\n  fgGroup( tuple('name', list(ids), mode, 'mainglyphname') ) - parametric\n           possible values for mode are 'FeaClassGroupMode', 'KernLeftGroupMode', 'KernRightGroupMode', 'KernBothSideGroupMode'\n\nNative bases: object\n\nCaptured native MRO: fgGroup, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGroup.__init__')

    def isBoth(self, *args: Any, **kwargs: Any) -> Any:
        "True if group mode is 'KernBothSideGroupMode'"
        _unavailable('fontgate.fgGroup.isBoth')

    def isFeaGroup(self, *args: Any, **kwargs: Any) -> Any:
        "True if group mode is 'FeaClassGroupMode'"
        _unavailable('fontgate.fgGroup.isFeaGroup')

    def isLeft(self, *args: Any, **kwargs: Any) -> Any:
        "True if group mode is 'KernLeftGroupMode' or 'KernBothSideGroupMode'"
        _unavailable('fontgate.fgGroup.isLeft')

    def isRight(self, *args: Any, **kwargs: Any) -> Any:
        "True if group mode is 'KernRightGroupMode' or 'KernBothSideGroupMode'"
        _unavailable('fontgate.fgGroup.isRight')

    id: Any
    '(int) group id'
    mode: Any
    "('FeaClassGroupMode'/'KernLeftGroupMode'/'KernRightGroupMode'/'KernBothSideGroupMode') group mode"
    name: Any
    '(string) group name'

class fgGroups:
    'Glyph groups list\n\nConstructors:\n  fgGroups() - default\n  fgGroups(fgDataOwnerData) - parametric\n\nNative bases: object\n\nCaptured native MRO: fgGroups, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGroups.__init__')

    def asDict(self) -> Any:
        "dict('name' : fgGroup) asDict()"
        _unavailable('fontgate.fgGroups.asDict')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontgate.fgGroups.clear')

    def fromClassRecords(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGroups.fromClassRecords; argument details are not documented.'
        _unavailable('fontgate.fgGroups.fromClassRecords')

    def fromDict(self, *args: Any, **kwargs: Any) -> Any:
        "fromDict(dict('name':fgGroup))"
        _unavailable('fontgate.fgGroups.fromDict')

    def get(self, *args: Any, **kwargs: Any) -> Any:
        "fgGroup get('name')"
        _unavailable('fontgate.fgGroups.get')

    def getAsClassRecords(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgGroups.getAsClassRecords; argument details are not documented.'
        _unavailable('fontgate.fgGroups.getAsClassRecords')

    def getCompiled(self) -> Any:
        'string getCompiled()'
        _unavailable('fontgate.fgGroups.getCompiled')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        "bool has_key('name')"
        _unavailable('fontgate.fgGroups.has_key')

    def items(self) -> Any:
        "list(tuple('name', fgGroup)) items()"
        _unavailable('fontgate.fgGroups.items')

    def keys(self) -> Any:
        'list(names of group) keys()'
        _unavailable('fontgate.fgGroups.keys')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        "bool remove('name')"
        _unavailable('fontgate.fgGroups.remove')

    def rename(self, *args: Any, **kwargs: Any) -> Any:
        "bool rename('old_name', 'new_name')"
        _unavailable('fontgate.fgGroups.rename')

    def values(self) -> Any:
        'list(fgGroup) values()'
        _unavailable('fontgate.fgGroups.values')


class fgGuide:
    "Guide representation\n\nConstructors:\n  fgGuide() - default\n  fgGuide(fgGuide) - copy\n  fgGuide(float pos[, bool horizontal = false])\n  fgGuide(fgPoint p0, fgPoint p1[, name=''[, horizonta=false[, color=fgColor]]])\n\nNative bases: object\n\nCaptured native MRO: fgGuide, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGuide.__init__')

    def copy(self) -> fgGuide:
        'fgGuide copy() - copy object'
        _unavailable('fontgate.fgGuide.copy')

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
    'list of fgGuide objects\n\nNative bases: object\n\nCaptured native MRO: fgGuides, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgGuides.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgGuides.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgGuides.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgGuides.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgGuides.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgGuides.insert')

    def remove(self, p0: fgPoint, p1: fgPoint) -> Any:
        "remove(fgPoint p0, fgPoint p1) - remove item if it's points are equal to specified"
        _unavailable('fontgate.fgGuides.remove')

    def removeHV(self, position: float, horizontal: bool) -> Any:
        'removeHV(float position, bool horizontal)'
        _unavailable('fontgate.fgGuides.removeHV')


class fgHint:
    'Hint representation\n\nConstructors:\n  fgHint() - default\n  fgHint(fgHint) - copy\n  fgHint(name= , v= , dv= , point0= , point1= , p0= , p1= , points0= , points1= , horizontal= )\n\nNative bases: object\n\nCaptured native MRO: fgHint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgHint.__init__')

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHint.copy; argument details are not documented.'
        _unavailable('fontgate.fgHint.copy')

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
    "HintCommand representation\n\nConstructors:\n  fgHintCommand() - default\n  fgHintCommand(fgHintCommand) - copy\n  fgHintCommand(code, index) - parametric, possible values for code are 'none'/'hintH'/'hintV'/'replace'\n\nNative bases: object\n\nCaptured native MRO: fgHintCommand, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgHintCommand.__init__')

    code: Any
    "('none'/'hintH'/'hintV'/'replace') code"
    index: Any
    '(int)'
    pointName: Any
    '(string)'
    subrIndex: Any
    '(int)'

class fgHintCommands:
    'list of fgHintCommand objects\n\nNative bases: object\n\nCaptured native MRO: fgHintCommands, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgHintCommands.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHintCommands.append; argument details are not documented.'
        _unavailable('fontgate.fgHintCommands.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHintCommands.asList; argument details are not documented.'
        _unavailable('fontgate.fgHintCommands.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHintCommands.clean; argument details are not documented.'
        _unavailable('fontgate.fgHintCommands.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHintCommands.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgHintCommands.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHintCommands.insert; argument details are not documented.'
        _unavailable('fontgate.fgHintCommands.insert')


class fgHints:
    'list of fgHint objects\n\nNative bases: object\n\nCaptured native MRO: fgHints, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgHints.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgHints.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgHints.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgHints.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgHints.del')

    def getAsDict(self) -> Any:
        'dict(items) getAsDict()'
        _unavailable('fontgate.fgHints.getAsDict')

    def getAsList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHints.getAsList; argument details are not documented.'
        _unavailable('fontgate.fgHints.getAsList')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgHints.insert')

    def removeByName(self, *args: Any, **kwargs: Any) -> Any:
        "removeByName('name')"
        _unavailable('fontgate.fgHints.removeByName')

    def removeHV(self, v: float, dv: float, horizontal: bool) -> Any:
        'removeHV(float v, float dv, bool horizontal)'
        _unavailable('fontgate.fgHints.removeHV')

    def setFromDict(self, *args: Any, **kwargs: Any) -> Any:
        'setFromDict(dict(items))'
        _unavailable('fontgate.fgHints.setFromDict')

    def setFromList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgHints.setFromList; argument details are not documented.'
        _unavailable('fontgate.fgHints.setFromList')


class fgIntDict:
    'int dictionary\n\nNative bases: object\n\nCaptured native MRO: fgIntDict, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgIntDict.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgIntDict.asDict; argument details are not documented.'
        _unavailable('fontgate.fgIntDict.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgIntDict.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgIntDict.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgIntDict.has_key; argument details are not documented.'
        _unavailable('fontgate.fgIntDict.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgIntDict.keys; argument details are not documented.'
        _unavailable('fontgate.fgIntDict.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgIntDict.value; argument details are not documented.'
        _unavailable('fontgate.fgIntDict.value')


class fgKerning:
    'Kerning representation\n\nConstructors:\n  fgKerning(fgDataOwnerData)\n\nNative bases: object\n\nCaptured native MRO: fgKerning, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgKerning.__init__')

    def addGroup(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.addGroup; argument details are not documented.'
        _unavailable('fontgate.fgKerning.addGroup')

    def asDict(self) -> Any:
        'dict(fgKerningObjectPair : float) asDict()'
        _unavailable('fontgate.fgKerning.asDict')

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.clear; argument details are not documented.'
        _unavailable('fontgate.fgKerning.clear')

    def deleteAllGroups(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.deleteAllGroups; argument details are not documented.'
        _unavailable('fontgate.fgKerning.deleteAllGroups')

    def deleteGroup(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.deleteGroup; argument details are not documented.'
        _unavailable('fontgate.fgKerning.deleteGroup')

    def get(self, *args: Any, **kwargs: Any) -> Any:
        "float get(fgKerningObjectPair / tuple('name1', 'name2')) - get kerning value"
        _unavailable('fontgate.fgKerning.get')

    def getPlainPairs(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.getPlainPairs; argument details are not documented.'
        _unavailable('fontgate.fgKerning.getPlainPairs')

    def getPlainPairsDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.getPlainPairsDict; argument details are not documented.'
        _unavailable('fontgate.fgKerning.getPlainPairsDict')

    def hasGroupKerning(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.hasGroupKerning; argument details are not documented.'
        _unavailable('fontgate.fgKerning.hasGroupKerning')

    def has_key(self, arg0: fgKerningObjectPair) -> bool:
        'bool has_key(fgKerningObjectPair)'
        _unavailable('fontgate.fgKerning.has_key')

    def items(self) -> Any:
        'list( tuple(fgKerningObjectPair, float) ) items()'
        _unavailable('fontgate.fgKerning.items')

    def keys(self) -> Any:
        'list(fgKerningObjectPair) keys()'
        _unavailable('fontgate.fgKerning.keys')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.remove; argument details are not documented.'
        _unavailable('fontgate.fgKerning.remove')

    def renameGroup(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.renameGroup; argument details are not documented.'
        _unavailable('fontgate.fgKerning.renameGroup')

    def scale(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.scale; argument details are not documented.'
        _unavailable('fontgate.fgKerning.scale')

    def set(self, *args: Any, **kwargs: Any) -> Any:
        "int set(fgKerningObjectPair / tuple('name1', 'name2'), double) - set kerning value"
        _unavailable('fontgate.fgKerning.set')

    def setPlainPairs(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgKerning.setPlainPairs; argument details are not documented.'
        _unavailable('fontgate.fgKerning.setPlainPairs')

    def values(self) -> Any:
        'list( float ) values()'
        _unavailable('fontgate.fgKerning.values')

    groups: Any

class fgKerningGroups:
    'Dictionary of kerning groups\n\nConstructors:\n  fgKerningGroups(fgDataOwnerData) - default\n\nNative bases: object\n\nCaptured native MRO: fgKerningGroups, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgKerningGroups.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgKerningGroups.asDict')

    def clear(self) -> Any:
        'clear() - delete all items'
        _unavailable('fontgate.fgKerningGroups.clear')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        "bool has_key('groupName')"
        _unavailable('fontgate.fgKerningGroups.has_key')

    def items(self) -> Any:
        "list( tuple('groupName', tuple( list('glyphName'), mode ) ) items()"
        _unavailable('fontgate.fgKerningGroups.items')

    def keys(self) -> Any:
        "list('groupName') keys()"
        _unavailable('fontgate.fgKerningGroups.keys')

    def remove(self, deleteDependentKerningPairs: Any = ...) -> Any:
        "remove('groupName'[, deleteDependentKerningPairs = false])"
        _unavailable('fontgate.fgKerningGroups.remove')

    def rename(self, *args: Any, **kwargs: Any) -> Any:
        "bool/Nothing rename('oldGroupName', 'newGroupName')"
        _unavailable('fontgate.fgKerningGroups.rename')

    def values(self) -> Any:
        "list ( tuple( list('glyphName'), mode ) ) values()"
        _unavailable('fontgate.fgKerningGroups.values')


class fgKerningObject:
    "KerningObject representation\n\nConstructors:  fgKerningObject() - default\n  fgKerningObject(fgKerningObject) - copy\n  fgKerningObject('name', mode) - mode must be one of 'glyphMode'/'groupMode'\n\nNative bases: object\n\nCaptured native MRO: fgKerningObject, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgKerningObject.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgKerningObject.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgKerningObject.asTuple')

    id: Any
    '(string) glyph or group name'
    mode: Any
    "('glyphMode'/'groupMode')"

class fgKerningObjectPair:
    "KerningObjectPair representation\n\nConstructors:  fgKerningObjectPair() - default\n  fgKerningObjectPair(fgKerningObjectPair) - copy\n  fgKerningObjectPair( tuple(fgKerningObject, fgKerningObject) )\n  fgKerningObjectPair('nameLeft', 'nameRight')\n  fgKerningObjectPair(fgKerningObject, fgKerningObject)\n  fgKerningObjectPair('nameLeft', 'nameRight', modeLeft, modeRight) - modeLeft, modeRight must be one of 'glyphMode'/'groupMode'\n\nNative bases: object\n\nCaptured native MRO: fgKerningObjectPair, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgKerningObjectPair.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgKerningObjectPair.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgKerningObjectPair.asTuple')

    left: Any
    '(fgKerningObject) - left glyph or group'
    right: Any
    '(fgKerningObject) - right glyph or group'

class fgLayer:
    "Layer representation\n\nConstructors:\n  fgLayer() - default\n  fgLayer(fgLayer) - copy\n  fgLayer('name') - create named layer\n\nMath operation:\n  fgLayer + fgLayer\n  fgLayer - fgLayer\n\nNative bases: object\n\nCaptured native MRO: fgLayer, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgLayer.__init__')

    def addContour(self, arg0: fgContour) -> fgContour:
        'fgContour addContour(fgContour) - add contour to layer'
        _unavailable('fontgate.fgLayer.addContour')

    def boundingBox(self, prepareExport: Any = ...) -> Any:
        'fgRect/Nothing boundingBox(fgMatrix[, prepareExport = false])'
        _unavailable('fontgate.fgLayer.boundingBox')

    def checkContours(self) -> Any:
        'checkContours()'
        _unavailable('fontgate.fgLayer.checkContours')

    def countContours(self) -> int:
        'int countContours()'
        _unavailable('fontgate.fgLayer.countContours')

    def countHints(self, horizontal: bool) -> int:
        'int countHints(bool horizontal)'
        _unavailable('fontgate.fgLayer.countHints')

    def countNodes(self) -> int:
        'int countNodes()'
        _unavailable('fontgate.fgLayer.countNodes')

    def countPictures(self) -> int:
        'int countPictures()'
        _unavailable('fontgate.fgLayer.countPictures')

    def countShapes(self) -> int:
        'int countShapes()'
        _unavailable('fontgate.fgLayer.countShapes')

    def findHint(self, arg0: fgHint) -> int:
        'int findHint(fgHint)'
        _unavailable('fontgate.fgLayer.findHint')

    def findNode(self, *args: Any, **kwargs: Any) -> Any:
        "fgNode/Nothing findNode(nodeIndex / 'nodeName') - find name by index or name"
        _unavailable('fontgate.fgLayer.findNode')

    def hasColors(self) -> bool:
        'bool hasColors()'
        _unavailable('fontgate.fgLayer.hasColors')

    def hasHints(self) -> bool:
        'bool hasHints()'
        _unavailable('fontgate.fgLayer.hasHints')

    def hasPictures(self) -> bool:
        'bool hasPictures()'
        _unavailable('fontgate.fgLayer.hasPictures')

    def hints2links(self, *args: Any, **kwargs: Any) -> Any:
        'hints2links(double tolerance[, fgCuspPoints])'
        _unavailable('fontgate.fgLayer.hints2links')

    def indexToName(self, nodeIndex: int) -> Any:
        "'nodeName' indexToName(int nodeIndex)"
        _unavailable('fontgate.fgLayer.indexToName')

    def isCompatible(self, arg0: flLayer) -> Any:
        'bool/Nothing isCompatible(flLayer)'
        _unavailable('fontgate.fgLayer.isCompatible')

    def nameToIndex(self, *args: Any, **kwargs: Any) -> Any:
        "int nameToIndex('nodeName')"
        _unavailable('fontgate.fgLayer.nameToIndex')

    def prepareNodeNames(self) -> Any:
        'prepareNodeNames()'
        _unavailable('fontgate.fgLayer.prepareNodeNames')

    def removeHints(self, horizontal: bool) -> Any:
        'removeHints(bool horizontal)'
        _unavailable('fontgate.fgLayer.removeHints')

    def transform(self, apply: Any = ...) -> Any:
        'transform(const Matrix& mx[, apply = true])'
        _unavailable('fontgate.fgLayer.transform')

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
    'list of fgLayer objects\n\nNative bases: object\n\nCaptured native MRO: fgLayers, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgLayers.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLayers.append; argument details are not documented.'
        _unavailable('fontgate.fgLayers.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLayers.asList; argument details are not documented.'
        _unavailable('fontgate.fgLayers.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLayers.clean; argument details are not documented.'
        _unavailable('fontgate.fgLayers.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLayers.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgLayers.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLayers.insert; argument details are not documented.'
        _unavailable('fontgate.fgLayers.insert')


class fgLib:
    'Dictionary with font- or glyph-related data\n\nNative bases: object\n\nCaptured native MRO: fgLib, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgLib.__init__')

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLib.clear; argument details are not documented.'
        _unavailable('fontgate.fgLib.clear')

    def get(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLib.get; argument details are not documented.'
        _unavailable('fontgate.fgLib.get')

    def hasKey(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLib.hasKey; argument details are not documented.'
        _unavailable('fontgate.fgLib.hasKey')

    def items(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLib.items; argument details are not documented.'
        _unavailable('fontgate.fgLib.items')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLib.keys; argument details are not documented.'
        _unavailable('fontgate.fgLib.keys')

    def update(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgLib.update; argument details are not documented.'
        _unavailable('fontgate.fgLib.update')


class fgMapBytes:
    'Raw data dictionary\n\nNative bases: object\n\nCaptured native MRO: fgMapBytes, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgMapBytes.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMapBytes.asDict; argument details are not documented.'
        _unavailable('fontgate.fgMapBytes.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMapBytes.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgMapBytes.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMapBytes.has_key; argument details are not documented.'
        _unavailable('fontgate.fgMapBytes.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMapBytes.keys; argument details are not documented.'
        _unavailable('fontgate.fgMapBytes.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMapBytes.value; argument details are not documented.'
        _unavailable('fontgate.fgMapBytes.value')


class fgMaster:
    "Anchor representation\n\nConstructors:\n  fgMaster() - default\n  fgMaster(fgMaster) - copy\n  fgMaster('name') - create with name='name'\n\nNative bases: object\n\nCaptured native MRO: fgMaster, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgMaster.__init__')

    name: Any
    '(string) - name'
    penColor: Any
    '(int) - penColor'
    position: Any
    '(fgDesignPosition)'

class fgMasters:
    'list of fgMaster objects\n\nNative bases: object\n\nCaptured native MRO: fgMasters, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgMasters.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgMasters.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgMasters.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgMasters.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgMasters.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgMasters.insert')


class fgMatrix:
    'Transformation matrix representation\n\nConstructors:\n  fgMatrix() - default\n  fgMatrix(fgMatrix) - copy\n  fgMatrix(float m11, float m12, float m21, float m22, float dx, float dy)\n\nMath operation:\n  fgMatrix * fgMatrix\n  \n\nNative bases: object\n\nCaptured native MRO: fgMatrix, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgMatrix.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgMatrix.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgMatrix.asTuple')

    def assign(self, m11: Any, m12: Any, m21: Any, m22: Any, dx: Any, dy: Any) -> Any:
        'assign(fgMatrix) or assign(m11, m12, m21, m22, dx, dy)'
        _unavailable('fontgate.fgMatrix.assign')

    def determinant(self) -> float:
        'float determinant()'
        _unavailable('fontgate.fgMatrix.determinant')

    def invert(self) -> bool:
        'bool invert()'
        _unavailable('fontgate.fgMatrix.invert')

    def inverted(self) -> fgMatrix:
        'fgMatrix inverted()'
        _unavailable('fontgate.fgMatrix.inverted')

    def invertible(self) -> bool:
        'bool invertible()'
        _unavailable('fontgate.fgMatrix.invertible')

    def noMove(self) -> bool:
        'bool noMove()'
        _unavailable('fontgate.fgMatrix.noMove')

    def noRotate(self) -> bool:
        'bool noRotate()'
        _unavailable('fontgate.fgMatrix.noRotate')

    def noScale(self) -> bool:
        'bool noScale()'
        _unavailable('fontgate.fgMatrix.noScale')

    def scale(self, s: float) -> Any:
        'scale(float s)'
        _unavailable('fontgate.fgMatrix.scale')

    def slant(self) -> Any:
        'slant(float angle) or float slant()'
        _unavailable('fontgate.fgMatrix.slant')

    def standard(self) -> bool:
        'bool standard()'
        _unavailable('fontgate.fgMatrix.standard')

    dx: Any
    dy: Any
    m11: Any
    m12: Any
    m21: Any
    m22: Any

class fgMaxP:
    'fgMaxP representation\n\nNative bases: object\n\nCaptured native MRO: fgMaxP, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgMaxP.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgMaxP.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgMaxP.asTuple')

    maxFunctionDefs: Any
    maxInstructionDefs: Any
    maxStackElements: Any
    maxStorage: Any
    maxTwilightPoints: Any
    maxZones: Any

class fgMetricsClass:
    'MetricsClass representation\n\nConstructors:\n  fgMetricsClass() - default\n  fgMetricsClass(fgMetricsClass) - copy\n\nNative bases: object\n\nCaptured native MRO: fgMetricsClass, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgMetricsClass.__init__')

    def hasGlyph(self, *args: Any, **kwargs: Any) -> Any:
        "bool hasGlyph(int glyphID/'glyphName')"
        _unavailable('fontgate.fgMetricsClass.hasGlyph')

    def keyGlyphName(self) -> Any:
        "'keyGlyphName' keyGlyphName()"
        _unavailable('fontgate.fgMetricsClass.keyGlyphName')

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
    'list of fgMetricsClass objects\n\nNative bases: object\n\nCaptured native MRO: fgMetricsClasses, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgMetricsClasses.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMetricsClasses.append; argument details are not documented.'
        _unavailable('fontgate.fgMetricsClasses.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMetricsClasses.asList; argument details are not documented.'
        _unavailable('fontgate.fgMetricsClasses.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMetricsClasses.clean; argument details are not documented.'
        _unavailable('fontgate.fgMetricsClasses.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMetricsClasses.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgMetricsClasses.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgMetricsClasses.insert; argument details are not documented.'
        _unavailable('fontgate.fgMetricsClasses.insert')


class fgNametable:
    'NameTable - unicode->name translation and vice versa\n\nNative bases: object\n\nCaptured native MRO: fgNametable, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgNametable.__init__')

    def easyCompare(self, *args: Any, **kwargs: Any) -> Any:
        "bool easyCompare('name0', 'name1')"
        _unavailable('fontgate.fgNametable.easyCompare')

    def getAlternativeNames(self, *args: Any, **kwargs: Any) -> Any:
        "list( 'altGlyphName' ) getAlternativeNames('glyphName')"
        _unavailable('fontgate.fgNametable.getAlternativeNames')

    def load(self, path_to_file: Any) -> bool:
        'bool load(string path_to_file)'
        _unavailable('fontgate.fgNametable.load')

    def name(self, unicode: int) -> Any:
        "'glyphName' name(int unicode)"
        _unavailable('fontgate.fgNametable.name')

    def unc(self, *args: Any, **kwargs: Any) -> Any:
        "int unc('glyphName')"
        _unavailable('fontgate.fgNametable.unc')

    loaded: Any
    '(bool)'

class fgNode:
    "Node representation\n\nConstructors:\n  fgNode() - default\n  fgNode(fgNode) - copy\n  fgNode('Move'/'On'/'Off'/'Curve', fgPoint[, smooth=false])\n  fgNode('Move'/'On'/'Off'/'Curve', fgPoint, 'name'[, smooth=false])\n\nMath operation:\n  fgNode + fgNode\n  fgNode - fgNode\n  fgNode * float\n\nNative bases: object\n\nCaptured native MRO: fgNode, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgNode.__init__')

    def isCurve(self) -> bool:
        'bool isCurve()'
        _unavailable('fontgate.fgNode.isCurve')

    def isCurveOff(self) -> bool:
        'bool isCurveOff()'
        _unavailable('fontgate.fgNode.isCurveOff')

    def isG2(self) -> bool:
        'bool isG2()'
        _unavailable('fontgate.fgNode.isG2')

    def isInterpolatedX(self) -> bool:
        'bool isInterpolatedX()'
        _unavailable('fontgate.fgNode.isInterpolatedX')

    def isInterpolatedY(self) -> bool:
        'bool isInterpolatedY()'
        _unavailable('fontgate.fgNode.isInterpolatedY')

    def isOff(self) -> bool:
        'bool isOff()'
        _unavailable('fontgate.fgNode.isOff')

    def isOn(self) -> bool:
        'bool isOn()'
        _unavailable('fontgate.fgNode.isOn')

    def isSelected(self) -> bool:
        'bool isSelected()'
        _unavailable('fontgate.fgNode.isSelected')

    def setG2(self, *args: Any, **kwargs: Any) -> Any:
        'setG2([true])'
        _unavailable('fontgate.fgNode.setG2')

    def setInterpolatedX(self, *args: Any, **kwargs: Any) -> Any:
        'setInterpolatedX([true])'
        _unavailable('fontgate.fgNode.setInterpolatedX')

    def setInterpolatedY(self, *args: Any, **kwargs: Any) -> Any:
        'setInterpolatedY([true])'
        _unavailable('fontgate.fgNode.setInterpolatedY')

    def setSelected(self, *args: Any, **kwargs: Any) -> Any:
        'setSelected([true])'
        _unavailable('fontgate.fgNode.setSelected')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix)'
        _unavailable('fontgate.fgNode.transform')

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
    'list of fgNode objects\n\nNative bases: object\n\nCaptured native MRO: fgNodes, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgNodes.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgNodes.append; argument details are not documented.'
        _unavailable('fontgate.fgNodes.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgNodes.asList; argument details are not documented.'
        _unavailable('fontgate.fgNodes.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgNodes.clean; argument details are not documented.'
        _unavailable('fontgate.fgNodes.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgNodes.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgNodes.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgNodes.insert; argument details are not documented.'
        _unavailable('fontgate.fgNodes.insert')


class fgOTLayout:
    'OpenType Layout representation\n\nConstructors:\n  fgOTLayout(fgDataOwnerData)\n  fgOTLayout(fgFont)\n\nNative bases: object\n\nCaptured native MRO: fgOTLayout, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOTLayout.__init__')

    def clear(self) -> Any:
        'clear() - remove all features'
        _unavailable('fontgate.fgOTLayout.clear')

    def get_feature(self, tag: Any) -> Any:
        'string get_feature(string / numeric tag) - get feature text'
        _unavailable('fontgate.fgOTLayout.get_feature')

    def get_prefix(self) -> Any:
        'string get_prefix() - get common part of fea data'
        _unavailable('fontgate.fgOTLayout.get_prefix')

    def has_key(self, tag: Any) -> bool:
        'bool has_key(string / numeric tag) - True if feature is present'
        _unavailable('fontgate.fgOTLayout.has_key')

    def keys(self) -> Any:
        'list(string) keys() - list of feature tags'
        _unavailable('fontgate.fgOTLayout.keys')

    def remove(self, tag: Any) -> Any:
        'remove(string / numeric tag) - remove feature'
        _unavailable('fontgate.fgOTLayout.remove')

    def set_feature(self, tag: Any, new_content: Any) -> Any:
        'set_feature(string / numeric tag, string new_content) - set feature text'
        _unavailable('fontgate.fgOTLayout.set_feature')

    def set_prefix(self, new_prefix: Any) -> Any:
        'set_prefix(string new_prefix) - set common part of fea data'
        _unavailable('fontgate.fgOTLayout.set_prefix')


class fgOpt_AutoMetrics:
    'fgOpt_AutoMetrics options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_AutoMetrics, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_AutoMetrics.__init__')

    close: Any
    left: Any
    right: Any

class fgOpt_EOTExport:
    'fgOpt_EOTExport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_EOTExport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_EOTExport.__init__')

    doCompression: Any
    doXORCryptData: Any

class fgOpt_ExpandKerning:
    'fgOpt_ExpandKerning options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_ExpandKerning, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_ExpandKerning.__init__')

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
    'fgOpt_Font options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_Font, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_Font.__init__')

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
    'fgOpt_KerningOptions options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_KerningOptions, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_KerningOptions.__init__')

    saveTheOnlySubtableInKernTable: Any
    useScriptInfoForOneSubtableCutting: Any

class fgOpt_OTExport:
    'fgOpt_OTExport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_OTExport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_OTExport.__init__')

    CBDT: Any
    COLR: Any
    SVG: Any
    addCharacters: Any
    applyBBoxSavings: Any
    autoWinAscDesc: Any
    autohint: Any
    autohintGlyphs: Any
    autohinterMode: Any
    autohintingMode: Any
    'Compatibility alias for autohinterMode'
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
    writeBinaryHinting: Any
    writeBitmaps: Any
    writeDeviceMetrics: Any
    writeGDEF: Any
    writeHintedFont: Any
    writeKernFeature: Any
    writeKernTable: Any
    writeOriginalHinting: Any

class fgOpt_OTExportFeaFile:
    'fgOpt_OTExportFeaFile options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_OTExportFeaFile, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_OTExportFeaFile.__init__')

    doWriteGDEF: Any
    inlineLookups: Any
    verbose: Any
    write_body: Any
    write_classes: Any
    write_prefix: Any

class fgOpt_OTImport:
    'fgOpt_OTImport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_OTImport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_OTImport.__init__')

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
    'fgOpt_Optimize options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_Optimize, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_Optimize.__init__')

    align: Any
    reduce: Any

class fgOpt_T1Autohint:
    'fgOpt_T1Autohint options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_T1Autohint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_T1Autohint.__init__')

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
    'fgOpt_T1Export options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_T1Export, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_T1Export.__init__')

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
    'fgOpt_T1Import options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_T1Import, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_T1Import.__init__')

    decompose: Any
    familyGrouping: Any
    ignoreGlyphs: Any
    readMacSpecificNaming: Any
    singleMasterOnly: Any

class fgOpt_TTAutohint:
    'fgOpt_TTAutohint options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_TTAutohint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_TTAutohint.__init__')

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
    'fgOpt_TTFAutohint options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_TTFAutohint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_TTFAutohint.__init__')

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
    'fgOpt_UfoFontExport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_UfoFontExport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_UfoFontExport.__init__')

    base64: Any
    compress: Any
    formatVersion: Any
    writeLayoutTTX: Any

class fgOpt_UfoFontImport:
    'fgOpt_UfoFontImport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_UfoFontImport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_UfoFontImport.__init__')

    compileFeatures: Any
    fixOrdering: Any
    readLayoutTTX: Any

class fgOpt_VfbExport:
    'fgOpt_VfbExport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_VfbExport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_VfbExport.__init__')

    saveEncoding: Any

class fgOpt_VfbImport:
    'fgOpt_VfbImport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_VfbImport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_VfbImport.__init__')

    compileFeatures: Any
    fixOrdering: Any
    separateMasters: Any

class fgOpt_WOFFExport:
    'fgOpt_WOFFExport options page\n\nNative bases: object\n\nCaptured native MRO: fgOpt_WOFFExport, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOpt_WOFFExport.__init__')


class fgOptions:
    'FontGate options\n\nNative bases: object\n\nCaptured native MRO: fgOptions, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOptions.__init__')

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
    'OT Info representation\n\nConstructors:\n  fgOtInfo() - default\n  fgOtInfo(fgOtInfo) - copy\n\nNative bases: object\n\nCaptured native MRO: fgOtInfo, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOtInfo.__init__')

    glyphClass: Any
    "('Unspecified'/'Simple'/'Ligature'/'Mark'/'Component')"
    markClass: Any
    '(int)'
    otClasses: Any
    '( [ int ] )'

class fgOtValue:
    'OT Value representation\n\nConstructors:\n  fgOtValue() - default\n  fgOtValue(fgOtValue) - copy\n  fgOtValue(float) - by float value\n  fgOtValue(int/long) - by int/long value\n\nMath operation:\n  fgOtValue + fgOtValue\n  fgOtValue - fgOtValue\n  fgOtValue * float\n\nNative bases: object\n\nCaptured native MRO: fgOtValue, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgOtValue.__init__')

    coordinate: Any
    '(float)'
    deviceTable: Any
    '(fgDeviceRecords)'
    point_index: Any
    '(int)'

class fgPackages:
    "Font packages representation\n\nConstructors:\n  fgPackages() - default\n  fgPackages(fgPackages) - copy\n  fgPackages('pathToFontFileOrFolder')\n\nNative bases: object\n\nCaptured native MRO: fgPackages, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature."
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgPackages.__init__')

    def add(self, object: Any) -> Any:
        'add(fgFont or fgPackages object) - add font(s)'
        _unavailable('fontgate.fgPackages.add')

    def close(self) -> Any:
        'close() - remove all font(s) from list'
        _unavailable('fontgate.fgPackages.close')

    def copyFrom(self, arg0: fgPackages) -> Any:
        'copyFrom(fgPackages) - copy all fonts from another fgPackages object'
        _unavailable('fontgate.fgPackages.copyFrom')

    def create(self) -> Any:
        "create() - add empty font to list and return it's index"
        _unavailable('fontgate.fgPackages.create')

    def indexOf(self, arg0: fgFont) -> Any:
        'indexOf(fgFont) - return font index or (-1) if missing in list'
        _unavailable('fontgate.fgPackages.indexOf')

    def open(self, path: Any) -> Any:
        "open(path) - open existing font(s) from 'path' location and return first index of created font(s)"
        _unavailable('fontgate.fgPackages.open')

    def remove(self, index: int) -> Any:
        'remove(int index) - remove font by index'
        _unavailable('fontgate.fgPackages.remove')


class fgPen:
    'Pen representation\n\nConstructors:\n  fgPen(fgGlyph) - default\n  fgPen(fgPen) - copy\n\nNative bases: object\n\nCaptured native MRO: fgPen, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgPen.__init__')

    def beginPath(self) -> Any:
        'beginPath()'
        _unavailable('fontgate.fgPen.beginPath')

    def closePath(self) -> Any:
        'closePath()'
        _unavailable('fontgate.fgPen.closePath')

    def curveTo(self, *args: Any, **kwargs: Any) -> Any:
        'curveTo(fgPoint...)'
        _unavailable('fontgate.fgPen.curveTo')

    def curveToOne(self, arg0: fgPoint, arg1: fgPoint, arg2: fgPoint) -> Any:
        'curveToOne(fgPoint, fgPoint, fgPoint)'
        _unavailable('fontgate.fgPen.curveToOne')

    def endPath(self) -> Any:
        'endPath()'
        _unavailable('fontgate.fgPen.endPath')

    def lineTo(self, arg0: fgPoint) -> Any:
        'lineTo(fgPoint)'
        _unavailable('fontgate.fgPen.lineTo')

    def moveTo(self, arg0: fgPoint) -> Any:
        'moveTo(fgPoint)'
        _unavailable('fontgate.fgPen.moveTo')

    def qCurveToOne(self, arg0: fgPoint, arg1: fgPoint) -> Any:
        'qCurveToOne(fgPoint, fgPoint)'
        _unavailable('fontgate.fgPen.qCurveToOne')

    smooth: Any
    '(bool)'

class fgPoint:
    'Point representation\n\nConstructors:\n  fgPoint() - default\n  fgPoint(fgPoint) - copy\n  fgPoint(float x)\n  fgPoint(tuple(float x, float y))\n  fgPoint(float x, float y)\n\nMath Operations:\n  fgPoint + fgPoint\n  fgPoint - fgPoint\n  fgPoint * fgPoint\n  fgPoint * float - vector product\n  fgPoint / float\n  fgPoint << fgPoint - True if first point is less or equal to second\n  fgPoint >> fgPoint - True if first point is greater or equal to second\n  fgPoint ^ fgPoint - scalar product\n\nNative bases: object\n\nCaptured native MRO: fgPoint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgPoint.__init__')

    def angleDiff(self, arg0: fgPoint) -> fgPoint:
        'fgPoint angleDiff(fgPoint)'
        _unavailable('fontgate.fgPoint.angleDiff')

    def angleSum(self, arg0: fgPoint) -> fgPoint:
        'fgPoint angleSum(fgPoint)'
        _unavailable('fontgate.fgPoint.angleSum')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgPoint.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgPoint.asTuple')

    def assign(self, x: float, y: float) -> Any:
        'assign(fgPoint) or assign(float x, float y)'
        _unavailable('fontgate.fgPoint.assign')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontgate.fgPoint.clear')

    def close_to(self, d: Any = ...) -> bool:
        'bool close_to(fgPoint[, d=0.00001])'
        _unavailable('fontgate.fgPoint.close_to')

    def collinear(self, arg0: fgPoint) -> bool:
        'bool collinear(fgPoint)'
        _unavailable('fontgate.fgPoint.collinear')

    def direction(self) -> fgPoint:
        'fgPoint direction()'
        _unavailable('fontgate.fgPoint.direction')

    def dist(self, arg0: fgPoint) -> float:
        'float dist(fgPoint)'
        _unavailable('fontgate.fgPoint.dist')

    def dist2(self, arg0: fgPoint) -> float:
        'float dist2(fgPoint)'
        _unavailable('fontgate.fgPoint.dist2')

    def distance(self, *args: Any, **kwargs: Any) -> Any:
        'float distance(fgPoint[, horizontal=false]'
        _unavailable('fontgate.fgPoint.distance')

    def doubleScale(self, *args: Any, **kwargs: Any) -> Any:
        'scale(fgPoint) or scale(float sx, float sy)'
        _unavailable('fontgate.fgPoint.doubleScale')

    def flip(self) -> Any:
        'flip()'
        _unavailable('fontgate.fgPoint.flip')

    def flipped(self) -> fgPoint:
        'fgPoint flipped()'
        _unavailable('fontgate.fgPoint.flipped')

    def ix(self) -> int:
        'int ix() - integer fast'
        _unavailable('fontgate.fgPoint.ix')

    def iy(self) -> int:
        'int iy() - integer fast'
        _unavailable('fontgate.fgPoint.iy')

    def len(self) -> float:
        'float len()'
        _unavailable('fontgate.fgPoint.len')

    def len2(self) -> float:
        'float len2()'
        _unavailable('fontgate.fgPoint.len2')

    def normal(self) -> fgPoint:
        'fgPoint normal()'
        _unavailable('fontgate.fgPoint.normal')

    def rotate(self, v: fgPoint, c: fgPoint) -> fgPoint:
        'fgPoint rotate(fgPoint v, fgPoint c)'
        _unavailable('fontgate.fgPoint.rotate')

    def round(self, *args: Any, **kwargs: Any) -> Any:
        'fgPoint round([doRound=true])'
        _unavailable('fontgate.fgPoint.round')

    def rx(self) -> int:
        'int rx() - integer rounded'
        _unavailable('fontgate.fgPoint.rx')

    def ry(self) -> int:
        'int ry() - integer rounded'
        _unavailable('fontgate.fgPoint.ry')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix)'
        _unavailable('fontgate.fgPoint.transform')

    def transformed(self, arg0: fgMatrix) -> fgPoint:
        'fgPoint transformed(fgMatrix)'
        _unavailable('fontgate.fgPoint.transformed')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'float value([horizontal=true])'
        _unavailable('fontgate.fgPoint.value')

    def zero(self) -> bool:
        'bool zero()'
        _unavailable('fontgate.fgPoint.zero')

    x: Any
    '(float)'
    y: Any
    '(float)'

class fgPointU:
    'PointU representation\n\nConstructors:\n  fgPointU() - default\n  fgPointU(fgPoint) - copy\n  fgPointU(fgPointU) - copy\n  fgPointU(fgPoint, float u)\n  fgPointU(tuple(float x, float y, float u))\n  fgPointU(float x, float y, float u)\n\nMath Operations:\n  fgPointU + fgPoint/fgPointU\n  fgPointU - fgPoint/fgPointU\n  fgPointU * fgPoint/fgPointU\n  fgPointU * float - vector product\n  fgPointU / float\n  fgPointU << fgPointU - True if first point is less or equal to second\n  fgPointU >> fgPointU - True if first point is greater or equal to second\n  fgPointU ^ fgPointU - scalar product\n\nNative bases: object\n\nCaptured native MRO: fgPointU, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgPointU.__init__')

    def angleDiff(self, arg0: fgPoint) -> fgPoint:
        'fgPoint angleDiff(fgPoint)'
        _unavailable('fontgate.fgPointU.angleDiff')

    def angleSum(self, arg0: fgPoint) -> fgPoint:
        'fgPoint angleSum(fgPoint)'
        _unavailable('fontgate.fgPointU.angleSum')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgPointU.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgPointU.asTuple')

    def assign(self, x: float, y: float, u: float) -> Any:
        'assign(fgPointU) or assign(float x, float y, float u)'
        _unavailable('fontgate.fgPointU.assign')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontgate.fgPointU.clear')

    def close_to(self, d: Any = ...) -> bool:
        'bool close_to(fgPointU[, d=0.00001])'
        _unavailable('fontgate.fgPointU.close_to')

    def collinear(self, arg0: fgPoint) -> bool:
        'bool collinear(fgPoint)'
        _unavailable('fontgate.fgPointU.collinear')

    def direction(self) -> fgPoint:
        'fgPoint direction()'
        _unavailable('fontgate.fgPointU.direction')

    def dist(self, arg0: fgPoint) -> float:
        'float dist(fgPoint)'
        _unavailable('fontgate.fgPointU.dist')

    def dist2(self, arg0: fgPoint) -> float:
        'float dist2(fgPoint)'
        _unavailable('fontgate.fgPointU.dist2')

    def distance(self, *args: Any, **kwargs: Any) -> Any:
        'float distance(fgPoint[, horizontal=false]'
        _unavailable('fontgate.fgPointU.distance')

    def doubleScale(self, *args: Any, **kwargs: Any) -> Any:
        'scale(fgPoint) or scale(float sx, float sy)'
        _unavailable('fontgate.fgPointU.doubleScale')

    def flip(self) -> Any:
        'flip()'
        _unavailable('fontgate.fgPointU.flip')

    def flipped(self) -> fgPoint:
        'fgPoint flipped()'
        _unavailable('fontgate.fgPointU.flipped')

    def ix(self) -> int:
        'int ix() - integer fast'
        _unavailable('fontgate.fgPointU.ix')

    def iy(self) -> int:
        'int iy() - integer fast'
        _unavailable('fontgate.fgPointU.iy')

    def len(self) -> float:
        'float len()'
        _unavailable('fontgate.fgPointU.len')

    def len2(self) -> float:
        'float len2()'
        _unavailable('fontgate.fgPointU.len2')

    def normal(self) -> fgPoint:
        'fgPoint normal()'
        _unavailable('fontgate.fgPointU.normal')

    def rotate(self, v: fgPointU, c: fgPoint) -> fgPoint:
        'fgPoint rotate(fgPointU v, fgPoint c)'
        _unavailable('fontgate.fgPointU.rotate')

    def round(self, *args: Any, **kwargs: Any) -> Any:
        'fgPoint round([doRound=true])'
        _unavailable('fontgate.fgPointU.round')

    def rx(self) -> int:
        'int rx() - integer rounded'
        _unavailable('fontgate.fgPointU.rx')

    def ry(self) -> int:
        'int ry() - integer rounded'
        _unavailable('fontgate.fgPointU.ry')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix)'
        _unavailable('fontgate.fgPointU.transform')

    def transformed(self, arg0: fgMatrix) -> fgPoint:
        'fgPoint transformed(fgMatrix)'
        _unavailable('fontgate.fgPointU.transformed')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'float value([horizontal=true])'
        _unavailable('fontgate.fgPointU.value')

    def zero(self) -> bool:
        'bool zero()'
        _unavailable('fontgate.fgPointU.zero')

    u: Any
    '(float)'
    x: Any
    '(float)'
    y: Any
    '(float)'

class fgRect:
    'Rectangle representation\n\nConstructors:\n  fgRect() - default\n  fgRect(fgRect) - copy\n  fgRect(fgPoint, fgPoint)\n  fgRect(fgPoint, fgPoint, bool empty)\n  fgRect(float x1, float y1, float x2, float y2)\n\nMath Operations:\n  fgRect + fgPoint\n  fgRect + fgRect\n  fgRect + float\n  fgRect - fgPoint\n  fgRect - fgRect\n  fgRect - float\n  fgRect * float\n  fgRect / float\n  fgRect & fgRect\n  fgRect | fgRect\n\nNative bases: object\n\nCaptured native MRO: fgRect, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgRect.__init__')

    def adjust(self, x1: float, y1: float, x2: float, y2: float) -> Any:
        'adjust(float x1, float y1, float x2, float y2)'
        _unavailable('fontgate.fgRect.adjust')

    def adjusted(self, x1: float, y1: float, x2: float, y2: float) -> fgRect:
        'fgRect adjusted(float x1, float y1, float x2, float y2)'
        _unavailable('fontgate.fgRect.adjusted')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent Py::Object as dictionary'
        _unavailable('fontgate.fgRect.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent Py::Object as tuple'
        _unavailable('fontgate.fgRect.asTuple')

    def assign(self, arg0: float, arg1: float, arg2: float, fix: Any = ...) -> Any:
        'assign(fgPoint, fgPoint[, fix=true]) or assign(float, float, float, float[, fix=true])'
        _unavailable('fontgate.fgRect.assign')

    def bottom(self) -> float:
        'float bottom()'
        _unavailable('fontgate.fgRect.bottom')

    def center(self) -> fgPoint:
        'fgPoint center()'
        _unavailable('fontgate.fgRect.center')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontgate.fgRect.clear')

    def contains(self, *args: Any, **kwargs: Any) -> Any:
        'bool contains(fgPoint) or bool contains(fgRect)'
        _unavailable('fontgate.fgRect.contains')

    def containsX(self, arg0: float) -> bool:
        'bool containsX(float)'
        _unavailable('fontgate.fgRect.containsX')

    def containsY(self, arg0: float) -> bool:
        'bool containsY(float)'
        _unavailable('fontgate.fgRect.containsY')

    def diagonal(self) -> float:
        'float diagonal()'
        _unavailable('fontgate.fgRect.diagonal')

    def empty(self) -> Any:
        'empty()'
        _unavailable('fontgate.fgRect.empty')

    def fix(self) -> Any:
        'fix()'
        _unavailable('fontgate.fgRect.fix')

    def fix_x(self) -> Any:
        'fix_x()'
        _unavailable('fontgate.fgRect.fix_x')

    def fix_y(self) -> Any:
        'fix_y()'
        _unavailable('fontgate.fgRect.fix_y')

    def height(self) -> float:
        'float height()'
        _unavailable('fontgate.fgRect.height')

    def intersects(self, arg0: fgRect) -> bool:
        'bool intersects(fgRect)'
        _unavailable('fontgate.fgRect.intersects')

    def left(self) -> float:
        'float left()'
        _unavailable('fontgate.fgRect.left')

    def move(self, dx: float, dy: float) -> Any:
        'move(float dx, float dy)'
        _unavailable('fontgate.fgRect.move')

    def moved(self, dx: float, dy: float) -> fgRect:
        'fgRect moved(float dx, float dy)'
        _unavailable('fontgate.fgRect.moved')

    def right(self) -> float:
        'float right()'
        _unavailable('fontgate.fgRect.right')

    def setBottom(self, arg0: float) -> Any:
        'setBottom(float)'
        _unavailable('fontgate.fgRect.setBottom')

    def setHeight(self, arg0: float) -> Any:
        'setHeight(float)'
        _unavailable('fontgate.fgRect.setHeight')

    def setLeft(self, arg0: float) -> Any:
        'setLeft(float)'
        _unavailable('fontgate.fgRect.setLeft')

    def setRect(self, x: int, y: int, w: int, h: int) -> Any:
        'setRect(int x, int y, int w, int h)'
        _unavailable('fontgate.fgRect.setRect')

    def setRight(self, arg0: float) -> Any:
        'setRight(float)'
        _unavailable('fontgate.fgRect.setRight')

    def setSize(self, arg0: fgPoint) -> Any:
        'setSize(fgPoint)'
        _unavailable('fontgate.fgRect.setSize')

    def setTop(self, arg0: float) -> Any:
        'setTop(float)'
        _unavailable('fontgate.fgRect.setTop')

    def setWidth(self, arg0: float) -> Any:
        'setWidth(float)'
        _unavailable('fontgate.fgRect.setWidth')

    def size(self) -> fgPoint:
        'fgPoint size()'
        _unavailable('fontgate.fgRect.size')

    def top(self) -> float:
        'float top()'
        _unavailable('fontgate.fgRect.top')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix)'
        _unavailable('fontgate.fgRect.transform')

    def transformed(self, arg0: fgMatrix) -> fgRect:
        'fgRect transformed(fgMatrix)'
        _unavailable('fontgate.fgRect.transformed')

    def width(self) -> float:
        'float width()'
        _unavailable('fontgate.fgRect.width')

    def zero(self) -> Any:
        'zero()'
        _unavailable('fontgate.fgRect.zero')

    _empty: Any
    '(bool) True if Rect is empty'
    ll: Any
    '(fgPoint) lower left point'
    ur: Any
    '(fgPoint) upper right point'

class fgRendered:
    'fgRendered representation\n\nNative bases: object\n\nCaptured native MRO: fgRendered, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgRendered.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgRendered.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgRendered.asTuple')

    bitmap: Any
    metrics: Any
    position: Any
    ppm: Any

class fgShape:
    'Shape representation\n\nConstructors:\n  fgShape() - default\n  fgShape(fgShape) - copy\n  fgShape(fgShape, fgShape, float tx, float ty)\n  fgShape(fgShape, fgShape, float tx, float ty, int blend_mode)\n\nMath Operations:\n  fgShape + fgShape\n  fgShape - fgShape\n  fgShape * float\n\nNative bases: object\n\nCaptured native MRO: fgShape, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgShape.__init__')

    def addContour(self, arg0: fgContour) -> fgContour:
        'fgContour addContour(fgContour)'
        _unavailable('fontgate.fgShape.addContour')

    def addShape(self, *args: Any, **kwargs: Any) -> Any:
        'int addShape(fgShape, int mode) ???'
        _unavailable('fontgate.fgShape.addShape')

    def applyTransform(self) -> Any:
        'applyTransform()'
        _unavailable('fontgate.fgShape.applyTransform')

    def area(self) -> float:
        'float area()'
        _unavailable('fontgate.fgShape.area')

    def assignStyle(self, arg0: fgShape) -> Any:
        'assignStyle(fgShape)'
        _unavailable('fontgate.fgShape.assignStyle')

    def autoInterpolated(self) -> bool:
        'bool autoInterpolated()'
        _unavailable('fontgate.fgShape.autoInterpolated')

    def autoSmooth(self) -> bool:
        'bool autoSmooth()'
        _unavailable('fontgate.fgShape.autoSmooth')

    def boundingBox(self, prepareExport: Any = ...) -> Any:
        'fgRect/Nothing boundingBox(fgMatrix[, bool prepareExport=false])'
        _unavailable('fontgate.fgShape.boundingBox')

    def checkContours(self) -> Any:
        'checkContours()'
        _unavailable('fontgate.fgShape.checkContours')

    def containsOffPoint(self) -> bool:
        'bool containsOffPoint()'
        _unavailable('fontgate.fgShape.containsOffPoint')

    def countContours(self) -> int:
        'int countContours()'
        _unavailable('fontgate.fgShape.countContours')

    def countNodes(self) -> int:
        'int countNodes()'
        _unavailable('fontgate.fgShape.countNodes')

    def excludeShape(self, *args: Any, **kwargs: Any) -> Any:
        'int excludeShape(fgShape, int mode) ???'
        _unavailable('fontgate.fgShape.excludeShape')

    def hasBody(self) -> bool:
        'bool hasBody()'
        _unavailable('fontgate.fgShape.hasBody')

    def hasContours(self) -> bool:
        'bool hasContours()'
        _unavailable('fontgate.fgShape.hasContours')

    def intersectShape(self, *args: Any, **kwargs: Any) -> Any:
        'int intersectShape(fgShape, int mode) ???'
        _unavailable('fontgate.fgShape.intersectShape')

    def isCompatible(self, arg0: fgShape) -> Any:
        'bool/Nothing isCompatible(fgShape)'
        _unavailable('fontgate.fgShape.isCompatible')

    def makeStroke(self, *args: Any, **kwargs: Any) -> Any:
        'fgShape/None makeStroke([cap0, cap1]); returns a detached filled outline'
        _unavailable('fontgate.fgShape.makeStroke')

    def removeOverlap(self) -> int:
        'int removeOverlap()'
        _unavailable('fontgate.fgShape.removeOverlap')

    def reverse(self) -> Any:
        'reverse()'
        _unavailable('fontgate.fgShape.reverse')

    def sortContours(self) -> Any:
        'sortContours()'
        _unavailable('fontgate.fgShape.sortContours')

    def subtractShape(self, *args: Any, **kwargs: Any) -> Any:
        'int subtractShape(fgShape, int mode) ???'
        _unavailable('fontgate.fgShape.subtractShape')

    def transform(self, arg0: fgMatrix) -> Any:
        'transform(fgMatrix)'
        _unavailable('fontgate.fgShape.transform')

    body: Any
    '(fgBrush)'
    contours: Any
    '(fgContours)'
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

class fgShapes:
    'list of fgShape objects\n\nNative bases: object\n\nCaptured native MRO: fgShapes, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgShapes.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgShapes.append; argument details are not documented.'
        _unavailable('fontgate.fgShapes.append')

    def asList(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgShapes.asList; argument details are not documented.'
        _unavailable('fontgate.fgShapes.asList')

    def clean(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgShapes.clean; argument details are not documented.'
        _unavailable('fontgate.fgShapes.clean')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgShapes.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgShapes.del')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgShapes.insert; argument details are not documented.'
        _unavailable('fontgate.fgShapes.insert')


class fgStem:
    'Stem representation\n\nConstructors:\n  fgStem() - default\n  fgStem(fgStem) - copy\n  fgStem(float)\n\nNative bases: object\n\nCaptured native MRO: fgStem, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgStem.__init__')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontgate.fgStem.clear')

    def fillProgram(self, upm: float) -> Any:
        'list(int) fillProgram(float upm)'
        _unavailable('fontgate.fgStem.fillProgram')

    def ppm(self, upm: float, k: int) -> int:
        'int ppm(float upm, int k)'
        _unavailable('fontgate.fgStem.ppm')

    def setProgram(self, k: int, ppm: int, keepValues: bool) -> Any:
        'setProgram(int k, int ppm, bool keepValues)'
        _unavailable('fontgate.fgStem.setProgram')

    name: Any
    '(string)'
    program: Any
    '( dict(int:int) )'
    value: Any
    '(float)'

class fgStems:
    'list of fgStem objects\n\nNative bases: object\n\nCaptured native MRO: fgStems, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgStems.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgStems.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgStems.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgStems.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgStems.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgStems.insert')


class fgStringDict:
    'string dictionary\n\nNative bases: object\n\nCaptured native MRO: fgStringDict, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgStringDict.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgStringDict.asDict; argument details are not documented.'
        _unavailable('fontgate.fgStringDict.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgStringDict.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgStringDict.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgStringDict.has_key; argument details are not documented.'
        _unavailable('fontgate.fgStringDict.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgStringDict.keys; argument details are not documented.'
        _unavailable('fontgate.fgStringDict.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgStringDict.value; argument details are not documented.'
        _unavailable('fontgate.fgStringDict.value')


class fgTTInterpreter:
    'TTInterpreter representation\n\nConstructors:\n  fgTTInterpreter() - default\n  fgTTInterpreter(fgTTInterpreter) - copy\n\nNative bases: object\n\nCaptured native MRO: fgTTInterpreter, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgTTInterpreter.__init__')


class fgTrueTypeData:
    'TrueTypeData representation\n\nConstructors:\n  fgTrueTypeData() - default\n  fgTrueTypeData(fgTrueTypeData) - copy\n\nNative bases: object\n\nCaptured native MRO: fgTrueTypeData, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgTrueTypeData.__init__')

    def OK(self) -> bool:
        'bool OK() - return true if status is gdsOK'
        _unavailable('fontgate.fgTrueTypeData.OK')

    def bad(self) -> bool:
        "bool bad() - return true if status isn't gdsOK"
        _unavailable('fontgate.fgTrueTypeData.bad')

    def bottomSideBearing(self) -> int:
        'int bottomSideBearing()'
        _unavailable('fontgate.fgTrueTypeData.bottomSideBearing')

    def boundingBox(self, arg0: fgGlyphsR, arg1: fgMatrix, prepareExport: bool) -> fgRect:
        'fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box'
        _unavailable('fontgate.fgTrueTypeData.boundingBox')

    def clearImports(self) -> Any:
        'clearImports() - clear instructions and hdmx, set yPels = 1'
        _unavailable('fontgate.fgTrueTypeData.clearImports')

    def copy(self) -> fgTrueTypeData:
        'fgTrueTypeData copy() - create alone copy of data'
        _unavailable('fontgate.fgTrueTypeData.copy')

    def countPictures(self) -> int:
        'int countPictures() - return pictures count'
        _unavailable('fontgate.fgTrueTypeData.countPictures')

    def empty(self) -> bool:
        'bool empty() - return true if state == sEmpty or no endpoints present'
        _unavailable('fontgate.fgTrueTypeData.empty')

    def getFontGateData(self) -> fgFontGateData:
        'fgFontGateData getFontGateData() - return Nothing'
        _unavailable('fontgate.fgTrueTypeData.getFontGateData')

    def getType(self) -> Any:
        "string getType() - return 'dtTrueType'"
        _unavailable('fontgate.fgTrueTypeData.getType')

    def hasBody(self, prepareExport: bool) -> bool:
        'bool hasBody(bool prepareExport) - return true if non-empty body layer is present'
        _unavailable('fontgate.fgTrueTypeData.hasBody')

    def hasColors(self) -> bool:
        'bool hasColors() - return true if colors is present'
        _unavailable('fontgate.fgTrueTypeData.hasColors')

    def hasHints(self) -> bool:
        'bool hasHints() - return true if hints is present'
        _unavailable('fontgate.fgTrueTypeData.hasHints')

    def hasPictures(self) -> bool:
        'bool hasPictures() - return true if pictures is present'
        _unavailable('fontgate.fgTrueTypeData.hasPictures')

    def modified(self) -> bool:
        'bool modified() - return true if data was changed'
        _unavailable('fontgate.fgTrueTypeData.modified')

    def rightSideBearing(self) -> int:
        'int rightSideBearing()'
        _unavailable('fontgate.fgTrueTypeData.rightSideBearing')

    def setParent(self, arg0: fgGlyph) -> Any:
        'setParent(fgGlyph) - set parent glyph'
        _unavailable('fontgate.fgTrueTypeData.setParent')

    def status(self) -> Any:
        "'gdsOK'/'gdsInvalid' status()"
        _unavailable('fontgate.fgTrueTypeData.status')

    def transform(self, arg0: fgMatrix, bool: Any) -> Any:
        'transform(fgMatrix, bool) - unsupported; raises NotImplementedError without changing data'
        _unavailable('fontgate.fgTrueTypeData.transform')

    def updateBoundingBox(self) -> Any:
        'updateBoundingBox()'
        _unavailable('fontgate.fgTrueTypeData.updateBoundingBox')

    def updated(self) -> Any:
        'updated() - mark data as changed, reset internal caches'
        _unavailable('fontgate.fgTrueTypeData.updated')

    def valid(self) -> bool:
        'bool valid() - return true if state == sValid | sDecomposed'
        _unavailable('fontgate.fgTrueTypeData.valid')

    def xExtent(self) -> int:
        'int xExtent()'
        _unavailable('fontgate.fgTrueTypeData.xExtent')

    def yExtent(self) -> int:
        'int yExtent()'
        _unavailable('fontgate.fgTrueTypeData.yExtent')

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
    'TrueType Point representation\n\nConstructors:\n  fgTrueTypePoint() - default\n  fgTrueTypePoint(fgTrueTypePoint) - copy\n  fgTrueTypePoint(fgPoint)\n  fgTrueTypePoint(bool on, int x, int y)\n\nNative bases: object\n\nCaptured native MRO: fgTrueTypePoint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgTrueTypePoint.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgTrueTypePoint.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgTrueTypePoint.asTuple')

    def assign(self, x: int, y: int) -> Any:
        'assign(int x, int y)'
        _unavailable('fontgate.fgTrueTypePoint.assign')

    def onCurve(self, value: Any) -> bool:
        'bool onCurve() or onCurve(bool value)'
        _unavailable('fontgate.fgTrueTypePoint.onCurve')

    def repeat(self, value: Any) -> bool:
        'bool repeat()  or repeat(bool value)'
        _unavailable('fontgate.fgTrueTypePoint.repeat')

    def touched(self, value: Any) -> bool:
        'bool touched() or touched(bool value)'
        _unavailable('fontgate.fgTrueTypePoint.touched')

    def xSame(self, value: Any) -> bool:
        'bool xSame()   or xSame(bool value)'
        _unavailable('fontgate.fgTrueTypePoint.xSame')

    def xShort(self, value: Any) -> bool:
        'bool xShort()  or xShort(bool value)'
        _unavailable('fontgate.fgTrueTypePoint.xShort')

    def ySame(self, value: Any) -> bool:
        'bool ySame()   or ySame(bool value)'
        _unavailable('fontgate.fgTrueTypePoint.ySame')

    def yShort(self, value: Any) -> bool:
        'bool yShort()  or yShort(bool value)'
        _unavailable('fontgate.fgTrueTypePoint.yShort')

    flag: Any
    '(int)'
    x: Any
    '(int)'
    y: Any
    '(int)'

class fgTrueTypePoints:
    'list of fgTrueTypePoint objects\n\nNative bases: object\n\nCaptured native MRO: fgTrueTypePoints, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgTrueTypePoints.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgTrueTypePoints.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgTrueTypePoints.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgTrueTypePoints.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgTrueTypePoints.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgTrueTypePoints.insert')


class fgValuesDict:
    'float values dictionary\n\nNative bases: object\n\nCaptured native MRO: fgValuesDict, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgValuesDict.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgValuesDict.asDict; argument details are not documented.'
        _unavailable('fontgate.fgValuesDict.asDict')

    def del_(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgValuesDict.del; argument details are not documented.\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgValuesDict.del')

    def has_key(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgValuesDict.has_key; argument details are not documented.'
        _unavailable('fontgate.fgValuesDict.has_key')

    def keys(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgValuesDict.keys; argument details are not documented.'
        _unavailable('fontgate.fgValuesDict.keys')

    def value(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontgate.fgValuesDict.value; argument details are not documented.'
        _unavailable('fontgate.fgValuesDict.value')


class fgVdmxRecord:
    'fgVdmxRecord representation\n\nNative bases: object\n\nCaptured native MRO: fgVdmxRecord, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVdmxRecord.__init__')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgVdmxRecord.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgVdmxRecord.asTuple')

    yMax: Any
    yMin: Any
    yPelHeight: Any

class fgVdmxRecords:
    'list of fgVdmxRecord objects\n\nNative bases: object\n\nCaptured native MRO: fgVdmxRecords, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVdmxRecords.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVdmxRecords.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVdmxRecords.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVdmxRecords.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVdmxRecords.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVdmxRecords.insert')


class fgVector:
    'Vector representation\n\nConstructors:\n  fgVector() - default\n  fgVector(fgVector) - copy\n  fgVector(fgPoint q0[, fgPoint q1]) - from one or two points\n  fgVector(fgPoint, float l, float a)\n\nNative bases: object\n\nCaptured native MRO: fgVector, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVector.__init__')

    def angle(self) -> float:
        'float angle()'
        _unavailable('fontgate.fgVector.angle')

    def angleTo(self, arg0: fgVector) -> float:
        'float angleTo(fgVector)'
        _unavailable('fontgate.fgVector.angleTo')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontgate.fgVector.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontgate.fgVector.asTuple')

    def bbox(self) -> fgRect:
        'fgRect bbox()'
        _unavailable('fontgate.fgVector.bbox')

    def center(self) -> fgPoint:
        'fgPoint center()'
        _unavailable('fontgate.fgVector.center')

    def delta(self) -> fgPoint:
        'fgPoint delta()'
        _unavailable('fontgate.fgVector.delta')

    def direction(self) -> fgPoint:
        'fgPoint direction()'
        _unavailable('fontgate.fgVector.direction')

    def equivalent(self, arg0: fgVector) -> bool:
        'bool equivalent(fgVector)'
        _unavailable('fontgate.fgVector.equivalent')

    def intersect(self, *args: Any, **kwargs: Any) -> Any:
        'fgPoint/None intersect(fgVector) or (fgPoint, t)/None intersect(fgVector, bool get_t)'
        _unavailable('fontgate.fgVector.intersect')

    def intersectY(self, pos: float) -> Any:
        'float/None intersectY(float pos)'
        _unavailable('fontgate.fgVector.intersectY')

    def len(self) -> float:
        'float len() - distance between q0 and q1'
        _unavailable('fontgate.fgVector.len')

    def parallel(self, arg0: fgVector) -> bool:
        'bool parallel(fgVector)'
        _unavailable('fontgate.fgVector.parallel')

    def point(self, time: float) -> fgPoint:
        'fgPoint point(float time)'
        _unavailable('fontgate.fgVector.point')

    def time(self, arg0: fgPoint) -> float:
        'float time(fgPoint)'
        _unavailable('fontgate.fgVector.time')

    q0: Any
    '(fgPoint)'
    q1: Any
    '(fgPoint)'

class fgVectorBool:
    '[char] vector\n\nNative bases: object\n\nCaptured native MRO: fgVectorBool, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVectorBool.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVectorBool.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVectorBool.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVectorBool.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVectorBool.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVectorBool.insert')


class fgVectorChar:
    '[char] vector\n\nNative bases: object\n\nCaptured native MRO: fgVectorChar, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVectorChar.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVectorChar.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVectorChar.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVectorChar.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVectorChar.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVectorChar.insert')


class fgVectorDouble:
    '[double] vector\n\nNative bases: object\n\nCaptured native MRO: fgVectorDouble, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVectorDouble.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVectorDouble.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVectorDouble.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVectorDouble.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVectorDouble.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVectorDouble.insert')


class fgVectorInt:
    '[int] vector\n\nNative bases: object\n\nCaptured native MRO: fgVectorInt, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVectorInt.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVectorInt.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVectorInt.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVectorInt.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVectorInt.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVectorInt.insert')


class fgVectorPoint:
    '[fgPoint] vector\n\nNative bases: object\n\nCaptured native MRO: fgVectorPoint, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVectorPoint.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVectorPoint.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVectorPoint.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVectorPoint.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVectorPoint.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVectorPoint.insert')


class fgVectorUInt16:
    '[uint16_t] vector\n\nNative bases: object\n\nCaptured native MRO: fgVectorUInt16, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVectorUInt16.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVectorUInt16.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVectorUInt16.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVectorUInt16.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVectorUInt16.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVectorUInt16.insert')


class fgVectorUInt32:
    '[uint32t] vector\n\nNative bases: object\n\nCaptured native MRO: fgVectorUInt32, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgVectorUInt32.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgVectorUInt32.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgVectorUInt32.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgVectorUInt32.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgVectorUInt32.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgVectorUInt32.insert')


class fgZone:
    'Zone representation\n\nConstructors:\n  fgZone() - default\n  fgZone(fgZone) - copy\n\nNative bases: object\n\nCaptured native MRO: fgZone, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgZone.__init__')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontgate.fgZone.clear')

    def getIntValues(self) -> Any:
        'tuple( int y0, int y1 ) getIntValues()'
        _unavailable('fontgate.fgZone.getIntValues')

    def v0(self) -> float:
        'float v0()'
        _unavailable('fontgate.fgZone.v0')

    def v1(self) -> float:
        'float v1()'
        _unavailable('fontgate.fgZone.v1')

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
    'list of fgZone objects\n\nNative bases: object\n\nCaptured native MRO: fgZones, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.fgZones.__init__')

    def append(self, *args: Any, **kwargs: Any) -> Any:
        'append(item) or append( list(item) ) - add items to the end of the list'
        _unavailable('fontgate.fgZones.append')

    def asList(self) -> Any:
        'list(items) asList() - get items as list'
        _unavailable('fontgate.fgZones.asList')

    def clean(self) -> Any:
        'clean() - delete all items'
        _unavailable('fontgate.fgZones.clean')

    def del_(self, index: Any) -> Any:
        'del(index) - delete item by index\n\nNative spelling: del; access it through getattr on the native object.'
        _unavailable('fontgate.fgZones.del')

    def insert(self, position: Any, item: Any) -> Any:
        'insert(position, item) - insert item into list at specified position'
        _unavailable('fontgate.fgZones.insert')


class pyfgDataOwnerData:
    'pyfgDataOwnerData objects\n\nNative bases: object\n\nCaptured native MRO: pyfgDataOwnerData, object\n\nNative __new__ allocation evidence (not an __init__ overload):\n(*args, **kwargs)\nCreate and return a new object.  See help(type) for accurate signature.'
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        'Initialize self.  See help(type(self)) for accurate signature.'
        _unavailable('fontgate.pyfgDataOwnerData.__init__')


fgCURVE: int
fgLINE: int
fgMOVE: int
fgOFFCURVE: int
options: fgOptions

__echopy_source_aliases__ = {}
__all__ = ['fgAnchor', 'fgAnchors', 'fgAxes', 'fgAxis', 'fgBitmap', 'fgBitmaps', 'fgBitmapsData', 'fgBrush', 'fgCMaps', 'fgCURVE', 'fgCapParams', 'fgCaret', 'fgCarets', 'fgCmapRecord', 'fgCoding', 'fgColor', 'fgComponent', 'fgComponents', 'fgContour', 'fgContours', 'fgCurve', 'fgCuspPoint', 'fgCuspPoints', 'fgDesignPosition', 'fgDeviceRecord', 'fgDeviceRecords', 'fgExtMapIntTofgShape', 'fgExtMapUCharToUChar', 'fgExtMapUIntToString', 'fgExtMapUShortToShort', 'fgFlagsDict', 'fgFont', 'fgFontGateData', 'fgFontHinting', 'fgFontInfo', 'fgFontInfoDict', 'fgGaspRecord', 'fgGaspRecords', 'fgGlyph', 'fgGlyphData', 'fgGlyphDict', 'fgGlyphIDsSet', 'fgGlyphs', 'fgGlyphsR', 'fgGroup', 'fgGroups', 'fgGuide', 'fgGuides', 'fgHint', 'fgHintCommand', 'fgHintCommands', 'fgHints', 'fgIntDict', 'fgKerning', 'fgKerningGroups', 'fgKerningObject', 'fgKerningObjectPair', 'fgLINE', 'fgLayer', 'fgLayers', 'fgLib', 'fgMOVE', 'fgMapBytes', 'fgMaster', 'fgMasters', 'fgMatrix', 'fgMaxP', 'fgMetricsClass', 'fgMetricsClasses', 'fgNametable', 'fgNode', 'fgNodes', 'fgOFFCURVE', 'fgOTLayout', 'fgOpt_AutoMetrics', 'fgOpt_EOTExport', 'fgOpt_ExpandKerning', 'fgOpt_Font', 'fgOpt_KerningOptions', 'fgOpt_OTExport', 'fgOpt_OTExportFeaFile', 'fgOpt_OTImport', 'fgOpt_Optimize', 'fgOpt_T1Autohint', 'fgOpt_T1Export', 'fgOpt_T1Import', 'fgOpt_TTAutohint', 'fgOpt_TTFAutohint', 'fgOpt_UfoFontExport', 'fgOpt_UfoFontImport', 'fgOpt_VfbExport', 'fgOpt_VfbImport', 'fgOpt_WOFFExport', 'fgOptions', 'fgOtInfo', 'fgOtValue', 'fgPackages', 'fgPen', 'fgPoint', 'fgPointU', 'fgRect', 'fgRendered', 'fgShape', 'fgShapes', 'fgStem', 'fgStems', 'fgStringDict', 'fgTTInterpreter', 'fgTrueTypeData', 'fgTrueTypePoint', 'fgTrueTypePoints', 'fgValuesDict', 'fgVdmxRecord', 'fgVdmxRecords', 'fgVector', 'fgVectorBool', 'fgVectorChar', 'fgVectorDouble', 'fgVectorInt', 'fgVectorPoint', 'fgVectorUInt16', 'fgVectorUInt32', 'fgZone', 'fgZones', 'options', 'pyfgDataOwnerData']
_bind(globals(), 'fontgate', __echopy_source_aliases__)
