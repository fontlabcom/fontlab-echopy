# this_file: generated/fontlab.py
# Generated from native API metadata; edit enrichment inputs, then merge.
'Python interface for FontLab data objects\n\nCurveEx: CurveEx representation\nExportControl: ExportControl representation\nFaBasicPtr: FaBasicPtr representation\nInterval: Interval representation\nPaintBrush: PaintBrush representation\nTransformFrame: TransformFrame representation\nfgSymbol: fgSymbol representation\nfgSymbolList: fgSymbolList representation\nflAbstractEditor: flAbstractEditor representation\nflAbstractVectorNode: flAbstractVectorNode representation\nflAnchor: flAnchor representation\nflAuditInfo: flAuditInfo representation\nflAxis: flAxis representation\nflBasicTool: flBasicTool representation\nflCanvas: flCanvas representation\nflContour: flContour representation\nflContourInfo: flContourInfo representation\nflEvent: flEvent representation\nflExpression: flExpression representation\nflGlyph: flGlyph representation\nflGlyphInfo: flGlyphInfo representation\nflGraphicsInfo: flGraphicsInfo representation\nflGuideLine: flGuideLine representation\nflHintingParameters: flHintingParameters representation\nflInstance: flInstance representation\nflItems: flItems representation\nflLayer: flLayer representation\nflLayerInfo: flLayerInfo representation\nflLocation: flLocation representation\nLocationValue: LocationValue representation\nflMarkerPoint: flMarkerPoint representation\nflMouseEvent: flMouseEvent representation\nflModelProducer: flModelProducer representation\nflNode: flNode representation\nflNodeInfo: flNodeInfo representation\nflObject: flObject representation\nflPackage: flPackage representation\nflPaper: flPaper representation\nflPinPoint: flPinPoint representation\nflPreferences: flPreferences representation\nflProperty: flProperty representation\nflPropertyDouble: flPropertyDouble representation\nflPropertyPoint: flPropertyPoint representation\nflSearchInfo: flSearchInfo representation\nflShape: flShape representation\nflShapeBuilder: flShapeBuilder representation\nflShapeData: flShapeData representation\nflShapeInfo: flShapeInfo representation\nflSnapLine: flSnapLine representation\nflSnapObject: flSnapObject representation\nflStem: flStem representation\nflZone: flZone representation\nflSticker: flSticker representation\nflTextBlock: flTextBlock representation\nflTransform: flTransform representation\nflVectorNode: flVectorNode representation\nflVisualItem: flVisualItem representation\nflWorkspace: flWorkspace representation\nFontMetrics: FontMetrics representation\nGlyphComponent: GlyphComponent representation\nflTTHCommand: flTTHCommand representation\nYPanelManager: YPanelManager representation\nYPanelWidget: YPanelWidget representation\nInfo: Font Info data\nFontLayer: FontLayer object\nflObjectsList<flGuideLine>: flObjectsList<flGuideLine> doc\nflObjectsList<flShape>: flObjectsList<flShape> doc\nflSnaps: snap object constants\nflModel: flModel representation\nPaintBrushShape: Data wrapper\nSmartCornerParameters: Data wrapper\nAccentInfo: Data wrapper\nflLayerAttributes: Data wrapper'
from __future__ import annotations
from typing import Any
from fontlab_echopy._runtime import bind as _bind, unavailable as _unavailable

class AccentInfo:
    'Data wrapper\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.AccentInfo')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontlab.AccentInfo.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontlab.AccentInfo.asTuple')

    layer: Any
    offset: Any

class CurveEx:
    'CurveEx representation\n\nConstructors:\n  CurveEx() - default\n  CurveEx(QPointF p0, QPointF p1[, int leftIdx=0[, int _rightIdx=0]])\n  CurveEx(QPointF p0, QPointF p1, QPointF p2, QPointF p3)\n  CurveEx( list(QPointF) )\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.CurveEx')

    def applyTransform(self, tx: QTransform) -> None:
        'void applyTransform(QTransform& tx)'
        _unavailable('fontlab.CurveEx.applyTransform')

    def empty(self) -> bool:
        'bool empty()'
        _unavailable('fontlab.CurveEx.empty')

    def extremum(self, prev: Any) -> bool:
        'bool extremum(CurveEx prev)'
        _unavailable('fontlab.CurveEx.extremum')

    def fastLength(self) -> float:
        'double fastLength()'
        _unavailable('fontlab.CurveEx.fastLength')

    def improve(self, curvature: Any = ...) -> bool:
        'bool improve([double curvature = 1.0])'
        _unavailable('fontlab.CurveEx.improve')

    def smooth(self, prev: Any) -> bool:
        'bool smooth(CurveEx prev)'
        _unavailable('fontlab.CurveEx.smooth')

    def smoothCurvature(self, c1: Any, complete: bool) -> Any:
        'CurveEx smoothCurvature(CurveEx c1, bool complete)'
        _unavailable('fontlab.CurveEx.smoothCurvature')

    def split(self, *args: Any, **kwargs: Any) -> Any:
        'bool split(CurveEx, CurveEx)'
        _unavailable('fontlab.CurveEx.split')

    def updateBRect(self) -> None:
        'void updateBRect()'
        _unavailable('fontlab.CurveEx.updateBRect')

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
    'ExportControl representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.ExportControl')

    def init(self) -> Any:
        'init()'
        _unavailable('fontlab.ExportControl.init')

    def load(self) -> bool:
        'bool load()'
        _unavailable('fontlab.ExportControl.load')

    def store(self) -> Any:
        'store()'
        _unavailable('fontlab.ExportControl.store')

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
    'FaBasicPtr representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.FaBasicPtr')

    def fix(self) -> Any:
        'flGlyph/Nothing fix()'
        _unavailable('fontlab.FaBasicPtr.fix')

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
    'FontLayer object\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.FontLayer')


class FontMetrics:
    'FontMetrics representation\n\nConstructors:\n  FontMetrics() - default\n  FontMetrics(FontMetrics)\n  FontMetrics(double upm)\n  FontMetrics(fg::Package *p)\n  FontMetrics(flPackage p, string layer_name)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.FontMetrics')

    def init(self) -> Any:
        'init()'
        _unavailable('fontlab.FontMetrics.init')

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
    'GlyphComponent representation\n\nConstructors:\n  GlyphComponent() - default\n  GlyphComponent(GlyphComponent)\n  GlyphComponent(uint id)\n  GlyphComponent(string name)\n  GlyphComponent(uint id, QTransform tx, double w, bool ua)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.GlyphComponent')

    name_id: Any
    'uint'
    transform: Any
    'QTransform'
    use_anchors: Any
    'bool'
    width_scale: Any
    'double'

class Info:
    'Font Info data\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.Info')

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
    'Interval representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.Interval')

    def isEmpty(self) -> bool:
        'bool isEmpty()'
        _unavailable('fontlab.Interval.isEmpty')

    def middle(self) -> float:
        'double middle()'
        _unavailable('fontlab.Interval.middle')

    def reversed(self) -> Any:
        'Interval reversed()'
        _unavailable('fontlab.Interval.reversed')

    def setT0T1(self, t0: float, t1: float) -> None:
        'void setT0T1(double t0, double t1)'
        _unavailable('fontlab.Interval.setT0T1')

    def toAbsolute(self, v: float) -> float:
        'double toAbsolute(double v)'
        _unavailable('fontlab.Interval.toAbsolute')

    def toInterval(self, absv: float) -> float:
        'double toInterval(double absv)'
        _unavailable('fontlab.Interval.toInterval')

    d: Any
    'double d'
    key: Any
    'uint key'
    t0: Any
    'double t0'
    t1: Any
    'double t1'

class LocationValue:
    'LocationValue representation\n\nConstructors:\n  LocationValue(flLocation)\n  LocationValue(double)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.LocationValue')


class PaintBrush:
    'PaintBrush representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.PaintBrush')

    def assign(self, PaintBrush: Any) -> None:
        'void assign(PaintBrush)'
        _unavailable('fontlab.PaintBrush.assign')

    def init(self) -> None:
        'void init()'
        _unavailable('fontlab.PaintBrush.init')

    def render(self, scale: float) -> None:
        'void render(double scale)'
        _unavailable('fontlab.PaintBrush.render')

    def toString(self) -> str:
        'QString toString()'
        _unavailable('fontlab.PaintBrush.toString')

    angle: Any
    'double'
    flatness: Any
    'double'
    shape: Any
    'PaintBrushShape'
    size: Any
    'double'

class PaintBrushShape:
    'Data wrapper\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.PaintBrushShape')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontlab.PaintBrushShape.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontlab.PaintBrushShape.asTuple')

    cap0: Any
    cap1: Any
    cap_length0: Any
    cap_length1: Any
    data: Any

class SmartCornerParameters:
    'Data wrapper\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.SmartCornerParameters')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontlab.SmartCornerParameters.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontlab.SmartCornerParameters.asTuple')

    curvature: Any

class TransformFrame:
    'TransformFrame representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.TransformFrame')

    def boundingRect(self) -> QRectF:
        'QRectF boundingRect()'
        _unavailable('fontlab.TransformFrame.boundingRect')

    def bw(self) -> float:
        'double bw()          '
        _unavailable('fontlab.TransformFrame.bw')

    def doTransformation(self, code: int, value: QPointF) -> None:
        'void doTransformation(int code, QPointF value)'
        _unavailable('fontlab.TransformFrame.doTransformation')

    def expandPolygon(self, polygon: QPolygonF) -> QPolygonF:
        'QPolygonF expandPolygon(QPolygonF polygon)'
        _unavailable('fontlab.TransformFrame.expandPolygon')

    def flipHorizontal(self) -> None:
        'void flipHorizontal()                         '
        _unavailable('fontlab.TransformFrame.flipHorizontal')

    def flipVertical(self) -> None:
        'void flipVertical()                           '
        _unavailable('fontlab.TransformFrame.flipVertical')

    def getControlPos(self, TransformFrameControls: Any) -> QPointF:
        'QPointF getControlPos(TransformFrameControls) '
        _unavailable('fontlab.TransformFrame.getControlPos')

    def getMapped(self, t: QTransform) -> Any:
        'TransformFrame getMapped(QTransform t)        '
        _unavailable('fontlab.TransformFrame.getMapped')

    def getTransform(self) -> QTransform:
        'QTransform getTransform()'
        _unavailable('fontlab.TransformFrame.getTransform')

    def horizontalReflection(self) -> None:
        'void horizontalReflection()                   '
        _unavailable('fontlab.TransformFrame.horizontalReflection')

    def initCenter(self) -> None:
        'void initCenter()                             '
        _unavailable('fontlab.TransformFrame.initCenter')

    def lh(self) -> float:
        'double lh()          '
        _unavailable('fontlab.TransformFrame.lh')

    def mb(self) -> QPointF:
        'QPointF mb()         '
        _unavailable('fontlab.TransformFrame.mb')

    def mh(self) -> float:
        'double mh()          '
        _unavailable('fontlab.TransformFrame.mh')

    def ml(self) -> QPointF:
        'QPointF ml()         '
        _unavailable('fontlab.TransformFrame.ml')

    def mr(self) -> QPointF:
        'QPointF mr()         '
        _unavailable('fontlab.TransformFrame.mr')

    def mt(self) -> QPointF:
        'QPointF mt()         '
        _unavailable('fontlab.TransformFrame.mt')

    def mw(self) -> float:
        'double mw()          '
        _unavailable('fontlab.TransformFrame.mw')

    def polygon(self) -> QPolygonF:
        'QPolygonF polygon()  '
        _unavailable('fontlab.TransformFrame.polygon')

    def prepareTransformations(self, scale: Any) -> None:
        'void prepareTransformations([TransformFrameControls control, QPointF p,] double scale)'
        _unavailable('fontlab.TransformFrame.prepareTransformations')

    def rh(self) -> float:
        'double rh()          '
        _unavailable('fontlab.TransformFrame.rh')

    def rotate(self, double: Any) -> None:
        'void rotate(double)                           '
        _unavailable('fontlab.TransformFrame.rotate')

    def rotate180(self) -> None:
        'void rotate180()                              '
        _unavailable('fontlab.TransformFrame.rotate180')

    def scale(self, s: QPointF) -> None:
        'void scale(QPointF s)                         '
        _unavailable('fontlab.TransformFrame.scale')

    def setControlPos(self, position: Any, reflection: bool, proportional: bool, fixed: bool) -> None:
        'void setControlPos([TransformFrameControls control,] QPointF position, bool reflection, bool proportional, bool fixed)'
        _unavailable('fontlab.TransformFrame.setControlPos')

    def setProjectionPos(self, position: Any, reflection: bool, proportional: bool, fixed: bool) -> None:
        'void setProjectionPos([TransformFrameControls control,] QPointF position, bool reflection, bool proportional, bool fixed)'
        _unavailable('fontlab.TransformFrame.setProjectionPos')

    def slant(self, *args: Any, **kwargs: Any) -> Any:
        'void slant(double angle, double angle)        '
        _unavailable('fontlab.TransformFrame.slant')

    def translate(self, arg0: QPointF) -> None:
        'void translate(QPointF)                       '
        _unavailable('fontlab.TransformFrame.translate')

    def tw(self) -> float:
        'double tw()          '
        _unavailable('fontlab.TransformFrame.tw')

    def verticalReflection(self) -> None:
        'void verticalReflection()                     '
        _unavailable('fontlab.TransformFrame.verticalReflection')

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
    'PythonQtInstanceWrapper object\n\nNative bases: PythonQtInstanceWrapper'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.YPanelManager')

    def blockSignals(self, b: Any) -> bool:
        'X.blockSignals(b) -> bool'
        _unavailable('fontlab.YPanelManager.blockSignals')

    def childEvent(self, event: Any) -> Any:
        'X.childEvent(event)'
        _unavailable('fontlab.YPanelManager.childEvent')

    def children(self) -> tuple:
        'X.children() -> tuple'
        _unavailable('fontlab.YPanelManager.children')

    def className(self, *args: Any, **kwargs: Any) -> Any:
        'Return the classname of the object'
        _unavailable('fontlab.YPanelManager.className')

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        'X.connect(signal, receiver, slot, type) -> bool'
        _unavailable('fontlab.YPanelManager.connect')

    def customEvent(self, event: Any) -> Any:
        'X.customEvent(event)'
        _unavailable('fontlab.YPanelManager.customEvent')

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        'Deletes the C++ object (at your own risk, my friend!)'
        _unavailable('fontlab.YPanelManager.delete')

    def deleteLater(self) -> Any:
        'X.deleteLater()'
        _unavailable('fontlab.YPanelManager.deleteLater')

    def desktopClientRectChanged(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelManager.desktopClientRectChanged; argument details are not documented.'
        _unavailable('fontlab.YPanelManager.desktopClientRectChanged')

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelManager.destroyed; argument details are not documented.'
        _unavailable('fontlab.YPanelManager.destroyed')

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        'X.disconnect(signal, receiver, slot) -> bool'
        _unavailable('fontlab.YPanelManager.disconnect')

    def dumpObjectInfo(self) -> Any:
        'X.dumpObjectInfo()'
        _unavailable('fontlab.YPanelManager.dumpObjectInfo')

    def dumpObjectTree(self) -> Any:
        'X.dumpObjectTree()'
        _unavailable('fontlab.YPanelManager.dumpObjectTree')

    def dynamicPropertyNames(self) -> Any:
        'X.dynamicPropertyNames()'
        _unavailable('fontlab.YPanelManager.dynamicPropertyNames')

    def event(self, event: Any) -> bool:
        'X.event(event) -> bool'
        _unavailable('fontlab.YPanelManager.event')

    def eventFilter(self, watched: Any, event: Any) -> bool:
        'X.eventFilter(watched, event) -> bool'
        _unavailable('fontlab.YPanelManager.eventFilter')

    def findChild(self, type: Any, name: Any) -> Any:
        'X.findChild(type, name) -> PythonQt.private.QObject'
        _unavailable('fontlab.YPanelManager.findChild')

    def findChildren(self, type: Any, name: Any) -> tuple:
        'X.findChildren(type, name) -> tuple'
        _unavailable('fontlab.YPanelManager.findChildren')

    def help(self, *args: Any, **kwargs: Any) -> Any:
        'Shows the help of available methods for this class'
        _unavailable('fontlab.YPanelManager.help')

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        'Returns if the class inherits or is of given type name'
        _unavailable('fontlab.YPanelManager.inherits')

    def installEventFilter(self, filterObj: Any) -> Any:
        'X.installEventFilter(filterObj)'
        _unavailable('fontlab.YPanelManager.installEventFilter')

    def isSignalConnected(self, signal: Any) -> bool:
        'X.isSignalConnected(signal) -> bool'
        _unavailable('fontlab.YPanelManager.isSignalConnected')

    def isWidgetType(self) -> bool:
        'X.isWidgetType() -> bool'
        _unavailable('fontlab.YPanelManager.isWidgetType')

    def isWindowType(self) -> bool:
        'X.isWindowType() -> bool'
        _unavailable('fontlab.YPanelManager.isWindowType')

    def killTimer(self, id: Any) -> Any:
        'X.killTimer(id)'
        _unavailable('fontlab.YPanelManager.killTimer')

    def metaObject(self) -> Any:
        'X.metaObject() -> PythonQt.QtCore.QMetaObject'
        _unavailable('fontlab.YPanelManager.metaObject')

    def moveToThread(self, thread: Any) -> Any:
        'X.moveToThread(thread)'
        _unavailable('fontlab.YPanelManager.moveToThread')

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelManager.objectNameChanged; argument details are not documented.'
        _unavailable('fontlab.YPanelManager.objectNameChanged')

    def panelClosed(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelManager.panelClosed; argument details are not documented.'
        _unavailable('fontlab.YPanelManager.panelClosed')

    def parent(self) -> Any:
        'X.parent() -> PythonQt.private.QObject'
        _unavailable('fontlab.YPanelManager.parent')

    def property(self, name: Any) -> Any:
        'X.property(name) -> object'
        _unavailable('fontlab.YPanelManager.property')

    def removeEventFilter(self, obj: Any) -> Any:
        'X.removeEventFilter(obj)'
        _unavailable('fontlab.YPanelManager.removeEventFilter')

    def sender(self) -> Any:
        'X.sender() -> PythonQt.private.QObject'
        _unavailable('fontlab.YPanelManager.sender')

    def senderSignalIndex(self) -> int:
        'X.senderSignalIndex() -> int'
        _unavailable('fontlab.YPanelManager.senderSignalIndex')

    def setObjectName(self, name: Any) -> Any:
        'X.setObjectName(name)'
        _unavailable('fontlab.YPanelManager.setObjectName')

    def setParent(self, parent: Any) -> Any:
        'X.setParent(parent)'
        _unavailable('fontlab.YPanelManager.setParent')

    def setProperty(self, name: Any, value: Any) -> bool:
        'X.setProperty(name, value) -> bool'
        _unavailable('fontlab.YPanelManager.setProperty')

    def showContextMenu(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelManager.showContextMenu; argument details are not documented.'
        _unavailable('fontlab.YPanelManager.showContextMenu')

    def signalsBlocked(self) -> bool:
        'X.signalsBlocked() -> bool'
        _unavailable('fontlab.YPanelManager.signalsBlocked')

    def startTimer(self, interval: Any, timerType: Any) -> int:
        'X.startTimer(interval, timerType) -> int'
        _unavailable('fontlab.YPanelManager.startTimer')

    def thread(self) -> Any:
        'X.thread()'
        _unavailable('fontlab.YPanelManager.thread')

    def timerEvent(self, event: Any) -> Any:
        'X.timerEvent(event)'
        _unavailable('fontlab.YPanelManager.timerEvent')

    def toolbarClosed(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelManager.toolbarClosed; argument details are not documented.'
        _unavailable('fontlab.YPanelManager.toolbarClosed')

    def toolbarOpened(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelManager.toolbarOpened; argument details are not documented.'
        _unavailable('fontlab.YPanelManager.toolbarOpened')

    def tr(self, text: Any, ambig: Any, n: Any) -> str:
        'X.tr(text, ambig, n) -> str'
        _unavailable('fontlab.YPanelManager.tr')

    objectName: Any

class YPanelWidget:
    'PythonQtInstanceWrapper object\n\nNative bases: PythonQtInstanceWrapper'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.YPanelWidget')

    def actionEvent(self, event: Any) -> Any:
        'X.actionEvent(event)'
        _unavailable('fontlab.YPanelWidget.actionEvent')

    def actions(self) -> tuple:
        'X.actions() -> tuple'
        _unavailable('fontlab.YPanelWidget.actions')

    def activateWindow(self) -> Any:
        'X.activateWindow()'
        _unavailable('fontlab.YPanelWidget.activateWindow')

    def addAction(self, action: Any) -> Any:
        'X.addAction(action)'
        _unavailable('fontlab.YPanelWidget.addAction')

    def addActions(self, actions: Any) -> Any:
        'X.addActions(actions)'
        _unavailable('fontlab.YPanelWidget.addActions')

    def adjustSize(self) -> Any:
        'X.adjustSize()'
        _unavailable('fontlab.YPanelWidget.adjustSize')

    def backgroundRole(self) -> Any:
        'X.backgroundRole()'
        _unavailable('fontlab.YPanelWidget.backgroundRole')

    def backingStore(self) -> Any:
        'X.backingStore() -> PythonQt.QtGui.QBackingStore'
        _unavailable('fontlab.YPanelWidget.backingStore')

    def blockSignals(self, b: Any) -> bool:
        'X.blockSignals(b) -> bool'
        _unavailable('fontlab.YPanelWidget.blockSignals')

    def changeEvent(self, arg__1: Any) -> Any:
        'X.changeEvent(arg__1)'
        _unavailable('fontlab.YPanelWidget.changeEvent')

    def childAt(self, x: Any, y: Any) -> Any:
        'X.childAt(x, y) -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.childAt')

    def childEvent(self, event: Any) -> Any:
        'X.childEvent(event)'
        _unavailable('fontlab.YPanelWidget.childEvent')

    def children(self) -> tuple:
        'X.children() -> tuple'
        _unavailable('fontlab.YPanelWidget.children')

    def className(self, *args: Any, **kwargs: Any) -> Any:
        'Return the classname of the object'
        _unavailable('fontlab.YPanelWidget.className')

    def clearFocus(self) -> Any:
        'X.clearFocus()'
        _unavailable('fontlab.YPanelWidget.clearFocus')

    def clearMask(self) -> Any:
        'X.clearMask()'
        _unavailable('fontlab.YPanelWidget.clearMask')

    def close(self) -> bool:
        'X.close() -> bool'
        _unavailable('fontlab.YPanelWidget.close')

    def closeEvent(self, event: Any) -> Any:
        'X.closeEvent(event)'
        _unavailable('fontlab.YPanelWidget.closeEvent')

    def colorCount(self) -> int:
        'X.colorCount() -> int'
        _unavailable('fontlab.YPanelWidget.colorCount')

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        'X.connect(signal, receiver, slot, type) -> bool'
        _unavailable('fontlab.YPanelWidget.connect')

    def contentsMargins(self) -> Any:
        'X.contentsMargins() -> PythonQt.QtGui.QMargins'
        _unavailable('fontlab.YPanelWidget.contentsMargins')

    def contentsRect(self) -> Any:
        'X.contentsRect() -> PythonQt.QtCore.QRect'
        _unavailable('fontlab.YPanelWidget.contentsRect')

    def contextMenuEvent(self, event: Any) -> Any:
        'X.contextMenuEvent(event)'
        _unavailable('fontlab.YPanelWidget.contextMenuEvent')

    def createWinId(self) -> Any:
        'X.createWinId()'
        _unavailable('fontlab.YPanelWidget.createWinId')

    def createWindowContainer(self, window: Any, parent: Any, arg2: flags) -> Any:
        'X.createWindowContainer(window, parent, flags) -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.createWindowContainer')

    def customContextMenuRequested(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelWidget.customContextMenuRequested; argument details are not documented.'
        _unavailable('fontlab.YPanelWidget.customContextMenuRequested')

    def customEvent(self, event: Any) -> Any:
        'X.customEvent(event)'
        _unavailable('fontlab.YPanelWidget.customEvent')

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        'Deletes the C++ object (at your own risk, my friend!)'
        _unavailable('fontlab.YPanelWidget.delete')

    def deleteLater(self) -> Any:
        'X.deleteLater()'
        _unavailable('fontlab.YPanelWidget.deleteLater')

    def depth(self) -> int:
        'X.depth() -> int'
        _unavailable('fontlab.YPanelWidget.depth')

    def destroy(self, destroyWindow: Any, destroySubWindows: Any) -> Any:
        'X.destroy(destroyWindow, destroySubWindows)'
        _unavailable('fontlab.YPanelWidget.destroy')

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelWidget.destroyed; argument details are not documented.'
        _unavailable('fontlab.YPanelWidget.destroyed')

    def devType(self) -> int:
        'X.devType() -> int'
        _unavailable('fontlab.YPanelWidget.devType')

    def devicePixelRatio(self) -> int:
        'X.devicePixelRatio() -> int'
        _unavailable('fontlab.YPanelWidget.devicePixelRatio')

    def devicePixelRatioF(self) -> float:
        'X.devicePixelRatioF() -> float'
        _unavailable('fontlab.YPanelWidget.devicePixelRatioF')

    def devicePixelRatioFScale(self) -> float:
        'X.devicePixelRatioFScale() -> float'
        _unavailable('fontlab.YPanelWidget.devicePixelRatioFScale')

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        'X.disconnect(signal, receiver, slot) -> bool'
        _unavailable('fontlab.YPanelWidget.disconnect')

    def dragEnterEvent(self, event: Any) -> Any:
        'X.dragEnterEvent(event)'
        _unavailable('fontlab.YPanelWidget.dragEnterEvent')

    def dragLeaveEvent(self, event: Any) -> Any:
        'X.dragLeaveEvent(event)'
        _unavailable('fontlab.YPanelWidget.dragLeaveEvent')

    def dragMoveEvent(self, event: Any) -> Any:
        'X.dragMoveEvent(event)'
        _unavailable('fontlab.YPanelWidget.dragMoveEvent')

    def dropEvent(self, event: Any) -> Any:
        'X.dropEvent(event)'
        _unavailable('fontlab.YPanelWidget.dropEvent')

    def dumpObjectInfo(self) -> Any:
        'X.dumpObjectInfo()'
        _unavailable('fontlab.YPanelWidget.dumpObjectInfo')

    def dumpObjectTree(self) -> Any:
        'X.dumpObjectTree()'
        _unavailable('fontlab.YPanelWidget.dumpObjectTree')

    def dynamicPropertyNames(self) -> Any:
        'X.dynamicPropertyNames()'
        _unavailable('fontlab.YPanelWidget.dynamicPropertyNames')

    def effectiveWinId(self) -> int:
        'X.effectiveWinId() -> int'
        _unavailable('fontlab.YPanelWidget.effectiveWinId')

    def ensurePolished(self) -> Any:
        'X.ensurePolished()'
        _unavailable('fontlab.YPanelWidget.ensurePolished')

    def enterEvent(self, event: Any) -> Any:
        'X.enterEvent(event)'
        _unavailable('fontlab.YPanelWidget.enterEvent')

    def event(self, event: Any) -> bool:
        'X.event(event) -> bool'
        _unavailable('fontlab.YPanelWidget.event')

    def eventFilter(self, watched: Any, event: Any) -> bool:
        'X.eventFilter(watched, event) -> bool'
        _unavailable('fontlab.YPanelWidget.eventFilter')

    def findChild(self, type: Any, name: Any) -> Any:
        'X.findChild(type, name) -> PythonQt.private.QObject'
        _unavailable('fontlab.YPanelWidget.findChild')

    def findChildren(self, type: Any, name: Any) -> tuple:
        'X.findChildren(type, name) -> tuple'
        _unavailable('fontlab.YPanelWidget.findChildren')

    def focusInEvent(self, event: Any) -> Any:
        'X.focusInEvent(event)'
        _unavailable('fontlab.YPanelWidget.focusInEvent')

    def focusNextChild(self) -> bool:
        'X.focusNextChild() -> bool'
        _unavailable('fontlab.YPanelWidget.focusNextChild')

    def focusNextPrevChild(self, next: Any) -> bool:
        'X.focusNextPrevChild(next) -> bool'
        _unavailable('fontlab.YPanelWidget.focusNextPrevChild')

    def focusOutEvent(self, event: Any) -> Any:
        'X.focusOutEvent(event)'
        _unavailable('fontlab.YPanelWidget.focusOutEvent')

    def focusPreviousChild(self) -> bool:
        'X.focusPreviousChild() -> bool'
        _unavailable('fontlab.YPanelWidget.focusPreviousChild')

    def focusProxy(self) -> Any:
        'X.focusProxy() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.focusProxy')

    def focusWidget(self) -> Any:
        'X.focusWidget() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.focusWidget')

    def fontInfo(self) -> Any:
        'X.fontInfo() -> PythonQt.QtGui.QFontInfo'
        _unavailable('fontlab.YPanelWidget.fontInfo')

    def fontMetrics(self) -> Any:
        'X.fontMetrics() -> PythonQt.QtGui.QFontMetrics'
        _unavailable('fontlab.YPanelWidget.fontMetrics')

    def foregroundRole(self) -> Any:
        'X.foregroundRole()'
        _unavailable('fontlab.YPanelWidget.foregroundRole')

    def grab(self, rectangle: Any) -> Any:
        'X.grab(rectangle) -> PythonQt.QtGui.QPixmap'
        _unavailable('fontlab.YPanelWidget.grab')

    def grabGesture(self, type: Any, arg1: flags) -> Any:
        'X.grabGesture(type, flags)'
        _unavailable('fontlab.YPanelWidget.grabGesture')

    def grabKeyboard(self) -> Any:
        'X.grabKeyboard()'
        _unavailable('fontlab.YPanelWidget.grabKeyboard')

    def grabMouse(self, arg__1: Any) -> Any:
        'X.grabMouse(arg__1)'
        _unavailable('fontlab.YPanelWidget.grabMouse')

    def grabShortcut(self, key: Any, context: Any) -> int:
        'X.grabShortcut(key, context) -> int'
        _unavailable('fontlab.YPanelWidget.grabShortcut')

    def graphicsEffect(self) -> Any:
        'X.graphicsEffect() -> PythonQt.QtGui.QGraphicsEffect'
        _unavailable('fontlab.YPanelWidget.graphicsEffect')

    def graphicsProxyWidget(self) -> Any:
        'X.graphicsProxyWidget() -> PythonQt.QtGui.QGraphicsProxyWidget'
        _unavailable('fontlab.YPanelWidget.graphicsProxyWidget')

    def hasFocus(self) -> bool:
        'X.hasFocus() -> bool'
        _unavailable('fontlab.YPanelWidget.hasFocus')

    def hasHeightForWidth(self) -> bool:
        'X.hasHeightForWidth() -> bool'
        _unavailable('fontlab.YPanelWidget.hasHeightForWidth')

    def hasMouseTracking(self) -> bool:
        'X.hasMouseTracking() -> bool'
        _unavailable('fontlab.YPanelWidget.hasMouseTracking')

    def heightForWidth(self, arg__1: Any) -> int:
        'X.heightForWidth(arg__1) -> int'
        _unavailable('fontlab.YPanelWidget.heightForWidth')

    def heightMM(self) -> int:
        'X.heightMM() -> int'
        _unavailable('fontlab.YPanelWidget.heightMM')

    def help(self, *args: Any, **kwargs: Any) -> Any:
        'Shows the help of available methods for this class'
        _unavailable('fontlab.YPanelWidget.help')

    def hide(self) -> Any:
        'X.hide()'
        _unavailable('fontlab.YPanelWidget.hide')

    def hideEvent(self, event: Any) -> Any:
        'X.hideEvent(event)'
        _unavailable('fontlab.YPanelWidget.hideEvent')

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        'Returns if the class inherits or is of given type name'
        _unavailable('fontlab.YPanelWidget.inherits')

    def initPainter(self, painter: Any) -> Any:
        'X.initPainter(painter)'
        _unavailable('fontlab.YPanelWidget.initPainter')

    def inputMethodEvent(self, arg__1: Any) -> Any:
        'X.inputMethodEvent(arg__1)'
        _unavailable('fontlab.YPanelWidget.inputMethodEvent')

    def inputMethodQuery(self, arg__1: Any) -> Any:
        'X.inputMethodQuery(arg__1) -> object'
        _unavailable('fontlab.YPanelWidget.inputMethodQuery')

    def insertAction(self, before: Any, action: Any) -> Any:
        'X.insertAction(before, action)'
        _unavailable('fontlab.YPanelWidget.insertAction')

    def insertActions(self, before: Any, actions: Any) -> Any:
        'X.insertActions(before, actions)'
        _unavailable('fontlab.YPanelWidget.insertActions')

    def installEventFilter(self, filterObj: Any) -> Any:
        'X.installEventFilter(filterObj)'
        _unavailable('fontlab.YPanelWidget.installEventFilter')

    def isAncestorOf(self, child: Any) -> bool:
        'X.isAncestorOf(child) -> bool'
        _unavailable('fontlab.YPanelWidget.isAncestorOf')

    def isEnabled(self) -> bool:
        'X.isEnabled() -> bool'
        _unavailable('fontlab.YPanelWidget.isEnabled')

    def isEnabledTo(self, arg__1: Any) -> bool:
        'X.isEnabledTo(arg__1) -> bool'
        _unavailable('fontlab.YPanelWidget.isEnabledTo')

    def isFullScreen(self) -> bool:
        'X.isFullScreen() -> bool'
        _unavailable('fontlab.YPanelWidget.isFullScreen')

    def isHidden(self) -> bool:
        'X.isHidden() -> bool'
        _unavailable('fontlab.YPanelWidget.isHidden')

    def isLeftToRight(self) -> bool:
        'X.isLeftToRight() -> bool'
        _unavailable('fontlab.YPanelWidget.isLeftToRight')

    def isMaximized(self) -> bool:
        'X.isMaximized() -> bool'
        _unavailable('fontlab.YPanelWidget.isMaximized')

    def isMinimized(self) -> bool:
        'X.isMinimized() -> bool'
        _unavailable('fontlab.YPanelWidget.isMinimized')

    def isModal(self) -> bool:
        'X.isModal() -> bool'
        _unavailable('fontlab.YPanelWidget.isModal')

    def isRightToLeft(self) -> bool:
        'X.isRightToLeft() -> bool'
        _unavailable('fontlab.YPanelWidget.isRightToLeft')

    def isSignalConnected(self, signal: Any) -> bool:
        'X.isSignalConnected(signal) -> bool'
        _unavailable('fontlab.YPanelWidget.isSignalConnected')

    def isVisible(self) -> bool:
        'X.isVisible() -> bool'
        _unavailable('fontlab.YPanelWidget.isVisible')

    def isVisibleTo(self, arg__1: Any) -> bool:
        'X.isVisibleTo(arg__1) -> bool'
        _unavailable('fontlab.YPanelWidget.isVisibleTo')

    def isWidgetType(self) -> bool:
        'X.isWidgetType() -> bool'
        _unavailable('fontlab.YPanelWidget.isWidgetType')

    def isWindow(self) -> bool:
        'X.isWindow() -> bool'
        _unavailable('fontlab.YPanelWidget.isWindow')

    def isWindowModified(self) -> bool:
        'X.isWindowModified() -> bool'
        _unavailable('fontlab.YPanelWidget.isWindowModified')

    def isWindowType(self) -> bool:
        'X.isWindowType() -> bool'
        _unavailable('fontlab.YPanelWidget.isWindowType')

    def keyPressEvent(self, event: Any) -> Any:
        'X.keyPressEvent(event)'
        _unavailable('fontlab.YPanelWidget.keyPressEvent')

    def keyReleaseEvent(self, event: Any) -> Any:
        'X.keyReleaseEvent(event)'
        _unavailable('fontlab.YPanelWidget.keyReleaseEvent')

    def keyboardGrabber(self) -> Any:
        'X.keyboardGrabber() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.keyboardGrabber')

    def killTimer(self, id: Any) -> Any:
        'X.killTimer(id)'
        _unavailable('fontlab.YPanelWidget.killTimer')

    def layout(self) -> Any:
        'X.layout() -> PythonQt.QtGui.QLayout'
        _unavailable('fontlab.YPanelWidget.layout')

    def leaveEvent(self, event: Any) -> Any:
        'X.leaveEvent(event)'
        _unavailable('fontlab.YPanelWidget.leaveEvent')

    def logicalDpiX(self) -> int:
        'X.logicalDpiX() -> int'
        _unavailable('fontlab.YPanelWidget.logicalDpiX')

    def logicalDpiY(self) -> int:
        'X.logicalDpiY() -> int'
        _unavailable('fontlab.YPanelWidget.logicalDpiY')

    def lower(self) -> Any:
        'X.lower()'
        _unavailable('fontlab.YPanelWidget.lower')

    def mapFrom(self, arg__1: Any, arg__2: Any) -> Any:
        'X.mapFrom(arg__1, arg__2) -> PythonQt.QtCore.QPoint'
        _unavailable('fontlab.YPanelWidget.mapFrom')

    def mapFromGlobal(self, arg__1: Any) -> Any:
        'X.mapFromGlobal(arg__1) -> PythonQt.QtCore.QPoint'
        _unavailable('fontlab.YPanelWidget.mapFromGlobal')

    def mapFromParent(self, arg__1: Any) -> Any:
        'X.mapFromParent(arg__1) -> PythonQt.QtCore.QPoint'
        _unavailable('fontlab.YPanelWidget.mapFromParent')

    def mapTo(self, arg__1: Any, arg__2: Any) -> Any:
        'X.mapTo(arg__1, arg__2) -> PythonQt.QtCore.QPoint'
        _unavailable('fontlab.YPanelWidget.mapTo')

    def mapToGlobal(self, arg__1: Any) -> Any:
        'X.mapToGlobal(arg__1) -> PythonQt.QtCore.QPoint'
        _unavailable('fontlab.YPanelWidget.mapToGlobal')

    def mapToParent(self, arg__1: Any) -> Any:
        'X.mapToParent(arg__1) -> PythonQt.QtCore.QPoint'
        _unavailable('fontlab.YPanelWidget.mapToParent')

    def mask(self) -> Any:
        'X.mask() -> PythonQt.QtGui.QRegion'
        _unavailable('fontlab.YPanelWidget.mask')

    def metaObject(self) -> Any:
        'X.metaObject() -> PythonQt.QtCore.QMetaObject'
        _unavailable('fontlab.YPanelWidget.metaObject')

    def metric(self, arg__1: Any) -> int:
        'X.metric(arg__1) -> int'
        _unavailable('fontlab.YPanelWidget.metric')

    def mouseDoubleClickEvent(self, event: Any) -> Any:
        'X.mouseDoubleClickEvent(event)'
        _unavailable('fontlab.YPanelWidget.mouseDoubleClickEvent')

    def mouseGrabber(self) -> Any:
        'X.mouseGrabber() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.mouseGrabber')

    def mouseMoveEvent(self, event: Any) -> Any:
        'X.mouseMoveEvent(event)'
        _unavailable('fontlab.YPanelWidget.mouseMoveEvent')

    def mousePressEvent(self, event: Any) -> Any:
        'X.mousePressEvent(event)'
        _unavailable('fontlab.YPanelWidget.mousePressEvent')

    def mouseReleaseEvent(self, event: Any) -> Any:
        'X.mouseReleaseEvent(event)'
        _unavailable('fontlab.YPanelWidget.mouseReleaseEvent')

    def move(self, x: Any, y: Any) -> Any:
        'X.move(x, y)'
        _unavailable('fontlab.YPanelWidget.move')

    def moveEvent(self, event: Any) -> Any:
        'X.moveEvent(event)'
        _unavailable('fontlab.YPanelWidget.moveEvent')

    def moveToThread(self, thread: Any) -> Any:
        'X.moveToThread(thread)'
        _unavailable('fontlab.YPanelWidget.moveToThread')

    def nativeEvent(self, eventType: Any, message: Any, result: Any) -> bool:
        'X.nativeEvent(eventType, message, result) -> bool'
        _unavailable('fontlab.YPanelWidget.nativeEvent')

    def nativeParentWidget(self) -> Any:
        'X.nativeParentWidget() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.nativeParentWidget')

    def nextInFocusChain(self) -> Any:
        'X.nextInFocusChain() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.nextInFocusChain')

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelWidget.objectNameChanged; argument details are not documented.'
        _unavailable('fontlab.YPanelWidget.objectNameChanged')

    def overrideWindowFlags(self, type: Any) -> Any:
        'X.overrideWindowFlags(type)'
        _unavailable('fontlab.YPanelWidget.overrideWindowFlags')

    def overrideWindowState(self, state: Any) -> Any:
        'X.overrideWindowState(state)'
        _unavailable('fontlab.YPanelWidget.overrideWindowState')

    def paintEngine(self) -> Any:
        'X.paintEngine() -> PythonQt.QtGui.QPaintEngine'
        _unavailable('fontlab.YPanelWidget.paintEngine')

    def paintEvent(self, event: Any) -> Any:
        'X.paintEvent(event)'
        _unavailable('fontlab.YPanelWidget.paintEvent')

    def paintingActive(self) -> bool:
        'X.paintingActive() -> bool'
        _unavailable('fontlab.YPanelWidget.paintingActive')

    def parent(self) -> Any:
        'X.parent() -> PythonQt.private.QObject'
        _unavailable('fontlab.YPanelWidget.parent')

    def parentWidget(self) -> Any:
        'X.parentWidget() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.parentWidget')

    def physicalDpiX(self) -> int:
        'X.physicalDpiX() -> int'
        _unavailable('fontlab.YPanelWidget.physicalDpiX')

    def physicalDpiY(self) -> int:
        'X.physicalDpiY() -> int'
        _unavailable('fontlab.YPanelWidget.physicalDpiY')

    def previousInFocusChain(self) -> Any:
        'X.previousInFocusChain() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.previousInFocusChain')

    def property(self, name: Any) -> Any:
        'X.property(name) -> object'
        _unavailable('fontlab.YPanelWidget.property')

    def raise_(self) -> Any:
        'X.raise()\n\nNative spelling: raise; access it through getattr on the native object.'
        _unavailable('fontlab.YPanelWidget.raise')

    def redirected(self, offset: Any) -> Any:
        'X.redirected(offset) -> PythonQt.QtGui.QPaintDevice'
        _unavailable('fontlab.YPanelWidget.redirected')

    def releaseKeyboard(self) -> Any:
        'X.releaseKeyboard()'
        _unavailable('fontlab.YPanelWidget.releaseKeyboard')

    def releaseMouse(self) -> Any:
        'X.releaseMouse()'
        _unavailable('fontlab.YPanelWidget.releaseMouse')

    def releaseShortcut(self, id: Any) -> Any:
        'X.releaseShortcut(id)'
        _unavailable('fontlab.YPanelWidget.releaseShortcut')

    def removeAction(self, action: Any) -> Any:
        'X.removeAction(action)'
        _unavailable('fontlab.YPanelWidget.removeAction')

    def removeEventFilter(self, obj: Any) -> Any:
        'X.removeEventFilter(obj)'
        _unavailable('fontlab.YPanelWidget.removeEventFilter')

    def render(self, target: Any, targetOffset: Any, sourceRegion: Any, renderFlags: Any) -> Any:
        'X.render(target, targetOffset, sourceRegion, renderFlags)'
        _unavailable('fontlab.YPanelWidget.render')

    def repaint(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        'X.repaint(x, y, w, h)'
        _unavailable('fontlab.YPanelWidget.repaint')

    def resize(self, w: Any, h: Any) -> Any:
        'X.resize(w, h)'
        _unavailable('fontlab.YPanelWidget.resize')

    def resizeEvent(self, event: Any) -> Any:
        'X.resizeEvent(event)'
        _unavailable('fontlab.YPanelWidget.resizeEvent')

    def restoreGeometry(self, geometry: Any) -> bool:
        'X.restoreGeometry(geometry) -> bool'
        _unavailable('fontlab.YPanelWidget.restoreGeometry')

    def saveGeometry(self) -> Any:
        'X.saveGeometry() -> PythonQt.QtCore.QByteArray'
        _unavailable('fontlab.YPanelWidget.saveGeometry')

    def scroll(self, dx: Any, dy: Any, arg__3: Any) -> Any:
        'X.scroll(dx, dy, arg__3)'
        _unavailable('fontlab.YPanelWidget.scroll')

    def sender(self) -> Any:
        'X.sender() -> PythonQt.private.QObject'
        _unavailable('fontlab.YPanelWidget.sender')

    def senderSignalIndex(self) -> int:
        'X.senderSignalIndex() -> int'
        _unavailable('fontlab.YPanelWidget.senderSignalIndex')

    def setAcceptDrops(self, on: Any) -> Any:
        'X.setAcceptDrops(on)'
        _unavailable('fontlab.YPanelWidget.setAcceptDrops')

    def setAccessibleDescription(self, description: Any) -> Any:
        'X.setAccessibleDescription(description)'
        _unavailable('fontlab.YPanelWidget.setAccessibleDescription')

    def setAccessibleName(self, name: Any) -> Any:
        'X.setAccessibleName(name)'
        _unavailable('fontlab.YPanelWidget.setAccessibleName')

    def setAttribute(self, arg__1: Any, on: Any) -> Any:
        'X.setAttribute(arg__1, on)'
        _unavailable('fontlab.YPanelWidget.setAttribute')

    def setAutoFillBackground(self, enabled: Any) -> Any:
        'X.setAutoFillBackground(enabled)'
        _unavailable('fontlab.YPanelWidget.setAutoFillBackground')

    def setBackgroundRole(self, arg__1: Any) -> Any:
        'X.setBackgroundRole(arg__1)'
        _unavailable('fontlab.YPanelWidget.setBackgroundRole')

    def setBaseSize(self, basew: Any, baseh: Any) -> Any:
        'X.setBaseSize(basew, baseh)'
        _unavailable('fontlab.YPanelWidget.setBaseSize')

    def setContentsMargins(self, left: Any, top: Any, right: Any, bottom: Any) -> Any:
        'X.setContentsMargins(left, top, right, bottom)'
        _unavailable('fontlab.YPanelWidget.setContentsMargins')

    def setContextMenuPolicy(self, policy: Any) -> Any:
        'X.setContextMenuPolicy(policy)'
        _unavailable('fontlab.YPanelWidget.setContextMenuPolicy')

    def setCursor(self, arg__1: Any) -> Any:
        'X.setCursor(arg__1)'
        _unavailable('fontlab.YPanelWidget.setCursor')

    def setDisabled(self, a: Any) -> Any:
        'X.setDisabled(a)'
        _unavailable('fontlab.YPanelWidget.setDisabled')

    def setEnabled(self, a: Any) -> Any:
        'X.setEnabled(a)'
        _unavailable('fontlab.YPanelWidget.setEnabled')

    def setFixedHeight(self, h: Any) -> Any:
        'X.setFixedHeight(h)'
        _unavailable('fontlab.YPanelWidget.setFixedHeight')

    def setFixedSize(self, w: Any, h: Any) -> Any:
        'X.setFixedSize(w, h)'
        _unavailable('fontlab.YPanelWidget.setFixedSize')

    def setFixedWidth(self, w: Any) -> Any:
        'X.setFixedWidth(w)'
        _unavailable('fontlab.YPanelWidget.setFixedWidth')

    def setFocus(self, reason: Any) -> Any:
        'X.setFocus(reason)'
        _unavailable('fontlab.YPanelWidget.setFocus')

    def setFocusPolicy(self, policy: Any) -> Any:
        'X.setFocusPolicy(policy)'
        _unavailable('fontlab.YPanelWidget.setFocusPolicy')

    def setFocusProxy(self, arg__1: Any) -> Any:
        'X.setFocusProxy(arg__1)'
        _unavailable('fontlab.YPanelWidget.setFocusProxy')

    def setFont(self, arg__1: Any) -> Any:
        'X.setFont(arg__1)'
        _unavailable('fontlab.YPanelWidget.setFont')

    def setForegroundRole(self, arg__1: Any) -> Any:
        'X.setForegroundRole(arg__1)'
        _unavailable('fontlab.YPanelWidget.setForegroundRole')

    def setGeometry(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        'X.setGeometry(x, y, w, h)'
        _unavailable('fontlab.YPanelWidget.setGeometry')

    def setGraphicsEffect(self, effect: Any) -> Any:
        'X.setGraphicsEffect(effect)'
        _unavailable('fontlab.YPanelWidget.setGraphicsEffect')

    def setHidden(self, hidden: Any) -> Any:
        'X.setHidden(hidden)'
        _unavailable('fontlab.YPanelWidget.setHidden')

    def setInputMethodHints(self, hints: Any) -> Any:
        'X.setInputMethodHints(hints)'
        _unavailable('fontlab.YPanelWidget.setInputMethodHints')

    def setLayout(self, arg__1: Any) -> Any:
        'X.setLayout(arg__1)'
        _unavailable('fontlab.YPanelWidget.setLayout')

    def setLayoutDirection(self, direction: Any) -> Any:
        'X.setLayoutDirection(direction)'
        _unavailable('fontlab.YPanelWidget.setLayoutDirection')

    def setLocale(self, locale: Any) -> Any:
        'X.setLocale(locale)'
        _unavailable('fontlab.YPanelWidget.setLocale')

    def setMask(self, arg__1: Any) -> Any:
        'X.setMask(arg__1)'
        _unavailable('fontlab.YPanelWidget.setMask')

    def setMaximumHeight(self, maxh: Any) -> Any:
        'X.setMaximumHeight(maxh)'
        _unavailable('fontlab.YPanelWidget.setMaximumHeight')

    def setMaximumSize(self, maxw: Any, maxh: Any) -> Any:
        'X.setMaximumSize(maxw, maxh)'
        _unavailable('fontlab.YPanelWidget.setMaximumSize')

    def setMaximumWidth(self, maxw: Any) -> Any:
        'X.setMaximumWidth(maxw)'
        _unavailable('fontlab.YPanelWidget.setMaximumWidth')

    def setMinimumHeight(self, minh: Any) -> Any:
        'X.setMinimumHeight(minh)'
        _unavailable('fontlab.YPanelWidget.setMinimumHeight')

    def setMinimumSize(self, minw: Any, minh: Any) -> Any:
        'X.setMinimumSize(minw, minh)'
        _unavailable('fontlab.YPanelWidget.setMinimumSize')

    def setMinimumWidth(self, minw: Any) -> Any:
        'X.setMinimumWidth(minw)'
        _unavailable('fontlab.YPanelWidget.setMinimumWidth')

    def setMouseTracking(self, enable: Any) -> Any:
        'X.setMouseTracking(enable)'
        _unavailable('fontlab.YPanelWidget.setMouseTracking')

    def setObjectName(self, name: Any) -> Any:
        'X.setObjectName(name)'
        _unavailable('fontlab.YPanelWidget.setObjectName')

    def setPalette(self, arg__1: Any) -> Any:
        'X.setPalette(arg__1)'
        _unavailable('fontlab.YPanelWidget.setPalette')

    def setParent(self, parent: Any, f: Any) -> Any:
        'X.setParent(parent, f)'
        _unavailable('fontlab.YPanelWidget.setParent')

    def setProperty(self, name: Any, value: Any) -> bool:
        'X.setProperty(name, value) -> bool'
        _unavailable('fontlab.YPanelWidget.setProperty')

    def setShortcutAutoRepeat(self, id: Any, enable: Any) -> Any:
        'X.setShortcutAutoRepeat(id, enable)'
        _unavailable('fontlab.YPanelWidget.setShortcutAutoRepeat')

    def setShortcutEnabled(self, id: Any, enable: Any) -> Any:
        'X.setShortcutEnabled(id, enable)'
        _unavailable('fontlab.YPanelWidget.setShortcutEnabled')

    def setSizeIncrement(self, w: Any, h: Any) -> Any:
        'X.setSizeIncrement(w, h)'
        _unavailable('fontlab.YPanelWidget.setSizeIncrement')

    def setSizePolicy(self, horizontal: Any, vertical: Any) -> Any:
        'X.setSizePolicy(horizontal, vertical)'
        _unavailable('fontlab.YPanelWidget.setSizePolicy')

    def setStatusTip(self, arg__1: Any) -> Any:
        'X.setStatusTip(arg__1)'
        _unavailable('fontlab.YPanelWidget.setStatusTip')

    def setStyle(self, arg__1: Any) -> Any:
        'X.setStyle(arg__1)'
        _unavailable('fontlab.YPanelWidget.setStyle')

    def setStyleSheet(self, styleSheet: Any) -> Any:
        'X.setStyleSheet(styleSheet)'
        _unavailable('fontlab.YPanelWidget.setStyleSheet')

    def setTabOrder(self, arg__1: Any, arg__2: Any) -> Any:
        'X.setTabOrder(arg__1, arg__2)'
        _unavailable('fontlab.YPanelWidget.setTabOrder')

    def setToolTip(self, arg__1: Any) -> Any:
        'X.setToolTip(arg__1)'
        _unavailable('fontlab.YPanelWidget.setToolTip')

    def setToolTipDuration(self, msec: Any) -> Any:
        'X.setToolTipDuration(msec)'
        _unavailable('fontlab.YPanelWidget.setToolTipDuration')

    def setUpdatesEnabled(self, enable: Any) -> Any:
        'X.setUpdatesEnabled(enable)'
        _unavailable('fontlab.YPanelWidget.setUpdatesEnabled')

    def setVisible(self, visible: Any) -> Any:
        'X.setVisible(visible)'
        _unavailable('fontlab.YPanelWidget.setVisible')

    def setWhatsThis(self, arg__1: Any) -> Any:
        'X.setWhatsThis(arg__1)'
        _unavailable('fontlab.YPanelWidget.setWhatsThis')

    def setWindowFilePath(self, filePath: Any) -> Any:
        'X.setWindowFilePath(filePath)'
        _unavailable('fontlab.YPanelWidget.setWindowFilePath')

    def setWindowFlags(self, type: Any) -> Any:
        'X.setWindowFlags(type)'
        _unavailable('fontlab.YPanelWidget.setWindowFlags')

    def setWindowIcon(self, icon: Any) -> Any:
        'X.setWindowIcon(icon)'
        _unavailable('fontlab.YPanelWidget.setWindowIcon')

    def setWindowIconText(self, arg__1: Any) -> Any:
        'X.setWindowIconText(arg__1)'
        _unavailable('fontlab.YPanelWidget.setWindowIconText')

    def setWindowModality(self, windowModality: Any) -> Any:
        'X.setWindowModality(windowModality)'
        _unavailable('fontlab.YPanelWidget.setWindowModality')

    def setWindowModified(self, a: Any) -> Any:
        'X.setWindowModified(a)'
        _unavailable('fontlab.YPanelWidget.setWindowModified')

    def setWindowOpacity(self, level: Any) -> Any:
        'X.setWindowOpacity(level)'
        _unavailable('fontlab.YPanelWidget.setWindowOpacity')

    def setWindowRole(self, arg__1: Any) -> Any:
        'X.setWindowRole(arg__1)'
        _unavailable('fontlab.YPanelWidget.setWindowRole')

    def setWindowState(self, state: Any) -> Any:
        'X.setWindowState(state)'
        _unavailable('fontlab.YPanelWidget.setWindowState')

    def setWindowTitle(self, a: Any) -> Any:
        'X.setWindowTitle(a)'
        _unavailable('fontlab.YPanelWidget.setWindowTitle')

    def sharedPainter(self) -> Any:
        'X.sharedPainter() -> PythonQt.QtGui.QPainter'
        _unavailable('fontlab.YPanelWidget.sharedPainter')

    def show(self) -> Any:
        'X.show()'
        _unavailable('fontlab.YPanelWidget.show')

    def showEvent(self, event: Any) -> Any:
        'X.showEvent(event)'
        _unavailable('fontlab.YPanelWidget.showEvent')

    def showFullScreen(self) -> Any:
        'X.showFullScreen()'
        _unavailable('fontlab.YPanelWidget.showFullScreen')

    def showMaximized(self) -> Any:
        'X.showMaximized()'
        _unavailable('fontlab.YPanelWidget.showMaximized')

    def showMinimized(self) -> Any:
        'X.showMinimized()'
        _unavailable('fontlab.YPanelWidget.showMinimized')

    def showNormal(self) -> Any:
        'X.showNormal()'
        _unavailable('fontlab.YPanelWidget.showNormal')

    def signalsBlocked(self) -> bool:
        'X.signalsBlocked() -> bool'
        _unavailable('fontlab.YPanelWidget.signalsBlocked')

    def stackUnder(self, arg__1: Any) -> Any:
        'X.stackUnder(arg__1)'
        _unavailable('fontlab.YPanelWidget.stackUnder')

    def startTimer(self, interval: Any, timerType: Any) -> int:
        'X.startTimer(interval, timerType) -> int'
        _unavailable('fontlab.YPanelWidget.startTimer')

    def style(self) -> Any:
        'X.style() -> PythonQt.QtGui.QStyle'
        _unavailable('fontlab.YPanelWidget.style')

    def tabletEvent(self, event: Any) -> Any:
        'X.tabletEvent(event)'
        _unavailable('fontlab.YPanelWidget.tabletEvent')

    def testAttribute(self, arg__1: Any) -> bool:
        'X.testAttribute(arg__1) -> bool'
        _unavailable('fontlab.YPanelWidget.testAttribute')

    def thread(self) -> Any:
        'X.thread()'
        _unavailable('fontlab.YPanelWidget.thread')

    def timerEvent(self, event: Any) -> Any:
        'X.timerEvent(event)'
        _unavailable('fontlab.YPanelWidget.timerEvent')

    def tr(self, text: Any, ambig: Any, n: Any) -> str:
        'X.tr(text, ambig, n) -> str'
        _unavailable('fontlab.YPanelWidget.tr')

    def underMouse(self) -> bool:
        'X.underMouse() -> bool'
        _unavailable('fontlab.YPanelWidget.underMouse')

    def ungrabGesture(self, type: Any) -> Any:
        'X.ungrabGesture(type)'
        _unavailable('fontlab.YPanelWidget.ungrabGesture')

    def unsetCursor(self) -> Any:
        'X.unsetCursor()'
        _unavailable('fontlab.YPanelWidget.unsetCursor')

    def unsetLayoutDirection(self) -> Any:
        'X.unsetLayoutDirection()'
        _unavailable('fontlab.YPanelWidget.unsetLayoutDirection')

    def unsetLocale(self) -> Any:
        'X.unsetLocale()'
        _unavailable('fontlab.YPanelWidget.unsetLocale')

    def update(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        'X.update(x, y, w, h)'
        _unavailable('fontlab.YPanelWidget.update')

    def updateGeometry(self) -> Any:
        'X.updateGeometry()'
        _unavailable('fontlab.YPanelWidget.updateGeometry')

    def visibleRegion(self) -> Any:
        'X.visibleRegion() -> PythonQt.QtGui.QRegion'
        _unavailable('fontlab.YPanelWidget.visibleRegion')

    def wheelEvent(self, event: Any) -> Any:
        'X.wheelEvent(event)'
        _unavailable('fontlab.YPanelWidget.wheelEvent')

    def widthMM(self) -> int:
        'X.widthMM() -> int'
        _unavailable('fontlab.YPanelWidget.widthMM')

    def winId(self) -> int:
        'X.winId() -> int'
        _unavailable('fontlab.YPanelWidget.winId')

    def window(self) -> Any:
        'X.window() -> PythonQt.QtGui.QWidget'
        _unavailable('fontlab.YPanelWidget.window')

    def windowFlags(self) -> Any:
        'X.windowFlags()'
        _unavailable('fontlab.YPanelWidget.windowFlags')

    def windowHandle(self) -> Any:
        'X.windowHandle() -> PythonQt.QtGui.QWindow'
        _unavailable('fontlab.YPanelWidget.windowHandle')

    def windowIconChanged(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelWidget.windowIconChanged; argument details are not documented.'
        _unavailable('fontlab.YPanelWidget.windowIconChanged')

    def windowIconTextChanged(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelWidget.windowIconTextChanged; argument details are not documented.'
        _unavailable('fontlab.YPanelWidget.windowIconTextChanged')

    def windowRole(self) -> str:
        'X.windowRole() -> str'
        _unavailable('fontlab.YPanelWidget.windowRole')

    def windowState(self) -> Any:
        'X.windowState()'
        _unavailable('fontlab.YPanelWidget.windowState')

    def windowTitleChanged(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.YPanelWidget.windowTitleChanged; argument details are not documented.'
        _unavailable('fontlab.YPanelWidget.windowTitleChanged')

    def windowType(self) -> Any:
        'X.windowType()'
        _unavailable('fontlab.YPanelWidget.windowType')

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
    "fgSymbol representation\n\nConstructors:\n  fgSymbol() - default\n  fgSymbol(fgSymbol) - copy\n  fgSymbol(unicode)\n  fgSymbol('name')\n  fgSymbol(id, fgFont)\n  fgSymbol(glyph_id, package_id)\n  fgSymbol(unicode, 'name', id)\n\nNative bases: object"
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.fgSymbol')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontlab.fgSymbol.clear')

    def clearData(self, DataCode: Any) -> Any:
        'clearData(DataCode)'
        _unavailable('fontlab.fgSymbol.clearData')

    def clearID(self) -> Any:
        'clearID()'
        _unavailable('fontlab.fgSymbol.clearID')

    def compare(self, arg0: fgSymbol) -> bool:
        'bool compare(fgSymbol)'
        _unavailable('fontlab.fgSymbol.compare')

    def computeID(self, arg0: fgFont) -> bool:
        'bool computeID(fgFont)'
        _unavailable('fontlab.fgSymbol.computeID')

    def containsData(self, DataCode: Any) -> bool:
        'bool containsData(DataCode)'
        _unavailable('fontlab.fgSymbol.containsData')

    def data(self, DataCode: Any) -> Any:
        'QVariant data(DataCode)'
        _unavailable('fontlab.fgSymbol.data')

    def glyph(self, arg0: fgFont, setId: bool) -> fgGlyph:
        'fgGlyph glyph(fgFont, bool setId)'
        _unavailable('fontlab.fgSymbol.glyph')

    def init(self) -> Any:
        'init()'
        _unavailable('fontlab.fgSymbol.init')

    def setData(self, DataCode: Any, d: Any) -> Any:
        'setData(DataCode, QVariant d)'
        _unavailable('fontlab.fgSymbol.setData')

    def setSterile(self) -> Any:
        'setSterile()'
        _unavailable('fontlab.fgSymbol.setSterile')

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
    'fgSymbolList representation\n\nConstructors:\n  fgSymbolList() - default\n  fgSymbolList(fgSymbolList) - copy\n  fgSymbolList(list(fgSymbol))\n  fgSymbolList(string[, bool advancedProcessing = false])\n  fgSymbolList(fgSymbolList, int len)\n  fgSymbolList(fgFont, fgGlyphIDsSet)\n  fgSymbolList(fgFont, list(glyph_id))\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.fgSymbolList')

    def append(self, fgSymbolList: Any) -> Any:
        'append(fgSymbol | fgSymbolList)'
        _unavailable('fontlab.fgSymbolList.append')

    def assign(self, *args: Any, **kwargs: Any) -> Any:
        'assign(fgFont, list(glyphsId))'
        _unavailable('fontlab.fgSymbolList.assign')

    def at(self, index: Any) -> fgSymbol:
        'fgSymbol at(index)'
        _unavailable('fontlab.fgSymbolList.at')

    def clear(self) -> Any:
        'clear()'
        _unavailable('fontlab.fgSymbolList.clear')

    def clearData(self, dataCode: int) -> Any:
        'clearData(int dataCode)'
        _unavailable('fontlab.fgSymbolList.clearData')

    def clearString(self) -> Any:
        'clearString()'
        _unavailable('fontlab.fgSymbolList.clearString')

    def compare(self, arg0: fgSymbolList) -> bool:
        'bool compare(fgSymbolList)'
        _unavailable('fontlab.fgSymbolList.compare')

    def computeString(self, advancedProcessing: bool) -> Any:
        'computeString(bool advancedProcessing)'
        _unavailable('fontlab.fgSymbolList.computeString')

    def data(self, index: int, v: Any = ...) -> Any:
        'QVariant data(int index, int dataCode[, QVariant v = QVariant()])'
        _unavailable('fontlab.fgSymbolList.data')

    def empty(self) -> bool:
        'bool empty()'
        _unavailable('fontlab.fgSymbolList.empty')

    def equals(self, arg0: fgSymbolList) -> bool:
        'bool equals(fgSymbolList)'
        _unavailable('fontlab.fgSymbolList.equals')

    def insert(self, index: Any, arg1: fgSymbol) -> Any:
        'insert(index, fgSymbol)'
        _unavailable('fontlab.fgSymbolList.insert')

    def last(self) -> fgSymbol:
        'fgSymbol last()'
        _unavailable('fontlab.fgSymbolList.last')

    def limitLineLength(self, len: int) -> bool:
        'bool limitLineLength(int len)'
        _unavailable('fontlab.fgSymbolList.limitLineLength')

    def mid(self, count: Any = ...) -> fgSymbolList:
        'fgSymbolList mid(int index[, int count=-1])'
        _unavailable('fontlab.fgSymbolList.mid')

    def remove(self, index: Any, count: Any) -> Any:
        'remove(index, count)'
        _unavailable('fontlab.fgSymbolList.remove')

    def replace(self, index: Any, count: Any, arg2: fgSymbolList) -> Any:
        'replace(index,  count, fgSymbolList)'
        _unavailable('fontlab.fgSymbolList.replace')

    def reserve(self, count: int) -> Any:
        'reserve(int count)'
        _unavailable('fontlab.fgSymbolList.reserve')

    def restore(self, *args: Any, **kwargs: Any) -> Any:
        'bool restore(QByteArray, list(fgFont))'
        _unavailable('fontlab.fgSymbolList.restore')

    def set(self, index: Any, arg1: fgSymbol) -> Any:
        'set(index, fgSymbol)'
        _unavailable('fontlab.fgSymbolList.set')

    def setData(self, index: Any, DataCode: Any, arg2: Any) -> Any:
        'setData(index,  DataCode, QVariant)'
        _unavailable('fontlab.fgSymbolList.setData')

    def setGlyphsList(self, *args: Any, **kwargs: Any) -> Any:
        'setGlyphsList(list(fgGlyph), fgFont)'
        _unavailable('fontlab.fgSymbolList.setGlyphsList')

    def setIdList(self, *args: Any, **kwargs: Any) -> Any:
        'setIdList(list(id), fgFont)'
        _unavailable('fontlab.fgSymbolList.setIdList')

    def setList(self, list: fgSymbols) -> Any:
        'setList(fgSymbols list)'
        _unavailable('fontlab.fgSymbolList.setList')

    def setNamesList(self, QStringList: Any) -> Any:
        'setNamesList(string | QStringList)'
        _unavailable('fontlab.fgSymbolList.setNamesList')

    def setSterile(self) -> Any:
        'setSterile()'
        _unavailable('fontlab.fgSymbolList.setSterile')

    def setString(self, advancedProcessing: Any = ...) -> Any:
        'setString(string[, bool advancedProcessing = true])'
        _unavailable('fontlab.fgSymbolList.setString')

    def setUnicodeList(self, *args: Any, **kwargs: Any) -> Any:
        'setUnicodeList( list(unicodes) )'
        _unavailable('fontlab.fgSymbolList.setUnicodeList')

    def size(self) -> int:
        'int size()'
        _unavailable('fontlab.fgSymbolList.size')

    def store(self, packageID: Any) -> bytes:
        'QByteArray store(packageID)'
        _unavailable('fontlab.fgSymbolList.store')

    def string(self, advancedProcessing: bool) -> str:
        'QString string(bool advancedProcessing)'
        _unavailable('fontlab.fgSymbolList.string')

    def symbols(self) -> Any:
        'list(fgSymbol) symbols()'
        _unavailable('fontlab.fgSymbolList.symbols')


class flAbstractEditor:
    'flAbstractEditor representation\n\nConstructors:\n  flAbstractEditor()\n  flAbstractEditor(flObject)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flAbstractEditor')

    def activate(self) -> Any:
        'activate()'
        _unavailable('fontlab.flAbstractEditor.activate')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flAbstractEditor.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flAbstractEditor.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flAbstractEditor.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flAbstractEditor.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flAbstractEditor.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flAbstractEditor.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flAbstractEditor.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flAbstractEditor.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flAbstractEditor.currentHistoryState')

    def deactivate(self) -> Any:
        'deactivate()'
        _unavailable('fontlab.flAbstractEditor.deactivate')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flAbstractEditor.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flAbstractEditor.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flAbstractEditor.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flAbstractEditor.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flAbstractEditor.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flAbstractEditor.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flAbstractEditor.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flAbstractEditor.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flAbstractEditor.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flAbstractEditor.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flAbstractEditor.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flAbstractEditor.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flAbstractEditor.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flAbstractEditor.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flAbstractEditor.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flAbstractEditor.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flAbstractEditor.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flAbstractEditor.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flAbstractEditor.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flAbstractEditor.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flAbstractEditor.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flAbstractEditor.update')

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
    'flAbstractVectorNode representation\n\nConstructors:\n  flAbstractVectorNode(flAbstractVectorNode)\n  flAbstractVectorNode(flObject)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flAbstractVectorNode')

    def angleTo(self, p: QPointF) -> float:
        'double angleTo(QPointF p)'
        _unavailable('fontlab.flAbstractVectorNode.angleTo')

    def applyTransform(self, arg0: QTransform) -> Any:
        'applyTransform(QTransform)'
        _unavailable('fontlab.flAbstractVectorNode.applyTransform')

    def canBeHobby(self) -> bool:
        'bool canBeHobby()'
        _unavailable('fontlab.flAbstractVectorNode.canBeHobby')

    def canBeSmooth(self) -> bool:
        'bool canBeSmooth()'
        _unavailable('fontlab.flAbstractVectorNode.canBeSmooth')

    def canCollapse(self) -> bool:
        'bool canCollapse()'
        _unavailable('fontlab.flAbstractVectorNode.canCollapse')

    def canImprove(self) -> bool:
        'bool canImprove()'
        _unavailable('fontlab.flAbstractVectorNode.canImprove')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flAbstractVectorNode.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flAbstractVectorNode.checkInitHistoryState')

    def checkVectors(self) -> bool:
        'bool checkVectors()'
        _unavailable('fontlab.flAbstractVectorNode.checkVectors')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flAbstractVectorNode.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flAbstractVectorNode.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flAbstractVectorNode.clearFlags')

    def clearStored(self) -> Any:
        'clearStored()'
        _unavailable('fontlab.flAbstractVectorNode.clearStored')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flAbstractVectorNode.clone')

    def cloneMapped(self, arg0: QTransform) -> flNode:
        'flNode cloneMapped(QTransform)'
        _unavailable('fontlab.flAbstractVectorNode.cloneMapped')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flAbstractVectorNode.cloneObject')

    def collapseHandles(self) -> bool:
        'bool collapseHandles()'
        _unavailable('fontlab.flAbstractVectorNode.collapseHandles')

    def convertToCurve(self, smooth: Any = ...) -> bool:
        'bool convertToCurve([bool smooth = false])'
        _unavailable('fontlab.flAbstractVectorNode.convertToCurve')

    def convertToCurves(self) -> bool:
        'bool convertToCurves()'
        _unavailable('fontlab.flAbstractVectorNode.convertToCurves')

    def convertToLine(self) -> bool:
        'bool convertToLine()'
        _unavailable('fontlab.flAbstractVectorNode.convertToLine')

    def copyFrom(self, withSelected: Any = ...) -> Any:
        'copyFrom(Node[, withSelected=False])'
        _unavailable('fontlab.flAbstractVectorNode.copyFrom')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flAbstractVectorNode.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flAbstractVectorNode.currentHistoryState')

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        'double distanceTo(Node/QPointF)'
        _unavailable('fontlab.flAbstractVectorNode.distanceTo')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flAbstractVectorNode.flag')

    def getLines(self, *args: Any, **kwargs: Any) -> Any:
        '(QLineF, QLineF)/None getLines()'
        _unavailable('fontlab.flAbstractVectorNode.getLines')

    def getOn(self) -> Any:
        'Node/None getOn()'
        _unavailable('fontlab.flAbstractVectorNode.getOn')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flAbstractVectorNode.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flAbstractVectorNode.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flAbstractVectorNode.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flAbstractVectorNode.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flAbstractVectorNode.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flAbstractVectorNode.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flAbstractVectorNode.historyStates')

    def improve(self) -> bool:
        'bool improve()'
        _unavailable('fontlab.flAbstractVectorNode.improve')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flAbstractVectorNode.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flAbstractVectorNode.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flAbstractVectorNode.instanceType')

    def isCorner(self, a: Any = ...) -> bool:
        'bool isCorner([double a = 10.])'
        _unavailable('fontlab.flAbstractVectorNode.isCorner')

    def isCurve(self) -> bool:
        'bool isCurve()'
        _unavailable('fontlab.flAbstractVectorNode.isCurve')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flAbstractVectorNode.isEqual')

    def isEqualTo(self, tolerance: Any = ...) -> bool:
        'bool isEqualTo(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])'
        _unavailable('fontlab.flAbstractVectorNode.isEqualTo')

    def isExtreme(self, open: Any = ...) -> bool:
        'bool isExtreme(bool x[, bool open = true[, double limit = 0]])'
        _unavailable('fontlab.flAbstractVectorNode.isExtreme')

    def isFirst(self) -> bool:
        'bool isFirst()'
        _unavailable('fontlab.flAbstractVectorNode.isFirst')

    def isG2(self, tolerance: float) -> bool:
        'bool isG2(double tolerance)'
        _unavailable('fontlab.flAbstractVectorNode.isG2')

    def isInternal(self, clockwise: bool) -> bool:
        'bool isInternal(bool clockwise)'
        _unavailable('fontlab.flAbstractVectorNode.isInternal')

    def isInterpolated(self, x: bool) -> bool:
        'bool isInterpolated(bool x)'
        _unavailable('fontlab.flAbstractVectorNode.isInterpolated')

    def isLast(self) -> bool:
        'bool isLast()'
        _unavailable('fontlab.flAbstractVectorNode.isLast')

    def isOff(self) -> bool:
        'bool isOff()'
        _unavailable('fontlab.flAbstractVectorNode.isOff')

    def isOn(self) -> bool:
        'bool isOn()'
        _unavailable('fontlab.flAbstractVectorNode.isOn')

    def isSmartAngle(self) -> bool:
        'bool isSmartAngle()'
        _unavailable('fontlab.flAbstractVectorNode.isSmartAngle')

    def makeStart(self) -> bool:
        'bool makeStart()'
        _unavailable('fontlab.flAbstractVectorNode.makeStart')

    def moveBy(self, *args: Any, **kwargs: Any) -> Any:
        'moveBy(float dx, float dy[, bool round=false]'
        _unavailable('fontlab.flAbstractVectorNode.moveBy')

    def nextNode(self, nodeType: Any = ...) -> Any:
        'Node/None nextNode([string nodeType= [, int searchDepth=1]])'
        _unavailable('fontlab.flAbstractVectorNode.nextNode')

    def pointG2(self) -> Any:
        'QPointF/None pointG2()'
        _unavailable('fontlab.flAbstractVectorNode.pointG2')

    def prevNode(self, nodeType: Any = ...) -> Any:
        'Node/None prevNode([string nodeType= [, int searchDepth=1]])'
        _unavailable('fontlab.flAbstractVectorNode.prevNode')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flAbstractVectorNode.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flAbstractVectorNode.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flAbstractVectorNode.removeChild')

    def restoreCoordinates(self) -> Any:
        'restoreCoordinates()'
        _unavailable('fontlab.flAbstractVectorNode.restoreCoordinates')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flAbstractVectorNode.restoreHistoryState')

    def rotateBy(self, origin: Any = ...) -> Any:
        'rotateBy(valueDegree[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flAbstractVectorNode.rotateBy')

    def round(self) -> Any:
        "round() - Round the node's coordinate"
        _unavailable('fontlab.flAbstractVectorNode.round')

    def scaleBy(self, origin: Any = ...) -> Any:
        'scaleBy(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flAbstractVectorNode.scaleBy')

    def setExtraLast(self, bool: Any) -> Any:
        'setExtraLast(bool)'
        _unavailable('fontlab.flAbstractVectorNode.setExtraLast')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flAbstractVectorNode.setFlag')

    def setNextSmooth(self, base: QPointF) -> Any:
        'setNextSmooth(QPointF base)'
        _unavailable('fontlab.flAbstractVectorNode.setNextSmooth')

    def setPosition(self, arg0: QPointF) -> None:
        'void setPosition(QPointF)'
        _unavailable('fontlab.flAbstractVectorNode.setPosition')

    def setPrevSmooth(self, base: QPointF) -> Any:
        'setPrevSmooth(QPointF base)'
        _unavailable('fontlab.flAbstractVectorNode.setPrevSmooth')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flAbstractVectorNode.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flAbstractVectorNode.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flAbstractVectorNode.setPropertyInt')

    def setSmartAngleEnbl(self, bool: Any) -> bool:
        'bool setSmartAngleEnbl(bool)'
        _unavailable('fontlab.flAbstractVectorNode.setSmartAngleEnbl')

    def setSmartSharp(self, tension: Any = ...) -> bool:
        'bool setSmartSharp([double tension = 0.6])'
        _unavailable('fontlab.flAbstractVectorNode.setSmartSharp')

    def skewBy(self, origin: Any = ...) -> Any:
        'skewBy(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flAbstractVectorNode.skewBy')

    def smartMove(self, offset: Any) -> Any:
        'list(uint) smartMove(offset)'
        _unavailable('fontlab.flAbstractVectorNode.smartMove')

    def smartSetXY(self, arg0: QPointF) -> Any:
        'smartSetXY(QPointF)'
        _unavailable('fontlab.flAbstractVectorNode.smartSetXY')

    def storeCoordinates(self) -> Any:
        'storeCoordinates()'
        _unavailable('fontlab.flAbstractVectorNode.storeCoordinates')

    def storeTestParameters(self) -> Any:
        'storeTestParameters()'
        _unavailable('fontlab.flAbstractVectorNode.storeTestParameters')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flAbstractVectorNode.tag')

    def transformBy(self, origin: Any = ...) -> Any:
        'transformBy(QTransform tx[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flAbstractVectorNode.transformBy')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flAbstractVectorNode.update')

    def updateG2(self) -> bool:
        'bool updateG2()'
        _unavailable('fontlab.flAbstractVectorNode.updateG2')

    def updateSmooth(self, extended_neibh: Any = ...) -> Any:
        'updateSmooth([bool extended_neibh=true])'
        _unavailable('fontlab.flAbstractVectorNode.updateSmooth')

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
    'flAnchor representation\n\nConstructors:\n  flAnchor() - default\n  flAnchor(flAnchor) - copy\n  flAnchor(flObject)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flAnchor')

    def added(self) -> Any:
        'added()'
        _unavailable('fontlab.flAnchor.added')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flAnchor.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flAnchor.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flAnchor.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flAnchor.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flAnchor.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flAnchor.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flAnchor.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flAnchor.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flAnchor.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flAnchor.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flAnchor.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flAnchor.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flAnchor.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flAnchor.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flAnchor.hasHistoryState')

    def hasObject(self, arg0: flObject) -> bool:
        'bool hasObject(flObject)'
        _unavailable('fontlab.flAnchor.hasObject')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flAnchor.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flAnchor.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flAnchor.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flAnchor.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flAnchor.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flAnchor.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flAnchor.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flAnchor.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flAnchor.removeChild')

    def removed(self) -> Any:
        'removed()'
        _unavailable('fontlab.flAnchor.removed')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flAnchor.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flAnchor.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flAnchor.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flAnchor.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flAnchor.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flAnchor.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flAnchor.update')

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
    'flAuditInfo representation\n\nConstructors:\n  flAuditInfo()\n  flAuditInfo(flObject)\n  flAuditInfo(flAuditInfo)\n  flAuditInfo(FaBasic, QTransform)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flAuditInfo')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flAuditInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flAuditInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flAuditInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flAuditInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flAuditInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flAuditInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flAuditInfo.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flAuditInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flAuditInfo.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flAuditInfo.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flAuditInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flAuditInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flAuditInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flAuditInfo.getPropertyInt')

    def glyphLocation(self, *args: Any, **kwargs: Any) -> Any:
        'QPointF glyphLocation([QPointF])'
        _unavailable('fontlab.flAuditInfo.glyphLocation')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flAuditInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flAuditInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flAuditInfo.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flAuditInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flAuditInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flAuditInfo.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flAuditInfo.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flAuditInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flAuditInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flAuditInfo.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flAuditInfo.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flAuditInfo.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flAuditInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flAuditInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flAuditInfo.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flAuditInfo.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flAuditInfo.update')

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
    'flAxis representation\n\nConstructors:\n  flAxis() - default\n  flAxis(string name)\n  flAxis(string name, string tag, string short_name)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flAxis')

    def _has_axis_name(self, *args: Any, **kwargs: Any) -> Any:
        'QString _check_axis_name(QList<flAxis> axes, int exclude, strin gname)'
        _unavailable('fontlab.flAxis._has_axis_name')

    def checkValue(self, v: float) -> float:
        'double checkValue(double v)'
        _unavailable('fontlab.flAxis.checkValue')

    def getRange(self) -> float:
        'double getRange()'
        _unavailable('fontlab.flAxis.getRange')

    def instanceIndex(self, v: float) -> int:
        'int instanceIndex(double v)'
        _unavailable('fontlab.flAxis.instanceIndex')

    def instances2map(self) -> bool:
        'bool instances2map()'
        _unavailable('fontlab.flAxis.instances2map')

    def instances2string(self) -> Any:
        'string instances2string()'
        _unavailable('fontlab.flAxis.instances2string')

    def isWeight(self, s: Any) -> bool:
        'bool isWeight(string s)'
        _unavailable('fontlab.flAxis.isWeight')

    def isWidth(self, s: Any) -> bool:
        'bool isWidth(string s)'
        _unavailable('fontlab.flAxis.isWidth')

    def locationName(self, axes: list[flAxis], location: flLocation) -> str:
        'QString locationName(QList<flAxis> axes, flLocation location)'
        _unavailable('fontlab.flAxis.locationName')

    def map2instances(self) -> bool:
        'bool map2instances()'
        _unavailable('fontlab.flAxis.map2instances')

    def mappedValue(self, v: float) -> float:
        'double mappedValue(double v)'
        _unavailable('fontlab.flAxis.mappedValue')

    def normalize(self, userValue: float) -> float:
        'double normalize(double userValue)'
        _unavailable('fontlab.flAxis.normalize')

    def onEdge(self, v: float) -> bool:
        'bool onEdge(double v)'
        _unavailable('fontlab.flAxis.onEdge')

    def string2instances(self, s: Any) -> bool:
        'bool string2instances(string s)'
        _unavailable('fontlab.flAxis.string2instances')

    def styleName(self, v: float) -> Any:
        'string styleName(double v)'
        _unavailable('fontlab.flAxis.styleName')

    def styleValue(self, style_name: Any) -> float:
        'double styleValue(string style_name)'
        _unavailable('fontlab.flAxis.styleValue')

    def updateInstances(self) -> None:
        'void updateInstances()'
        _unavailable('fontlab.flAxis.updateInstances')

    def updateShortName(self) -> None:
        'void updateShortName()'
        _unavailable('fontlab.flAxis.updateShortName')

    def updateTag(self) -> None:
        'void updateTag()'
        _unavailable('fontlab.flAxis.updateTag')

    def valueWeight(self, location: flLocation, value: float) -> float:
        'double valueWeight(flLocation location, double value)'
        _unavailable('fontlab.flAxis.valueWeight')

    def valueWidth(self, location: flLocation, value: float) -> float:
        'double valueWidth(flLocation location, double value)'
        _unavailable('fontlab.flAxis.valueWidth')

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
    'flBasicTool representation\n\nConstructors:\n  flBasicTool()\n  flBasicTool(flObject)\n  flBasicTool(flBasicTool)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flBasicTool')

    def activateTool(self) -> Any:
        'activateTool()'
        _unavailable('fontlab.flBasicTool.activateTool')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flBasicTool.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flBasicTool.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flBasicTool.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flBasicTool.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flBasicTool.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flBasicTool.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flBasicTool.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flBasicTool.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flBasicTool.currentHistoryState')

    def deactivateTool(self) -> Any:
        'deactivateTool()'
        _unavailable('fontlab.flBasicTool.deactivateTool')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flBasicTool.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flBasicTool.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flBasicTool.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flBasicTool.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flBasicTool.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flBasicTool.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flBasicTool.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flBasicTool.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flBasicTool.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flBasicTool.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flBasicTool.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flBasicTool.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flBasicTool.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flBasicTool.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flBasicTool.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flBasicTool.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flBasicTool.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flBasicTool.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flBasicTool.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flBasicTool.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flBasicTool.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flBasicTool.update')

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
    'flCanvas representation\n\nConstructors:\n  flCanvas()\n  flCanvas(flCanvas)\n  flCanvas(flObject)\n  flCanvas(id)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flCanvas')

    def _finalize_smart_angles(self) -> bool:
        'bool _finalize_smart_angles()'
        _unavailable('fontlab.flCanvas._finalize_smart_angles')

    def acceptEvents(self) -> int:
        'int acceptEvents()'
        _unavailable('fontlab.flCanvas.acceptEvents')

    def activateEditor(self, canvas_pos: QPointF) -> None:
        'void activateEditor(QPointF canvas_pos)'
        _unavailable('fontlab.flCanvas.activateEditor')

    def activatePreviewNodes(self) -> Any:
        'activatePreviewNodes()'
        _unavailable('fontlab.flCanvas.activatePreviewNodes')

    def addTextBlock(self, arg0: flTextBlock) -> Any:
        'addTextBlock(flTextBlock)'
        _unavailable('fontlab.flCanvas.addTextBlock')

    def addedToCanvas(self, arg0: flCanvas) -> None:
        'void addedToCanvas(flCanvas)'
        _unavailable('fontlab.flCanvas.addedToCanvas')

    def addedToWorkspace(self, arg0: flWorkspace) -> Any:
        'addedToWorkspace(flWorkspace)'
        _unavailable('fontlab.flCanvas.addedToWorkspace')

    def adjustCanvasPosition(self, arg0: QPointF) -> QPointF:
        'QPointF adjustCanvasPosition(QPointF)'
        _unavailable('fontlab.flCanvas.adjustCanvasPosition')

    def adjustPosition(self, double: Any) -> Any:
        'QPointF | double adjustPosition(QPointF | double)'
        _unavailable('fontlab.flCanvas.adjustPosition')

    def appendDecorator(self, arg0: flVisualItem, DecoratorOrder: Any) -> None:
        'void appendDecorator(flVisualItem, DecoratorOrder)'
        _unavailable('fontlab.flCanvas.appendDecorator')

    def availableRect(self) -> QRectF:
        'QRectF availableRect()'
        _unavailable('fontlab.flCanvas.availableRect')

    def boundingRectOnCanvas(self, *args: Any, **kwargs: Any) -> Any:
        'QRectF boundingRectOnCanvas('
        _unavailable('fontlab.flCanvas.boundingRectOnCanvas')

    def canvas(self) -> flCanvas:
        'flCanvas canvas()'
        _unavailable('fontlab.flCanvas.canvas')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flCanvas.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flCanvas.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flCanvas.clearAboveHistory')

    def clearDecorators(self) -> Any:
        'clearDecorators()'
        _unavailable('fontlab.flCanvas.clearDecorators')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flCanvas.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flCanvas.clearFlags')

    def clearItems(self) -> Any:
        'clearItems()'
        _unavailable('fontlab.flCanvas.clearItems')

    def clearSurfaces(self) -> Any:
        'clearSurfaces()'
        _unavailable('fontlab.flCanvas.clearSurfaces')

    def clearTextBlocks(self) -> Any:
        'clearTextBlocks()'
        _unavailable('fontlab.flCanvas.clearTextBlocks')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flCanvas.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flCanvas.cloneObject')

    def collectChangedRects(self) -> Any:
        'collectChangedRects()'
        _unavailable('fontlab.flCanvas.collectChangedRects')

    def contain(self, canvas_pos: QPointF) -> bool:
        'bool contain(QPointF canvas_pos)'
        _unavailable('fontlab.flCanvas.contain')

    def containsItem(self, arg0: flVisualItem) -> bool:
        'bool containsItem(flVisualItem)'
        _unavailable('fontlab.flCanvas.containsItem')

    def createFrame(self, list: fgSymbolList, position: QPointF) -> fgSymbolList:
        'fgSymbolList createFrame(fgSymbolList list, QPointF position)'
        _unavailable('fontlab.flCanvas.createFrame')

    def createInstance(self) -> flCanvas:
        'flCanvas createInstance()'
        _unavailable('fontlab.flCanvas.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flCanvas.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flCanvas.currentHistoryState')

    def deactivateEditor(self) -> Any:
        'deactivateEditor()'
        _unavailable('fontlab.flCanvas.deactivateEditor')

    def deactivatePreviewNodes(self) -> Any:
        'deactivatePreviewNodes()'
        _unavailable('fontlab.flCanvas.deactivatePreviewNodes')

    def distanceTo(self, arg0: QPointF) -> float:
        'double distanceTo(QPointF)'
        _unavailable('fontlab.flCanvas.distanceTo')

    def ensureVisible(self, total_cover: Any = ...) -> Any:
        'ensureVisible(QPointF | QRectF canvas_rect[, bool total_cover = true])'
        _unavailable('fontlab.flCanvas.ensureVisible')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flCanvas.flag')

    def getHighlight(self) -> Any:
        'QRectF/Nothing getHighlight()'
        _unavailable('fontlab.flCanvas.getHighlight')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flCanvas.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flCanvas.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flCanvas.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flCanvas.getPropertyInt')

    def getScaleTo(self, arg0: flShapeInfo) -> float:
        'double getScaleTo(flShapeInfo)'
        _unavailable('fontlab.flCanvas.getScaleTo')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flCanvas.hasHistoryState')

    def haveCanvas(self) -> bool:
        'bool haveCanvas()'
        _unavailable('fontlab.flCanvas.haveCanvas')

    def haveEditor(self, canvas_pos: QPointF) -> bool:
        'bool haveEditor(QPointF canvas_pos)'
        _unavailable('fontlab.flCanvas.haveEditor')

    def haveHoveredItem(self) -> bool:
        'bool haveHoveredItem()'
        _unavailable('fontlab.flCanvas.haveHoveredItem')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flCanvas.haveObject')

    def haveSelectedNodes(self) -> bool:
        'bool haveSelectedNodes()'
        _unavailable('fontlab.flCanvas.haveSelectedNodes')

    def hide(self) -> Any:
        'hide()'
        _unavailable('fontlab.flCanvas.hide')

    def highlight(self, arg0: QRectF) -> Any:
        'highlight(QRectF)'
        _unavailable('fontlab.flCanvas.highlight')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flCanvas.historyStates')

    def hoveredItem(self) -> flVisualItem:
        'flVisualItem hoveredItem()'
        _unavailable('fontlab.flCanvas.hoveredItem')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flCanvas.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flCanvas.initialHistoryState')

    def instanceAcceptEvents(self) -> int:
        'int instanceAcceptEvents()'
        _unavailable('fontlab.flCanvas.instanceAcceptEvents')

    def instanceType(self) -> int:
        'int instanceType()'
        _unavailable('fontlab.flCanvas.instanceType')

    def invertSelectedNodes(self, *args: Any, **kwargs: Any) -> Any:
        'invertSelectedNodes(QList<flNodeInfo>)'
        _unavailable('fontlab.flCanvas.invertSelectedNodes')

    def invselect(self) -> Any:
        'invselect()'
        _unavailable('fontlab.flCanvas.invselect')

    def isActiveCanvas(self) -> bool:
        'bool isActiveCanvas()'
        _unavailable('fontlab.flCanvas.isActiveCanvas')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flCanvas.isEqual')

    def isFocusedCanvas(self) -> bool:
        'bool isFocusedCanvas()'
        _unavailable('fontlab.flCanvas.isFocusedCanvas')

    def isSelectable(self) -> bool:
        'bool isSelectable()'
        _unavailable('fontlab.flCanvas.isSelectable')

    def isStableSelect(self) -> bool:
        'bool isStableSelect()'
        _unavailable('fontlab.flCanvas.isStableSelect')

    def itemScale(self) -> float:
        'double itemScale()'
        _unavailable('fontlab.flCanvas.itemScale')

    def mapCanvasDistanceToItem(self, arg0: QPointF) -> QPointF:
        'QPointF mapCanvasDistanceToItem(QPointF)'
        _unavailable('fontlab.flCanvas.mapCanvasDistanceToItem')

    def mapCanvasToItem(self, QRectF: Any) -> Any:
        'QPointF | QRectF mapCanvasToItem(QPointF | QRectF)'
        _unavailable('fontlab.flCanvas.mapCanvasToItem')

    def mapDeltaFromGlobalToCanvas(self, arg0: QPoint) -> QPointF:
        'QPointF mapDeltaFromGlobalToCanvas(QPoint)'
        _unavailable('fontlab.flCanvas.mapDeltaFromGlobalToCanvas')

    def mapFromGlobal(self, QPoint: Any) -> Any:
        'QRectF | QPointF mapFromGlobal(QRect | QPoint)'
        _unavailable('fontlab.flCanvas.mapFromGlobal')

    def mapFromViewport(self, QPoint: Any) -> Any:
        'QRectF | QLineF | QPointF mapFromViewport(QRectF | QRect | QLineF | QPointF | QPoint)'
        _unavailable('fontlab.flCanvas.mapFromViewport')

    def mapItemToCanvas(self, QRectF: Any) -> Any:
        'QPointF | QRectF mapItemToCanvas(QPointF | QRectF)'
        _unavailable('fontlab.flCanvas.mapItemToCanvas')

    def mapToGlobal(self, arg0: QPointF) -> QPointF:
        'QPointF mapToGlobal(QPointF)'
        _unavailable('fontlab.flCanvas.mapToGlobal')

    def mapToViewport(self, QPoint: Any) -> Any:
        'QPolygonF | QRect | QPoint mapToViewport(QPolygonF | QRect | QPoint)'
        _unavailable('fontlab.flCanvas.mapToViewport')

    def mapToViewportF(self, QLineF: Any) -> Any:
        'QPointF | QLineF mapToViewportF(QPointF | QLineF)'
        _unavailable('fontlab.flCanvas.mapToViewportF')

    def metricStep(self) -> float:
        'double metricStep()'
        _unavailable('fontlab.flCanvas.metricStep')

    def mousePosition(self) -> QPointF:
        'QPointF mousePosition()'
        _unavailable('fontlab.flCanvas.mousePosition')

    def mousePressed(self) -> bool:
        'bool mousePressed()'
        _unavailable('fontlab.flCanvas.mousePressed')

    def move(self, arg0: QPointF) -> None:
        'void move(QPointF)'
        _unavailable('fontlab.flCanvas.move')

    def operationAdjustMetrics(self, delta: float, percent: bool) -> Any:
        'operationAdjustMetrics(double delta, bool percent)'
        _unavailable('fontlab.flCanvas.operationAdjustMetrics')

    def operationAlign(self, *args: Any, **kwargs: Any) -> Any:
        'operationAlign(Qt::Alignment)'
        _unavailable('fontlab.flCanvas.operationAlign')

    def operationBeauty(self, bool: Any) -> Any:
        'operationBeauty(bool)'
        _unavailable('fontlab.flCanvas.operationBeauty')

    def operationBreak(self, notify: bool, alone_selected: bool) -> bool:
        'bool operationBreak(bool notify, bool alone_selected)'
        _unavailable('fontlab.flCanvas.operationBreak')

    def operationCopyToMask(self, *args: Any, **kwargs: Any) -> Any:
        'operationCopyToMask(bool global = false)'
        _unavailable('fontlab.flCanvas.operationCopyToMask')

    def operationDecompose(self) -> bool:
        'bool operationDecompose()'
        _unavailable('fontlab.flCanvas.operationDecompose')

    def operationFlipHorizontal(self) -> Any:
        'operationFlipHorizontal()'
        _unavailable('fontlab.flCanvas.operationFlipHorizontal')

    def operationFlipVertical(self) -> Any:
        'operationFlipVertical()'
        _unavailable('fontlab.flCanvas.operationFlipVertical')

    def operationGenius(self, bool: Any) -> Any:
        'operationGenius(bool)'
        _unavailable('fontlab.flCanvas.operationGenius')

    def operationHarmonize(self) -> Any:
        'operationHarmonize()'
        _unavailable('fontlab.flCanvas.operationHarmonize')

    def operationImprove(self) -> Any:
        'operationImprove()'
        _unavailable('fontlab.flCanvas.operationImprove')

    def operationJoin(self) -> Any:
        'operationJoin()'
        _unavailable('fontlab.flCanvas.operationJoin')

    def operationNoServant(self) -> Any:
        'operationNoServant()'
        _unavailable('fontlab.flCanvas.operationNoServant')

    def operationPrepare(self, *args: Any, **kwargs: Any) -> Any:
        '(flModelProducer, QList<flNodeInfo> selection, flShapeInfo, flGlyphInfo)/Nothing operationPrepare(bool allow_all_contours, bool allow_all_nodes = false)'
        _unavailable('fontlab.flCanvas.operationPrepare')

    def operationReverseContours(self) -> Any:
        'operationReverseContours()'
        _unavailable('fontlab.flCanvas.operationReverseContours')

    def operationRotate180(self) -> Any:
        'operationRotate180()'
        _unavailable('fontlab.flCanvas.operationRotate180')

    def operationRotate90(self) -> Any:
        'operationRotate90()'
        _unavailable('fontlab.flCanvas.operationRotate90')

    def operationServantX(self, bool: Any) -> Any:
        'operationServantX(bool)'
        _unavailable('fontlab.flCanvas.operationServantX')

    def operationServantY(self, bool: Any) -> Any:
        'operationServantY(bool)'
        _unavailable('fontlab.flCanvas.operationServantY')

    def operationSetMetrics(self, mode: int) -> Any:
        'operationSetMetrics(int mode)'
        _unavailable('fontlab.flCanvas.operationSetMetrics')

    def operationSimplify(self) -> Any:
        'operationSimplify()'
        _unavailable('fontlab.flCanvas.operationSimplify')

    def operationSmartAngle(self, bool: Any) -> Any:
        'operationSmartAngle(bool)'
        _unavailable('fontlab.flCanvas.operationSmartAngle')

    def operationSmooth(self, bool: Any) -> Any:
        'operationSmooth(bool)'
        _unavailable('fontlab.flCanvas.operationSmooth')

    def operationToBeziers(self) -> Any:
        'operationToBeziers()'
        _unavailable('fontlab.flCanvas.operationToBeziers')

    def operationToCurve(self) -> Any:
        'operationToCurve()'
        _unavailable('fontlab.flCanvas.operationToCurve')

    def operationToLine(self) -> Any:
        'operationToLine()'
        _unavailable('fontlab.flCanvas.operationToLine')

    def operationToSplines(self) -> Any:
        'operationToSplines()'
        _unavailable('fontlab.flCanvas.operationToSplines')

    def paint(self, *args: Any, **kwargs: Any) -> Any:
        'void paint(QPainter*)'
        _unavailable('fontlab.flCanvas.paint')

    def placeAICB(self, position: QPointF, mime_data: Any) -> bool:
        'bool placeAICB(QPointF position, QString filename | QMimeData mime_data)'
        _unavailable('fontlab.flCanvas.placeAICB')

    def placeArtwork(self, position: QPointF, urls_list: list[QUrl]) -> bool:
        'bool placeArtwork(QPointF position, QList<QUrl> urls_list)'
        _unavailable('fontlab.flCanvas.placeArtwork')

    def popupHost(self) -> Any:
        'YPopupHost* popupHost()'
        _unavailable('fontlab.flCanvas.popupHost')

    def preview(self) -> Any:
        'preview()'
        _unavailable('fontlab.flCanvas.preview')

    def producer(self) -> flObject:
        'flObject producer()'
        _unavailable('fontlab.flCanvas.producer')

    def rectToUpdate(self) -> QRect:
        'QRect& rectToUpdate()'
        _unavailable('fontlab.flCanvas.rectToUpdate')

    def referencePoint(self) -> QPointF:
        'QPointF referencePoint()'
        _unavailable('fontlab.flCanvas.referencePoint')

    def refresh(self) -> Any:
        'refresh()'
        _unavailable('fontlab.flCanvas.refresh')

    def refreshAll(self) -> Any:
        'refreshAll()'
        _unavailable('fontlab.flCanvas.refreshAll')

    def refreshCanvasRect(self, arg0: QRectF) -> Any:
        'refreshCanvasRect(QRectF)'
        _unavailable('fontlab.flCanvas.refreshCanvasRect')

    def refreshGlyphRect(self, arg0: QRectF) -> Any:
        'refreshGlyphRect(QRectF)'
        _unavailable('fontlab.flCanvas.refreshGlyphRect')

    def regionToUpdate(self) -> QRegion:
        'QRegion& regionToUpdate()'
        _unavailable('fontlab.flCanvas.regionToUpdate')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flCanvas.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flCanvas.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flCanvas.removeChild')

    def removeDeadSmartAngles(self) -> Any:
        'removeDeadSmartAngles()'
        _unavailable('fontlab.flCanvas.removeDeadSmartAngles')

    def removeDecorator(self, arg0: flVisualItem) -> None:
        'void removeDecorator(flVisualItem)'
        _unavailable('fontlab.flCanvas.removeDecorator')

    def removeItem(self, arg0: flVisualItem) -> Any:
        'removeItem(flVisualItem)'
        _unavailable('fontlab.flCanvas.removeItem')

    def removeTextBlock(self, arg0: flTextBlock) -> Any:
        'removeTextBlock(flTextBlock)'
        _unavailable('fontlab.flCanvas.removeTextBlock')

    def removedFromCanvas(self) -> Any:
        'removedFromCanvas()'
        _unavailable('fontlab.flCanvas.removedFromCanvas')

    def removedFromWorkspace(self, arg0: flWorkspace) -> Any:
        'removedFromWorkspace(flWorkspace)'
        _unavailable('fontlab.flCanvas.removedFromWorkspace')

    def resetHighlight(self) -> Any:
        'resetHighlight()'
        _unavailable('fontlab.flCanvas.resetHighlight')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flCanvas.restoreHistoryState')

    def scale(self) -> float:
        'double scale()'
        _unavailable('fontlab.flCanvas.scale')

    def scaled(self, d: float) -> float:
        'double scaled(double d)'
        _unavailable('fontlab.flCanvas.scaled')

    def select(self) -> Any:
        'select()'
        _unavailable('fontlab.flCanvas.select')

    def selectNode(self, arg0: flNodeInfo) -> Any:
        'selectNode(flNodeInfo)'
        _unavailable('fontlab.flCanvas.selectNode')

    def selectNodes(self, *args: Any, **kwargs: Any) -> Any:
        'selectNodes(QList<flNodeInfo>)'
        _unavailable('fontlab.flCanvas.selectNodes')

    def selectedNodes(self) -> list[flNodeInfo]:
        'QList<flNodeInfo> selectedNodes()'
        _unavailable('fontlab.flCanvas.selectedNodes')

    def selection(self) -> list[flVisualItem]:
        'QList<flVisualItem> selection()'
        _unavailable('fontlab.flCanvas.selection')

    def setCursor(self, arg0: QCursor) -> Any:
        'setCursor(QCursor)'
        _unavailable('fontlab.flCanvas.setCursor')

    def setCursorId(self, CursorId: Any) -> Any:
        'setCursorId(CursorId)'
        _unavailable('fontlab.flCanvas.setCursorId')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flCanvas.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flCanvas.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flCanvas.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flCanvas.setPropertyInt')

    def setSelectedNodes(self, *args: Any, **kwargs: Any) -> Any:
        'setSelectedNodes(QList<flNodeInfo>, bool )'
        _unavailable('fontlab.flCanvas.setSelectedNodes')

    def show(self) -> Any:
        'show()'
        _unavailable('fontlab.flCanvas.show')

    def slantTransform(self, glyph_info: flGlyphInfo) -> QTransform:
        'QTransform slantTransform(flGlyphInfo glyph_info)'
        _unavailable('fontlab.flCanvas.slantTransform')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flCanvas.tag')

    def textBlocks(self) -> list[flTextBlock]:
        'QList<flTextBlock> textBlocks()'
        _unavailable('fontlab.flCanvas.textBlocks')

    def unselect(self) -> Any:
        'unselect()'
        _unavailable('fontlab.flCanvas.unselect')

    def unselectAll(self) -> bool:
        'bool unselectAll()'
        _unavailable('fontlab.flCanvas.unselectAll')

    def unselectAllNodes(self) -> bool:
        'bool unselectAllNodes()'
        _unavailable('fontlab.flCanvas.unselectAllNodes')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flCanvas.update')

    def updateCanvasRectA(self, arg0: QRectF) -> Any:
        'updateCanvasRectA(QRectF)'
        _unavailable('fontlab.flCanvas.updateCanvasRectA')

    def updateMousePos(self, arg0: QPoint) -> Any:
        'updateMousePos(QPoint)'
        _unavailable('fontlab.flCanvas.updateMousePos')

    def updateScreenRect(self, arg0: QRectF) -> Any:
        'updateScreenRect(QRectF)'
        _unavailable('fontlab.flCanvas.updateScreenRect')

    def updateScreenRegion(self, arg0: QRegion) -> Any:
        'updateScreenRegion(QRegion)'
        _unavailable('fontlab.flCanvas.updateScreenRegion')

    def updateViewRect(self) -> Any:
        'updateViewRect()'
        _unavailable('fontlab.flCanvas.updateViewRect')

    def updateViewport(self) -> Any:
        'updateViewport()'
        _unavailable('fontlab.flCanvas.updateViewport')

    def viewPortHasFocus(self) -> bool:
        'bool viewPortHasFocus()'
        _unavailable('fontlab.flCanvas.viewPortHasFocus')

    def viewPortRect(self) -> QRect:
        'QRect viewPortRect()'
        _unavailable('fontlab.flCanvas.viewPortRect')

    def viewRect(self) -> QRectF:
        'QRectF viewRect()'
        _unavailable('fontlab.flCanvas.viewRect')

    def zoomTo(self, canvas_rect: QRectF) -> Any:
        'zoomTo(QPointF canvas_point, double scale, ViewPointAlignment=vpCenter) | zoomTo(QRectF canvas_rect)'
        _unavailable('fontlab.flCanvas.zoomTo')

    def zoomToReaded(self) -> Any:
        'zoomToReaded()'
        _unavailable('fontlab.flCanvas.zoomToReaded')

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
    'flContour representation\n\nConstructors:\n  flContour()\n  flContour(flObject)\n  flContour(flContour)\n  flContour(fgContour)\n  flContour(id)\n  flContour(list(Node)[, bool closed=false])\n  flContour(list(QPointF)[, flNode::NodeType=flNode::On[, bool closed=false]])\n  flContour(QRectF)\n  flContour(QLineF)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flContour')

    def add(self, QPointF: Any) -> Any:
        'add(flNode | QPointF)'
        _unavailable('fontlab.flContour.add')

    def append(self, flContour: Any) -> Any:
        'append(list(flNode) | flContour)'
        _unavailable('fontlab.flContour.append')

    def appendMapped(self, flContour: Any, arg1: QTransform) -> Any:
        'appendMapped(list(flNode) | flContour, QTransform)'
        _unavailable('fontlab.flContour.appendMapped')

    def applyTransform(self) -> Any:
        'applyTransform()'
        _unavailable('fontlab.flContour.applyTransform')

    def assign(self, *args: Any, **kwargs: Any) -> Any:
        'assign(flContour | fgContour | list(flNode))'
        _unavailable('fontlab.flContour.assign')

    def assignOwner(self) -> Any:
        'assignOwner()'
        _unavailable('fontlab.flContour.assignOwner')

    def at(self, index: int) -> flNode:
        'flNode at(int index)'
        _unavailable('fontlab.flContour.at')

    def autoG2(self, tolerance: float) -> Any:
        'autoG2(float tolerance)'
        _unavailable('fontlab.flContour.autoG2')

    def beautify(self, precision: Any = ...) -> bool:
        'bool beautify([int precision = 1])'
        _unavailable('fontlab.flContour.beautify')

    def bindDependencies(self) -> Any:
        'bindDependencies()'
        _unavailable('fontlab.flContour.bindDependencies')

    def boundingBox(self, *args: Any, **kwargs: Any) -> Any:
        'QRectF boundingBox([QTransform])'
        _unavailable('fontlab.flContour.boundingBox')

    def breakContour(self, *args: Any, **kwargs: Any) -> Any:
        '(flContour, flNode, flNode)/Nothing breakContour(flNode) | flContour/Nothing breakContour(int node_ix)'
        _unavailable('fontlab.flContour.breakContour')

    def breakContourExpanded(self, *args: Any, **kwargs: Any) -> Any:
        'flContour/Nothing breakContourExpanded(int node_ix | flNode [, float extrapolate_d]'
        _unavailable('fontlab.flContour.breakContourExpanded')

    def calculate(self, *args: Any, **kwargs: Any) -> Any:
        'QPointF calculate(float t[, QTransform tx])'
        _unavailable('fontlab.flContour.calculate')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flContour.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flContour.checkInitHistoryState')

    def checkSmooth(self) -> Any:
        'checkSmooth()'
        _unavailable('fontlab.flContour.checkSmooth')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flContour.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flContour.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flContour.clearFlags')

    def clearNodes(self) -> Any:
        'clearNodes()'
        _unavailable('fontlab.flContour.clearNodes')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flContour.clone')

    def cloneMapped(self, *args: Any, **kwargs: Any) -> Any:
        'flContour cloneMapped(QTransform[, float ex_t0, float ex_t1])'
        _unavailable('fontlab.flContour.cloneMapped')

    def cloneMappedByT(self, tx: QTransform, t0: float, t1: float) -> flContour:
        'flContour cloneMappedByT(QTransform tx, float t0, float t1)'
        _unavailable('fontlab.flContour.cloneMappedByT')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flContour.cloneObject')

    def cloneSelected(self, ignore_alone: Any = ...) -> Any:
        'list(flContour)/Nothing cloneSelected([QTransform, [bool ignore_alone=true]])'
        _unavailable('fontlab.flContour.cloneSelected')

    def compare(self, *args: Any, **kwargs: Any) -> Any:
        '(bool result, QPointF offset) compare(flContour, float error)'
        _unavailable('fontlab.flContour.compare')

    def contains(self, QPointF: Any) -> bool:
        'bool contains(flContour knife | QPointF)'
        _unavailable('fontlab.flContour.contains')

    def convertExToT(self, arg0: float) -> float:
        'float convertExToT(float)'
        _unavailable('fontlab.flContour.convertExToT')

    def convertTTtoCurve(self) -> Any:
        'convertTTtoCurve()'
        _unavailable('fontlab.flContour.convertTTtoCurve')

    def convertToFgContour(self, *args: Any, **kwargs: Any) -> Any:
        'fgContour convertToFgContour([QTransform tx])'
        _unavailable('fontlab.flContour.convertToFgContour')

    def convertTtoEx(self, arg0: float) -> float:
        'float convertTtoEx(float)'
        _unavailable('fontlab.flContour.convertTtoEx')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flContour.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flContour.currentHistoryState')

    def curvature(self, arg0: float) -> float:
        'float  curvature(float)'
        _unavailable('fontlab.flContour.curvature')

    def derivative(self, arg0: float) -> QPointF:
        'QPointF derivative(float)'
        _unavailable('fontlab.flContour.derivative')

    def distanceBetween(self, t0: float, step: Any = ...) -> float:
        'float distanceBetween(float t0, float t1[, float step =0.1])'
        _unavailable('fontlab.flContour.distanceBetween')

    def draw(self, pen: Any) -> Any:
        'draw(pen) - Draw the contour’s outline data to the given type-pen'
        _unavailable('fontlab.flContour.draw')

    def drawPoints(self, *args: Any, **kwargs: Any) -> Any:
        'drawPoints(point-pen) - Draw the contour’s outline data to the given type-point-pen'
        _unavailable('fontlab.flContour.drawPoints')

    def extrapolateFirst(self, arg0: float) -> Any:
        'extrapolateFirst(float)'
        _unavailable('fontlab.flContour.extrapolateFirst')

    def extrapolateLast(self, arg0: float) -> Any:
        'extrapolateLast(float)'
        _unavailable('fontlab.flContour.extrapolateLast')

    def fastAppend(self, *args: Any, **kwargs: Any) -> Any:
        'fastAppend( list(flNode) )'
        _unavailable('fontlab.flContour.fastAppend')

    def fastClone(self, ex_t0: float, ex_t1: float) -> flContour:
        'flContour fastClone(float ex_t0, float ex_t1)'
        _unavailable('fontlab.flContour.fastClone')

    def fastCloneByT(self, t0: float, t1: float) -> flContour:
        'flContour fastCloneByT(float t0, float t1)'
        _unavailable('fontlab.flContour.fastCloneByT')

    def find(self, *args: Any, **kwargs: Any) -> Any:
        'flNode find(QPointF, float, flNode::NodeType)'
        _unavailable('fontlab.flContour.find')

    def findNearest(self, *args: Any, **kwargs: Any) -> Any:
        '(float out_nearest_t, float dist)/Nothing findNearest(QPointF shape_p[, int orientation=0])'
        _unavailable('fontlab.flContour.findNearest')

    def findNearestNode(self, *args: Any, **kwargs: Any) -> Any:
        '(flNode, float new_maxd)/Nothing findNearestNode(QPointF p, flNode::NodeType node_type, float maxd)'
        _unavailable('fontlab.flContour.findNearestNode')

    def findNearestOn(self, p: QPointF, base_t: float) -> Any:
        'float out_nearest_t/Nothing findNearestOn(QPointF  p, float base_t)'
        _unavailable('fontlab.flContour.findNearestOn')

    def findNode(self, name: Any) -> Any:
        'flNode/Nothing findNode(uint id | string name)'
        _unavailable('fontlab.flContour.findNode')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flContour.flag')

    def getBoundedT(self, param_t: float, radius: float) -> float:
        'float getBoundedT(float param_t, float radius)'
        _unavailable('fontlab.flContour.getBoundedT')

    def getChangesRect(self) -> QRectF:
        'QRectF getChangesRect()'
        _unavailable('fontlab.flContour.getChangesRect')

    def getFirstPoint(self, *args: Any, **kwargs: Any) -> Any:
        'QPointF/Nothing getFirstPoint([int =0])'
        _unavailable('fontlab.flContour.getFirstPoint')

    def getLastPoint(self, *args: Any, **kwargs: Any) -> Any:
        'QPointF/Nothing getLastPoint([int =0])'
        _unavailable('fontlab.flContour.getLastPoint')

    def getLength(self, int: Any = 10) -> float:
        'float getLength([float t0, float t1,] int =10)'
        _unavailable('fontlab.flContour.getLength')

    def getLengthSquareBRect(self, *args: Any, **kwargs: Any) -> Any:
        '(float square, float length, QRectF brect) getLengthSquareBRect(float t0, float t1[, int step=10])'
        _unavailable('fontlab.flContour.getLengthSquareBRect')

    def getNext(self, *args: Any, **kwargs: Any) -> Any:
        'flNode/Nothing getNext(index[, flNode::NodeType=flNode::On])'
        _unavailable('fontlab.flContour.getNext')

    def getNextT(self, *args: Any, **kwargs: Any) -> Any:
        '(bool, float) getNextT(float base_t, float offset)'
        _unavailable('fontlab.flContour.getNextT')

    def getNodeAt(self, *args: Any, **kwargs: Any) -> Any:
        'flNode/Nothing getNodeAt(int idx[, flNode::NodeType = flNode::AnyNodeMask])'
        _unavailable('fontlab.flContour.getNodeAt')

    def getPoint(self, *args: Any, **kwargs: Any) -> Any:
        'QPointF/Nothing getPoint(int idx[, flNode::NodeType = flNode::On])'
        _unavailable('fontlab.flContour.getPoint')

    def getPrev(self, *args: Any, **kwargs: Any) -> Any:
        'flNode/Nothing getPrev(index[, flNode::NodeType=flNode::On])'
        _unavailable('fontlab.flContour.getPrev')

    def getPrevT(self, *args: Any, **kwargs: Any) -> Any:
        '(bool, float) getPrevT(float base_t, float offset)'
        _unavailable('fontlab.flContour.getPrevT')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flContour.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flContour.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flContour.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flContour.getPropertyInt')

    def getSegment(self, i0: int, i1: int, left: bool) -> Any:
        'list(flNode) getSegment(int i0, int i1, bool left)'
        _unavailable('fontlab.flContour.getSegment')

    def getSelectedBoundingBox(self) -> QRectF:
        'QRectF getSelectedBoundingBox()'
        _unavailable('fontlab.flContour.getSelectedBoundingBox')

    def getSelectedNodes(self) -> Any:
        'list(flNode)/Nothing getSelectedNodes()'
        _unavailable('fontlab.flContour.getSelectedNodes')

    def getSquare(self) -> float:
        'double getSquare()'
        _unavailable('fontlab.flContour.getSquare')

    def getT(self, arg0: flNode) -> float:
        'float getT(flNode)'
        _unavailable('fontlab.flContour.getT')

    def getUpdateRect(self, ex_t: float) -> QRectF:
        'QRectF getUpdateRect(float ex_t)'
        _unavailable('fontlab.flContour.getUpdateRect')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flContour.hasHistoryState')

    def hasIntersPoints(self, arg0: flContour) -> bool:
        'bool hasIntersPoints(flContour)'
        _unavailable('fontlab.flContour.hasIntersPoints')

    def hasSelected(self, SelectionMode: Any) -> bool:
        'bool hasSelected(SelectionMode)'
        _unavailable('fontlab.flContour.hasSelected')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flContour.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flContour.historyStates')

    def improve(self) -> bool:
        'bool improve()'
        _unavailable('fontlab.flContour.improve')

    def indentParamT(self, base_t: float, step: Any = ...) -> float:
        'float indentParamT(float base_t, float indent[, float step =0.1])'
        _unavailable('fontlab.flContour.indentParamT')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flContour.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flContour.initialHistoryState')

    def inkBox(self, *args: Any, **kwargs: Any) -> Any:
        'QRectF inkBox([QTransform tx])'
        _unavailable('fontlab.flContour.inkBox')

    def insert(self, *args: Any, **kwargs: Any) -> Any:
        'insert(index, flNode | list(flNode) )'
        _unavailable('fontlab.flContour.insert')

    def insertNodeTo(self, t: float) -> flNode:
        'flNode insertNodeTo(float t)'
        _unavailable('fontlab.flContour.insertNodeTo')

    def insertSafeNodeTo(self, t: float, dst: float) -> flNode:
        'flNode insertSafeNodeTo(float t, float dst)'
        _unavailable('fontlab.flContour.insertSafeNodeTo')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flContour.instanceType')

    def isAllNodesSelected(self) -> bool:
        'bool isAllNodesSelected()'
        _unavailable('fontlab.flContour.isAllNodesSelected')

    def isCompatible(self, arg0: flContour, strong: bool) -> bool:
        'bool isCompatible(flContour, bool strong)'
        _unavailable('fontlab.flContour.isCompatible')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flContour.isEqual')

    def isFirst(self, arg0: flNode) -> bool:
        'bool isFirst(flNode)'
        _unavailable('fontlab.flContour.isFirst')

    def isLast(self, arg0: flNode) -> bool:
        'bool isLast(flNode)'
        _unavailable('fontlab.flContour.isLast')

    def isSelected(self, arg0: float) -> bool:
        'bool isSelected(float)'
        _unavailable('fontlab.flContour.isSelected')

    def mapParamT(self, arg0: float, arg1: float, arg2: float) -> float:
        'float mapParamT(float, float, float)'
        _unavailable('fontlab.flContour.mapParamT')

    def move(self, arg0: QPointF) -> Any:
        'move(QPointF)'
        _unavailable('fontlab.flContour.move')

    def nodes(self) -> Any:
        'list(flNode) nodes()'
        _unavailable('fontlab.flContour.nodes')

    def normalAt(self, *args: Any, **kwargs: Any) -> Any:
        'float normalAt(float t[, QTransform])'
        _unavailable('fontlab.flContour.normalAt')

    def normalPoint(self, t: float, length: float) -> QPointF:
        'QPointF normalPoint(float t, float length)'
        _unavailable('fontlab.flContour.normalPoint')

    def normalizeExT(self, arg0: float) -> float:
        'float normalizeExT(float)'
        _unavailable('fontlab.flContour.normalizeExT')

    def path(self) -> QPainterPath:
        'QPainterPath path()'
        _unavailable('fontlab.flContour.path')

    def pointInside(self, pt: QPointF) -> Any:
        'pointInside(QPointF pt) - Bool indicating if the point pt in the black area of the contour'
        _unavailable('fontlab.flContour.pointInside')

    def pointf(self, index: int) -> QPointF:
        'QPointF pointf(int index)'
        _unavailable('fontlab.flContour.pointf')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flContour.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flContour.remove')

    def removeAt(self, index: int) -> Any:
        'removeAt(int index)'
        _unavailable('fontlab.flContour.removeAt')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flContour.removeChild')

    def removeLast(self) -> Any:
        'removeLast()'
        _unavailable('fontlab.flContour.removeLast')

    def removeNodesBetween(self, prev: flNode, next: flNode) -> Any:
        'removeNodesBetween(flNode prev,  flNode next)'
        _unavailable('fontlab.flContour.removeNodesBetween')

    def removeOne(self, arg0: flNode) -> Any:
        'removeOne(flNode)'
        _unavailable('fontlab.flContour.removeOne')

    def replace(self, old_node: flNode, new_node: flNode) -> Any:
        'replace(flNode old_node, flNode new_node)'
        _unavailable('fontlab.flContour.replace')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flContour.restoreHistoryState')

    def reverse(self) -> Any:
        'reverse() - Reverse the direction of the contour'
        _unavailable('fontlab.flContour.reverse')

    def secondDerivative(self, arg0: float) -> QPointF:
        'QPointF secondDerivative(float)'
        _unavailable('fontlab.flContour.secondDerivative')

    def segment(self, t: float) -> Any:
        'CurveEx/Nothing segment(float t)'
        _unavailable('fontlab.flContour.segment')

    def segments(self) -> Any:
        'list(CurveEx) segments()'
        _unavailable('fontlab.flContour.segments')

    def selectedPath(self) -> QPainterPath:
        'QPainterPath selectedPath()'
        _unavailable('fontlab.flContour.selectedPath')

    def selectionChanged(self) -> Any:
        'selectionChanged()'
        _unavailable('fontlab.flContour.selectionChanged')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flContour.setFlag')

    def setNext(self, int: Any, arg1: QPointF) -> flNode:
        'flNode setNext(int, QPointF)'
        _unavailable('fontlab.flContour.setNext')

    def setPoint(self, index: int, p: QPointF) -> flNode:
        'flNode setPoint(int index, QPointF p)'
        _unavailable('fontlab.flContour.setPoint')

    def setPrev(self, int: Any, arg1: QPointF) -> flNode:
        'flNode setPrev(int, QPointF)'
        _unavailable('fontlab.flContour.setPrev')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flContour.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flContour.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flContour.setPropertyInt')

    def setSelectedNodes(self, bool: Any) -> Any:
        'setSelectedNodes(bool)'
        _unavailable('fontlab.flContour.setSelectedNodes')

    def setStartPoint(self, i: int) -> bool:
        'bool setStartPoint(int i)'
        _unavailable('fontlab.flContour.setStartPoint')

    def simplify(self, precision: float, lossy: bool, extremes: bool) -> Any:
        'simplify(float precision, bool lossy, bool extremes)'
        _unavailable('fontlab.flContour.simplify')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flContour.tag')

    def takeNodes(self) -> Any:
        'list(flNode) takeNodes()'
        _unavailable('fontlab.flContour.takeNodes')

    def tangent(self, t: float) -> float:
        'float tangent(float t)'
        _unavailable('fontlab.flContour.tangent')

    def toBeziers(self, tolerance: float) -> Any:
        'toBeziers(float tolerance)'
        _unavailable('fontlab.flContour.toBeziers')

    def toSplines(self, tolerance: float, short_splines: bool) -> Any:
        'toSplines(float tolerance, bool short_splines)'
        _unavailable('fontlab.flContour.toSplines')

    def unselectAll(self) -> Any:
        'unselectAll()'
        _unavailable('fontlab.flContour.unselectAll')

    def unselectedPath(self) -> QPainterPath:
        'QPainterPath unselectedPath()'
        _unavailable('fontlab.flContour.unselectedPath')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flContour.update')

    def updateG2(self, all_nodes: bool) -> Any:
        'updateG2(bool all_nodes)'
        _unavailable('fontlab.flContour.updateG2')

    def updateHobby(self, all_nodes: bool) -> Any:
        'updateHobby(bool all_nodes)'
        _unavailable('fontlab.flContour.updateHobby')

    def updateIndices(self) -> Any:
        'updateIndices()'
        _unavailable('fontlab.flContour.updateIndices')

    def validateExT(self, *args: Any, **kwargs: Any) -> Any:
        '(new_ex_t, bool) validateExT(float ex_t)'
        _unavailable('fontlab.flContour.validateExT')

    def validateIndex(self, *args: Any, **kwargs: Any) -> Any:
        '(new_inx, bool) validateIndex(int inx)'
        _unavailable('fontlab.flContour.validateIndex')

    def validateSmartR(self, *args: Any, **kwargs: Any) -> Any:
        '(new_r, max_available_r, bool) validateSmartR(int node_ix, float r)'
        _unavailable('fontlab.flContour.validateSmartR')

    def validateT(self, *args: Any, **kwargs: Any) -> Any:
        '(new_t, bool) validateT(float t)'
        _unavailable('fontlab.flContour.validateT')

    def validatedT(self, t: float) -> float:
        'float validatedT(float t)'
        _unavailable('fontlab.flContour.validatedT')

    def verifySmooth(self) -> Any:
        'verifySmooth()'
        _unavailable('fontlab.flContour.verifySmooth')

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
    'flContourInfo representation\n\nConstructors:\n  flContourInfo()\n  flContourInfo(flObject)\n  flContourInfo(flContour, flSearchInfo)\n  flContourInfo(flContour, flShapeInfo)\n  flContourInfo(flContour, flContourInfo)\n  flContourInfo(flContour, QTransform)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flContourInfo')

    def brectOnCanvas(self) -> QRectF:
        'QRectF brectOnCanvas()'
        _unavailable('fontlab.flContourInfo.brectOnCanvas')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flContourInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flContourInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flContourInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flContourInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flContourInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flContourInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flContourInfo.cloneObject')

    def cloneSelected(self) -> list[flContourInfo]:
        'QList<flContourInfo> cloneSelected()'
        _unavailable('fontlab.flContourInfo.cloneSelected')

    def combine(self, transform: QTransform) -> Any:
        'combine(QTransform transform)'
        _unavailable('fontlab.flContourInfo.combine')

    def createInstance(self) -> flContourInfo:
        'flContourInfo createInstance()'
        _unavailable('fontlab.flContourInfo.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flContourInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flContourInfo.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flContourInfo.flag')

    def getHitNode(self, canvas_pos: QPointF, node_mask: Any = ...) -> Any:
        'flNodeInfo/Nothing getHitNode(QPointF canvas_pos, double dist[, int node_mask=flNode::AnyNodeMask])'
        _unavailable('fontlab.flContourInfo.getHitNode')

    def getNodesInfo(self) -> list[flNodeInfo]:
        'QList<flNodeInfo> getNodesInfo()'
        _unavailable('fontlab.flContourInfo.getNodesInfo')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flContourInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flContourInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flContourInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flContourInfo.getPropertyInt')

    def getUpdateRect(self, ex_t: float) -> QRectF:
        'QRectF getUpdateRect(double ex_t)'
        _unavailable('fontlab.flContourInfo.getUpdateRect')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flContourInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flContourInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flContourInfo.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flContourInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flContourInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flContourInfo.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flContourInfo.isEqual')

    def paramExT(self) -> float:
        'double paramExT()'
        _unavailable('fontlab.flContourInfo.paramExT')

    def paramT(self) -> float:
        'double paramT()'
        _unavailable('fontlab.flContourInfo.paramT')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flContourInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flContourInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flContourInfo.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flContourInfo.restoreHistoryState')

    def setExT(self, ex_t: float) -> Any:
        'setExT(double ex_t)'
        _unavailable('fontlab.flContourInfo.setExT')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flContourInfo.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flContourInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flContourInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flContourInfo.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flContourInfo.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flContourInfo.update')

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
    'flEvent representation\n\nConstructors:\n  flEvent(flEvent)\n  flEvent(flEvent(EventType type[, int modifiers=-1])\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flEvent')

    EventType: dict
    modifiers: Any
    'int'
    type: Any
    'EventType'

class flExpression:
    'flExpression representation\n\nConstructors:\n  flExpression()\n  flExpression(flObject)\n  flExpression(flExpression)\n  flExpression(string)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flExpression')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flExpression.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flExpression.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flExpression.clearAboveHistory')

    def clearError(self) -> Any:
        'clearError()'
        _unavailable('fontlab.flExpression.clearError')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flExpression.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flExpression.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flExpression.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flExpression.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flExpression.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flExpression.currentHistoryState')

    def expression(self, aliases: dict[str, str]) -> str:
        'QString expression(QMap<QString, QString> aliases)'
        _unavailable('fontlab.flExpression.expression')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flExpression.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flExpression.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flExpression.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flExpression.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flExpression.getPropertyInt')

    def hasError(self) -> bool:
        'bool hasError()'
        _unavailable('fontlab.flExpression.hasError')

    def hasExpression(self) -> bool:
        'bool hasExpression()'
        _unavailable('fontlab.flExpression.hasExpression')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flExpression.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flExpression.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flExpression.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flExpression.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flExpression.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flExpression.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flExpression.isEqual')

    def isNeedToComplete(self) -> bool:
        'bool isNeedToComplete()'
        _unavailable('fontlab.flExpression.isNeedToComplete')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flExpression.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flExpression.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flExpression.removeChild')

    def resetReady(self) -> Any:
        'resetReady()'
        _unavailable('fontlab.flExpression.resetReady')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flExpression.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flExpression.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flExpression.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flExpression.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flExpression.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flExpression.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flExpression.update')

    def variables(self, *args: Any, **kwargs: Any) -> Any:
        'QStringList variables([QMap<QString, QString> aliases])'
        _unavailable('fontlab.flExpression.variables')

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
    'flGlyph representation\n\nConstructors:\n  flGlyph()\n  flGlyph(flGlyph)\n  flGlyph(flObject)\n  flGlyph(fgGlyph, fgFont)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flGlyph')

    def addLayer(self, back: Any = ...) -> None:
        'void addLayer(flLayer[, bool back = false])'
        _unavailable('fontlab.flGlyph.addLayer')

    def addLayers(self, *args: Any, **kwargs: Any) -> Any:
        'void addLayers(list(flLayer))'
        _unavailable('fontlab.flGlyph.addLayers')

    def applyTransform(self, *args: Any, **kwargs: Any) -> Any:
        'applyTransform([QTransform transform])'
        _unavailable('fontlab.flGlyph.applyTransform')

    def assignFontGateData(self, arg0: fgFontGateData, doGuide: bool = True, doHints: bool = True, doAnchors: bool = True) -> None:
        'void assignFontGateData(fgFontGateData, bool doGuide = true, bool doHints = true, bool doAnchors = true)'
        _unavailable('fontlab.flGlyph.assignFontGateData')

    def bindDependencies(self) -> Any:
        'bindDependencies()'
        _unavailable('fontlab.flGlyph.bindDependencies')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flGlyph.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flGlyph.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flGlyph.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flGlyph.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flGlyph.clearFlags')

    def clearUpdateFgGlyphs(self) -> Any:
        'clearUpdateFgGlyphs()'
        _unavailable('fontlab.flGlyph.clearUpdateFgGlyphs')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flGlyph.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flGlyph.cloneObject')

    def createInstance(self) -> flGlyph:
        'flGlyph createInstance()'
        _unavailable('fontlab.flGlyph.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flGlyph.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flGlyph.currentHistoryState')

    def deactivateAll(self) -> Any:
        'deactivateAll()'
        _unavailable('fontlab.flGlyph.deactivateAll')

    def ensureFgData(self, arg0: fgGlyph) -> fgFontGateData:
        'fgFontGateData ensureFgData(fgGlyph)'
        _unavailable('fontlab.flGlyph.ensureFgData')

    def ensureMaskLayer(self) -> flLayer:
        'flLayer ensureMaskLayer()'
        _unavailable('fontlab.flGlyph.ensureMaskLayer')

    def fillFgData(self, doGuides: bool, doHints: bool) -> fgFontGateData:
        'fgFontGateData fillFgData(bool doGuides, bool doHints)'
        _unavailable('fontlab.flGlyph.fillFgData')

    def findLayer(self, cs: Any = ...) -> flLayer:
        'flLayer findLayer(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])'
        _unavailable('fontlab.flGlyph.findLayer')

    def findLayerCreate(self, cs: Any = ...) -> flLayer:
        'flLayer findLayerCreate(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])'
        _unavailable('fontlab.flGlyph.findLayerCreate')

    def findVerticalGuideline(self, arg0: str) -> Any:
        'double/Nothing findVerticalGuideline(QString)'
        _unavailable('fontlab.flGlyph.findVerticalGuideline')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flGlyph.flag')

    def getAuditInfo(self) -> Any:
        'list(flAuditInfo) getAuditInfo()'
        _unavailable('fontlab.flGlyph.getAuditInfo')

    def getLSB(self, tr: QTransform) -> float:
        'double getLSB(QTransform tr)'
        _unavailable('fontlab.flGlyph.getLSB')

    def getLayerByName(self, create: Any = ...) -> flLayer:
        'flLayer getLayerByName(QString[, bool create =false])'
        _unavailable('fontlab.flGlyph.getLayerByName')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flGlyph.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flGlyph.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flGlyph.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flGlyph.getPropertyInt')

    def getRSB(self, tr: QTransform) -> float:
        'double getRSB(QTransform tr)'
        _unavailable('fontlab.flGlyph.getRSB')

    def getSB(self, *args: Any, **kwargs: Any) -> Any:
        '(double l, double r) getSB(QTransform tr)'
        _unavailable('fontlab.flGlyph.getSB')

    def glyphName(self) -> str:
        'QString glyphName()'
        _unavailable('fontlab.flGlyph.glyphName')

    def hasFontAudit(self) -> bool:
        'bool hasFontAudit()'
        _unavailable('fontlab.flGlyph.hasFontAudit')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flGlyph.hasHistoryState')

    def hasInstance(self, arg0: fgGlyph) -> bool:
        'bool hasInstance(fgGlyph)'
        _unavailable('fontlab.flGlyph.hasInstance')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flGlyph.haveObject')

    def haveSelected(self, SelectionMode: Any) -> bool:
        'bool haveSelected(SelectionMode)'
        _unavailable('fontlab.flGlyph.haveSelected')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flGlyph.historyStates')

    def horzReflection(self) -> bool:
        'bool horzReflection()'
        _unavailable('fontlab.flGlyph.horzReflection')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flGlyph.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flGlyph.initialHistoryState')

    def inkBox(self, tx: Any = ...) -> QRectF:
        'QRectF inkBox([QTransform tx = QTransform()])'
        _unavailable('fontlab.flGlyph.inkBox')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flGlyph.instanceType')

    def interpolateInstance(self, location: flLocation, round: bool) -> flLayer:
        'flLayer interpolateInstance(flLocation location, bool round)'
        _unavailable('fontlab.flGlyph.interpolateInstance')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flGlyph.isEqual')

    def isUnbindedDependecies(self) -> bool:
        'bool isUnbindedDependecies()'
        _unavailable('fontlab.flGlyph.isUnbindedDependecies')

    def linkInstances(self, arg0: flGlyph, arg1: fgGlyph) -> bool:
        'bool linkInstances(flGlyph, fgGlyph)'
        _unavailable('fontlab.flGlyph.linkInstances')

    def masters2PS(self, precision: float) -> bool:
        'bool masters2PS(double precision)'
        _unavailable('fontlab.flGlyph.masters2PS')

    def masters2TT(self, precision: float) -> bool:
        'bool masters2TT(double precision)'
        _unavailable('fontlab.flGlyph.masters2TT')

    def measurementLine(self) -> Any:
        'double/Nothing measurementLine()'
        _unavailable('fontlab.flGlyph.measurementLine')

    def prepareTransformationData(self) -> Any:
        'prepareTransformationData()'
        _unavailable('fontlab.flGlyph.prepareTransformationData')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flGlyph.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flGlyph.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flGlyph.removeChild')

    def removeEmptyShapes(self) -> Any:
        'removeEmptyShapes()'
        _unavailable('fontlab.flGlyph.removeEmptyShapes')

    def removeLayer(self, arg0: flLayer) -> None:
        'void removeLayer(flLayer)'
        _unavailable('fontlab.flGlyph.removeLayer')

    def resetInkBox(self) -> Any:
        'resetInkBox()'
        _unavailable('fontlab.flGlyph.resetInkBox')

    def resetTransformationData(self) -> Any:
        'resetTransformationData()'
        _unavailable('fontlab.flGlyph.resetTransformationData')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flGlyph.restoreHistoryState')

    def setAllShapesSelected(self, bool: Any) -> Any:
        'setAllShapesSelected(bool)'
        _unavailable('fontlab.flGlyph.setAllShapesSelected')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flGlyph.setFlag')

    def setLSB(self, v: float, move_guidelines: bool, tr: QTransform) -> bool:
        'bool setLSB(double v, bool move_guidelines, QTransform tr)'
        _unavailable('fontlab.flGlyph.setLSB')

    def setLayers(self, *args: Any, **kwargs: Any) -> Any:
        'void setLayers(list(flLayer))'
        _unavailable('fontlab.flGlyph.setLayers')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flGlyph.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flGlyph.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flGlyph.setPropertyInt')

    def setRSB(self, v: float, tr: QTransform) -> bool:
        'bool setRSB(double v, QTransform tr)'
        _unavailable('fontlab.flGlyph.setRSB')

    def setReflected(self, *args: Any, **kwargs: Any) -> Any:
        'setReflected(bool, bool)'
        _unavailable('fontlab.flGlyph.setReflected')

    def setSB(self, l: float, r: float, move_guidelines: bool, all_layers: bool, tr: QTransform) -> bool:
        'bool setSB(double l, double r, bool move_guidelines, bool all_layers, QTransform tr)'
        _unavailable('fontlab.flGlyph.setSB')

    def setTag(self, arg0: str, bool: Any) -> None:
        'void setTag(QString, bool)'
        _unavailable('fontlab.flGlyph.setTag')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flGlyph.tag')

    def unselectAllNodes(self) -> Any:
        'unselectAllNodes()'
        _unavailable('fontlab.flGlyph.unselectAllNodes')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flGlyph.update')

    def updateActiveLayer(self, bool: Any) -> flLayer:
        'flLayer updateActiveLayer(bool)'
        _unavailable('fontlab.flGlyph.updateActiveLayer')

    def updateAudit(self, *args: Any, **kwargs: Any) -> Any:
        'void updateAudit(list(int))'
        _unavailable('fontlab.flGlyph.updateAudit')

    def updateFgGlyph(self, id: int) -> Any:
        'updateFgGlyph(uint id)'
        _unavailable('fontlab.flGlyph.updateFgGlyph')

    def updateSidebearings(self, nofify: bool) -> bool:
        'bool updateSidebearings(bool nofify)'
        _unavailable('fontlab.flGlyph.updateSidebearings')

    def updatedFgGlyphs(self) -> Any:
        'list(uint32_t) updatedFgGlyphs()'
        _unavailable('fontlab.flGlyph.updatedFgGlyphs')

    def vertReflection(self) -> bool:
        'bool vertReflection()'
        _unavailable('fontlab.flGlyph.vertReflection')

    def virtualTags(self) -> Any:
        'QSet<QString>/Nothing virtualTags()'
        _unavailable('fontlab.flGlyph.virtualTags')

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

class flGlyphInfo:
    'flGlyphInfo representation\n\nConstructors:\n  flGlyphInfo()\n  flGlyphInfo(flObject)\n  flGlyphInfo(flGlyphInfo)\n  flGlyphInfo(flGlyph, QTransform)\n  flGlyphInfo(fgSymbol, fgGlyph, fgFont)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flGlyphInfo')

    def applyTransform(self) -> Any:
        'applyTransform()'
        _unavailable('fontlab.flGlyphInfo.applyTransform')

    def applyTransformTo(self, type: int) -> Any:
        'applyTransformTo(uint type)'
        _unavailable('fontlab.flGlyphInfo.applyTransformTo')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flGlyphInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flGlyphInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flGlyphInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flGlyphInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flGlyphInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flGlyphInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flGlyphInfo.cloneObject')

    def createBoundingBox(self) -> Any:
        'createBoundingBox()'
        _unavailable('fontlab.flGlyphInfo.createBoundingBox')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flGlyphInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flGlyphInfo.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flGlyphInfo.flag')

    def getNearbyContours(self, arg0: QPointF, max_dist: float, exclude_attr: str) -> Any:
        'list(flContourInfo) getNearbyContours(QPointF, double max_dist, QString exclude_attr)'
        _unavailable('fontlab.flGlyphInfo.getNearbyContours')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flGlyphInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flGlyphInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flGlyphInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flGlyphInfo.getPropertyInt')

    def getTopHitShape(self, arg0: QPointF) -> Any:
        'flShapeInfo/Nothing getTopHitShape(QPointF)'
        _unavailable('fontlab.flGlyphInfo.getTopHitShape')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flGlyphInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flGlyphInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flGlyphInfo.historyStates')

    def hitToShape(self, arg0: QPointF) -> bool:
        'bool hitToShape(QPointF)'
        _unavailable('fontlab.flGlyphInfo.hitToShape')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flGlyphInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flGlyphInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flGlyphInfo.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flGlyphInfo.isEqual')

    def kerningOffset(self, useKerning: bool) -> float:
        'double kerningOffset(bool useKerning)'
        _unavailable('fontlab.flGlyphInfo.kerningOffset')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flGlyphInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flGlyphInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flGlyphInfo.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flGlyphInfo.restoreHistoryState')

    def setBoundAscender(self, double: Any) -> Any:
        'setBoundAscender(double)'
        _unavailable('fontlab.flGlyphInfo.setBoundAscender')

    def setBoundDescender(self, double: Any) -> Any:
        'setBoundDescender(double)'
        _unavailable('fontlab.flGlyphInfo.setBoundDescender')

    def setBoundLeft(self, double: Any) -> Any:
        'setBoundLeft(double)'
        _unavailable('fontlab.flGlyphInfo.setBoundLeft')

    def setBoundRight(self, double: Any) -> Any:
        'setBoundRight(double)'
        _unavailable('fontlab.flGlyphInfo.setBoundRight')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flGlyphInfo.setFlag')

    def setGlyphScale(self, *args: Any, **kwargs: Any) -> Any:
        'setGlyphScale(double, double)'
        _unavailable('fontlab.flGlyphInfo.setGlyphScale')

    def setKerningOffset(self, offs: float) -> Any:
        'setKerningOffset(double offs)'
        _unavailable('fontlab.flGlyphInfo.setKerningOffset')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flGlyphInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flGlyphInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flGlyphInfo.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flGlyphInfo.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flGlyphInfo.update')

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
    'flGraphicsInfo representation\n\nConstructors:\n  flGraphicsInfo()\n  flGraphicsInfo(flObject)\n  flGraphicsInfo(flGraphicsInfo)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flGraphicsInfo')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flGraphicsInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flGraphicsInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flGraphicsInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flGraphicsInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flGraphicsInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flGraphicsInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flGraphicsInfo.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flGraphicsInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flGraphicsInfo.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flGraphicsInfo.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flGraphicsInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flGraphicsInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flGraphicsInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flGraphicsInfo.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flGraphicsInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flGraphicsInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flGraphicsInfo.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flGraphicsInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flGraphicsInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flGraphicsInfo.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flGraphicsInfo.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flGraphicsInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flGraphicsInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flGraphicsInfo.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flGraphicsInfo.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flGraphicsInfo.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flGraphicsInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flGraphicsInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flGraphicsInfo.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flGraphicsInfo.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flGraphicsInfo.update')

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
    'flGuideLine representation\n\nConstructors:\n  flGuideLine()\n  flGuideLine(flObject)\n  flGuideLine(flGuideLine)\n  flGuideLine(double angle, QPointF canvas_point, uint=flSnaps::Vector, SnapObjectsStyle=gsPageGuideline)\n  flGuideLine(QLineF line, uint=flSnaps::Vector, SnapObjectsStyle=gsPageGuideline)\n  flGuideLine(QPointF center, QPointF vector_point, uint =flSnaps::Vector, SnapObjectsStyle=gsPageGuideline)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flGuideLine')

    def applyTransform(self, arg0: QTransform) -> None:
        'void applyTransform(QTransform)'
        _unavailable('fontlab.flGuideLine.applyTransform')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flGuideLine.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flGuideLine.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flGuideLine.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flGuideLine.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flGuideLine.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flGuideLine.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flGuideLine.cloneObject')

    def counterPaper(self) -> int:
        'int counterPaper()'
        _unavailable('fontlab.flGuideLine.counterPaper')

    def createInstance(self) -> flGuideLine:
        'flGuideLine createInstance()'
        _unavailable('fontlab.flGuideLine.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flGuideLine.createObject')

    def createPowerGuides(self, arg0: fgFont, arg1: flLayer, horizontal: bool, vertical: bool, use_glyph_guides: Any = ...) -> bool:
        'bool createPowerGuides(fgFont, flLayer, bool horizontal, bool vertical, bool diagonal[, bool use_glyph_guides=true[, bool use_font_guides = true]])'
        _unavailable('fontlab.flGuideLine.createPowerGuides')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flGuideLine.currentHistoryState')

    def disconnectFromContour(self) -> Any:
        'disconnectFromContour()'
        _unavailable('fontlab.flGuideLine.disconnectFromContour')

    def distanceTo(self, arg0: QPointF, mode: int) -> float:
        'double distanceTo(QPointF, uint mode)'
        _unavailable('fontlab.flGuideLine.distanceTo')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flGuideLine.flag')

    def getHashCode(self, arg0: QPointF, angle: float) -> int:
        'long getHashCode(QPointF, double angle)'
        _unavailable('fontlab.flGuideLine.getHashCode')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flGuideLine.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flGuideLine.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flGuideLine.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flGuideLine.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flGuideLine.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flGuideLine.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flGuideLine.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flGuideLine.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flGuideLine.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flGuideLine.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flGuideLine.isEqual')

    def isGuideLine(self, arg0: flObject) -> bool:
        'bool isGuideLine(flObject)'
        _unavailable('fontlab.flGuideLine.isGuideLine')

    def isHorizontal(self, a: Any = ...) -> bool:
        'bool isHorizontal([double a=1])'
        _unavailable('fontlab.flGuideLine.isHorizontal')

    def isSnapLine(self, arg0: flObject) -> bool:
        'bool isSnapLine(flObject)'
        _unavailable('fontlab.flGuideLine.isSnapLine')

    def isVertical(self, a: Any = ...) -> bool:
        'bool isVertical([double a=1])'
        _unavailable('fontlab.flGuideLine.isVertical')

    def offsetTo(self, arg0: QPointF, mode: int) -> QPointF:
        'QPointF offsetTo(QPointF, uint mode)'
        _unavailable('fontlab.flGuideLine.offsetTo')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flGuideLine.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flGuideLine.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flGuideLine.removeChild')

    def reset(self) -> Any:
        'reset()'
        _unavailable('fontlab.flGuideLine.reset')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flGuideLine.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flGuideLine.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flGuideLine.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flGuideLine.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flGuideLine.setPropertyInt')

    def setSnapFlag(self, role: int, snapFlags: int) -> Any:
        'setSnapFlag(uint role, uint snapFlags)'
        _unavailable('fontlab.flGuideLine.setSnapFlag')

    def setSnapFlagValue(self, role: int, bool: Any) -> Any:
        'setSnapFlagValue(uint role, bool)'
        _unavailable('fontlab.flGuideLine.setSnapFlagValue')

    def snapFlag(self, role: int) -> int:
        'uint snapFlag(uint role)'
        _unavailable('fontlab.flGuideLine.snapFlag')

    def sortGuideLines(self, ascending: Any = ...) -> Any:
        'list(flGuideLine) sortGuideLines(list(flGuideLine)[, bool ascending = true])'
        _unavailable('fontlab.flGuideLine.sortGuideLines')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flGuideLine.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flGuideLine.update')

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
    'flHintingParameters representation\n\nConstructors:\n  flHintingParameters() - default\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flHintingParameters')

    def init(self) -> Any:
        'init()'
        _unavailable('fontlab.flHintingParameters.init')

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
    'flInstance representation\n\nConstructors:\n  flInstance()\n  flInstance(string name, string tsn, flLocation location)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flInstance')

    def autoSGN(self, *args: Any, **kwargs: Any) -> Any:
        'string autoSGN(const string &tfn)'
        _unavailable('fontlab.flInstance.autoSGN')

    def autoSLV(self) -> int:
        'int autoSLV()'
        _unavailable('fontlab.flInstance.autoSLV')

    def autoTSN(self) -> Any:
        'string autoTSN()'
        _unavailable('fontlab.flInstance.autoTSN')

    def setSLV(self, bold: bool, italic: bool) -> Any:
        'setSLV(bool bold, bool italic)'
        _unavailable('fontlab.flInstance.setSLV')

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
    'flItems representation\n\nConstructors:\n  flItems()\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flItems')

    def appendRecentFile(self, arg0: str, file_name: str) -> Any:
        'appendRecentFile(QString, QString file_name)'
        _unavailable('fontlab.flItems.appendRecentFile')

    def buildRecentList(self, arg0: str) -> Any:
        'QStringList/Nothing buildRecentList(QString)'
        _unavailable('fontlab.flItems.buildRecentList')

    def clearRecentFiles(self, arg0: str) -> Any:
        'clearRecentFiles(QString )'
        _unavailable('fontlab.flItems.clearRecentFiles')

    def createObject(self, type: int, key: flObject) -> flObject:
        'flObject createObject(int type, flObject key)'
        _unavailable('fontlab.flItems.createObject')

    def getCursor(self, CursorId: Any) -> QCursor:
        'QCursor getCursor(CursorId)'
        _unavailable('fontlab.flItems.getCursor')

    def getCursorId(self, arg0: str, hot_x: int, hot_y: int) -> Any:
        'CursorId getCursorId(QString, int hot_x, int hot_y)'
        _unavailable('fontlab.flItems.getCursorId')

    def guidelinesEditingEnabled(self) -> bool:
        'bool guidelinesEditingEnabled()'
        _unavailable('fontlab.flItems.guidelinesEditingEnabled')

    def init(self) -> Any:
        'init()'
        _unavailable('fontlab.flItems.init')

    def instance(self) -> flItems:
        'flItems instance()'
        _unavailable('fontlab.flItems.instance')

    def notifyActivateGlyph(self, arg0: flGlyphInfo) -> Any:
        'notifyActivateGlyph(flGlyphInfo)'
        _unavailable('fontlab.flItems.notifyActivateGlyph')

    def notifyAnchorsChanged(self) -> Any:
        'notifyAnchorsChanged()'
        _unavailable('fontlab.flItems.notifyAnchorsChanged')

    def notifyApplyTranformFrame(self) -> Any:
        'notifyApplyTranformFrame()'
        _unavailable('fontlab.flItems.notifyApplyTranformFrame')

    def notifyAuditHovered(self, id: int) -> Any:
        'notifyAuditHovered(uint id)'
        _unavailable('fontlab.flItems.notifyAuditHovered')

    def notifyAutoShapseChanges(self, arg0: flLayer) -> Any:
        'notifyAutoShapseChanges(flLayer)'
        _unavailable('fontlab.flItems.notifyAutoShapseChanges')

    def notifyAvailableToSelectNodes(self, *args: Any, **kwargs: Any) -> Any:
        'notifyAvailableToSelectNodes( list(list(flNodeInfo)) )'
        _unavailable('fontlab.flItems.notifyAvailableToSelectNodes')

    def notifyBrushModeSelected(self, smart: int) -> Any:
        'notifyBrushModeSelected(int smart)'
        _unavailable('fontlab.flItems.notifyBrushModeSelected')

    def notifyBrushSelected(self, PaintBrush: Any) -> Any:
        'notifyBrushSelected(PaintBrush)'
        _unavailable('fontlab.flItems.notifyBrushSelected')

    def notifyBrushSet(self) -> Any:
        'notifyBrushSet()'
        _unavailable('fontlab.flItems.notifyBrushSet')

    def notifyCancelTranformFrame(self) -> Any:
        'notifyCancelTranformFrame()'
        _unavailable('fontlab.flItems.notifyCancelTranformFrame')

    def notifyCanvasAttached(self, arg0: flCanvas) -> Any:
        'notifyCanvasAttached(flCanvas)'
        _unavailable('fontlab.flItems.notifyCanvasAttached')

    def notifyCanvasEnterFocus(self, arg0: flCanvas) -> Any:
        'notifyCanvasEnterFocus(flCanvas)'
        _unavailable('fontlab.flItems.notifyCanvasEnterFocus')

    def notifyCanvasLeaveFocus(self, arg0: flCanvas) -> Any:
        'notifyCanvasLeaveFocus(flCanvas)'
        _unavailable('fontlab.flItems.notifyCanvasLeaveFocus')

    def notifyCanvasRemoved(self, arg0: flCanvas) -> Any:
        'notifyCanvasRemoved(flCanvas)'
        _unavailable('fontlab.flItems.notifyCanvasRemoved')

    def notifyChangesApplied(self, recursive: Any = ...) -> Any:
        'notifyChangesApplied([QString title, flObject object / list(flObject)[, bool recursive=false]])'
        _unavailable('fontlab.flItems.notifyChangesApplied')

    def notifyClipboardChanged(self) -> Any:
        'notifyClipboardChanged()'
        _unavailable('fontlab.flItems.notifyClipboardChanged')

    def notifyColorSet(self, arg0: QColor, b: bool) -> Any:
        'notifyColorSet(QColor, bool b)'
        _unavailable('fontlab.flItems.notifyColorSet')

    def notifyCommandSelected(self) -> Any:
        'notifyCommandSelected()'
        _unavailable('fontlab.flItems.notifyCommandSelected')

    def notifyCurrentPaperChanged(self, arg0: flPaper) -> Any:
        'notifyCurrentPaperChanged(flPaper)'
        _unavailable('fontlab.flItems.notifyCurrentPaperChanged')

    def notifyDropDone(self, canvas: flCanvas) -> Any:
        'notifyDropDone(flCanvas& canvas)'
        _unavailable('fontlab.flItems.notifyDropDone')

    def notifyEditActionFinished(self) -> Any:
        'notifyEditActionFinished()'
        _unavailable('fontlab.flItems.notifyEditActionFinished')

    def notifyEditActionStarted(self) -> Any:
        'notifyEditActionStarted()'
        _unavailable('fontlab.flItems.notifyEditActionStarted')

    def notifyEditModeChanged(self, mode: Any) -> Any:
        'notifyEditModeChanged(EditMode mode)'
        _unavailable('fontlab.flItems.notifyEditModeChanged')

    def notifyEditingChanged(self, arg0: flAbstractEditor) -> Any:
        'notifyEditingChanged(flAbstractEditor)'
        _unavailable('fontlab.flItems.notifyEditingChanged')

    def notifyEditingFinished(self) -> Any:
        'notifyEditingFinished()'
        _unavailable('fontlab.flItems.notifyEditingFinished')

    def notifyFeaturesChanged(self, package_id: int, binary: bool) -> Any:
        'notifyFeaturesChanged(uint package_id, bool binary)'
        _unavailable('fontlab.flItems.notifyFeaturesChanged')

    def notifyFontPanelActivated(self, b: bool) -> Any:
        'notifyFontPanelActivated(bool b)'
        _unavailable('fontlab.flItems.notifyFontPanelActivated')

    def notifyFontSelected(self, *args: Any, **kwargs: Any) -> Any:
        'notifyFontSelected(uint id);'
        _unavailable('fontlab.flItems.notifyFontSelected')

    def notifyFrameSelected(self, *args: Any, **kwargs: Any) -> Any:
        'notifyFrameSelected(list(flNodeInfo))'
        _unavailable('fontlab.flItems.notifyFrameSelected')

    def notifyGalleryChanged(self, arg0: flObject) -> Any:
        'notifyGalleryChanged(flObject)'
        _unavailable('fontlab.flItems.notifyGalleryChanged')

    def notifyGlyphActivated(self, arg0: flGlyphInfo) -> Any:
        'notifyGlyphActivated(flGlyphInfo)'
        _unavailable('fontlab.flItems.notifyGlyphActivated')

    def notifyGlyphDeactivated(self) -> Any:
        'notifyGlyphDeactivated()'
        _unavailable('fontlab.flItems.notifyGlyphDeactivated')

    def notifyGlyphDoubleClick(self, arg0: flGlyphInfo) -> Any:
        'notifyGlyphDoubleClick(flGlyphInfo)'
        _unavailable('fontlab.flItems.notifyGlyphDoubleClick')

    def notifyGlyphIdSelected(self, packageId: int, glyphId: int, replace: bool) -> Any:
        'notifyGlyphIdSelected(uint packageId, uint glyphId, bool replace)'
        _unavailable('fontlab.flItems.notifyGlyphIdSelected')

    def notifyGlyphMaximized(self, arg0: flGlyphInfo) -> Any:
        'notifyGlyphMaximized(flGlyphInfo)'
        _unavailable('fontlab.flItems.notifyGlyphMaximized')

    def notifyGlyphPinPointChanged(self, pin_point: Any = ...) -> Any:
        'notifyGlyphPinPointChanged([flPinPoint pin_point = flnull[, flGlyphInfo glyph_info = flnull]])'
        _unavailable('fontlab.flItems.notifyGlyphPinPointChanged')

    def notifyGlyphPinPointCreated(self, arg0: flGlyphInfo) -> Any:
        'notifyGlyphPinPointCreated(flGlyphInfo)'
        _unavailable('fontlab.flItems.notifyGlyphPinPointCreated')

    def notifyGlyphUpdated(self, packageId: int, glyphId: int) -> Any:
        'notifyGlyphUpdated(uint packageId, uint glyphId)'
        _unavailable('fontlab.flItems.notifyGlyphUpdated')

    def notifyGlyphWindowInactive(self) -> Any:
        'notifyGlyphWindowInactive()'
        _unavailable('fontlab.flItems.notifyGlyphWindowInactive')

    def notifyGlyphsUpdated(self, packageId: int, glyphIds: set[Any]) -> Any:
        'notifyGlyphsUpdated(uint packageId, QSet<uint32_t> glyphIds)'
        _unavailable('fontlab.flItems.notifyGlyphsUpdated')

    def notifyGraphEdgeSelectionChanged(self, arg0: flObject) -> Any:
        'notifyGraphEdgeSelectionChanged(flObject)'
        _unavailable('fontlab.flItems.notifyGraphEdgeSelectionChanged')

    def notifyGuidelinesChanged(self, arg0: flCanvas) -> Any:
        'notifyGuidelinesChanged(flCanvas)'
        _unavailable('fontlab.flItems.notifyGuidelinesChanged')

    def notifyGuidelinesSelected(self, *args: Any, **kwargs: Any) -> Any:
        'notifyGuidelinesSelected(list(flGuideLine))'
        _unavailable('fontlab.flItems.notifyGuidelinesSelected')

    def notifyHidePanels(self) -> Any:
        'notifyHidePanels()'
        _unavailable('fontlab.flItems.notifyHidePanels')

    def notifyHistoryChanged(self) -> Any:
        'notifyHistoryChanged()'
        _unavailable('fontlab.flItems.notifyHistoryChanged')

    def notifyKeyHash(self) -> Any:
        'notifyKeyHash()'
        _unavailable('fontlab.flItems.notifyKeyHash')

    def notifyKeyRepeat(self, key: int) -> Any:
        'notifyKeyRepeat(int key)'
        _unavailable('fontlab.flItems.notifyKeyRepeat')

    def notifyKeySlash(self) -> Any:
        'notifyKeySlash()'
        _unavailable('fontlab.flItems.notifyKeySlash')

    def notifyLayerActivated(self, arg0: flLayer) -> Any:
        'notifyLayerActivated(flLayer)'
        _unavailable('fontlab.flItems.notifyLayerActivated')

    def notifyModelChanged(self) -> Any:
        'notifyModelChanged()'
        _unavailable('fontlab.flItems.notifyModelChanged')

    def notifyNodeChanged(self, arg0: flNodeInfo) -> Any:
        'notifyNodeChanged(flNodeInfo)'
        _unavailable('fontlab.flItems.notifyNodeChanged')

    def notifyNodesSelected(self, *args: Any, **kwargs: Any) -> Any:
        'notifyNodesSelected(list(flNodeInfo))'
        _unavailable('fontlab.flItems.notifyNodesSelected')

    def notifyPackageAdded(self, arg0: flPackage) -> Any:
        'notifyPackageAdded(flPackage)'
        _unavailable('fontlab.flItems.notifyPackageAdded')

    def notifyPackageClosed(self, arg0: flPackage) -> Any:
        'notifyPackageClosed(flPackage)'
        _unavailable('fontlab.flItems.notifyPackageClosed')

    def notifyPackageContentUpdated(self, id: int) -> Any:
        'notifyPackageContentUpdated(uint id)'
        _unavailable('fontlab.flItems.notifyPackageContentUpdated')

    def notifyPackageReaded(self, arg0: flPackage) -> Any:
        'notifyPackageReaded(flPackage)'
        _unavailable('fontlab.flItems.notifyPackageReaded')

    def notifyPackageRemoved(self, arg0: flPackage) -> Any:
        'notifyPackageRemoved(flPackage)'
        _unavailable('fontlab.flItems.notifyPackageRemoved')

    def notifyPackageUpdated(self, id: Any) -> Any:
        'notifyPackageUpdated(flPackage | uint id)'
        _unavailable('fontlab.flItems.notifyPackageUpdated')

    def notifyPackagesRemoved(self, *args: Any, **kwargs: Any) -> Any:
        'notifyPackagesRemoved(list(flObject))'
        _unavailable('fontlab.flItems.notifyPackagesRemoved')

    def notifyPackagesUpdated(self) -> Any:
        'notifyPackagesUpdated()'
        _unavailable('fontlab.flItems.notifyPackagesUpdated')

    def notifyPinPointChanged(self, pin_point: Any = ...) -> Any:
        'notifyPinPointChanged([flPinPoint pin_point = flnull[, flShapeInfo shape_info = flnull]])'
        _unavailable('fontlab.flItems.notifyPinPointChanged')

    def notifyPinPointCreated(self, arg0: flShapeInfo) -> Any:
        'notifyPinPointCreated(flShapeInfo)'
        _unavailable('fontlab.flItems.notifyPinPointCreated')

    def notifyPinPointSelectionChanged(self) -> Any:
        'notifyPinPointSelectionChanged()'
        _unavailable('fontlab.flItems.notifyPinPointSelectionChanged')

    def notifyPinSelected(self, id: int) -> Any:
        'notifyPinSelected(uint id)'
        _unavailable('fontlab.flItems.notifyPinSelected')

    def notifyPreferencesChanged(self) -> Any:
        'notifyPreferencesChanged()'
        _unavailable('fontlab.flItems.notifyPreferencesChanged')

    def notifyProjectClosed(self) -> Any:
        'notifyProjectClosed()'
        _unavailable('fontlab.flItems.notifyProjectClosed')

    def notifyProjectReaded(self, file_name: str) -> Any:
        'notifyProjectReaded(QString file_name)'
        _unavailable('fontlab.flItems.notifyProjectReaded')

    def notifyProjectSaved(self, file_name: str) -> Any:
        'notifyProjectSaved(QString file_name)'
        _unavailable('fontlab.flItems.notifyProjectSaved')

    def notifyPropertiesChanged(self, arg0: flObject) -> Any:
        'notifyPropertiesChanged(flObject)'
        _unavailable('fontlab.flItems.notifyPropertiesChanged')

    def notifyRenderingBegin(self, info: str) -> Any:
        'notifyRenderingBegin(QString info)'
        _unavailable('fontlab.flItems.notifyRenderingBegin')

    def notifyRenderingFinished(self, success: bool) -> Any:
        'notifyRenderingFinished(bool success)'
        _unavailable('fontlab.flItems.notifyRenderingFinished')

    def notifyReplaceGlyphsByFgId(self, *args: Any, **kwargs: Any) -> Any:
        'notifyReplaceGlyphsByFgId(list(unsigned long), int replace_count)'
        _unavailable('fontlab.flItems.notifyReplaceGlyphsByFgId')

    def notifyRequestChangeCurrentClipboard(self, xml: str) -> Any:
        'notifyRequestChangeCurrentClipboard(QString xml)'
        _unavailable('fontlab.flItems.notifyRequestChangeCurrentClipboard')

    def notifyRequestNewProject(self) -> Any:
        'notifyRequestNewProject()'
        _unavailable('fontlab.flItems.notifyRequestNewProject')

    def notifyRequestOpenProject(self, file_name: str) -> Any:
        'notifyRequestOpenProject(QString file_name)'
        _unavailable('fontlab.flItems.notifyRequestOpenProject')

    def notifyRequestPasteAction(self) -> Any:
        'notifyRequestPasteAction()'
        _unavailable('fontlab.flItems.notifyRequestPasteAction')

    def notifyRequestShowWelcome(self) -> Any:
        'notifyRequestShowWelcome()'
        _unavailable('fontlab.flItems.notifyRequestShowWelcome')

    def notifyRequestShowWorkspace(self) -> Any:
        'notifyRequestShowWorkspace()'
        _unavailable('fontlab.flItems.notifyRequestShowWorkspace')

    def notifySCVItemsChanged(self) -> Any:
        'notifySCVItemsChanged()'
        _unavailable('fontlab.flItems.notifySCVItemsChanged')

    def notifyScrollToGlyph(self, arg0: flGlyphInfo) -> Any:
        'notifyScrollToGlyph(flGlyphInfo)'
        _unavailable('fontlab.flItems.notifyScrollToGlyph')

    def notifySelectionChanged(self) -> Any:
        'notifySelectionChanged()'
        _unavailable('fontlab.flItems.notifySelectionChanged')

    def notifyShapeActivated(self, arg0: flShapeInfo) -> Any:
        'notifyShapeActivated(flShapeInfo)'
        _unavailable('fontlab.flItems.notifyShapeActivated')

    def notifyShapeDeactivated(self) -> Any:
        'notifyShapeDeactivated()'
        _unavailable('fontlab.flItems.notifyShapeDeactivated')

    def notifyShowPanels(self) -> Any:
        'notifyShowPanels()'
        _unavailable('fontlab.flItems.notifyShowPanels')

    def notifySnapLineChanged(self, arg0: flGuideLine) -> Any:
        'notifySnapLineChanged(flGuideLine)'
        _unavailable('fontlab.flItems.notifySnapLineChanged')

    def notifySnapLinesChanged(self, *args: Any, **kwargs: Any) -> Any:
        'notifySnapLinesChanged(list(flGuideLine))'
        _unavailable('fontlab.flItems.notifySnapLinesChanged')

    def notifyStaplerPreviewEnabled(self, enbl: bool) -> Any:
        'notifyStaplerPreviewEnabled(bool enbl)'
        _unavailable('fontlab.flItems.notifyStaplerPreviewEnabled')

    def notifyStickerCreated(self) -> Any:
        'notifyStickerCreated()'
        _unavailable('fontlab.flItems.notifyStickerCreated')

    def notifyStopButtonClicked(self) -> Any:
        'notifyStopButtonClicked()'
        _unavailable('fontlab.flItems.notifyStopButtonClicked')

    def notifyTextBlockAdded(self, arg0: flTextBlock) -> Any:
        'notifyTextBlockAdded(flTextBlock)'
        _unavailable('fontlab.flItems.notifyTextBlockAdded')

    def notifyTextBlockItemActivated(self, check_tools: Any = ...) -> Any:
        'notifyTextBlockItemActivated(flTextBlockItem[, bool check_tools = true])'
        _unavailable('fontlab.flItems.notifyTextBlockItemActivated')

    def notifyTextBlockItemChanged(self, arg0: flTextBlockItem) -> Any:
        'notifyTextBlockItemChanged(flTextBlockItem)'
        _unavailable('fontlab.flItems.notifyTextBlockItemChanged')

    def notifyTextBlockItemDeactivated(self, arg0: flTextBlockItem) -> Any:
        'notifyTextBlockItemDeactivated(flTextBlockItem)'
        _unavailable('fontlab.flItems.notifyTextBlockItemDeactivated')

    def notifyTextBlockItemMaximized(self, arg0: flTextBlockItem) -> Any:
        'notifyTextBlockItemMaximized(flTextBlockItem)'
        _unavailable('fontlab.flItems.notifyTextBlockItemMaximized')

    def notifyTextBlockItemNormalized(self, arg0: flTextBlockItem) -> Any:
        'notifyTextBlockItemNormalized(flTextBlockItem)'
        _unavailable('fontlab.flItems.notifyTextBlockItemNormalized')

    def notifyTextBlockItemsSelectionChanged(self, arg0: flCanvas) -> Any:
        'notifyTextBlockItemsSelectionChanged(flCanvas)'
        _unavailable('fontlab.flItems.notifyTextBlockItemsSelectionChanged')

    def notifyTextBlockRemoved(self, arg0: flTextBlock) -> Any:
        'notifyTextBlockRemoved(flTextBlock)'
        _unavailable('fontlab.flItems.notifyTextBlockRemoved')

    def notifyToolChanged(self, tool: flBasicTool) -> Any:
        'notifyToolChanged(flBasicTool& tool)'
        _unavailable('fontlab.flItems.notifyToolChanged')

    def notifyTransformDataChanged(self, TransformFrame: Any) -> Any:
        'notifyTransformDataChanged(TransformFrame)'
        _unavailable('fontlab.flItems.notifyTransformDataChanged')

    def notifyTransformFrameChanged(self, arg0: flObject) -> Any:
        'notifyTransformFrameChanged(flObject)'
        _unavailable('fontlab.flItems.notifyTransformFrameChanged')

    def notifyTransformFrameFinished(self, arg0: flObject) -> Any:
        'notifyTransformFrameFinished(flObject)'
        _unavailable('fontlab.flItems.notifyTransformFrameFinished')

    def notifyTransformFrameStarted(self, arg0: flObject) -> Any:
        'notifyTransformFrameStarted(flObject)'
        _unavailable('fontlab.flItems.notifyTransformFrameStarted')

    def notifyTransformStarted(self) -> Any:
        'notifyTransformStarted()'
        _unavailable('fontlab.flItems.notifyTransformStarted')

    def notifyUpdateHistory(self) -> Any:
        'notifyUpdateHistory()'
        _unavailable('fontlab.flItems.notifyUpdateHistory')

    def notifyUpdateStaplers(self) -> Any:
        'notifyUpdateStaplers()'
        _unavailable('fontlab.flItems.notifyUpdateStaplers')

    def notifyViewportChanged(self, old_viewport: QWidget, new_viewport: QWidget) -> Any:
        'notifyViewportChanged(QWidget* old_viewport, QWidget* new_viewport)'
        _unavailable('fontlab.flItems.notifyViewportChanged')

    def notifyWorkspaceClosed(self, arg0: flWorkspace) -> Any:
        'notifyWorkspaceClosed(flWorkspace)'
        _unavailable('fontlab.flItems.notifyWorkspaceClosed')

    def notifyWorkspaceHasChanges(self, c: bool) -> Any:
        'notifyWorkspaceHasChanges(bool c)'
        _unavailable('fontlab.flItems.notifyWorkspaceHasChanges')

    def notifyWorkspaceInitialized(self, arg0: flWorkspace) -> Any:
        'notifyWorkspaceInitialized(flWorkspace)'
        _unavailable('fontlab.flItems.notifyWorkspaceInitialized')

    def notifyZoomChanged(self, canvas: flCanvas) -> Any:
        'notifyZoomChanged(flCanvas& canvas)'
        _unavailable('fontlab.flItems.notifyZoomChanged')

    def requestActivateNodesTool(self) -> Any:
        'requestActivateNodesTool()'
        _unavailable('fontlab.flItems.requestActivateNodesTool')

    def requestActivateShapeTool(self) -> Any:
        'requestActivateShapeTool()'
        _unavailable('fontlab.flItems.requestActivateShapeTool')

    def requestActivateTransformTool(self) -> Any:
        'requestActivateTransformTool()'
        _unavailable('fontlab.flItems.requestActivateTransformTool')

    def requestCheckHistoryInitIndex(self, arg0: flGlyphInfo) -> Any:
        'requestCheckHistoryInitIndex(flGlyphInfo)'
        _unavailable('fontlab.flItems.requestCheckHistoryInitIndex')

    def requestContent(self, *args: Any, **kwargs: Any) -> Any:
        'requestContent(fgSymbolList characters, int cursorLocation'
        _unavailable('fontlab.flItems.requestContent')

    def requestFontInfoDlg(self) -> Any:
        'requestFontInfoDlg()'
        _unavailable('fontlab.flItems.requestFontInfoDlg')

    def requestGlyphActivate(self, pid: int, gid: int) -> Any:
        'requestGlyphActivate(uint pid, uint gid)'
        _unavailable('fontlab.flItems.requestGlyphActivate')

    def requestGlyphDeactivate(self) -> Any:
        'requestGlyphDeactivate()'
        _unavailable('fontlab.flItems.requestGlyphDeactivate')

    def requestGlyphReactivated(self) -> Any:
        'requestGlyphReactivated()'
        _unavailable('fontlab.flItems.requestGlyphReactivated')

    def requestLoadingFont(self, font_source: str) -> Any:
        'requestLoadingFont(QString font_source)'
        _unavailable('fontlab.flItems.requestLoadingFont')

    def requestPackageAcceptFonts(self, arg0: flPackage) -> Any:
        'requestPackageAcceptFonts(flPackage)'
        _unavailable('fontlab.flItems.requestPackageAcceptFonts')

    def requestPackageBorn(self, arg0: flPackage) -> Any:
        'requestPackageBorn(flPackage)'
        _unavailable('fontlab.flItems.requestPackageBorn')

    def requestPackagePostProcess(self, arg0: flPackage, encoding: str) -> Any:
        'requestPackagePostProcess(flPackage, QString encoding)'
        _unavailable('fontlab.flItems.requestPackagePostProcess')

    def requestPermissionsForDragGuidelineByNode(self, canvas_pos: QPointF, modifiers: int) -> bool:
        'bool requestPermissionsForDragGuidelineByNode(QPointF canvas_pos, uint modifiers)'
        _unavailable('fontlab.flItems.requestPermissionsForDragGuidelineByNode')

    def requestProgressMessage(self, message: str) -> Any:
        'requestProgressMessage(QString message)'
        _unavailable('fontlab.flItems.requestProgressMessage')

    def requestProgressRange(self, v: int) -> Any:
        'requestProgressRange(int v)'
        _unavailable('fontlab.flItems.requestProgressRange')

    def requestProgressShow(self, b: bool) -> Any:
        'requestProgressShow(bool b)'
        _unavailable('fontlab.flItems.requestProgressShow')

    def requestProgressValue(self, v: int) -> Any:
        'requestProgressValue(int v)'
        _unavailable('fontlab.flItems.requestProgressValue')

    def requestSaveBar(self, b: bool) -> Any:
        'requestSaveBar(bool b)'
        _unavailable('fontlab.flItems.requestSaveBar')

    def requestSaveBarValue(self, v: int) -> Any:
        'requestSaveBarValue(int v)'
        _unavailable('fontlab.flItems.requestSaveBarValue')

    def requestSubContent(self, *args: Any, **kwargs: Any) -> Any:
        'requestSubContent(fgSymbolList characters, int cursorLocation'
        _unavailable('fontlab.flItems.requestSubContent')

    def requestUpdateActiveShape(self, arg0: flShapeInfo) -> Any:
        'requestUpdateActiveShape(flShapeInfo)'
        _unavailable('fontlab.flItems.requestUpdateActiveShape')

    def resetToolCursor(self) -> Any:
        'resetToolCursor()'
        _unavailable('fontlab.flItems.resetToolCursor')

    def setCursor(self, *args: Any, **kwargs: Any) -> Any:
        'setCursor(CursorId cursor_id);'
        _unavailable('fontlab.flItems.setCursor')

    def setEllipseCurvature(self, d: float) -> Any:
        'setEllipseCurvature(double d)'
        _unavailable('fontlab.flItems.setEllipseCurvature')

    def setEllipseData(self, p0: QPointF, p1: QPointF) -> Any:
        'setEllipseData(QPointF p0, QPointF p1)'
        _unavailable('fontlab.flItems.setEllipseData')

    def setGuidelinesEditingEnabled(self, b: bool) -> Any:
        'setGuidelinesEditingEnabled(bool b)'
        _unavailable('fontlab.flItems.setGuidelinesEditingEnabled')

    def setMeterData(self, p0: QPointF, p1: QPointF) -> Any:
        'setMeterData(QPointF p0, QPointF p1)'
        _unavailable('fontlab.flItems.setMeterData')

    def setParameterName(self, arg0: flObject, arg1: str) -> Any:
        'setParameterName(flObject, QString)'
        _unavailable('fontlab.flItems.setParameterName')

    def setTransformation(self, code: int, value: QPointF) -> Any:
        'setTransformation(int code, QPointF value)'
        _unavailable('fontlab.flItems.setTransformation')

    def shapeBuilders(self) -> Any:
        'list(flObject) shapeBuilders()'
        _unavailable('fontlab.flItems.shapeBuilders')

    def strToType(self, arg0: str) -> int:
        'int strToType(QString)'
        _unavailable('fontlab.flItems.strToType')

    def typeToStr(self, type: int) -> str:
        'QString typeToStr(int type)'
        _unavailable('fontlab.flItems.typeToStr')

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
    "flLayer representation\n\nConstructors:\n  flLayer()\n  flLayer(flObject)\n  flLayer(flGlyph)\n  flLayer('title')\n\nNative bases: object"
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flLayer')

    def addAnchor(self, arg0: flPinPoint) -> Any:
        'addAnchor(flPinPoint)'
        _unavailable('fontlab.flLayer.addAnchor')

    def addComponent(self, component: flComponent) -> Any:
        'addComponent(flComponent component)'
        _unavailable('fontlab.flLayer.addComponent')

    def addShape(self, arg0: flShape) -> flShape:
        'flShape addShape(flShape)'
        _unavailable('fontlab.flLayer.addShape')

    def addShapes(self, *args: Any, **kwargs: Any) -> Any:
        'addShapes(list(flShape))'
        _unavailable('fontlab.flLayer.addShapes')

    def appendGuidelines(self, *args: Any, **kwargs: Any) -> Any:
        'appendGuidelines(list(flGuideLine))'
        _unavailable('fontlab.flLayer.appendGuidelines')

    def applyTransform(self, *args: Any, **kwargs: Any) -> Any:
        'applyTransform([QTransform transform])'
        _unavailable('fontlab.flLayer.applyTransform')

    def assignFgLayer(self, arg0: fgLayer, doGuides: bool, doHints: bool, doAnchors: bool, doShapes: bool, doTTH: bool) -> Any:
        'assignFgLayer(fgLayer, bool doGuides, bool doHints, bool doAnchors, bool doShapes, bool doTTH)'
        _unavailable('fontlab.flLayer.assignFgLayer')

    def assignStyle(self, layer: flLayer) -> Any:
        'assignStyle(flLayer layer)'
        _unavailable('fontlab.flLayer.assignStyle')

    def autohint(self) -> bool:
        'bool autohint()'
        _unavailable('fontlab.flLayer.autohint')

    def bindDependencies(self) -> Any:
        'bindDependencies()'
        _unavailable('fontlab.flLayer.bindDependencies')

    def buildAuto(self) -> bool:
        'bool buildAuto()'
        _unavailable('fontlab.flLayer.buildAuto')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flLayer.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flLayer.checkInitHistoryState')

    def checkTags(self, glyph_tags: set[str], item_tags: str) -> bool:
        'bool checkTags(QSet<QString> glyph_tags, QString item_tags)'
        _unavailable('fontlab.flLayer.checkTags')

    def cleanEmptyShapes(self) -> Any:
        'cleanEmptyShapes()'
        _unavailable('fontlab.flLayer.cleanEmptyShapes')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flLayer.clearAboveHistory')

    def clearAnchors(self) -> Any:
        'clearAnchors()'
        _unavailable('fontlab.flLayer.clearAnchors')

    def clearAudit(self) -> None:
        'void clearAudit()'
        _unavailable('fontlab.flLayer.clearAudit')

    def clearComponents(self) -> Any:
        'clearComponents()'
        _unavailable('fontlab.flLayer.clearComponents')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flLayer.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flLayer.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flLayer.clone')

    def cloneCustom(self, *args: Any, **kwargs: Any) -> Any:
        '(flLayer, list(flObject)) cloneCustom(uint)'
        _unavailable('fontlab.flLayer.cloneCustom')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flLayer.cloneObject')

    def compare(self, layer: flLayer, error: float) -> bool:
        'bool compare(flLayer layer, double error)'
        _unavailable('fontlab.flLayer.compare')

    def compoundMakeSelected(self, set_active: bool, process_all: bool) -> bool:
        'bool compoundMakeSelected(bool set_active, bool process_all)'
        _unavailable('fontlab.flLayer.compoundMakeSelected')

    def compoundMakeSelectedToShapes(self, set_active: Any = ...) -> bool:
        'bool compoundMakeSelectedToShapes([bool set_active =true])'
        _unavailable('fontlab.flLayer.compoundMakeSelectedToShapes')

    def contourRect(self) -> QRectF:
        'QRectF contourRect()'
        _unavailable('fontlab.flLayer.contourRect')

    def createAnchor(self, name: Any, p: QPointF, location: int) -> flPinPoint:
        'flPinPoint createAnchor(string name, QPointF p, int location)'
        _unavailable('fontlab.flLayer.createAnchor')

    def createInstance(self, *args: Any, **kwargs: Any) -> Any:
        'Native fontlab.flLayer.createInstance; argument details are not documented.'
        _unavailable('fontlab.flLayer.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flLayer.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flLayer.currentHistoryState')

    def deactivateAllShapes(self) -> Any:
        'deactivateAllShapes()'
        _unavailable('fontlab.flLayer.deactivateAllShapes')

    def fillFgAnchors(self, arg0: fgLayer) -> Any:
        'fillFgAnchors(fgLayer)'
        _unavailable('fontlab.flLayer.fillFgAnchors')

    def fillFgGuides(self, arg0: fgLayer) -> Any:
        'fillFgGuides(fgLayer)'
        _unavailable('fontlab.flLayer.fillFgGuides')

    def findAnchor(self, name: str) -> flPinPoint:
        'flPinPoint findAnchor(QString name)'
        _unavailable('fontlab.flLayer.findAnchor')

    def findNearestNode(self, *args: Any, **kwargs: Any) -> Any:
        '(flShape, flNode best_node, double maxd) findNearestNode(QPointF, flNode::NodeType node_type, double maxd)'
        _unavailable('fontlab.flLayer.findNearestNode')

    def findNode(self, *args: Any, **kwargs: Any) -> Any:
        '(flNode, QPointF)/Nothing findNode(string name)'
        _unavailable('fontlab.flLayer.findNode')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flLayer.flag')

    def getActiveComposite(self) -> Any:
        'flShape/Nothing getActiveComposite()'
        _unavailable('fontlab.flLayer.getActiveComposite')

    def getActiveShape(self, *args: Any, **kwargs: Any) -> Any:
        '(flShape, QTransform)/Nothing getActiveShape([bool = true])'
        _unavailable('fontlab.flLayer.getActiveShape')

    def getAuditInfo(self) -> Any:
        'list(flAuditInfo) getAuditInfo()'
        _unavailable('fontlab.flLayer.getAuditInfo')

    def getContours(self) -> Any:
        'list(flContour) getContours()'
        _unavailable('fontlab.flLayer.getContours')

    def getImgLayer(self, create: bool) -> flLayer:
        'flLayer getImgLayer(bool create)'
        _unavailable('fontlab.flLayer.getImgLayer')

    def getMaskLayer(self, create: bool) -> flLayer:
        'flLayer getMaskLayer(bool create)'
        _unavailable('fontlab.flLayer.getMaskLayer')

    def getMasterPosition(self) -> Any:
        'QMap<QString, double>/Nothing getMasterPosition()'
        _unavailable('fontlab.flLayer.getMasterPosition')

    def getOwnerComposite(self, *args: Any, **kwargs: Any) -> Any:
        'flShapeInfo getOwnerComposite(flShape, QTransform) / flShapeData getOwnerComposite(flShape)'
        _unavailable('fontlab.flLayer.getOwnerComposite')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flLayer.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flLayer.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flLayer.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flLayer.getPropertyInt')

    def getSelected(self, SelectionMode: Any) -> Any:
        'list(flContour)/Nothing getSelected(SelectionMode)'
        _unavailable('fontlab.flLayer.getSelected')

    def getShapes(self, shape_type: Any) -> Any:
        'list(flShape) getShapes(ShapeType shape_type)'
        _unavailable('fontlab.flLayer.getShapes')

    def getTthCode(self, fg_layer: fgLayer, itr: fgTTInterpreter) -> bool:
        'bool getTthCode(fgLayer fg_layer, fgTTInterpreter itr)'
        _unavailable('fontlab.flLayer.getTthCode')

    def getTthData(self, fg_layer: fgLayer, itr: fgTTInterpreter) -> Any:
        'list(bytes) / Nothing getTthData(fgLayer fg_layer, fgTTInterpreter itr)'
        _unavailable('fontlab.flLayer.getTthData')

    def getTthProgram(self, itr: fgTTInterpreter) -> str:
        'QString getTthProgram(fgTTInterpreter itr)'
        _unavailable('fontlab.flLayer.getTthProgram')

    def goDown(self, arg0: flShape) -> bool:
        'bool goDown(flShape)'
        _unavailable('fontlab.flLayer.goDown')

    def goUp(self, arg0: flShape) -> bool:
        'bool goUp(flShape)'
        _unavailable('fontlab.flLayer.goUp')

    def hasFontAudit(self) -> bool:
        'bool hasFontAudit()'
        _unavailable('fontlab.flLayer.hasFontAudit')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flLayer.hasHistoryState')

    def hasShape(self, arg0: flShape) -> bool:
        'bool hasShape(flShape)'
        _unavailable('fontlab.flLayer.hasShape')

    def hasShapeData(self, arg0: flShapeData) -> bool:
        'bool hasShapeData(flShapeData)'
        _unavailable('fontlab.flLayer.hasShapeData')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flLayer.haveObject')

    def haveSelected(self, SelectionMode: Any) -> bool:
        'bool haveSelected(SelectionMode)'
        _unavailable('fontlab.flLayer.haveSelected')

    def hints2links(self) -> bool:
        'bool hints2links()'
        _unavailable('fontlab.flLayer.hints2links')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flLayer.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flLayer.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flLayer.initialHistoryState')

    def inkBox(self, tx: Any = ...) -> QRectF:
        'QRectF inkBox([QTransform tx = QTransform()])'
        _unavailable('fontlab.flLayer.inkBox')

    def insertShape(self, index: int, shape: flShape) -> flShape:
        'flShape insertShape(int index, flShape shape)'
        _unavailable('fontlab.flLayer.insertShape')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flLayer.instanceType')

    def isBack(self, arg0: flShape) -> bool:
        'bool isBack(flShape)'
        _unavailable('fontlab.flLayer.isBack')

    def isCompatible(self, arg0: flLayer, strong: bool) -> bool:
        'bool isCompatible(flLayer, bool strong)'
        _unavailable('fontlab.flLayer.isCompatible')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flLayer.isEqual')

    def isFront(self, arg0: flShape) -> bool:
        'bool isFront(flShape)'
        _unavailable('fontlab.flLayer.isFront')

    def killAuto(self) -> Any:
        'killAuto()'
        _unavailable('fontlab.flLayer.killAuto')

    def nodesCount(self) -> int:
        'int nodesCount()'
        _unavailable('fontlab.flLayer.nodesCount')

    def prepareTransformationData(self) -> Any:
        'prepareTransformationData()'
        _unavailable('fontlab.flLayer.prepareTransformationData')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flLayer.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flLayer.remove')

    def removeAllShapes(self, shape_type: Any = ...) -> Any:
        'removeAllShapes([ShapeType shape_type=AnyShape])'
        _unavailable('fontlab.flLayer.removeAllShapes')

    def removeAnchor(self, arg0: flPinPoint) -> Any:
        'removeAnchor(flPinPoint)'
        _unavailable('fontlab.flLayer.removeAnchor')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flLayer.removeChild')

    def removeGuides(self, horizontal: bool, vertical: bool) -> bool:
        'bool removeGuides(bool horizontal, bool vertical)'
        _unavailable('fontlab.flLayer.removeGuides')

    def removeHints(self, horizontal: bool, vertical: bool) -> bool:
        'bool removeHints(bool horizontal, bool vertical)'
        _unavailable('fontlab.flLayer.removeHints')

    def removeShape(self, recursive: Any = ...) -> Any:
        'removeShape(flShape[, bool recursive=true])'
        _unavailable('fontlab.flLayer.removeShape')

    def reorderShapes(self, *args: Any, **kwargs: Any) -> Any:
        'reorderShapes(QList<uint>)'
        _unavailable('fontlab.flLayer.reorderShapes')

    def replaceShape(self, old_shape: flShape, new_shape: flShape) -> Any:
        'replaceShape(flShape old_shape, flShape new_shape)'
        _unavailable('fontlab.flLayer.replaceShape')

    def resetInkBox(self) -> Any:
        'resetInkBox()'
        _unavailable('fontlab.flLayer.resetInkBox')

    def resetMetricsLeft(self) -> Any:
        'resetMetricsLeft()'
        _unavailable('fontlab.flLayer.resetMetricsLeft')

    def resetMetricsRight(self) -> Any:
        'resetMetricsRight()'
        _unavailable('fontlab.flLayer.resetMetricsRight')

    def resetMetricsWidth(self) -> Any:
        'resetMetricsWidth()'
        _unavailable('fontlab.flLayer.resetMetricsWidth')

    def resetTransformationData(self) -> Any:
        'resetTransformationData()'
        _unavailable('fontlab.flLayer.resetTransformationData')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flLayer.restoreHistoryState')

    def selectAll(self) -> Any:
        'selectAll()'
        _unavailable('fontlab.flLayer.selectAll')

    def sendToBack(self, arg0: flShape) -> bool:
        'bool sendToBack(flShape)'
        _unavailable('fontlab.flLayer.sendToBack')

    def sendToFront(self, arg0: flShape) -> bool:
        'bool sendToFront(flShape)'
        _unavailable('fontlab.flLayer.sendToFront')

    def setActive(self) -> Any:
        'setActive()'
        _unavailable('fontlab.flLayer.setActive')

    def setActiveShape(self, arg0: flShape) -> Any:
        'setActiveShape(flShape)'
        _unavailable('fontlab.flLayer.setActiveShape')

    def setAllShapesSelected(self, bool: Any) -> Any:
        'setAllShapesSelected(bool)'
        _unavailable('fontlab.flLayer.setAllShapesSelected')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flLayer.setFlag')

    def setGlyphComponents(self, result: list[Any], width: float, package: flPackage, colorize: bool, flags: int) -> bool:
        'bool setGlyphComponents(QList<GlyphComponent> result, double width, flPackage package, bool colorize, uint flags)'
        _unavailable('fontlab.flLayer.setGlyphComponents')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flLayer.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flLayer.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flLayer.setPropertyInt')

    def setWireframeColorIx(self, int: Any) -> Any:
        'setWireframeColorIx(int)'
        _unavailable('fontlab.flLayer.setWireframeColorIx')

    def sortShapes(self) -> Any:
        'sortShapes()'
        _unavailable('fontlab.flLayer.sortShapes')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flLayer.tag')

    def takeShapes(self, shape_type: Any) -> list[flShape]:
        'QList<flShape> takeShapes(ShapeType shape_type)'
        _unavailable('fontlab.flLayer.takeShapes')

    def transferNames(self, layer: flLayer) -> Any:
        'transferNames(flLayer layer)'
        _unavailable('fontlab.flLayer.transferNames')

    def transferTTH(self, arg0: flLayer) -> bool:
        'bool transferTTH(flLayer)'
        _unavailable('fontlab.flLayer.transferTTH')

    def tthAutohint(self, make_hints: bool, itr: fgTTInterpreter) -> Any:
        'tthAutohint(bool make_hints, fgTTInterpreter itr)'
        _unavailable('fontlab.flLayer.tthAutohint')

    def tthFixZones(self, itr: fgTTInterpreter) -> Any:
        'tthFixZones(fgTTInterpreter itr)'
        _unavailable('fontlab.flLayer.tthFixZones')

    def tthReassignStems(self, itr: fgTTInterpreter) -> Any:
        'tthReassignStems(fgTTInterpreter itr)'
        _unavailable('fontlab.flLayer.tthReassignStems')

    def tthReassignZones(self, itr: fgTTInterpreter, bool: Any) -> Any:
        'tthReassignZones(fgTTInterpreter itr, bool)'
        _unavailable('fontlab.flLayer.tthReassignZones')

    def tthRemoveCommands(self, vertical: bool, horizontal: bool) -> Any:
        'tthRemoveCommands(bool vertical, bool horizontal)'
        _unavailable('fontlab.flLayer.tthRemoveCommands')

    def tthRemoveDeltas(self, middle: bool, final: bool) -> Any:
        'tthRemoveDeltas(bool middle, bool final)'
        _unavailable('fontlab.flLayer.tthRemoveDeltas')

    def unselectAllNodes(self) -> Any:
        'unselectAllNodes()'
        _unavailable('fontlab.flLayer.unselectAllNodes')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flLayer.update')

    def updateAnchors(self) -> Any:
        'updateAnchors()'
        _unavailable('fontlab.flLayer.updateAnchors')

    def updateAudit(self, *args: Any, **kwargs: Any) -> Any:
        'void updateAudit(list(int))'
        _unavailable('fontlab.flLayer.updateAudit')

    def updateGuidelineNode(self, node: flNode) -> flNode:
        'flNode updateGuidelineNode(flNode node)'
        _unavailable('fontlab.flLayer.updateGuidelineNode')

    def updatePreviewLinks(self) -> None:
        'void updatePreviewLinks()'
        _unavailable('fontlab.flLayer.updatePreviewLinks')

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
    'Data wrapper\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flLayerAttributes')

    def asDict(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as dictionary'
        _unavailable('fontlab.flLayerAttributes.asDict')

    def asTuple(self, *args: Any, **kwargs: Any) -> Any:
        'represent object as tuple'
        _unavailable('fontlab.flLayerAttributes.asTuple')

    isActive: Any
    isLocked: Any
    isService: Any
    isVisible: Any
    isWireframe: Any
    wireframeColor: Any

class flLayerInfo:
    'flLayerInfo representation\n\nConstructors:\n  flLayerInfo()\n  flLayerInfo(flObject)\n  flLayerInfo(flLayerInfo)\n  flLayerInfo(flLayer, QTransform)\n  flLayerInfo(flLayer, flObject glyph_info, QTransform)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flLayerInfo')

    def brectOnCanvas(self) -> QRectF:
        'QRectF brectOnCanvas()'
        _unavailable('fontlab.flLayerInfo.brectOnCanvas')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flLayerInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flLayerInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flLayerInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flLayerInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flLayerInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flLayerInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flLayerInfo.cloneObject')

    def combine(self, transform: QTransform) -> Any:
        'combine(QTransform transform)'
        _unavailable('fontlab.flLayerInfo.combine')

    def createInstance(self) -> flLayerInfo:
        'flLayerInfo createInstance()'
        _unavailable('fontlab.flLayerInfo.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flLayerInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flLayerInfo.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flLayerInfo.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flLayerInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flLayerInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flLayerInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flLayerInfo.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flLayerInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flLayerInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flLayerInfo.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flLayerInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flLayerInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flLayerInfo.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flLayerInfo.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flLayerInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flLayerInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flLayerInfo.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flLayerInfo.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flLayerInfo.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flLayerInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flLayerInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flLayerInfo.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flLayerInfo.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flLayerInfo.update')

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
    'flLocation representation\n\nConstructors:\n  flLocation(flLocation)\n  flLocation()\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flLocation')


class flMarkerPoint:
    'flMarkerPoint representation\n\nConstructors:\n  flMarkerPoint()\n  flMarkerPoint(flObject)\n  flMarkerPoint(flMarkerPoint)\n  flMarkerPoint(double marker_pos, uint markerFlags, flSnaps::MarkerKey key)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flMarkerPoint')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flMarkerPoint.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flMarkerPoint.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flMarkerPoint.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flMarkerPoint.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flMarkerPoint.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flMarkerPoint.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flMarkerPoint.cloneObject')

    def createInstance(self) -> flMarkerPoint:
        'flMarkerPoint createInstance()'
        _unavailable('fontlab.flMarkerPoint.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flMarkerPoint.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flMarkerPoint.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flMarkerPoint.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flMarkerPoint.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flMarkerPoint.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flMarkerPoint.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flMarkerPoint.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flMarkerPoint.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flMarkerPoint.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flMarkerPoint.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flMarkerPoint.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flMarkerPoint.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flMarkerPoint.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flMarkerPoint.isEqual')

    def markerFlag(self, role: int) -> int:
        'uint markerFlag(uint role)'
        _unavailable('fontlab.flMarkerPoint.markerFlag')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flMarkerPoint.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flMarkerPoint.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flMarkerPoint.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flMarkerPoint.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flMarkerPoint.setFlag')

    def setMarkerFlag(self, role: int, markerFlags: int) -> Any:
        'setMarkerFlag(uint role, uint markerFlags)'
        _unavailable('fontlab.flMarkerPoint.setMarkerFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flMarkerPoint.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flMarkerPoint.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flMarkerPoint.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flMarkerPoint.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flMarkerPoint.update')

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
    'flModel representation\n\nConstructors:\nNone, static only methods\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flModel')

    def createObject(self, type: int) -> Any:
        'flObject/Nothing createObject(int type)'
        _unavailable('fontlab.flModel.createObject')

    def getClassMask(self, type: int) -> int:
        'int  getClassMask(int type)'
        _unavailable('fontlab.flModel.getClassMask')

    def instance(self) -> flModel:
        'flModel instance()'
        _unavailable('fontlab.flModel.instance')

    def isClassMask(self, type: int) -> bool:
        'bool isClassMask(int type)'
        _unavailable('fontlab.flModel.isClassMask')

    def notifyGlyphChanged(self, fg_glyphId: Any) -> Any:
        'notifyGlyphChanged(unsigned long fg_glyphId)'
        _unavailable('fontlab.flModel.notifyGlyphChanged')

    def notifyGlyphUpdate(self, fg_glyphId: Any) -> Any:
        'notifyGlyphUpdate(unsigned long fg_glyphId)'
        _unavailable('fontlab.flModel.notifyGlyphUpdate')

    def notifyGlyphsChanged(self, glyphs: set[Any]) -> Any:
        'notifyGlyphsChanged(QSet<uint32_t> glyphs)'
        _unavailable('fontlab.flModel.notifyGlyphsChanged')

    def typeToStr(self, flObject: Any) -> str:
        'QString typeToStr(int type | flObject)'
        _unavailable('fontlab.flModel.typeToStr')

    ModelType: dict
    ObjectParameter: dict

class flModelProducer:
    'flModelProducer representation\n\nConstructors:\n  flModelProducer()\n  flModelProducer(flModelProducer)\n  flModelProducer(flObject)\n  flModelProducer(flCanvas)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flModelProducer')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flModelProducer.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flModelProducer.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flModelProducer.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flModelProducer.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flModelProducer.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flModelProducer.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flModelProducer.cloneObject')

    def copyToClipboard(self, package_id: Any, objects: list[flObject]) -> Any:
        'copyToClipboard(objId package_id, QList<flObject> objects)'
        _unavailable('fontlab.flModelProducer.copyToClipboard')

    def countGlyphsInData(self, *args: Any, **kwargs: Any) -> Any:
        'int countGlyphsInData(QByteArray *data)'
        _unavailable('fontlab.flModelProducer.countGlyphsInData')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flModelProducer.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flModelProducer.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flModelProducer.flag')

    def getClipboardData(self, *args: Any, **kwargs: Any) -> Any:
        'QByteArray getClipboardData(objId package_id, QList<flObject>)'
        _unavailable('fontlab.flModelProducer.getClipboardData')

    def getObjectsFromClipboard(self) -> Any:
        'flObjects/Nothing getObjectsFromClipboard()'
        _unavailable('fontlab.flModelProducer.getObjectsFromClipboard')

    def getObjectsFromData(self, *args: Any, **kwargs: Any) -> Any:
        'flObjects/Nothing getObjectsFromData(QByteArray *data)'
        _unavailable('fontlab.flModelProducer.getObjectsFromData')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flModelProducer.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flModelProducer.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flModelProducer.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flModelProducer.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flModelProducer.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flModelProducer.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flModelProducer.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flModelProducer.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flModelProducer.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flModelProducer.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flModelProducer.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flModelProducer.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flModelProducer.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flModelProducer.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flModelProducer.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flModelProducer.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flModelProducer.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flModelProducer.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flModelProducer.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flModelProducer.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flModelProducer.update')

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
    'flMouseEvent representation\n\nConstructors:\n  flMouseEvent(flMouseEvent)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flMouseEvent')

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
    'flNode representation\n\nConstructors:\n  flNode()\n  flNode(Node) - make clone\n  flNode(QPointF position[, string nodeType="on"[, int nodeKind=None]])\n  flNode(double x, double y[, string nodeType="on"[, int nodeKind=None]])\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flNode')

    def angleTo(self, p: QPointF) -> float:
        'double angleTo(QPointF p)'
        _unavailable('fontlab.flNode.angleTo')

    def applyTransform(self, arg0: QTransform) -> Any:
        'applyTransform(QTransform)'
        _unavailable('fontlab.flNode.applyTransform')

    def canBeHobby(self) -> bool:
        'bool canBeHobby()'
        _unavailable('fontlab.flNode.canBeHobby')

    def canBeSmooth(self) -> bool:
        'bool canBeSmooth()'
        _unavailable('fontlab.flNode.canBeSmooth')

    def canCollapse(self) -> bool:
        'bool canCollapse()'
        _unavailable('fontlab.flNode.canCollapse')

    def canImprove(self) -> bool:
        'bool canImprove()'
        _unavailable('fontlab.flNode.canImprove')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flNode.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flNode.checkInitHistoryState')

    def checkVectors(self) -> bool:
        'bool checkVectors()'
        _unavailable('fontlab.flNode.checkVectors')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flNode.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flNode.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flNode.clearFlags')

    def clearStored(self) -> Any:
        'clearStored()'
        _unavailable('fontlab.flNode.clearStored')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flNode.clone')

    def cloneMapped(self, arg0: QTransform) -> flNode:
        'flNode cloneMapped(QTransform)'
        _unavailable('fontlab.flNode.cloneMapped')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flNode.cloneObject')

    def collapseHandles(self) -> bool:
        'bool collapseHandles()'
        _unavailable('fontlab.flNode.collapseHandles')

    def convertToCurve(self, smooth: Any = ...) -> bool:
        'bool convertToCurve([bool smooth = false])'
        _unavailable('fontlab.flNode.convertToCurve')

    def convertToCurves(self) -> bool:
        'bool convertToCurves()'
        _unavailable('fontlab.flNode.convertToCurves')

    def convertToLine(self) -> bool:
        'bool convertToLine()'
        _unavailable('fontlab.flNode.convertToLine')

    def copyFrom(self, withSelected: Any = ...) -> Any:
        'copyFrom(Node[, withSelected=False])'
        _unavailable('fontlab.flNode.copyFrom')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flNode.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flNode.currentHistoryState')

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        'double distanceTo(Node/QPointF)'
        _unavailable('fontlab.flNode.distanceTo')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flNode.flag')

    def getLines(self, *args: Any, **kwargs: Any) -> Any:
        '(QLineF, QLineF)/None getLines()'
        _unavailable('fontlab.flNode.getLines')

    def getOn(self) -> Any:
        'Node/None getOn()'
        _unavailable('fontlab.flNode.getOn')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flNode.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flNode.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flNode.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flNode.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flNode.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flNode.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flNode.historyStates')

    def improve(self) -> bool:
        'bool improve()'
        _unavailable('fontlab.flNode.improve')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flNode.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flNode.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flNode.instanceType')

    def isCorner(self, a: Any = ...) -> bool:
        'bool isCorner([double a = 10.])'
        _unavailable('fontlab.flNode.isCorner')

    def isCurve(self) -> bool:
        'bool isCurve()'
        _unavailable('fontlab.flNode.isCurve')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flNode.isEqual')

    def isEqualTo(self, tolerance: Any = ...) -> bool:
        'bool isEqualTo(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])'
        _unavailable('fontlab.flNode.isEqualTo')

    def isExtreme(self, open: Any = ...) -> bool:
        'bool isExtreme(bool x[, bool open = true[, double limit = 0]])'
        _unavailable('fontlab.flNode.isExtreme')

    def isFirst(self) -> bool:
        'bool isFirst()'
        _unavailable('fontlab.flNode.isFirst')

    def isG2(self, tolerance: float) -> bool:
        'bool isG2(double tolerance)'
        _unavailable('fontlab.flNode.isG2')

    def isInternal(self, clockwise: bool) -> bool:
        'bool isInternal(bool clockwise)'
        _unavailable('fontlab.flNode.isInternal')

    def isInterpolated(self, x: bool) -> bool:
        'bool isInterpolated(bool x)'
        _unavailable('fontlab.flNode.isInterpolated')

    def isLast(self) -> bool:
        'bool isLast()'
        _unavailable('fontlab.flNode.isLast')

    def isOff(self) -> bool:
        'bool isOff()'
        _unavailable('fontlab.flNode.isOff')

    def isOn(self) -> bool:
        'bool isOn()'
        _unavailable('fontlab.flNode.isOn')

    def isSmartAngle(self) -> bool:
        'bool isSmartAngle()'
        _unavailable('fontlab.flNode.isSmartAngle')

    def makeStart(self) -> bool:
        'bool makeStart()'
        _unavailable('fontlab.flNode.makeStart')

    def moveBy(self, *args: Any, **kwargs: Any) -> Any:
        'moveBy(float dx, float dy[, bool round=false]'
        _unavailable('fontlab.flNode.moveBy')

    def nextNode(self, nodeType: Any = ...) -> Any:
        'Node/None nextNode([string nodeType= [, int searchDepth=1]])'
        _unavailable('fontlab.flNode.nextNode')

    def pointG2(self) -> Any:
        'QPointF/None pointG2()'
        _unavailable('fontlab.flNode.pointG2')

    def prevNode(self, nodeType: Any = ...) -> Any:
        'Node/None prevNode([string nodeType= [, int searchDepth=1]])'
        _unavailable('fontlab.flNode.prevNode')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flNode.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flNode.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flNode.removeChild')

    def restoreCoordinates(self) -> Any:
        'restoreCoordinates()'
        _unavailable('fontlab.flNode.restoreCoordinates')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flNode.restoreHistoryState')

    def rotateBy(self, origin: Any = ...) -> Any:
        'rotateBy(valueDegree[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flNode.rotateBy')

    def round(self) -> Any:
        "round() - Round the node's coordinate"
        _unavailable('fontlab.flNode.round')

    def scaleBy(self, origin: Any = ...) -> Any:
        'scaleBy(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flNode.scaleBy')

    def setExtraLast(self, bool: Any) -> Any:
        'setExtraLast(bool)'
        _unavailable('fontlab.flNode.setExtraLast')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flNode.setFlag')

    def setNextSmooth(self, base: QPointF) -> Any:
        'setNextSmooth(QPointF base)'
        _unavailable('fontlab.flNode.setNextSmooth')

    def setPrevSmooth(self, base: QPointF) -> Any:
        'setPrevSmooth(QPointF base)'
        _unavailable('fontlab.flNode.setPrevSmooth')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flNode.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flNode.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flNode.setPropertyInt')

    def setSmartAngleEnbl(self, bool: Any) -> bool:
        'bool setSmartAngleEnbl(bool)'
        _unavailable('fontlab.flNode.setSmartAngleEnbl')

    def setSmartSharp(self, tension: Any = ...) -> bool:
        'bool setSmartSharp([double tension = 0.6])'
        _unavailable('fontlab.flNode.setSmartSharp')

    def skewBy(self, origin: Any = ...) -> Any:
        'skewBy(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flNode.skewBy')

    def smartMove(self, offset: Any) -> Any:
        'list(uint) smartMove(offset)'
        _unavailable('fontlab.flNode.smartMove')

    def smartSetXY(self, arg0: QPointF) -> Any:
        'smartSetXY(QPointF)'
        _unavailable('fontlab.flNode.smartSetXY')

    def storeCoordinates(self) -> Any:
        'storeCoordinates()'
        _unavailable('fontlab.flNode.storeCoordinates')

    def storeTestParameters(self) -> Any:
        'storeTestParameters()'
        _unavailable('fontlab.flNode.storeTestParameters')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flNode.tag')

    def transformBy(self, origin: Any = ...) -> Any:
        'transformBy(QTransform tx[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flNode.transformBy')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flNode.update')

    def updateG2(self) -> bool:
        'bool updateG2()'
        _unavailable('fontlab.flNode.updateG2')

    def updateSmooth(self, extended_neibh: Any = ...) -> Any:
        'updateSmooth([bool extended_neibh=true])'
        _unavailable('fontlab.flNode.updateSmooth')

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
    'flNodeInfo representation\n\nConstructors:\n  flNodeInfo()\n  flNodeInfo(flObject)\n  flNodeInfo(flNodeInfo)\n  flNodeInfo(flNode, QTransform)\n  flNodeInfo(flNode, flObject contour_info)\n  flNodeInfo(flNode, flObject glyph_info, QTransform)\n  flNodeInfo(flNode, flNodeInfo)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flNodeInfo')

    def breakContourExpanded(self, extrapolate_d: Any = ...) -> bool:
        'bool breakContourExpanded([double extrapolate_d=0.5])'
        _unavailable('fontlab.flNodeInfo.breakContourExpanded')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flNodeInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flNodeInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flNodeInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flNodeInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flNodeInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flNodeInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flNodeInfo.cloneObject')

    def combine(self, transform: QTransform) -> Any:
        'combine(QTransform transform)'
        _unavailable('fontlab.flNodeInfo.combine')

    def contour(self) -> flContour:
        'flContour contour()'
        _unavailable('fontlab.flNodeInfo.contour')

    def createInstance(self) -> flNodeInfo:
        'flNodeInfo createInstance()'
        _unavailable('fontlab.flNodeInfo.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flNodeInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flNodeInfo.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flNodeInfo.flag')

    def getGlyphPoint(self, round: bool) -> QPointF:
        'QPointF getGlyphPoint(bool round)'
        _unavailable('fontlab.flNodeInfo.getGlyphPoint')

    def getMappedNeighborsRect(self) -> QRectF:
        'QRectF getMappedNeighborsRect()'
        _unavailable('fontlab.flNodeInfo.getMappedNeighborsRect')

    def getMappedPoint(self, *args: Any, **kwargs: Any) -> Any:
        'QPointF getMappedPoint([QPointF])'
        _unavailable('fontlab.flNodeInfo.getMappedPoint')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flNodeInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flNodeInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flNodeInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flNodeInfo.getPropertyInt')

    def getUpdateCanvasRect(self) -> QRectF:
        'QRectF getUpdateCanvasRect()'
        _unavailable('fontlab.flNodeInfo.getUpdateCanvasRect')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flNodeInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flNodeInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flNodeInfo.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flNodeInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flNodeInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flNodeInfo.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flNodeInfo.isEqual')

    def isValid(self) -> bool:
        'bool isValid()'
        _unavailable('fontlab.flNodeInfo.isValid')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flNodeInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flNodeInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flNodeInfo.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flNodeInfo.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flNodeInfo.setFlag')

    def setGlyphPoint(self, arg0: QPointF) -> Any:
        'setGlyphPoint(QPointF)'
        _unavailable('fontlab.flNodeInfo.setGlyphPoint')

    def setGlyphPointX(self, x: float) -> Any:
        'setGlyphPointX(double x)'
        _unavailable('fontlab.flNodeInfo.setGlyphPointX')

    def setGlyphPointY(self, y: float) -> Any:
        'setGlyphPointY(double y)'
        _unavailable('fontlab.flNodeInfo.setGlyphPointY')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flNodeInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flNodeInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flNodeInfo.setPropertyInt')

    def shape(self) -> flShape:
        'flShape shape()'
        _unavailable('fontlab.flNodeInfo.shape')

    def shapeInfo(self) -> flShapeInfo:
        'flShapeInfo shapeInfo()'
        _unavailable('fontlab.flNodeInfo.shapeInfo')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flNodeInfo.tag')

    def toNodesInfo(self, *args: Any, **kwargs: Any) -> Any:
        'list(flNodeInfo) toNodesInfo(list(flNode))'
        _unavailable('fontlab.flNodeInfo.toNodesInfo')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flNodeInfo.update')

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
    'flObject representation\n\nConstructors:\n  flObject()\n  flObject(flObject)\n  flObject(uint id)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flObject')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flObject.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flObject.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flObject.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flObject.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flObject.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flObject.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flObject.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flObject.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flObject.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flObject.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flObject.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flObject.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flObject.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flObject.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flObject.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flObject.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flObject.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flObject.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flObject.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flObject.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flObject.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flObject.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flObject.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flObject.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flObject.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flObject.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flObject.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flObject.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flObject.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flObject.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flObject.update')

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
    'flObjectsList<flGuideLine> doc\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flObjectsList<flGuideLine>')

    def append(self, o: Any) -> None:
        'void append(T o)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.append')

    def at(self, i: int) -> Any:
        'T at(int i)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.at')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.clearAboveHistory')

    def clearContent(self) -> None:
        'void clearContent()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.clearContent')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flObjectsList<flGuideLine>.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flObjectsList<flGuideLine>.cloneObject')

    def contains(self, o: Any) -> bool:
        'bool contains(T o)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.contains')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flObjectsList<flGuideLine>.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flObjectsList<flGuideLine>.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flObjectsList<flGuideLine>.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flObjectsList<flGuideLine>.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flObjectsList<flGuideLine>.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flObjectsList<flGuideLine>.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.independedAll')

    def indexOf(self, o: Any) -> int:
        'int indexOf(T o)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.indexOf')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.initialHistoryState')

    def insert(self, index: int, o: Any) -> None:
        'void insert(int index, T o)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.insert')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flObjectsList<flGuideLine>.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flObjectsList<flGuideLine>.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.removeChild')

    def removeOne(self, o: Any) -> None:
        'void removeOne(T o)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.removeOne')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flObjectsList<flGuideLine>.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flObjectsList<flGuideLine>.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flObjectsList<flGuideLine>.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flObjectsList<flGuideLine>.setPropertyInt')

    def swap(self, i0: int, i1: int) -> None:
        'void swap(int i0, int i1)'
        _unavailable('fontlab.flObjectsList<flGuideLine>.swap')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flObjectsList<flGuideLine>.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flObjectsList<flGuideLine>.update')

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
    'flObjectsList<flShape> doc\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flObjectsList<flShape>')

    def append(self, o: Any) -> None:
        'void append(T o)'
        _unavailable('fontlab.flObjectsList<flShape>.append')

    def at(self, i: int) -> Any:
        'T at(int i)'
        _unavailable('fontlab.flObjectsList<flShape>.at')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flObjectsList<flShape>.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flShape>.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flShape>.clearAboveHistory')

    def clearContent(self) -> None:
        'void clearContent()'
        _unavailable('fontlab.flObjectsList<flShape>.clearContent')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flObjectsList<flShape>.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flObjectsList<flShape>.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flObjectsList<flShape>.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flObjectsList<flShape>.cloneObject')

    def contains(self, o: Any) -> bool:
        'bool contains(T o)'
        _unavailable('fontlab.flObjectsList<flShape>.contains')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flObjectsList<flShape>.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flObjectsList<flShape>.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flObjectsList<flShape>.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flObjectsList<flShape>.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flObjectsList<flShape>.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flObjectsList<flShape>.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flObjectsList<flShape>.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flShape>.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flObjectsList<flShape>.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flObjectsList<flShape>.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flObjectsList<flShape>.independedAll')

    def indexOf(self, o: Any) -> int:
        'int indexOf(T o)'
        _unavailable('fontlab.flObjectsList<flShape>.indexOf')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flObjectsList<flShape>.initialHistoryState')

    def insert(self, index: int, o: Any) -> None:
        'void insert(int index, T o)'
        _unavailable('fontlab.flObjectsList<flShape>.insert')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flObjectsList<flShape>.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flObjectsList<flShape>.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flObjectsList<flShape>.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flObjectsList<flShape>.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flObjectsList<flShape>.removeChild')

    def removeOne(self, o: Any) -> None:
        'void removeOne(T o)'
        _unavailable('fontlab.flObjectsList<flShape>.removeOne')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flObjectsList<flShape>.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flObjectsList<flShape>.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flObjectsList<flShape>.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flObjectsList<flShape>.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flObjectsList<flShape>.setPropertyInt')

    def swap(self, i0: int, i1: int) -> None:
        'void swap(int i0, int i1)'
        _unavailable('fontlab.flObjectsList<flShape>.swap')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flObjectsList<flShape>.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flObjectsList<flShape>.update')

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
    'flPackage representation\n\nConstructors:\n  flPackage()\n  flPackage(flObject)\n  flPackage(fgFont)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flPackage')

    def activateGlyph(self, arg0: flGlyph) -> Any:
        'activateGlyph(flGlyph)'
        _unavailable('fontlab.flPackage.activateGlyph')

    def addAxis(self, variable: flAxis) -> Any:
        'string addAxis(flAxis variable)'
        _unavailable('fontlab.flPackage.addAxis')

    def addGlyph(self, flGlyph: Any) -> Any:
        'addGlyph(fgGlyph / flGlyph )'
        _unavailable('fontlab.flPackage.addGlyph')

    def addInstance(self, *args: Any, **kwargs: Any) -> Any:
        'addInstance(const flInstance &instance)'
        _unavailable('fontlab.flPackage.addInstance')

    def addMaster(self, *args: Any, **kwargs: Any) -> Any:
        'string addMaster(string master_name, bool create_glyphs, flPackage source, string source_layer_name, bool copy_metrics, bool create_missing_glyphs[, flLocation location])'
        _unavailable('fontlab.flPackage.addMaster')

    def assignData(self, *args: Any, **kwargs: Any) -> Any:
        'assignData(const flPackage &package)'
        _unavailable('fontlab.flPackage.assignData')

    def autoKern(self, left: flGlyph, right: flGlyph, master_name: Any) -> Any:
        'autoKern(flGlyph left, flGlyph right, string master_name)'
        _unavailable('fontlab.flPackage.autoKern')

    def autohintGlyphs(self, glyphs: list[flGlyph], make_hints: bool) -> Any:
        'autohintGlyphs(QList<flGlyph> glyphs, bool make_hints)'
        _unavailable('fontlab.flPackage.autohintGlyphs')

    def buildShapeDataNames(self, *args: Any, **kwargs: Any) -> Any:
        'QSet<string> buildShapeDataNames(objId exclude[, string layer_name])'
        _unavailable('fontlab.flPackage.buildShapeDataNames')

    def can_interpolate(self, *args: Any, **kwargs: Any) -> Any:
        'bool can_interpolate([string master_name])'
        _unavailable('fontlab.flPackage.can_interpolate')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flPackage.changed')

    def checkAxisName(self, name: Any) -> Any:
        'string checkAxisName(string name)'
        _unavailable('fontlab.flPackage.checkAxisName')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flPackage.checkInitHistoryState')

    def checkVariableName(self, name: Any) -> Any:
        'string checkVariableName(string name)'
        _unavailable('fontlab.flPackage.checkVariableName')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flPackage.clearAboveHistory')

    def clearActiveGlyphs(self) -> Any:
        'clearActiveGlyphs()'
        _unavailable('fontlab.flPackage.clearActiveGlyphs')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flPackage.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flPackage.clearFlags')

    def clearInstances(self) -> Any:
        'clearInstances()'
        _unavailable('fontlab.flPackage.clearInstances')

    def clearMasters(self, release: bool) -> Any:
        'clearMasters(bool release)'
        _unavailable('fontlab.flPackage.clearMasters')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flPackage.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flPackage.cloneObject')

    def close(self, save: Any = False) -> Any:
        'close(save=False) - Close the font'
        _unavailable('fontlab.flPackage.close')

    def collectNames(self, storage: Any) -> Any:
        'collectNames(StorageInfo * storage)'
        _unavailable('fontlab.flPackage.collectNames')

    def completeData(self, fg_data: Any = ...) -> Any:
        'completeData([bool fg_data = false])'
        _unavailable('fontlab.flPackage.completeData')

    def convertZonesToGuidelines(self, zonesT: flZones, zonesB: flZones) -> Any:
        'convertZonesToGuidelines(flZones zonesT, flZones zonesB)'
        _unavailable('fontlab.flPackage.convertZonesToGuidelines')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flPackage.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flPackage.currentHistoryState')

    def deleteGlyph(self, flGlyph: Any) -> bool:
        'bool deleteGlyph(fgGlyph / flGlyph )'
        _unavailable('fontlab.flPackage.deleteGlyph')

    def deleteGroups(self, ids: set[int], deleteDependentContent: bool) -> Any:
        'deleteGroups(QSet<uint> ids, bool deleteDependentContent)'
        _unavailable('fontlab.flPackage.deleteGroups')

    def ensureProteusData(self) -> Any:
        'ensureProteusData()'
        _unavailable('fontlab.flPackage.ensureProteusData')

    def family_zones(self, top: bool) -> Any:
        'list(flZone)& family_zones(bool top)'
        _unavailable('fontlab.flPackage.family_zones')

    def featuresContainer(self) -> flObject:
        'flObject featuresContainer()'
        _unavailable('fontlab.flPackage.featuresContainer')

    def findAxis(self, cs: Any = ...) -> Any:
        'flAxis/Nothing findAxis(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])'
        _unavailable('fontlab.flPackage.findAxis')

    def findAxisShort(self, short_name: Any) -> Any:
        'flAxis/Nothing findAxisShort(string short_name)'
        _unavailable('fontlab.flPackage.findAxisShort')

    def findFgId(self, id: int) -> flGlyph:
        'flGlyph findFgId(uint id)'
        _unavailable('fontlab.flPackage.findFgId')

    def findGroup(self, _id: int) -> Any:
        'fg::GlyphGroup* findGroup(int _id)'
        _unavailable('fontlab.flPackage.findGroup')

    def findName(self, name: Any) -> flGlyph:
        'flGlyph findName(string name)'
        _unavailable('fontlab.flPackage.findName')

    def findNameId(self, fg_id: int) -> flGlyph:
        'flGlyph findNameId(uint fg_id)'
        _unavailable('fontlab.flPackage.findNameId')

    def findNewName(self, name: Any) -> Any:
        'string findNewName(string name)'
        _unavailable('fontlab.flPackage.findNewName')

    def findShapeRoot(self, shape_data: flShapeData) -> flGlyph:
        'flGlyph findShapeRoot(flShapeData shape_data)'
        _unavailable('fontlab.flPackage.findShapeRoot')

    def findStem(self, n: Any, b: bool, loose: bool) -> int:
        'int findStem(string n, bool b, bool loose)'
        _unavailable('fontlab.flPackage.findStem')

    def findUnicode(self, uni: int) -> flGlyph:
        'flGlyph findUnicode(uint uni)'
        _unavailable('fontlab.flPackage.findUnicode')

    def findZone(self, n: Any, b: bool) -> int:
        'int findZone(string n, bool b)'
        _unavailable('fontlab.flPackage.findZone')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flPackage.flag')

    def generateGlyph(self, recipe: Any, layer_name: Any, metrics: Any, rtl: bool) -> Any:
        'QList<GlyphComponent>/Nothing generateGlyph(string recipe, string layer_name, FontMetrics metrics, bool rtl)'
        _unavailable('fontlab.flPackage.generateGlyph')

    def getAccentsInfo(self, arg0: flLayer, arg1: flPinPoint) -> Any:
        'list(AccentInfo)/Nothing getAccentsInfo(flLayer, flPinPoint)'
        _unavailable('fontlab.flPackage.getAccentsInfo')

    def getAllGroups(self) -> Any:
        'list( (bool kernGroup, string groupName, int id, int mark, list(string glyphName) )/Nothing getAllGroups()'
        _unavailable('fontlab.flPackage.getAllGroups')

    def getAxisName(self, short_name: Any) -> Any:
        'string getAxisName(string short_name)'
        _unavailable('fontlab.flPackage.getAxisName')

    def getAxisShortName(self, name: Any) -> Any:
        'string getAxisShortName(string name)'
        _unavailable('fontlab.flPackage.getAxisShortName')

    def getLayerName(self) -> Any:
        'string getLayerName()'
        _unavailable('fontlab.flPackage.getLayerName')

    def getMarkOffset(self, g1: flGlyph, g2: flGlyph, layer_name: Any) -> Any:
        'QPointF/Nothing getMarkOffset(flGlyph g1, flGlyph g2, string layer_name)'
        _unavailable('fontlab.flPackage.getMarkOffset')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flPackage.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flPackage.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flPackage.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flPackage.getPropertyInt')

    def getShapes(self, *args: Any, **kwargs: Any) -> Any:
        'QList<int>/Nothing getShapes(string filter[, string layer_name])'
        _unavailable('fontlab.flPackage.getShapes')

    def hasAxis(self, cs: Any = ...) -> bool:
        'bool hasAxis(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])'
        _unavailable('fontlab.flPackage.hasAxis')

    def hasAxisShort(self, short_name: Any) -> bool:
        'bool hasAxisShort(string short_name)'
        _unavailable('fontlab.flPackage.hasAxisShort')

    def hasGuides(self) -> bool:
        'bool hasGuides()'
        _unavailable('fontlab.flPackage.hasGuides')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flPackage.hasHistoryState')

    def hasInstaceFor(self, arg0: fgFont) -> bool:
        'bool hasInstaceFor(fgFont)'
        _unavailable('fontlab.flPackage.hasInstaceFor')

    def hasMaster(self, name: Any) -> bool:
        'bool hasMaster(string name)'
        _unavailable('fontlab.flPackage.hasMaster')

    def hasName(self, relaxed: Any = ...) -> bool:
        'bool hasName(string name[, bool relaxed=false])'
        _unavailable('fontlab.flPackage.hasName')

    def hasPackageHistoryStorages(self, to_history_ix: int) -> bool:
        'bool hasPackageHistoryStorages(uint to_history_ix)'
        _unavailable('fontlab.flPackage.hasPackageHistoryStorages')

    def hasZones(self) -> bool:
        'bool hasZones()'
        _unavailable('fontlab.flPackage.hasZones')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flPackage.haveObject')

    def historyStack(self) -> flObject:
        'flObject historyStack()'
        _unavailable('fontlab.flPackage.historyStack')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flPackage.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flPackage.independedAll')

    def initItr(self, itr: fgTTInterpreter) -> Any:
        'initItr(fgTTInterpreter itr)'
        _unavailable('fontlab.flPackage.initItr')

    def initItrGlyph(self, itr: fgTTInterpreter, glyph: flGlyph) -> Any:
        'initItrGlyph(fgTTInterpreter itr, flGlyph glyph)'
        _unavailable('fontlab.flPackage.initItrGlyph')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flPackage.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flPackage.instanceType')

    def interpolateInstance(self, location: flLocation, round: bool) -> flPackage:
        'flPackage interpolateInstance(flLocation location, bool round)'
        _unavailable('fontlab.flPackage.interpolateInstance')

    def interpolateMaster(self, location: flLocation, master_name: Any) -> bool:
        'bool interpolateMaster(flLocation location, string master_name)'
        _unavailable('fontlab.flPackage.interpolateMaster')

    def isComponent(self, *args: Any, **kwargs: Any) -> Any:
        '(flGlyph, QTransform) isComponent(flShapeData[, string layer_name])'
        _unavailable('fontlab.flPackage.isComponent')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flPackage.isEqual')

    def kerning(self, *args: Any, **kwargs: Any) -> Any:
        'fgKerning kerning([string master_name])'
        _unavailable('fontlab.flPackage.kerning')

    def kerningContainer(self) -> flObject:
        'flObject kerningContainer()'
        _unavailable('fontlab.flPackage.kerningContainer')

    def location(self, *args: Any, **kwargs: Any) -> Any:
        'flLocation& location([string master_name])'
        _unavailable('fontlab.flPackage.location')

    def makeShapeDataName(self, name: Any, _id: Any, layer_name: Any) -> Any:
        'string makeShapeDataName(string name, objId _id, string layer_name)'
        _unavailable('fontlab.flPackage.makeShapeDataName')

    def mastersContainer(self) -> flObject:
        'flObject mastersContainer()'
        _unavailable('fontlab.flPackage.mastersContainer')

    def optimizeShapeTransformations(self, changes: list[flObject]) -> bool:
        'bool optimizeShapeTransformations(QList<flObject> changes)'
        _unavailable('fontlab.flPackage.optimizeShapeTransformations')

    def optimizeStemData(self, *args: Any, **kwargs: Any) -> Any:
        '(flStems stemsH, flStems stemsV) optimizeStemData(flStems stemsH, flStems stemsV)'
        _unavailable('fontlab.flPackage.optimizeStemData')

    def prepareAxes(self, packages: list[flPackage], glyphs: list[flGlyph]) -> Any:
        'QList<flAxis>/Nothing prepareAxes(QList<flPackage> packages, QList<flGlyph> glyphs)'
        _unavailable('fontlab.flPackage.prepareAxes')

    def prepareFontGateData(self, prepare_tth: bool) -> Any:
        'prepareFontGateData(bool prepare_tth)'
        _unavailable('fontlab.flPackage.prepareFontGateData')

    def preparePropertiesData(self) -> Any:
        'preparePropertiesData()'
        _unavailable('fontlab.flPackage.preparePropertiesData')

    def projectPackageName(self) -> Any:
        'string projectPackageName()'
        _unavailable('fontlab.flPackage.projectPackageName')

    def readFromFile(self, *args: Any, **kwargs: Any) -> Any:
        'flPackage/Nothing readFromFile(string[, StorageInfo*=0])'
        _unavailable('fontlab.flPackage.readFromFile')

    def referencesCount(self, shapeDataId: int) -> int:
        'int referencesCount(uint shapeDataId)'
        _unavailable('fontlab.flPackage.referencesCount')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flPackage.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flPackage.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flPackage.removeChild')

    def removeMaster(self, name: Any, remove_glyph_masters: bool) -> Any:
        'removeMaster(string name, bool remove_glyph_masters)'
        _unavailable('fontlab.flPackage.removeMaster')

    def renameGlyph(self, glyph: fgGlyph, name: Any, rename: bool) -> bool:
        'bool renameGlyph(fgGlyph glyph, string name, bool rename)'
        _unavailable('fontlab.flPackage.renameGlyph')

    def renameMaster(self, old_name: Any, new_name: Any) -> Any:
        'string renameMaster(string old_name, string new_name)'
        _unavailable('fontlab.flPackage.renameMaster')

    def replaceGlyph(self, target: fgGlyph, newGlyph: fgGlyph, rename: bool) -> bool:
        'bool replaceGlyph(fgGlyph target, fgGlyph newGlyph, bool rename)'
        _unavailable('fontlab.flPackage.replaceGlyph')

    def replaceShapeWithReference(self, *args: Any, **kwargs: Any) -> Any:
        'flShape/Nothing replaceShapeWithReference(flShape shape, bool process[, string layer_name])'
        _unavailable('fontlab.flPackage.replaceShapeWithReference')

    def resetPackage(self) -> Any:
        'resetPackage()'
        _unavailable('fontlab.flPackage.resetPackage')

    def resetStemData(self, *args: Any, **kwargs: Any) -> Any:
        '(flStems stemsH, flStems stemsV) resetStemData(flStems stemsH, flStems stemsV)'
        _unavailable('fontlab.flPackage.resetStemData')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flPackage.restoreHistoryState')

    def runActions(self, *args: Any, **kwargs: Any) -> Any:
        'void runActions(QList<flGlyph> &glyphs, QStringList actions, int layer_mode, bool do_undo)'
        _unavailable('fontlab.flPackage.runActions')

    def setAxis(self, *args: Any, **kwargs: Any) -> Any:
        'setAxis(const flAxis &p)'
        _unavailable('fontlab.flPackage.setAxis')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flPackage.setFlag')

    def setLocation(self, *args: Any, **kwargs: Any) -> Any:
        'setLocation(flLocation location[, string master_name])'
        _unavailable('fontlab.flPackage.setLocation')

    def setMaster(self, notify: Any = ...) -> Any:
        'setMaster(string name[, bool notify = false])'
        _unavailable('fontlab.flPackage.setMaster')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flPackage.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flPackage.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flPackage.setPropertyInt')

    def setUpm(self, upm: int, scale: bool) -> Any:
        'setUpm(int upm, bool scale)'
        _unavailable('fontlab.flPackage.setUpm')

    def set_ascender_locked(self, b: bool) -> Any:
        'set_ascender_locked(bool b)'
        _unavailable('fontlab.flPackage.set_ascender_locked')

    def set_capsHeight_locked(self, b: bool) -> Any:
        'set_capsHeight_locked(bool b)'
        _unavailable('fontlab.flPackage.set_capsHeight_locked')

    def set_descender_locked(self, b: bool) -> Any:
        'set_descender_locked(bool b)'
        _unavailable('fontlab.flPackage.set_descender_locked')

    def set_interpolate(self, *args: Any, **kwargs: Any) -> Any:
        'set_interpolate(bool b[, string master_name])'
        _unavailable('fontlab.flPackage.set_interpolate')

    def set_measurement_locked(self, b: bool) -> Any:
        'set_measurement_locked(bool b)'
        _unavailable('fontlab.flPackage.set_measurement_locked')

    def set_xHeight_locked(self, b: bool) -> Any:
        'set_xHeight_locked(bool b)'
        _unavailable('fontlab.flPackage.set_xHeight_locked')

    def stems(self, HintingDataType: Any, top: bool) -> Any:
        'list(flStem)& stems(HintingDataType, bool top)'
        _unavailable('fontlab.flPackage.stems')

    def store_font_info(self, *args: Any, **kwargs: Any) -> Any:
        'store_font_info(fg::Package *package)'
        _unavailable('fontlab.flPackage.store_font_info')

    def store_hinting_data(self, package: fgPackage) -> Any:
        'store_hinting_data(fgPackage package)'
        _unavailable('fontlab.flPackage.store_hinting_data')

    def styleCode(self) -> Any:
        'unsigned char styleCode()'
        _unavailable('fontlab.flPackage.styleCode')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flPackage.tag')

    def title_name(self, force_full: Any = ...) -> Any:
        'string title_name([bool force_full = true])'
        _unavailable('fontlab.flPackage.title_name')

    def tthRenameStems(self, map_h: dict[str, str], map_v: dict[str, str]) -> bool:
        'bool tthRenameStems(QMap<QString, QString> map_h, QMap<QString, QString> map_v)'
        _unavailable('fontlab.flPackage.tthRenameStems')

    def tthRenameZones(self, map_top: dict[str, str], map_bottom: dict[str, str]) -> bool:
        'bool tthRenameZones(QMap<QString, QString> map_top, QMap<QString, QString> map_bottom)'
        _unavailable('fontlab.flPackage.tthRenameZones')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flPackage.update')

    def updateAxesMap(self) -> Any:
        'updateAxesMap()'
        _unavailable('fontlab.flPackage.updateAxesMap')

    def updateFontMetrics(self) -> Any:
        'updateFontMetrics()'
        _unavailable('fontlab.flPackage.updateFontMetrics')

    def updateShapeReferenceCount(self) -> Any:
        'updateShapeReferenceCount()'
        _unavailable('fontlab.flPackage.updateShapeReferenceCount')

    def updateZonesFromGuidelines(self, *args: Any, **kwargs: Any) -> Any:
        'updateZonesFromGuidelines([flZones zonesT, flZones zonesB])'
        _unavailable('fontlab.flPackage.updateZonesFromGuidelines')

    def zones(self, HintingDataType: Any, top: bool) -> Any:
        'list(flZone)& zones(HintingDataType, bool top)'
        _unavailable('fontlab.flPackage.zones')

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
    'flPaper representation\n\nConstructors:\n  flPaper()\n  flPaper(flPaper)\n  flPaper(flObject)\n  flPaper(QBrush)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flPaper')

    def activeGlyphInfo(self) -> flObject:
        'flObject activeGlyphInfo()'
        _unavailable('fontlab.flPaper.activeGlyphInfo')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flPaper.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flPaper.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flPaper.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flPaper.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flPaper.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flPaper.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flPaper.cloneObject')

    def createInstance(self) -> flPaper:
        'flPaper createInstance()'
        _unavailable('fontlab.flPaper.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flPaper.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flPaper.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flPaper.flag')

    def getGlyphInfo(self, arg0: flObject) -> flObject:
        'flObject getGlyphInfo(flObject)'
        _unavailable('fontlab.flPaper.getGlyphInfo')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flPaper.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flPaper.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flPaper.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flPaper.getPropertyInt')

    def glyph(self) -> flObject:
        'flObject glyph()'
        _unavailable('fontlab.flPaper.glyph')

    def glyphInfoAt(self, index: int) -> flObject:
        'flObject glyphInfoAt(int index)'
        _unavailable('fontlab.flPaper.glyphInfoAt')

    def glyphsBoundRect(self) -> QRectF:
        'QRectF glyphsBoundRect()'
        _unavailable('fontlab.flPaper.glyphsBoundRect')

    def hasActive(self) -> bool:
        'bool hasActive()'
        _unavailable('fontlab.flPaper.hasActive')

    def hasContent(self) -> bool:
        'bool hasContent()'
        _unavailable('fontlab.flPaper.hasContent')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flPaper.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flPaper.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flPaper.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flPaper.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flPaper.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flPaper.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flPaper.isEqual')

    def package(self) -> flObject:
        'flObject package()'
        _unavailable('fontlab.flPaper.package')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flPaper.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flPaper.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flPaper.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flPaper.restoreHistoryState')

    def setActiveGlyph(self, glyph: flObject) -> flObject:
        'flObject setActiveGlyph(flObject glyph)'
        _unavailable('fontlab.flPaper.setActiveGlyph')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flPaper.setFlag')

    def setPaperGlyph(self, glyph: flObject) -> flObject:
        'flObject setPaperGlyph(flObject glyph)'
        _unavailable('fontlab.flPaper.setPaperGlyph')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flPaper.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flPaper.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flPaper.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flPaper.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flPaper.update')

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
    'flPinPoint representation\n\nConstructors:\n  flPinPoint()\n  flPinPoint(flPinPoint)\n  flPinPoint(flObject)\n  flPinPoint(QPointF[, PinPointStyle=FreePosition])\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flPinPoint')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flPinPoint.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flPinPoint.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flPinPoint.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flPinPoint.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flPinPoint.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flPinPoint.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flPinPoint.cloneObject')

    def createInstance(self) -> flPinPoint:
        'flPinPoint createInstance()'
        _unavailable('fontlab.flPinPoint.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flPinPoint.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flPinPoint.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flPinPoint.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flPinPoint.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flPinPoint.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flPinPoint.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flPinPoint.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flPinPoint.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flPinPoint.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flPinPoint.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flPinPoint.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flPinPoint.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flPinPoint.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flPinPoint.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flPinPoint.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flPinPoint.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flPinPoint.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flPinPoint.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flPinPoint.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flPinPoint.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flPinPoint.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flPinPoint.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flPinPoint.tag')

    def translate(self, arg0: QPointF) -> Any:
        'translate(QPointF)'
        _unavailable('fontlab.flPinPoint.translate')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flPinPoint.update')

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
    'flPreferences representation\n\nConstructors:\n  flPreferences()\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flPreferences')

    def doInterpolate(self) -> bool:
        'bool doInterpolate()'
        _unavailable('fontlab.flPreferences.doInterpolate')

    def fontAuditTests(self) -> Any:
        'list(int) fontAuditTests()'
        _unavailable('fontlab.flPreferences.fontAuditTests')

    def instance(self) -> flPreferences:
        'flPreferences instance()'
        _unavailable('fontlab.flPreferences.instance')

    def load(self, arg0: dict[str, Any]) -> Any:
        'load(QVariantMap)'
        _unavailable('fontlab.flPreferences.load')

    def namecaptionFont(self, *args: Any, **kwargs: Any) -> Any:
        'QFont  namecaptionFont (bool condensed)'
        _unavailable('fontlab.flPreferences.namecaptionFont')

    def namecaptionFontFamilyName(self, *args: Any, **kwargs: Any) -> Any:
        'string namecaptionFontFamilyName (bool condensed)'
        _unavailable('fontlab.flPreferences.namecaptionFontFamilyName')

    def namecaptionFontId(self, *args: Any, **kwargs: Any) -> Any:
        'int    namecaptionFontId (bool condensed)'
        _unavailable('fontlab.flPreferences.namecaptionFontId')

    def options2tracer_precision(self) -> float:
        'double options2tracer_precision()'
        _unavailable('fontlab.flPreferences.options2tracer_precision')

    def options2tracer_smoothness(self) -> int:
        'int options2tracer_smoothness()'
        _unavailable('fontlab.flPreferences.options2tracer_smoothness')

    def save(self) -> dict[str, Any]:
        'QVariantMap save()'
        _unavailable('fontlab.flPreferences.save')

    def saveView(self) -> Any:
        'saveView()'
        _unavailable('fontlab.flPreferences.saveView')

    def setFontAuditTest(self, id: int, value: bool) -> Any:
        'setFontAuditTest(int id, bool value)'
        _unavailable('fontlab.flPreferences.setFontAuditTest')

    def setGridDistances(self, x: float, y: float) -> Any:
        'setGridDistances(double x, double y)'
        _unavailable('fontlab.flPreferences.setGridDistances')

    def sourceMetricsSamples(self) -> str:
        'QString sourceMetricsSamples()'
        _unavailable('fontlab.flPreferences.sourceMetricsSamples')

    def tracer2options_precision(self, curve_fit: float) -> float:
        'double tracer2options_precision(double curve_fit)'
        _unavailable('fontlab.flPreferences.tracer2options_precision')

    def tracer2options_smoothness(self, straighten_angle: int) -> float:
        'double tracer2options_smoothness(int straighten_angle)'
        _unavailable('fontlab.flPreferences.tracer2options_smoothness')

    def unicode2text(self, unc: int) -> str:
        'QString unicode2text(uint unc)'
        _unavailable('fontlab.flPreferences.unicode2text')

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
    'flProperty representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flProperty')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flProperty.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flProperty.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flProperty.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flProperty.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flProperty.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flProperty.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flProperty.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flProperty.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flProperty.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flProperty.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flProperty.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flProperty.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flProperty.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flProperty.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flProperty.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flProperty.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flProperty.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flProperty.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flProperty.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flProperty.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flProperty.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flProperty.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flProperty.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flProperty.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flProperty.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flProperty.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flProperty.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flProperty.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flProperty.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flProperty.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flProperty.update')

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
    'flPropertyDouble representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flPropertyDouble')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flPropertyDouble.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flPropertyDouble.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flPropertyDouble.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flPropertyDouble.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flPropertyDouble.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flPropertyDouble.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flPropertyDouble.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flPropertyDouble.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flPropertyDouble.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flPropertyDouble.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flPropertyDouble.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flPropertyDouble.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flPropertyDouble.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flPropertyDouble.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flPropertyDouble.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flPropertyDouble.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flPropertyDouble.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flPropertyDouble.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flPropertyDouble.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flPropertyDouble.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flPropertyDouble.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flPropertyDouble.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flPropertyDouble.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flPropertyDouble.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flPropertyDouble.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flPropertyDouble.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flPropertyDouble.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flPropertyDouble.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flPropertyDouble.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flPropertyDouble.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flPropertyDouble.update')

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
    'flPropertyPoint representation\n\nConstructors:\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flPropertyPoint')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flPropertyPoint.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flPropertyPoint.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flPropertyPoint.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flPropertyPoint.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flPropertyPoint.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flPropertyPoint.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flPropertyPoint.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flPropertyPoint.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flPropertyPoint.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flPropertyPoint.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flPropertyPoint.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flPropertyPoint.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flPropertyPoint.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flPropertyPoint.getPropertyInt')

    def hasExpression(self) -> bool:
        'bool hasExpression()'
        _unavailable('fontlab.flPropertyPoint.hasExpression')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flPropertyPoint.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flPropertyPoint.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flPropertyPoint.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flPropertyPoint.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flPropertyPoint.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flPropertyPoint.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flPropertyPoint.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flPropertyPoint.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flPropertyPoint.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flPropertyPoint.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flPropertyPoint.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flPropertyPoint.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flPropertyPoint.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flPropertyPoint.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flPropertyPoint.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flPropertyPoint.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flPropertyPoint.update')

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
    'flSearchInfo representation\n\nConstructors:\n  flSearchInfo()\n  flSearchInfo(flObject)\n  flSearchInfo(flSearchInfo)\n  flSearchInfo(QTransform)\n  flSearchInfo(QTransform, flObject glyph_info)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flSearchInfo')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flSearchInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flSearchInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flSearchInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flSearchInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flSearchInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flSearchInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flSearchInfo.cloneObject')

    def combine(self, transform: QTransform) -> Any:
        'combine(QTransform transform)'
        _unavailable('fontlab.flSearchInfo.combine')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flSearchInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flSearchInfo.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flSearchInfo.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flSearchInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flSearchInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flSearchInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flSearchInfo.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flSearchInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flSearchInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flSearchInfo.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flSearchInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flSearchInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flSearchInfo.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flSearchInfo.isEqual')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flSearchInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flSearchInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flSearchInfo.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flSearchInfo.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flSearchInfo.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flSearchInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flSearchInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flSearchInfo.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flSearchInfo.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flSearchInfo.update')

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
    'flShape representation\n\nConstructors:\n  flShape()\n  flShape(flObject)\n  flShape(flShapeData)\n  flShape(flSticker)\n  flShape(QImage)\n  flShape(fgShape)\n  flShape(flShapeBuilder)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flShape')

    def activateBuilder(self) -> Any:
        'activateBuilder()'
        _unavailable('fontlab.flShape.activateBuilder')

    def addContour(self, arg0: flContour) -> Any:
        'addContour(flContour)'
        _unavailable('fontlab.flShape.addContour')

    def addContours(self, *args: Any, **kwargs: Any) -> Any:
        'addContours(list(flContour))'
        _unavailable('fontlab.flShape.addContours')

    def appendAnchor(self, node: flNode, guideline: flObject) -> Any:
        'appendAnchor(flAnchor) | void appendAnchor(flNode node, flObject guideline)'
        _unavailable('fontlab.flShape.appendAnchor')

    def applyTransform(self, *args: Any, **kwargs: Any) -> Any:
        'applyTransform([QTransform transform])'
        _unavailable('fontlab.flShape.applyTransform')

    def assign(self, arg0: fgShape) -> Any:
        'assign(fgShape)'
        _unavailable('fontlab.flShape.assign')

    def assignStyle(self, arg0: flShape) -> Any:
        'assignStyle(flShape)'
        _unavailable('fontlab.flShape.assignStyle')

    def bindDependencies(self) -> Any:
        'bindDependencies()'
        _unavailable('fontlab.flShape.bindDependencies')

    def canUngroup(self) -> bool:
        'bool canUngroup()'
        _unavailable('fontlab.flShape.canUngroup')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flShape.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flShape.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flShape.clearAboveHistory')

    def clearContours(self) -> Any:
        'clearContours()'
        _unavailable('fontlab.flShape.clearContours')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flShape.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flShape.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flShape.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flShape.cloneObject')

    def cloneTopLevel(self) -> flShape:
        'flShape cloneTopLevel()'
        _unavailable('fontlab.flShape.cloneTopLevel')

    def contains(self, arg0: QPointF) -> bool:
        'bool contains(QPointF)'
        _unavailable('fontlab.flShape.contains')

    def containsInInclude(self, id: Any) -> bool:
        'bool containsInInclude(flShape | uint id)'
        _unavailable('fontlab.flShape.containsInInclude')

    def convertToFgShape(self, arg0: fgShape) -> Any:
        'convertToFgShape(fgShape)'
        _unavailable('fontlab.flShape.convertToFgShape')

    def copyToFgShape(self, arg0: fgShape) -> Any:
        'copyToFgShape(fgShape)'
        _unavailable('fontlab.flShape.copyToFgShape')

    def createInstance(self) -> flShape:
        'flShape createInstance()'
        _unavailable('fontlab.flShape.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flShape.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flShape.currentHistoryState')

    def cutContour(self, *args: Any, **kwargs: Any) -> Any:
        '(list(flContour) inner, list(flContour) outer)/Nothing cutContour(flContour, QTransform)'
        _unavailable('fontlab.flShape.cutContour')

    def decomposite(self) -> Any:
        'decomposite()'
        _unavailable('fontlab.flShape.decomposite')

    def eject(self, arg0: flShape) -> Any:
        'eject(flShape)'
        _unavailable('fontlab.flShape.eject')

    def ejectTo(self, clone: Any = ...) -> Any:
        'list(flShape) ejectTo([bool clone =true[, bool apply_tx =true]])'
        _unavailable('fontlab.flShape.ejectTo')

    def ensurePaths(self) -> Any:
        'ensurePaths()'
        _unavailable('fontlab.flShape.ensurePaths')

    def findNode(self, arg0: str) -> flNode:
        'flNode findNode(QString)'
        _unavailable('fontlab.flShape.findNode')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flShape.flag')

    def getActiveComposite(self) -> Any:
        'flShape/Nothing getActiveComposite()'
        _unavailable('fontlab.flShape.getActiveComposite')

    def getActiveIncludeShape(self) -> Any:
        'flShape/Nothing getActiveIncludeShape()'
        _unavailable('fontlab.flShape.getActiveIncludeShape')

    def getAnchorForObject(self, arg0: flObject) -> Any:
        'flAnchor/Nothing getAnchorForObject(flObject)'
        _unavailable('fontlab.flShape.getAnchorForObject')

    def getAnchors(self) -> Any:
        'list(flAnchor)/Nothing getAnchors()'
        _unavailable('fontlab.flShape.getAnchors')

    def getCompositesBounding(self) -> QRectF:
        'QRectF getCompositesBounding()'
        _unavailable('fontlab.flShape.getCompositesBounding')

    def getContours(self) -> Any:
        'list(flContour) getContours()'
        _unavailable('fontlab.flShape.getContours')

    def getNodeAt(self, index: int, nodetype: Any) -> Any:
        'flNode/Nothing getNodeAt(int index, flNode::NodeType nodetype)'
        _unavailable('fontlab.flShape.getNodeAt')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flShape.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flShape.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flShape.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flShape.getPropertyInt')

    def getSelected(self, SelectionMode: Any) -> Any:
        'list(flContour)/Nothing getSelected(SelectionMode)'
        _unavailable('fontlab.flShape.getSelected')

    def getSquare(self) -> float:
        'double getSquare()'
        _unavailable('fontlab.flShape.getSquare')

    def getTransformationPermissions(self, *args: Any, **kwargs: Any) -> Any:
        '(bool enbl_horz, bool enbl_vert, bool enbl_rotation) getTransformationPermissions()'
        _unavailable('fontlab.flShape.getTransformationPermissions')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flShape.hasHistoryState')

    def hasImage(self, bitmap_only: bool) -> bool:
        'bool hasImage(bool bitmap_only)'
        _unavailable('fontlab.flShape.hasImage')

    def hasSelected(self, SelectionMode: Any) -> bool:
        'bool hasSelected(SelectionMode)'
        _unavailable('fontlab.flShape.hasSelected')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flShape.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flShape.historyStates')

    def horzReflection(self) -> bool:
        'bool horzReflection()'
        _unavailable('fontlab.flShape.horzReflection')

    def include(self, *args: Any, **kwargs: Any) -> Any:
        'include(list(flShape) | flShape, [ flLayer remove_from])'
        _unavailable('fontlab.flShape.include')

    def includeTo(self, ix: int, arg1: flShape) -> Any:
        'includeTo(int ix, flShape)'
        _unavailable('fontlab.flShape.includeTo')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flShape.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flShape.initialHistoryState')

    def inkBox(self, tx: Any = ...) -> QRectF:
        'QRectF inkBox([QTransform tx = QTransform()])'
        _unavailable('fontlab.flShape.inkBox')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flShape.instanceType')

    def isCompatible(self, arg0: flShape, strong: bool) -> bool:
        'bool isCompatible(flShape, bool strong)'
        _unavailable('fontlab.flShape.isCompatible')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flShape.isEqual')

    def isShape(self, arg0: flObject) -> bool:
        'bool isShape(flObject)'
        _unavailable('fontlab.flShape.isShape')

    def mergeTopComposite(self) -> Any:
        'mergeTopComposite()'
        _unavailable('fontlab.flShape.mergeTopComposite')

    def prepareTransformationData(self) -> Any:
        'prepareTransformationData()'
        _unavailable('fontlab.flShape.prepareTransformationData')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flShape.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flShape.remove')

    def removeAnchor(self, arg0: flAnchor) -> Any:
        'removeAnchor(flAnchor)'
        _unavailable('fontlab.flShape.removeAnchor')

    def removeAnchorsForObject(self, arg0: flObject) -> Any:
        'removeAnchorsForObject(flObject)'
        _unavailable('fontlab.flShape.removeAnchorsForObject')

    def removeBackContour(self) -> Any:
        'removeBackContour()'
        _unavailable('fontlab.flShape.removeBackContour')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flShape.removeChild')

    def removeContour(self, arg0: flContour) -> Any:
        'removeContour(flContour)'
        _unavailable('fontlab.flShape.removeContour')

    def removeContours(self, *args: Any, **kwargs: Any) -> Any:
        'removeContours(list(flContour))'
        _unavailable('fontlab.flShape.removeContours')

    def replaceInclude(self, old_shape: flShape, new_shape: flShape) -> Any:
        'replaceInclude(flShape old_shape, flShape new_shape)'
        _unavailable('fontlab.flShape.replaceInclude')

    def resetInkBox(self) -> Any:
        'resetInkBox()'
        _unavailable('fontlab.flShape.resetInkBox')

    def resetTransformationData(self) -> Any:
        'resetTransformationData()'
        _unavailable('fontlab.flShape.resetTransformationData')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flShape.restoreHistoryState')

    def selectAllData(self) -> Any:
        'selectAllData()'
        _unavailable('fontlab.flShape.selectAllData')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flShape.setFlag')

    def setIncludes(self, *args: Any, **kwargs: Any) -> Any:
        'setIncludes(list(flShape))'
        _unavailable('fontlab.flShape.setIncludes')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flShape.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flShape.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flShape.setPropertyInt')

    def setReflected(self, *args: Any, **kwargs: Any) -> Any:
        'setReflected(bool, bool)'
        _unavailable('fontlab.flShape.setReflected')

    def simpleShape(self) -> bool:
        'bool simpleShape()'
        _unavailable('fontlab.flShape.simpleShape')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flShape.tag')

    def unselectAllNodes(self) -> Any:
        'unselectAllNodes()'
        _unavailable('fontlab.flShape.unselectAllNodes')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flShape.update')

    def vertReflection(self) -> bool:
        'bool vertReflection()'
        _unavailable('fontlab.flShape.vertReflection')

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
    'flShapeBuilder representation\n\nConstructors:\n  flShapeBuilder()\n  flShapeBuilder(flShapeBuilder)\n  flShapeBuilder(flObject)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flShapeBuilder')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flShapeBuilder.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeBuilder.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flShapeBuilder.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flShapeBuilder.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flShapeBuilder.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flShapeBuilder.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flShapeBuilder.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flShapeBuilder.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flShapeBuilder.currentHistoryState')

    def deactivate(self) -> Any:
        'deactivate()'
        _unavailable('fontlab.flShapeBuilder.deactivate')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flShapeBuilder.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flShapeBuilder.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flShapeBuilder.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flShapeBuilder.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flShapeBuilder.getPropertyInt')

    def getSmartNodes(self) -> Any:
        'list(flNode)/Nothing getSmartNodes()'
        _unavailable('fontlab.flShapeBuilder.getSmartNodes')

    def hasFeature(self, BuilderFeatures: Any) -> bool:
        'bool hasFeature(BuilderFeatures)'
        _unavailable('fontlab.flShapeBuilder.hasFeature')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeBuilder.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flShapeBuilder.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flShapeBuilder.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flShapeBuilder.independedAll')

    def init(self) -> Any:
        'init()'
        _unavailable('fontlab.flShapeBuilder.init')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flShapeBuilder.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flShapeBuilder.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flShapeBuilder.isEqual')

    def prepareTransformationData(self) -> Any:
        'prepareTransformationData()'
        _unavailable('fontlab.flShapeBuilder.prepareTransformationData')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flShapeBuilder.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flShapeBuilder.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flShapeBuilder.removeChild')

    def resetTransformationData(self) -> Any:
        'resetTransformationData()'
        _unavailable('fontlab.flShapeBuilder.resetTransformationData')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeBuilder.restoreHistoryState')

    def setDestShape(self, arg0: flShape) -> Any:
        'setDestShape(flShape)'
        _unavailable('fontlab.flShapeBuilder.setDestShape')

    def setDestShapeData(self, arg0: flShapeData) -> Any:
        'setDestShapeData(flShapeData)'
        _unavailable('fontlab.flShapeBuilder.setDestShapeData')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flShapeBuilder.setFlag')

    def setOwnerLayer(self, arg0: flObject) -> Any:
        'setOwnerLayer(flObject)'
        _unavailable('fontlab.flShapeBuilder.setOwnerLayer')

    def setOwnerShapeData(self, arg0: flObject) -> Any:
        'setOwnerShapeData(flObject)'
        _unavailable('fontlab.flShapeBuilder.setOwnerShapeData')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flShapeBuilder.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flShapeBuilder.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flShapeBuilder.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flShapeBuilder.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flShapeBuilder.update')

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
    'flShapeData representation\n\nConstructors:\n  flShapeData()\n  flShapeData(flObject)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flShapeData')

    def addContour(self, arg0: flContour) -> Any:
        'addContour(flContour)'
        _unavailable('fontlab.flShapeData.addContour')

    def addContours(self, *args: Any, **kwargs: Any) -> Any:
        'addContours(list(flContour))'
        _unavailable('fontlab.flShapeData.addContours')

    def arrangeContours(self) -> bool:
        'bool arrangeContours()'
        _unavailable('fontlab.flShapeData.arrangeContours')

    def assignContours(self, *args: Any, **kwargs: Any) -> Any:
        'QMap<objId, flContour> assignContours(list(flContour)) | Nothing assignContours(fgShape)'
        _unavailable('fontlab.flShapeData.assignContours')

    def bindDependencies(self) -> Any:
        'bindDependencies()'
        _unavailable('fontlab.flShapeData.bindDependencies')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flShapeData.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeData.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flShapeData.clearAboveHistory')

    def clearContours(self) -> Any:
        'clearContours()'
        _unavailable('fontlab.flShapeData.clearContours')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flShapeData.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flShapeData.clearFlags')

    def clearIncludesList(self) -> Any:
        'clearIncludesList()'
        _unavailable('fontlab.flShapeData.clearIncludesList')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flShapeData.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flShapeData.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flShapeData.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flShapeData.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flShapeData.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flShapeData.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flShapeData.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flShapeData.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flShapeData.getPropertyInt')

    def goDown(self, arg0: flShape) -> bool:
        'bool goDown(flShape)'
        _unavailable('fontlab.flShapeData.goDown')

    def goUp(self, arg0: flShape) -> bool:
        'bool goUp(flShape)'
        _unavailable('fontlab.flShapeData.goUp')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeData.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flShapeData.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flShapeData.historyStates')

    def includesList(self) -> Any:
        'list(flShape) includesList()'
        _unavailable('fontlab.flShapeData.includesList')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flShapeData.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flShapeData.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flShapeData.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flShapeData.isEqual')

    def prepareTransformationData(self) -> Any:
        'prepareTransformationData()'
        _unavailable('fontlab.flShapeData.prepareTransformationData')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flShapeData.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flShapeData.remove')

    def removeAnchor(self, arg0: flAnchor) -> Any:
        'removeAnchor(flAnchor)'
        _unavailable('fontlab.flShapeData.removeAnchor')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flShapeData.removeChild')

    def removeContour(self, arg0: flContour) -> Any:
        'removeContour(flContour)'
        _unavailable('fontlab.flShapeData.removeContour')

    def resetTransformationData(self) -> Any:
        'resetTransformationData()'
        _unavailable('fontlab.flShapeData.resetTransformationData')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeData.restoreHistoryState')

    def sendToBack(self, arg0: flShape) -> bool:
        'bool sendToBack(flShape)'
        _unavailable('fontlab.flShapeData.sendToBack')

    def sendToFront(self, arg0: flShape) -> bool:
        'bool sendToFront(flShape)'
        _unavailable('fontlab.flShapeData.sendToFront')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flShapeData.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flShapeData.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flShapeData.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flShapeData.setPropertyInt')

    def sortContours(self, action: bool) -> Any:
        'sortContours(bool action)'
        _unavailable('fontlab.flShapeData.sortContours')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flShapeData.tag')

    def takeIncludesList(self) -> Any:
        'list(flShape) takeIncludesList()'
        _unavailable('fontlab.flShapeData.takeIncludesList')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flShapeData.update')

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
    'flShapeInfo representation\n\nConstructors:\n  flShapeInfo()\n  flShapeInfo(flObject)\n  flShapeInfo(flShapeInfo)\n  flShapeInfo(flShape, flSearchInfo)\n  flShapeInfo(flShape, QTransform)\n  flShapeInfo(flShape, QTransform, QList<flShapeInfo> composites)\n  flShapeInfo(flShape, QTransform, flObject glyph_info, QList<flShapeInfo> composites)\n  flShapeInfo(flShape, flLayer, QTransform)\n  flShapeInfo(flShape, flLayer, flObject glyph_info[, QTransform transform=QTransform()[, QList<flShapeInfo> composites=QList<flShapeInfo>()]])\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flShapeInfo')

    def appendComposite(self, arg0: flShapeInfo) -> Any:
        'appendComposite(flShapeInfo)'
        _unavailable('fontlab.flShapeInfo.appendComposite')

    def boundingBox(self) -> QRectF:
        'QRectF boundingBox()'
        _unavailable('fontlab.flShapeInfo.boundingBox')

    def brectOnCanvas(self) -> QRectF:
        'QRectF brectOnCanvas()'
        _unavailable('fontlab.flShapeInfo.brectOnCanvas')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flShapeInfo.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeInfo.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flShapeInfo.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flShapeInfo.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flShapeInfo.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flShapeInfo.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flShapeInfo.cloneObject')

    def combine(self, transform: QTransform) -> Any:
        'combine(QTransform transform)'
        _unavailable('fontlab.flShapeInfo.combine')

    def compositesTransform(self) -> QTransform:
        'QTransform compositesTransform()'
        _unavailable('fontlab.flShapeInfo.compositesTransform')

    def contains(self, s: Any = ...) -> bool:
        'bool contains(QPointF canvas_pos[, double s=1])'
        _unavailable('fontlab.flShapeInfo.contains')

    def createInstance(self) -> flShapeInfo:
        'flShapeInfo createInstance()'
        _unavailable('fontlab.flShapeInfo.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flShapeInfo.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flShapeInfo.currentHistoryState')

    def findNode(self, arg0: QPointF) -> flNode:
        'flNode findNode(QPointF)'
        _unavailable('fontlab.flShapeInfo.findNode')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flShapeInfo.flag')

    def getContoursInfo(self) -> list[flObject]:
        'QList<flObject> getContoursInfo()'
        _unavailable('fontlab.flShapeInfo.getContoursInfo')

    def getHitIncludedShape(self, canvas_pos: QPointF, to_bottom: Any = ...) -> Any:
        'flShapeInfo/Nothing getHitIncludedShape(QPointF canvas_pos, double scale[, bool to_bottom=false])'
        _unavailable('fontlab.flShapeInfo.getHitIncludedShape')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flShapeInfo.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flShapeInfo.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flShapeInfo.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flShapeInfo.getPropertyInt')

    def hasAboveComposites(self) -> bool:
        'bool hasAboveComposites()'
        _unavailable('fontlab.flShapeInfo.hasAboveComposites')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeInfo.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flShapeInfo.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flShapeInfo.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flShapeInfo.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flShapeInfo.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flShapeInfo.instanceType')

    def isContentLockedSibling(self) -> bool:
        'bool isContentLockedSibling()'
        _unavailable('fontlab.flShapeInfo.isContentLockedSibling')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flShapeInfo.isEqual')

    def move(self, arg0: QPointF) -> QRectF:
        'QRectF move(QPointF)'
        _unavailable('fontlab.flShapeInfo.move')

    def ownerComposite(self) -> flShape:
        'flShape ownerComposite()'
        _unavailable('fontlab.flShapeInfo.ownerComposite')

    def ownerCompositeInfo(self) -> flShapeInfo:
        'flShapeInfo ownerCompositeInfo()'
        _unavailable('fontlab.flShapeInfo.ownerCompositeInfo')

    def pushFrontComposite(self, arg0: flShapeInfo) -> Any:
        'pushFrontComposite(flShapeInfo)'
        _unavailable('fontlab.flShapeInfo.pushFrontComposite')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flShapeInfo.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flShapeInfo.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flShapeInfo.removeChild')

    def replaceShape(self, arg0: flShape) -> Any:
        'replaceShape(flShape)'
        _unavailable('fontlab.flShapeInfo.replaceShape')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flShapeInfo.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flShapeInfo.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flShapeInfo.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flShapeInfo.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flShapeInfo.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flShapeInfo.tag')

    def takeFirstComposite(self) -> flShapeInfo:
        'flShapeInfo takeFirstComposite()'
        _unavailable('fontlab.flShapeInfo.takeFirstComposite')

    def takeLastComposite(self) -> flShapeInfo:
        'flShapeInfo takeLastComposite()'
        _unavailable('fontlab.flShapeInfo.takeLastComposite')

    def toCanvasTransform(self) -> QTransform:
        'QTransform toCanvasTransform()'
        _unavailable('fontlab.flShapeInfo.toCanvasTransform')

    def toGlyphTransform(self) -> QTransform:
        'QTransform toGlyphTransform()'
        _unavailable('fontlab.flShapeInfo.toGlyphTransform')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flShapeInfo.update')

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
    'flSnapLine representation\n\nConstructors:\n  flSnapLine()\n  flSnapLine(flObject)\n  flSnapLine(flSnapLine)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flSnapLine')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flSnapLine.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flSnapLine.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flSnapLine.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flSnapLine.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flSnapLine.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flSnapLine.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flSnapLine.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flSnapLine.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flSnapLine.currentHistoryState')

    def distanceTo(self, arg0: QPointF, mode: int) -> float:
        'double distanceTo(QPointF, uint mode)'
        _unavailable('fontlab.flSnapLine.distanceTo')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flSnapLine.flag')

    def getHashCode(self) -> Any:
        'SnapHashCode getHashCode()'
        _unavailable('fontlab.flSnapLine.getHashCode')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flSnapLine.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flSnapLine.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flSnapLine.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flSnapLine.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flSnapLine.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flSnapLine.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flSnapLine.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flSnapLine.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flSnapLine.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flSnapLine.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flSnapLine.isEqual')

    def isSnapLine(self, arg0: flObject) -> bool:
        'bool isSnapLine(flObject)'
        _unavailable('fontlab.flSnapLine.isSnapLine')

    def offsetTo(self, arg0: QPointF, mode: int) -> QPointF:
        'QPointF offsetTo(QPointF, uint mode)'
        _unavailable('fontlab.flSnapLine.offsetTo')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flSnapLine.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flSnapLine.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flSnapLine.removeChild')

    def reset(self) -> Any:
        'reset()'
        _unavailable('fontlab.flSnapLine.reset')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flSnapLine.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flSnapLine.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flSnapLine.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flSnapLine.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flSnapLine.setPropertyInt')

    def setSnapFlag(self, role: int, snapFlags: int) -> Any:
        'setSnapFlag(uint role, uint snapFlags)'
        _unavailable('fontlab.flSnapLine.setSnapFlag')

    def setSnapFlagValue(self, role: int, bool: Any) -> Any:
        'setSnapFlagValue(uint role, bool)'
        _unavailable('fontlab.flSnapLine.setSnapFlagValue')

    def snapFlag(self, role: int) -> int:
        'uint snapFlag(uint role)'
        _unavailable('fontlab.flSnapLine.snapFlag')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flSnapLine.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flSnapLine.update')

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
    'flSnapObject representation\n\nConstructors:\n  flSnapObject()\n  flSnapObject(flObject)\n  flSnapObject(flSnapObject)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flSnapObject')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flSnapObject.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flSnapObject.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flSnapObject.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flSnapObject.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flSnapObject.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flSnapObject.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flSnapObject.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flSnapObject.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flSnapObject.currentHistoryState')

    def distanceTo(self, arg0: QPointF, mode: int) -> float:
        'double distanceTo(QPointF, uint mode)'
        _unavailable('fontlab.flSnapObject.distanceTo')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flSnapObject.flag')

    def getHashCode(self) -> Any:
        'SnapHashCode getHashCode()'
        _unavailable('fontlab.flSnapObject.getHashCode')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flSnapObject.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flSnapObject.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flSnapObject.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flSnapObject.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flSnapObject.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flSnapObject.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flSnapObject.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flSnapObject.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flSnapObject.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flSnapObject.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flSnapObject.isEqual')

    def offsetTo(self, arg0: QPointF, mode: int) -> QPointF:
        'QPointF offsetTo(QPointF, uint mode)'
        _unavailable('fontlab.flSnapObject.offsetTo')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flSnapObject.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flSnapObject.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flSnapObject.removeChild')

    def reset(self) -> Any:
        'reset()'
        _unavailable('fontlab.flSnapObject.reset')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flSnapObject.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flSnapObject.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flSnapObject.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flSnapObject.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flSnapObject.setPropertyInt')

    def setSnapFlag(self, role: int, snapFlags: int) -> Any:
        'setSnapFlag(uint role, uint snapFlags)'
        _unavailable('fontlab.flSnapObject.setSnapFlag')

    def setSnapFlagValue(self, role: int, bool: Any) -> Any:
        'setSnapFlagValue(uint role, bool)'
        _unavailable('fontlab.flSnapObject.setSnapFlagValue')

    def snapFlag(self, role: int) -> int:
        'uint snapFlag(uint role)'
        _unavailable('fontlab.flSnapObject.snapFlag')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flSnapObject.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flSnapObject.update')

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
    'snap object constants\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flSnaps')

    FastGuidelines: dict
    MarkerFlags: dict
    MarkerKey: dict
    SnapLineFlags: dict
    SnapMode: dict
    SnapStyle: dict
    ViewMode: dict

class flStem:
    'flStem representation\n\nConstructors:\n  flStem()\n  flStem(double _v[, QString _n = ])\n  flStem(fgStem)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flStem')

    def guaranteeName(self) -> Any:
        'guaranteeName()'
        _unavailable('fontlab.flStem.guaranteeName')

    def linear(self, upm: float, k: int) -> int:
        'int linear(double upm, int k)'
        _unavailable('fontlab.flStem.linear')

    def ppm(self, upm: float, k: int) -> int:
        'int ppm(double upm, int k)'
        _unavailable('fontlab.flStem.ppm')

    def tagsSet(self) -> Any:
        'QSet<QString>/Nothing tagsSet()'
        _unavailable('fontlab.flStem.tagsSet')

    def toStem(self, arg0: fgStem) -> Any:
        'toStem(fgStem)'
        _unavailable('fontlab.flStem.toStem')

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
    'flSticker representation\n\nConstructors:\n  flSticker()\n  flSticker(flObject)\n  flSticker(flSticker)\n  flSticker(QString)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flSticker')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flSticker.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flSticker.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flSticker.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flSticker.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flSticker.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flSticker.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flSticker.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flSticker.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flSticker.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flSticker.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flSticker.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flSticker.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flSticker.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flSticker.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flSticker.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flSticker.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flSticker.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flSticker.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flSticker.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flSticker.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flSticker.isEqual')

    def move(self, arg0: QPointF) -> Any:
        'move(QPointF)'
        _unavailable('fontlab.flSticker.move')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flSticker.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flSticker.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flSticker.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flSticker.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flSticker.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flSticker.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flSticker.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flSticker.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flSticker.tag')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flSticker.update')

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
    'flTTHCommand representation\n\nConstructors:\n  flTTHCommand() - default\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flTTHCommand')

    def fromString(self, arg0: str, itr: Any) -> bool:
        'bool fromString(QString, itr)'
        _unavailable('fontlab.flTTHCommand.fromString')

    def isDelta(self) -> bool:
        'bool isDelta()'
        _unavailable('fontlab.flTTHCommand.isDelta')

    def isFinal(self) -> bool:
        'bool isFinal()'
        _unavailable('fontlab.flTTHCommand.isFinal')

    def isHorizontal(self) -> bool:
        'bool isHorizontal()'
        _unavailable('fontlab.flTTHCommand.isHorizontal')

    def isVertical(self) -> bool:
        'bool isVertical()'
        _unavailable('fontlab.flTTHCommand.isVertical')

    def nodesCount(self) -> int:
        'int nodesCount()'
        _unavailable('fontlab.flTTHCommand.nodesCount')

    def parametersCount(self) -> int:
        'int parametersCount()'
        _unavailable('fontlab.flTTHCommand.parametersCount')

    def stemIndex(self) -> int:
        'int stemIndex()'
        _unavailable('fontlab.flTTHCommand.stemIndex')

    def zoneIndex(self) -> int:
        'int zoneIndex()'
        _unavailable('fontlab.flTTHCommand.zoneIndex')

    code: Any
    'int'
    parameters: Any
    'QList<QVariant>'
    point_names: Any
    'QList<QString>'

class flTextBlock:
    'flTextBlock representation\n\nConstructors:\n  flTextBlock()\n  flTextBlock(flObject)\n  flTextBlock(flTextBlock)\n  flTextBlock(flPackage, flTextObject[, int font_size=42[, int formatMode=tbfText[, QRectF canvas_rect=QRectF(0,0, 800,600)]]])\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flTextBlock')

    def activeObjectChanged(self) -> flNotifier:
        'flNotifier activeObjectChanged()'
        _unavailable('fontlab.flTextBlock.activeObjectChanged')

    def activeRowRect(self) -> QRectF:
        'QRectF activeRowRect()'
        _unavailable('fontlab.flTextBlock.activeRowRect')

    def addFeature(self, feature: str) -> Any:
        'addFeature(QString feature)'
        _unavailable('fontlab.flTextBlock.addFeature')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flTextBlock.changed')

    def charsCount(self) -> int:
        'int charsCount()'
        _unavailable('fontlab.flTextBlock.charsCount')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flTextBlock.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flTextBlock.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flTextBlock.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flTextBlock.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flTextBlock.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flTextBlock.cloneObject')

    def createInstance(self) -> flTextBlock:
        'flTextBlock createInstance()'
        _unavailable('fontlab.flTextBlock.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flTextBlock.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flTextBlock.currentHistoryState')

    def drawContent(self, *args: Any, **kwargs: Any) -> Any:
        'drawContent(QPainter*, flCanvas, QRectF painted_nodes_screen_rect)'
        _unavailable('fontlab.flTextBlock.drawContent')

    def features(self) -> Any:
        'list(QString) features()'
        _unavailable('fontlab.flTextBlock.features')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flTextBlock.flag')

    def formatChanged(self) -> flNotifier:
        'flNotifier formatChanged()'
        _unavailable('fontlab.flTextBlock.formatChanged')

    def getActiveGlyph(self) -> Any:
        'flGlyphInfo/Nothing getActiveGlyph()'
        _unavailable('fontlab.flTextBlock.getActiveGlyph')

    def getAllGlyphs(self, line_index: Any = ...) -> Any:
        'list(flGlyphInfo)/Nothing getAllGlyphs([int line_index = -1])'
        _unavailable('fontlab.flTextBlock.getAllGlyphs')

    def getCurrentPosition(self) -> QPointF:
        'QPointF getCurrentPosition()'
        _unavailable('fontlab.flTextBlock.getCurrentPosition')

    def getGlyphAt(self, glyph_index: int) -> Any:
        'flGlyphInfo/Nothinf getGlyphAt(int glyph_index)'
        _unavailable('fontlab.flTextBlock.getGlyphAt')

    def getGlyphInfo(self, *args: Any, **kwargs: Any) -> Any:
        'flGlyphInfo/Nothing getGlyphInfo(fgSymbol, &)'
        _unavailable('fontlab.flTextBlock.getGlyphInfo')

    def getGlyphTransform(self, glyph_index: int) -> QTransform:
        'QTransform getGlyphTransform(int glyph_index)'
        _unavailable('fontlab.flTextBlock.getGlyphTransform')

    def getGlyphsInLine(self, lineIndex: Any) -> Any:
        'list(flGlyphInfo)/Nothing getGlyphsInLine(flGlyphInfo | int lineIndex)'
        _unavailable('fontlab.flTextBlock.getGlyphsInLine')

    def getHitGlyph(self, canvas_pos: QPointF) -> Any:
        'flGlyphInfo/Nothing getHitGlyph(QPointF canvas_pos)'
        _unavailable('fontlab.flTextBlock.getHitGlyph')

    def getHitToShapeGlyph(self, canvas_pos: QPointF) -> Any:
        'flGlyphInfo/Nothing getHitToShapeGlyph(QPointF canvas_pos)'
        _unavailable('fontlab.flTextBlock.getHitToShapeGlyph')

    def getHitToShapes(self, canvas_pos: QPointF) -> Any:
        'list(flContourInfo)/Nothing getHitToShapes(QPointF canvas_pos)'
        _unavailable('fontlab.flTextBlock.getHitToShapes')

    def getIntersectsGlyphs(self, canvas_rect: QRectF) -> Any:
        'list(flGlyphInfo)/Nothing getIntersectsGlyphs(QRectF canvas_rect)'
        _unavailable('fontlab.flTextBlock.getIntersectsGlyphs')

    def getLineIndex(self, glyph_index: int) -> int:
        'int getLineIndex(int glyph_index)'
        _unavailable('fontlab.flTextBlock.getLineIndex')

    def getLineLocation(self, glyph_info: flGlyphInfo) -> int:
        'int getLineLocation(flGlyphInfo glyph_info)'
        _unavailable('fontlab.flTextBlock.getLineLocation')

    def getMouseHitNode(self) -> Any:
        'flNodeInfo/Nothing getMouseHitNode()'
        _unavailable('fontlab.flTextBlock.getMouseHitNode')

    def getNearbyGlyphs(self, text_block_point: QPointF, max_dist: float) -> Any:
        'list(flGlyphInfo)/Nothing getNearbyGlyphs(QPointF text_block_point, double max_dist)'
        _unavailable('fontlab.flTextBlock.getNearbyGlyphs')

    def getNextGlyphInLine(self, glyph_index: int) -> Any:
        'flGlyphInfo/Nothing getNextGlyphInLine(int glyph_index)'
        _unavailable('fontlab.flTextBlock.getNextGlyphInLine')

    def getPrevGlyphInLine(self, glyph_index: int) -> Any:
        'flGlyphInfo/Nothing getPrevGlyphInLine(int glyph_index)'
        _unavailable('fontlab.flTextBlock.getPrevGlyphInLine')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flTextBlock.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flTextBlock.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flTextBlock.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flTextBlock.getPropertyInt')

    def getScvNode(self) -> Any:
        'flNodeInfo/Nothing getScvNode()'
        _unavailable('fontlab.flTextBlock.getScvNode')

    def getSelectedCharacters(self) -> Any:
        'fgSymbolList/Nothing getSelectedCharacters()'
        _unavailable('fontlab.flTextBlock.getSelectedCharacters')

    def getSelectedGlyphs(self) -> Any:
        'list(flGlyphInfo)/Nothing getSelectedGlyphs()'
        _unavailable('fontlab.flTextBlock.getSelectedGlyphs')

    def glyphsBoundsOnCanvas(self, EditMode: Any) -> QRectF:
        'QRectF glyphsBoundsOnCanvas(EditMode)'
        _unavailable('fontlab.flTextBlock.glyphsBoundsOnCanvas')

    def glyphsChanged(self) -> Any:
        'glyphsChanged()'
        _unavailable('fontlab.flTextBlock.glyphsChanged')

    def glyphsCount(self) -> int:
        'int glyphsCount()'
        _unavailable('fontlab.flTextBlock.glyphsCount')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flTextBlock.hasHistoryState')

    def hasHoveredNodeEdit(self) -> bool:
        'bool hasHoveredNodeEdit()'
        _unavailable('fontlab.flTextBlock.hasHoveredNodeEdit')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flTextBlock.haveObject')

    def haveText(self) -> bool:
        'bool haveText()'
        _unavailable('fontlab.flTextBlock.haveText')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flTextBlock.historyStates')

    def hoveredNodeEdit(self) -> flNodeInfo:
        'flNodeInfo hoveredNodeEdit()'
        _unavailable('fontlab.flTextBlock.hoveredNodeEdit')

    def hoveredNodeEditDetails(self) -> Any:
        'HoveredInfoDetails hoveredNodeEditDetails()'
        _unavailable('fontlab.flTextBlock.hoveredNodeEditDetails')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flTextBlock.independedAll')

    def init(self, canvas: flCanvas) -> Any:
        'init(flCanvas& canvas)'
        _unavailable('fontlab.flTextBlock.init')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flTextBlock.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flTextBlock.instanceType')

    def isAltPressed(self) -> bool:
        'bool isAltPressed()'
        _unavailable('fontlab.flTextBlock.isAltPressed')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flTextBlock.isEqual')

    def isFramed(self) -> bool:
        'bool isFramed()'
        _unavailable('fontlab.flTextBlock.isFramed')

    def isMetaPressed(self) -> bool:
        'bool isMetaPressed()'
        _unavailable('fontlab.flTextBlock.isMetaPressed')

    def keyPressEvent(self, *args: Any, **kwargs: Any) -> Any:
        'bool keyPressEvent(QKeyEvent*)'
        _unavailable('fontlab.flTextBlock.keyPressEvent')

    def lastCharIndex(self) -> int:
        'int lastCharIndex()'
        _unavailable('fontlab.flTextBlock.lastCharIndex')

    def lastIndex(self) -> int:
        'int lastIndex()'
        _unavailable('fontlab.flTextBlock.lastIndex')

    def mouseDoubleClickEvent(self, *args: Any, **kwargs: Any) -> Any:
        'bool mouseDoubleClickEvent(QMouseEvent*)'
        _unavailable('fontlab.flTextBlock.mouseDoubleClickEvent')

    def mouseMoveEvent(self, *args: Any, **kwargs: Any) -> Any:
        'bool mouseMoveEvent(QMouseEvent*)'
        _unavailable('fontlab.flTextBlock.mouseMoveEvent')

    def mousePressEvent(self, *args: Any, **kwargs: Any) -> Any:
        'bool mousePressEvent(QMouseEvent*)'
        _unavailable('fontlab.flTextBlock.mousePressEvent')

    def mouseReleaseEvent(self, *args: Any, **kwargs: Any) -> Any:
        'bool mouseReleaseEvent(QMouseEvent*)'
        _unavailable('fontlab.flTextBlock.mouseReleaseEvent')

    def paintedNodesScreenRect(self) -> QRectF:
        'QRectF paintedNodesScreenRect()'
        _unavailable('fontlab.flTextBlock.paintedNodesScreenRect')

    def paragraphBlock(self) -> fgParagraphBlock:
        'fgParagraphBlock paragraphBlock()'
        _unavailable('fontlab.flTextBlock.paragraphBlock')

    def parentTextBlock(self) -> flTextBlock:
        'flTextBlock parentTextBlock()'
        _unavailable('fontlab.flTextBlock.parentTextBlock')

    def reformat(self) -> Any:
        'reformat()'
        _unavailable('fontlab.flTextBlock.reformat')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flTextBlock.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flTextBlock.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flTextBlock.removeChild')

    def removeFeature(self, feature: str) -> Any:
        'removeFeature(QString feature)'
        _unavailable('fontlab.flTextBlock.removeFeature')

    def removeFeatures(self) -> Any:
        'removeFeatures()'
        _unavailable('fontlab.flTextBlock.removeFeatures')

    def removedFromCanvas(self) -> Any:
        'removedFromCanvas()'
        _unavailable('fontlab.flTextBlock.removedFromCanvas')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flTextBlock.restoreHistoryState')

    def setActiveGlyph(self, arg0: flGlyphInfo) -> Any:
        'setActiveGlyph(flGlyphInfo)'
        _unavailable('fontlab.flTextBlock.setActiveGlyph')

    def setAltPressed(self, redraw: Any = ...) -> Any:
        'setAltPressed(bool b[, bool redraw = true])'
        _unavailable('fontlab.flTextBlock.setAltPressed')

    def setCheckMouseHoverNode(self, bool: Any) -> Any:
        'setCheckMouseHoverNode(bool)'
        _unavailable('fontlab.flTextBlock.setCheckMouseHoverNode')

    def setExclusiveEditing(self, bool: Any) -> Any:
        'setExclusiveEditing(bool)'
        _unavailable('fontlab.flTextBlock.setExclusiveEditing')

    def setFeatures(self, *args: Any, **kwargs: Any) -> Any:
        'setFeatures(list(QString), bool reformat)'
        _unavailable('fontlab.flTextBlock.setFeatures')

    def setFixedHeight(self, *args: Any, **kwargs: Any) -> Any:
        'setFixedHeight(bool, bool)'
        _unavailable('fontlab.flTextBlock.setFixedHeight')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flTextBlock.setFlag')

    def setFrameSize(self, canvas_size: QSizeF) -> Any:
        'setFrameSize(QSizeF canvas_size)'
        _unavailable('fontlab.flTextBlock.setFrameSize')

    def setFrameWidth(self, double: Any) -> Any:
        'setFrameWidth(double)'
        _unavailable('fontlab.flTextBlock.setFrameWidth')

    def setLeftMetric(self, glyph_info: flGlyphInfo, measurement: bool) -> Any:
        'setLeftMetric(flGlyphInfo glyph_info, bool measurement)'
        _unavailable('fontlab.flTextBlock.setLeftMetric')

    def setMetaPressed(self, redraw: Any = ...) -> Any:
        'setMetaPressed(bool b[, bool redraw = true])'
        _unavailable('fontlab.flTextBlock.setMetaPressed')

    def setParentTextBlock(self, arg0: flTextBlock) -> Any:
        'setParentTextBlock(flTextBlock)'
        _unavailable('fontlab.flTextBlock.setParentTextBlock')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flTextBlock.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flTextBlock.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flTextBlock.setPropertyInt')

    def setRightMetric(self, arg0: QPointF, glyph_info: flGlyphInfo, measurement: bool) -> Any:
        'setRightMetric(QPointF, flGlyphInfo glyph_info, bool measurement)'
        _unavailable('fontlab.flTextBlock.setRightMetric')

    def setShowCursor(self, bool: Any) -> Any:
        'setShowCursor(bool)'
        _unavailable('fontlab.flTextBlock.setShowCursor')

    def setShowNodes(self, bool: Any) -> Any:
        'setShowNodes(bool)'
        _unavailable('fontlab.flTextBlock.setShowNodes')

    def setTextBlockMode(self, viewport_pos: Any = ...) -> Any:
        'setTextBlockMode(EditMode text_block_mode[, QPoint viewport_pos=QPoint()])'
        _unavailable('fontlab.flTextBlock.setTextBlockMode')

    def symbolList(self) -> fgSymbolList:
        'fgSymbolList symbolList()'
        _unavailable('fontlab.flTextBlock.symbolList')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flTextBlock.tag')

    def textFits(self) -> bool:
        'bool textFits()'
        _unavailable('fontlab.flTextBlock.textFits')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flTextBlock.update')

    def updateSymbols(self) -> Any:
        'updateSymbols()'
        _unavailable('fontlab.flTextBlock.updateSymbols')

    def visibleShapes(self) -> Any:
        'list(flShape)/Nothing visibleShapes()'
        _unavailable('fontlab.flTextBlock.visibleShapes')

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
    'flTransform representation\n\nConstructors:\n  flTransform()\n  flTransform(flTransform)\n  flTransform(flObject)\n  flTransform(QTransform)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flTransform')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flTransform.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flTransform.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flTransform.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flTransform.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flTransform.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flTransform.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flTransform.cloneObject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flTransform.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flTransform.currentHistoryState')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flTransform.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flTransform.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flTransform.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flTransform.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flTransform.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flTransform.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flTransform.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flTransform.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flTransform.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flTransform.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flTransform.instanceType')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flTransform.isEqual')

    def map(self, *args: Any, **kwargs: Any) -> Any:
        'QPointF map(QPointF) | QLineF map(QLineF) | double map(double)'
        _unavailable('fontlab.flTransform.map')

    def mapRect(self, QRect: Any) -> QRectF:
        'QRectF mapRect(QRectF | QRect)'
        _unavailable('fontlab.flTransform.mapRect')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flTransform.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flTransform.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flTransform.removeChild')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flTransform.restoreHistoryState')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flTransform.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flTransform.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flTransform.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flTransform.setPropertyInt')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flTransform.tag')

    def translate(self, x: Any, y: float) -> None:
        'void translate(QPointF | double x, double y)'
        _unavailable('fontlab.flTransform.translate')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flTransform.update')

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
    'flVectorNode representation\n\nConstructors:\n  flVectorNode(flObject)\n  flVectorNode(flVectorNode)\n  flVectorNode(flGuideLine, QPointF)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flVectorNode')

    def angleTo(self, p: QPointF) -> float:
        'double angleTo(QPointF p)'
        _unavailable('fontlab.flVectorNode.angleTo')

    def applyTransform(self, arg0: QTransform) -> Any:
        'applyTransform(QTransform)'
        _unavailable('fontlab.flVectorNode.applyTransform')

    def canBeHobby(self) -> bool:
        'bool canBeHobby()'
        _unavailable('fontlab.flVectorNode.canBeHobby')

    def canBeSmooth(self) -> bool:
        'bool canBeSmooth()'
        _unavailable('fontlab.flVectorNode.canBeSmooth')

    def canCollapse(self) -> bool:
        'bool canCollapse()'
        _unavailable('fontlab.flVectorNode.canCollapse')

    def canImprove(self) -> bool:
        'bool canImprove()'
        _unavailable('fontlab.flVectorNode.canImprove')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flVectorNode.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flVectorNode.checkInitHistoryState')

    def checkVectors(self) -> bool:
        'bool checkVectors()'
        _unavailable('fontlab.flVectorNode.checkVectors')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flVectorNode.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flVectorNode.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flVectorNode.clearFlags')

    def clearStored(self) -> Any:
        'clearStored()'
        _unavailable('fontlab.flVectorNode.clearStored')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flVectorNode.clone')

    def cloneMapped(self, arg0: QTransform) -> flNode:
        'flNode cloneMapped(QTransform)'
        _unavailable('fontlab.flVectorNode.cloneMapped')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flVectorNode.cloneObject')

    def collapseHandles(self) -> bool:
        'bool collapseHandles()'
        _unavailable('fontlab.flVectorNode.collapseHandles')

    def convertToCurve(self, smooth: Any = ...) -> bool:
        'bool convertToCurve([bool smooth = false])'
        _unavailable('fontlab.flVectorNode.convertToCurve')

    def convertToCurves(self) -> bool:
        'bool convertToCurves()'
        _unavailable('fontlab.flVectorNode.convertToCurves')

    def convertToLine(self) -> bool:
        'bool convertToLine()'
        _unavailable('fontlab.flVectorNode.convertToLine')

    def copyFrom(self, withSelected: Any = ...) -> Any:
        'copyFrom(Node[, withSelected=False])'
        _unavailable('fontlab.flVectorNode.copyFrom')

    def createInstance(self) -> flVectorNode:
        'flVectorNode createInstance()'
        _unavailable('fontlab.flVectorNode.createInstance')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flVectorNode.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flVectorNode.currentHistoryState')

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        'double distanceTo(Node/QPointF)'
        _unavailable('fontlab.flVectorNode.distanceTo')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flVectorNode.flag')

    def getLines(self, *args: Any, **kwargs: Any) -> Any:
        '(QLineF, QLineF)/None getLines()'
        _unavailable('fontlab.flVectorNode.getLines')

    def getOn(self) -> Any:
        'Node/None getOn()'
        _unavailable('fontlab.flVectorNode.getOn')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flVectorNode.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flVectorNode.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flVectorNode.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flVectorNode.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flVectorNode.hasHistoryState')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flVectorNode.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flVectorNode.historyStates')

    def improve(self) -> bool:
        'bool improve()'
        _unavailable('fontlab.flVectorNode.improve')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flVectorNode.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flVectorNode.initialHistoryState')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flVectorNode.instanceType')

    def isCorner(self, a: Any = ...) -> bool:
        'bool isCorner([double a = 10.])'
        _unavailable('fontlab.flVectorNode.isCorner')

    def isCurve(self) -> bool:
        'bool isCurve()'
        _unavailable('fontlab.flVectorNode.isCurve')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flVectorNode.isEqual')

    def isEqualTo(self, tolerance: Any = ...) -> bool:
        'bool isEqualTo(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])'
        _unavailable('fontlab.flVectorNode.isEqualTo')

    def isExtreme(self, open: Any = ...) -> bool:
        'bool isExtreme(bool x[, bool open = true[, double limit = 0]])'
        _unavailable('fontlab.flVectorNode.isExtreme')

    def isFirst(self) -> bool:
        'bool isFirst()'
        _unavailable('fontlab.flVectorNode.isFirst')

    def isG2(self, tolerance: float) -> bool:
        'bool isG2(double tolerance)'
        _unavailable('fontlab.flVectorNode.isG2')

    def isInternal(self, clockwise: bool) -> bool:
        'bool isInternal(bool clockwise)'
        _unavailable('fontlab.flVectorNode.isInternal')

    def isInterpolated(self, x: bool) -> bool:
        'bool isInterpolated(bool x)'
        _unavailable('fontlab.flVectorNode.isInterpolated')

    def isLast(self) -> bool:
        'bool isLast()'
        _unavailable('fontlab.flVectorNode.isLast')

    def isOff(self) -> bool:
        'bool isOff()'
        _unavailable('fontlab.flVectorNode.isOff')

    def isOn(self) -> bool:
        'bool isOn()'
        _unavailable('fontlab.flVectorNode.isOn')

    def isSmartAngle(self) -> bool:
        'bool isSmartAngle()'
        _unavailable('fontlab.flVectorNode.isSmartAngle')

    def isVectorNode(self, arg0: flObject) -> bool:
        'bool isVectorNode(flObject)'
        _unavailable('fontlab.flVectorNode.isVectorNode')

    def makeStart(self) -> bool:
        'bool makeStart()'
        _unavailable('fontlab.flVectorNode.makeStart')

    def moveBy(self, *args: Any, **kwargs: Any) -> Any:
        'moveBy(float dx, float dy[, bool round=false]'
        _unavailable('fontlab.flVectorNode.moveBy')

    def nextNode(self, nodeType: Any = ...) -> Any:
        'Node/None nextNode([string nodeType= [, int searchDepth=1]])'
        _unavailable('fontlab.flVectorNode.nextNode')

    def pointG2(self) -> Any:
        'QPointF/None pointG2()'
        _unavailable('fontlab.flVectorNode.pointG2')

    def prevNode(self, nodeType: Any = ...) -> Any:
        'Node/None prevNode([string nodeType= [, int searchDepth=1]])'
        _unavailable('fontlab.flVectorNode.prevNode')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flVectorNode.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flVectorNode.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flVectorNode.removeChild')

    def restoreCoordinates(self) -> Any:
        'restoreCoordinates()'
        _unavailable('fontlab.flVectorNode.restoreCoordinates')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flVectorNode.restoreHistoryState')

    def rotateBy(self, origin: Any = ...) -> Any:
        'rotateBy(valueDegree[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flVectorNode.rotateBy')

    def round(self) -> Any:
        "round() - Round the node's coordinate"
        _unavailable('fontlab.flVectorNode.round')

    def scaleBy(self, origin: Any = ...) -> Any:
        'scaleBy(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flVectorNode.scaleBy')

    def setExtraLast(self, bool: Any) -> Any:
        'setExtraLast(bool)'
        _unavailable('fontlab.flVectorNode.setExtraLast')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flVectorNode.setFlag')

    def setNextSmooth(self, base: QPointF) -> Any:
        'setNextSmooth(QPointF base)'
        _unavailable('fontlab.flVectorNode.setNextSmooth')

    def setPosition(self, arg0: QPointF) -> None:
        'void setPosition(QPointF)'
        _unavailable('fontlab.flVectorNode.setPosition')

    def setPositionMode(self, m: Any) -> None:
        'void setPositionMode(Mode m)'
        _unavailable('fontlab.flVectorNode.setPositionMode')

    def setPrevSmooth(self, base: QPointF) -> Any:
        'setPrevSmooth(QPointF base)'
        _unavailable('fontlab.flVectorNode.setPrevSmooth')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flVectorNode.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flVectorNode.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flVectorNode.setPropertyInt')

    def setSmartAngleEnbl(self, bool: Any) -> bool:
        'bool setSmartAngleEnbl(bool)'
        _unavailable('fontlab.flVectorNode.setSmartAngleEnbl')

    def setSmartSharp(self, tension: Any = ...) -> bool:
        'bool setSmartSharp([double tension = 0.6])'
        _unavailable('fontlab.flVectorNode.setSmartSharp')

    def skewBy(self, origin: Any = ...) -> Any:
        'skewBy(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flVectorNode.skewBy')

    def smartMove(self, offset: Any) -> Any:
        'list(uint) smartMove(offset)'
        _unavailable('fontlab.flVectorNode.smartMove')

    def smartSetXY(self, arg0: QPointF) -> Any:
        'smartSetXY(QPointF)'
        _unavailable('fontlab.flVectorNode.smartSetXY')

    def storeCoordinates(self) -> Any:
        'storeCoordinates()'
        _unavailable('fontlab.flVectorNode.storeCoordinates')

    def storeTestParameters(self) -> Any:
        'storeTestParameters()'
        _unavailable('fontlab.flVectorNode.storeTestParameters')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flVectorNode.tag')

    def transformBy(self, origin: Any = ...) -> Any:
        'transformBy(QTransform tx[, QPointF origin=(0, 0)])'
        _unavailable('fontlab.flVectorNode.transformBy')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flVectorNode.update')

    def updateG2(self) -> bool:
        'bool updateG2()'
        _unavailable('fontlab.flVectorNode.updateG2')

    def updateSmooth(self, extended_neibh: Any = ...) -> Any:
        'updateSmooth([bool extended_neibh=true])'
        _unavailable('fontlab.flVectorNode.updateSmooth')

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
    'flVisualItem representation\n\nConstructors:\n  flVisualItem()\n  flVisualItem(flVisualItem)\n  flVisualItem(flObject)\n  flVisualItem(objId id)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flVisualItem')

    def acceptEvents(self) -> int:
        'int acceptEvents()'
        _unavailable('fontlab.flVisualItem.acceptEvents')

    def activateEditor(self, canvas_pos: QPointF) -> None:
        'void activateEditor(QPointF canvas_pos)'
        _unavailable('fontlab.flVisualItem.activateEditor')

    def addedToCanvas(self, arg0: flCanvas) -> None:
        'void addedToCanvas(flCanvas)'
        _unavailable('fontlab.flVisualItem.addedToCanvas')

    def adjustCanvasPosition(self, arg0: QPointF) -> QPointF:
        'QPointF adjustCanvasPosition(QPointF)'
        _unavailable('fontlab.flVisualItem.adjustCanvasPosition')

    def adjustPosition(self, double: Any) -> Any:
        'QPointF | double adjustPosition(QPointF | double)'
        _unavailable('fontlab.flVisualItem.adjustPosition')

    def appendDecorator(self, arg0: flVisualItem, DecoratorOrder: Any) -> None:
        'void appendDecorator(flVisualItem, DecoratorOrder)'
        _unavailable('fontlab.flVisualItem.appendDecorator')

    def boundingRectOnCanvas(self, *args: Any, **kwargs: Any) -> Any:
        'QRectF boundingRectOnCanvas('
        _unavailable('fontlab.flVisualItem.boundingRectOnCanvas')

    def canvas(self) -> flCanvas:
        'flCanvas canvas()'
        _unavailable('fontlab.flVisualItem.canvas')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flVisualItem.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flVisualItem.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flVisualItem.clearAboveHistory')

    def clearDecorators(self) -> Any:
        'clearDecorators()'
        _unavailable('fontlab.flVisualItem.clearDecorators')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flVisualItem.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flVisualItem.clearFlags')

    def clearItems(self) -> Any:
        'clearItems()'
        _unavailable('fontlab.flVisualItem.clearItems')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flVisualItem.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flVisualItem.cloneObject')

    def contain(self, canvas_pos: QPointF) -> bool:
        'bool contain(QPointF canvas_pos)'
        _unavailable('fontlab.flVisualItem.contain')

    def containsItem(self, arg0: flVisualItem) -> bool:
        'bool containsItem(flVisualItem)'
        _unavailable('fontlab.flVisualItem.containsItem')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flVisualItem.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flVisualItem.currentHistoryState')

    def deactivateEditor(self) -> Any:
        'deactivateEditor()'
        _unavailable('fontlab.flVisualItem.deactivateEditor')

    def distanceTo(self, arg0: QPointF) -> float:
        'double distanceTo(QPointF)'
        _unavailable('fontlab.flVisualItem.distanceTo')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flVisualItem.flag')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flVisualItem.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flVisualItem.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flVisualItem.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flVisualItem.getPropertyInt')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flVisualItem.hasHistoryState')

    def haveCanvas(self) -> bool:
        'bool haveCanvas()'
        _unavailable('fontlab.flVisualItem.haveCanvas')

    def haveEditor(self, canvas_pos: QPointF) -> bool:
        'bool haveEditor(QPointF canvas_pos)'
        _unavailable('fontlab.flVisualItem.haveEditor')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flVisualItem.haveObject')

    def hide(self) -> Any:
        'hide()'
        _unavailable('fontlab.flVisualItem.hide')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flVisualItem.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flVisualItem.independedAll')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flVisualItem.initialHistoryState')

    def instanceAcceptEvents(self) -> int:
        'int instanceAcceptEvents()'
        _unavailable('fontlab.flVisualItem.instanceAcceptEvents')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flVisualItem.instanceType')

    def invselect(self) -> Any:
        'invselect()'
        _unavailable('fontlab.flVisualItem.invselect')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flVisualItem.isEqual')

    def isSelectable(self) -> bool:
        'bool isSelectable()'
        _unavailable('fontlab.flVisualItem.isSelectable')

    def isStableSelect(self) -> bool:
        'bool isStableSelect()'
        _unavailable('fontlab.flVisualItem.isStableSelect')

    def itemScale(self) -> float:
        'double itemScale()'
        _unavailable('fontlab.flVisualItem.itemScale')

    def mapCanvasDistanceToItem(self, arg0: QPointF) -> QPointF:
        'QPointF mapCanvasDistanceToItem(QPointF)'
        _unavailable('fontlab.flVisualItem.mapCanvasDistanceToItem')

    def mapCanvasToItem(self, QRectF: Any) -> Any:
        'QPointF | QRectF mapCanvasToItem(QPointF | QRectF)'
        _unavailable('fontlab.flVisualItem.mapCanvasToItem')

    def mapItemToCanvas(self, QRectF: Any) -> Any:
        'QPointF | QRectF mapItemToCanvas(QPointF | QRectF)'
        _unavailable('fontlab.flVisualItem.mapItemToCanvas')

    def metricStep(self) -> float:
        'double metricStep()'
        _unavailable('fontlab.flVisualItem.metricStep')

    def move(self, arg0: QPointF) -> None:
        'void move(QPointF)'
        _unavailable('fontlab.flVisualItem.move')

    def paint(self, *args: Any, **kwargs: Any) -> Any:
        'void paint(QPainter*)'
        _unavailable('fontlab.flVisualItem.paint')

    def preview(self) -> Any:
        'preview()'
        _unavailable('fontlab.flVisualItem.preview')

    def referencePoint(self) -> QPointF:
        'QPointF referencePoint()'
        _unavailable('fontlab.flVisualItem.referencePoint')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flVisualItem.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flVisualItem.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flVisualItem.removeChild')

    def removeDecorator(self, arg0: flVisualItem) -> None:
        'void removeDecorator(flVisualItem)'
        _unavailable('fontlab.flVisualItem.removeDecorator')

    def removeItem(self, arg0: flVisualItem) -> None:
        'void removeItem(flVisualItem)'
        _unavailable('fontlab.flVisualItem.removeItem')

    def removedFromCanvas(self) -> Any:
        'removedFromCanvas()'
        _unavailable('fontlab.flVisualItem.removedFromCanvas')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flVisualItem.restoreHistoryState')

    def select(self) -> Any:
        'select()'
        _unavailable('fontlab.flVisualItem.select')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flVisualItem.setFlag')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flVisualItem.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flVisualItem.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flVisualItem.setPropertyInt')

    def show(self) -> Any:
        'show()'
        _unavailable('fontlab.flVisualItem.show')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flVisualItem.tag')

    def unselect(self) -> Any:
        'unselect()'
        _unavailable('fontlab.flVisualItem.unselect')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flVisualItem.update')

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
    'flWorkspace representation\n\nConstructors:\n  flWorkspace()\n  flWorkspace(flWorkspace)\n  flWorkspace(flObject)\n  flWorkspace(objId id)\n  flWorkspace(QString title)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flWorkspace')

    def activateEditor(self, arg0: flVisualItem, canvas_pos: QPointF) -> Any:
        'activateEditor(flVisualItem, QPointF canvas_pos)'
        _unavailable('fontlab.flWorkspace.activateEditor')

    def activateNext(self) -> Any:
        'activateNext()'
        _unavailable('fontlab.flWorkspace.activateNext')

    def activatePrev(self) -> Any:
        'activatePrev()'
        _unavailable('fontlab.flWorkspace.activatePrev')

    def addFamilyMembers(self, match_subfamily: Any = ...) -> bool:
        'bool addFamilyMembers(QList<flPackage> &packages[, bool match_subfamily = false])'
        _unavailable('fontlab.flWorkspace.addFamilyMembers')

    def addPackage(self, arg0: flPackage) -> Any:
        'addPackage(flPackage)'
        _unavailable('fontlab.flWorkspace.addPackage')

    def attachCanvas(self, arg0: flCanvas) -> Any:
        'attachCanvas(flCanvas)'
        _unavailable('fontlab.flWorkspace.attachCanvas')

    def blockUpdate(self, time: Any = ...) -> Any:
        'blockUpdate([int time = 2000])'
        _unavailable('fontlab.flWorkspace.blockUpdate')

    def canvases(self) -> list[flObject]:
        'QList<flObject> canvases()'
        _unavailable('fontlab.flWorkspace.canvases')

    def changed(self) -> Any:
        'changed()'
        _unavailable('fontlab.flWorkspace.changed')

    def checkInitHistoryState(self, history_ix: int) -> Any:
        'checkInitHistoryState(uint history_ix)'
        _unavailable('fontlab.flWorkspace.checkInitHistoryState')

    def clearAboveHistory(self, history_ix: int) -> Any:
        'clearAboveHistory(uint history_ix)'
        _unavailable('fontlab.flWorkspace.clearAboveHistory')

    def clearFlag(self, f: int) -> Any:
        'clearFlag(uint f)'
        _unavailable('fontlab.flWorkspace.clearFlag')

    def clearFlags(self) -> Any:
        'clearFlags()'
        _unavailable('fontlab.flWorkspace.clearFlags')

    def clone(self, *args: Any, **kwargs: Any) -> Any:
        'Clone the object'
        _unavailable('fontlab.flWorkspace.clone')

    def cloneObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject cloneObject(const flObject&); '
        _unavailable('fontlab.flWorkspace.cloneObject')

    def closePackage(self, arg0: flPackage) -> Any:
        'closePackage(flPackage)'
        _unavailable('fontlab.flWorkspace.closePackage')

    def closeProject(self) -> Any:
        'closeProject()'
        _unavailable('fontlab.flWorkspace.closeProject')

    def convertMouseEvent(self, QMouseEvent: Any, arg1: QPoint) -> flMouseEvent:
        'flMouseEvent convertMouseEvent(QEvent | QMouseEvent, QPoint)'
        _unavailable('fontlab.flWorkspace.convertMouseEvent')

    def createNewProject(self) -> Any:
        'createNewProject()'
        _unavailable('fontlab.flWorkspace.createNewProject')

    def createObject(self, *args: Any, **kwargs: Any) -> Any:
        'flObject/Nothing createObject(int);    '
        _unavailable('fontlab.flWorkspace.createObject')

    def currentHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'currentHistoryIx()'
        _unavailable('fontlab.flWorkspace.currentHistoryState')

    def deactivateEditor(self) -> Any:
        'deactivateEditor()'
        _unavailable('fontlab.flWorkspace.deactivateEditor')

    def destroyCanvas(self, arg0: flCanvas) -> Any:
        'destroyCanvas(flCanvas)'
        _unavailable('fontlab.flWorkspace.destroyCanvas')

    def doZoomIn(self, s: Any = ...) -> Any:
        'doZoomIn([double s = 2.0])'
        _unavailable('fontlab.flWorkspace.doZoomIn')

    def doZoomOut(self, s: Any = ...) -> Any:
        'doZoomOut([double s = 0.5])'
        _unavailable('fontlab.flWorkspace.doZoomOut')

    def exportCurrentFont(self) -> Any:
        'exportCurrentFont()'
        _unavailable('fontlab.flWorkspace.exportCurrentFont')

    def exportFont(self, arg0: flPackage, ExportControl: Any) -> Any:
        'exportFont(flPackage, ExportControl)'
        _unavailable('fontlab.flWorkspace.exportFont')

    def exportTo(self, filename: str, format: str = ...) -> bool:
        "bool exportTo(QString filename, QString format=['EPS' | 'JPG' | 'PDF' | 'PNG' | 'SVG'])"
        _unavailable('fontlab.flWorkspace.exportTo')

    def findPackageId(self, id: int) -> flPackage:
        'flPackage findPackageId(uint id)'
        _unavailable('fontlab.flWorkspace.findPackageId')

    def flag(self, f: int) -> Any:
        'flag(uint f)'
        _unavailable('fontlab.flWorkspace.flag')

    def getActiveCanvas(self) -> Any:
        'flCanvas/Nothing getActiveCanvas()'
        _unavailable('fontlab.flWorkspace.getActiveCanvas')

    def getActiveTextBlock(self) -> Any:
        'flTextBlockItem/Nothing getActiveTextBlock()'
        _unavailable('fontlab.flWorkspace.getActiveTextBlock')

    def getBoundingRect(self) -> QRectF:
        'QRectF getBoundingRect()'
        _unavailable('fontlab.flWorkspace.getBoundingRect')

    def getCanvasForViewport(self, *args: Any, **kwargs: Any) -> Any:
        'flCanvas/Nothing getCanvasForViewport(QWidget*)'
        _unavailable('fontlab.flWorkspace.getCanvasForViewport')

    def getCanvasUnderCursor(self) -> flCanvas:
        'flCanvas getCanvasUnderCursor()'
        _unavailable('fontlab.flWorkspace.getCanvasUnderCursor')

    def getProperties(self, *args: Any, **kwargs: Any) -> Any:
        "Get object's properties list"
        _unavailable('fontlab.flWorkspace.getProperties')

    def getProperty(self, *args: Any, **kwargs: Any) -> Any:
        "getProperty('key') - get object property by 'key' or number "
        _unavailable('fontlab.flWorkspace.getProperty')

    def getPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyFloat('key') - get float object property by 'key'"
        _unavailable('fontlab.flWorkspace.getPropertyFloat')

    def getPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "getPropertyInt('key') - get int object property by 'key'"
        _unavailable('fontlab.flWorkspace.getPropertyInt')

    def guidelinesUpdater(self) -> flNotifier:
        'flNotifier guidelinesUpdater()'
        _unavailable('fontlab.flWorkspace.guidelinesUpdater')

    def hasHistoryState(self, history_ix: int) -> Any:
        'hasHistoryState(uint history_ix)'
        _unavailable('fontlab.flWorkspace.hasHistoryState')

    def hasPackage(self, flPackage: Any) -> bool:
        'bool hasPackage(const flPackage)'
        _unavailable('fontlab.flWorkspace.hasPackage')

    def haveActiveEditor(self) -> bool:
        'bool haveActiveEditor()'
        _unavailable('fontlab.flWorkspace.haveActiveEditor')

    def haveObject(self, *args: Any, **kwargs: Any) -> Any:
        'bool haveObject(uint);                 '
        _unavailable('fontlab.flWorkspace.haveObject')

    def historyStates(self, accepted_state: bool) -> Any:
        'historyStates(bool accepted_state)'
        _unavailable('fontlab.flWorkspace.historyStates')

    def independedAll(self) -> Any:
        'independedAll()'
        _unavailable('fontlab.flWorkspace.independedAll')

    def init(self) -> Any:
        'init()'
        _unavailable('fontlab.flWorkspace.init')

    def initialHistoryState(self, *args: Any, **kwargs: Any) -> Any:
        'initialHistoryIx()'
        _unavailable('fontlab.flWorkspace.initialHistoryState')

    def instance(self) -> flWorkspace:
        'flWorkspace instance()'
        _unavailable('fontlab.flWorkspace.instance')

    def instanceType(self, *args: Any, **kwargs: Any) -> Any:
        'int instanceType();                    '
        _unavailable('fontlab.flWorkspace.instanceType')

    def isActiveCanvas(self, flCanvas: Any) -> bool:
        'bool isActiveCanvas(const flCanvas)'
        _unavailable('fontlab.flWorkspace.isActiveCanvas')

    def isEqual(self, arg0: flObject) -> Any:
        'isEqual(flObject)'
        _unavailable('fontlab.flWorkspace.isEqual')

    def isRulersEnabled(self) -> bool:
        'bool isRulersEnabled()'
        _unavailable('fontlab.flWorkspace.isRulersEnabled')

    def packages(self) -> list[flObject]:
        'QList<flObject>& packages()'
        _unavailable('fontlab.flWorkspace.packages')

    def previewRender(self) -> bool:
        'bool previewRender()'
        _unavailable('fontlab.flWorkspace.previewRender')

    def readProject(self, QString: Any) -> bool:
        'bool readProject(const QString)'
        _unavailable('fontlab.flWorkspace.readProject')

    def release(self) -> Any:
        'release()'
        _unavailable('fontlab.flWorkspace.release')

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        'remove([flObject])'
        _unavailable('fontlab.flWorkspace.remove')

    def removeChild(self, arg0: flObject) -> Any:
        'removeChild(flObject)'
        _unavailable('fontlab.flWorkspace.removeChild')

    def resetToolCursor(self) -> Any:
        'resetToolCursor()'
        _unavailable('fontlab.flWorkspace.resetToolCursor')

    def restoreHistoryState(self, history_ix: int) -> Any:
        'restoreHistoryState(uint history_ix)'
        _unavailable('fontlab.flWorkspace.restoreHistoryState')

    def saveProject(self, *args: Any, **kwargs: Any) -> Any:
        'saveProject([QString]) | bool saveProject(QString, QList<fgFont>, QString ui_state'
        _unavailable('fontlab.flWorkspace.saveProject')

    def setActiveCanvas(self, arg0: flCanvas) -> Any:
        'setActiveCanvas(flCanvas)'
        _unavailable('fontlab.flWorkspace.setActiveCanvas')

    def setActiveSketchboard(self) -> Any:
        'setActiveSketchboard()'
        _unavailable('fontlab.flWorkspace.setActiveSketchboard')

    def setAutoMode(self) -> Any:
        'setAutoMode()'
        _unavailable('fontlab.flWorkspace.setAutoMode')

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        'setFlag(uint f [, bool value])'
        _unavailable('fontlab.flWorkspace.setFlag')

    def setFocusToCanvas(self, arg0: flCanvas) -> Any:
        'setFocusToCanvas(flCanvas)'
        _unavailable('fontlab.flWorkspace.setFocusToCanvas')

    def setPreviewRender(self, bool: Any) -> Any:
        'setPreviewRender(bool)'
        _unavailable('fontlab.flWorkspace.setPreviewRender')

    def setProperty(self, *args: Any, **kwargs: Any) -> Any:
        "setProperty('key', value) - set object property by 'key' or number "
        _unavailable('fontlab.flWorkspace.setProperty')

    def setPropertyFloat(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyFloat('key', value) - set float object property by 'key'"
        _unavailable('fontlab.flWorkspace.setPropertyFloat')

    def setPropertyInt(self, *args: Any, **kwargs: Any) -> Any:
        "setPropertyInt('key', value) - set int object property by 'key'"
        _unavailable('fontlab.flWorkspace.setPropertyInt')

    def setRenderMode(self, RenderMode: Any) -> Any:
        'setRenderMode(RenderMode)'
        _unavailable('fontlab.flWorkspace.setRenderMode')

    def setRulers(self, enabled: bool) -> Any:
        'setRulers(bool enabled)'
        _unavailable('fontlab.flWorkspace.setRulers')

    def setToolBrush(self) -> Any:
        'setToolBrush()'
        _unavailable('fontlab.flWorkspace.setToolBrush')

    def setToolBucket(self) -> Any:
        'setToolBucket()'
        _unavailable('fontlab.flWorkspace.setToolBucket')

    def setToolCursor(self, CursorId: Any) -> Any:
        'setToolCursor(CursorId)'
        _unavailable('fontlab.flWorkspace.setToolCursor')

    def setToolEditor(self) -> Any:
        'setToolEditor()'
        _unavailable('fontlab.flWorkspace.setToolEditor')

    def setToolEllipse(self) -> Any:
        'setToolEllipse()'
        _unavailable('fontlab.flWorkspace.setToolEllipse')

    def setToolGuidelines(self) -> Any:
        'setToolGuidelines()'
        _unavailable('fontlab.flWorkspace.setToolGuidelines')

    def setToolKnife(self) -> Any:
        'setToolKnife()'
        _unavailable('fontlab.flWorkspace.setToolKnife')

    def setToolMagnet(self) -> Any:
        'setToolMagnet()'
        _unavailable('fontlab.flWorkspace.setToolMagnet')

    def setToolMetrics(self) -> Any:
        'setToolMetrics()'
        _unavailable('fontlab.flWorkspace.setToolMetrics')

    def setToolOptimizer(self) -> Any:
        'setToolOptimizer()'
        _unavailable('fontlab.flWorkspace.setToolOptimizer')

    def setToolPen(self) -> Any:
        'setToolPen()'
        _unavailable('fontlab.flWorkspace.setToolPen')

    def setToolPencil(self) -> Any:
        'setToolPencil()'
        _unavailable('fontlab.flWorkspace.setToolPencil')

    def setToolRectangle(self) -> Any:
        'setToolRectangle()'
        _unavailable('fontlab.flWorkspace.setToolRectangle')

    def setToolRotate(self) -> Any:
        'setToolRotate()'
        _unavailable('fontlab.flWorkspace.setToolRotate')

    def setToolScale(self) -> Any:
        'setToolScale()'
        _unavailable('fontlab.flWorkspace.setToolScale')

    def setToolScissors(self) -> Any:
        'setToolScissors()'
        _unavailable('fontlab.flWorkspace.setToolScissors')

    def setToolShape(self) -> Any:
        'setToolShape()'
        _unavailable('fontlab.flWorkspace.setToolShape')

    def setToolSlant(self) -> Any:
        'setToolSlant()'
        _unavailable('fontlab.flWorkspace.setToolSlant')

    def setToolSmartPen(self) -> Any:
        'setToolSmartPen()'
        _unavailable('fontlab.flWorkspace.setToolSmartPen')

    def setToolText(self) -> Any:
        'setToolText()'
        _unavailable('fontlab.flWorkspace.setToolText')

    def setToolTransform(self) -> Any:
        'setToolTransform()'
        _unavailable('fontlab.flWorkspace.setToolTransform')

    def showFocus(self) -> bool:
        'bool showFocus()'
        _unavailable('fontlab.flWorkspace.showFocus')

    def showSmallItems(self) -> bool:
        'bool showSmallItems()'
        _unavailable('fontlab.flWorkspace.showSmallItems')

    def tag(self, *args: Any, **kwargs: Any) -> Any:
        'tag([string])'
        _unavailable('fontlab.flWorkspace.tag')

    def turnTextModeOff(self) -> Any:
        'turnTextModeOff()'
        _unavailable('fontlab.flWorkspace.turnTextModeOff')

    def unblockUpdate(self) -> Any:
        'unblockUpdate()'
        _unavailable('fontlab.flWorkspace.unblockUpdate')

    def update(self) -> Any:
        'update()'
        _unavailable('fontlab.flWorkspace.update')

    def updateActiveViewport(self) -> Any:
        'updateActiveViewport()'
        _unavailable('fontlab.flWorkspace.updateActiveViewport')

    def weAreOnPaper(self) -> bool:
        'bool weAreOnPaper()'
        _unavailable('fontlab.flWorkspace.weAreOnPaper')

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
    'flZone representation\n\nConstructors:\n  flZone()\n  flZone(double p, double w[, QString _n = ])\n  flZone(flZone)\n\nNative bases: object'
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        'Native constructor; consult class documentation for supported overloads.'
        _unavailable('fontlab.flZone')

    def guaranteeName(self, top: bool) -> Any:
        'guaranteeName(bool top)'
        _unavailable('fontlab.flZone.guaranteeName')

    def tagsSet(self) -> Any:
        'QSet<QString>/Nothing tagsSet()'
        _unavailable('fontlab.flZone.tagsSet')

    def toZone(self, arg0: fgZone, top: bool) -> Any:
        'toZone(fgZone, bool top)'
        _unavailable('fontlab.flZone.toZone')

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

def AcceptChanges(clearChangedState: Any = ...) -> Any:
    'AcceptChanges([bool clearChangedState = true])'
    _unavailable('fontlab.AcceptChanges')

def AllFonts(*args: Any, **kwargs: Any) -> Any:
    'Get a list of currently opened fonts'
    _unavailable('fontlab.AllFonts')

def ApplicationPath(*args: Any, **kwargs: Any) -> Any:
    'Return path to FontLab main application'
    _unavailable('fontlab.ApplicationPath')

def CountFonts(*args: Any, **kwargs: Any) -> Any:
    'Return number of currently opened fonts'
    _unavailable('fontlab.CountFonts')

def CreatePanel(*args: Any, **kwargs: Any) -> Any:
    'Create YPanelWidget instance'
    _unavailable('fontlab.CreatePanel')

def CurrentFont(*args: Any, **kwargs: Any) -> Any:
    'Get currently active font'
    _unavailable('fontlab.CurrentFont')

def CurrentGlyph(*args: Any, **kwargs: Any) -> Any:
    'Get currently active glyph'
    _unavailable('fontlab.CurrentGlyph')

def GetFileName(open_save: Any, extension: Any, filename: Any, filters: Any) -> Any:
    'GetFileName(open_save, string extension, string filename, string filters) - opens the file dialog. open_save = 1 for file open dialog'
    _unavailable('fontlab.GetFileName')

def GetPathName(*args: Any, **kwargs: Any) -> Any:
    'GetPathName(String title, ...) - allows to select folder'
    _unavailable('fontlab.GetPathName')

def GetProperty(*args: Any, **kwargs: Any) -> Any:
    'Get FL properties (keywords: output, ...)'
    _unavailable('fontlab.GetProperty')

def MainWindow(*args: Any, **kwargs: Any) -> Any:
    'Get MainWindow object'
    _unavailable('fontlab.MainWindow')

def PanelManager(*args: Any, **kwargs: Any) -> Any:
    'Get YPanelManager object'
    _unavailable('fontlab.PanelManager')

def SetCurrentFont(*args: Any, **kwargs: Any) -> Any:
    'Set active font'
    _unavailable('fontlab.SetCurrentFont')

def SetCurrentGlyph(*args: Any, **kwargs: Any) -> Any:
    'Set active glyph'
    _unavailable('fontlab.SetCurrentGlyph')

def SetProperty(*args: Any, **kwargs: Any) -> Any:
    'Set FL properties (keywords: output, ...)'
    _unavailable('fontlab.SetProperty')

def TestBuilder(*args: Any, **kwargs: Any) -> Any:
    'Test Glyph Builder'
    _unavailable('fontlab.TestBuilder')

def Update(*args: Any, **kwargs: Any) -> Any:
    "Update object and it's visual representations. Without argument update all changed objects. Update([fgGlyph|fgFont|flObject object])"
    _unavailable('fontlab.Update')

def UpdateActiveCanvas() -> Any:
    'UpdateActiveCanvas()'
    _unavailable('fontlab.UpdateActiveCanvas')

def UpdateAll() -> Any:
    'UpdateAll()'
    _unavailable('fontlab.UpdateAll')

def UpdateGlyphRect(x0: Any, y0: Any, x1: Any, y1: Any) -> Any:
    'UpdateGlyphRect(x0, y0, x1, y1)'
    _unavailable('fontlab.UpdateGlyphRect')

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
globals()['flObjectsList<flGuideLine>'] = flObjectsList_flGuideLine_
globals()['flObjectsList<flShape>'] = flObjectsList_flShape_

__all__ = ['AccentInfo', 'AcceptChanges', 'AllFonts', 'ApplicationPath', 'BinaryFormatVersion', 'BuilderFeatures', 'CountFonts', 'CreatePanel', 'CurrentFont', 'CurrentGlyph', 'CurveEx', 'DecoratorOrder', 'EditMode', 'ExportControl', 'FaBasicPtr', 'FontLayer', 'FontMetrics', 'GetFileName', 'GetPathName', 'GetProperty', 'GlyphComponent', 'GlyphInfoState', 'HintingDataType', 'Info', 'Interval', 'LightNodesMode', 'LocationValue', 'MainWindow', 'ObjectFlag', 'PaintBrush', 'PaintBrushShape', 'PanelManager', 'SelectionMode', 'SetCurrentFont', 'SetCurrentGlyph', 'SetProperty', 'ShapeCloneInfo', 'ShapeType', 'SmartCornerParameters', 'SnapAngleMode', 'SnapObjectsStyle', 'TestBuilder', 'TextBlockFormat', 'TransformFrame', 'TransformFrameControls', 'Update', 'UpdateActiveCanvas', 'UpdateAll', 'UpdateGlyphRect', 'ViewPointAlignment', 'YPanelManager', 'YPanelWidget', 'fgSymbol', 'fgSymbolList', 'flAbstractEditor', 'flAbstractVectorNode', 'flAnchor', 'flAuditInfo', 'flAxis', 'flBasicTool', 'flCanvas', 'flContour', 'flContourInfo', 'flEvent', 'flExpression', 'flGlyph', 'flGlyphInfo', 'flGraphicsInfo', 'flGuideLine', 'flHintingParameters', 'flInstance', 'flItems', 'flLayer', 'flLayerAttributes', 'flLayerInfo', 'flLocation', 'flMarkerPoint', 'flModel', 'flModelProducer', 'flMouseEvent', 'flNode', 'flNodeInfo', 'flObject', 'flObjectsList<flGuideLine>', 'flObjectsList<flShape>', 'flPackage', 'flPaper', 'flPinPoint', 'flPreferences', 'flProperty', 'flPropertyDouble', 'flPropertyPoint', 'flSearchInfo', 'flShape', 'flShapeBuilder', 'flShapeData', 'flShapeInfo', 'flSnapLine', 'flSnapObject', 'flSnaps', 'flStem', 'flSticker', 'flTTHCommand', 'flTextBlock', 'flTools', 'flTransform', 'flVectorNode', 'flVisualItem', 'flWorkspace', 'flZone']
_bind(globals(), 'fontlab')
flObjectsList_flGuideLine_ = globals()['flObjectsList<flGuideLine>']
flObjectsList_flShape_ = globals()['flObjectsList<flShape>']
