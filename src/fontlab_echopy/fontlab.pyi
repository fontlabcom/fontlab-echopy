# this_file: src/fontlab_echopy/fontlab.pyi
# Generated from native metadata and independent enrichment inputs.
"""Python interface for FontLab data objects

CurveEx: CurveEx representation
ExportControl: ExportControl representation
FaBasicPtr: FaBasicPtr representation
Interval: Interval representation
PaintBrush: PaintBrush representation
TransformFrame: TransformFrame representation
fgSymbol: fgSymbol representation
fgSymbolList: fgSymbolList representation
flAbstractEditor: flAbstractEditor representation
flAbstractVectorNode: flAbstractVectorNode representation
flAnchor: flAnchor representation
flAuditInfo: flAuditInfo representation
flAxis: flAxis representation
flBasicTool: flBasicTool representation
flCanvas: flCanvas representation
flContour: flContour representation
flContourInfo: flContourInfo representation
flEvent: flEvent representation
flExpression: flExpression representation
flGlyph: flGlyph representation
flGlyphInfo: flGlyphInfo representation
flGraphicsInfo: flGraphicsInfo representation
flGuideLine: flGuideLine representation
flHintingParameters: flHintingParameters representation
flInstance: flInstance representation
flItems: flItems representation
flLayer: flLayer representation
flLayerInfo: flLayerInfo representation
flLocation: flLocation representation
LocationValue: LocationValue representation
flMarkerPoint: flMarkerPoint representation
flMouseEvent: flMouseEvent representation
flModelProducer: flModelProducer representation
flNode: flNode representation
flNodeInfo: flNodeInfo representation
flObject: flObject representation
flPackage: flPackage representation
flPaper: flPaper representation
flPinPoint: flPinPoint representation
flPreferences: flPreferences representation
flProperty: flProperty representation
flPropertyDouble: flPropertyDouble representation
flPropertyPoint: flPropertyPoint representation
flSearchInfo: flSearchInfo representation
flShape: flShape representation
flShapeBuilder: flShapeBuilder representation
flShapeData: flShapeData representation
flShapeInfo: flShapeInfo representation
flSnapLine: flSnapLine representation
flSnapObject: flSnapObject representation
flStem: flStem representation
flZone: flZone representation
flSticker: flSticker representation
flTextBlock: flTextBlock representation
flTransform: flTransform representation
flVectorNode: flVectorNode representation
flVisualItem: flVisualItem representation
flWorkspace: flWorkspace representation
FontMetrics: FontMetrics representation
GlyphComponent: GlyphComponent representation
flTTHCommand: flTTHCommand representation
YPanelManager: YPanelManager representation
YPanelWidget: YPanelWidget representation
Info: Font Info data
FontLayer: FontLayer object
flObjectsList<flGuideLine>: flObjectsList<flGuideLine> doc
flObjectsList<flShape>: flObjectsList<flShape> doc
flSnaps: snap object constants
flModel: flModel representation
PaintBrushShape: Data wrapper
SmartCornerParameters: Data wrapper
AccentInfo: Data wrapper
flLayerAttributes: Data wrapper

Supplemental documentation:
High-level FontLab editing API. flGlyph contains drawing layers, flLayer contains shapes, and flContour contains nodes. CurrentFont() and CurrentGlyph() access the active editing context."""
from __future__ import annotations
from typing import Any

class AccentInfo:
    """Data wrapper

Native bases: object

Supplemental documentation:
A data wrapper with the attributes `layer` and `offset`. The captured declaration exposes `asDict` (represent the object as a dictionary) and `asTuple` (represent it as a tuple).

Source: generated/fontlab.py: AccentInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    layer: Any
    offset: Any

class CurveEx:
    """CurveEx representation

Constructors:
  CurveEx() - default
  CurveEx(QPointF p0, QPointF p1[, int leftIdx=0[, int _rightIdx=0]])
  CurveEx(QPointF p0, QPointF p1, QPointF p2, QPointF p3)
  CurveEx( list(QPointF) )

Native bases: object

Supplemental documentation:
A curve segment record. The captured declaration exposes the end points `p0` and `p1`, the control points `bcp0` and `bcp1`, the control vectors `bcv0` and `bcv1`, the bounding rectangle `brect`, and the index attributes `leftIdx`, `rightIdx` and `contourIx`. Captured methods include `split`, `extremum`, `smooth`, `improve`, `fastLength` and `applyTransform`. Consult the retained constructor documentation for the supported point-based creation forms.

Source: generated/fontlab.py: CurveEx captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def applyTransform(self, tx: QTransform) -> None:
        """void applyTransform(QTransform& tx)"""
        ...

    def empty(self) -> bool:
        """bool empty()"""
        ...

    def extremum(self, prev: Any) -> bool:
        """bool extremum(CurveEx prev)"""
        ...

    def fastLength(self) -> float:
        """double fastLength()"""
        ...

    def improve(self, curvature: Any=...) -> bool:
        """bool improve([double curvature = 1.0])"""
        ...

    def smooth(self, prev: Any) -> bool:
        """bool smooth(CurveEx prev)"""
        ...

    def smoothCurvature(self, c1: Any, complete: bool) -> Any:
        """CurveEx smoothCurvature(CurveEx c1, bool complete)"""
        ...

    def split(self, *args: Any, **kwargs: Any) -> Any:
        """bool split(CurveEx, CurveEx)"""
        ...

    def updateBRect(self) -> None:
        """void updateBRect()"""
        ...
    bcp0: Any
    'QPointF bcp0'
    bcp1: Any
    'QPointF bcp1'
    bcv0: Any
    'QPointF bcv0'
    bcv1: Any
    'QPointF bcv1'
    brect: Any
    'QRectF'
    contourIx: Any
    'int'
    countPoints: Any
    'int'
    leftIdx: Any
    'int'
    p0: Any
    'QPointF p0'
    p1: Any
    'QPointF p1'
    paramT: Any
    'int'
    rightIdx: Any
    'int'

class ExportControl:
    """ExportControl representation

Constructors:

Native bases: object

Supplemental documentation:
An export control record. The captured declaration exposes the attributes `conflictMode`, `contentMode`, `contentName`, `destinationFolder`, `destinationMode`, `groupFamily`, `groupProfiles`, `profileId` and `profileName`, and the methods `init`, `load` and `store`. `load` returns a bool.

Source: generated/fontlab.py: ExportControl captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def init(self) -> Any:
        """init()"""
        ...

    def load(self) -> bool:
        """bool load()"""
        ...

    def store(self) -> Any:
        """store()"""
        ...
    conflictMode: Any
    'int'
    contentMode: Any
    'int'
    contentName: Any
    'string contentName'
    destinationFolder: Any
    'string'
    destinationMode: Any
    'int'
    groupFamily: Any
    'bool'
    groupProfiles: Any
    'bool'
    profileId: Any
    'int'
    profileName: Any
    'string'

class FaBasicPtr:
    """FaBasicPtr representation

Constructors:

Native bases: object

Supplemental documentation:
A fix-pointer record. The captured declaration exposes the method `fix` and the attributes `canBeFixed`, `contour`, `id`, `location`, `nodeIndex`, `priority`, `report`, `title` and `vector`. Test `canBeFixed` before calling `fix`; the captured `fix` is declared as returning an flGlyph or nothing.

Source: generated/fontlab.py: FaBasicPtr captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def fix(self) -> Any:
        """flGlyph/Nothing fix()"""
        ...
    canBeFixed: Any
    'bool     '
    contour: Any
    'flContour'
    id: Any
    'int      '
    location: Any
    'QPointF  '
    nodeIndex: Any
    'int      '
    priority: Any
    'int      '
    report: Any
    'QString  '
    title: Any
    'QString  '
    vector: Any
    'QPointF  '

class FontLayer:
    """FontLayer object

Native bases: object

Supplemental documentation:
A font layer object. The captured declaration exposes no named members, only a native constructor. Do not rely on any attribute of `FontLayer`; glyph layers belong to flLayer.

Source: generated/fontlab.py: FontLayer captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

class FontMetrics:
    """FontMetrics representation

Constructors:
  FontMetrics() - default
  FontMetrics(FontMetrics)
  FontMetrics(double upm)
  FontMetrics(fg::Package *p)
  FontMetrics(flPackage p, string layer_name)

Native bases: object

Supplemental documentation:
Vertical metrics record for a font. The captured declaration exposes `upm`, `ascender`, `descender`, `lineGap`, `capsHeight` and `xHeight` as numeric (double) attributes, and `init` for initialisation. Consult the retained constructor documentation for the supported creation forms, which take a units-per-em value, an existing record, or a package with a layer name.

Source: generated/fontlab.py: FontMetrics captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def init(self) -> Any:
        """init()"""
        ...
    ascender: Any
    'double'
    capsHeight: Any
    'double'
    descender: Any
    'double'
    lineGap: Any
    'double'
    upm: Any
    'double'
    xHeight: Any
    'double'

class GlyphComponent:
    """GlyphComponent representation

Constructors:
  GlyphComponent() - default
  GlyphComponent(GlyphComponent)
  GlyphComponent(uint id)
  GlyphComponent(string name)
  GlyphComponent(uint id, QTransform tx, double w, bool ua)

Native bases: object

Supplemental documentation:
A glyph component described by `name_id` (uint), `transform` (QTransform), `use_anchors` (bool) and `width_scale` (double). It is created as `GlyphComponent()`, as a copy `GlyphComponent(GlyphComponent)`, from an id `GlyphComponent(uint id)`, from a name `GlyphComponent(string name)` or as `GlyphComponent(uint id, QTransform tx, double w, bool ua)`.

Source: generated/fontlab.py: GlyphComponent captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    name_id: Any
    'uint'
    transform: Any
    'QTransform'
    use_anchors: Any
    'bool'
    width_scale: Any
    'double'

class Info:
    """Font Info data

Native bases: object

Supplemental documentation:
Font info. The captured declaration exposes `ascender`, `capHeight`, `copyright`, `descender`, `familyName`, `italicAngle`, `note`, `openTypeHeadCreated`, `openTypeHheaAscender`, `openTypeHheaDescender`, `openTypeHheaLineGap`, `openTypeNameDesigner`, `openTypeNameLicense`, `openTypeNameVersion` and `openTypeOS2Panose`. It is created with no captured constructor overloads.

Source: generated/fontlab.py: Info captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    ascender: Any
    'Ascender value. This should be a integer or float'
    capHeight: Any
    'Cap height value. This should be a integer or float'
    copyright: Any
    'Copyright statement. This should be a string'
    descender: Any
    'Descender value. This should be a integer or float'
    familyName: Any
    'Family name. This should be a string'
    italicAngle: Any
    'Italic angle. This must be an angle in counter-clockwise degrees from the vertical. This should be a integer or float'
    macintoshFONDFamilyID: Any
    'Family ID number. Corresponds to the ffFamID in the FOND resource. This should be a integer'
    macintoshFONDName: Any
    'Font name for the FOND resource. This should be a string'
    note: Any
    'Arbitrary note about the font. This should be a string'
    openTypeGaspRangeRecords: Any
    'A list of gasp Range Records. These must be sorted in ascending order based on the rangeMaxPPEM value of the record. This should be a list'
    openTypeHeadCreated: Any
    'Creation date. Expressed as a string of the format "YYYY/MM/DD HH:MM:SS". "YYYY/MM/DD" is year/month/day. The month must be in the range 1-12 and the day must be in the range 1-end of month. "HH:MM:SS" is hour:minute:second. The hour must be in the range 0:23. The minute and second must each be in the range 0-59. This should be a string'
    openTypeHeadFlags: Any
    'A list of bit numbers indicating the flags. The bit numbers are listed in the OpenType head specification. Corresponds to the OpenType head table flags field. This should be a list'
    openTypeHeadLowestRecPPEM: Any
    'Smallest readable size in pixels. Corresponds to the OpenType head table lowestRecPPEM field. This should be a non-negative integer'
    openTypeHheaAscender: Any
    'Ascender value. Corresponds to the OpenType hhea table Ascender field. This should be a integer'
    openTypeHheaCaretOffset: Any
    'Caret offset value. Corresponds to the OpenType hhea table caretOffset field. This should be a integer'
    openTypeHheaCaretSlopeRise: Any
    'Caret slope rise value. Corresponds to the OpenType hhea table caretSlopeRise field. This should be a integer'
    openTypeHheaCaretSlopeRun: Any
    'Caret slope run value. Corresponds to the OpenType hhea table caretSlopeRun field. This should be a integer'
    openTypeHheaDescender: Any
    'Descender value. Corresponds to the OpenType hhea table Descender field. This should be a integer'
    openTypeHheaLineGap: Any
    'Line gap value. Corresponds to the OpenType hhea table LineGap field. This should be a integer'
    openTypeNameCompatibleFullName: Any
    'Compatible full name. Corresponds to the OpenType name table name ID 18. This should be a string'
    openTypeNameDescription: Any
    'Description of the font. Corresponds to the OpenType name table name ID 10. This should be a string'
    openTypeNameDesigner: Any
    'Designer name. Corresponds to the OpenType name table name ID 9. This should be a string'
    openTypeNameDesignerURL: Any
    'URL for the designer. Corresponds to the OpenType name table name ID 12. This should be a string'
    openTypeNameLicense: Any
    'License text. Corresponds to the OpenType name table name ID 13. This should be a string'
    openTypeNameLicenseURL: Any
    'URL for the license. Corresponds to the OpenType name table name ID 14. This should be a string'
    openTypeNameManufacturer: Any
    'Manufacturer name. Corresponds to the OpenType name table name ID 8. This should be a string'
    openTypeNameManufacturerURL: Any
    'Manufacturer URL. Corresponds to the OpenType name table name ID 11. This should be a string'
    openTypeNamePreferredFamilyName: Any
    'Preferred family name. Corresponds to the OpenType name table name ID 16. This should be a string'
    openTypeNamePreferredSubfamilyName: Any
    'Preferred subfamily name. Corresponds to the OpenType name table name ID 17. This should be a string'
    openTypeNameRecords: Any
    'A list of name records. This name record storage area is intended for records that require platform, encoding and or language localization. This should be a list'
    openTypeNameSampleText: Any
    'Sample text. Corresponds to the OpenType name table name ID 19. This should be a string'
    openTypeNameUniqueID: Any
    'Unique ID string. Corresponds to the OpenType name table name ID 3. This should be a string'
    openTypeNameVersion: Any
    'Version string. Corresponds to the OpenType name table name ID 5. This should be a string'
    openTypeNameWWSFamilyName: Any
    'WWS family name. Corresponds to the OpenType name table name ID 21. This should be a string'
    openTypeNameWWSSubfamilyName: Any
    'WWS Subfamily name. Corresponds to the OpenType name table name ID 22. This should be a string'
    openTypeOS2CodePageRanges: Any
    'A list of bit numbers that are supported code page ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulCodePageRange1 and ulCodePageRange2 fields. This should be a list'
    openTypeOS2FamilyClass: Any
    'Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, must be in the range 0-14. The second number, representing the subclass, must be in the range 0-15. The numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table sFamilyClass field. This should be a list'
    openTypeOS2Panose: Any
    'The list must contain 10 non-negative integers that represent the setting for each category in the Panose specification. The integers correspond with the option numbers in each of the Panose categories. This corresponds to the OpenType OS/2 table Panose field. This should be a list'
    openTypeOS2Selection: Any
    'A list of bit numbers indicating the bits that should be set in fsSelection. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table selection field. Note: Bits 0 (italic), 5 (bold) and 6 (regular) must not be set here. These bits should be taken from the generic styleMapStyle attribute. This should be a list'
    openTypeOS2StrikeoutPosition: Any
    'Strikeout position. Corresponds to the OpenType OS/2 table yStrikeoutPosition field. This should be a integer'
    openTypeOS2StrikeoutSize: Any
    'Strikeout size. Corresponds to the OpenType OS/2 table yStrikeoutSize field. This should be a integer'
    openTypeOS2SubscriptXOffset: Any
    'Subscript x offset. Corresponds to the OpenType OS/2 table ySubscriptXOffset field. This should be a integer'
    openTypeOS2SubscriptXSize: Any
    'Subscript horizontal font size. Corresponds to the OpenType OS/2 table ySubscriptXSize field. This should be a integer'
    openTypeOS2SubscriptYOffset: Any
    'Subscript y offset. Corresponds to the OpenType OS/2 table ySubscriptYOffset field. This should be a integer'
    openTypeOS2SubscriptYSize: Any
    'Subscript vertical font size. Corresponds to the OpenType OS/2 table ySubscriptYSize field. This should be a integer'
    openTypeOS2SuperscriptXOffset: Any
    'Superscript x offset. Corresponds to the OpenType OS/2 table ySuperscriptXOffset field. This should be a integer'
    openTypeOS2SuperscriptXSize: Any
    'Superscript horizontal font size. Corresponds to the OpenType OS/2 table ySuperscriptXSize field. This should be a integer'
    openTypeOS2SuperscriptYOffset: Any
    'Superscript y offset. Corresponds to the OpenType OS/2 table ySuperscriptYOffset field. This should be a integer'
    openTypeOS2SuperscriptYSize: Any
    'Superscript vertical font size. Corresponds to the OpenType OS/2 table ySuperscriptYSize field. This should be a integer'
    openTypeOS2Type: Any
    'A list of bit numbers indicating the embedding type. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table fsType field. This should be a list'
    openTypeOS2TypoAscender: Any
    'Ascender value. Corresponds to the OpenType OS/2 table sTypoAscender field. This should be a integer'
    openTypeOS2TypoDescender: Any
    'Descender value. Corresponds to the OpenType OS/2 table sTypoDescender field. This should be a integer'
    openTypeOS2TypoLineGap: Any
    'Line gap value. Corresponds to the OpenType OS/2 table sTypoLineGap field. This should be a integer'
    openTypeOS2UnicodeRanges: Any
    'A list of bit numbers that are supported Unicode ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulUnicodeRange1, ulUnicodeRange2, ulUnicodeRange3 and ulUnicodeRange4 fields. This should be a list'
    openTypeOS2VendorID: Any
    'Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table achVendID field. This should be a string'
    openTypeOS2WeightClass: Any
    'Weight class value. Must be a non-negative integer. Corresponds to the OpenType OS/2 table usWeightClass field. This should be a integer'
    openTypeOS2WidthClass: Any
    'Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table usWidthClass field. This should be a integer'
    openTypeOS2WinAscent: Any
    'Ascender value. Corresponds to the OpenType OS/2 table usWinAscent field. This should be a non-negative integer'
    openTypeOS2WinDescent: Any
    'Descender value. Corresponds to the OpenType OS/2 table usWinDescent field. This should be a non-negative integer'
    openTypeVheaCaretOffset: Any
    'Caret offset value. Corresponds to the OpenType vhea table caretOffset field. This should be a integer'
    openTypeVheaCaretSlopeRise: Any
    'Caret slope rise value. Corresponds to the OpenType vhea table caretSlopeRise field. This should be a integer'
    openTypeVheaCaretSlopeRun: Any
    'Caret slope run value. Corresponds to the OpenType vhea table caretSlopeRun field. This should be a integer'
    openTypeVheaVertTypoAscender: Any
    'Ascender value. Corresponds to the OpenType vhea table vertTypoAscender field. This should be a integer'
    openTypeVheaVertTypoDescender: Any
    'Descender value. Corresponds to the OpenType vhea table vertTypoDescender field. This should be a integer'
    openTypeVheaVertTypoLineGap: Any
    'Line gap value. Corresponds to the OpenType vhea table vertTypoLineGap field. This should be a integer'
    panose: Any
    'PANOSE identification. Should be a string containing 10 space-separated numbers'
    postscriptBlueFuzz: Any
    'BlueFuzz value. This corresponds to the Type 1/CFF BlueFuzz field. This should be a integer or float'
    postscriptBlueScale: Any
    'BlueScale value. This corresponds to the Type 1/CFF BlueScale field. This should be a float'
    postscriptBlueShift: Any
    'BlueShift value. This corresponds to the Type 1/CFF BlueShift field. This should be a integer or float'
    postscriptBlueValues: Any
    'A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list'
    postscriptDefaultCharacter: Any
    'The name of the glyph that should be used as the default character in PFM files. This should be a string'
    postscriptDefaultWidthX: Any
    'Default width for glyphs. This should be a integer or float'
    postscriptFamilyBlues: Any
    'A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list'
    postscriptFamilyOtherBlues: Any
    'A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list'
    postscriptFontName: Any
    'Name to be used for the FontName field in Type 1/CFF table. This should be a string'
    postscriptForceBold: Any
    'Indicates how the Type 1/CFF ForceBold field should be set. This should be a boolean'
    postscriptFullName: Any
    'Name to be used for the FullName field in Type 1/CFF table. This should be a string'
    postscriptIsFixedPitch: Any
    'Indicates if the font is monospaced. An authoring tool could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF isFixedPitched field This should be a boolean'
    postscriptNominalWidthX: Any
    'Nominal width for glyphs. This should be a integer or float'
    postscriptOtherBlues: Any
    'A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list'
    postscriptStemSnapH: Any
    'List of horizontal stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapH field. This should be a list'
    postscriptStemSnapV: Any
    'List of vertical stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapV field. This should be a list'
    postscriptUnderlinePosition: Any
    'Underline position value. Corresponds to the Type 1/CFF/post table UnderlinePosition field. This should be a integer or float'
    postscriptUnderlineThickness: Any
    'Underline thickness value. Corresponds to the Type 1/CFF/post table UnderlineThickness field. This should be a integer or float'
    postscriptUniqueID: Any
    'A unique ID number as defined in the Type 1/CFF specification. This should be a integer'
    postscriptWeightName: Any
    'A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the openTypeOS2WeightClass value. This should be a string'
    postscriptWindowsCharacterSet: Any
    'The Windows character set. The values are defined below. This should be a integer'
    styleMapFamilyName: Any
    'Family name used for bold, italic and bold italic style mapping. This should be a string'
    styleMapStyleName: Any
    'Style map style. The possible values are regular, italic, bold and bold italic. These are case sensitive. This should be a string'
    styleName: Any
    'Style name. This should be a string'
    trademark: Any
    'Trademark statement. This should be a string'
    unitsPerEm: Any
    'Units per em. This should be a non-negative integer or float'
    versionMajor: Any
    'Major version. This should be a integer'
    versionMinor: Any
    'Minor version. This should be a non-negative integer'
    xHeight: Any
    'x-height value. This should be a integer or float'
    year: Any
    "The year the font was created. This attribute is deprecated as of version 2. It's presence should not be relied upon by authoring tools. However, it may occur in a font's info so authoring tools should preserve it if present. This should be a integer"

class Interval:
    """Interval representation

Constructors:

Native bases: object

Supplemental documentation:
A numeric interval with `t0` and `t1` (both double) and `d` and `key` attributes. The captured declaration exposes `isEmpty`, `middle`, `reversed`, `setT0T1`, `toAbsolute` and `toInterval`. Consult the retained constructor documentation for the supported creation forms.

Source: generated/fontlab.py: Interval captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def isEmpty(self) -> bool:
        """bool isEmpty()"""
        ...

    def middle(self) -> float:
        """double middle()"""
        ...

    def reversed(self) -> Any:
        """Interval reversed()"""
        ...

    def setT0T1(self, t0: float, t1: float) -> None:
        """void setT0T1(double t0, double t1)"""
        ...

    def toAbsolute(self, v: float) -> float:
        """double toAbsolute(double v)"""
        ...

    def toInterval(self, absv: float) -> float:
        """double toInterval(double absv)"""
        ...
    d: Any
    'double d'
    key: Any
    'uint key'
    t0: Any
    'double t0'
    t1: Any
    'double t1'

class LocationValue:
    """LocationValue representation

Constructors:
  LocationValue(flLocation)
  LocationValue(double)

Native bases: object

Supplemental documentation:
A location value, `LocationValue`. The captured declaration exposes no named members, only the native constructors `LocationValue(flLocation)` and `LocationValue(double)`.

Source: generated/fontlab.py: LocationValue captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

class PaintBrush:
    """PaintBrush representation

Constructors:

Native bases: object

Supplemental documentation:
A paint brush described by `angle`, `flatness` and `size` (all double) and a `shape` attribute. The captured declaration exposes `assign`, `init`, `render` and `toString`. Consult the retained constructor documentation for the supported creation forms.

Source: generated/fontlab.py: PaintBrush captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def assign(self, PaintBrush: Any) -> None:
        """void assign(PaintBrush)"""
        ...

    def init(self) -> None:
        """void init()"""
        ...

    def render(self, scale: float) -> None:
        """void render(double scale)"""
        ...

    def toString(self) -> str:
        """QString toString()"""
        ...
    angle: Any
    'double'
    flatness: Any
    'double'
    shape: Any
    'PaintBrushShape'
    size: Any
    'double'

class PaintBrushShape:
    """Data wrapper

Native bases: object

Supplemental documentation:
A data wrapper for a brush shape. The captured declaration exposes the attributes `cap0`, `cap1`, `cap_length0`, `cap_length1` and `data`, and the methods `asDict` and `asTuple`, which represent the object as a dictionary or a tuple.

Source: generated/fontlab.py: PaintBrushShape captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    cap0: Any
    cap1: Any
    cap_length0: Any
    cap_length1: Any
    data: Any

class SmartCornerParameters:
    """Data wrapper

Native bases: object

Supplemental documentation:
A data wrapper with the single attribute `curvature`. The captured declaration exposes `asDict` (represent the object as a dictionary) and `asTuple` (represent it as a tuple).

Source: generated/fontlab.py: SmartCornerParameters captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    curvature: Any

class TransformFrame:
    """TransformFrame representation

Constructors:

Native bases: object

Supplemental documentation:
A transformation frame. The captured declaration exposes the transformation methods `translate`, `scale`, `rotate`, `rotate180`, `slant`, `flipHorizontal`, `flipVertical`, `horizontalReflection`, `verticalReflection` and `doTransformation`, the geometry methods `boundingRect`, `polygon`, `expandPolygon`, `getMapped`, `getTransform`, `initCenter` and `prepareTransformations`, the control methods `getControlPos`, `setControlPos` and `setProjectionPos`, the size and margin methods `bw`, `lh`, `mb`, `mh`, `ml`, `mr`, `mt`, `mw`, `rh` and `tw`, and the attributes `tl`, `tr`, `bl`, `br` and `cr`. It is created with no captured constructor overloads.

Source: generated/fontlab.py: TransformFrame captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def boundingRect(self) -> QRectF:
        """QRectF boundingRect()"""
        ...

    def bw(self) -> float:
        """double bw()          """
        ...

    def doTransformation(self, code: int, value: QPointF) -> None:
        """void doTransformation(int code, QPointF value)"""
        ...

    def expandPolygon(self, polygon: QPolygonF) -> QPolygonF:
        """QPolygonF expandPolygon(QPolygonF polygon)"""
        ...

    def flipHorizontal(self) -> None:
        """void flipHorizontal()                         """
        ...

    def flipVertical(self) -> None:
        """void flipVertical()                           """
        ...

    def getControlPos(self, TransformFrameControls: Any) -> QPointF:
        """QPointF getControlPos(TransformFrameControls) """
        ...

    def getMapped(self, t: QTransform) -> Any:
        """TransformFrame getMapped(QTransform t)        """
        ...

    def getTransform(self) -> QTransform:
        """QTransform getTransform()"""
        ...

    def horizontalReflection(self) -> None:
        """void horizontalReflection()                   """
        ...

    def initCenter(self) -> None:
        """void initCenter()                             """
        ...

    def lh(self) -> float:
        """double lh()          """
        ...

    def mb(self) -> QPointF:
        """QPointF mb()         """
        ...

    def mh(self) -> float:
        """double mh()          """
        ...

    def ml(self) -> QPointF:
        """QPointF ml()         """
        ...

    def mr(self) -> QPointF:
        """QPointF mr()         """
        ...

    def mt(self) -> QPointF:
        """QPointF mt()         """
        ...

    def mw(self) -> float:
        """double mw()          """
        ...

    def polygon(self) -> QPolygonF:
        """QPolygonF polygon()  """
        ...

    def prepareTransformations(self, scale: Any) -> None:
        """void prepareTransformations([TransformFrameControls control, QPointF p,] double scale)"""
        ...

    def rh(self) -> float:
        """double rh()          """
        ...

    def rotate(self, double: Any) -> None:
        """void rotate(double)                           """
        ...

    def rotate180(self) -> None:
        """void rotate180()                              """
        ...

    def scale(self, s: QPointF) -> None:
        """void scale(QPointF s)                         """
        ...

    def setControlPos(self, position: Any, reflection: bool, proportional: bool, fixed: bool) -> None:
        """void setControlPos([TransformFrameControls control,] QPointF position, bool reflection, bool proportional, bool fixed)"""
        ...

    def setProjectionPos(self, position: Any, reflection: bool, proportional: bool, fixed: bool) -> None:
        """void setProjectionPos([TransformFrameControls control,] QPointF position, bool reflection, bool proportional, bool fixed)"""
        ...

    def slant(self, *args: Any, **kwargs: Any) -> Any:
        """void slant(double angle, double angle)        """
        ...

    def translate(self, arg0: QPointF) -> None:
        """void translate(QPointF)                       """
        ...

    def tw(self) -> float:
        """double tw()          """
        ...

    def verticalReflection(self) -> None:
        """void verticalReflection()                     """
        ...
    bl: Any
    'QPointF'
    br: Any
    'QPointF'
    cr: Any
    'QPointF'
    tl: Any
    'QPointF'
    tr: Any
    'QPointF'

class YPanelManager:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
A panel manager. The captured declaration exposes the signals `desktopClientRectChanged`, `panelClosed`, `toolbarOpened` and `toolbarClosed` and the method `showContextMenu`. It also carries the Qt object members `parent`, `children`, `findChild`, `findChildren`, `setParent`, `connect`, `disconnect`, `deleteLater` and `property`, and the attribute `objectName`. It is created with no captured constructor overloads.

Source: generated/fontlab.py: YPanelManager captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def childEvent(self, event: Any) -> Any:
        """X.childEvent(event)"""
        ...

    def children(self) -> tuple:
        """X.children() -> tuple"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def desktopClientRectChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelManager.desktopClientRectChanged; argument details are not documented."""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelManager.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def dumpObjectInfo(self) -> Any:
        """X.dumpObjectInfo()"""
        ...

    def dumpObjectTree(self) -> Any:
        """X.dumpObjectTree()"""
        ...

    def dynamicPropertyNames(self) -> Any:
        """X.dynamicPropertyNames()"""
        ...

    def event(self, event: Any) -> bool:
        """X.event(event) -> bool"""
        ...

    def eventFilter(self, watched: Any, event: Any) -> bool:
        """X.eventFilter(watched, event) -> bool"""
        ...

    def findChild(self, type: Any, name: Any) -> Any:
        """X.findChild(type, name) -> PythonQt.private.QObject"""
        ...

    def findChildren(self, type: Any, name: Any) -> tuple:
        """X.findChildren(type, name) -> tuple"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelManager.objectNameChanged; argument details are not documented."""
        ...

    def panelClosed(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelManager.panelClosed; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def showContextMenu(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelManager.showContextMenu; argument details are not documented."""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def thread(self) -> Any:
        """X.thread()"""
        ...

    def timerEvent(self, event: Any) -> Any:
        """X.timerEvent(event)"""
        ...

    def toolbarClosed(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelManager.toolbarClosed; argument details are not documented."""
        ...

    def toolbarOpened(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelManager.toolbarOpened; argument details are not documented."""
        ...

    def tr(self, text: Any, ambig: Any, n: Any) -> str:
        """X.tr(text, ambig, n) -> str"""
        ...
    objectName: Any

class YPanelWidget:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Panel widget. The captured declaration exposes `addAction`, `adjustSize`, `close`, `hide`, `show`, `move`, `resize`, `update`, `setEnabled`, `setVisible`, `isVisible`, `isEnabled`, `connect`, `disconnect`, `deleteLater`, `findChild`, `findChildren`, `className` and `grab`. It is created with no captured constructor overloads.

Source: generated/fontlab.py: YPanelWidget captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def actionEvent(self, event: Any) -> Any:
        """X.actionEvent(event)"""
        ...

    def actions(self) -> tuple:
        """X.actions() -> tuple"""
        ...

    def activateWindow(self) -> Any:
        """X.activateWindow()"""
        ...

    def addAction(self, action: Any) -> Any:
        """X.addAction(action)"""
        ...

    def addActions(self, actions: Any) -> Any:
        """X.addActions(actions)"""
        ...

    def adjustSize(self) -> Any:
        """X.adjustSize()"""
        ...

    def backgroundRole(self) -> Any:
        """X.backgroundRole()"""
        ...

    def backingStore(self) -> Any:
        """X.backingStore() -> PythonQt.QtGui.QBackingStore"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def changeEvent(self, arg__1: Any) -> Any:
        """X.changeEvent(arg__1)"""
        ...

    def childAt(self, x: Any, y: Any) -> Any:
        """X.childAt(x, y) -> PythonQt.QtGui.QWidget"""
        ...

    def childEvent(self, event: Any) -> Any:
        """X.childEvent(event)"""
        ...

    def children(self) -> tuple:
        """X.children() -> tuple"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def clearFocus(self) -> Any:
        """X.clearFocus()"""
        ...

    def clearMask(self) -> Any:
        """X.clearMask()"""
        ...

    def close(self) -> bool:
        """X.close() -> bool"""
        ...

    def closeEvent(self, event: Any) -> Any:
        """X.closeEvent(event)"""
        ...

    def colorCount(self) -> int:
        """X.colorCount() -> int"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def contentsMargins(self) -> Any:
        """X.contentsMargins() -> PythonQt.QtGui.QMargins"""
        ...

    def contentsRect(self) -> Any:
        """X.contentsRect() -> PythonQt.QtCore.QRect"""
        ...

    def contextMenuEvent(self, event: Any) -> Any:
        """X.contextMenuEvent(event)"""
        ...

    def createWinId(self) -> Any:
        """X.createWinId()"""
        ...

    def createWindowContainer(self, window: Any, parent: Any, arg2: flags) -> Any:
        """X.createWindowContainer(window, parent, flags) -> PythonQt.QtGui.QWidget"""
        ...

    def customContextMenuRequested(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelWidget.customContextMenuRequested; argument details are not documented."""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def depth(self) -> int:
        """X.depth() -> int"""
        ...

    def destroy(self, destroyWindow: Any, destroySubWindows: Any) -> Any:
        """X.destroy(destroyWindow, destroySubWindows)"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelWidget.destroyed; argument details are not documented."""
        ...

    def devType(self) -> int:
        """X.devType() -> int"""
        ...

    def devicePixelRatio(self) -> int:
        """X.devicePixelRatio() -> int"""
        ...

    def devicePixelRatioF(self) -> float:
        """X.devicePixelRatioF() -> float"""
        ...

    def devicePixelRatioFScale(self) -> float:
        """X.devicePixelRatioFScale() -> float"""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def dragEnterEvent(self, event: Any) -> Any:
        """X.dragEnterEvent(event)"""
        ...

    def dragLeaveEvent(self, event: Any) -> Any:
        """X.dragLeaveEvent(event)"""
        ...

    def dragMoveEvent(self, event: Any) -> Any:
        """X.dragMoveEvent(event)"""
        ...

    def dropEvent(self, event: Any) -> Any:
        """X.dropEvent(event)"""
        ...

    def dumpObjectInfo(self) -> Any:
        """X.dumpObjectInfo()"""
        ...

    def dumpObjectTree(self) -> Any:
        """X.dumpObjectTree()"""
        ...

    def dynamicPropertyNames(self) -> Any:
        """X.dynamicPropertyNames()"""
        ...

    def effectiveWinId(self) -> int:
        """X.effectiveWinId() -> int"""
        ...

    def ensurePolished(self) -> Any:
        """X.ensurePolished()"""
        ...

    def enterEvent(self, event: Any) -> Any:
        """X.enterEvent(event)"""
        ...

    def event(self, event: Any) -> bool:
        """X.event(event) -> bool"""
        ...

    def eventFilter(self, watched: Any, event: Any) -> bool:
        """X.eventFilter(watched, event) -> bool"""
        ...

    def findChild(self, type: Any, name: Any) -> Any:
        """X.findChild(type, name) -> PythonQt.private.QObject"""
        ...

    def findChildren(self, type: Any, name: Any) -> tuple:
        """X.findChildren(type, name) -> tuple"""
        ...

    def focusInEvent(self, event: Any) -> Any:
        """X.focusInEvent(event)"""
        ...

    def focusNextChild(self) -> bool:
        """X.focusNextChild() -> bool"""
        ...

    def focusNextPrevChild(self, next: Any) -> bool:
        """X.focusNextPrevChild(next) -> bool"""
        ...

    def focusOutEvent(self, event: Any) -> Any:
        """X.focusOutEvent(event)"""
        ...

    def focusPreviousChild(self) -> bool:
        """X.focusPreviousChild() -> bool"""
        ...

    def focusProxy(self) -> Any:
        """X.focusProxy() -> PythonQt.QtGui.QWidget"""
        ...

    def focusWidget(self) -> Any:
        """X.focusWidget() -> PythonQt.QtGui.QWidget"""
        ...

    def fontInfo(self) -> Any:
        """X.fontInfo() -> PythonQt.QtGui.QFontInfo"""
        ...

    def fontMetrics(self) -> Any:
        """X.fontMetrics() -> PythonQt.QtGui.QFontMetrics"""
        ...

    def foregroundRole(self) -> Any:
        """X.foregroundRole()"""
        ...

    def grab(self, rectangle: Any) -> Any:
        """X.grab(rectangle) -> PythonQt.QtGui.QPixmap"""
        ...

    def grabGesture(self, type: Any, arg1: flags) -> Any:
        """X.grabGesture(type, flags)"""
        ...

    def grabKeyboard(self) -> Any:
        """X.grabKeyboard()"""
        ...

    def grabMouse(self, arg__1: Any) -> Any:
        """X.grabMouse(arg__1)"""
        ...

    def grabShortcut(self, key: Any, context: Any) -> int:
        """X.grabShortcut(key, context) -> int"""
        ...

    def graphicsEffect(self) -> Any:
        """X.graphicsEffect() -> PythonQt.QtGui.QGraphicsEffect"""
        ...

    def graphicsProxyWidget(self) -> Any:
        """X.graphicsProxyWidget() -> PythonQt.QtGui.QGraphicsProxyWidget"""
        ...

    def hasFocus(self) -> bool:
        """X.hasFocus() -> bool"""
        ...

    def hasHeightForWidth(self) -> bool:
        """X.hasHeightForWidth() -> bool"""
        ...

    def hasMouseTracking(self) -> bool:
        """X.hasMouseTracking() -> bool"""
        ...

    def heightForWidth(self, arg__1: Any) -> int:
        """X.heightForWidth(arg__1) -> int"""
        ...

    def heightMM(self) -> int:
        """X.heightMM() -> int"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hide(self) -> Any:
        """X.hide()"""
        ...

    def hideEvent(self, event: Any) -> Any:
        """X.hideEvent(event)"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def initPainter(self, painter: Any) -> Any:
        """X.initPainter(painter)"""
        ...

    def inputMethodEvent(self, arg__1: Any) -> Any:
        """X.inputMethodEvent(arg__1)"""
        ...

    def inputMethodQuery(self, arg__1: Any) -> Any:
        """X.inputMethodQuery(arg__1) -> object"""
        ...

    def insertAction(self, before: Any, action: Any) -> Any:
        """X.insertAction(before, action)"""
        ...

    def insertActions(self, before: Any, actions: Any) -> Any:
        """X.insertActions(before, actions)"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isAncestorOf(self, child: Any) -> bool:
        """X.isAncestorOf(child) -> bool"""
        ...

    def isEnabled(self) -> bool:
        """X.isEnabled() -> bool"""
        ...

    def isEnabledTo(self, arg__1: Any) -> bool:
        """X.isEnabledTo(arg__1) -> bool"""
        ...

    def isFullScreen(self) -> bool:
        """X.isFullScreen() -> bool"""
        ...

    def isHidden(self) -> bool:
        """X.isHidden() -> bool"""
        ...

    def isLeftToRight(self) -> bool:
        """X.isLeftToRight() -> bool"""
        ...

    def isMaximized(self) -> bool:
        """X.isMaximized() -> bool"""
        ...

    def isMinimized(self) -> bool:
        """X.isMinimized() -> bool"""
        ...

    def isModal(self) -> bool:
        """X.isModal() -> bool"""
        ...

    def isRightToLeft(self) -> bool:
        """X.isRightToLeft() -> bool"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isVisible(self) -> bool:
        """X.isVisible() -> bool"""
        ...

    def isVisibleTo(self, arg__1: Any) -> bool:
        """X.isVisibleTo(arg__1) -> bool"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindow(self) -> bool:
        """X.isWindow() -> bool"""
        ...

    def isWindowModified(self) -> bool:
        """X.isWindowModified() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def keyPressEvent(self, event: Any) -> Any:
        """X.keyPressEvent(event)"""
        ...

    def keyReleaseEvent(self, event: Any) -> Any:
        """X.keyReleaseEvent(event)"""
        ...

    def keyboardGrabber(self) -> Any:
        """X.keyboardGrabber() -> PythonQt.QtGui.QWidget"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def layout(self) -> Any:
        """X.layout() -> PythonQt.QtGui.QLayout"""
        ...

    def leaveEvent(self, event: Any) -> Any:
        """X.leaveEvent(event)"""
        ...

    def logicalDpiX(self) -> int:
        """X.logicalDpiX() -> int"""
        ...

    def logicalDpiY(self) -> int:
        """X.logicalDpiY() -> int"""
        ...

    def lower(self) -> Any:
        """X.lower()"""
        ...

    def mapFrom(self, arg__1: Any, arg__2: Any) -> Any:
        """X.mapFrom(arg__1, arg__2) -> PythonQt.QtCore.QPoint"""
        ...

    def mapFromGlobal(self, arg__1: Any) -> Any:
        """X.mapFromGlobal(arg__1) -> PythonQt.QtCore.QPoint"""
        ...

    def mapFromParent(self, arg__1: Any) -> Any:
        """X.mapFromParent(arg__1) -> PythonQt.QtCore.QPoint"""
        ...

    def mapTo(self, arg__1: Any, arg__2: Any) -> Any:
        """X.mapTo(arg__1, arg__2) -> PythonQt.QtCore.QPoint"""
        ...

    def mapToGlobal(self, arg__1: Any) -> Any:
        """X.mapToGlobal(arg__1) -> PythonQt.QtCore.QPoint"""
        ...

    def mapToParent(self, arg__1: Any) -> Any:
        """X.mapToParent(arg__1) -> PythonQt.QtCore.QPoint"""
        ...

    def mask(self) -> Any:
        """X.mask() -> PythonQt.QtGui.QRegion"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def metric(self, arg__1: Any) -> int:
        """X.metric(arg__1) -> int"""
        ...

    def mouseDoubleClickEvent(self, event: Any) -> Any:
        """X.mouseDoubleClickEvent(event)"""
        ...

    def mouseGrabber(self) -> Any:
        """X.mouseGrabber() -> PythonQt.QtGui.QWidget"""
        ...

    def mouseMoveEvent(self, event: Any) -> Any:
        """X.mouseMoveEvent(event)"""
        ...

    def mousePressEvent(self, event: Any) -> Any:
        """X.mousePressEvent(event)"""
        ...

    def mouseReleaseEvent(self, event: Any) -> Any:
        """X.mouseReleaseEvent(event)"""
        ...

    def move(self, x: Any, y: Any) -> Any:
        """X.move(x, y)"""
        ...

    def moveEvent(self, event: Any) -> Any:
        """X.moveEvent(event)"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def nativeEvent(self, eventType: Any, message: Any, result: Any) -> bool:
        """X.nativeEvent(eventType, message, result) -> bool"""
        ...

    def nativeParentWidget(self) -> Any:
        """X.nativeParentWidget() -> PythonQt.QtGui.QWidget"""
        ...

    def nextInFocusChain(self) -> Any:
        """X.nextInFocusChain() -> PythonQt.QtGui.QWidget"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelWidget.objectNameChanged; argument details are not documented."""
        ...

    def overrideWindowFlags(self, type: Any) -> Any:
        """X.overrideWindowFlags(type)"""
        ...

    def overrideWindowState(self, state: Any) -> Any:
        """X.overrideWindowState(state)"""
        ...

    def paintEngine(self) -> Any:
        """X.paintEngine() -> PythonQt.QtGui.QPaintEngine"""
        ...

    def paintEvent(self, event: Any) -> Any:
        """X.paintEvent(event)"""
        ...

    def paintingActive(self) -> bool:
        """X.paintingActive() -> bool"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def parentWidget(self) -> Any:
        """X.parentWidget() -> PythonQt.QtGui.QWidget"""
        ...

    def physicalDpiX(self) -> int:
        """X.physicalDpiX() -> int"""
        ...

    def physicalDpiY(self) -> int:
        """X.physicalDpiY() -> int"""
        ...

    def previousInFocusChain(self) -> Any:
        """X.previousInFocusChain() -> PythonQt.QtGui.QWidget"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def raise_(self) -> Any:
        """X.raise()

Native spelling: raise; access it through getattr on the native object."""
        ...

    def redirected(self, offset: Any) -> Any:
        """X.redirected(offset) -> PythonQt.QtGui.QPaintDevice"""
        ...

    def releaseKeyboard(self) -> Any:
        """X.releaseKeyboard()"""
        ...

    def releaseMouse(self) -> Any:
        """X.releaseMouse()"""
        ...

    def releaseShortcut(self, id: Any) -> Any:
        """X.releaseShortcut(id)"""
        ...

    def removeAction(self, action: Any) -> Any:
        """X.removeAction(action)"""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def render(self, target: Any, targetOffset: Any, sourceRegion: Any, renderFlags: Any) -> Any:
        """X.render(target, targetOffset, sourceRegion, renderFlags)"""
        ...

    def repaint(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.repaint(x, y, w, h)"""
        ...

    def resize(self, w: Any, h: Any) -> Any:
        """X.resize(w, h)"""
        ...

    def resizeEvent(self, event: Any) -> Any:
        """X.resizeEvent(event)"""
        ...

    def restoreGeometry(self, geometry: Any) -> bool:
        """X.restoreGeometry(geometry) -> bool"""
        ...

    def saveGeometry(self) -> Any:
        """X.saveGeometry() -> PythonQt.QtCore.QByteArray"""
        ...

    def scroll(self, dx: Any, dy: Any, arg__3: Any) -> Any:
        """X.scroll(dx, dy, arg__3)"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setAcceptDrops(self, on: Any) -> Any:
        """X.setAcceptDrops(on)"""
        ...

    def setAccessibleDescription(self, description: Any) -> Any:
        """X.setAccessibleDescription(description)"""
        ...

    def setAccessibleName(self, name: Any) -> Any:
        """X.setAccessibleName(name)"""
        ...

    def setAttribute(self, arg__1: Any, on: Any) -> Any:
        """X.setAttribute(arg__1, on)"""
        ...

    def setAutoFillBackground(self, enabled: Any) -> Any:
        """X.setAutoFillBackground(enabled)"""
        ...

    def setBackgroundRole(self, arg__1: Any) -> Any:
        """X.setBackgroundRole(arg__1)"""
        ...

    def setBaseSize(self, basew: Any, baseh: Any) -> Any:
        """X.setBaseSize(basew, baseh)"""
        ...

    def setContentsMargins(self, left: Any, top: Any, right: Any, bottom: Any) -> Any:
        """X.setContentsMargins(left, top, right, bottom)"""
        ...

    def setContextMenuPolicy(self, policy: Any) -> Any:
        """X.setContextMenuPolicy(policy)"""
        ...

    def setCursor(self, arg__1: Any) -> Any:
        """X.setCursor(arg__1)"""
        ...

    def setDisabled(self, a: Any) -> Any:
        """X.setDisabled(a)"""
        ...

    def setEnabled(self, a: Any) -> Any:
        """X.setEnabled(a)"""
        ...

    def setFixedHeight(self, h: Any) -> Any:
        """X.setFixedHeight(h)"""
        ...

    def setFixedSize(self, w: Any, h: Any) -> Any:
        """X.setFixedSize(w, h)"""
        ...

    def setFixedWidth(self, w: Any) -> Any:
        """X.setFixedWidth(w)"""
        ...

    def setFocus(self, reason: Any) -> Any:
        """X.setFocus(reason)"""
        ...

    def setFocusPolicy(self, policy: Any) -> Any:
        """X.setFocusPolicy(policy)"""
        ...

    def setFocusProxy(self, arg__1: Any) -> Any:
        """X.setFocusProxy(arg__1)"""
        ...

    def setFont(self, arg__1: Any) -> Any:
        """X.setFont(arg__1)"""
        ...

    def setForegroundRole(self, arg__1: Any) -> Any:
        """X.setForegroundRole(arg__1)"""
        ...

    def setGeometry(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.setGeometry(x, y, w, h)"""
        ...

    def setGraphicsEffect(self, effect: Any) -> Any:
        """X.setGraphicsEffect(effect)"""
        ...

    def setHidden(self, hidden: Any) -> Any:
        """X.setHidden(hidden)"""
        ...

    def setInputMethodHints(self, hints: Any) -> Any:
        """X.setInputMethodHints(hints)"""
        ...

    def setLayout(self, arg__1: Any) -> Any:
        """X.setLayout(arg__1)"""
        ...

    def setLayoutDirection(self, direction: Any) -> Any:
        """X.setLayoutDirection(direction)"""
        ...

    def setLocale(self, locale: Any) -> Any:
        """X.setLocale(locale)"""
        ...

    def setMask(self, arg__1: Any) -> Any:
        """X.setMask(arg__1)"""
        ...

    def setMaximumHeight(self, maxh: Any) -> Any:
        """X.setMaximumHeight(maxh)"""
        ...

    def setMaximumSize(self, maxw: Any, maxh: Any) -> Any:
        """X.setMaximumSize(maxw, maxh)"""
        ...

    def setMaximumWidth(self, maxw: Any) -> Any:
        """X.setMaximumWidth(maxw)"""
        ...

    def setMinimumHeight(self, minh: Any) -> Any:
        """X.setMinimumHeight(minh)"""
        ...

    def setMinimumSize(self, minw: Any, minh: Any) -> Any:
        """X.setMinimumSize(minw, minh)"""
        ...

    def setMinimumWidth(self, minw: Any) -> Any:
        """X.setMinimumWidth(minw)"""
        ...

    def setMouseTracking(self, enable: Any) -> Any:
        """X.setMouseTracking(enable)"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setPalette(self, arg__1: Any) -> Any:
        """X.setPalette(arg__1)"""
        ...

    def setParent(self, parent: Any, f: Any) -> Any:
        """X.setParent(parent, f)"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setShortcutAutoRepeat(self, id: Any, enable: Any) -> Any:
        """X.setShortcutAutoRepeat(id, enable)"""
        ...

    def setShortcutEnabled(self, id: Any, enable: Any) -> Any:
        """X.setShortcutEnabled(id, enable)"""
        ...

    def setSizeIncrement(self, w: Any, h: Any) -> Any:
        """X.setSizeIncrement(w, h)"""
        ...

    def setSizePolicy(self, horizontal: Any, vertical: Any) -> Any:
        """X.setSizePolicy(horizontal, vertical)"""
        ...

    def setStatusTip(self, arg__1: Any) -> Any:
        """X.setStatusTip(arg__1)"""
        ...

    def setStyle(self, arg__1: Any) -> Any:
        """X.setStyle(arg__1)"""
        ...

    def setStyleSheet(self, styleSheet: Any) -> Any:
        """X.setStyleSheet(styleSheet)"""
        ...

    def setTabOrder(self, arg__1: Any, arg__2: Any) -> Any:
        """X.setTabOrder(arg__1, arg__2)"""
        ...

    def setToolTip(self, arg__1: Any) -> Any:
        """X.setToolTip(arg__1)"""
        ...

    def setToolTipDuration(self, msec: Any) -> Any:
        """X.setToolTipDuration(msec)"""
        ...

    def setUpdatesEnabled(self, enable: Any) -> Any:
        """X.setUpdatesEnabled(enable)"""
        ...

    def setVisible(self, visible: Any) -> Any:
        """X.setVisible(visible)"""
        ...

    def setWhatsThis(self, arg__1: Any) -> Any:
        """X.setWhatsThis(arg__1)"""
        ...

    def setWindowFilePath(self, filePath: Any) -> Any:
        """X.setWindowFilePath(filePath)"""
        ...

    def setWindowFlags(self, type: Any) -> Any:
        """X.setWindowFlags(type)"""
        ...

    def setWindowIcon(self, icon: Any) -> Any:
        """X.setWindowIcon(icon)"""
        ...

    def setWindowIconText(self, arg__1: Any) -> Any:
        """X.setWindowIconText(arg__1)"""
        ...

    def setWindowModality(self, windowModality: Any) -> Any:
        """X.setWindowModality(windowModality)"""
        ...

    def setWindowModified(self, a: Any) -> Any:
        """X.setWindowModified(a)"""
        ...

    def setWindowOpacity(self, level: Any) -> Any:
        """X.setWindowOpacity(level)"""
        ...

    def setWindowRole(self, arg__1: Any) -> Any:
        """X.setWindowRole(arg__1)"""
        ...

    def setWindowState(self, state: Any) -> Any:
        """X.setWindowState(state)"""
        ...

    def setWindowTitle(self, a: Any) -> Any:
        """X.setWindowTitle(a)"""
        ...

    def sharedPainter(self) -> Any:
        """X.sharedPainter() -> PythonQt.QtGui.QPainter"""
        ...

    def show(self) -> Any:
        """X.show()"""
        ...

    def showEvent(self, event: Any) -> Any:
        """X.showEvent(event)"""
        ...

    def showFullScreen(self) -> Any:
        """X.showFullScreen()"""
        ...

    def showMaximized(self) -> Any:
        """X.showMaximized()"""
        ...

    def showMinimized(self) -> Any:
        """X.showMinimized()"""
        ...

    def showNormal(self) -> Any:
        """X.showNormal()"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def stackUnder(self, arg__1: Any) -> Any:
        """X.stackUnder(arg__1)"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def style(self) -> Any:
        """X.style() -> PythonQt.QtGui.QStyle"""
        ...

    def tabletEvent(self, event: Any) -> Any:
        """X.tabletEvent(event)"""
        ...

    def testAttribute(self, arg__1: Any) -> bool:
        """X.testAttribute(arg__1) -> bool"""
        ...

    def thread(self) -> Any:
        """X.thread()"""
        ...

    def timerEvent(self, event: Any) -> Any:
        """X.timerEvent(event)"""
        ...

    def tr(self, text: Any, ambig: Any, n: Any) -> str:
        """X.tr(text, ambig, n) -> str"""
        ...

    def underMouse(self) -> bool:
        """X.underMouse() -> bool"""
        ...

    def ungrabGesture(self, type: Any) -> Any:
        """X.ungrabGesture(type)"""
        ...

    def unsetCursor(self) -> Any:
        """X.unsetCursor()"""
        ...

    def unsetLayoutDirection(self) -> Any:
        """X.unsetLayoutDirection()"""
        ...

    def unsetLocale(self) -> Any:
        """X.unsetLocale()"""
        ...

    def update(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.update(x, y, w, h)"""
        ...

    def updateGeometry(self) -> Any:
        """X.updateGeometry()"""
        ...

    def visibleRegion(self) -> Any:
        """X.visibleRegion() -> PythonQt.QtGui.QRegion"""
        ...

    def wheelEvent(self, event: Any) -> Any:
        """X.wheelEvent(event)"""
        ...

    def widthMM(self) -> int:
        """X.widthMM() -> int"""
        ...

    def winId(self) -> int:
        """X.winId() -> int"""
        ...

    def window(self) -> Any:
        """X.window() -> PythonQt.QtGui.QWidget"""
        ...

    def windowFlags(self) -> Any:
        """X.windowFlags()"""
        ...

    def windowHandle(self) -> Any:
        """X.windowHandle() -> PythonQt.QtGui.QWindow"""
        ...

    def windowIconChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelWidget.windowIconChanged; argument details are not documented."""
        ...

    def windowIconTextChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelWidget.windowIconTextChanged; argument details are not documented."""
        ...

    def windowRole(self) -> str:
        """X.windowRole() -> str"""
        ...

    def windowState(self) -> Any:
        """X.windowState()"""
        ...

    def windowTitleChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.YPanelWidget.windowTitleChanged; argument details are not documented."""
        ...

    def windowType(self) -> Any:
        """X.windowType()"""
        ...
    DrawChildren: Any
    DrawWindowBackground: Any
    IgnoreMask: Any
    PaintDeviceMetric: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PdmDepth: Any
    PdmDevicePixelRatio: Any
    PdmDevicePixelRatioScaled: Any
    PdmDpiX: Any
    PdmDpiY: Any
    PdmHeight: Any
    PdmHeightMM: Any
    PdmNumColors: Any
    PdmPhysicalDpiX: Any
    PdmPhysicalDpiY: Any
    PdmWidth: Any
    PdmWidthMM: Any
    RenderFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    RenderFlags: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    acceptDrops: Any
    accessibleDescription: Any
    accessibleName: Any
    autoFillBackground: Any
    baseSize: QSize
    childrenRect: QRect
    childrenRegion: QRegion
    contextMenuPolicy: Any
    cursor: QCursor
    enabled: Any
    focus: Any
    focusPolicy: Any
    font: QFont
    frameGeometry: QRect
    frameSize: QSize
    fullScreen: Any
    geometry: QRect
    height: Any
    inputMethodHints: Any
    isActiveWindow: Any
    layoutDirection: Any
    locale: QLocale
    maximized: Any
    maximumHeight: Any
    maximumSize: QSize
    maximumWidth: Any
    minimized: Any
    minimumHeight: Any
    minimumSize: QSize
    minimumSizeHint: QSize
    minimumWidth: Any
    modal: Any
    mouseTracking: Any
    normalGeometry: QRect
    objectName: Any
    palette: QPalette
    pos: QPoint
    rect: QRect
    size: QSize
    sizeHint: QSize
    sizeIncrement: QSize
    sizePolicy: QSizePolicy
    statusTip: Any
    styleSheet: Any
    tabletTracking: Any
    toolTip: Any
    toolTipDuration: Any
    updatesEnabled: Any
    visible: Any
    whatsThis: Any
    width: Any
    windowFilePath: Any
    windowIcon: QIcon
    windowIconText: Any
    windowModality: Any
    windowModified: Any
    windowOpacity: Any
    windowTitle: Any
    x: Any
    y: Any

class fgSymbol:
    """fgSymbol representation

Constructors:
  fgSymbol() - default
  fgSymbol(fgSymbol) - copy
  fgSymbol(unicode)
  fgSymbol('name')
  fgSymbol(id, fgFont)
  fgSymbol(glyph_id, package_id)
  fgSymbol(unicode, 'name', id)

Native bases: object

Supplemental documentation:
A glyph reference identified by `unicode`, `name`, `id` and `pid`, with the flags `hasName`, `hasUnicode` and `empty`. The captured declaration exposes `glyph` (returning a glyph for a font), `computeID`, `compare`, `clear`, and `data`, `setData`, `containsData` and `clearData` keyed by the `DataCode` attribute. Consult the retained constructor documentation for the supported creation forms. Caution: FontLab 9.0.9809 terminates when fgSymbol() is called with no arguments (Fontlab/fl#8632, open).

Source: generated/fontlab.py: fgSymbol captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def clearData(self, DataCode: Any) -> Any:
        """clearData(DataCode)"""
        ...

    def clearID(self) -> Any:
        """clearID()"""
        ...

    def compare(self, arg0: fgSymbol) -> bool:
        """bool compare(fgSymbol)"""
        ...

    def computeID(self, arg0: fgFont) -> bool:
        """bool computeID(fgFont)"""
        ...

    def containsData(self, DataCode: Any) -> bool:
        """bool containsData(DataCode)"""
        ...

    def data(self, DataCode: Any) -> Any:
        """QVariant data(DataCode)"""
        ...

    def glyph(self, arg0: fgFont, setId: bool) -> fgGlyph:
        """fgGlyph glyph(fgFont, bool setId)"""
        ...

    def init(self) -> Any:
        """init()"""
        ...

    def setData(self, DataCode: Any, d: Any) -> Any:
        """setData(DataCode, QVariant d)"""
        ...

    def setSterile(self) -> Any:
        """setSterile()"""
        ...
    DataCode: dict
    cr: Any
    'bool'
    empty: Any
    'bool'
    glyphIndex: Any
    'int'
    hasName: Any
    'bool'
    hasUnicode: Any
    'bool'
    id: Any
    'unsigned long'
    layerName: Any
    'string'
    ligatureIndex: Any
    'int'
    name: Any
    'QString'
    pid: Any
    'unsigned long'
    space: Any
    'bool'
    unicode: Any
    'uint'
    unicodeEnsure: Any
    'uint'

class fgSymbolList:
    """fgSymbolList representation

Constructors:
  fgSymbolList() - default
  fgSymbolList(fgSymbolList) - copy
  fgSymbolList(list(fgSymbol))
  fgSymbolList(string[, bool advancedProcessing = false])
  fgSymbolList(fgSymbolList, int len)
  fgSymbolList(fgFont, fgGlyphIDsSet)
  fgSymbolList(fgFont, list(glyph_id))

Native bases: object

Supplemental documentation:
A list of symbols. The captured declaration exposes the list methods `append`, `insert`, `remove`, `replace`, `clear`, `at`, `last`, `mid`, `size`, `empty`, `assign`, `compare` and `equals`, the loading methods `set`, `setList`, `setGlyphsList`, `setIdList`, `setNamesList`, `setUnicodeList`, `setData`, `setString` and `setSterile`, and the reading and storage methods `data`, `string`, `symbols`, `computeString`, `store`, `restore`, `reserve`, `clearData`, `clearString` and `limitLineLength`. It is created with no captured constructor overloads.

Source: generated/fontlab.py: fgSymbolList captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, fgSymbolList: Any) -> Any:
        """append(fgSymbol | fgSymbolList)"""
        ...

    def assign(self, *args: Any, **kwargs: Any) -> Any:
        """assign(fgFont, list(glyphsId))"""
        ...

    def at(self, index: Any) -> fgSymbol:
        """fgSymbol at(index)"""
        ...

    def clear(self) -> Any:
        """clear()"""
        ...

    def clearData(self, dataCode: int) -> Any:
        """clearData(int dataCode)"""
        ...

    def clearString(self) -> Any:
        """clearString()"""
        ...

    def compare(self, arg0: fgSymbolList) -> bool:
        """bool compare(fgSymbolList)"""
        ...

    def computeString(self, advancedProcessing: bool) -> Any:
        """computeString(bool advancedProcessing)"""
        ...

    def data(self, index: int, v: Any=...) -> Any:
        """QVariant data(int index, int dataCode[, QVariant v = QVariant()])"""
        ...

    def empty(self) -> bool:
        """bool empty()"""
        ...

    def equals(self, arg0: fgSymbolList) -> bool:
        """bool equals(fgSymbolList)"""
        ...

    def insert(self, index: Any, arg1: fgSymbol) -> Any:
        """insert(index, fgSymbol)"""
        ...

    def last(self) -> fgSymbol:
        """fgSymbol last()"""
        ...

    def limitLineLength(self, len: int) -> bool:
        """bool limitLineLength(int len)"""
        ...

    def mid(self, count: Any=...) -> fgSymbolList:
        """fgSymbolList mid(int index[, int count=-1])"""
        ...

    def remove(self, index: Any, count: Any) -> Any:
        """remove(index, count)"""
        ...

    def replace(self, index: Any, count: Any, arg2: fgSymbolList) -> Any:
        """replace(index,  count, fgSymbolList)"""
        ...

    def reserve(self, count: int) -> Any:
        """reserve(int count)"""
        ...

    def restore(self, *args: Any, **kwargs: Any) -> Any:
        """bool restore(QByteArray, list(fgFont))"""
        ...

    def set(self, index: Any, arg1: fgSymbol) -> Any:
        """set(index, fgSymbol)"""
        ...

    def setData(self, index: Any, DataCode: Any, arg2: Any) -> Any:
        """setData(index,  DataCode, QVariant)"""
        ...

    def setGlyphsList(self, *args: Any, **kwargs: Any) -> Any:
        """setGlyphsList(list(fgGlyph), fgFont)"""
        ...

    def setIdList(self, *args: Any, **kwargs: Any) -> Any:
        """setIdList(list(id), fgFont)"""
        ...

    def setList(self, list: fgSymbols) -> Any:
        """setList(fgSymbols list)"""
        ...

    def setNamesList(self, QStringList: Any) -> Any:
        """setNamesList(string | QStringList)"""
        ...

    def setSterile(self) -> Any:
        """setSterile()"""
        ...

    def setString(self, advancedProcessing: Any=...) -> Any:
        """setString(string[, bool advancedProcessing = true])"""
        ...

    def setUnicodeList(self, *args: Any, **kwargs: Any) -> Any:
        """setUnicodeList( list(unicodes) )"""
        ...

    def size(self) -> int:
        """int size()"""
        ...

    def store(self, packageID: Any) -> bytes:
        """QByteArray store(packageID)"""
        ...

    def string(self, advancedProcessing: bool) -> str:
        """QString string(bool advancedProcessing)"""
        ...

    def symbols(self) -> Any:
        """list(fgSymbol) symbols()"""
        ...

class flAbstractEditor:
    """flAbstractEditor representation

Constructors:
  flAbstractEditor()
  flAbstractEditor(flObject)

Native bases: object

Supplemental documentation:
Abstract editor. The captured declaration exposes `activate`, `deactivate` and `widget`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flAbstractEditor captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activate(self) -> Any:
        """activate()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivate(self) -> Any:
        """deactivate()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'
    widget: Any
    'QWidget*'

class flAbstractVectorNode:
    """flAbstractVectorNode representation

Constructors:
  flAbstractVectorNode(flAbstractVectorNode)
  flAbstractVectorNode(flObject)

Native bases: object

Supplemental documentation:
Abstract vector node. The captured declaration exposes `angleTo`, `canBeSmooth`, `canCollapse`, `collapseHandles`, `convertToCurve`, `convertToLine`, `moveBy`, `rotateBy`, `scaleBy`, `skewBy`, `makeStart`, `nextNode`, `prevNode`, `isCurve`, `isOn`, `isOff`, `isFirst`, `isLast`, `smooth`, `position`, `selected`, `x` and `y`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flAbstractVectorNode captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def angleTo(self, p: QPointF) -> float:
        """double angleTo(QPointF p)"""
        ...

    def applyTransform(self, arg0: QTransform) -> Any:
        """applyTransform(QTransform)"""
        ...

    def canBeHobby(self) -> bool:
        """bool canBeHobby()"""
        ...

    def canBeSmooth(self) -> bool:
        """bool canBeSmooth()"""
        ...

    def canCollapse(self) -> bool:
        """bool canCollapse()"""
        ...

    def canImprove(self) -> bool:
        """bool canImprove()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def checkVectors(self) -> bool:
        """bool checkVectors()"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearStored(self) -> Any:
        """clearStored()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneMapped(self, arg0: QTransform) -> flNode:
        """flNode cloneMapped(QTransform)"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def collapseHandles(self) -> bool:
        """bool collapseHandles()"""
        ...

    def convertToCurve(self, smooth: Any=...) -> bool:
        """bool convertToCurve([bool smooth = false])"""
        ...

    def convertToCurves(self) -> bool:
        """bool convertToCurves()"""
        ...

    def convertToLine(self) -> bool:
        """bool convertToLine()"""
        ...

    def copyFrom(self, withSelected: Any=...) -> Any:
        """copyFrom(Node[, withSelected=False])"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        """double distanceTo(Node/QPointF)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getLines(self, *args: Any, **kwargs: Any) -> Any:
        """(QLineF, QLineF)/None getLines()"""
        ...

    def getOn(self) -> Any:
        """Node/None getOn()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def improve(self) -> bool:
        """bool improve()"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isCorner(self, a: Any=...) -> bool:
        """bool isCorner([double a = 10.])"""
        ...

    def isCurve(self) -> bool:
        """bool isCurve()"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isEqualTo(self, tolerance: Any=...) -> bool:
        """bool isEqualTo(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])"""
        ...

    def isExtreme(self, open: Any=...) -> bool:
        """bool isExtreme(bool x[, bool open = true[, double limit = 0]])"""
        ...

    def isFirst(self) -> bool:
        """bool isFirst()"""
        ...

    def isG2(self, tolerance: float) -> bool:
        """bool isG2(double tolerance)"""
        ...

    def isInternal(self, clockwise: bool) -> bool:
        """bool isInternal(bool clockwise)"""
        ...

    def isInterpolated(self, x: bool) -> bool:
        """bool isInterpolated(bool x)"""
        ...

    def isLast(self) -> bool:
        """bool isLast()"""
        ...

    def isOff(self) -> bool:
        """bool isOff()"""
        ...

    def isOn(self) -> bool:
        """bool isOn()"""
        ...

    def isSmartAngle(self) -> bool:
        """bool isSmartAngle()"""
        ...

    def makeStart(self) -> bool:
        """bool makeStart()"""
        ...

    def moveBy(self, *args: Any, **kwargs: Any) -> Any:
        """moveBy(float dx, float dy[, bool round=false]"""
        ...

    def nextNode(self, nodeType: Any=...) -> Any:
        """Node/None nextNode([string nodeType= [, int searchDepth=1]])"""
        ...

    def pointG2(self) -> Any:
        """QPointF/None pointG2()"""
        ...

    def prevNode(self, nodeType: Any=...) -> Any:
        """Node/None prevNode([string nodeType= [, int searchDepth=1]])"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreCoordinates(self) -> Any:
        """restoreCoordinates()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def rotateBy(self, origin: Any=...) -> Any:
        """rotateBy(valueDegree[, QPointF origin=(0, 0)])"""
        ...

    def round(self) -> Any:
        """round() - Round the node's coordinate"""
        ...

    def scaleBy(self, origin: Any=...) -> Any:
        """scaleBy(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])"""
        ...

    def setExtraLast(self, bool: Any) -> Any:
        """setExtraLast(bool)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setNextSmooth(self, base: QPointF) -> Any:
        """setNextSmooth(QPointF base)"""
        ...

    def setPosition(self, arg0: QPointF) -> None:
        """void setPosition(QPointF)"""
        ...

    def setPrevSmooth(self, base: QPointF) -> Any:
        """setPrevSmooth(QPointF base)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSmartAngleEnbl(self, bool: Any) -> bool:
        """bool setSmartAngleEnbl(bool)"""
        ...

    def setSmartSharp(self, tension: Any=...) -> bool:
        """bool setSmartSharp([double tension = 0.6])"""
        ...

    def skewBy(self, origin: Any=...) -> Any:
        """skewBy(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])"""
        ...

    def smartMove(self, offset: Any) -> Any:
        """list(uint) smartMove(offset)"""
        ...

    def smartSetXY(self, arg0: QPointF) -> Any:
        """smartSetXY(QPointF)"""
        ...

    def storeCoordinates(self) -> Any:
        """storeCoordinates()"""
        ...

    def storeTestParameters(self) -> Any:
        """storeTestParameters()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def transformBy(self, origin: Any=...) -> Any:
        """transformBy(QTransform tx[, QPointF origin=(0, 0)])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateG2(self) -> bool:
        """bool updateG2()"""
        ...

    def updateSmooth(self, extended_neibh: Any=...) -> Any:
        """updateSmooth([bool extended_neibh=true])"""
        ...
    NodeKind: dict
    NodeType: dict
    angle: Any
    'angle'
    contour: Any
    'The parent Contour or None if not present'
    flObjectFlags: dict
    g2: Any
    'g2'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hobby: Any
    'hobby'
    id: Any
    'object id'
    index: Any
    "The index of the node in parent's contour (if present, otherwise -1)"
    interpolated: Any
    'interpolated'
    interpolatedX: Any
    'interpolatedX'
    interpolatedY: Any
    'interpolatedY'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isSelectedAlone: Any
    'bool'
    isTerminal: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    nodeState: Any
    'nodeState'
    position: Any
    'Coordinates of the node as QPointF'
    preview: Any
    'preview'
    refCnt: Any
    'object references count'
    scv: Any
    'scv'
    selected: Any
    'The selected flag'
    smartAngleR: Any
    'smartAngleR'
    smooth: Any
    'The smooth flag'
    state: Any
    'state'
    type: Any
    'The node type'
    x: Any
    'The x coordinate of the node'
    y: Any
    'The y coordinate of the node'

class flAnchor:
    """flAnchor representation

Constructors:
  flAnchor() - default
  flAnchor(flAnchor) - copy
  flAnchor(flObject)

Native bases: object

Supplemental documentation:
An editing anchor whose `name` identifies the object and whose `anchorPoint` holds its QPointF position. The captured declaration exposes `isGlobal`, `fixHorzDirection` and `fixVertDirection` as boolean attributes. Consult the retained constructor documentation for supported creation forms.

Source: generated/fontlab.py: flAnchor captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def added(self) -> Any:
        """added()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasObject(self, arg0: flObject) -> bool:
        """bool hasObject(flObject)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removed(self) -> Any:
        """removed()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    ModeSnap: dict
    anchorCode: Any
    'quint64'
    anchorPoint: Any
    'QPointF'
    fixHorzDirection: Any
    'bool'
    fixVertDirection: Any
    'bool'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isGlobal: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flAuditInfo:
    """flAuditInfo representation

Constructors:
  flAuditInfo()
  flAuditInfo(flObject)
  flAuditInfo(flAuditInfo)
  flAuditInfo(FaBasic, QTransform)

Native bases: object

Supplemental documentation:
Audit information. The captured declaration exposes `glyphLocation`, and the attributes `basic`, `item`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flAuditInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def glyphLocation(self, *args: Any, **kwargs: Any) -> Any:
        """QPointF glyphLocation([QPointF])"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    basic: Any
    'FaBasic'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    item: Any
    'flObject'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flAxis:
    """flAxis representation

Constructors:
  flAxis() - default
  flAxis(string name)
  flAxis(string name, string tag, string short_name)

Native bases: object

Supplemental documentation:
A variation axis. The captured declaration exposes the attributes `name`, `tag`, `shortName`, `minimal`, `default`, `maximum`, `designMin`, `designDef`, `designMax`, `hidden`, `map` and `playRange`, and methods including `checkValue`, `getRange`, `mappedValue`, `normalize`, `styleName`, `styleValue`, `valueWeight` and `valueWidth`. It is created as `flAxis()`, `flAxis(string name)` or `flAxis(string name, string tag, string short_name)`.

Source: generated/fontlab.py: flAxis captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def _has_axis_name(self, *args: Any, **kwargs: Any) -> Any:
        """QString _check_axis_name(QList<flAxis> axes, int exclude, strin gname)"""
        ...

    def checkValue(self, v: float) -> float:
        """double checkValue(double v)"""
        ...

    def getRange(self) -> float:
        """double getRange()"""
        ...

    def instanceIndex(self, v: float) -> int:
        """int instanceIndex(double v)"""
        ...

    def instances2map(self) -> bool:
        """bool instances2map()"""
        ...

    def instances2string(self) -> Any:
        """string instances2string()"""
        ...

    def isWeight(self, s: Any) -> bool:
        """bool isWeight(string s)"""
        ...

    def isWidth(self, s: Any) -> bool:
        """bool isWidth(string s)"""
        ...

    def locationName(self, axes: list[flAxis], location: flLocation) -> str:
        """QString locationName(QList<flAxis> axes, flLocation location)"""
        ...

    def map2instances(self) -> bool:
        """bool map2instances()"""
        ...

    def mappedValue(self, v: float) -> float:
        """double mappedValue(double v)"""
        ...

    def normalize(self, userValue: float) -> float:
        """double normalize(double userValue)"""
        ...

    def onEdge(self, v: float) -> bool:
        """bool onEdge(double v)"""
        ...

    def string2instances(self, s: Any) -> bool:
        """bool string2instances(string s)"""
        ...

    def styleName(self, v: float) -> Any:
        """string styleName(double v)"""
        ...

    def styleValue(self, style_name: Any) -> float:
        """double styleValue(string style_name)"""
        ...

    def updateInstances(self) -> None:
        """void updateInstances()"""
        ...

    def updateShortName(self) -> None:
        """void updateShortName()"""
        ...

    def updateTag(self) -> None:
        """void updateTag()"""
        ...

    def valueWeight(self, location: flLocation, value: float) -> float:
        """double valueWeight(flLocation location, double value)"""
        ...

    def valueWidth(self, location: flLocation, value: float) -> float:
        """double valueWidth(flLocation location, double value)"""
        ...
    default: Any
    'double'
    designDef: Any
    'double'
    designMax: Any
    'double'
    designMin: Any
    'double'
    hidden: Any
    'bool'
    map: Any
    'QMap<double,double>'
    maximum: Any
    'double'
    minimal: Any
    'double'
    name: Any
    'string'
    playRange: Any
    '(double, double)'
    shortName: Any
    'string'
    tag: Any
    'string'

class flBasicTool:
    """flBasicTool representation

Constructors:
  flBasicTool()
  flBasicTool(flObject)
  flBasicTool(flBasicTool)

Native bases: object

Supplemental documentation:
A basic tool. The captured declaration exposes `activateTool`, `deactivateTool`, and the attributes `cursorId`, `needDeactivateParent`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flBasicTool captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activateTool(self) -> Any:
        """activateTool()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivateTool(self) -> Any:
        """deactivateTool()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    cursorId: Any
    'CursorId'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    needDeactivateParent: Any
    'bool'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flCanvas:
    """flCanvas representation

Constructors:
  flCanvas()
  flCanvas(flCanvas)
  flCanvas(flObject)
  flCanvas(id)

Native bases: object

Supplemental documentation:
Canvas. The captured declaration exposes `activateEditor`, `deactivateEditor`, `addTextBlock`, `clearTextBlocks`, `clearItems`, `appendDecorator`, `clearDecorators`, `hoveredItem`, `haveSelectedNodes`, `invertSelectedNodes`, `isActiveCanvas`, `isFocusedCanvas`, `ensureVisible`, `hide`, `currentHistoryState` and `hasHistoryState`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flCanvas captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def _finalize_smart_angles(self) -> bool:
        """bool _finalize_smart_angles()"""
        ...

    def acceptEvents(self) -> int:
        """int acceptEvents()"""
        ...

    def activateEditor(self, canvas_pos: QPointF) -> None:
        """void activateEditor(QPointF canvas_pos)"""
        ...

    def activatePreviewNodes(self) -> Any:
        """activatePreviewNodes()"""
        ...

    def addTextBlock(self, arg0: flTextBlock) -> Any:
        """addTextBlock(flTextBlock)"""
        ...

    def addedToCanvas(self, arg0: flCanvas) -> None:
        """void addedToCanvas(flCanvas)"""
        ...

    def addedToWorkspace(self, arg0: flWorkspace) -> Any:
        """addedToWorkspace(flWorkspace)"""
        ...

    def adjustCanvasPosition(self, arg0: QPointF) -> QPointF:
        """QPointF adjustCanvasPosition(QPointF)"""
        ...

    def adjustPosition(self, double: Any) -> Any:
        """QPointF | double adjustPosition(QPointF | double)"""
        ...

    def appendDecorator(self, arg0: flVisualItem, DecoratorOrder: Any) -> None:
        """void appendDecorator(flVisualItem, DecoratorOrder)"""
        ...

    def availableRect(self) -> QRectF:
        """QRectF availableRect()"""
        ...

    def boundingRectOnCanvas(self, *args: Any, **kwargs: Any) -> Any:
        """QRectF boundingRectOnCanvas("""
        ...

    def canvas(self) -> flCanvas:
        """flCanvas canvas()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearDecorators(self) -> Any:
        """clearDecorators()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearItems(self) -> Any:
        """clearItems()"""
        ...

    def clearSurfaces(self) -> Any:
        """clearSurfaces()"""
        ...

    def clearTextBlocks(self) -> Any:
        """clearTextBlocks()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def collectChangedRects(self) -> Any:
        """collectChangedRects()"""
        ...

    def contain(self, canvas_pos: QPointF) -> bool:
        """bool contain(QPointF canvas_pos)"""
        ...

    def containsItem(self, arg0: flVisualItem) -> bool:
        """bool containsItem(flVisualItem)"""
        ...

    def createFrame(self, list: fgSymbolList, position: QPointF) -> fgSymbolList:
        """fgSymbolList createFrame(fgSymbolList list, QPointF position)"""
        ...

    def createInstance(self) -> flCanvas:
        """flCanvas createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivateEditor(self) -> Any:
        """deactivateEditor()"""
        ...

    def deactivatePreviewNodes(self) -> Any:
        """deactivatePreviewNodes()"""
        ...

    def distanceTo(self, arg0: QPointF) -> float:
        """double distanceTo(QPointF)"""
        ...

    def ensureVisible(self, total_cover: Any=...) -> Any:
        """ensureVisible(QPointF | QRectF canvas_rect[, bool total_cover = true])"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getHighlight(self) -> Any:
        """QRectF/Nothing getHighlight()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getScaleTo(self, arg0: flShapeInfo) -> float:
        """double getScaleTo(flShapeInfo)"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveCanvas(self) -> bool:
        """bool haveCanvas()"""
        ...

    def haveEditor(self, canvas_pos: QPointF) -> bool:
        """bool haveEditor(QPointF canvas_pos)"""
        ...

    def haveHoveredItem(self) -> bool:
        """bool haveHoveredItem()"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def haveSelectedNodes(self) -> bool:
        """bool haveSelectedNodes()"""
        ...

    def hide(self) -> Any:
        """hide()"""
        ...

    def highlight(self, arg0: QRectF) -> Any:
        """highlight(QRectF)"""
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def hoveredItem(self) -> flVisualItem:
        """flVisualItem hoveredItem()"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceAcceptEvents(self) -> int:
        """int instanceAcceptEvents()"""
        ...

    def instanceType(self) -> int:
        """int instanceType()"""
        ...

    def invertSelectedNodes(self, *args: Any, **kwargs: Any) -> Any:
        """invertSelectedNodes(QList<flNodeInfo>)"""
        ...

    def invselect(self) -> Any:
        """invselect()"""
        ...

    def isActiveCanvas(self) -> bool:
        """bool isActiveCanvas()"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isFocusedCanvas(self) -> bool:
        """bool isFocusedCanvas()"""
        ...

    def isSelectable(self) -> bool:
        """bool isSelectable()"""
        ...

    def isStableSelect(self) -> bool:
        """bool isStableSelect()"""
        ...

    def itemScale(self) -> float:
        """double itemScale()"""
        ...

    def mapCanvasDistanceToItem(self, arg0: QPointF) -> QPointF:
        """QPointF mapCanvasDistanceToItem(QPointF)"""
        ...

    def mapCanvasToItem(self, QRectF: Any) -> Any:
        """QPointF | QRectF mapCanvasToItem(QPointF | QRectF)"""
        ...

    def mapDeltaFromGlobalToCanvas(self, arg0: QPoint) -> QPointF:
        """QPointF mapDeltaFromGlobalToCanvas(QPoint)"""
        ...

    def mapFromGlobal(self, QPoint: Any) -> Any:
        """QRectF | QPointF mapFromGlobal(QRect | QPoint)"""
        ...

    def mapFromViewport(self, QPoint: Any) -> Any:
        """QRectF | QLineF | QPointF mapFromViewport(QRectF | QRect | QLineF | QPointF | QPoint)"""
        ...

    def mapItemToCanvas(self, QRectF: Any) -> Any:
        """QPointF | QRectF mapItemToCanvas(QPointF | QRectF)"""
        ...

    def mapToGlobal(self, arg0: QPointF) -> QPointF:
        """QPointF mapToGlobal(QPointF)"""
        ...

    def mapToViewport(self, QPoint: Any) -> Any:
        """QPolygonF | QRect | QPoint mapToViewport(QPolygonF | QRect | QPoint)"""
        ...

    def mapToViewportF(self, QLineF: Any) -> Any:
        """QPointF | QLineF mapToViewportF(QPointF | QLineF)"""
        ...

    def metricStep(self) -> float:
        """double metricStep()"""
        ...

    def mousePosition(self) -> QPointF:
        """QPointF mousePosition()"""
        ...

    def mousePressed(self) -> bool:
        """bool mousePressed()"""
        ...

    def move(self, arg0: QPointF) -> None:
        """void move(QPointF)"""
        ...

    def operationAdjustMetrics(self, delta: float, percent: bool) -> Any:
        """operationAdjustMetrics(double delta, bool percent)"""
        ...

    def operationAlign(self, *args: Any, **kwargs: Any) -> Any:
        """operationAlign(Qt::Alignment)"""
        ...

    def operationBeauty(self, bool: Any) -> Any:
        """operationBeauty(bool)"""
        ...

    def operationBreak(self, notify: bool, alone_selected: bool) -> bool:
        """bool operationBreak(bool notify, bool alone_selected)"""
        ...

    def operationCopyToMask(self, *args: Any, **kwargs: Any) -> Any:
        """operationCopyToMask(bool global = false)"""
        ...

    def operationDecompose(self) -> bool:
        """bool operationDecompose()"""
        ...

    def operationFlipHorizontal(self) -> Any:
        """operationFlipHorizontal()"""
        ...

    def operationFlipVertical(self) -> Any:
        """operationFlipVertical()"""
        ...

    def operationGenius(self, bool: Any) -> Any:
        """operationGenius(bool)"""
        ...

    def operationHarmonize(self) -> Any:
        """operationHarmonize()"""
        ...

    def operationImprove(self) -> Any:
        """operationImprove()"""
        ...

    def operationJoin(self) -> Any:
        """operationJoin()"""
        ...

    def operationNoServant(self) -> Any:
        """operationNoServant()"""
        ...

    def operationPrepare(self, *args: Any, **kwargs: Any) -> Any:
        """(flModelProducer, QList<flNodeInfo> selection, flShapeInfo, flGlyphInfo)/Nothing operationPrepare(bool allow_all_contours, bool allow_all_nodes = false)"""
        ...

    def operationReverseContours(self) -> Any:
        """operationReverseContours()"""
        ...

    def operationRotate180(self) -> Any:
        """operationRotate180()"""
        ...

    def operationRotate90(self) -> Any:
        """operationRotate90()"""
        ...

    def operationServantX(self, bool: Any) -> Any:
        """operationServantX(bool)"""
        ...

    def operationServantY(self, bool: Any) -> Any:
        """operationServantY(bool)"""
        ...

    def operationSetMetrics(self, mode: int) -> Any:
        """operationSetMetrics(int mode)"""
        ...

    def operationSimplify(self) -> Any:
        """operationSimplify()"""
        ...

    def operationSmartAngle(self, bool: Any) -> Any:
        """operationSmartAngle(bool)"""
        ...

    def operationSmooth(self, bool: Any) -> Any:
        """operationSmooth(bool)"""
        ...

    def operationToBeziers(self) -> Any:
        """operationToBeziers()"""
        ...

    def operationToCurve(self) -> Any:
        """operationToCurve()"""
        ...

    def operationToLine(self) -> Any:
        """operationToLine()"""
        ...

    def operationToSplines(self) -> Any:
        """operationToSplines()"""
        ...

    def paint(self, *args: Any, **kwargs: Any) -> Any:
        """void paint(QPainter*)"""
        ...

    def placeAICB(self, position: QPointF, mime_data: Any) -> bool:
        """bool placeAICB(QPointF position, QString filename | QMimeData mime_data)"""
        ...

    def placeArtwork(self, position: QPointF, urls_list: list[QUrl]) -> bool:
        """bool placeArtwork(QPointF position, QList<QUrl> urls_list)"""
        ...

    def popupHost(self) -> Any:
        """YPopupHost* popupHost()"""
        ...

    def preview(self) -> Any:
        """preview()"""
        ...

    def producer(self) -> flObject:
        """flObject producer()"""
        ...

    def rectToUpdate(self) -> QRect:
        """QRect& rectToUpdate()"""
        ...

    def referencePoint(self) -> QPointF:
        """QPointF referencePoint()"""
        ...

    def refresh(self) -> Any:
        """refresh()"""
        ...

    def refreshAll(self) -> Any:
        """refreshAll()"""
        ...

    def refreshCanvasRect(self, arg0: QRectF) -> Any:
        """refreshCanvasRect(QRectF)"""
        ...

    def refreshGlyphRect(self, arg0: QRectF) -> Any:
        """refreshGlyphRect(QRectF)"""
        ...

    def regionToUpdate(self) -> QRegion:
        """QRegion& regionToUpdate()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeDeadSmartAngles(self) -> Any:
        """removeDeadSmartAngles()"""
        ...

    def removeDecorator(self, arg0: flVisualItem) -> None:
        """void removeDecorator(flVisualItem)"""
        ...

    def removeItem(self, arg0: flVisualItem) -> Any:
        """removeItem(flVisualItem)"""
        ...

    def removeTextBlock(self, arg0: flTextBlock) -> Any:
        """removeTextBlock(flTextBlock)"""
        ...

    def removedFromCanvas(self) -> Any:
        """removedFromCanvas()"""
        ...

    def removedFromWorkspace(self, arg0: flWorkspace) -> Any:
        """removedFromWorkspace(flWorkspace)"""
        ...

    def resetHighlight(self) -> Any:
        """resetHighlight()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def scale(self) -> float:
        """double scale()"""
        ...

    def scaled(self, d: float) -> float:
        """double scaled(double d)"""
        ...

    def select(self) -> Any:
        """select()"""
        ...

    def selectNode(self, arg0: flNodeInfo) -> Any:
        """selectNode(flNodeInfo)"""
        ...

    def selectNodes(self, *args: Any, **kwargs: Any) -> Any:
        """selectNodes(QList<flNodeInfo>)"""
        ...

    def selectedNodes(self) -> list[flNodeInfo]:
        """QList<flNodeInfo> selectedNodes()"""
        ...

    def selection(self) -> list[flVisualItem]:
        """QList<flVisualItem> selection()"""
        ...

    def setCursor(self, arg0: QCursor) -> Any:
        """setCursor(QCursor)"""
        ...

    def setCursorId(self, CursorId: Any) -> Any:
        """setCursorId(CursorId)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSelectedNodes(self, *args: Any, **kwargs: Any) -> Any:
        """setSelectedNodes(QList<flNodeInfo>, bool )"""
        ...

    def show(self) -> Any:
        """show()"""
        ...

    def slantTransform(self, glyph_info: flGlyphInfo) -> QTransform:
        """QTransform slantTransform(flGlyphInfo glyph_info)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def textBlocks(self) -> list[flTextBlock]:
        """QList<flTextBlock> textBlocks()"""
        ...

    def unselect(self) -> Any:
        """unselect()"""
        ...

    def unselectAll(self) -> bool:
        """bool unselectAll()"""
        ...

    def unselectAllNodes(self) -> bool:
        """bool unselectAllNodes()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateCanvasRectA(self, arg0: QRectF) -> Any:
        """updateCanvasRectA(QRectF)"""
        ...

    def updateMousePos(self, arg0: QPoint) -> Any:
        """updateMousePos(QPoint)"""
        ...

    def updateScreenRect(self, arg0: QRectF) -> Any:
        """updateScreenRect(QRectF)"""
        ...

    def updateScreenRegion(self, arg0: QRegion) -> Any:
        """updateScreenRegion(QRegion)"""
        ...

    def updateViewRect(self) -> Any:
        """updateViewRect()"""
        ...

    def updateViewport(self) -> Any:
        """updateViewport()"""
        ...

    def viewPortHasFocus(self) -> bool:
        """bool viewPortHasFocus()"""
        ...

    def viewPortRect(self) -> QRect:
        """QRect viewPortRect()"""
        ...

    def viewRect(self) -> QRectF:
        """QRectF viewRect()"""
        ...

    def zoomTo(self, canvas_rect: QRectF) -> Any:
        """zoomTo(QPointF canvas_point, double scale, ViewPointAlignment=vpCenter) | zoomTo(QRectF canvas_rect)"""
        ...

    def zoomToReaded(self) -> Any:
        """zoomToReaded()"""
        ...
    Listeners: dict
    SetMetricsAuto: int
    SetMetricsDefault: int
    SetMetricsZero: int
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hovered: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    locked: Any
    'bool'
    modelProducer: Any
    'flModelProducer'
    name: Any
    'object name'
    opacity: Any
    'double'
    owner: Any
    'flVisualItem'
    paper: Any
    'flPaper'
    refCnt: Any
    'object references count'
    selected: Any
    'bool'
    transform: Any
    'QTransform'
    type: Any
    'object type'
    viewPoint: Any
    'QPointF'
    viewPort: Any
    'QWidget*'
    viewTransform: Any
    'flTransform'
    visible: Any
    'bool'
    workspace: Any
    'flWorkspace'

class flContour:
    """flContour representation

Constructors:
  flContour()
  flContour(flObject)
  flContour(flContour)
  flContour(fgContour)
  flContour(id)
  flContour(list(Node)[, bool closed=false])
  flContour(list(QPointF)[, flNode::NodeType=flNode::On[, bool closed=false]])
  flContour(QRectF)
  flContour(QLineF)

Native bases: object

Supplemental documentation:
A closed or open path made of flNode objects. The captured declaration exposes `nodes` and `closed`. Obtain contours with the getContours method of a layer.

Example::

    for contour in layer.getContours():
        for node in contour.nodes:
            print(node.x, node.y)

Source: generated/fontlab.py: flContour captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def add(self, QPointF: Any) -> Any:
        """add(flNode | QPointF)"""
        ...

    def append(self, flContour: Any) -> Any:
        """append(list(flNode) | flContour)"""
        ...

    def appendMapped(self, flContour: Any, arg1: QTransform) -> Any:
        """appendMapped(list(flNode) | flContour, QTransform)"""
        ...

    def applyTransform(self) -> Any:
        """applyTransform()"""
        ...

    def assign(self, *args: Any, **kwargs: Any) -> Any:
        """assign(flContour | fgContour | list(flNode))"""
        ...

    def assignOwner(self) -> Any:
        """assignOwner()"""
        ...

    def at(self, index: int) -> flNode:
        """flNode at(int index)"""
        ...

    def autoG2(self, tolerance: float) -> Any:
        """autoG2(float tolerance)"""
        ...

    def beautify(self, precision: Any=...) -> bool:
        """bool beautify([int precision = 1])"""
        ...

    def bindDependencies(self) -> Any:
        """bindDependencies()"""
        ...

    def boundingBox(self, *args: Any, **kwargs: Any) -> Any:
        """QRectF boundingBox([QTransform])"""
        ...

    def breakContour(self, *args: Any, **kwargs: Any) -> Any:
        """(flContour, flNode, flNode)/Nothing breakContour(flNode) | flContour/Nothing breakContour(int node_ix)"""
        ...

    def breakContourExpanded(self, *args: Any, **kwargs: Any) -> Any:
        """flContour/Nothing breakContourExpanded(int node_ix | flNode [, float extrapolate_d]"""
        ...

    def calculate(self, *args: Any, **kwargs: Any) -> Any:
        """QPointF calculate(float t[, QTransform tx])"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def checkSmooth(self) -> Any:
        """checkSmooth()"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearNodes(self) -> Any:
        """clearNodes()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneMapped(self, *args: Any, **kwargs: Any) -> Any:
        """flContour cloneMapped(QTransform[, float ex_t0, float ex_t1])"""
        ...

    def cloneMappedByT(self, tx: QTransform, t0: float, t1: float) -> flContour:
        """flContour cloneMappedByT(QTransform tx, float t0, float t1)"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def cloneSelected(self, ignore_alone: Any=...) -> Any:
        """list(flContour)/Nothing cloneSelected([QTransform, [bool ignore_alone=true]])"""
        ...

    def compare(self, *args: Any, **kwargs: Any) -> Any:
        """(bool result, QPointF offset) compare(flContour, float error)"""
        ...

    def contains(self, QPointF: Any) -> bool:
        """bool contains(flContour knife | QPointF)"""
        ...

    def convertExToT(self, arg0: float) -> float:
        """float convertExToT(float)"""
        ...

    def convertTTtoCurve(self) -> Any:
        """convertTTtoCurve()"""
        ...

    def convertToFgContour(self, *args: Any, **kwargs: Any) -> Any:
        """fgContour convertToFgContour([QTransform tx])"""
        ...

    def convertTtoEx(self, arg0: float) -> float:
        """float convertTtoEx(float)"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def curvature(self, arg0: float) -> float:
        """float  curvature(float)"""
        ...

    def derivative(self, arg0: float) -> QPointF:
        """QPointF derivative(float)"""
        ...

    def distanceBetween(self, t0: float, step: Any=...) -> float:
        """float distanceBetween(float t0, float t1[, float step =0.1])"""
        ...

    def draw(self, pen: Any) -> Any:
        """draw(pen) - Draw the contour’s outline data to the given type-pen"""
        ...

    def drawPoints(self, *args: Any, **kwargs: Any) -> Any:
        """drawPoints(point-pen) - Draw the contour’s outline data to the given type-point-pen"""
        ...

    def extrapolateFirst(self, arg0: float) -> Any:
        """extrapolateFirst(float)"""
        ...

    def extrapolateLast(self, arg0: float) -> Any:
        """extrapolateLast(float)"""
        ...

    def fastAppend(self, *args: Any, **kwargs: Any) -> Any:
        """fastAppend( list(flNode) )"""
        ...

    def fastClone(self, ex_t0: float, ex_t1: float) -> flContour:
        """flContour fastClone(float ex_t0, float ex_t1)"""
        ...

    def fastCloneByT(self, t0: float, t1: float) -> flContour:
        """flContour fastCloneByT(float t0, float t1)"""
        ...

    def find(self, *args: Any, **kwargs: Any) -> Any:
        """flNode find(QPointF, float, flNode::NodeType)"""
        ...

    def findNearest(self, *args: Any, **kwargs: Any) -> Any:
        """(float out_nearest_t, float dist)/Nothing findNearest(QPointF shape_p[, int orientation=0])"""
        ...

    def findNearestNode(self, *args: Any, **kwargs: Any) -> Any:
        """(flNode, float new_maxd)/Nothing findNearestNode(QPointF p, flNode::NodeType node_type, float maxd)"""
        ...

    def findNearestOn(self, p: QPointF, base_t: float) -> Any:
        """float out_nearest_t/Nothing findNearestOn(QPointF  p, float base_t)"""
        ...

    def findNode(self, name: Any) -> Any:
        """flNode/Nothing findNode(uint id | string name)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getBoundedT(self, param_t: float, radius: float) -> float:
        """float getBoundedT(float param_t, float radius)"""
        ...

    def getChangesRect(self) -> QRectF:
        """QRectF getChangesRect()"""
        ...

    def getFirstPoint(self, *args: Any, **kwargs: Any) -> Any:
        """QPointF/Nothing getFirstPoint([int =0])"""
        ...

    def getLastPoint(self, *args: Any, **kwargs: Any) -> Any:
        """QPointF/Nothing getLastPoint([int =0])"""
        ...

    def getLength(self, int: Any=10) -> float:
        """float getLength([float t0, float t1,] int =10)"""
        ...

    def getLengthSquareBRect(self, *args: Any, **kwargs: Any) -> Any:
        """(float square, float length, QRectF brect) getLengthSquareBRect(float t0, float t1[, int step=10])"""
        ...

    def getNext(self, *args: Any, **kwargs: Any) -> Any:
        """flNode/Nothing getNext(index[, flNode::NodeType=flNode::On])"""
        ...

    def getNextT(self, *args: Any, **kwargs: Any) -> Any:
        """(bool, float) getNextT(float base_t, float offset)"""
        ...

    def getNodeAt(self, *args: Any, **kwargs: Any) -> Any:
        """flNode/Nothing getNodeAt(int idx[, flNode::NodeType = flNode::AnyNodeMask])"""
        ...

    def getPoint(self, *args: Any, **kwargs: Any) -> Any:
        """QPointF/Nothing getPoint(int idx[, flNode::NodeType = flNode::On])"""
        ...

    def getPrev(self, *args: Any, **kwargs: Any) -> Any:
        """flNode/Nothing getPrev(index[, flNode::NodeType=flNode::On])"""
        ...

    def getPrevT(self, *args: Any, **kwargs: Any) -> Any:
        """(bool, float) getPrevT(float base_t, float offset)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getSegment(self, i0: int, i1: int, left: bool) -> Any:
        """list(flNode) getSegment(int i0, int i1, bool left)"""
        ...

    def getSelectedBoundingBox(self) -> QRectF:
        """QRectF getSelectedBoundingBox()"""
        ...

    def getSelectedNodes(self) -> Any:
        """list(flNode)/Nothing getSelectedNodes()"""
        ...

    def getSquare(self) -> float:
        """double getSquare()"""
        ...

    def getT(self, arg0: flNode) -> float:
        """float getT(flNode)"""
        ...

    def getUpdateRect(self, ex_t: float) -> QRectF:
        """QRectF getUpdateRect(float ex_t)"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasIntersPoints(self, arg0: flContour) -> bool:
        """bool hasIntersPoints(flContour)"""
        ...

    def hasSelected(self, SelectionMode: Any) -> bool:
        """bool hasSelected(SelectionMode)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def improve(self) -> bool:
        """bool improve()"""
        ...

    def indentParamT(self, base_t: float, step: Any=...) -> float:
        """float indentParamT(float base_t, float indent[, float step =0.1])"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def inkBox(self, *args: Any, **kwargs: Any) -> Any:
        """QRectF inkBox([QTransform tx])"""
        ...

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """insert(index, flNode | list(flNode) )"""
        ...

    def insertNodeTo(self, t: float) -> flNode:
        """flNode insertNodeTo(float t)"""
        ...

    def insertSafeNodeTo(self, t: float, dst: float) -> flNode:
        """flNode insertSafeNodeTo(float t, float dst)"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isAllNodesSelected(self) -> bool:
        """bool isAllNodesSelected()"""
        ...

    def isCompatible(self, arg0: flContour, strong: bool) -> bool:
        """bool isCompatible(flContour, bool strong)"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isFirst(self, arg0: flNode) -> bool:
        """bool isFirst(flNode)"""
        ...

    def isLast(self, arg0: flNode) -> bool:
        """bool isLast(flNode)"""
        ...

    def isSelected(self, arg0: float) -> bool:
        """bool isSelected(float)"""
        ...

    def mapParamT(self, arg0: float, arg1: float, arg2: float) -> float:
        """float mapParamT(float, float, float)"""
        ...

    def move(self, arg0: QPointF) -> Any:
        """move(QPointF)"""
        ...

    def nodes(self) -> Any:
        """list(flNode) nodes()"""
        ...

    def normalAt(self, *args: Any, **kwargs: Any) -> Any:
        """float normalAt(float t[, QTransform])"""
        ...

    def normalPoint(self, t: float, length: float) -> QPointF:
        """QPointF normalPoint(float t, float length)"""
        ...

    def normalizeExT(self, arg0: float) -> float:
        """float normalizeExT(float)"""
        ...

    def path(self) -> QPainterPath:
        """QPainterPath path()"""
        ...

    def pointInside(self, pt: QPointF) -> Any:
        """pointInside(QPointF pt) - Bool indicating if the point pt in the black area of the contour"""
        ...

    def pointf(self, index: int) -> QPointF:
        """QPointF pointf(int index)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeAt(self, index: int) -> Any:
        """removeAt(int index)"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeLast(self) -> Any:
        """removeLast()"""
        ...

    def removeNodesBetween(self, prev: flNode, next: flNode) -> Any:
        """removeNodesBetween(flNode prev,  flNode next)"""
        ...

    def removeOne(self, arg0: flNode) -> Any:
        """removeOne(flNode)"""
        ...

    def replace(self, old_node: flNode, new_node: flNode) -> Any:
        """replace(flNode old_node, flNode new_node)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def reverse(self) -> Any:
        """reverse() - Reverse the direction of the contour"""
        ...

    def secondDerivative(self, arg0: float) -> QPointF:
        """QPointF secondDerivative(float)"""
        ...

    def segment(self, t: float) -> Any:
        """CurveEx/Nothing segment(float t)"""
        ...

    def segments(self) -> Any:
        """list(CurveEx) segments()"""
        ...

    def selectedPath(self) -> QPainterPath:
        """QPainterPath selectedPath()"""
        ...

    def selectionChanged(self) -> Any:
        """selectionChanged()"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setNext(self, int: Any, arg1: QPointF) -> flNode:
        """flNode setNext(int, QPointF)"""
        ...

    def setPoint(self, index: int, p: QPointF) -> flNode:
        """flNode setPoint(int index, QPointF p)"""
        ...

    def setPrev(self, int: Any, arg1: QPointF) -> flNode:
        """flNode setPrev(int, QPointF)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSelectedNodes(self, bool: Any) -> Any:
        """setSelectedNodes(bool)"""
        ...

    def setStartPoint(self, i: int) -> bool:
        """bool setStartPoint(int i)"""
        ...

    def simplify(self, precision: float, lossy: bool, extremes: bool) -> Any:
        """simplify(float precision, bool lossy, bool extremes)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def takeNodes(self) -> Any:
        """list(flNode) takeNodes()"""
        ...

    def tangent(self, t: float) -> float:
        """float tangent(float t)"""
        ...

    def toBeziers(self, tolerance: float) -> Any:
        """toBeziers(float tolerance)"""
        ...

    def toSplines(self, tolerance: float, short_splines: bool) -> Any:
        """toSplines(float tolerance, bool short_splines)"""
        ...

    def unselectAll(self) -> Any:
        """unselectAll()"""
        ...

    def unselectedPath(self) -> QPainterPath:
        """QPainterPath unselectedPath()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateG2(self, all_nodes: bool) -> Any:
        """updateG2(bool all_nodes)"""
        ...

    def updateHobby(self, all_nodes: bool) -> Any:
        """updateHobby(bool all_nodes)"""
        ...

    def updateIndices(self) -> Any:
        """updateIndices()"""
        ...

    def validateExT(self, *args: Any, **kwargs: Any) -> Any:
        """(new_ex_t, bool) validateExT(float ex_t)"""
        ...

    def validateIndex(self, *args: Any, **kwargs: Any) -> Any:
        """(new_inx, bool) validateIndex(int inx)"""
        ...

    def validateSmartR(self, *args: Any, **kwargs: Any) -> Any:
        """(new_r, max_available_r, bool) validateSmartR(int node_ix, float r)"""
        ...

    def validateT(self, *args: Any, **kwargs: Any) -> Any:
        """(new_t, bool) validateT(float t)"""
        ...

    def validatedT(self, t: float) -> float:
        """float validatedT(float t)"""
        ...

    def verifySmooth(self) -> Any:
        """verifySmooth()"""
        ...
    FigureType: dict
    bounds: Any
    'The bounds of the contour as tuple (xMin, yMin, xMax, yMax) or None'
    clockwise: Any
    'Bool indicating if the contour’s winding direction is clockwise'
    closed: Any
    'closed attribute'
    closedT1: Any
    'closedT1 attr'
    first: Any
    'first node'
    flObjectFlags: dict
    font: Any
    'The contour’s parent font'
    glyph: Any
    'The contour’s parent glyph'
    hasChanges: Any
    'bool'
    hasCorners: Any
    'hasCorners'
    hasHistoryStates: Any
    'bool'
    hasSmartAngle: Any
    'hasSmartAngle'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isComplete: Any
    'isComplete'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isTT: Any
    'is truetype'
    isValid: Any
    'bool'
    last: Any
    'last node'
    layer: Any
    'The contour’s parent layer'
    name: Any
    'object name'
    nodesCount: Any
    'nodes count'
    paramT0: Any
    'paramT0 attr'
    paramT1: Any
    'paramT1 attr'
    prevLast: Any
    'last but one node'
    refCnt: Any
    'object references count'
    reversed: Any
    'reversed'
    selection: Any
    'selection list (list<bool>)'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flContourInfo:
    """flContourInfo representation

Constructors:
  flContourInfo()
  flContourInfo(flObject)
  flContourInfo(flContour, flSearchInfo)
  flContourInfo(flContour, flShapeInfo)
  flContourInfo(flContour, flContourInfo)
  flContourInfo(flContour, QTransform)

Native bases: object

Supplemental documentation:
Contour information. The captured declaration exposes `contour`, `shapeInfo`, `glyphInfo`, `getHitNode`, `getNodesInfo`, `cloneSelected`, `brectOnCanvas`, `combine`, `dist` and `transform`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flContourInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def brectOnCanvas(self) -> QRectF:
        """QRectF brectOnCanvas()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def cloneSelected(self) -> list[flContourInfo]:
        """QList<flContourInfo> cloneSelected()"""
        ...

    def combine(self, transform: QTransform) -> Any:
        """combine(QTransform transform)"""
        ...

    def createInstance(self) -> flContourInfo:
        """flContourInfo createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getHitNode(self, canvas_pos: QPointF, node_mask: Any=...) -> Any:
        """flNodeInfo/Nothing getHitNode(QPointF canvas_pos, double dist[, int node_mask=flNode::AnyNodeMask])"""
        ...

    def getNodesInfo(self) -> list[flNodeInfo]:
        """QList<flNodeInfo> getNodesInfo()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getUpdateRect(self, ex_t: float) -> QRectF:
        """QRectF getUpdateRect(double ex_t)"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def paramExT(self) -> float:
        """double paramExT()"""
        ...

    def paramT(self) -> float:
        """double paramT()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setExT(self, ex_t: float) -> Any:
        """setExT(double ex_t)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    contour: Any
    'flContour>'
    dist: Any
    'double dist'
    flObjectFlags: dict
    glyphInfo: Any
    'flObject - glyph info'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    shapeInfo: Any
    'flShapeInfo'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flEvent:
    """flEvent representation

Constructors:
  flEvent(flEvent)
  flEvent(flEvent(EventType type[, int modifiers=-1])

Native bases: object

Supplemental documentation:
An event with `type` (EventType) and `modifiers` (int) attributes and an `EventType` dict. It is created as a copy `flEvent(flEvent)` or as `flEvent(EventType type[, int modifiers=-1])`.

Source: generated/fontlab.py: flEvent captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    EventType: dict
    modifiers: Any
    'int'
    type: Any
    'EventType'

class flExpression:
    """flExpression representation

Constructors:
  flExpression()
  flExpression(flObject)
  flExpression(flExpression)
  flExpression(string)

Native bases: object

Supplemental documentation:
Expression holder. The captured declaration exposes `expression`, `hasExpression`, `hasError`, `error`, `clearError`, `isNeedToComplete`, `resetReady`, `ready` and `variables`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flExpression captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearError(self) -> Any:
        """clearError()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def expression(self, aliases: dict[str, str]) -> str:
        """QString expression(QMap<QString, QString> aliases)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasError(self) -> bool:
        """bool hasError()"""
        ...

    def hasExpression(self) -> bool:
        """bool hasExpression()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isNeedToComplete(self) -> bool:
        """bool isNeedToComplete()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def resetReady(self) -> Any:
        """resetReady()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def variables(self, *args: Any, **kwargs: Any) -> Any:
        """QStringList variables([QMap<QString, QString> aliases])"""
        ...
    error: Any
    'int'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    ready: Any
    'bool'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flGlyph:
    """flGlyph representation

Constructors:
  flGlyph()
  flGlyph(flGlyph)
  flGlyph(flObject)
  flGlyph(fgGlyph, fgFont)

Native bases: object

Supplemental documentation:
A FontLab editing glyph containing flLayer objects. The captured declaration exposes `name` and `layers`; iterate `layers` to inspect layer names. Unicode assignments belong to the associated fontgate glyph; they are not flGlyph attributes.

Example::

    glyph = fl.CurrentGlyph()
    if glyph:
        print(glyph.name)
        for layer in glyph.layers:
            print(layer.name)

Source: generated/fontlab.py: flGlyph captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addLayer(self, back: Any=...) -> None:
        """void addLayer(flLayer[, bool back = false])"""
        ...

    def addLayers(self, *args: Any, **kwargs: Any) -> Any:
        """void addLayers(list(flLayer))"""
        ...

    def applyTransform(self, *args: Any, **kwargs: Any) -> Any:
        """applyTransform([QTransform transform])"""
        ...

    def assignFontGateData(self, arg0: fgFontGateData, doGuide: bool=True, doHints: bool=True, doAnchors: bool=True) -> None:
        """void assignFontGateData(fgFontGateData, bool doGuide = true, bool doHints = true, bool doAnchors = true)"""
        ...

    def bindDependencies(self) -> Any:
        """bindDependencies()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearUpdateFgGlyphs(self) -> Any:
        """clearUpdateFgGlyphs()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createInstance(self) -> flGlyph:
        """flGlyph createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivateAll(self) -> Any:
        """deactivateAll()"""
        ...

    def ensureFgData(self, arg0: fgGlyph) -> fgFontGateData:
        """fgFontGateData ensureFgData(fgGlyph)"""
        ...

    def ensureMaskLayer(self) -> flLayer:
        """flLayer ensureMaskLayer()"""
        ...

    def fillFgData(self, doGuides: bool, doHints: bool) -> fgFontGateData:
        """fgFontGateData fillFgData(bool doGuides, bool doHints)"""
        ...

    def findLayer(self, cs: Any=...) -> flLayer:
        """flLayer findLayer(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])"""
        ...

    def findLayerCreate(self, cs: Any=...) -> flLayer:
        """flLayer findLayerCreate(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])"""
        ...

    def findVerticalGuideline(self, arg0: str) -> Any:
        """double/Nothing findVerticalGuideline(QString)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getAuditInfo(self) -> Any:
        """list(flAuditInfo) getAuditInfo()"""
        ...

    def getLSB(self, tr: QTransform) -> float:
        """double getLSB(QTransform tr)"""
        ...

    def getLayerByName(self, create: Any=...) -> flLayer:
        """flLayer getLayerByName(QString[, bool create =false])"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getRSB(self, tr: QTransform) -> float:
        """double getRSB(QTransform tr)"""
        ...

    def getSB(self, *args: Any, **kwargs: Any) -> Any:
        """(double l, double r) getSB(QTransform tr)"""
        ...

    def glyphName(self) -> str:
        """QString glyphName()"""
        ...

    def hasFontAudit(self) -> bool:
        """bool hasFontAudit()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasInstance(self, arg0: fgGlyph) -> bool:
        """bool hasInstance(fgGlyph)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def haveSelected(self, SelectionMode: Any) -> bool:
        """bool haveSelected(SelectionMode)"""
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def horzReflection(self) -> bool:
        """bool horzReflection()"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def inkBox(self, tx: Any=...) -> QRectF:
        """QRectF inkBox([QTransform tx = QTransform()])"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def interpolateInstance(self, location: flLocation, round: bool) -> flLayer:
        """flLayer interpolateInstance(flLocation location, bool round)"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isUnbindedDependecies(self) -> bool:
        """bool isUnbindedDependecies()"""
        ...

    def linkInstances(self, arg0: flGlyph, arg1: fgGlyph) -> bool:
        """bool linkInstances(flGlyph, fgGlyph)"""
        ...

    def masters2PS(self, precision: float) -> bool:
        """bool masters2PS(double precision)"""
        ...

    def masters2TT(self, precision: float) -> bool:
        """bool masters2TT(double precision)"""
        ...

    def measurementLine(self) -> Any:
        """double/Nothing measurementLine()"""
        ...

    def prepareTransformationData(self) -> Any:
        """prepareTransformationData()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeEmptyShapes(self) -> Any:
        """removeEmptyShapes()"""
        ...

    def removeLayer(self, arg0: flLayer) -> None:
        """void removeLayer(flLayer)"""
        ...

    def resetInkBox(self) -> Any:
        """resetInkBox()"""
        ...

    def resetTransformationData(self) -> Any:
        """resetTransformationData()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setAllShapesSelected(self, bool: Any) -> Any:
        """setAllShapesSelected(bool)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setLSB(self, v: float, move_guidelines: bool, tr: QTransform) -> bool:
        """bool setLSB(double v, bool move_guidelines, QTransform tr)"""
        ...

    def setLayers(self, *args: Any, **kwargs: Any) -> Any:
        """void setLayers(list(flLayer))"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setRSB(self, v: float, tr: QTransform) -> bool:
        """bool setRSB(double v, QTransform tr)"""
        ...

    def setReflected(self, *args: Any, **kwargs: Any) -> Any:
        """setReflected(bool, bool)"""
        ...

    def setSB(self, l: float, r: float, move_guidelines: bool, all_layers: bool, tr: QTransform) -> bool:
        """bool setSB(double l, double r, bool move_guidelines, bool all_layers, QTransform tr)"""
        ...

    def setTag(self, arg0: str, bool: Any) -> None:
        """void setTag(QString, bool)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def unselectAllNodes(self) -> Any:
        """unselectAllNodes()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateActiveLayer(self, bool: Any) -> flLayer:
        """flLayer updateActiveLayer(bool)"""
        ...

    def updateAudit(self, *args: Any, **kwargs: Any) -> Any:
        """void updateAudit(list(int))"""
        ...

    def updateFgGlyph(self, id: int) -> Any:
        """updateFgGlyph(uint id)"""
        ...

    def updateSidebearings(self, nofify: bool) -> bool:
        """bool updateSidebearings(bool nofify)"""
        ...

    def updatedFgGlyphs(self) -> Any:
        """list(uint32_t) updatedFgGlyphs()"""
        ...

    def vertReflection(self) -> bool:
        """bool vertReflection()"""
        ...

    def virtualTags(self) -> Any:
        """QSet<QString>/Nothing virtualTags()"""
        ...
    activeLayer: Any
    'flLayer'
    advanceWidth: Any
    'double'
    ascender: Any
    'double'
    bodyLayer: Any
    'flLayer'
    bodyRect: Any
    'QRectF'
    boundingBox: Any
    'QRectF'
    descender: Any
    'double'
    fgGlyph: Any
    'fgGlyph'
    fgGlyphId: Any
    'FgTypeId'
    fgPackage: Any
    'fgFont'
    flObjectFlags: dict
    glyphRect: Any
    'QRectF'
    hasBody: Any
    'bool'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    lastModified: Any
    'QDateTime'
    layers: Any
    'list(flLayer)'
    leftMetric: Any
    'QPointF'
    lib: Any
    'dict(name, QVariant)'
    mark: Any
    'int'
    metricsLeft: Any
    'QString'
    metricsRect: Any
    'QRectF'
    metricsRight: Any
    'QString'
    metricsWidth: Any
    'QString'
    name: Any
    'QString'
    nodesCount: Any
    'int'
    note: Any
    'QString'
    otGlyphClass: Any
    'int'
    otLigaturesCount: Any
    'int'
    otMarkClass: Any
    'int'
    package: Any
    'flObject'
    refCnt: Any
    'object references count'
    rightMetric: Any
    'QPointF'
    tags: Any
    'QStringList'
    type: Any
    'object type'

    def layer_names(self) -> list[str]:
        """List layer names; immutable native classes use extensions.layer_names."""
        ...

    def has_layer(self, name: str) -> bool:
        """Check for a named layer; see extensions.has_layer on immutable classes."""
        ...

class flGlyphInfo:
    """flGlyphInfo representation

Constructors:
  flGlyphInfo()
  flGlyphInfo(flObject)
  flGlyphInfo(flGlyphInfo)
  flGlyphInfo(flGlyph, QTransform)
  flGlyphInfo(fgSymbol, fgGlyph, fgFont)

Native bases: object

Supplemental documentation:
Glyph information. The captured declaration exposes `glyph`, `boundingBox`, `createBoundingBox`, `applyTransform`, `applyTransformTo`, `getNearbyContours`, `getTopHitShape`, `hitToShape`, `kerningOffset`, `setKerningOffset`, `setBoundAscender`, `setBoundDescender`, `setBoundLeft`, `setBoundRight`, `setGlyphScale`, `fontSize`, `leftOffset`, `rightOffset`, `isActive`, `isSelected` and `isNullGlyph`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flGlyphInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def applyTransform(self) -> Any:
        """applyTransform()"""
        ...

    def applyTransformTo(self, type: int) -> Any:
        """applyTransformTo(uint type)"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createBoundingBox(self) -> Any:
        """createBoundingBox()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getNearbyContours(self, arg0: QPointF, max_dist: float, exclude_attr: str) -> Any:
        """list(flContourInfo) getNearbyContours(QPointF, double max_dist, QString exclude_attr)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getTopHitShape(self, arg0: QPointF) -> Any:
        """flShapeInfo/Nothing getTopHitShape(QPointF)"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def hitToShape(self, arg0: QPointF) -> bool:
        """bool hitToShape(QPointF)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def kerningOffset(self, useKerning: bool) -> float:
        """double kerningOffset(bool useKerning)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setBoundAscender(self, double: Any) -> Any:
        """setBoundAscender(double)"""
        ...

    def setBoundDescender(self, double: Any) -> Any:
        """setBoundDescender(double)"""
        ...

    def setBoundLeft(self, double: Any) -> Any:
        """setBoundLeft(double)"""
        ...

    def setBoundRight(self, double: Any) -> Any:
        """setBoundRight(double)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setGlyphScale(self, *args: Any, **kwargs: Any) -> Any:
        """setGlyphScale(double, double)"""
        ...

    def setKerningOffset(self, offs: float) -> Any:
        """setKerningOffset(double offs)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    bodyRectOnCanvas: Any
    'QRectF'
    boundingBox: Any
    'QRectF'
    brectOnCanvas: Any
    'QRectF'
    changedRect: Any
    'QRectF'
    dist: Any
    'double'
    flObjectFlags: dict
    fontSize: Any
    'int'
    glyph: Any
    'flGlyph'
    glyphRectCanvas: Any
    'QRectF'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isActive: Any
    'bool'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isNullGlyph: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isSelected: Any
    'bool'
    isValid: Any
    'bool'
    leftOffset: Any
    'double'
    metricsRectOnCanvas: Any
    'QRectF'
    name: Any
    'QString'
    refCnt: Any
    'object references count'
    rightOffset: Any
    'double'
    shapesBoundingBoxOnCanvas: Any
    'QRectF'
    state: Any
    'uint'
    symbol: Any
    'fgSymbol'
    textBlock: Any
    'flTextBlock, int'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flGraphicsInfo:
    """flGraphicsInfo representation

Constructors:
  flGraphicsInfo()
  flGraphicsInfo(flObject)
  flGraphicsInfo(flGraphicsInfo)

Native bases: object

Supplemental documentation:
Graphics information. The captured declaration exposes the attribute `transform`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flGraphicsInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flGuideLine:
    """flGuideLine representation

Constructors:
  flGuideLine()
  flGuideLine(flObject)
  flGuideLine(flGuideLine)
  flGuideLine(double angle, QPointF canvas_point, uint=flSnaps::Vector, SnapObjectsStyle=gsPageGuideline)
  flGuideLine(QLineF line, uint=flSnaps::Vector, SnapObjectsStyle=gsPageGuideline)
  flGuideLine(QPointF center, QPointF vector_point, uint =flSnaps::Vector, SnapObjectsStyle=gsPageGuideline)

Native bases: object

Supplemental documentation:
An editing guideline with `angle`, `centerPoint` and `vectorPoint` attributes. The captured declaration identifies `centerPoint` and `vectorPoint` as QPointF values, and `linef` as a QLineF. `name` identifies the object; `color` is a QColor value. Consult the retained constructors for supported line and point forms.

Source: generated/fontlab.py: flGuideLine captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def applyTransform(self, arg0: QTransform) -> None:
        """void applyTransform(QTransform)"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def counterPaper(self) -> int:
        """int counterPaper()"""
        ...

    def createInstance(self) -> flGuideLine:
        """flGuideLine createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def createPowerGuides(self, arg0: fgFont, arg1: flLayer, horizontal: bool, vertical: bool, use_glyph_guides: Any=...) -> bool:
        """bool createPowerGuides(fgFont, flLayer, bool horizontal, bool vertical, bool diagonal[, bool use_glyph_guides=true[, bool use_font_guides = true]])"""
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def disconnectFromContour(self) -> Any:
        """disconnectFromContour()"""
        ...

    def distanceTo(self, arg0: QPointF, mode: int) -> float:
        """double distanceTo(QPointF, uint mode)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getHashCode(self, arg0: QPointF, angle: float) -> int:
        """long getHashCode(QPointF, double angle)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isGuideLine(self, arg0: flObject) -> bool:
        """bool isGuideLine(flObject)"""
        ...

    def isHorizontal(self, a: Any=...) -> bool:
        """bool isHorizontal([double a=1])"""
        ...

    def isSnapLine(self, arg0: flObject) -> bool:
        """bool isSnapLine(flObject)"""
        ...

    def isVertical(self, a: Any=...) -> bool:
        """bool isVertical([double a=1])"""
        ...

    def offsetTo(self, arg0: QPointF, mode: int) -> QPointF:
        """QPointF offsetTo(QPointF, uint mode)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def reset(self) -> Any:
        """reset()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSnapFlag(self, role: int, snapFlags: int) -> Any:
        """setSnapFlag(uint role, uint snapFlags)"""
        ...

    def setSnapFlagValue(self, role: int, bool: Any) -> Any:
        """setSnapFlagValue(uint role, bool)"""
        ...

    def snapFlag(self, role: int) -> int:
        """uint snapFlag(uint role)"""
        ...

    def sortGuideLines(self, ascending: Any=...) -> Any:
        """list(flGuideLine) sortGuideLines(list(flGuideLine)[, bool ascending = true])"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    angle: Any
    'double'
    angleMode: Any
    'SnapAngleMode'
    center: Any
    'flNode'
    centerPoint: Any
    'QPointF'
    color: Any
    'QColor'
    constraints: Any
    'QRectF'
    expression: Any
    'QString'
    extLinef: Any
    'QLineF'
    extPosition: Any
    'double'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasColor: Any
    'bool'
    hasExpression: Any
    'bool'
    hasExtLine: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hasTags: Any
    'bool'
    id: Any
    'object id'
    isAbsoluteMarkerPos: Any
    'bool'
    isChanged: Any
    'bool'
    isExluded: Any
    'bool'
    isHint: Any
    'bool'
    isInUse: Any
    'bool'
    isMeasurementLine: Any
    'bool'
    isNull: Any
    'bool'
    isPassive: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isShortGuideline: Any
    'bool'
    isValid: Any
    'bool'
    isVerticalQuarter: Any
    'bool'
    isZone: Any
    'bool'
    length: Any
    'double'
    linef: Any
    'QLineF'
    markers: Any
    'list(flMarkerPoint)'
    markersStructVersion: Any
    'int'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    snapFlags: Any
    'uint'
    style: Any
    'SnapObjectsStyle'
    tags: Any
    'QSet<QString>'
    type: Any
    'object type'
    vector: Any
    'flNode'
    vectorPoint: Any
    'QPointF'

class flHintingParameters:
    """flHintingParameters representation

Constructors:
  flHintingParameters() - default

Native bases: object

Supplemental documentation:
Font-level hinting parameters. The captured declaration exposes the method `init` and the attributes `blueFuzz`, `blueScale`, `blueShift`, `codePPM`, `dropoutPPM`, `flex`, `fontDirectionHint`, `forceBold`, `forceBoldTreshold`, `lowestRecPPEM`, `maxFunctionDefs`, `maxInstructionDefs`, `maxStackElements`, `maxStorage`, `maxTwilightPoints`, `maxZones`, `stemSnapLimit` and `zonePPM`. It is created as `flHintingParameters()`. Note the captured spelling `forceBoldTreshold`.

Source: generated/fontlab.py: flHintingParameters captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def init(self) -> Any:
        """init()"""
        ...
    blueFuzz: Any
    'int'
    blueScale: Any
    'double'
    blueShift: Any
    'int'
    codePPM: Any
    'int'
    dropoutPPM: Any
    'int'
    flex: Any
    'bool'
    fontDirectionHint: Any
    'int'
    forceBold: Any
    'bool'
    forceBoldTreshold: Any
    'double'
    lowestRecPPEM: Any
    'int'
    maxFunctionDefs: Any
    'int'
    maxInstructionDefs: Any
    'int'
    maxStackElements: Any
    'int'
    maxStorage: Any
    'int'
    maxTwilightPoints: Any
    'int'
    maxZones: Any
    'int'
    stemSnapLimit: Any
    'int'
    zonePPM: Any
    'int'

class flInstance:
    """flInstance representation

Constructors:
  flInstance()
  flInstance(string name, string tsn, flLocation location)

Native bases: object

Supplemental documentation:
A font instance with the string attributes `name`, `sgn`, `tsn`, `weight` and `width`, the bool attributes `bold`, `exportable` and `italic`, the numeric attributes `slv` (int) and `weightValue` (double), and a `location` attribute. The captured declaration exposes `autoSGN`, `autoSLV`, `autoTSN` and `setSLV`. It is created as `flInstance()` or as `flInstance(name, tsn, location)`.

Source: generated/fontlab.py: flInstance captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def autoSGN(self, *args: Any, **kwargs: Any) -> Any:
        """string autoSGN(const string &tfn)"""
        ...

    def autoSLV(self) -> int:
        """int autoSLV()"""
        ...

    def autoTSN(self) -> Any:
        """string autoTSN()"""
        ...

    def setSLV(self, bold: bool, italic: bool) -> Any:
        """setSLV(bool bold, bool italic)"""
        ...
    bold: Any
    'bool'
    exportable: Any
    'bool'
    italic: Any
    'bool'
    location: Any
    'flLocation'
    name: Any
    'string'
    sgn: Any
    'string'
    slv: Any
    'int'
    tsn: Any
    'string'
    weight: Any
    'string'
    weightValue: Any
    'double'
    width: Any
    'string'

class flItems:
    """flItems representation

Constructors:
  flItems()

Native bases: object

Supplemental documentation:
Application items. The captured declaration exposes `appendRecentFile`, `buildRecentList`, `clearRecentFiles`, `getCursor`, `getCursorId`, `instance`, `notifyActivateGlyph`, `notifyClipboardChanged`, `notifyGlyphActivated`, `notifyGlyphDeactivated`, `notifyFontSelected` and `notifyEditModeChanged`. It is created with no captured constructor overloads.

Source: generated/fontlab.py: flItems captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def appendRecentFile(self, arg0: str, file_name: str) -> Any:
        """appendRecentFile(QString, QString file_name)"""
        ...

    def buildRecentList(self, arg0: str) -> Any:
        """QStringList/Nothing buildRecentList(QString)"""
        ...

    def clearRecentFiles(self, arg0: str) -> Any:
        """clearRecentFiles(QString )"""
        ...

    def createObject(self, type: int, key: flObject) -> flObject:
        """flObject createObject(int type, flObject key)"""
        ...

    def getCursor(self, CursorId: Any) -> QCursor:
        """QCursor getCursor(CursorId)"""
        ...

    def getCursorId(self, arg0: str, hot_x: int, hot_y: int) -> Any:
        """CursorId getCursorId(QString, int hot_x, int hot_y)"""
        ...

    def guidelinesEditingEnabled(self) -> bool:
        """bool guidelinesEditingEnabled()"""
        ...

    def init(self) -> Any:
        """init()"""
        ...

    def instance(self) -> flItems:
        """flItems instance()"""
        ...

    def notifyActivateGlyph(self, arg0: flGlyphInfo) -> Any:
        """notifyActivateGlyph(flGlyphInfo)"""
        ...

    def notifyAnchorsChanged(self) -> Any:
        """notifyAnchorsChanged()"""
        ...

    def notifyApplyTranformFrame(self) -> Any:
        """notifyApplyTranformFrame()"""
        ...

    def notifyAuditHovered(self, id: int) -> Any:
        """notifyAuditHovered(uint id)"""
        ...

    def notifyAutoShapseChanges(self, arg0: flLayer) -> Any:
        """notifyAutoShapseChanges(flLayer)"""
        ...

    def notifyAvailableToSelectNodes(self, *args: Any, **kwargs: Any) -> Any:
        """notifyAvailableToSelectNodes( list(list(flNodeInfo)) )"""
        ...

    def notifyBrushModeSelected(self, smart: int) -> Any:
        """notifyBrushModeSelected(int smart)"""
        ...

    def notifyBrushSelected(self, PaintBrush: Any) -> Any:
        """notifyBrushSelected(PaintBrush)"""
        ...

    def notifyBrushSet(self) -> Any:
        """notifyBrushSet()"""
        ...

    def notifyCancelTranformFrame(self) -> Any:
        """notifyCancelTranformFrame()"""
        ...

    def notifyCanvasAttached(self, arg0: flCanvas) -> Any:
        """notifyCanvasAttached(flCanvas)"""
        ...

    def notifyCanvasEnterFocus(self, arg0: flCanvas) -> Any:
        """notifyCanvasEnterFocus(flCanvas)"""
        ...

    def notifyCanvasLeaveFocus(self, arg0: flCanvas) -> Any:
        """notifyCanvasLeaveFocus(flCanvas)"""
        ...

    def notifyCanvasRemoved(self, arg0: flCanvas) -> Any:
        """notifyCanvasRemoved(flCanvas)"""
        ...

    def notifyChangesApplied(self, recursive: Any=...) -> Any:
        """notifyChangesApplied([QString title, flObject object / list(flObject)[, bool recursive=false]])"""
        ...

    def notifyClipboardChanged(self) -> Any:
        """notifyClipboardChanged()"""
        ...

    def notifyColorSet(self, arg0: QColor, b: bool) -> Any:
        """notifyColorSet(QColor, bool b)"""
        ...

    def notifyCommandSelected(self) -> Any:
        """notifyCommandSelected()"""
        ...

    def notifyCurrentPaperChanged(self, arg0: flPaper) -> Any:
        """notifyCurrentPaperChanged(flPaper)"""
        ...

    def notifyDropDone(self, canvas: flCanvas) -> Any:
        """notifyDropDone(flCanvas& canvas)"""
        ...

    def notifyEditActionFinished(self) -> Any:
        """notifyEditActionFinished()"""
        ...

    def notifyEditActionStarted(self) -> Any:
        """notifyEditActionStarted()"""
        ...

    def notifyEditModeChanged(self, mode: Any) -> Any:
        """notifyEditModeChanged(EditMode mode)"""
        ...

    def notifyEditingChanged(self, arg0: flAbstractEditor) -> Any:
        """notifyEditingChanged(flAbstractEditor)"""
        ...

    def notifyEditingFinished(self) -> Any:
        """notifyEditingFinished()"""
        ...

    def notifyFeaturesChanged(self, package_id: int, binary: bool) -> Any:
        """notifyFeaturesChanged(uint package_id, bool binary)"""
        ...

    def notifyFontPanelActivated(self, b: bool) -> Any:
        """notifyFontPanelActivated(bool b)"""
        ...

    def notifyFontSelected(self, *args: Any, **kwargs: Any) -> Any:
        """notifyFontSelected(uint id);"""
        ...

    def notifyFrameSelected(self, *args: Any, **kwargs: Any) -> Any:
        """notifyFrameSelected(list(flNodeInfo))"""
        ...

    def notifyGalleryChanged(self, arg0: flObject) -> Any:
        """notifyGalleryChanged(flObject)"""
        ...

    def notifyGlyphActivated(self, arg0: flGlyphInfo) -> Any:
        """notifyGlyphActivated(flGlyphInfo)"""
        ...

    def notifyGlyphDeactivated(self) -> Any:
        """notifyGlyphDeactivated()"""
        ...

    def notifyGlyphDoubleClick(self, arg0: flGlyphInfo) -> Any:
        """notifyGlyphDoubleClick(flGlyphInfo)"""
        ...

    def notifyGlyphIdSelected(self, packageId: int, glyphId: int, replace: bool) -> Any:
        """notifyGlyphIdSelected(uint packageId, uint glyphId, bool replace)"""
        ...

    def notifyGlyphMaximized(self, arg0: flGlyphInfo) -> Any:
        """notifyGlyphMaximized(flGlyphInfo)"""
        ...

    def notifyGlyphPinPointChanged(self, pin_point: Any=...) -> Any:
        """notifyGlyphPinPointChanged([flPinPoint pin_point = flnull[, flGlyphInfo glyph_info = flnull]])"""
        ...

    def notifyGlyphPinPointCreated(self, arg0: flGlyphInfo) -> Any:
        """notifyGlyphPinPointCreated(flGlyphInfo)"""
        ...

    def notifyGlyphUpdated(self, packageId: int, glyphId: int) -> Any:
        """notifyGlyphUpdated(uint packageId, uint glyphId)"""
        ...

    def notifyGlyphWindowInactive(self) -> Any:
        """notifyGlyphWindowInactive()"""
        ...

    def notifyGlyphsUpdated(self, packageId: int, glyphIds: set[Any]) -> Any:
        """notifyGlyphsUpdated(uint packageId, QSet<uint32_t> glyphIds)"""
        ...

    def notifyGraphEdgeSelectionChanged(self, arg0: flObject) -> Any:
        """notifyGraphEdgeSelectionChanged(flObject)"""
        ...

    def notifyGuidelinesChanged(self, arg0: flCanvas) -> Any:
        """notifyGuidelinesChanged(flCanvas)"""
        ...

    def notifyGuidelinesSelected(self, *args: Any, **kwargs: Any) -> Any:
        """notifyGuidelinesSelected(list(flGuideLine))"""
        ...

    def notifyHidePanels(self) -> Any:
        """notifyHidePanels()"""
        ...

    def notifyHistoryChanged(self) -> Any:
        """notifyHistoryChanged()"""
        ...

    def notifyKeyHash(self) -> Any:
        """notifyKeyHash()"""
        ...

    def notifyKeyRepeat(self, key: int) -> Any:
        """notifyKeyRepeat(int key)"""
        ...

    def notifyKeySlash(self) -> Any:
        """notifyKeySlash()"""
        ...

    def notifyLayerActivated(self, arg0: flLayer) -> Any:
        """notifyLayerActivated(flLayer)"""
        ...

    def notifyModelChanged(self) -> Any:
        """notifyModelChanged()"""
        ...

    def notifyNodeChanged(self, arg0: flNodeInfo) -> Any:
        """notifyNodeChanged(flNodeInfo)"""
        ...

    def notifyNodesSelected(self, *args: Any, **kwargs: Any) -> Any:
        """notifyNodesSelected(list(flNodeInfo))"""
        ...

    def notifyPackageAdded(self, arg0: flPackage) -> Any:
        """notifyPackageAdded(flPackage)"""
        ...

    def notifyPackageClosed(self, arg0: flPackage) -> Any:
        """notifyPackageClosed(flPackage)"""
        ...

    def notifyPackageContentUpdated(self, id: int) -> Any:
        """notifyPackageContentUpdated(uint id)"""
        ...

    def notifyPackageReaded(self, arg0: flPackage) -> Any:
        """notifyPackageReaded(flPackage)"""
        ...

    def notifyPackageRemoved(self, arg0: flPackage) -> Any:
        """notifyPackageRemoved(flPackage)"""
        ...

    def notifyPackageUpdated(self, id: Any) -> Any:
        """notifyPackageUpdated(flPackage | uint id)"""
        ...

    def notifyPackagesRemoved(self, *args: Any, **kwargs: Any) -> Any:
        """notifyPackagesRemoved(list(flObject))"""
        ...

    def notifyPackagesUpdated(self) -> Any:
        """notifyPackagesUpdated()"""
        ...

    def notifyPinPointChanged(self, pin_point: Any=...) -> Any:
        """notifyPinPointChanged([flPinPoint pin_point = flnull[, flShapeInfo shape_info = flnull]])"""
        ...

    def notifyPinPointCreated(self, arg0: flShapeInfo) -> Any:
        """notifyPinPointCreated(flShapeInfo)"""
        ...

    def notifyPinPointSelectionChanged(self) -> Any:
        """notifyPinPointSelectionChanged()"""
        ...

    def notifyPinSelected(self, id: int) -> Any:
        """notifyPinSelected(uint id)"""
        ...

    def notifyPreferencesChanged(self) -> Any:
        """notifyPreferencesChanged()"""
        ...

    def notifyProjectClosed(self) -> Any:
        """notifyProjectClosed()"""
        ...

    def notifyProjectReaded(self, file_name: str) -> Any:
        """notifyProjectReaded(QString file_name)"""
        ...

    def notifyProjectSaved(self, file_name: str) -> Any:
        """notifyProjectSaved(QString file_name)"""
        ...

    def notifyPropertiesChanged(self, arg0: flObject) -> Any:
        """notifyPropertiesChanged(flObject)"""
        ...

    def notifyRenderingBegin(self, info: str) -> Any:
        """notifyRenderingBegin(QString info)"""
        ...

    def notifyRenderingFinished(self, success: bool) -> Any:
        """notifyRenderingFinished(bool success)"""
        ...

    def notifyReplaceGlyphsByFgId(self, *args: Any, **kwargs: Any) -> Any:
        """notifyReplaceGlyphsByFgId(list(unsigned long), int replace_count)"""
        ...

    def notifyRequestChangeCurrentClipboard(self, xml: str) -> Any:
        """notifyRequestChangeCurrentClipboard(QString xml)"""
        ...

    def notifyRequestNewProject(self) -> Any:
        """notifyRequestNewProject()"""
        ...

    def notifyRequestOpenProject(self, file_name: str) -> Any:
        """notifyRequestOpenProject(QString file_name)"""
        ...

    def notifyRequestPasteAction(self) -> Any:
        """notifyRequestPasteAction()"""
        ...

    def notifyRequestShowWelcome(self) -> Any:
        """notifyRequestShowWelcome()"""
        ...

    def notifyRequestShowWorkspace(self) -> Any:
        """notifyRequestShowWorkspace()"""
        ...

    def notifySCVItemsChanged(self) -> Any:
        """notifySCVItemsChanged()"""
        ...

    def notifyScrollToGlyph(self, arg0: flGlyphInfo) -> Any:
        """notifyScrollToGlyph(flGlyphInfo)"""
        ...

    def notifySelectionChanged(self) -> Any:
        """notifySelectionChanged()"""
        ...

    def notifyShapeActivated(self, arg0: flShapeInfo) -> Any:
        """notifyShapeActivated(flShapeInfo)"""
        ...

    def notifyShapeDeactivated(self) -> Any:
        """notifyShapeDeactivated()"""
        ...

    def notifyShowPanels(self) -> Any:
        """notifyShowPanels()"""
        ...

    def notifySnapLineChanged(self, arg0: flGuideLine) -> Any:
        """notifySnapLineChanged(flGuideLine)"""
        ...

    def notifySnapLinesChanged(self, *args: Any, **kwargs: Any) -> Any:
        """notifySnapLinesChanged(list(flGuideLine))"""
        ...

    def notifyStaplerPreviewEnabled(self, enbl: bool) -> Any:
        """notifyStaplerPreviewEnabled(bool enbl)"""
        ...

    def notifyStickerCreated(self) -> Any:
        """notifyStickerCreated()"""
        ...

    def notifyStopButtonClicked(self) -> Any:
        """notifyStopButtonClicked()"""
        ...

    def notifyTextBlockAdded(self, arg0: flTextBlock) -> Any:
        """notifyTextBlockAdded(flTextBlock)"""
        ...

    def notifyTextBlockItemActivated(self, check_tools: Any=...) -> Any:
        """notifyTextBlockItemActivated(flTextBlockItem[, bool check_tools = true])"""
        ...

    def notifyTextBlockItemChanged(self, arg0: flTextBlockItem) -> Any:
        """notifyTextBlockItemChanged(flTextBlockItem)"""
        ...

    def notifyTextBlockItemDeactivated(self, arg0: flTextBlockItem) -> Any:
        """notifyTextBlockItemDeactivated(flTextBlockItem)"""
        ...

    def notifyTextBlockItemMaximized(self, arg0: flTextBlockItem) -> Any:
        """notifyTextBlockItemMaximized(flTextBlockItem)"""
        ...

    def notifyTextBlockItemNormalized(self, arg0: flTextBlockItem) -> Any:
        """notifyTextBlockItemNormalized(flTextBlockItem)"""
        ...

    def notifyTextBlockItemsSelectionChanged(self, arg0: flCanvas) -> Any:
        """notifyTextBlockItemsSelectionChanged(flCanvas)"""
        ...

    def notifyTextBlockRemoved(self, arg0: flTextBlock) -> Any:
        """notifyTextBlockRemoved(flTextBlock)"""
        ...

    def notifyToolChanged(self, tool: flBasicTool) -> Any:
        """notifyToolChanged(flBasicTool& tool)"""
        ...

    def notifyTransformDataChanged(self, TransformFrame: Any) -> Any:
        """notifyTransformDataChanged(TransformFrame)"""
        ...

    def notifyTransformFrameChanged(self, arg0: flObject) -> Any:
        """notifyTransformFrameChanged(flObject)"""
        ...

    def notifyTransformFrameFinished(self, arg0: flObject) -> Any:
        """notifyTransformFrameFinished(flObject)"""
        ...

    def notifyTransformFrameStarted(self, arg0: flObject) -> Any:
        """notifyTransformFrameStarted(flObject)"""
        ...

    def notifyTransformStarted(self) -> Any:
        """notifyTransformStarted()"""
        ...

    def notifyUpdateHistory(self) -> Any:
        """notifyUpdateHistory()"""
        ...

    def notifyUpdateStaplers(self) -> Any:
        """notifyUpdateStaplers()"""
        ...

    def notifyViewportChanged(self, old_viewport: QWidget, new_viewport: QWidget) -> Any:
        """notifyViewportChanged(QWidget* old_viewport, QWidget* new_viewport)"""
        ...

    def notifyWorkspaceClosed(self, arg0: flWorkspace) -> Any:
        """notifyWorkspaceClosed(flWorkspace)"""
        ...

    def notifyWorkspaceHasChanges(self, c: bool) -> Any:
        """notifyWorkspaceHasChanges(bool c)"""
        ...

    def notifyWorkspaceInitialized(self, arg0: flWorkspace) -> Any:
        """notifyWorkspaceInitialized(flWorkspace)"""
        ...

    def notifyZoomChanged(self, canvas: flCanvas) -> Any:
        """notifyZoomChanged(flCanvas& canvas)"""
        ...

    def requestActivateNodesTool(self) -> Any:
        """requestActivateNodesTool()"""
        ...

    def requestActivateShapeTool(self) -> Any:
        """requestActivateShapeTool()"""
        ...

    def requestActivateTransformTool(self) -> Any:
        """requestActivateTransformTool()"""
        ...

    def requestCheckHistoryInitIndex(self, arg0: flGlyphInfo) -> Any:
        """requestCheckHistoryInitIndex(flGlyphInfo)"""
        ...

    def requestContent(self, *args: Any, **kwargs: Any) -> Any:
        """requestContent(fgSymbolList characters, int cursorLocation"""
        ...

    def requestFontInfoDlg(self) -> Any:
        """requestFontInfoDlg()"""
        ...

    def requestGlyphActivate(self, pid: int, gid: int) -> Any:
        """requestGlyphActivate(uint pid, uint gid)"""
        ...

    def requestGlyphDeactivate(self) -> Any:
        """requestGlyphDeactivate()"""
        ...

    def requestGlyphReactivated(self) -> Any:
        """requestGlyphReactivated()"""
        ...

    def requestLoadingFont(self, font_source: str) -> Any:
        """requestLoadingFont(QString font_source)"""
        ...

    def requestPackageAcceptFonts(self, arg0: flPackage) -> Any:
        """requestPackageAcceptFonts(flPackage)"""
        ...

    def requestPackageBorn(self, arg0: flPackage) -> Any:
        """requestPackageBorn(flPackage)"""
        ...

    def requestPackagePostProcess(self, arg0: flPackage, encoding: str) -> Any:
        """requestPackagePostProcess(flPackage, QString encoding)"""
        ...

    def requestPermissionsForDragGuidelineByNode(self, canvas_pos: QPointF, modifiers: int) -> bool:
        """bool requestPermissionsForDragGuidelineByNode(QPointF canvas_pos, uint modifiers)"""
        ...

    def requestProgressMessage(self, message: str) -> Any:
        """requestProgressMessage(QString message)"""
        ...

    def requestProgressRange(self, v: int) -> Any:
        """requestProgressRange(int v)"""
        ...

    def requestProgressShow(self, b: bool) -> Any:
        """requestProgressShow(bool b)"""
        ...

    def requestProgressValue(self, v: int) -> Any:
        """requestProgressValue(int v)"""
        ...

    def requestSaveBar(self, b: bool) -> Any:
        """requestSaveBar(bool b)"""
        ...

    def requestSaveBarValue(self, v: int) -> Any:
        """requestSaveBarValue(int v)"""
        ...

    def requestSubContent(self, *args: Any, **kwargs: Any) -> Any:
        """requestSubContent(fgSymbolList characters, int cursorLocation"""
        ...

    def requestUpdateActiveShape(self, arg0: flShapeInfo) -> Any:
        """requestUpdateActiveShape(flShapeInfo)"""
        ...

    def resetToolCursor(self) -> Any:
        """resetToolCursor()"""
        ...

    def setCursor(self, *args: Any, **kwargs: Any) -> Any:
        """setCursor(CursorId cursor_id);"""
        ...

    def setEllipseCurvature(self, d: float) -> Any:
        """setEllipseCurvature(double d)"""
        ...

    def setEllipseData(self, p0: QPointF, p1: QPointF) -> Any:
        """setEllipseData(QPointF p0, QPointF p1)"""
        ...

    def setGuidelinesEditingEnabled(self, b: bool) -> Any:
        """setGuidelinesEditingEnabled(bool b)"""
        ...

    def setMeterData(self, p0: QPointF, p1: QPointF) -> Any:
        """setMeterData(QPointF p0, QPointF p1)"""
        ...

    def setParameterName(self, arg0: flObject, arg1: str) -> Any:
        """setParameterName(flObject, QString)"""
        ...

    def setTransformation(self, code: int, value: QPointF) -> Any:
        """setTransformation(int code, QPointF value)"""
        ...

    def shapeBuilders(self) -> Any:
        """list(flObject) shapeBuilders()"""
        ...

    def strToType(self, arg0: str) -> int:
        """int strToType(QString)"""
        ...

    def typeToStr(self, type: int) -> str:
        """QString typeToStr(int type)"""
        ...
    ItemStates: dict
    ItemType: dict
    bBrush: int
    bCount: int
    bEllipse: int
    bGlyph: int
    bGuideline: int
    bMeter: int
    bMetrics: int
    bPen: int
    bPin: int
    bSingleNode: int
    bText: int
    bTransform: int
    qobject: Any
    'QObject'
    transformRotate: int
    transformScale: int
    transformShift: int
    transformSlant: int
    workspace: Any
    'flObject'

class flLayer:
    """flLayer representation

Constructors:
  flLayer()
  flLayer(flObject)
  flLayer(flGlyph)
  flLayer('title')

Native bases: object

Supplemental documentation:
A drawing layer holding shapes, components and anchors. The captured declaration exposes `getContours`, `name`, `shapes`, `components`, `anchors`, `advanceWidth`, `boundingBox` and `isService`. Retrieve contours with `getContours`; the captured flLayer has no contours attribute.

Example::

    layer = glyph.layers[0]
    for contour in layer.getContours():
        for node in contour.nodes:
            print(node.x, node.y)

Source: generated/fontlab.py: flLayer captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addAnchor(self, arg0: flPinPoint) -> Any:
        """addAnchor(flPinPoint)"""
        ...

    def addComponent(self, component: flComponent) -> Any:
        """addComponent(flComponent component)"""
        ...

    def addShape(self, arg0: flShape) -> flShape:
        """flShape addShape(flShape)"""
        ...

    def addShapes(self, *args: Any, **kwargs: Any) -> Any:
        """addShapes(list(flShape))"""
        ...

    def appendGuidelines(self, *args: Any, **kwargs: Any) -> Any:
        """appendGuidelines(list(flGuideLine))"""
        ...

    def applyTransform(self, *args: Any, **kwargs: Any) -> Any:
        """applyTransform([QTransform transform])"""
        ...

    def assignFgLayer(self, arg0: fgLayer, doGuides: bool, doHints: bool, doAnchors: bool, doShapes: bool, doTTH: bool) -> Any:
        """assignFgLayer(fgLayer, bool doGuides, bool doHints, bool doAnchors, bool doShapes, bool doTTH)"""
        ...

    def assignStyle(self, layer: flLayer) -> Any:
        """assignStyle(flLayer layer)"""
        ...

    def autohint(self) -> bool:
        """bool autohint()"""
        ...

    def bindDependencies(self) -> Any:
        """bindDependencies()"""
        ...

    def buildAuto(self) -> bool:
        """bool buildAuto()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def checkTags(self, glyph_tags: set[str], item_tags: str) -> bool:
        """bool checkTags(QSet<QString> glyph_tags, QString item_tags)"""
        ...

    def cleanEmptyShapes(self) -> Any:
        """cleanEmptyShapes()"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearAnchors(self) -> Any:
        """clearAnchors()"""
        ...

    def clearAudit(self) -> None:
        """void clearAudit()"""
        ...

    def clearComponents(self) -> Any:
        """clearComponents()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneCustom(self, *args: Any, **kwargs: Any) -> Any:
        """(flLayer, list(flObject)) cloneCustom(uint)"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def compare(self, layer: flLayer, error: float) -> bool:
        """bool compare(flLayer layer, double error)"""
        ...

    def compoundMakeSelected(self, set_active: bool, process_all: bool) -> bool:
        """bool compoundMakeSelected(bool set_active, bool process_all)"""
        ...

    def compoundMakeSelectedToShapes(self, set_active: Any=...) -> bool:
        """bool compoundMakeSelectedToShapes([bool set_active =true])"""
        ...

    def contourRect(self) -> QRectF:
        """QRectF contourRect()"""
        ...

    def createAnchor(self, name: Any, p: QPointF, location: int) -> flPinPoint:
        """flPinPoint createAnchor(string name, QPointF p, int location)"""
        ...

    def createInstance(self, *args: Any, **kwargs: Any) -> Any:
        """Native fontlab.flLayer.createInstance; argument details are not documented."""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivateAllShapes(self) -> Any:
        """deactivateAllShapes()"""
        ...

    def fillFgAnchors(self, arg0: fgLayer) -> Any:
        """fillFgAnchors(fgLayer)"""
        ...

    def fillFgGuides(self, arg0: fgLayer) -> Any:
        """fillFgGuides(fgLayer)"""
        ...

    def findAnchor(self, name: str) -> flPinPoint:
        """flPinPoint findAnchor(QString name)"""
        ...

    def findNearestNode(self, *args: Any, **kwargs: Any) -> Any:
        """(flShape, flNode best_node, double maxd) findNearestNode(QPointF, flNode::NodeType node_type, double maxd)"""
        ...

    def findNode(self, *args: Any, **kwargs: Any) -> Any:
        """(flNode, QPointF)/Nothing findNode(string name)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getActiveComposite(self) -> Any:
        """flShape/Nothing getActiveComposite()"""
        ...

    def getActiveShape(self, *args: Any, **kwargs: Any) -> Any:
        """(flShape, QTransform)/Nothing getActiveShape([bool = true])"""
        ...

    def getAuditInfo(self) -> Any:
        """list(flAuditInfo) getAuditInfo()"""
        ...

    def getContours(self) -> Any:
        """list(flContour) getContours()"""
        ...

    def getImgLayer(self, create: bool) -> flLayer:
        """flLayer getImgLayer(bool create)"""
        ...

    def getMaskLayer(self, create: bool) -> flLayer:
        """flLayer getMaskLayer(bool create)"""
        ...

    def getMasterPosition(self) -> Any:
        """QMap<QString, double>/Nothing getMasterPosition()"""
        ...

    def getOwnerComposite(self, *args: Any, **kwargs: Any) -> Any:
        """flShapeInfo getOwnerComposite(flShape, QTransform) / flShapeData getOwnerComposite(flShape)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getSelected(self, SelectionMode: Any) -> Any:
        """list(flContour)/Nothing getSelected(SelectionMode)"""
        ...

    def getShapes(self, shape_type: Any) -> Any:
        """list(flShape) getShapes(ShapeType shape_type)"""
        ...

    def getTthCode(self, fg_layer: fgLayer, itr: fgTTInterpreter) -> bool:
        """bool getTthCode(fgLayer fg_layer, fgTTInterpreter itr)"""
        ...

    def getTthData(self, fg_layer: fgLayer, itr: fgTTInterpreter) -> Any:
        """list(bytes) / Nothing getTthData(fgLayer fg_layer, fgTTInterpreter itr)"""
        ...

    def getTthProgram(self, itr: fgTTInterpreter) -> str:
        """QString getTthProgram(fgTTInterpreter itr)"""
        ...

    def goDown(self, arg0: flShape) -> bool:
        """bool goDown(flShape)"""
        ...

    def goUp(self, arg0: flShape) -> bool:
        """bool goUp(flShape)"""
        ...

    def hasFontAudit(self) -> bool:
        """bool hasFontAudit()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasShape(self, arg0: flShape) -> bool:
        """bool hasShape(flShape)"""
        ...

    def hasShapeData(self, arg0: flShapeData) -> bool:
        """bool hasShapeData(flShapeData)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def haveSelected(self, SelectionMode: Any) -> bool:
        """bool haveSelected(SelectionMode)"""
        ...

    def hints2links(self) -> bool:
        """bool hints2links()"""
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def inkBox(self, tx: Any=...) -> QRectF:
        """QRectF inkBox([QTransform tx = QTransform()])"""
        ...

    def insertShape(self, index: int, shape: flShape) -> flShape:
        """flShape insertShape(int index, flShape shape)"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isBack(self, arg0: flShape) -> bool:
        """bool isBack(flShape)"""
        ...

    def isCompatible(self, arg0: flLayer, strong: bool) -> bool:
        """bool isCompatible(flLayer, bool strong)"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isFront(self, arg0: flShape) -> bool:
        """bool isFront(flShape)"""
        ...

    def killAuto(self) -> Any:
        """killAuto()"""
        ...

    def nodesCount(self) -> int:
        """int nodesCount()"""
        ...

    def prepareTransformationData(self) -> Any:
        """prepareTransformationData()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeAllShapes(self, shape_type: Any=...) -> Any:
        """removeAllShapes([ShapeType shape_type=AnyShape])"""
        ...

    def removeAnchor(self, arg0: flPinPoint) -> Any:
        """removeAnchor(flPinPoint)"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeGuides(self, horizontal: bool, vertical: bool) -> bool:
        """bool removeGuides(bool horizontal, bool vertical)"""
        ...

    def removeHints(self, horizontal: bool, vertical: bool) -> bool:
        """bool removeHints(bool horizontal, bool vertical)"""
        ...

    def removeShape(self, recursive: Any=...) -> Any:
        """removeShape(flShape[, bool recursive=true])"""
        ...

    def reorderShapes(self, *args: Any, **kwargs: Any) -> Any:
        """reorderShapes(QList<uint>)"""
        ...

    def replaceShape(self, old_shape: flShape, new_shape: flShape) -> Any:
        """replaceShape(flShape old_shape, flShape new_shape)"""
        ...

    def resetInkBox(self) -> Any:
        """resetInkBox()"""
        ...

    def resetMetricsLeft(self) -> Any:
        """resetMetricsLeft()"""
        ...

    def resetMetricsRight(self) -> Any:
        """resetMetricsRight()"""
        ...

    def resetMetricsWidth(self) -> Any:
        """resetMetricsWidth()"""
        ...

    def resetTransformationData(self) -> Any:
        """resetTransformationData()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def selectAll(self) -> Any:
        """selectAll()"""
        ...

    def sendToBack(self, arg0: flShape) -> bool:
        """bool sendToBack(flShape)"""
        ...

    def sendToFront(self, arg0: flShape) -> bool:
        """bool sendToFront(flShape)"""
        ...

    def setActive(self) -> Any:
        """setActive()"""
        ...

    def setActiveShape(self, arg0: flShape) -> Any:
        """setActiveShape(flShape)"""
        ...

    def setAllShapesSelected(self, bool: Any) -> Any:
        """setAllShapesSelected(bool)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setGlyphComponents(self, result: list[Any], width: float, package: flPackage, colorize: bool, flags: int) -> bool:
        """bool setGlyphComponents(QList<GlyphComponent> result, double width, flPackage package, bool colorize, uint flags)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setWireframeColorIx(self, int: Any) -> Any:
        """setWireframeColorIx(int)"""
        ...

    def sortShapes(self) -> Any:
        """sortShapes()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def takeShapes(self, shape_type: Any) -> list[flShape]:
        """QList<flShape> takeShapes(ShapeType shape_type)"""
        ...

    def transferNames(self, layer: flLayer) -> Any:
        """transferNames(flLayer layer)"""
        ...

    def transferTTH(self, arg0: flLayer) -> bool:
        """bool transferTTH(flLayer)"""
        ...

    def tthAutohint(self, make_hints: bool, itr: fgTTInterpreter) -> Any:
        """tthAutohint(bool make_hints, fgTTInterpreter itr)"""
        ...

    def tthFixZones(self, itr: fgTTInterpreter) -> Any:
        """tthFixZones(fgTTInterpreter itr)"""
        ...

    def tthReassignStems(self, itr: fgTTInterpreter) -> Any:
        """tthReassignStems(fgTTInterpreter itr)"""
        ...

    def tthReassignZones(self, itr: fgTTInterpreter, bool: Any) -> Any:
        """tthReassignZones(fgTTInterpreter itr, bool)"""
        ...

    def tthRemoveCommands(self, vertical: bool, horizontal: bool) -> Any:
        """tthRemoveCommands(bool vertical, bool horizontal)"""
        ...

    def tthRemoveDeltas(self, middle: bool, final: bool) -> Any:
        """tthRemoveDeltas(bool middle, bool final)"""
        ...

    def unselectAllNodes(self) -> Any:
        """unselectAllNodes()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateAnchors(self) -> Any:
        """updateAnchors()"""
        ...

    def updateAudit(self, *args: Any, **kwargs: Any) -> Any:
        """void updateAudit(list(int))"""
        ...

    def updateGuidelineNode(self, node: flNode) -> flNode:
        """flNode updateGuidelineNode(flNode node)"""
        ...

    def updatePreviewLinks(self) -> None:
        """void updatePreviewLinks()"""
        ...
    advanceHeight: Any
    'double'
    advanceWidth: Any
    'double'
    anchors: Any
    'list(flPinPoint) anchors()'
    autoLayer: Any
    'bool'
    boundingBox: Any
    'QRectF boundingBox()'
    components: Any
    'list(name, transform)'
    componentsCount: Any
    'int componentsCount()'
    compoundReleaseSelected: Any
    'bool compoundReleaseSelected();'
    counterAnchors: Any
    'int counterAnchors()'
    flObjectFlags: dict
    glyph: Any
    'flGlyph'
    guidelines: Any
    'list(flGuideLine) guidelines()'
    hasAdvanceHeight: Any
    'bool hasAdvanceHeight()'
    hasAdvanceWidth: Any
    'bool hasAdvanceWidth()'
    hasBody: Any
    'bool hasBody()'
    hasChanges: Any
    'bool'
    hasComponents: Any
    'bool hasComponents()'
    hasComposites: Any
    'bool hasComposites()'
    hasGuides: Any
    'bool hasGuides()'
    hasHints: Any
    'bool hasHints()'
    hasHistoryStates: Any
    'bool'
    hasNote: Any
    'bool hasNote()'
    hasTTData: Any
    'bool hasTTData()'
    hasTTH: Any
    'bool hasTTH()'
    haveActiveComposite: Any
    'bool haveActiveComposite()'
    id: Any
    'object id'
    isActive: Any
    'bool isActive()'
    isAllSelected: Any
    'bool'
    isBodyLayer: Any
    'bool isBodyLayer()'
    isChanged: Any
    'bool'
    isImg: Any
    'bool isImg()'
    isImgLayer: Any
    'bool isImgLayer()'
    isLocked: Any
    'bool'
    isLockedI: Any
    'bool isLockedI()'
    isMaskLayer: Any
    'bool isMaskLayer()'
    isMasterLayer: Any
    'bool isMasterLayer()'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isService: Any
    'bool'
    isServiceMA: Any
    'bool isServiceMA()'
    isValid: Any
    'bool'
    isVisible: Any
    'bool'
    isVisibleA: Any
    'bool isVisibleA()'
    isWireframe: Any
    'bool'
    lib: Any
    'dict(name, QVariant)'
    mark: Any
    'double'
    metricsLeft: Any
    'QString'
    metricsRight: Any
    'QString'
    metricsWidth: Any
    'QString'
    name: Any
    'object name'
    note: Any
    'QString'
    opacity: Any
    'double'
    recipe: Any
    'QString'
    refCnt: Any
    'object references count'
    shapes: Any
    'list(flShape) shapes()'
    shapesCount: Any
    'int shapesCount()'
    transform: Any
    'QTransform'
    ttData: Any
    'fgTrueTypeData'
    tthProgram: Any
    'QList<flTTHCommand>'
    type: Any
    'object type'
    wireframeColor: Any
    'QColor'

class flLayerAttributes:
    """Data wrapper

Native bases: object

Supplemental documentation:
A data wrapper with the attributes `isActive`, `isLocked`, `isService`, `isVisible`, `isWireframe` and `wireframeColor`. The captured declaration exposes `asDict` (represent the object as a dictionary) and `asTuple` (represent it as a tuple).

Source: generated/fontlab.py: flLayerAttributes captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as dictionary"""
        ...

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        """represent object as tuple"""
        ...
    isActive: Any
    isLocked: Any
    isService: Any
    isVisible: Any
    isWireframe: Any
    wireframeColor: Any

class flLayerInfo:
    """flLayerInfo representation

Constructors:
  flLayerInfo()
  flLayerInfo(flObject)
  flLayerInfo(flLayerInfo)
  flLayerInfo(flLayer, QTransform)
  flLayerInfo(flLayer, flObject glyph_info, QTransform)

Native bases: object

Supplemental documentation:
Layer information. The captured declaration exposes `layer`, `glyphInfo`, `combine`, `dist`, `transform` and `brectOnCanvas`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flLayerInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def brectOnCanvas(self) -> QRectF:
        """QRectF brectOnCanvas()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def combine(self, transform: QTransform) -> Any:
        """combine(QTransform transform)"""
        ...

    def createInstance(self) -> flLayerInfo:
        """flLayerInfo createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    dist: Any
    'double dist'
    flObjectFlags: dict
    glyphInfo: Any
    'flObject - glyph info'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    layer: Any
    'flLayer'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flLocation:
    """flLocation representation

Constructors:
  flLocation(flLocation)
  flLocation()

Native bases: object

Supplemental documentation:
A design-space location. The captured declaration exposes no named members, only the native constructors `flLocation()` and `flLocation(flLocation)`. The flAxis method locationName takes an flLocation.

Source: generated/fontlab.py: flLocation captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

class flMarkerPoint:
    """flMarkerPoint representation

Constructors:
  flMarkerPoint()
  flMarkerPoint(flObject)
  flMarkerPoint(flMarkerPoint)
  flMarkerPoint(double marker_pos, uint markerFlags, flSnaps::MarkerKey key)

Native bases: object

Supplemental documentation:
Marker point. The captured declaration exposes `markerFlag`, `setMarkerFlag`, `markerFlags`, `isStem`, `isSelected`, `key` and `position`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flMarkerPoint captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createInstance(self) -> flMarkerPoint:
        """flMarkerPoint createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def markerFlag(self, role: int) -> int:
        """uint markerFlag(uint role)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setMarkerFlag(self, role: int, markerFlags: int) -> Any:
        """setMarkerFlag(uint role, uint markerFlags)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isSelected: Any
    'bool'
    isStem: Any
    'bool'
    isValid: Any
    'bool'
    key: Any
    'flSnaps::MarkerKey key()'
    markerFlags: Any
    'uint'
    name: Any
    'object name'
    position: Any
    'double'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flModel:
    """flModel representation

Constructors:
None, static only methods

Native bases: object

Supplemental documentation:
A static-only model class with no constructor. The captured declaration exposes the methods `createObject`, `getClassMask`, `instance`, `isClassMask`, `notifyGlyphChanged`, `notifyGlyphUpdate`, `notifyGlyphsChanged` and `typeToStr`, and the dict attributes `ModelType` and `ObjectParameter`. Call `instance` to obtain the flModel object.

Source: generated/fontlab.py: flModel captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def createObject(self, type: int) -> Any:
        """flObject/Nothing createObject(int type)"""
        ...

    def getClassMask(self, type: int) -> int:
        """int  getClassMask(int type)"""
        ...

    def instance(self) -> flModel:
        """flModel instance()"""
        ...

    def isClassMask(self, type: int) -> bool:
        """bool isClassMask(int type)"""
        ...

    def notifyGlyphChanged(self, fg_glyphId: Any) -> Any:
        """notifyGlyphChanged(unsigned long fg_glyphId)"""
        ...

    def notifyGlyphUpdate(self, fg_glyphId: Any) -> Any:
        """notifyGlyphUpdate(unsigned long fg_glyphId)"""
        ...

    def notifyGlyphsChanged(self, glyphs: set[Any]) -> Any:
        """notifyGlyphsChanged(QSet<uint32_t> glyphs)"""
        ...

    def typeToStr(self, flObject: Any) -> str:
        """QString typeToStr(int type | flObject)"""
        ...
    ModelType: dict
    ObjectParameter: dict

class flModelProducer:
    """flModelProducer representation

Constructors:
  flModelProducer()
  flModelProducer(flModelProducer)
  flModelProducer(flObject)
  flModelProducer(flCanvas)

Native bases: object

Supplemental documentation:
A model producer. The captured declaration exposes `copyToClipboard`, `getClipboardData`, `getObjectsFromClipboard`, `getObjectsFromData`, `countGlyphsInData`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flModelProducer captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def copyToClipboard(self, package_id: Any, objects: list[flObject]) -> Any:
        """copyToClipboard(objId package_id, QList<flObject> objects)"""
        ...

    def countGlyphsInData(self, *args: Any, **kwargs: Any) -> Any:
        """int countGlyphsInData(QByteArray *data)"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getClipboardData(self, *args: Any, **kwargs: Any) -> Any:
        """QByteArray getClipboardData(objId package_id, QList<flObject>)"""
        ...

    def getObjectsFromClipboard(self) -> Any:
        """flObjects/Nothing getObjectsFromClipboard()"""
        ...

    def getObjectsFromData(self, *args: Any, **kwargs: Any) -> Any:
        """flObjects/Nothing getObjectsFromData(QByteArray *data)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flMouseEvent:
    """flMouseEvent representation

Constructors:
  flMouseEvent(flMouseEvent)

Native bases: object

Supplemental documentation:
A mouse event. The captured declaration exposes the attributes `button`, `buttons`, `delta`, `firstPressed`, `global_`, `modifiers`, `movement`, `origin`, `prev` and `type`. It is created as a copy `flMouseEvent(flMouseEvent)`.

Source: generated/fontlab.py: flMouseEvent captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    button: Any
    'Qt::MouseButton'
    buttons: Any
    'Qt::MouseButtons'
    delta: Any
    'QPointF'
    firstPressed: Any
    'bool'
    global_: Any
    'QPoint'
    modifiers: Any
    'int'
    movement: Any
    'float'
    origin: Any
    'QPoint'
    prev: Any
    'QPoint'
    type: Any
    'EventType'

class flNode:
    """flNode representation

Constructors:
  flNode()
  flNode(Node) - make clone
  flNode(QPointF position[, string nodeType="on"[, int nodeKind=None]])
  flNode(double x, double y[, string nodeType="on"[, int nodeKind=None]])

Native bases: object

Supplemental documentation:
A contour node. The captured declaration exposes `x`, `y`, `type` and `smooth`. The `type` member distinguishes on-curve points from off-curve control points. Read or assign `x` and `y` on the original native object.

Source: generated/fontlab.py: flNode captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def angleTo(self, p: QPointF) -> float:
        """double angleTo(QPointF p)"""
        ...

    def applyTransform(self, arg0: QTransform) -> Any:
        """applyTransform(QTransform)"""
        ...

    def canBeHobby(self) -> bool:
        """bool canBeHobby()"""
        ...

    def canBeSmooth(self) -> bool:
        """bool canBeSmooth()"""
        ...

    def canCollapse(self) -> bool:
        """bool canCollapse()"""
        ...

    def canImprove(self) -> bool:
        """bool canImprove()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def checkVectors(self) -> bool:
        """bool checkVectors()"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearStored(self) -> Any:
        """clearStored()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneMapped(self, arg0: QTransform) -> flNode:
        """flNode cloneMapped(QTransform)"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def collapseHandles(self) -> bool:
        """bool collapseHandles()"""
        ...

    def convertToCurve(self, smooth: Any=...) -> bool:
        """bool convertToCurve([bool smooth = false])"""
        ...

    def convertToCurves(self) -> bool:
        """bool convertToCurves()"""
        ...

    def convertToLine(self) -> bool:
        """bool convertToLine()"""
        ...

    def copyFrom(self, withSelected: Any=...) -> Any:
        """copyFrom(Node[, withSelected=False])"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        """double distanceTo(Node/QPointF)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getLines(self, *args: Any, **kwargs: Any) -> Any:
        """(QLineF, QLineF)/None getLines()"""
        ...

    def getOn(self) -> Any:
        """Node/None getOn()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def improve(self) -> bool:
        """bool improve()"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isCorner(self, a: Any=...) -> bool:
        """bool isCorner([double a = 10.])"""
        ...

    def isCurve(self) -> bool:
        """bool isCurve()"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isEqualTo(self, tolerance: Any=...) -> bool:
        """bool isEqualTo(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])"""
        ...

    def isExtreme(self, open: Any=...) -> bool:
        """bool isExtreme(bool x[, bool open = true[, double limit = 0]])"""
        ...

    def isFirst(self) -> bool:
        """bool isFirst()"""
        ...

    def isG2(self, tolerance: float) -> bool:
        """bool isG2(double tolerance)"""
        ...

    def isInternal(self, clockwise: bool) -> bool:
        """bool isInternal(bool clockwise)"""
        ...

    def isInterpolated(self, x: bool) -> bool:
        """bool isInterpolated(bool x)"""
        ...

    def isLast(self) -> bool:
        """bool isLast()"""
        ...

    def isOff(self) -> bool:
        """bool isOff()"""
        ...

    def isOn(self) -> bool:
        """bool isOn()"""
        ...

    def isSmartAngle(self) -> bool:
        """bool isSmartAngle()"""
        ...

    def makeStart(self) -> bool:
        """bool makeStart()"""
        ...

    def moveBy(self, *args: Any, **kwargs: Any) -> Any:
        """moveBy(float dx, float dy[, bool round=false]"""
        ...

    def nextNode(self, nodeType: Any=...) -> Any:
        """Node/None nextNode([string nodeType= [, int searchDepth=1]])"""
        ...

    def pointG2(self) -> Any:
        """QPointF/None pointG2()"""
        ...

    def prevNode(self, nodeType: Any=...) -> Any:
        """Node/None prevNode([string nodeType= [, int searchDepth=1]])"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreCoordinates(self) -> Any:
        """restoreCoordinates()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def rotateBy(self, origin: Any=...) -> Any:
        """rotateBy(valueDegree[, QPointF origin=(0, 0)])"""
        ...

    def round(self) -> Any:
        """round() - Round the node's coordinate"""
        ...

    def scaleBy(self, origin: Any=...) -> Any:
        """scaleBy(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])"""
        ...

    def setExtraLast(self, bool: Any) -> Any:
        """setExtraLast(bool)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setNextSmooth(self, base: QPointF) -> Any:
        """setNextSmooth(QPointF base)"""
        ...

    def setPrevSmooth(self, base: QPointF) -> Any:
        """setPrevSmooth(QPointF base)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSmartAngleEnbl(self, bool: Any) -> bool:
        """bool setSmartAngleEnbl(bool)"""
        ...

    def setSmartSharp(self, tension: Any=...) -> bool:
        """bool setSmartSharp([double tension = 0.6])"""
        ...

    def skewBy(self, origin: Any=...) -> Any:
        """skewBy(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])"""
        ...

    def smartMove(self, offset: Any) -> Any:
        """list(uint) smartMove(offset)"""
        ...

    def smartSetXY(self, arg0: QPointF) -> Any:
        """smartSetXY(QPointF)"""
        ...

    def storeCoordinates(self) -> Any:
        """storeCoordinates()"""
        ...

    def storeTestParameters(self) -> Any:
        """storeTestParameters()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def transformBy(self, origin: Any=...) -> Any:
        """transformBy(QTransform tx[, QPointF origin=(0, 0)])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateG2(self) -> bool:
        """bool updateG2()"""
        ...

    def updateSmooth(self, extended_neibh: Any=...) -> Any:
        """updateSmooth([bool extended_neibh=true])"""
        ...
    NodeKind: dict
    NodeType: dict
    angle: Any
    'angle'
    contour: Any
    'The parent Contour or None if not present'
    flObjectFlags: dict
    g2: Any
    'g2'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hobby: Any
    'hobby'
    id: Any
    'object id'
    index: Any
    "The index of the node in parent's contour (if present, otherwise -1)"
    interpolated: Any
    'interpolated'
    interpolatedX: Any
    'interpolatedX'
    interpolatedY: Any
    'interpolatedY'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isSelectedAlone: Any
    'bool'
    isTerminal: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    nodeState: Any
    'nodeState'
    position: Any
    'Coordinates of the node as QPointF'
    preview: Any
    'preview'
    refCnt: Any
    'object references count'
    scv: Any
    'scv'
    selected: Any
    'The selected flag'
    smartAngleR: Any
    'smartAngleR'
    smooth: Any
    'The smooth flag'
    state: Any
    'state'
    type: Any
    'The node type'
    x: Any
    'The x coordinate of the node'
    y: Any
    'The y coordinate of the node'

class flNodeInfo:
    """flNodeInfo representation

Constructors:
  flNodeInfo()
  flNodeInfo(flObject)
  flNodeInfo(flNodeInfo)
  flNodeInfo(flNode, QTransform)
  flNodeInfo(flNode, flObject contour_info)
  flNodeInfo(flNode, flObject glyph_info, QTransform)
  flNodeInfo(flNode, flNodeInfo)

Native bases: object

Supplemental documentation:
Node information. The captured declaration exposes `node`, `contour`, `contourInfo`, `shape`, `shapeInfo`, `glyphInfo`, `getGlyphPoint`, `setGlyphPoint`, `setGlyphPointX`, `setGlyphPointY`, `getMappedPoint`, `toNodesInfo`, `breakContourExpanded`, `combine`, `dist` and `transform`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flNodeInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def breakContourExpanded(self, extrapolate_d: Any=...) -> bool:
        """bool breakContourExpanded([double extrapolate_d=0.5])"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def combine(self, transform: QTransform) -> Any:
        """combine(QTransform transform)"""
        ...

    def contour(self) -> flContour:
        """flContour contour()"""
        ...

    def createInstance(self) -> flNodeInfo:
        """flNodeInfo createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getGlyphPoint(self, round: bool) -> QPointF:
        """QPointF getGlyphPoint(bool round)"""
        ...

    def getMappedNeighborsRect(self) -> QRectF:
        """QRectF getMappedNeighborsRect()"""
        ...

    def getMappedPoint(self, *args: Any, **kwargs: Any) -> Any:
        """QPointF getMappedPoint([QPointF])"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getUpdateCanvasRect(self) -> QRectF:
        """QRectF getUpdateCanvasRect()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isValid(self) -> bool:
        """bool isValid()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setGlyphPoint(self, arg0: QPointF) -> Any:
        """setGlyphPoint(QPointF)"""
        ...

    def setGlyphPointX(self, x: float) -> Any:
        """setGlyphPointX(double x)"""
        ...

    def setGlyphPointY(self, y: float) -> Any:
        """setGlyphPointY(double y)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def shape(self) -> flShape:
        """flShape shape()"""
        ...

    def shapeInfo(self) -> flShapeInfo:
        """flShapeInfo shapeInfo()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def toNodesInfo(self, *args: Any, **kwargs: Any) -> Any:
        """list(flNodeInfo) toNodesInfo(list(flNode))"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    contourInfo: Any
    'flObject'
    dist: Any
    'double dist'
    flObjectFlags: dict
    glyphInfo: Any
    'flObject - glyph info'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    name: Any
    'object name'
    node: Any
    'flNode'
    refCnt: Any
    'object references count'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flObject:
    """flObject representation

Constructors:
  flObject()
  flObject(flObject)
  flObject(uint id)

Native bases: object

Supplemental documentation:
Base editing object. The captured declaration exposes identity and state attributes `id`, `name`, `type`, `refCnt`, `isValid`, `isNull`, `isPresent`, `isReleased`, `isChanged` and `hasChanges`. Captured methods cover properties (`getProperty`, `setProperty`, `getProperties`), flags (`flag`, `setFlag`, `clearFlag`), history states (`historyStates`, `restoreHistoryState`, `hasHistoryState`) and object lifetime (`clone`, `release`, `remove`, `update`, `changed`).

Source: generated/fontlab.py: flObject captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flObjectsList_flGuideLine_:
    """flObjectsList<flGuideLine> doc

Native bases: object

Supplemental documentation:
Guideline list. The captured declaration exposes `append`, `at`, `clearContent`, `contains`, `count`, `first`, `indexOf`, `insert`, `last`, `list`, `removeOne` and `swap`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flObjectsList_flGuideLine_ captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, o: Any) -> None:
        """void append(T o)"""
        ...

    def at(self, i: int) -> Any:
        """T at(int i)"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearContent(self) -> None:
        """void clearContent()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def contains(self, o: Any) -> bool:
        """bool contains(T o)"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def indexOf(self, o: Any) -> int:
        """int indexOf(T o)"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def insert(self, index: int, o: Any) -> None:
        """void insert(int index, T o)"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeOne(self, o: Any) -> None:
        """void removeOne(T o)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def swap(self, i0: int, i1: int) -> None:
        """void swap(int i0, int i1)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    count: Any
    first: Any
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    last: Any
    list: Any
    'as list'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flObjectsList_flShape_:
    """flObjectsList<flShape> doc

Native bases: object

Supplemental documentation:
Shape list. The captured declaration exposes `append`, `at`, `clearContent`, `contains`, `count`, `first`, `indexOf`, `insert`, `last`, `list`, `removeOne` and `swap`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flObjectsList_flShape_ captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, o: Any) -> None:
        """void append(T o)"""
        ...

    def at(self, i: int) -> Any:
        """T at(int i)"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearContent(self) -> None:
        """void clearContent()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def contains(self, o: Any) -> bool:
        """bool contains(T o)"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def indexOf(self, o: Any) -> int:
        """int indexOf(T o)"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def insert(self, index: int, o: Any) -> None:
        """void insert(int index, T o)"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeOne(self, o: Any) -> None:
        """void removeOne(T o)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def swap(self, i0: int, i1: int) -> None:
        """void swap(int i0, int i1)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    count: Any
    first: Any
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    last: Any
    list: Any
    'as list'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flPackage:
    """flPackage representation

Constructors:
  flPackage()
  flPackage(flObject)
  flPackage(fgFont)

Native bases: object

Supplemental documentation:
Font package. The captured declaration exposes `addAxis`, `addGlyph`, `addInstance`, `addMaster`, `autoKern`, `autohintGlyphs`, `clearInstances`, `clearMasters`, `close`, `deleteGlyph`, `deleteGroups`, `findAxis`, `findGroup`, `findUnicode`, `generateGlyph`, `getAllGroups`, `hasAxis` and `hasMaster`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flPackage captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activateGlyph(self, arg0: flGlyph) -> Any:
        """activateGlyph(flGlyph)"""
        ...

    def addAxis(self, variable: flAxis) -> Any:
        """string addAxis(flAxis variable)"""
        ...

    def addGlyph(self, flGlyph: Any) -> Any:
        """addGlyph(fgGlyph / flGlyph )"""
        ...

    def addInstance(self, *args: Any, **kwargs: Any) -> Any:
        """addInstance(const flInstance &instance)"""
        ...

    def addMaster(self, *args: Any, **kwargs: Any) -> Any:
        """string addMaster(string master_name, bool create_glyphs, flPackage source, string source_layer_name, bool copy_metrics, bool create_missing_glyphs[, flLocation location])"""
        ...

    def assignData(self, *args: Any, **kwargs: Any) -> Any:
        """assignData(const flPackage &package)"""
        ...

    def autoKern(self, left: flGlyph, right: flGlyph, master_name: Any) -> Any:
        """autoKern(flGlyph left, flGlyph right, string master_name)"""
        ...

    def autohintGlyphs(self, glyphs: list[flGlyph], make_hints: bool) -> Any:
        """autohintGlyphs(QList<flGlyph> glyphs, bool make_hints)"""
        ...

    def buildShapeDataNames(self, *args: Any, **kwargs: Any) -> Any:
        """QSet<string> buildShapeDataNames(objId exclude[, string layer_name])"""
        ...

    def can_interpolate(self, *args: Any, **kwargs: Any) -> Any:
        """bool can_interpolate([string master_name])"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkAxisName(self, name: Any) -> Any:
        """string checkAxisName(string name)"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def checkVariableName(self, name: Any) -> Any:
        """string checkVariableName(string name)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearActiveGlyphs(self) -> Any:
        """clearActiveGlyphs()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearInstances(self) -> Any:
        """clearInstances()"""
        ...

    def clearMasters(self, release: bool) -> Any:
        """clearMasters(bool release)"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def close(self, save: Any=False) -> Any:
        """close(save=False) - Close the font"""
        ...

    def collectNames(self, storage: Any) -> Any:
        """collectNames(StorageInfo * storage)"""
        ...

    def completeData(self, fg_data: Any=...) -> Any:
        """completeData([bool fg_data = false])"""
        ...

    def convertZonesToGuidelines(self, zonesT: flZones, zonesB: flZones) -> Any:
        """convertZonesToGuidelines(flZones zonesT, flZones zonesB)"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deleteGlyph(self, flGlyph: Any) -> bool:
        """bool deleteGlyph(fgGlyph / flGlyph )"""
        ...

    def deleteGroups(self, ids: set[int], deleteDependentContent: bool) -> Any:
        """deleteGroups(QSet<uint> ids, bool deleteDependentContent)"""
        ...

    def ensureProteusData(self) -> Any:
        """ensureProteusData()"""
        ...

    def family_zones(self, top: bool) -> Any:
        """list(flZone)& family_zones(bool top)"""
        ...

    def featuresContainer(self) -> flObject:
        """flObject featuresContainer()"""
        ...

    def findAxis(self, cs: Any=...) -> Any:
        """flAxis/Nothing findAxis(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])"""
        ...

    def findAxisShort(self, short_name: Any) -> Any:
        """flAxis/Nothing findAxisShort(string short_name)"""
        ...

    def findFgId(self, id: int) -> flGlyph:
        """flGlyph findFgId(uint id)"""
        ...

    def findGroup(self, _id: int) -> Any:
        """fg::GlyphGroup* findGroup(int _id)"""
        ...

    def findName(self, name: Any) -> flGlyph:
        """flGlyph findName(string name)"""
        ...

    def findNameId(self, fg_id: int) -> flGlyph:
        """flGlyph findNameId(uint fg_id)"""
        ...

    def findNewName(self, name: Any) -> Any:
        """string findNewName(string name)"""
        ...

    def findShapeRoot(self, shape_data: flShapeData) -> flGlyph:
        """flGlyph findShapeRoot(flShapeData shape_data)"""
        ...

    def findStem(self, n: Any, b: bool, loose: bool) -> int:
        """int findStem(string n, bool b, bool loose)"""
        ...

    def findUnicode(self, uni: int) -> flGlyph:
        """flGlyph findUnicode(uint uni)"""
        ...

    def findZone(self, n: Any, b: bool) -> int:
        """int findZone(string n, bool b)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def generateGlyph(self, recipe: Any, layer_name: Any, metrics: Any, rtl: bool) -> Any:
        """QList<GlyphComponent>/Nothing generateGlyph(string recipe, string layer_name, FontMetrics metrics, bool rtl)"""
        ...

    def getAccentsInfo(self, arg0: flLayer, arg1: flPinPoint) -> Any:
        """list(AccentInfo)/Nothing getAccentsInfo(flLayer, flPinPoint)"""
        ...

    def getAllGroups(self) -> Any:
        """list( (bool kernGroup, string groupName, int id, int mark, list(string glyphName) )/Nothing getAllGroups()"""
        ...

    def getAxisName(self, short_name: Any) -> Any:
        """string getAxisName(string short_name)"""
        ...

    def getAxisShortName(self, name: Any) -> Any:
        """string getAxisShortName(string name)"""
        ...

    def getLayerName(self) -> Any:
        """string getLayerName()"""
        ...

    def getMarkOffset(self, g1: flGlyph, g2: flGlyph, layer_name: Any) -> Any:
        """QPointF/Nothing getMarkOffset(flGlyph g1, flGlyph g2, string layer_name)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getShapes(self, *args: Any, **kwargs: Any) -> Any:
        """QList<int>/Nothing getShapes(string filter[, string layer_name])"""
        ...

    def hasAxis(self, cs: Any=...) -> bool:
        """bool hasAxis(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])"""
        ...

    def hasAxisShort(self, short_name: Any) -> bool:
        """bool hasAxisShort(string short_name)"""
        ...

    def hasGuides(self) -> bool:
        """bool hasGuides()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasInstaceFor(self, arg0: fgFont) -> bool:
        """bool hasInstaceFor(fgFont)"""
        ...

    def hasMaster(self, name: Any) -> bool:
        """bool hasMaster(string name)"""
        ...

    def hasName(self, relaxed: Any=...) -> bool:
        """bool hasName(string name[, bool relaxed=false])"""
        ...

    def hasPackageHistoryStorages(self, to_history_ix: int) -> bool:
        """bool hasPackageHistoryStorages(uint to_history_ix)"""
        ...

    def hasZones(self) -> bool:
        """bool hasZones()"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStack(self) -> flObject:
        """flObject historyStack()"""
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initItr(self, itr: fgTTInterpreter) -> Any:
        """initItr(fgTTInterpreter itr)"""
        ...

    def initItrGlyph(self, itr: fgTTInterpreter, glyph: flGlyph) -> Any:
        """initItrGlyph(fgTTInterpreter itr, flGlyph glyph)"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def interpolateInstance(self, location: flLocation, round: bool) -> flPackage:
        """flPackage interpolateInstance(flLocation location, bool round)"""
        ...

    def interpolateMaster(self, location: flLocation, master_name: Any) -> bool:
        """bool interpolateMaster(flLocation location, string master_name)"""
        ...

    def isComponent(self, *args: Any, **kwargs: Any) -> Any:
        """(flGlyph, QTransform) isComponent(flShapeData[, string layer_name])"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def kerning(self, *args: Any, **kwargs: Any) -> Any:
        """fgKerning kerning([string master_name])"""
        ...

    def kerningContainer(self) -> flObject:
        """flObject kerningContainer()"""
        ...

    def location(self, *args: Any, **kwargs: Any) -> Any:
        """flLocation& location([string master_name])"""
        ...

    def makeShapeDataName(self, name: Any, _id: Any, layer_name: Any) -> Any:
        """string makeShapeDataName(string name, objId _id, string layer_name)"""
        ...

    def mastersContainer(self) -> flObject:
        """flObject mastersContainer()"""
        ...

    def optimizeShapeTransformations(self, changes: list[flObject]) -> bool:
        """bool optimizeShapeTransformations(QList<flObject> changes)"""
        ...

    def optimizeStemData(self, *args: Any, **kwargs: Any) -> Any:
        """(flStems stemsH, flStems stemsV) optimizeStemData(flStems stemsH, flStems stemsV)"""
        ...

    def prepareAxes(self, packages: list[flPackage], glyphs: list[flGlyph]) -> Any:
        """QList<flAxis>/Nothing prepareAxes(QList<flPackage> packages, QList<flGlyph> glyphs)"""
        ...

    def prepareFontGateData(self, prepare_tth: bool) -> Any:
        """prepareFontGateData(bool prepare_tth)"""
        ...

    def preparePropertiesData(self) -> Any:
        """preparePropertiesData()"""
        ...

    def projectPackageName(self) -> Any:
        """string projectPackageName()"""
        ...

    def readFromFile(self, *args: Any, **kwargs: Any) -> Any:
        """flPackage/Nothing readFromFile(string[, StorageInfo*=0])"""
        ...

    def referencesCount(self, shapeDataId: int) -> int:
        """int referencesCount(uint shapeDataId)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeMaster(self, name: Any, remove_glyph_masters: bool) -> Any:
        """removeMaster(string name, bool remove_glyph_masters)"""
        ...

    def renameGlyph(self, glyph: fgGlyph, name: Any, rename: bool) -> bool:
        """bool renameGlyph(fgGlyph glyph, string name, bool rename)"""
        ...

    def renameMaster(self, old_name: Any, new_name: Any) -> Any:
        """string renameMaster(string old_name, string new_name)"""
        ...

    def replaceGlyph(self, target: fgGlyph, newGlyph: fgGlyph, rename: bool) -> bool:
        """bool replaceGlyph(fgGlyph target, fgGlyph newGlyph, bool rename)"""
        ...

    def replaceShapeWithReference(self, *args: Any, **kwargs: Any) -> Any:
        """flShape/Nothing replaceShapeWithReference(flShape shape, bool process[, string layer_name])"""
        ...

    def resetPackage(self) -> Any:
        """resetPackage()"""
        ...

    def resetStemData(self, *args: Any, **kwargs: Any) -> Any:
        """(flStems stemsH, flStems stemsV) resetStemData(flStems stemsH, flStems stemsV)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def runActions(self, *args: Any, **kwargs: Any) -> Any:
        """void runActions(QList<flGlyph> &glyphs, QStringList actions, int layer_mode, bool do_undo)"""
        ...

    def setAxis(self, *args: Any, **kwargs: Any) -> Any:
        """setAxis(const flAxis &p)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setLocation(self, *args: Any, **kwargs: Any) -> Any:
        """setLocation(flLocation location[, string master_name])"""
        ...

    def setMaster(self, notify: Any=...) -> Any:
        """setMaster(string name[, bool notify = false])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setUpm(self, upm: int, scale: bool) -> Any:
        """setUpm(int upm, bool scale)"""
        ...

    def set_ascender_locked(self, b: bool) -> Any:
        """set_ascender_locked(bool b)"""
        ...

    def set_capsHeight_locked(self, b: bool) -> Any:
        """set_capsHeight_locked(bool b)"""
        ...

    def set_descender_locked(self, b: bool) -> Any:
        """set_descender_locked(bool b)"""
        ...

    def set_interpolate(self, *args: Any, **kwargs: Any) -> Any:
        """set_interpolate(bool b[, string master_name])"""
        ...

    def set_measurement_locked(self, b: bool) -> Any:
        """set_measurement_locked(bool b)"""
        ...

    def set_xHeight_locked(self, b: bool) -> Any:
        """set_xHeight_locked(bool b)"""
        ...

    def stems(self, HintingDataType: Any, top: bool) -> Any:
        """list(flStem)& stems(HintingDataType, bool top)"""
        ...

    def store_font_info(self, *args: Any, **kwargs: Any) -> Any:
        """store_font_info(fg::Package *package)"""
        ...

    def store_hinting_data(self, package: fgPackage) -> Any:
        """store_hinting_data(fgPackage package)"""
        ...

    def styleCode(self) -> Any:
        """unsigned char styleCode()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def title_name(self, force_full: Any=...) -> Any:
        """string title_name([bool force_full = true])"""
        ...

    def tthRenameStems(self, map_h: dict[str, str], map_v: dict[str, str]) -> bool:
        """bool tthRenameStems(QMap<QString, QString> map_h, QMap<QString, QString> map_v)"""
        ...

    def tthRenameZones(self, map_top: dict[str, str], map_bottom: dict[str, str]) -> bool:
        """bool tthRenameZones(QMap<QString, QString> map_top, QMap<QString, QString> map_bottom)"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateAxesMap(self) -> Any:
        """updateAxesMap()"""
        ...

    def updateFontMetrics(self) -> Any:
        """updateFontMetrics()"""
        ...

    def updateShapeReferenceCount(self) -> Any:
        """updateShapeReferenceCount()"""
        ...

    def updateZonesFromGuidelines(self, *args: Any, **kwargs: Any) -> Any:
        """updateZonesFromGuidelines([flZones zonesT, flZones zonesB])"""
        ...

    def zones(self, HintingDataType: Any, top: bool) -> Any:
        """list(flZone)& zones(HintingDataType, bool top)"""
        ...
    allGuidelines: Any
    'QList<flObject>'
    ascender_value: Any
    'double'
    axes: Any
    'QList<flAxis>'
    bold: Any
    'bool'
    capsHeight_value: Any
    'double'
    caretOffset_value: Any
    'double'
    cornerTension_value: Any
    'double'
    counterAnchors: Any
    'int'
    counterGuides: Any
    'int'
    currentSearch: Any
    'QByteArray'
    curveTension: Any
    'double'
    curveTension_value: Any
    'double'
    defaultMaster: Any
    'string'
    descender_value: Any
    'double'
    elidedName: Any
    'string'
    family_zonesB: Any
    'list(flZone)'
    family_zonesT: Any
    'list(flZone)'
    ffn: Any
    'string'
    fgId: Any
    'int'
    fgPackage: Any
    'fgFont'
    fileName: Any
    'string'
    flObjectFlags: dict
    fontLayerOrder: Any
    'A list of layer names indicating order of the layers in the font'
    glyphsCount: Any
    'int'
    guidelines: Any
    'list(flGuideLine)'
    guidelinesHost: Any
    'GuidelinesHostIntf*'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hasWeightAxis: Any
    'bool'
    hasWidthAxis: Any
    'bool'
    hinting: Any
    'flHintingParameters'
    id: Any
    'object id'
    info: Any
    'FontInfo'
    inktrapLen_value: Any
    'double'
    instanceAttributes: Any
    'flLayerAttributes'
    instances: Any
    'QList<flInstance>'
    interpolationCheckGeometry: Any
    'bool'
    interpolationExtrapolate: Any
    'bool'
    interpolationFlags: Any
    'int'
    interpolationMutatorMath: Any
    'bool'
    interpolationSortContours: Any
    'bool'
    isChanged: Any
    'bool'
    isKey: Any
    'bool'
    isMaster: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    italic: Any
    'bool'
    italicAngle_value: Any
    'double'
    keepShapeData: Any
    'bool'
    lineGap_value: Any
    'double'
    mask: Any
    'flLayer'
    master: Any
    'string'
    masterLib: Any
    'dict(name, QVariant)'
    masters: Any
    'QList<string>'
    mastersCount: Any
    'int'
    measurement_value: Any
    'double'
    monospaced: Any
    'bool'
    name: Any
    'object name'
    note: Any
    'string'
    other: Any
    'string'
    packageLib: Any
    'dict(name, QVariant)'
    panose: Any
    'string'
    path: Any
    'The path to the source font file'
    ps_stemsH: Any
    'list(flStem)'
    ps_stemsV: Any
    'list(flStem)'
    ps_zonesB: Any
    'list(flZone)'
    ps_zonesT: Any
    'list(flZone)'
    psn: Any
    'string'
    refCnt: Any
    'object references count'
    safeBottom_value: Any
    'double'
    safeTop_value: Any
    'double'
    sampleString: Any
    'string'
    sgn: Any
    'string'
    slantTransform: Any
    'QTransform'
    slope: Any
    'string'
    smartCornerParameters: Any
    'SmartCornerParameters'
    tfn: Any
    'string'
    tsn: Any
    'string'
    tt_stemsH: Any
    'list(flStem)'
    tt_stemsV: Any
    'list(flStem)'
    tt_zonesB: Any
    'list(flZone)'
    tt_zonesT: Any
    'list(flZone)'
    type: Any
    'object type'
    underlinePosition_value: Any
    'double'
    underlineThickness_value: Any
    'double'
    upm: Any
    'float'
    variables: Any
    'list(flPropertyDouble)'
    variationPackages: Any
    'QList<flPackage>'
    versionMajor: Any
    'int'
    versionMinor: Any
    'int'
    weight: Any
    'string'
    weight_value: Any
    'double'
    width: Any
    'string'
    width_value: Any
    'double'
    xHeight_value: Any
    'double'

class flPaper:
    """flPaper representation

Constructors:
  flPaper()
  flPaper(flPaper)
  flPaper(flObject)
  flPaper(QBrush)

Native bases: object

Supplemental documentation:
A paper object holding glyph information. The captured declaration exposes the methods `activeGlyphInfo`, `getGlyphInfo`, `glyphInfoAt`, `glyphsBoundRect`, `hasActive`, `hasContent`, `glyph`, `setActiveGlyph` and `setPaperGlyph`. It is created as `flPaper()`, `flPaper(flPaper)`, `flPaper(flObject)` or `flPaper(QBrush)`. It also carries the shared object members `name`, `id`, `type`, `isValid`, `release` and `remove`.

Source: generated/fontlab.py: flPaper captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activeGlyphInfo(self) -> flObject:
        """flObject activeGlyphInfo()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createInstance(self) -> flPaper:
        """flPaper createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getGlyphInfo(self, arg0: flObject) -> flObject:
        """flObject getGlyphInfo(flObject)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def glyph(self) -> flObject:
        """flObject glyph()"""
        ...

    def glyphInfoAt(self, index: int) -> flObject:
        """flObject glyphInfoAt(int index)"""
        ...

    def glyphsBoundRect(self) -> QRectF:
        """QRectF glyphsBoundRect()"""
        ...

    def hasActive(self) -> bool:
        """bool hasActive()"""
        ...

    def hasContent(self) -> bool:
        """bool hasContent()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def package(self) -> flObject:
        """flObject package()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setActiveGlyph(self, glyph: flObject) -> flObject:
        """flObject setActiveGlyph(flObject glyph)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setPaperGlyph(self, glyph: flObject) -> flObject:
        """flObject setPaperGlyph(flObject glyph)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flPinPoint:
    """flPinPoint representation

Constructors:
  flPinPoint()
  flPinPoint(flPinPoint)
  flPinPoint(flObject)
  flPinPoint(QPointF[, PinPointStyle=FreePosition])

Native bases: object

Supplemental documentation:
A pin point object with a `point` position, a `style`, an `appearance` value and the boolean attributes `anchor`, `isLatch`, `markEnabled`, `cloudEnabled` and `hasExpression`, plus the text attributes `expressionX` and `expressionY`. The captured declaration also exposes `translate`, `createInstance` and the object property, flag and history methods shared with the base editing object.

Source: generated/fontlab.py: flPinPoint captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createInstance(self) -> flPinPoint:
        """flPinPoint createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def translate(self, arg0: QPointF) -> Any:
        """translate(QPointF)"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    PinPointStyle: dict
    anchor: Any
    'bool'
    appearance: Any
    'int'
    cloudEnabled: Any
    'bool'
    expressionX: Any
    'string'
    expressionY: Any
    'string'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasExpression: Any
    'bool hasExpression()'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isLatch: Any
    'bool isLatch()'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    markEnabled: Any
    'bool'
    name: Any
    'object name'
    point: Any
    'QPointF'
    refCnt: Any
    'object references count'
    style: Any
    'PinPointStyle style()'
    type: Any
    'object type'

class flPreferences:
    """flPreferences representation

Constructors:
  flPreferences()

Native bases: object

Supplemental documentation:
Preferences. The captured declaration exposes `doInterpolate`, `fontAuditTests`, `instance`, `load`, `save`, `saveView`, `setFontAuditTest`, `setGridDistances`, `sourceMetricsSamples`, `unicode2text`, `ConflictOverwrite`, `ConflictRename`, `ConflictSkip`, `DestinationAsk`, `DestinationFolder` and `DsigAlgorithmSHA256`. It is created with no captured constructor overloads.

Source: generated/fontlab.py: flPreferences captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def doInterpolate(self) -> bool:
        """bool doInterpolate()"""
        ...

    def fontAuditTests(self) -> Any:
        """list(int) fontAuditTests()"""
        ...

    def instance(self) -> flPreferences:
        """flPreferences instance()"""
        ...

    def load(self, arg0: dict[str, Any]) -> Any:
        """load(QVariantMap)"""
        ...

    def namecaptionFont(self, *args: Any, **kwargs: Any) -> Any:
        """QFont  namecaptionFont (bool condensed)"""
        ...

    def namecaptionFontFamilyName(self, *args: Any, **kwargs: Any) -> Any:
        """string namecaptionFontFamilyName (bool condensed)"""
        ...

    def namecaptionFontId(self, *args: Any, **kwargs: Any) -> Any:
        """int    namecaptionFontId (bool condensed)"""
        ...

    def options2tracer_precision(self) -> float:
        """double options2tracer_precision()"""
        ...

    def options2tracer_smoothness(self) -> int:
        """int options2tracer_smoothness()"""
        ...

    def save(self) -> dict[str, Any]:
        """QVariantMap save()"""
        ...

    def saveView(self) -> Any:
        """saveView()"""
        ...

    def setFontAuditTest(self, id: int, value: bool) -> Any:
        """setFontAuditTest(int id, bool value)"""
        ...

    def setGridDistances(self, x: float, y: float) -> Any:
        """setGridDistances(double x, double y)"""
        ...

    def sourceMetricsSamples(self) -> str:
        """QString sourceMetricsSamples()"""
        ...

    def tracer2options_precision(self, curve_fit: float) -> float:
        """double tracer2options_precision(double curve_fit)"""
        ...

    def tracer2options_smoothness(self, straighten_angle: int) -> float:
        """double tracer2options_smoothness(int straighten_angle)"""
        ...

    def unicode2text(self, unc: int) -> str:
        """QString unicode2text(uint unc)"""
        ...
    ConflictOverwrite: int
    ConflictRename: int
    ConflictSkip: int
    ConflictTrash: int
    ContentCurrent: int
    ContentInstances: int
    ContentMasters: int
    ContentVisible: int
    CoordinanesNone: int
    CoordinatesAll: int
    CoordinatesSelected: int
    CurvatureLarge: int
    CurvatureMedium: int
    CurvatureSmall: int
    CurvatureSmart: int
    DestinationAsk: int
    DestinationFolder: int
    DestinationSource: int
    DrawFocusAlways: int
    DrawFocusNever: int
    DrawFocusPanels: int
    DsigAlgorithmMD5: int
    DsigAlgorithmSHA1: int
    DsigAlgorithmSHA256: int
    DsigAlgorithmSHA384: int
    DsigAlgorithmSHA512: int
    DsigAuthorityCommercial: int
    DsigAuthorityDefault: int
    DsigAuthorityIndividual: int
    FontCaptionAuto: int
    FontCaptionLarge: int
    FontCaptionMedium: int
    FontCaptionSmall: int
    GroupsAlignCenter: int
    GroupsAlignLeft: int
    GroupsAlignRight: int
    GroupsFillAlways: int
    GroupsFillAuto: int
    GroupsFillNever: int
    GroupsMaskMask: int
    GroupsMaskNone: int
    GroupsMaskOutline: int
    InactiveNodeNone: int
    InactiveNodeNormal: int
    InactiveNodeSmall: int
    InterpretName: int
    InterpretWeight: int
    InterpretWidth: int
    KeepDraw: int
    KeepGuidesHints: int
    KeepInsertDelete: int
    KeepNone: int
    MastersBackground: int
    MastersBar: int
    MastersNone: int
    MatchAll: int
    MatchConvertSegment: int
    MatchDeleteNode: int
    MatchGuides: int
    MatchHints: int
    MatchInsertNode: int
    MatchInsertShape: int
    MatchPins: int
    MatchRenameNode: int
    MetricsHideAnchors: int
    MetricsHideFontGuides: int
    MetricsHideFontMetrics: int
    MetricsHideGlyphMetrics: int
    MetricsHideGrid: int
    MetricsHideGuides: int
    MetricsHideHints: int
    MetricsHideZones: int
    ModeCategories: int
    ModeCodepages: int
    ModeIndex: int
    ModeNames: int
    ModeNone: int
    ModeRanges: int
    ModeScripts: int
    NiceGlyphs: int
    NiceNone: int
    NicePdf: int
    NiceRobo: int
    NiceUni: int
    NodeNameAlways: int
    NodeNameCoordinates: int
    NodeNameNever: int
    NodeStyleAuto: int
    NodeStyleFlat: int
    NodeStyleFrame: int
    OrganizeNone: int
    OrganizePSN: int
    OrganizeProfile: int
    OrganizeSGN: int
    OrganizeTFN: int
    OrganizeTFN_Profile: int
    PasteAlign: int
    PasteAscender_Descender: int
    PasteCapsHeight_Baseline: int
    PasteCapsHeight_Descender: int
    PasteUPM_Descender: int
    PasteUnscaled: int
    PowerAll: int
    PowerFont: int
    PowerGlyph: int
    PowerMetrics: int
    PowerZones: int
    RainbowNoCenterline: int
    RainbowNoEdges: int
    RainbowNoRainbow: int
    RainbowNone: int
    RainbowShow: int
    RoundAll: int
    RoundNone: int
    RoundOn: int
    SaveFolderAsk: int
    SaveFolderFolder: int
    SaveFolderSource: int
    SaveWorkspacePanels: int
    SaveWorkspaceWindows: int
    SingleBreak: int
    SingleRemove: int
    TaperBody: int
    TaperEdge: int
    TaperEverywhere: int
    TaperNone: int
    ThicknessNormal: int
    ThicknessThick: int
    ThicknessThin: int
    TransformModeRotate: int
    TransformModeScale: int
    TransformModeSlant: int
    UseItalicAll: int
    UseItalicMetrics: int
    UseItalicNone: int
    ViewAnchorGroups: int
    ViewAnchors: int
    ViewBackground: int
    ViewContourDirection: int
    ViewCoordinates: int
    ViewCount: int
    ViewCounters: int
    ViewCurvature: int
    ViewFilledPreview: int
    ViewFontAudit: int
    ViewFontGuides: int
    ViewFontMetrics: int
    ViewGlobalMask: int
    ViewGlyphBar: int
    ViewGlyphGuides: int
    ViewGlyphMetrics: int
    ViewGrid: int
    ViewGroups: int
    ViewHandles: int
    ViewHintShadows: int
    ViewHints: int
    ViewInactiveGlyphs: int
    ViewKerningGroups: int
    ViewLocalMask: int
    ViewMasterLinks: int
    ViewMeasurement: int
    ViewMeasurementPanel: int
    ViewMetricsTable: int
    ViewModeKerning: int
    ViewModeMetrics: int
    ViewModeOutline: int
    ViewModePreview: int
    ViewModeText: int
    ViewNodeLinks: int
    ViewNodes: int
    ViewPins: int
    ViewRulers: int
    ViewSelectionFrame: int
    ViewShapeConnection: int
    ViewShapeFrame: int
    ViewShapeGuides: int
    ViewShapeLinks: int
    ViewStickers: int
    ViewString: int
    ViewTapeLine: int
    ViewThickness: int
    ViewTunni: int
    ViewZones: int
    WindowsFontTabs: int
    WindowsTabs: int
    WindowsWindows: int
    ZoomModeLines: int
    ZoomModeMetrics: int
    ZoomModeSafe: int
    ZoomModeSize: int
    colorEncoding: Any
    'QColor'
    colorFontCell: Any
    'QColor'
    colorGrid: Any
    'QColor'
    colorKerning: Any
    'QColor'
    colorMask: Any
    'QColor'
    colorMaskGlobal: Any
    'QColor'
    colorMaskLocal: Any
    'QColor'
    colorMetrics: Any
    'QColor'
    colorMetricsLines: Any
    'QColor'
    colorWorkspace: Any
    'QColor'
    convertDetectZoneTags: Any
    'bool'
    convertPostScriptPrecision: Any
    'double'
    convertTrueTypePrecision: Any
    'double'
    convertTrueTypeShortCurves: Any
    'bool'
    dataPath: Any
    'QString'
    dataPathDefault: Any
    'string'
    defaultTexts: Any
    'QStringList'
    developerBacklightUpdate: Any
    'bool'
    developerLargeQuickHelp: Any
    'bool'
    developerNoParameters: Any
    'bool'
    developerOpenGL: Any
    'bool'
    developerShowKeys: Any
    'bool'
    drawFocusRect: Any
    'int'
    dsigAlgorithm: Any
    'int'
    dsigAuthority: Any
    'int'
    dsigCertificatePath: Any
    'QString'
    dsigPassword: Any
    'QString'
    dsigPrivateKeyPath: Any
    'QString'
    dsigTimestamp: Any
    'bool'
    dsigTimestampUrl: Any
    'QString'
    dsigUrl: Any
    'QString'
    dsigWrite: Any
    'bool'
    editorAcrossGlyphs: Any
    'bool'
    editorAcrossLayers: Any
    'bool'
    editorAcrossShapes: Any
    'bool'
    editorAllowCache: Any
    'bool'
    editorAlternativePencil: Any
    'bool'
    editorAutoNonSpacing: Any
    'bool'
    editorCenterGlyph: Any
    'bool'
    editorClickSelectsCurve: Any
    'bool'
    editorCloseDistance: Any
    'int'
    editorCommandSelector: Any
    'bool'
    editorContrast: Any
    'bool'
    editorCoordinates: Any
    'bool'
    editorCoordinatesEditable: Any
    'bool'
    editorCopyText: Any
    'bool'
    editorCross: Any
    'bool'
    editorCtrl100: Any
    'bool'
    editorCurvatureOpacity: Any
    'double'
    editorCurvatureSize: Any
    'int'
    editorDarkPreview: Any
    'bool'
    editorDeleteSingleNode: Any
    'int'
    editorDirectKerning: Any
    'bool'
    editorDragInactiveShape: Any
    'bool'
    editorFastPreview: Any
    'bool'
    editorFeatures: Any
    'bool'
    editorFillOpacity: Any
    'int'
    editorFillOpenContours: Any
    'bool'
    editorFixedBCP: Any
    'bool'
    editorFocus: Any
    'bool'
    editorForcedGrid: Any
    'bool'
    editorForcedSnap: Any
    'bool'
    editorFrameSelectsOnNodes: Any
    'bool'
    editorGestures: Any
    'bool'
    editorGuideHitDistance: Any
    'int'
    editorHidePlaceholders: Any
    'bool'
    editorInactiveHandles: Any
    'bool'
    editorInactiveNodes: Any
    'int'
    editorInactiveWireframe: Any
    'bool'
    editorInertion: Any
    'bool'
    editorInstanceLayer: Any
    'bool'
    editorInterpolate: Any
    'bool'
    editorInterpolateModifier: Any
    'bool'
    editorKeyboardJoin: Any
    'bool'
    editorLayerDoubleClick: Any
    'bool'
    editorListMaskLayers: Any
    'bool'
    editorLockInactiveGlyphs: Any
    'bool'
    editorMatch: Any
    'bool'
    editorMeterCoordinates: Any
    'bool'
    editorMetricsDoubleClick: Any
    'bool'
    editorMinHandle: Any
    'int'
    editorMissingGlyphs: Any
    'bool'
    editorModalPen: Any
    'bool'
    editorNodeColor: Any
    'int'
    editorNodeFontDefault: Any
    'int'
    editorNodeFontHovered: Any
    'int'
    editorNodeHighlightDistance: Any
    'int'
    editorNodeHitDistance: Any
    'int'
    editorNodeSize: Any
    'int'
    editorNoteExpanded: Any
    'bool'
    editorNudge1: Any
    'double'
    editorNudge10: Any
    'double'
    editorOffsetDuplicate: Any
    'QPointF'
    editorOffsetPaste: Any
    'QPointF'
    editorOutlineThickness: Any
    'int'
    editorPantographCurve: Any
    'int'
    editorPantographKerning: Any
    'int'
    editorPantographNode: Any
    'int'
    editorPasteArtwork: Any
    'int'
    editorPasteContourVisual: Any
    'bool'
    editorPasteReplace: Any
    'bool'
    editorPenCorrection: Any
    'bool'
    editorPenPreview: Any
    'bool'
    editorPreviewPowerNudge: Any
    'bool'
    editorProportionalThickness: Any
    'bool'
    editorRoundKerning: Any
    'bool'
    editorRoundMetrics: Any
    'bool'
    editorScrollBars: Any
    'bool'
    editorSetMetrics2Frame: Any
    'bool'
    editorShiftConstrains: Any
    'bool'
    editorShiftExtendsSelection: Any
    'bool'
    editorShortGuides: Any
    'bool'
    editorShowCoordinates: Any
    'int'
    editorShowCurves: Any
    'bool'
    editorShowHiddenNodeName: Any
    'bool'
    editorShowNodeName: Any
    'int'
    editorShowSb: Any
    'bool'
    editorSidebarInactive: Any
    'int'
    editorSmartDelay: Any
    'int'
    editorSnapDistance: Any
    'int'
    editorStrongRound: Any
    'bool'
    editorTaperMode: Any
    'int'
    editorTextWidth: Any
    'int'
    editorTopBottom: Any
    'bool'
    editorUndoSelection: Any
    'bool'
    editorUseItalicAngle: Any
    'int'
    editorZoneNodes: Any
    'bool'
    editorZoomAscender: Any
    'bool'
    exportConflictMode: Any
    'int'
    exportContent: Any
    'int'
    exportDestinationFolder: Any
    'QString'
    exportDestinationMode: Any
    'int'
    exportJsonContours: Any
    'bool'
    exportJsonFormatting: Any
    'bool'
    exportOrganizeMode: Any
    'int'
    exportPPM: Any
    'int'
    exportSaveFolder: Any
    'QString'
    exportSaveSketchboard: Any
    'bool'
    exportSaveVFJ: Any
    'bool'
    exportSaveWorkspaceVFC: Any
    'uint'
    exportSaveWorkspaceVFJ: Any
    'uint'
    exportSessionVFJ: Any
    'bool'
    featuresAddKerningClasses: Any
    'bool'
    featuresAddOpenTypeClasses: Any
    'bool'
    featuresAddTags: Any
    'bool'
    featuresAddVirtualTags: Any
    'bool'
    fontAbsentGray: Any
    'bool'
    fontAllGlyphs: Any
    'bool'
    fontAskFileName: Any
    'int'
    fontAuditInPlace: Any
    'bool'
    fontAuditStemTolerance: Any
    'double'
    fontCaptionEditable: Any
    'bool'
    fontCaptionHeight: Any
    'int'
    fontCaptionTop: Any
    'bool'
    fontClose: Any
    'bool'
    fontColoredCaption: Any
    'bool'
    fontColoredItems: Any
    'bool'
    fontCreateDynamic: Any
    'bool'
    fontCreateGenerate: Any
    'bool'
    fontDefaultEncoding: Any
    'QString'
    fontDefaultMode: Any
    'int'
    fontDefaultSorting: Any
    'int'
    fontDrawLines: Any
    'bool'
    fontExtraIcons: Any
    'bool'
    fontFriendlyEncoding: Any
    'bool'
    fontMarkBright: Any
    'bool'
    fontMarkOpacity: Any
    'int'
    fontMetricsLimit: Any
    'int'
    fontMonospaced: Any
    'QString'
    fontNamFileName: Any
    'QString'
    fontNamFileNameDefault: Any
    'string'
    fontNameUnicode: Any
    'bool'
    fontNewNames: Any
    'int'
    fontNewWindow: Any
    'bool'
    fontNoteIcon: Any
    'bool'
    fontNoteText: Any
    'bool'
    fontPropertyIcon: Any
    'bool'
    fontRedBar: Any
    'bool'
    fontShowGlyphMetrics: Any
    'bool'
    fontSpaceScroll: Any
    'bool'
    fontUnicodeName: Any
    'bool'
    fontUnicodeUppercase: Any
    'bool'
    fontWheelBrowse: Any
    'bool'
    fontWheelScroll: Any
    'int'
    fontsAutoSaveTimeInterval: Any
    'int'
    generalActivatePanels: Any
    'bool'
    generalBeta: Any
    'bool'
    generalCheckUpdates: Any
    'bool'
    generalClosePanels: Any
    'bool'
    generalDarkFont: Any
    'bool'
    generalDarkGlyph: Any
    'bool'
    generalSketchboard: Any
    'bool'
    generalTabs: Any
    'int'
    generalTabsDrag: Any
    'bool'
    generalTabsPreview: Any
    'bool'
    generalVirtualKeys: Any
    'bool'
    gridDistanceX: Any
    'double'
    gridDistanceY: Any
    'double'
    gridItalicAngle: Any
    'bool'
    gridOpacity: Any
    'double'
    gridPointOpacity: Any
    'double'
    gridSlant: Any
    'double'
    groupsAlign: Any
    'int'
    groupsColor: Any
    'QColor'
    groupsContent: Any
    'QString'
    groupsDoubleClick: Any
    'bool'
    groupsFill: Any
    'int'
    groupsMask: Any
    'int'
    groupsMasters: Any
    'bool'
    groupsMetrics: Any
    'bool'
    groupsOpacity: Any
    'int'
    groupsPreview: Any
    'bool'
    groupsShiftX: Any
    'double'
    groupsShiftY: Any
    'double'
    hintMaxH: Any
    'int'
    hintMaxV: Any
    'int'
    hintMinH: Any
    'int'
    hintMinV: Any
    'int'
    historyStoreSelection: Any
    'bool'
    historyStoreViewPoint: Any
    'bool'
    importCompileFeatures: Any
    'bool'
    importComponents: Any
    'bool'
    importConvertCurves: Any
    'bool'
    importConvertNames: Any
    'int'
    importDecompileFeatures: Any
    'bool'
    importDecompileTables: Any
    'bool'
    importDecompose: Any
    'bool'
    importDetectGenius: Any
    'bool'
    importDetectServant: Any
    'bool'
    importExcludeTables: Any
    'QStringList'
    importLockComposites: Any
    'bool'
    importOpenFontWindow: Any
    'bool'
    importRenameCID: Any
    'bool'
    importRoundCoordinates: Any
    'bool'
    importSeparateMasters: Any
    'bool'
    importTrueTypeShortCurves: Any
    'bool'
    inactiveMastersOpacity: Any
    'double'
    interpolateSmartRound: Any
    'bool'
    isDark: Any
    'bool'
    kerningAuditExceptions: Any
    'double'
    kerningAutoToleranceNegative: Any
    'double'
    kerningAutoTolerancePositive: Any
    'double'
    kerningPairs: Any
    'QString'
    lockFontGuidelines: Any
    'bool'
    lockFontMetrics: Any
    'bool'
    lockGrid: Any
    'bool'
    lockGuidelines: Any
    'bool'
    lockHints: Any
    'bool'
    lockMask: Any
    'bool'
    lockMaskGlobal: Any
    'bool'
    lockMetrics: Any
    'bool'
    lockOutline: Any
    'bool'
    lockPinPoints: Any
    'bool'
    lockZones: Any
    'bool'
    mastersBackgroundBrightness: Any
    'int'
    mastersBarThickness: Any
    'int'
    mastersPreviewColor: Any
    'int'
    match: Any
    'uint'
    matchNudge: Any
    'bool'
    meterToolActive: Any
    'bool'
    meterToolDrag: Any
    'bool'
    metricsFreeMetrics: Any
    'bool'
    metricsHideCursor: Any
    'bool'
    metricsNudge1: Any
    'double'
    metricsNudge10: Any
    'double'
    metricsSamples: Any
    'QString'
    metricsSmartNavigation: Any
    'bool'
    metricsTableArrowsNavigation: Any
    'bool'
    metricsToStroke: Any
    'bool'
    openRestorePanels: Any
    'bool'
    openRestoreWindows: Any
    'bool'
    openRestoreWindowsGlyphs: Any
    'bool'
    operationsOCR: Any
    'bool'
    operationsPowerGuides: Any
    'int'
    operationsSeparateDetectStrings: Any
    'bool'
    operationsSeparateMergeOverlapped: Any
    'bool'
    operationsSeparateMergeStacked: Any
    'bool'
    operationsTesseractLanguages: Any
    'QString'
    operationsTracePrecision: Any
    'double'
    operationsTraceSmoothness: Any
    'double'
    panelFontSize: Any
    'int'
    panelTabs: Any
    'int'
    panelWrap: Any
    'int'
    pantographActive: Any
    'bool'
    pasteEPS: Any
    'bool'
    pasteIgnoreAppearance: Any
    'bool'
    pathAutoSave: Any
    'string'
    pythonClearContext: Any
    'bool'
    qobject: Any
    'QObject'
    renderBlackWhite: int
    renderClearType: int
    renderGrayScale: int
    saveBackupFolder: Any
    'bool'
    saveConflictMode: Any
    'int'
    showAnchorCloudSelected: Any
    'bool'
    showElementNote: Any
    'bool'
    showHoveredCoordinates: Any
    'bool'
    showNodePositionLarge: Any
    'bool'
    showNodeStyle: Any
    'int'
    showPinName: Any
    'bool'
    showSelectionGlow: Any
    'bool'
    showStemThickness: Any
    'int'
    showTapeLine: Any
    'bool'
    sketchboardAutoSaveTimeInterval: Any
    'int'
    smartGuides: Any
    'bool'
    snapToBounds: Any
    'bool'
    snapToCenters: Any
    'bool'
    snapToDistance: Any
    'bool'
    snapToFontGuidelines: Any
    'bool'
    snapToFontMetrics: Any
    'bool'
    snapToGrid: Any
    'bool'
    snapToGuidelines: Any
    'bool'
    snapToHints: Any
    'bool'
    snapToMask: Any
    'bool'
    snapToMaskGlobal: Any
    'bool'
    snapToMetrics: Any
    'bool'
    snapToOutline: Any
    'bool'
    snapToPinPoints: Any
    'bool'
    snapToStems: Any
    'bool'
    snapToZones: Any
    'bool'
    stringIconLong: Any
    'QString'
    stringIconShort: Any
    'QString'
    stringNewTextBlock: Any
    'QString'
    stringPreview: Any
    'QString'
    stringSizeGlyphWaterfall: Any
    'QString'
    stringSizeTextWaterfall: Any
    'QString'
    stringSticker: Any
    'QString'
    templateFont: Any
    'QFont'
    templateFontFamilyName: Any
    'string'
    templateFontId: Any
    'int'
    texts: Any
    'QStringList'
    tthHintingFlag: Any
    'uint'
    tthHintingTolerance: Any
    'uint'
    tthPPM: Any
    'int'
    tthRender: Any
    'int'
    tthSamples: Any
    'QString'
    viewAlternative: Any
    'bool'
    viewAntialiasing: Any
    'bool'
    workFont: Any
    'QFont'
    workFontFamilyName: Any
    'string'
    workFontId: Any
    'int'
    zoomAscender: Any
    'int'
    zoomDescender: Any
    'int'
    zoomFactorKeyboard: Any
    'double'
    zoomFactorWheel: Any
    'double'
    zoomMode: Any
    'int'
    zoomSize: Any
    'int'

class flProperty:
    """flProperty representation

Constructors:

Native bases: object

Supplemental documentation:
A property object. The captured declaration exposes the property accessors `getProperty`, `getPropertyInt`, `getPropertyFloat`, `setProperty`, `setPropertyInt` and `setPropertyFloat`, and the attribute `objectAttr`. It is created with no captured constructor overloads. It also carries the shared object members `name`, `id`, `type`, `isValid`, `release` and `remove`.

Source: generated/fontlab.py: flProperty captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    objectAttr: Any
    'QString'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flPropertyDouble:
    """flPropertyDouble representation

Constructors:

Native bases: object

Supplemental documentation:
A numeric property. The captured declaration exposes the attributes `value`, `expression`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flPropertyDouble captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    expression: Any
    'flExpression'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    type: Any
    'object type'
    value: Any
    'double'

class flPropertyPoint:
    """flPropertyPoint representation

Constructors:

Native bases: object

Supplemental documentation:
A point property. The captured declaration exposes `hasExpression`, and the attributes `point`, `paramType`, `ParameterType`, `expressionX`, `expressionY`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flPropertyPoint captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasExpression(self) -> bool:
        """bool hasExpression()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    ParameterType: dict
    expressionX: Any
    expressionY: Any
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    paramType: Any
    'ParameterType'
    point: Any
    'QPointF'
    refCnt: Any
    'object references count'
    type: Any
    'object type'

class flSearchInfo:
    """flSearchInfo representation

Constructors:
  flSearchInfo()
  flSearchInfo(flObject)
  flSearchInfo(flSearchInfo)
  flSearchInfo(QTransform)
  flSearchInfo(QTransform, flObject glyph_info)

Native bases: object

Supplemental documentation:
Search information. The captured declaration exposes `combine`, and the attributes `dist`, `glyphInfo`, `transform`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flSearchInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def combine(self, transform: QTransform) -> Any:
        """combine(QTransform transform)"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    dist: Any
    'double dist'
    flObjectFlags: dict
    glyphInfo: Any
    'flObject - glyph info'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flShape:
    """flShape representation

Constructors:
  flShape()
  flShape(flObject)
  flShape(flShapeData)
  flShape(flSticker)
  flShape(QImage)
  flShape(fgShape)
  flShape(flShapeBuilder)

Native bases: object

Supplemental documentation:
An editing shape with a `contours` collection of flContour objects. `getContours()` also returns its contours, and `contoursCount` reports their count. `boundingBox` is a QRectF attribute. Read the captured boolean attributes `isComponent` and `isComposite` to inspect the shape kind.

Source: generated/fontlab.py: flShape captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activateBuilder(self) -> Any:
        """activateBuilder()"""
        ...

    def addContour(self, arg0: flContour) -> Any:
        """addContour(flContour)"""
        ...

    def addContours(self, *args: Any, **kwargs: Any) -> Any:
        """addContours(list(flContour))"""
        ...

    def appendAnchor(self, node: flNode, guideline: flObject) -> Any:
        """appendAnchor(flAnchor) | void appendAnchor(flNode node, flObject guideline)"""
        ...

    def applyTransform(self, *args: Any, **kwargs: Any) -> Any:
        """applyTransform([QTransform transform])"""
        ...

    def assign(self, arg0: fgShape) -> Any:
        """assign(fgShape)"""
        ...

    def assignStyle(self, arg0: flShape) -> Any:
        """assignStyle(flShape)"""
        ...

    def bindDependencies(self) -> Any:
        """bindDependencies()"""
        ...

    def canUngroup(self) -> bool:
        """bool canUngroup()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearContours(self) -> Any:
        """clearContours()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def cloneTopLevel(self) -> flShape:
        """flShape cloneTopLevel()"""
        ...

    def contains(self, arg0: QPointF) -> bool:
        """bool contains(QPointF)"""
        ...

    def containsInInclude(self, id: Any) -> bool:
        """bool containsInInclude(flShape | uint id)"""
        ...

    def convertToFgShape(self, arg0: fgShape) -> Any:
        """convertToFgShape(fgShape)"""
        ...

    def copyToFgShape(self, arg0: fgShape) -> Any:
        """copyToFgShape(fgShape)"""
        ...

    def createInstance(self) -> flShape:
        """flShape createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def cutContour(self, *args: Any, **kwargs: Any) -> Any:
        """(list(flContour) inner, list(flContour) outer)/Nothing cutContour(flContour, QTransform)"""
        ...

    def decomposite(self) -> Any:
        """decomposite()"""
        ...

    def eject(self, arg0: flShape) -> Any:
        """eject(flShape)"""
        ...

    def ejectTo(self, clone: Any=...) -> Any:
        """list(flShape) ejectTo([bool clone =true[, bool apply_tx =true]])"""
        ...

    def ensurePaths(self) -> Any:
        """ensurePaths()"""
        ...

    def findNode(self, arg0: str) -> flNode:
        """flNode findNode(QString)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getActiveComposite(self) -> Any:
        """flShape/Nothing getActiveComposite()"""
        ...

    def getActiveIncludeShape(self) -> Any:
        """flShape/Nothing getActiveIncludeShape()"""
        ...

    def getAnchorForObject(self, arg0: flObject) -> Any:
        """flAnchor/Nothing getAnchorForObject(flObject)"""
        ...

    def getAnchors(self) -> Any:
        """list(flAnchor)/Nothing getAnchors()"""
        ...

    def getCompositesBounding(self) -> QRectF:
        """QRectF getCompositesBounding()"""
        ...

    def getContours(self) -> Any:
        """list(flContour) getContours()"""
        ...

    def getNodeAt(self, index: int, nodetype: Any) -> Any:
        """flNode/Nothing getNodeAt(int index, flNode::NodeType nodetype)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getSelected(self, SelectionMode: Any) -> Any:
        """list(flContour)/Nothing getSelected(SelectionMode)"""
        ...

    def getSquare(self) -> float:
        """double getSquare()"""
        ...

    def getTransformationPermissions(self, *args: Any, **kwargs: Any) -> Any:
        """(bool enbl_horz, bool enbl_vert, bool enbl_rotation) getTransformationPermissions()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasImage(self, bitmap_only: bool) -> bool:
        """bool hasImage(bool bitmap_only)"""
        ...

    def hasSelected(self, SelectionMode: Any) -> bool:
        """bool hasSelected(SelectionMode)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def horzReflection(self) -> bool:
        """bool horzReflection()"""
        ...

    def include(self, *args: Any, **kwargs: Any) -> Any:
        """include(list(flShape) | flShape, [ flLayer remove_from])"""
        ...

    def includeTo(self, ix: int, arg1: flShape) -> Any:
        """includeTo(int ix, flShape)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def inkBox(self, tx: Any=...) -> QRectF:
        """QRectF inkBox([QTransform tx = QTransform()])"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isCompatible(self, arg0: flShape, strong: bool) -> bool:
        """bool isCompatible(flShape, bool strong)"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isShape(self, arg0: flObject) -> bool:
        """bool isShape(flObject)"""
        ...

    def mergeTopComposite(self) -> Any:
        """mergeTopComposite()"""
        ...

    def prepareTransformationData(self) -> Any:
        """prepareTransformationData()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeAnchor(self, arg0: flAnchor) -> Any:
        """removeAnchor(flAnchor)"""
        ...

    def removeAnchorsForObject(self, arg0: flObject) -> Any:
        """removeAnchorsForObject(flObject)"""
        ...

    def removeBackContour(self) -> Any:
        """removeBackContour()"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeContour(self, arg0: flContour) -> Any:
        """removeContour(flContour)"""
        ...

    def removeContours(self, *args: Any, **kwargs: Any) -> Any:
        """removeContours(list(flContour))"""
        ...

    def replaceInclude(self, old_shape: flShape, new_shape: flShape) -> Any:
        """replaceInclude(flShape old_shape, flShape new_shape)"""
        ...

    def resetInkBox(self) -> Any:
        """resetInkBox()"""
        ...

    def resetTransformationData(self) -> Any:
        """resetTransformationData()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def selectAllData(self) -> Any:
        """selectAllData()"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setIncludes(self, *args: Any, **kwargs: Any) -> Any:
        """setIncludes(list(flShape))"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setReflected(self, *args: Any, **kwargs: Any) -> Any:
        """setReflected(bool, bool)"""
        ...

    def simpleShape(self) -> bool:
        """bool simpleShape()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def unselectAllNodes(self) -> Any:
        """unselectAllNodes()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def vertReflection(self) -> bool:
        """bool vertReflection()"""
        ...
    active: Any
    'bool'
    allSelectedData: Any
    'bool'
    boundingBox: Any
    'QRectF'
    brush: Any
    'QBrush'
    closedPath: Any
    'QPainterPath'
    contentLocked: Any
    'bool'
    contours: Any
    'list(flContour)'
    contoursCount: Any
    'int'
    excluded: Any
    'bool'
    flObjectFlags: dict
    fl_transform: Any
    'flTransform'
    hasBody: Any
    'bool'
    hasChanges: Any
    'bool'
    hasComponents: Any
    'bool'
    hasContours: Any
    'bool'
    hasGlobalAnchoring: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hasPath: Any
    'bool'
    hasSmartAngle: Any
    'bool'
    haveActiveShape: Any
    'bool'
    haveClosed: Any
    'bool'
    haveData: Any
    'bool'
    haveUnclosed: Any
    'bool'
    id: Any
    'object id'
    image: Any
    'QImage'
    imagePtr: Any
    'QImage *'
    includesList: Any
    'list(flShape)'
    isChanged: Any
    'bool'
    isComponent: Any
    'bool'
    isComposite: Any
    'bool'
    isEmpty: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isUnbindedDependencies: Any
    'bool'
    isUniform: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    opacity: Any
    'double'
    openedPath: Any
    'QPainterPath'
    pen: Any
    'QPen'
    refCnt: Any
    'object references count'
    selected: Any
    'bool'
    shapeBuilder: Any
    'flShapeBuilder'
    shapeData: Any
    'flShapeData'
    shapeType: Any
    'ShapeType'
    sticker: Any
    'flSticker'
    transform: Any
    'transform'
    type: Any
    'object type'

class flShapeBuilder:
    """flShapeBuilder representation

Constructors:
  flShapeBuilder()
  flShapeBuilder(flShapeBuilder)
  flShapeBuilder(flObject)

Native bases: object

Supplemental documentation:
Shape builder. The captured declaration exposes `deactivate`, `getSmartNodes`, `hasFeature`, `init`, `prepareTransformationData`, `resetTransformationData`, `setDestShape`, `setDestShapeData`, `setOwnerLayer`, `setOwnerShapeData`, `canUngroup`, `haveResult` and `title`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flShapeBuilder captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivate(self) -> Any:
        """deactivate()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getSmartNodes(self) -> Any:
        """list(flNode)/Nothing getSmartNodes()"""
        ...

    def hasFeature(self, BuilderFeatures: Any) -> bool:
        """bool hasFeature(BuilderFeatures)"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def init(self) -> Any:
        """init()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def prepareTransformationData(self) -> Any:
        """prepareTransformationData()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def resetTransformationData(self) -> Any:
        """resetTransformationData()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setDestShape(self, arg0: flShape) -> Any:
        """setDestShape(flShape)"""
        ...

    def setDestShapeData(self, arg0: flShapeData) -> Any:
        """setDestShapeData(flShapeData)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setOwnerLayer(self, arg0: flObject) -> Any:
        """setOwnerLayer(flObject)"""
        ...

    def setOwnerShapeData(self, arg0: flObject) -> Any:
        """setOwnerShapeData(flObject)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    canUngroup: Any
    'bool canUngroup()'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    haveResult: Any
    'bool haveResult()'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    title: Any
    'QString title()'
    type: Any
    'object type'

class flShapeData:
    """flShapeData representation

Constructors:
  flShapeData()
  flShapeData(flObject)

Native bases: object

Supplemental documentation:
Shape data. The captured declaration exposes `addContour`, `addContours`, `arrangeContours`, `assignContours`, `clearContours`, `clearIncludesList`, `goDown`, `goUp`, `includesList`, `removeAnchor`, `removeContour`, `sendToBack`, `sendToFront`, `sortContours`, `takeIncludesList`, `builder`, `componentGlyph`, `componentLayer`, `contours`, `includes`, `isComponent`, `isComposite`, `referenceCount`, `segments` and `shapeType`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flShapeData captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addContour(self, arg0: flContour) -> Any:
        """addContour(flContour)"""
        ...

    def addContours(self, *args: Any, **kwargs: Any) -> Any:
        """addContours(list(flContour))"""
        ...

    def arrangeContours(self) -> bool:
        """bool arrangeContours()"""
        ...

    def assignContours(self, *args: Any, **kwargs: Any) -> Any:
        """QMap<objId, flContour> assignContours(list(flContour)) | Nothing assignContours(fgShape)"""
        ...

    def bindDependencies(self) -> Any:
        """bindDependencies()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearContours(self) -> Any:
        """clearContours()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearIncludesList(self) -> Any:
        """clearIncludesList()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def goDown(self, arg0: flShape) -> bool:
        """bool goDown(flShape)"""
        ...

    def goUp(self, arg0: flShape) -> bool:
        """bool goUp(flShape)"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def includesList(self) -> Any:
        """list(flShape) includesList()"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def prepareTransformationData(self) -> Any:
        """prepareTransformationData()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeAnchor(self, arg0: flAnchor) -> Any:
        """removeAnchor(flAnchor)"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeContour(self, arg0: flContour) -> Any:
        """removeContour(flContour)"""
        ...

    def resetTransformationData(self) -> Any:
        """resetTransformationData()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def sendToBack(self, arg0: flShape) -> bool:
        """bool sendToBack(flShape)"""
        ...

    def sendToFront(self, arg0: flShape) -> bool:
        """bool sendToFront(flShape)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def sortContours(self, action: bool) -> Any:
        """sortContours(bool action)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def takeIncludesList(self) -> Any:
        """list(flShape) takeIncludesList()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    builder: Any
    'flObject builder()'
    componentGlyph: Any
    'string'
    componentLayer: Any
    'string'
    contours: Any
    'list(flContour) contours()'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    includes: Any
    'flObjectsList<flShape> includes()'
    isChanged: Any
    'bool'
    isComponent: Any
    'bool'
    isComposite: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    note: Any
    'string'
    refCnt: Any
    'object references count'
    referenceCount: Any
    'int'
    segments: Any
    'list(CurveEx) segments()'
    shapeType: Any
    'ShapeType shapeType()'
    type: Any
    'object type'

class flShapeInfo:
    """flShapeInfo representation

Constructors:
  flShapeInfo()
  flShapeInfo(flObject)
  flShapeInfo(flShapeInfo)
  flShapeInfo(flShape, flSearchInfo)
  flShapeInfo(flShape, QTransform)
  flShapeInfo(flShape, QTransform, QList<flShapeInfo> composites)
  flShapeInfo(flShape, QTransform, flObject glyph_info, QList<flShapeInfo> composites)
  flShapeInfo(flShape, flLayer, QTransform)
  flShapeInfo(flShape, flLayer, flObject glyph_info[, QTransform transform=QTransform()[, QList<flShapeInfo> composites=QList<flShapeInfo>()]])

Native bases: object

Supplemental documentation:
Shape information. The captured declaration exposes `shape`, `layer`, `composites`, `appendComposite`, `pushFrontComposite`, `takeFirstComposite`, `takeLastComposite`, `ownerComposite`, `ownerCompositeInfo`, `getContoursInfo`, `findNode`, `contains`, `boundingBox`, `toCanvasTransform`, `toGlyphTransform`, `replaceShape`, `move` and `hasAboveComposites`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flShapeInfo captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def appendComposite(self, arg0: flShapeInfo) -> Any:
        """appendComposite(flShapeInfo)"""
        ...

    def boundingBox(self) -> QRectF:
        """QRectF boundingBox()"""
        ...

    def brectOnCanvas(self) -> QRectF:
        """QRectF brectOnCanvas()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def combine(self, transform: QTransform) -> Any:
        """combine(QTransform transform)"""
        ...

    def compositesTransform(self) -> QTransform:
        """QTransform compositesTransform()"""
        ...

    def contains(self, s: Any=...) -> bool:
        """bool contains(QPointF canvas_pos[, double s=1])"""
        ...

    def createInstance(self) -> flShapeInfo:
        """flShapeInfo createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def findNode(self, arg0: QPointF) -> flNode:
        """flNode findNode(QPointF)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getContoursInfo(self) -> list[flObject]:
        """QList<flObject> getContoursInfo()"""
        ...

    def getHitIncludedShape(self, canvas_pos: QPointF, to_bottom: Any=...) -> Any:
        """flShapeInfo/Nothing getHitIncludedShape(QPointF canvas_pos, double scale[, bool to_bottom=false])"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasAboveComposites(self) -> bool:
        """bool hasAboveComposites()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isContentLockedSibling(self) -> bool:
        """bool isContentLockedSibling()"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def move(self, arg0: QPointF) -> QRectF:
        """QRectF move(QPointF)"""
        ...

    def ownerComposite(self) -> flShape:
        """flShape ownerComposite()"""
        ...

    def ownerCompositeInfo(self) -> flShapeInfo:
        """flShapeInfo ownerCompositeInfo()"""
        ...

    def pushFrontComposite(self, arg0: flShapeInfo) -> Any:
        """pushFrontComposite(flShapeInfo)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def replaceShape(self, arg0: flShape) -> Any:
        """replaceShape(flShape)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def takeFirstComposite(self) -> flShapeInfo:
        """flShapeInfo takeFirstComposite()"""
        ...

    def takeLastComposite(self) -> flShapeInfo:
        """flShapeInfo takeLastComposite()"""
        ...

    def toCanvasTransform(self) -> QTransform:
        """QTransform toCanvasTransform()"""
        ...

    def toGlyphTransform(self) -> QTransform:
        """QTransform toGlyphTransform()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    composites: Any
    'QList<flShapeInfo>'
    dist: Any
    'double dist'
    flObjectFlags: dict
    glyphInfo: Any
    'flObject - glyph info'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    layer: Any
    'flLayer'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    shape: Any
    'flShape'
    transform: Any
    'transform matrix'
    type: Any
    'object type'

class flSnapLine:
    """flSnapLine representation

Constructors:
  flSnapLine()
  flSnapLine(flObject)
  flSnapLine(flSnapLine)

Native bases: object

Supplemental documentation:
Snap line. The captured declaration exposes `distanceTo`, `offsetTo`, `getHashCode`, `isSnapLine`, `reset`, `setSnapFlag`, `setSnapFlagValue`, `snapFlag`, `angle`, `angleMode`, `center`, `centerPoint`, `color`, `constraints`, `expression`, `extLinef`, `extPosition`, `length`, `hasColor`, `hasExtLine`, `isHint`, `isZone`, `isPassive` and `isMeasurementLine`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flSnapLine captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def distanceTo(self, arg0: QPointF, mode: int) -> float:
        """double distanceTo(QPointF, uint mode)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getHashCode(self) -> Any:
        """SnapHashCode getHashCode()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isSnapLine(self, arg0: flObject) -> bool:
        """bool isSnapLine(flObject)"""
        ...

    def offsetTo(self, arg0: QPointF, mode: int) -> QPointF:
        """QPointF offsetTo(QPointF, uint mode)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def reset(self) -> Any:
        """reset()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSnapFlag(self, role: int, snapFlags: int) -> Any:
        """setSnapFlag(uint role, uint snapFlags)"""
        ...

    def setSnapFlagValue(self, role: int, bool: Any) -> Any:
        """setSnapFlagValue(uint role, bool)"""
        ...

    def snapFlag(self, role: int) -> int:
        """uint snapFlag(uint role)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    angle: Any
    'double'
    angleMode: Any
    'SnapAngleMode'
    center: Any
    'flNode'
    centerPoint: Any
    'QPointF'
    color: Any
    'QColor'
    constraints: Any
    'QRectF'
    expression: Any
    'QString'
    extLinef: Any
    'QLineF'
    extPosition: Any
    'double'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasColor: Any
    'bool'
    hasExpression: Any
    'bool'
    hasExtLine: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isAbsoluteMarkerPos: Any
    'bool'
    isChanged: Any
    'bool'
    isExluded: Any
    'bool'
    isHint: Any
    'bool'
    isInUse: Any
    'bool'
    isMeasurementLine: Any
    'bool'
    isNull: Any
    'bool'
    isPassive: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isShortGuideline: Any
    'bool'
    isValid: Any
    'bool'
    isZone: Any
    'bool'
    length: Any
    'double'
    linef: Any
    'QLineF'
    markers: Any
    'list(flMarkerPoint)'
    markersStructVersion: Any
    'int'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    snapFlags: Any
    'uint'
    style: Any
    'SnapObjectsStyle'
    type: Any
    'object type'
    vector: Any
    'flNode'
    vectorPoint: Any
    'QPointF'

class flSnapObject:
    """flSnapObject representation

Constructors:
  flSnapObject()
  flSnapObject(flObject)
  flSnapObject(flSnapObject)

Native bases: object

Supplemental documentation:
Snap object. The captured declaration exposes `distanceTo`, `offsetTo`, `getHashCode`, `reset`, `setSnapFlag`, `setSnapFlagValue`, `snapFlag`, `snapFlags`, `style`, `isHint`, `isZone`, `isPassive` and `isMeasurementLine`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flSnapObject captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def distanceTo(self, arg0: QPointF, mode: int) -> float:
        """double distanceTo(QPointF, uint mode)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getHashCode(self) -> Any:
        """SnapHashCode getHashCode()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def offsetTo(self, arg0: QPointF, mode: int) -> QPointF:
        """QPointF offsetTo(QPointF, uint mode)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def reset(self) -> Any:
        """reset()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSnapFlag(self, role: int, snapFlags: int) -> Any:
        """setSnapFlag(uint role, uint snapFlags)"""
        ...

    def setSnapFlagValue(self, role: int, bool: Any) -> Any:
        """setSnapFlagValue(uint role, bool)"""
        ...

    def snapFlag(self, role: int) -> int:
        """uint snapFlag(uint role)"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isExluded: Any
    'bool'
    isHint: Any
    'bool'
    isInUse: Any
    'bool'
    isMeasurementLine: Any
    'bool'
    isNull: Any
    'bool'
    isPassive: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    isZone: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    snapFlags: Any
    'uint'
    style: Any
    'SnapObjectsStyle'
    type: Any
    'object type'

class flSnaps:
    """snap object constants

Native bases: object

Supplemental documentation:
A holder of snap constants. The captured declaration exposes the dict attributes `FastGuidelines`, `MarkerFlags`, `MarkerKey`, `SnapLineFlags`, `SnapMode`, `SnapStyle` and `ViewMode`; it has no methods beyond the constructor.

Source: generated/fontlab.py: flSnaps captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...
    FastGuidelines: dict
    MarkerFlags: dict
    MarkerKey: dict
    SnapLineFlags: dict
    SnapMode: dict
    SnapStyle: dict
    ViewMode: dict

class flStem:
    """flStem representation

Constructors:
  flStem()
  flStem(double _v[, QString _n = ])
  flStem(fgStem)

Native bases: object

Supplemental documentation:
A stem described by `value` (double), with `name`, `tags`, `program` and `programText` attributes. The captured declaration also exposes `guaranteeName`, `linear`, `ppm`, `tagsSet` and `toStem`. Consult the retained constructor documentation for the supported creation forms.

Source: generated/fontlab.py: flStem captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def guaranteeName(self) -> Any:
        """guaranteeName()"""
        ...

    def linear(self, upm: float, k: int) -> int:
        """int linear(double upm, int k)"""
        ...

    def ppm(self, upm: float, k: int) -> int:
        """int ppm(double upm, int k)"""
        ...

    def tagsSet(self) -> Any:
        """QSet<QString>/Nothing tagsSet()"""
        ...

    def toStem(self, arg0: fgStem) -> Any:
        """toStem(fgStem)"""
        ...
    name: Any
    'string'
    program: Any
    'QSet<int, int>'
    programText: Any
    'QString'
    tags: Any
    'string'
    value: Any
    'double'

class flSticker:
    """flSticker representation

Constructors:
  flSticker()
  flSticker(flObject)
  flSticker(flSticker)
  flSticker(QString)

Native bases: object

Supplemental documentation:
A sticker object on the canvas. The captured declaration exposes the attributes `text`, `textRect`, `shape` and `boundingBox`, and the method `move`. It is created as `flSticker()`, `flSticker(flObject)`, `flSticker(flSticker)` or `flSticker(QString)`. It also carries the shared object members `name`, `id`, `type`, `isValid`, `release` and `remove`.

Source: generated/fontlab.py: flSticker captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def move(self, arg0: QPointF) -> Any:
        """move(QPointF)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    boundingBox: Any
    'QRectF boundingBox()'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    shape: Any
    'flShape shape()'
    text: Any
    'QString'
    textRect: Any
    'QRectF'
    type: Any
    'object type'

class flTTHCommand:
    """flTTHCommand representation

Constructors:
  flTTHCommand() - default

Native bases: object

Supplemental documentation:
A TrueType hinting command with `code`, `parameters` and `point_names` attributes. The captured declaration exposes `fromString`, `isDelta`, `isFinal`, `isHorizontal`, `isVertical`, `nodesCount`, `parametersCount`, `stemIndex` and `zoneIndex`. It is created as `flTTHCommand()`.

Source: generated/fontlab.py: flTTHCommand captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def fromString(self, arg0: str, itr: Any) -> bool:
        """bool fromString(QString, itr)"""
        ...

    def isDelta(self) -> bool:
        """bool isDelta()"""
        ...

    def isFinal(self) -> bool:
        """bool isFinal()"""
        ...

    def isHorizontal(self) -> bool:
        """bool isHorizontal()"""
        ...

    def isVertical(self) -> bool:
        """bool isVertical()"""
        ...

    def nodesCount(self) -> int:
        """int nodesCount()"""
        ...

    def parametersCount(self) -> int:
        """int parametersCount()"""
        ...

    def stemIndex(self) -> int:
        """int stemIndex()"""
        ...

    def zoneIndex(self) -> int:
        """int zoneIndex()"""
        ...
    code: Any
    'int'
    parameters: Any
    'QList<QVariant>'
    point_names: Any
    'QList<QString>'

class flTextBlock:
    """flTextBlock representation

Constructors:
  flTextBlock()
  flTextBlock(flObject)
  flTextBlock(flTextBlock)
  flTextBlock(flPackage, flTextObject[, int font_size=42[, int formatMode=tbfText[, QRectF canvas_rect=QRectF(0,0, 800,600)]]])

Native bases: object

Supplemental documentation:
Text block. The captured declaration exposes `addFeature`, `removeFeature`, `removeFeatures`, `setFeatures`, `features`, `fontSize`, `charsCount`, `glyphsCount`, `getAllGlyphs`, `getGlyphAt`, `getActiveGlyph`, `setActiveGlyph`, `getSelectedGlyphs`, `getSelectedCharacters`, `getLineIndex`, `getGlyphsInLine`, `reformat`, `textFits`, `script`, `frameRect` and `locked`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flTextBlock captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activeObjectChanged(self) -> flNotifier:
        """flNotifier activeObjectChanged()"""
        ...

    def activeRowRect(self) -> QRectF:
        """QRectF activeRowRect()"""
        ...

    def addFeature(self, feature: str) -> Any:
        """addFeature(QString feature)"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def charsCount(self) -> int:
        """int charsCount()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createInstance(self) -> flTextBlock:
        """flTextBlock createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def drawContent(self, *args: Any, **kwargs: Any) -> Any:
        """drawContent(QPainter*, flCanvas, QRectF painted_nodes_screen_rect)"""
        ...

    def features(self) -> Any:
        """list(QString) features()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def formatChanged(self) -> flNotifier:
        """flNotifier formatChanged()"""
        ...

    def getActiveGlyph(self) -> Any:
        """flGlyphInfo/Nothing getActiveGlyph()"""
        ...

    def getAllGlyphs(self, line_index: Any=...) -> Any:
        """list(flGlyphInfo)/Nothing getAllGlyphs([int line_index = -1])"""
        ...

    def getCurrentPosition(self) -> QPointF:
        """QPointF getCurrentPosition()"""
        ...

    def getGlyphAt(self, glyph_index: int) -> Any:
        """flGlyphInfo/Nothinf getGlyphAt(int glyph_index)"""
        ...

    def getGlyphInfo(self, *args: Any, **kwargs: Any) -> Any:
        """flGlyphInfo/Nothing getGlyphInfo(fgSymbol, &)"""
        ...

    def getGlyphTransform(self, glyph_index: int) -> QTransform:
        """QTransform getGlyphTransform(int glyph_index)"""
        ...

    def getGlyphsInLine(self, lineIndex: Any) -> Any:
        """list(flGlyphInfo)/Nothing getGlyphsInLine(flGlyphInfo | int lineIndex)"""
        ...

    def getHitGlyph(self, canvas_pos: QPointF) -> Any:
        """flGlyphInfo/Nothing getHitGlyph(QPointF canvas_pos)"""
        ...

    def getHitToShapeGlyph(self, canvas_pos: QPointF) -> Any:
        """flGlyphInfo/Nothing getHitToShapeGlyph(QPointF canvas_pos)"""
        ...

    def getHitToShapes(self, canvas_pos: QPointF) -> Any:
        """list(flContourInfo)/Nothing getHitToShapes(QPointF canvas_pos)"""
        ...

    def getIntersectsGlyphs(self, canvas_rect: QRectF) -> Any:
        """list(flGlyphInfo)/Nothing getIntersectsGlyphs(QRectF canvas_rect)"""
        ...

    def getLineIndex(self, glyph_index: int) -> int:
        """int getLineIndex(int glyph_index)"""
        ...

    def getLineLocation(self, glyph_info: flGlyphInfo) -> int:
        """int getLineLocation(flGlyphInfo glyph_info)"""
        ...

    def getMouseHitNode(self) -> Any:
        """flNodeInfo/Nothing getMouseHitNode()"""
        ...

    def getNearbyGlyphs(self, text_block_point: QPointF, max_dist: float) -> Any:
        """list(flGlyphInfo)/Nothing getNearbyGlyphs(QPointF text_block_point, double max_dist)"""
        ...

    def getNextGlyphInLine(self, glyph_index: int) -> Any:
        """flGlyphInfo/Nothing getNextGlyphInLine(int glyph_index)"""
        ...

    def getPrevGlyphInLine(self, glyph_index: int) -> Any:
        """flGlyphInfo/Nothing getPrevGlyphInLine(int glyph_index)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def getScvNode(self) -> Any:
        """flNodeInfo/Nothing getScvNode()"""
        ...

    def getSelectedCharacters(self) -> Any:
        """fgSymbolList/Nothing getSelectedCharacters()"""
        ...

    def getSelectedGlyphs(self) -> Any:
        """list(flGlyphInfo)/Nothing getSelectedGlyphs()"""
        ...

    def glyphsBoundsOnCanvas(self, EditMode: Any) -> QRectF:
        """QRectF glyphsBoundsOnCanvas(EditMode)"""
        ...

    def glyphsChanged(self) -> Any:
        """glyphsChanged()"""
        ...

    def glyphsCount(self) -> int:
        """int glyphsCount()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasHoveredNodeEdit(self) -> bool:
        """bool hasHoveredNodeEdit()"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def haveText(self) -> bool:
        """bool haveText()"""
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def hoveredNodeEdit(self) -> flNodeInfo:
        """flNodeInfo hoveredNodeEdit()"""
        ...

    def hoveredNodeEditDetails(self) -> Any:
        """HoveredInfoDetails hoveredNodeEditDetails()"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def init(self, canvas: flCanvas) -> Any:
        """init(flCanvas& canvas)"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isAltPressed(self) -> bool:
        """bool isAltPressed()"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isFramed(self) -> bool:
        """bool isFramed()"""
        ...

    def isMetaPressed(self) -> bool:
        """bool isMetaPressed()"""
        ...

    def keyPressEvent(self, *args: Any, **kwargs: Any) -> Any:
        """bool keyPressEvent(QKeyEvent*)"""
        ...

    def lastCharIndex(self) -> int:
        """int lastCharIndex()"""
        ...

    def lastIndex(self) -> int:
        """int lastIndex()"""
        ...

    def mouseDoubleClickEvent(self, *args: Any, **kwargs: Any) -> Any:
        """bool mouseDoubleClickEvent(QMouseEvent*)"""
        ...

    def mouseMoveEvent(self, *args: Any, **kwargs: Any) -> Any:
        """bool mouseMoveEvent(QMouseEvent*)"""
        ...

    def mousePressEvent(self, *args: Any, **kwargs: Any) -> Any:
        """bool mousePressEvent(QMouseEvent*)"""
        ...

    def mouseReleaseEvent(self, *args: Any, **kwargs: Any) -> Any:
        """bool mouseReleaseEvent(QMouseEvent*)"""
        ...

    def paintedNodesScreenRect(self) -> QRectF:
        """QRectF paintedNodesScreenRect()"""
        ...

    def paragraphBlock(self) -> fgParagraphBlock:
        """fgParagraphBlock paragraphBlock()"""
        ...

    def parentTextBlock(self) -> flTextBlock:
        """flTextBlock parentTextBlock()"""
        ...

    def reformat(self) -> Any:
        """reformat()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeFeature(self, feature: str) -> Any:
        """removeFeature(QString feature)"""
        ...

    def removeFeatures(self) -> Any:
        """removeFeatures()"""
        ...

    def removedFromCanvas(self) -> Any:
        """removedFromCanvas()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setActiveGlyph(self, arg0: flGlyphInfo) -> Any:
        """setActiveGlyph(flGlyphInfo)"""
        ...

    def setAltPressed(self, redraw: Any=...) -> Any:
        """setAltPressed(bool b[, bool redraw = true])"""
        ...

    def setCheckMouseHoverNode(self, bool: Any) -> Any:
        """setCheckMouseHoverNode(bool)"""
        ...

    def setExclusiveEditing(self, bool: Any) -> Any:
        """setExclusiveEditing(bool)"""
        ...

    def setFeatures(self, *args: Any, **kwargs: Any) -> Any:
        """setFeatures(list(QString), bool reformat)"""
        ...

    def setFixedHeight(self, *args: Any, **kwargs: Any) -> Any:
        """setFixedHeight(bool, bool)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setFrameSize(self, canvas_size: QSizeF) -> Any:
        """setFrameSize(QSizeF canvas_size)"""
        ...

    def setFrameWidth(self, double: Any) -> Any:
        """setFrameWidth(double)"""
        ...

    def setLeftMetric(self, glyph_info: flGlyphInfo, measurement: bool) -> Any:
        """setLeftMetric(flGlyphInfo glyph_info, bool measurement)"""
        ...

    def setMetaPressed(self, redraw: Any=...) -> Any:
        """setMetaPressed(bool b[, bool redraw = true])"""
        ...

    def setParentTextBlock(self, arg0: flTextBlock) -> Any:
        """setParentTextBlock(flTextBlock)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setRightMetric(self, arg0: QPointF, glyph_info: flGlyphInfo, measurement: bool) -> Any:
        """setRightMetric(QPointF, flGlyphInfo glyph_info, bool measurement)"""
        ...

    def setShowCursor(self, bool: Any) -> Any:
        """setShowCursor(bool)"""
        ...

    def setShowNodes(self, bool: Any) -> Any:
        """setShowNodes(bool)"""
        ...

    def setTextBlockMode(self, viewport_pos: Any=...) -> Any:
        """setTextBlockMode(EditMode text_block_mode[, QPoint viewport_pos=QPoint()])"""
        ...

    def symbolList(self) -> fgSymbolList:
        """fgSymbolList symbolList()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def textFits(self) -> bool:
        """bool textFits()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateSymbols(self) -> Any:
        """updateSymbols()"""
        ...

    def visibleShapes(self) -> Any:
        """list(flShape)/Nothing visibleShapes()"""
        ...
    editMode: Any
    'EditMode'
    flObjectFlags: dict
    fontSize: Any
    'int'
    formatMode: Any
    'int'
    frameRect: Any
    'QRectF'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    initiallySelected: Any
    'bool'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    kerningProcessing: Any
    'bool'
    layoutProcessing: Any
    'bool'
    locked: Any
    'bool'
    marksProcessing: Any
    'bool'
    name: Any
    'object name'
    package: Any
    'flPackage'
    refCnt: Any
    'object references count'
    script: Any
    'uint'
    textObject: Any
    'flTextObject'
    transform: Any
    'QTransform'
    type: Any
    'object type'

class flTransform:
    """flTransform representation

Constructors:
  flTransform()
  flTransform(flTransform)
  flTransform(flObject)
  flTransform(QTransform)

Native bases: object

Supplemental documentation:
A transform object. The captured declaration exposes the attributes `transform` and `scale` and the methods `map`, `mapRect` and `translate`. It is created as `flTransform()`, `flTransform(flTransform)`, `flTransform(flObject)` or `flTransform(QTransform)`. It also carries the shared object members `name`, `id`, `type`, `isValid`, `release` and `remove`.

Source: generated/fontlab.py: flTransform captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def map(self, *args: Any, **kwargs: Any) -> Any:
        """QPointF map(QPointF) | QLineF map(QLineF) | double map(double)"""
        ...

    def mapRect(self, QRect: Any) -> QRectF:
        """QRectF mapRect(QRectF | QRect)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def translate(self, x: Any, y: float) -> None:
        """void translate(QPointF | double x, double y)"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    name: Any
    'object name'
    refCnt: Any
    'object references count'
    scale: Any
    'double'
    transform: Any
    'QTransform'
    type: Any
    'object type'

class flVectorNode:
    """flVectorNode representation

Constructors:
  flVectorNode(flObject)
  flVectorNode(flVectorNode)
  flVectorNode(flGuideLine, QPointF)

Native bases: object

Supplemental documentation:
Vector node. The captured declaration exposes `angleTo`, `canBeSmooth`, `canCollapse`, `collapseHandles`, `convertToCurve`, `convertToLine`, `moveBy`, `rotateBy`, `scaleBy`, `skewBy`, `makeStart`, `nextNode`, `prevNode`, `isCurve`, `isOn`, `isOff`, `isFirst`, `isLast`, `smooth`, `position`, `selected`, `x`, `y`, `guideline`, `mode`, `setPositionMode` and `isVectorNode`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flVectorNode captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def angleTo(self, p: QPointF) -> float:
        """double angleTo(QPointF p)"""
        ...

    def applyTransform(self, arg0: QTransform) -> Any:
        """applyTransform(QTransform)"""
        ...

    def canBeHobby(self) -> bool:
        """bool canBeHobby()"""
        ...

    def canBeSmooth(self) -> bool:
        """bool canBeSmooth()"""
        ...

    def canCollapse(self) -> bool:
        """bool canCollapse()"""
        ...

    def canImprove(self) -> bool:
        """bool canImprove()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def checkVectors(self) -> bool:
        """bool checkVectors()"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearStored(self) -> Any:
        """clearStored()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneMapped(self, arg0: QTransform) -> flNode:
        """flNode cloneMapped(QTransform)"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def collapseHandles(self) -> bool:
        """bool collapseHandles()"""
        ...

    def convertToCurve(self, smooth: Any=...) -> bool:
        """bool convertToCurve([bool smooth = false])"""
        ...

    def convertToCurves(self) -> bool:
        """bool convertToCurves()"""
        ...

    def convertToLine(self) -> bool:
        """bool convertToLine()"""
        ...

    def copyFrom(self, withSelected: Any=...) -> Any:
        """copyFrom(Node[, withSelected=False])"""
        ...

    def createInstance(self) -> flVectorNode:
        """flVectorNode createInstance()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        """double distanceTo(Node/QPointF)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getLines(self, *args: Any, **kwargs: Any) -> Any:
        """(QLineF, QLineF)/None getLines()"""
        ...

    def getOn(self) -> Any:
        """Node/None getOn()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def improve(self) -> bool:
        """bool improve()"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isCorner(self, a: Any=...) -> bool:
        """bool isCorner([double a = 10.])"""
        ...

    def isCurve(self) -> bool:
        """bool isCurve()"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isEqualTo(self, tolerance: Any=...) -> bool:
        """bool isEqualTo(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])"""
        ...

    def isExtreme(self, open: Any=...) -> bool:
        """bool isExtreme(bool x[, bool open = true[, double limit = 0]])"""
        ...

    def isFirst(self) -> bool:
        """bool isFirst()"""
        ...

    def isG2(self, tolerance: float) -> bool:
        """bool isG2(double tolerance)"""
        ...

    def isInternal(self, clockwise: bool) -> bool:
        """bool isInternal(bool clockwise)"""
        ...

    def isInterpolated(self, x: bool) -> bool:
        """bool isInterpolated(bool x)"""
        ...

    def isLast(self) -> bool:
        """bool isLast()"""
        ...

    def isOff(self) -> bool:
        """bool isOff()"""
        ...

    def isOn(self) -> bool:
        """bool isOn()"""
        ...

    def isSmartAngle(self) -> bool:
        """bool isSmartAngle()"""
        ...

    def isVectorNode(self, arg0: flObject) -> bool:
        """bool isVectorNode(flObject)"""
        ...

    def makeStart(self) -> bool:
        """bool makeStart()"""
        ...

    def moveBy(self, *args: Any, **kwargs: Any) -> Any:
        """moveBy(float dx, float dy[, bool round=false]"""
        ...

    def nextNode(self, nodeType: Any=...) -> Any:
        """Node/None nextNode([string nodeType= [, int searchDepth=1]])"""
        ...

    def pointG2(self) -> Any:
        """QPointF/None pointG2()"""
        ...

    def prevNode(self, nodeType: Any=...) -> Any:
        """Node/None prevNode([string nodeType= [, int searchDepth=1]])"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def restoreCoordinates(self) -> Any:
        """restoreCoordinates()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def rotateBy(self, origin: Any=...) -> Any:
        """rotateBy(valueDegree[, QPointF origin=(0, 0)])"""
        ...

    def round(self) -> Any:
        """round() - Round the node's coordinate"""
        ...

    def scaleBy(self, origin: Any=...) -> Any:
        """scaleBy(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])"""
        ...

    def setExtraLast(self, bool: Any) -> Any:
        """setExtraLast(bool)"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setNextSmooth(self, base: QPointF) -> Any:
        """setNextSmooth(QPointF base)"""
        ...

    def setPosition(self, arg0: QPointF) -> None:
        """void setPosition(QPointF)"""
        ...

    def setPositionMode(self, m: Any) -> None:
        """void setPositionMode(Mode m)"""
        ...

    def setPrevSmooth(self, base: QPointF) -> Any:
        """setPrevSmooth(QPointF base)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setSmartAngleEnbl(self, bool: Any) -> bool:
        """bool setSmartAngleEnbl(bool)"""
        ...

    def setSmartSharp(self, tension: Any=...) -> bool:
        """bool setSmartSharp([double tension = 0.6])"""
        ...

    def skewBy(self, origin: Any=...) -> Any:
        """skewBy(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])"""
        ...

    def smartMove(self, offset: Any) -> Any:
        """list(uint) smartMove(offset)"""
        ...

    def smartSetXY(self, arg0: QPointF) -> Any:
        """smartSetXY(QPointF)"""
        ...

    def storeCoordinates(self) -> Any:
        """storeCoordinates()"""
        ...

    def storeTestParameters(self) -> Any:
        """storeTestParameters()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def transformBy(self, origin: Any=...) -> Any:
        """transformBy(QTransform tx[, QPointF origin=(0, 0)])"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateG2(self) -> bool:
        """bool updateG2()"""
        ...

    def updateSmooth(self, extended_neibh: Any=...) -> Any:
        """updateSmooth([bool extended_neibh=true])"""
        ...
    Mode: dict
    NodeKind: dict
    NodeType: dict
    angle: Any
    'angle'
    contour: Any
    'The parent Contour or None if not present'
    flObjectFlags: dict
    g2: Any
    'g2'
    guideline: Any
    'flGuideLine'
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hobby: Any
    'hobby'
    id: Any
    'object id'
    index: Any
    "The index of the node in parent's contour (if present, otherwise -1)"
    interpolated: Any
    'interpolated'
    interpolatedX: Any
    'interpolatedX'
    interpolatedY: Any
    'interpolatedY'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isSelectedAlone: Any
    'bool'
    isTerminal: Any
    'bool'
    isValid: Any
    'bool'
    mode: Any
    'uint'
    name: Any
    'object name'
    nodeState: Any
    'nodeState'
    position: Any
    'Coordinates of the node as QPointF'
    preview: Any
    'preview'
    refCnt: Any
    'object references count'
    scv: Any
    'scv'
    selected: Any
    'The selected flag'
    smartAngleR: Any
    'smartAngleR'
    smooth: Any
    'The smooth flag'
    state: Any
    'state'
    type: Any
    'The node type'
    x: Any
    'The x coordinate of the node'
    y: Any
    'The y coordinate of the node'

class flVisualItem:
    """flVisualItem representation

Constructors:
  flVisualItem()
  flVisualItem(flVisualItem)
  flVisualItem(flObject)
  flVisualItem(objId id)

Native bases: object

Supplemental documentation:
Visual item. The captured declaration exposes `appendDecorator`, `clearDecorators`, `clearItems`, `contain`, `containsItem`, `hide`, `show`, `move`, `select`, `unselect`, `invselect`, `mapCanvasToItem`, `mapItemToCanvas`, `mapCanvasDistanceToItem`, `paint`, `canvas`, `opacity`, `visible`, `selected`, `locked` and `itemScale`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flVisualItem captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def acceptEvents(self) -> int:
        """int acceptEvents()"""
        ...

    def activateEditor(self, canvas_pos: QPointF) -> None:
        """void activateEditor(QPointF canvas_pos)"""
        ...

    def addedToCanvas(self, arg0: flCanvas) -> None:
        """void addedToCanvas(flCanvas)"""
        ...

    def adjustCanvasPosition(self, arg0: QPointF) -> QPointF:
        """QPointF adjustCanvasPosition(QPointF)"""
        ...

    def adjustPosition(self, double: Any) -> Any:
        """QPointF | double adjustPosition(QPointF | double)"""
        ...

    def appendDecorator(self, arg0: flVisualItem, DecoratorOrder: Any) -> None:
        """void appendDecorator(flVisualItem, DecoratorOrder)"""
        ...

    def boundingRectOnCanvas(self, *args: Any, **kwargs: Any) -> Any:
        """QRectF boundingRectOnCanvas("""
        ...

    def canvas(self) -> flCanvas:
        """flCanvas canvas()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearDecorators(self) -> Any:
        """clearDecorators()"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clearItems(self) -> Any:
        """clearItems()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def contain(self, canvas_pos: QPointF) -> bool:
        """bool contain(QPointF canvas_pos)"""
        ...

    def containsItem(self, arg0: flVisualItem) -> bool:
        """bool containsItem(flVisualItem)"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivateEditor(self) -> Any:
        """deactivateEditor()"""
        ...

    def distanceTo(self, arg0: QPointF) -> float:
        """double distanceTo(QPointF)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def haveCanvas(self) -> bool:
        """bool haveCanvas()"""
        ...

    def haveEditor(self, canvas_pos: QPointF) -> bool:
        """bool haveEditor(QPointF canvas_pos)"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def hide(self) -> Any:
        """hide()"""
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instanceAcceptEvents(self) -> int:
        """int instanceAcceptEvents()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def invselect(self) -> Any:
        """invselect()"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isSelectable(self) -> bool:
        """bool isSelectable()"""
        ...

    def isStableSelect(self) -> bool:
        """bool isStableSelect()"""
        ...

    def itemScale(self) -> float:
        """double itemScale()"""
        ...

    def mapCanvasDistanceToItem(self, arg0: QPointF) -> QPointF:
        """QPointF mapCanvasDistanceToItem(QPointF)"""
        ...

    def mapCanvasToItem(self, QRectF: Any) -> Any:
        """QPointF | QRectF mapCanvasToItem(QPointF | QRectF)"""
        ...

    def mapItemToCanvas(self, QRectF: Any) -> Any:
        """QPointF | QRectF mapItemToCanvas(QPointF | QRectF)"""
        ...

    def metricStep(self) -> float:
        """double metricStep()"""
        ...

    def move(self, arg0: QPointF) -> None:
        """void move(QPointF)"""
        ...

    def paint(self, *args: Any, **kwargs: Any) -> Any:
        """void paint(QPainter*)"""
        ...

    def preview(self) -> Any:
        """preview()"""
        ...

    def referencePoint(self) -> QPointF:
        """QPointF referencePoint()"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def removeDecorator(self, arg0: flVisualItem) -> None:
        """void removeDecorator(flVisualItem)"""
        ...

    def removeItem(self, arg0: flVisualItem) -> None:
        """void removeItem(flVisualItem)"""
        ...

    def removedFromCanvas(self) -> Any:
        """removedFromCanvas()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def select(self) -> Any:
        """select()"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def show(self) -> Any:
        """show()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def unselect(self) -> Any:
        """unselect()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...
    Listeners: dict
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    hovered: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    locked: Any
    'bool'
    name: Any
    'object name'
    opacity: Any
    'double'
    owner: Any
    'flVisualItem'
    refCnt: Any
    'object references count'
    selected: Any
    'bool'
    transform: Any
    'QTransform'
    type: Any
    'object type'
    visible: Any
    'bool'

class flWorkspace:
    """flWorkspace representation

Constructors:
  flWorkspace()
  flWorkspace(flWorkspace)
  flWorkspace(flObject)
  flWorkspace(objId id)
  flWorkspace(QString title)

Native bases: object

Supplemental documentation:
Workspace. The captured declaration exposes `addPackage`, `closePackage`, `closeProject`, `createNewProject`, `readProject`, `saveProject`, `currentPackage`, `currentGlyph`, `packages`, `canvases`, `getActiveCanvas`, `setActiveCanvas`, `hasPackage`, `findPackageId`, `exportCurrentFont`, `exportFont`, `doZoomIn`, `doZoomOut`, `setRulers` and `isRulersEnabled`. It is created with no captured constructor overloads. It also carries the shared object members `changed`, `clone`, `cloneObject`, `getProperty`, `setProperty`, `release`, `remove` and `update` and the shared attributes `id`, `name`, `type`, `isValid` and `isNull`.

Source: generated/fontlab.py: flWorkspace captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activateEditor(self, arg0: flVisualItem, canvas_pos: QPointF) -> Any:
        """activateEditor(flVisualItem, QPointF canvas_pos)"""
        ...

    def activateNext(self) -> Any:
        """activateNext()"""
        ...

    def activatePrev(self) -> Any:
        """activatePrev()"""
        ...

    def addFamilyMembers(self, match_subfamily: Any=...) -> bool:
        """bool addFamilyMembers(QList<flPackage> &packages[, bool match_subfamily = false])"""
        ...

    def addPackage(self, arg0: flPackage) -> Any:
        """addPackage(flPackage)"""
        ...

    def attachCanvas(self, arg0: flCanvas) -> Any:
        """attachCanvas(flCanvas)"""
        ...

    def blockUpdate(self, time: Any=...) -> Any:
        """blockUpdate([int time = 2000])"""
        ...

    def canvases(self) -> list[flObject]:
        """QList<flObject> canvases()"""
        ...

    def changed(self) -> Any:
        """changed()"""
        ...

    def checkInitHistoryState(self, history_ix: int) -> Any:
        """checkInitHistoryState(uint history_ix)"""
        ...

    def clearAboveHistory(self, history_ix: int) -> Any:
        """clearAboveHistory(uint history_ix)"""
        ...

    def clearFlag(self, f: int) -> Any:
        """clearFlag(uint f)"""
        ...

    def clearFlags(self) -> Any:
        """clearFlags()"""
        ...

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone the object"""
        ...

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject cloneObject(const flObject&); """
        ...

    def closePackage(self, arg0: flPackage) -> Any:
        """closePackage(flPackage)"""
        ...

    def closeProject(self) -> Any:
        """closeProject()"""
        ...

    def convertMouseEvent(self, QMouseEvent: Any, arg1: QPoint) -> flMouseEvent:
        """flMouseEvent convertMouseEvent(QEvent | QMouseEvent, QPoint)"""
        ...

    def createNewProject(self) -> Any:
        """createNewProject()"""
        ...

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        """flObject/Nothing createObject(int);    """
        ...

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """currentHistoryIx()"""
        ...

    def deactivateEditor(self) -> Any:
        """deactivateEditor()"""
        ...

    def destroyCanvas(self, arg0: flCanvas) -> Any:
        """destroyCanvas(flCanvas)"""
        ...

    def doZoomIn(self, s: Any=...) -> Any:
        """doZoomIn([double s = 2.0])"""
        ...

    def doZoomOut(self, s: Any=...) -> Any:
        """doZoomOut([double s = 0.5])"""
        ...

    def exportCurrentFont(self) -> Any:
        """exportCurrentFont()"""
        ...

    def exportFont(self, arg0: flPackage, ExportControl: Any) -> Any:
        """exportFont(flPackage, ExportControl)"""
        ...

    def exportTo(self, filename: str, format: str=...) -> bool:
        """bool exportTo(QString filename, QString format=['EPS' | 'JPG' | 'PDF' | 'PNG' | 'SVG'])"""
        ...

    def findPackageId(self, id: int) -> flPackage:
        """flPackage findPackageId(uint id)"""
        ...

    def flag(self, f: int) -> Any:
        """flag(uint f)"""
        ...

    def getActiveCanvas(self) -> Any:
        """flCanvas/Nothing getActiveCanvas()"""
        ...

    def getActiveTextBlock(self) -> Any:
        """flTextBlockItem/Nothing getActiveTextBlock()"""
        ...

    def getBoundingRect(self) -> QRectF:
        """QRectF getBoundingRect()"""
        ...

    def getCanvasForViewport(self, *args: Any, **kwargs: Any) -> Any:
        """flCanvas/Nothing getCanvasForViewport(QWidget*)"""
        ...

    def getCanvasUnderCursor(self) -> flCanvas:
        """flCanvas getCanvasUnderCursor()"""
        ...

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        """Get object's properties list"""
        ...

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        """getProperty('key') - get object property by 'key' or number """
        ...

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyFloat('key') - get float object property by 'key'"""
        ...

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """getPropertyInt('key') - get int object property by 'key'"""
        ...

    def guidelinesUpdater(self) -> flNotifier:
        """flNotifier guidelinesUpdater()"""
        ...

    def hasHistoryState(self, history_ix: int) -> Any:
        """hasHistoryState(uint history_ix)"""
        ...

    def hasPackage(self, flPackage: Any) -> bool:
        """bool hasPackage(const flPackage)"""
        ...

    def haveActiveEditor(self) -> bool:
        """bool haveActiveEditor()"""
        ...

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        """bool haveObject(uint);                 """
        ...

    def historyStates(self, accepted_state: bool) -> Any:
        """historyStates(bool accepted_state)"""
        ...

    def independedAll(self) -> Any:
        """independedAll()"""
        ...

    def init(self) -> Any:
        """init()"""
        ...

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        """initialHistoryIx()"""
        ...

    def instance(self) -> flWorkspace:
        """flWorkspace instance()"""
        ...

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        """int instanceType();                    """
        ...

    def isActiveCanvas(self, flCanvas: Any) -> bool:
        """bool isActiveCanvas(const flCanvas)"""
        ...

    def isEqual(self, arg0: flObject) -> Any:
        """isEqual(flObject)"""
        ...

    def isRulersEnabled(self) -> bool:
        """bool isRulersEnabled()"""
        ...

    def packages(self) -> list[flObject]:
        """QList<flObject>& packages()"""
        ...

    def previewRender(self) -> bool:
        """bool previewRender()"""
        ...

    def readProject(self, QString: Any) -> bool:
        """bool readProject(const QString)"""
        ...

    def release(self) -> Any:
        """release()"""
        ...

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove([flObject])"""
        ...

    def removeChild(self, arg0: flObject) -> Any:
        """removeChild(flObject)"""
        ...

    def resetToolCursor(self) -> Any:
        """resetToolCursor()"""
        ...

    def restoreHistoryState(self, history_ix: int) -> Any:
        """restoreHistoryState(uint history_ix)"""
        ...

    def saveProject(self, *args: Any, **kwargs: Any) -> Any:
        """saveProject([QString]) | bool saveProject(QString, QList<fgFont>, QString ui_state"""
        ...

    def setActiveCanvas(self, arg0: flCanvas) -> Any:
        """setActiveCanvas(flCanvas)"""
        ...

    def setActiveSketchboard(self) -> Any:
        """setActiveSketchboard()"""
        ...

    def setAutoMode(self) -> Any:
        """setAutoMode()"""
        ...

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """setFlag(uint f [, bool value])"""
        ...

    def setFocusToCanvas(self, arg0: flCanvas) -> Any:
        """setFocusToCanvas(flCanvas)"""
        ...

    def setPreviewRender(self, bool: Any) -> Any:
        """setPreviewRender(bool)"""
        ...

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        """setProperty('key', value) - set object property by 'key' or number """
        ...

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyFloat('key', value) - set float object property by 'key'"""
        ...

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        """setPropertyInt('key', value) - set int object property by 'key'"""
        ...

    def setRenderMode(self, RenderMode: Any) -> Any:
        """setRenderMode(RenderMode)"""
        ...

    def setRulers(self, enabled: bool) -> Any:
        """setRulers(bool enabled)"""
        ...

    def setToolBrush(self) -> Any:
        """setToolBrush()"""
        ...

    def setToolBucket(self) -> Any:
        """setToolBucket()"""
        ...

    def setToolCursor(self, CursorId: Any) -> Any:
        """setToolCursor(CursorId)"""
        ...

    def setToolEditor(self) -> Any:
        """setToolEditor()"""
        ...

    def setToolEllipse(self) -> Any:
        """setToolEllipse()"""
        ...

    def setToolGuidelines(self) -> Any:
        """setToolGuidelines()"""
        ...

    def setToolKnife(self) -> Any:
        """setToolKnife()"""
        ...

    def setToolMagnet(self) -> Any:
        """setToolMagnet()"""
        ...

    def setToolMetrics(self) -> Any:
        """setToolMetrics()"""
        ...

    def setToolOptimizer(self) -> Any:
        """setToolOptimizer()"""
        ...

    def setToolPen(self) -> Any:
        """setToolPen()"""
        ...

    def setToolPencil(self) -> Any:
        """setToolPencil()"""
        ...

    def setToolRectangle(self) -> Any:
        """setToolRectangle()"""
        ...

    def setToolRotate(self) -> Any:
        """setToolRotate()"""
        ...

    def setToolScale(self) -> Any:
        """setToolScale()"""
        ...

    def setToolScissors(self) -> Any:
        """setToolScissors()"""
        ...

    def setToolShape(self) -> Any:
        """setToolShape()"""
        ...

    def setToolSlant(self) -> Any:
        """setToolSlant()"""
        ...

    def setToolSmartPen(self) -> Any:
        """setToolSmartPen()"""
        ...

    def setToolText(self) -> Any:
        """setToolText()"""
        ...

    def setToolTransform(self) -> Any:
        """setToolTransform()"""
        ...

    def showFocus(self) -> bool:
        """bool showFocus()"""
        ...

    def showSmallItems(self) -> bool:
        """bool showSmallItems()"""
        ...

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        """tag([string])"""
        ...

    def turnTextModeOff(self) -> Any:
        """turnTextModeOff()"""
        ...

    def unblockUpdate(self) -> Any:
        """unblockUpdate()"""
        ...

    def update(self) -> Any:
        """update()"""
        ...

    def updateActiveViewport(self) -> Any:
        """updateActiveViewport()"""
        ...

    def weAreOnPaper(self) -> bool:
        """bool weAreOnPaper()"""
        ...
    RenderMode: dict
    activeFontPanel: Any
    'QWidget*'
    activeTextMode: Any
    'EditMode'
    currentFontPanel: Any
    'QWidget*'
    currentGlyph: Any
    'flGlyphInfo'
    currentPackage: Any
    'flPackage'
    cursorId: Any
    'CursorId'
    defaultFontSize: Any
    'int'
    flObjectFlags: dict
    hasChanges: Any
    'bool'
    hasHistoryStates: Any
    'bool'
    id: Any
    'object id'
    isChanged: Any
    'bool'
    isNull: Any
    'bool'
    isPresent: Any
    'bool'
    isReleased: Any
    'bool'
    isValid: Any
    'bool'
    mainWindow: Any
    'QWidget*'
    name: Any
    'object name'
    paintBrush: Any
    'PaintBrush'
    refCnt: Any
    'object references count'
    signedObjects: Any
    'QMap<objId,flObject>'
    sketchboard: Any
    'flCanvas, bool new_paper'
    toolBarButtonStyle: Any
    'toolBarButtonStyle'
    type: Any
    'object type'
    uiState: Any
    'QString'

class flZone:
    """flZone representation

Constructors:
  flZone()
  flZone(double p, double w[, QString _n = ])
  flZone(flZone)

Native bases: object

Supplemental documentation:
An alignment zone described by `position` and `width` (both double), with `name`, `tags`, `program` and `programText` attributes. The captured declaration also exposes `guaranteeName`, `tagsSet` and `toZone`. Consult the retained constructor documentation for the supported creation forms.

Source: generated/fontlab.py: flZone captured declaration"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def guaranteeName(self, top: bool) -> Any:
        """guaranteeName(bool top)"""
        ...

    def tagsSet(self) -> Any:
        """QSet<QString>/Nothing tagsSet()"""
        ...

    def toZone(self, arg0: fgZone, top: bool) -> Any:
        """toZone(fgZone, bool top)"""
        ...
    name: Any
    'string'
    position: Any
    'double'
    program: Any
    'QSet<int, int>'
    programText: Any
    'QString'
    tags: Any
    'string'
    width: Any
    'double'

def AcceptChanges(clearChangedState: Any=...) -> Any:
    """AcceptChanges([bool clearChangedState = true])"""
    ...

def AllFonts(*args: Any, **kwargs: Any) -> Any:
    """Get a list of currently opened fonts"""
    ...

def ApplicationPath(*args: Any, **kwargs: Any) -> Any:
    """Return path to FontLab main application"""
    ...

def CountFonts(*args: Any, **kwargs: Any) -> Any:
    """Return number of currently opened fonts"""
    ...

def CreatePanel(*args: Any, **kwargs: Any) -> Any:
    """Create YPanelWidget instance"""
    ...

def CurrentFont(*args: Any, **kwargs: Any) -> Any:
    """Get currently active font"""
    ...

def CurrentGlyph(*args: Any, **kwargs: Any) -> Any:
    """Get currently active glyph"""
    ...

def GetFileName(open_save: Any, extension: Any, filename: Any, filters: Any) -> Any:
    """GetFileName(open_save, string extension, string filename, string filters) - opens the file dialog. open_save = 1 for file open dialog"""
    ...

def GetPathName(*args: Any, **kwargs: Any) -> Any:
    """GetPathName(String title, ...) - allows to select folder"""
    ...

def GetProperty(*args: Any, **kwargs: Any) -> Any:
    """Get FL properties (keywords: output, ...)"""
    ...

def MainWindow(*args: Any, **kwargs: Any) -> Any:
    """Get MainWindow object"""
    ...

def PanelManager(*args: Any, **kwargs: Any) -> Any:
    """Get YPanelManager object"""
    ...

def SetCurrentFont(*args: Any, **kwargs: Any) -> Any:
    """Set active font"""
    ...

def SetCurrentGlyph(*args: Any, **kwargs: Any) -> Any:
    """Set active glyph"""
    ...

def SetProperty(*args: Any, **kwargs: Any) -> Any:
    """Set FL properties (keywords: output, ...)"""
    ...

def TestBuilder(*args: Any, **kwargs: Any) -> Any:
    """Test Glyph Builder"""
    ...

def Update(*args: Any, **kwargs: Any) -> Any:
    """Update object and it's visual representations. Without argument update all changed objects. Update([fgGlyph|fgFont|flObject object])"""
    ...

def UpdateActiveCanvas() -> Any:
    """UpdateActiveCanvas()"""
    ...

def UpdateAll() -> Any:
    """UpdateAll()"""
    ...

def UpdateGlyphRect(x0: Any, y0: Any, x1: Any, y1: Any) -> Any:
    """UpdateGlyphRect(x0, y0, x1, y1)"""
    ...
BinaryFormatVersion: dict
BuilderFeatures: dict
DecoratorOrder: dict
EditMode: dict
GlyphInfoState: dict
HintingDataType: dict
LightNodesMode: dict
ObjectFlag: dict
SelectionMode: dict
ShapeCloneInfo: dict
ShapeType: dict
SnapAngleMode: dict
SnapObjectsStyle: dict
TextBlockFormat: dict
TransformFrameControls: dict
ViewPointAlignment: dict
flTools: dict
__all__ = ['AccentInfo', 'AcceptChanges', 'AllFonts', 'ApplicationPath', 'BinaryFormatVersion', 'BuilderFeatures', 'CountFonts', 'CreatePanel', 'CurrentFont', 'CurrentGlyph', 'CurveEx', 'DecoratorOrder', 'EditMode', 'ExportControl', 'FaBasicPtr', 'FontLayer', 'FontMetrics', 'GetFileName', 'GetPathName', 'GetProperty', 'GlyphComponent', 'GlyphInfoState', 'HintingDataType', 'Info', 'Interval', 'LightNodesMode', 'LocationValue', 'MainWindow', 'ObjectFlag', 'PaintBrush', 'PaintBrushShape', 'PanelManager', 'SelectionMode', 'SetCurrentFont', 'SetCurrentGlyph', 'SetProperty', 'ShapeCloneInfo', 'ShapeType', 'SmartCornerParameters', 'SnapAngleMode', 'SnapObjectsStyle', 'TestBuilder', 'TextBlockFormat', 'TransformFrame', 'TransformFrameControls', 'Update', 'UpdateActiveCanvas', 'UpdateAll', 'UpdateGlyphRect', 'ViewPointAlignment', 'YPanelManager', 'YPanelWidget', 'fgSymbol', 'fgSymbolList', 'flAbstractEditor', 'flAbstractVectorNode', 'flAnchor', 'flAuditInfo', 'flAxis', 'flBasicTool', 'flCanvas', 'flContour', 'flContourInfo', 'flEvent', 'flExpression', 'flGlyph', 'flGlyphInfo', 'flGraphicsInfo', 'flGuideLine', 'flHintingParameters', 'flInstance', 'flItems', 'flLayer', 'flLayerAttributes', 'flLayerInfo', 'flLocation', 'flMarkerPoint', 'flModel', 'flModelProducer', 'flMouseEvent', 'flNode', 'flNodeInfo', 'flObject', 'flObjectsList<flGuideLine>', 'flObjectsList<flShape>', 'flPackage', 'flPaper', 'flPinPoint', 'flPreferences', 'flProperty', 'flPropertyDouble', 'flPropertyPoint', 'flSearchInfo', 'flShape', 'flShapeBuilder', 'flShapeData', 'flShapeInfo', 'flSnapLine', 'flSnapObject', 'flSnaps', 'flStem', 'flSticker', 'flTTHCommand', 'flTextBlock', 'flTools', 'flTransform', 'flVectorNode', 'flVisualItem', 'flWorkspace', 'flZone']
