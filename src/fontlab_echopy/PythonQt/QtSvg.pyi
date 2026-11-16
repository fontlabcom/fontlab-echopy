# this_file: src/fontlab_echopy/PythonQt/QtSvg.pyi
# Generated from native metadata and independent enrichment inputs.
"""Native API for PythonQt.QtSvg."""
from __future__ import annotations
from typing import Any

class QGraphicsSvgItem:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QGraphicsSvgItem provides a way of rendering SVG files onto
[QGraphicsView](https://doc.qt.io/archives/qt-5.15/qgraphicsview.html). QGraphicsSvgItem
can be created by passing the SVG file to be rendered to its constructor or by explicit
setting a shared [QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) on
it.

Note that setting [QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html)
on a QGraphicsSvgItem doesn't make the item take ownership of the renderer, therefore if
using
[setSharedRenderer](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setSharedRenderer)()
method one has to make sure that the lifetime of the
[QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) object will be at
least as long as that of the QGraphicsSvgItem.

QGraphicsSvgItem provides a way of rendering only parts of the SVG files via the
[setElementId](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setElementId).
If
[setElementId](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setElementId)()
method is called, only the SVG element (and its children) with the passed id will be
renderer. This provides a convenient way of selectively rendering large SVG files that
contain a number of discrete elements. For example the following code renders only
jokers from a SVG file containing a whole card deck:

```
QSvgRenderer *renderer = new QSvgRenderer(QLatin1String("SvgCardDeck.svg"));
QGraphicsSvgItem *black = new QGraphicsSvgItem();
QGraphicsSvgItem *red   = new QGraphicsSvgItem();

black->setSharedRenderer(renderer);
black->setElementId(QLatin1String("black_joker"));

red->setSharedRenderer(renderer);
red->setElementId(QLatin1String("red_joker"));
```

Size of the item can be set via direct manipulation of the items transformation matrix.

By default the SVG rendering is cached using
[QGraphicsItem::DeviceCoordinateCache](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#CacheMode-enum)
mode to speedup the display of items. Caching can be disabled by passing
[QGraphicsItem::NoCache](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#CacheMode-enum)
to the
[QGraphicsItem::setCacheMode](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#setCacheMode)()
method.

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def acceptDrops(self) -> bool:
        """X.acceptDrops() -> bool"""
        ...

    def acceptHoverEvents(self) -> bool:
        """X.acceptHoverEvents() -> bool"""
        ...

    def acceptTouchEvents(self) -> bool:
        """X.acceptTouchEvents() -> bool"""
        ...

    def acceptedMouseButtons(self) -> Any:
        """X.acceptedMouseButtons()"""
        ...

    def addToIndex(self) -> Any:
        """X.addToIndex()"""
        ...

    def advance(self, phase: Any) -> Any:
        """X.advance(phase)"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def boundingRect(self) -> Any:
        """X.boundingRect() -> PythonQt.QtCore.QRectF

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) QGraphicsSvgItem::boundingRect() const

Reimplements:
[QGraphicsItem::boundingRect](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#boundingRect)()
const.

Returns the bounding rectangle of this item.

Upstream PySide2 reference signatures (binding differences may apply):

```python
boundingRect(self) -> PySide2.QtCore.QRectF
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#boundingRect"""
        ...

    def boundingRegion(self, itemToDeviceTransform: Any) -> Any:
        """X.boundingRegion(itemToDeviceTransform) -> PythonQt.QtGui.QRegion"""
        ...

    def boundingRegionGranularity(self) -> float:
        """X.boundingRegionGranularity() -> float"""
        ...

    def cacheMode(self) -> Any:
        """X.cacheMode()"""
        ...

    def childEvent(self, event: Any) -> Any:
        """X.childEvent(event)"""
        ...

    def childItems(self) -> tuple:
        """X.childItems() -> tuple"""
        ...

    def childrenBoundingRect(self) -> Any:
        """X.childrenBoundingRect() -> PythonQt.QtCore.QRectF"""
        ...

    def childrenChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.childrenChanged; argument details are not documented."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def clearFocus(self) -> Any:
        """X.clearFocus()"""
        ...

    def clipPath(self) -> Any:
        """X.clipPath() -> PythonQt.QtGui.QPainterPath"""
        ...

    def collidesWithItem(self, other: Any, mode: Any) -> bool:
        """X.collidesWithItem(other, mode) -> bool"""
        ...

    def collidesWithPath(self, path: Any, mode: Any) -> bool:
        """X.collidesWithPath(path, mode) -> bool"""
        ...

    def collidingItems(self, mode: Any) -> tuple:
        """X.collidingItems(mode) -> tuple"""
        ...

    def commonAncestorItem(self, other: Any) -> Any:
        """X.commonAncestorItem(other) -> PythonQt.QtGui.QGraphicsItem"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def contains(self, point: Any) -> bool:
        """X.contains(point) -> bool"""
        ...

    def contextMenuEvent(self, event: Any) -> Any:
        """X.contextMenuEvent(event)"""
        ...

    def cursor(self) -> Any:
        """X.cursor() -> PythonQt.QtGui.QCursor"""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def data(self, key: Any) -> Any:
        """X.data(key) -> object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.destroyed; argument details are not documented."""
        ...

    def deviceTransform(self, viewportTransform: Any) -> Any:
        """X.deviceTransform(viewportTransform) -> PythonQt.QtGui.QTransform"""
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

    def effectiveOpacity(self) -> float:
        """X.effectiveOpacity() -> float"""
        ...

    def enabledChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.enabledChanged; argument details are not documented."""
        ...

    def ensureVisible(self, x: Any, y: Any, w: Any, h: Any, xmargin: Any, ymargin: Any) -> Any:
        """X.ensureVisible(x, y, w, h, xmargin, ymargin)"""
        ...

    def event(self, ev: Any) -> bool:
        """X.event(ev) -> bool"""
        ...

    def eventFilter(self, watched: Any, event: Any) -> bool:
        """X.eventFilter(watched, event) -> bool"""
        ...

    def extension(self, variant: Any) -> Any:
        """X.extension(variant) -> object"""
        ...

    def filtersChildEvents(self) -> bool:
        """X.filtersChildEvents() -> bool"""
        ...

    def findChild(self, type: Any, name: Any) -> Any:
        """X.findChild(type, name) -> PythonQt.private.QObject"""
        ...

    def findChildren(self, type: Any, name: Any) -> tuple:
        """X.findChildren(type, name) -> tuple"""
        ...

    def flags(self) -> Any:
        """X.flags()"""
        ...

    def focusInEvent(self, event: Any) -> Any:
        """X.focusInEvent(event)"""
        ...

    def focusItem(self) -> Any:
        """X.focusItem() -> PythonQt.QtGui.QGraphicsItem"""
        ...

    def focusOutEvent(self, event: Any) -> Any:
        """X.focusOutEvent(event)"""
        ...

    def focusProxy(self) -> Any:
        """X.focusProxy() -> PythonQt.QtGui.QGraphicsItem"""
        ...

    def focusScopeItem(self) -> Any:
        """X.focusScopeItem() -> PythonQt.QtGui.QGraphicsItem"""
        ...

    def grabGesture(self, type: Any, arg1: flags) -> Any:
        """X.grabGesture(type, flags)"""
        ...

    def grabKeyboard(self) -> Any:
        """X.grabKeyboard()"""
        ...

    def grabMouse(self) -> Any:
        """X.grabMouse()"""
        ...

    def graphicsEffect(self) -> Any:
        """X.graphicsEffect() -> PythonQt.QtGui.QGraphicsEffect"""
        ...

    def group(self) -> Any:
        """X.group() -> PythonQt.QtGui.QGraphicsItemGroup"""
        ...

    def handlesChildEvents(self) -> bool:
        """X.handlesChildEvents() -> bool"""
        ...

    def hasCursor(self) -> bool:
        """X.hasCursor() -> bool"""
        ...

    def hasFocus(self) -> bool:
        """X.hasFocus() -> bool"""
        ...

    def heightChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.heightChanged; argument details are not documented."""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hide(self) -> Any:
        """X.hide()"""
        ...

    def hoverEnterEvent(self, event: Any) -> Any:
        """X.hoverEnterEvent(event)"""
        ...

    def hoverLeaveEvent(self, event: Any) -> Any:
        """X.hoverLeaveEvent(event)"""
        ...

    def hoverMoveEvent(self, event: Any) -> Any:
        """X.hoverMoveEvent(event)"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def inputMethodEvent(self, event: Any) -> Any:
        """X.inputMethodEvent(event)"""
        ...

    def inputMethodHints(self) -> Any:
        """X.inputMethodHints()"""
        ...

    def inputMethodQuery(self, query: Any) -> Any:
        """X.inputMethodQuery(query) -> object"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def installSceneEventFilter(self, filterItem: Any) -> Any:
        """X.installSceneEventFilter(filterItem)"""
        ...

    def isActive(self) -> bool:
        """X.isActive() -> bool"""
        ...

    def isAncestorOf(self, child: Any) -> bool:
        """X.isAncestorOf(child) -> bool"""
        ...

    def isBlockedByModalPanel(self, blockingPanel: Any) -> bool:
        """X.isBlockedByModalPanel(blockingPanel) -> bool"""
        ...

    def isCachingEnabled(self) -> bool:
        """X.isCachingEnabled() -> bool

Upstream PySide2 reference signatures (binding differences may apply):

```python
isCachingEnabled(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#isCachingEnabled"""
        ...

    def isClipped(self) -> bool:
        """X.isClipped() -> bool"""
        ...

    def isEnabled(self) -> bool:
        """X.isEnabled() -> bool"""
        ...

    def isObscured(self, x: Any, y: Any, w: Any, h: Any) -> bool:
        """X.isObscured(x, y, w, h) -> bool"""
        ...

    def isObscuredBy(self, item: Any) -> bool:
        """X.isObscuredBy(item) -> bool"""
        ...

    def isPanel(self) -> bool:
        """X.isPanel() -> bool"""
        ...

    def isSelected(self) -> bool:
        """X.isSelected() -> bool"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isUnderMouse(self) -> bool:
        """X.isUnderMouse() -> bool"""
        ...

    def isVisible(self) -> bool:
        """X.isVisible() -> bool"""
        ...

    def isVisibleTo(self, parent: Any) -> bool:
        """X.isVisibleTo(parent) -> bool"""
        ...

    def isWidget(self) -> bool:
        """X.isWidget() -> bool"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindow(self) -> bool:
        """X.isWindow() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def itemChange(self, change: Any, value: Any) -> Any:
        """X.itemChange(change, value) -> object"""
        ...

    def itemTransform(self, other: Any, ok: Any) -> Any:
        """X.itemTransform(other, ok) -> PythonQt.QtGui.QTransform"""
        ...

    def keyPressEvent(self, event: Any) -> Any:
        """X.keyPressEvent(event)"""
        ...

    def keyReleaseEvent(self, event: Any) -> Any:
        """X.keyReleaseEvent(event)"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def mapFromItem(self, item: Any, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapFromItem(item, x, y, w, h) -> PythonQt.QtGui.QPainterPath"""
        ...

    def mapFromParent(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapFromParent(x, y, w, h) -> PythonQt.QtGui.QPainterPath"""
        ...

    def mapFromScene(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapFromScene(x, y, w, h) -> PythonQt.QtGui.QPainterPath"""
        ...

    def mapRectFromItem(self, item: Any, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapRectFromItem(item, x, y, w, h) -> PythonQt.QtCore.QRectF"""
        ...

    def mapRectFromParent(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapRectFromParent(x, y, w, h) -> PythonQt.QtCore.QRectF"""
        ...

    def mapRectFromScene(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapRectFromScene(x, y, w, h) -> PythonQt.QtCore.QRectF"""
        ...

    def mapRectToItem(self, item: Any, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapRectToItem(item, x, y, w, h) -> PythonQt.QtCore.QRectF"""
        ...

    def mapRectToParent(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapRectToParent(x, y, w, h) -> PythonQt.QtCore.QRectF"""
        ...

    def mapRectToScene(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapRectToScene(x, y, w, h) -> PythonQt.QtCore.QRectF"""
        ...

    def mapToItem(self, item: Any, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapToItem(item, x, y, w, h) -> PythonQt.QtGui.QPainterPath"""
        ...

    def mapToParent(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapToParent(x, y, w, h) -> PythonQt.QtGui.QPainterPath"""
        ...

    def mapToScene(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.mapToScene(x, y, w, h) -> PythonQt.QtGui.QPainterPath"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def mouseDoubleClickEvent(self, event: Any) -> Any:
        """X.mouseDoubleClickEvent(event)"""
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

    def moveBy(self, dx: Any, dy: Any) -> Any:
        """X.moveBy(dx, dy)"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.objectNameChanged; argument details are not documented."""
        ...

    def opacityChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.opacityChanged; argument details are not documented."""
        ...

    def opaqueArea(self) -> Any:
        """X.opaqueArea() -> PythonQt.QtGui.QPainterPath"""
        ...

    def paint(self, painter: Any, option: Any, widget: Any) -> None:
        """X.paint(painter, option, widget)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QGraphicsSvgItem::paint([QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) \\**painter*, const [QStyleOptionGraphicsItem](https://doc.qt.io/archives/qt-5.15/qstyleoptiongraphicsitem.html) \\**option*, [QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html) \\**widget* \\= nullptr)

Reimplements:
[QGraphicsItem::paint](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#paint)(QPainter
\\*painter, const QStyleOptionGraphicsItem \\*option, QWidget \\*widget).

Upstream PySide2 reference signatures (binding differences may apply):

```python
paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[PySide2.QtWidgets.QWidget]=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#paint"""
        ...

    def panel(self) -> Any:
        """X.panel() -> PythonQt.QtGui.QGraphicsItem"""
        ...

    def panelModality(self) -> Any:
        """X.panelModality()"""
        ...

    def parentChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.parentChanged; argument details are not documented."""
        ...

    def parentItem(self) -> Any:
        """X.parentItem() -> PythonQt.QtGui.QGraphicsItem"""
        ...

    def parentObject(self) -> Any:
        """X.parentObject() -> PythonQt.QtGui.QGraphicsObject"""
        ...

    def parentWidget(self) -> Any:
        """X.parentWidget() -> PythonQt.QtGui.QGraphicsWidget"""
        ...

    def prepareGeometryChange(self) -> Any:
        """X.prepareGeometryChange()"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def removeFromIndex(self) -> Any:
        """X.removeFromIndex()"""
        ...

    def removeSceneEventFilter(self, filterItem: Any) -> Any:
        """X.removeSceneEventFilter(filterItem)"""
        ...

    def renderer(self) -> Any:
        """X.renderer() -> PythonQt.QtSvg.QSvgRenderer

Supplemental documentation:
Qt 5 reference:

### [QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) \\*QGraphicsSvgItem::renderer() const

Returns the currently use
[QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
renderer(self) -> PySide2.QtSvg.QSvgRenderer
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#renderer"""
        ...

    def resetTransform(self) -> Any:
        """X.resetTransform()"""
        ...

    def rotationChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.rotationChanged; argument details are not documented."""
        ...

    def scaleChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.scaleChanged; argument details are not documented."""
        ...

    def scene(self) -> Any:
        """X.scene() -> PythonQt.QtGui.QGraphicsScene"""
        ...

    def sceneBoundingRect(self) -> Any:
        """X.sceneBoundingRect() -> PythonQt.QtCore.QRectF"""
        ...

    def sceneEvent(self, event: Any) -> bool:
        """X.sceneEvent(event) -> bool"""
        ...

    def sceneEventFilter(self, watched: Any, event: Any) -> bool:
        """X.sceneEventFilter(watched, event) -> bool"""
        ...

    def scenePos(self) -> Any:
        """X.scenePos() -> PythonQt.QtCore.QPointF"""
        ...

    def sceneTransform(self) -> Any:
        """X.sceneTransform() -> PythonQt.QtGui.QTransform"""
        ...

    def scroll(self, dx: Any, dy: Any, rect: Any) -> Any:
        """X.scroll(dx, dy, rect)"""
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

    def setAcceptHoverEvents(self, enabled: Any) -> Any:
        """X.setAcceptHoverEvents(enabled)"""
        ...

    def setAcceptTouchEvents(self, enabled: Any) -> Any:
        """X.setAcceptTouchEvents(enabled)"""
        ...

    def setAcceptedMouseButtons(self, buttons: Any) -> Any:
        """X.setAcceptedMouseButtons(buttons)"""
        ...

    def setActive(self, active: Any) -> Any:
        """X.setActive(active)"""
        ...

    def setBoundingRegionGranularity(self, granularity: Any) -> Any:
        """X.setBoundingRegionGranularity(granularity)"""
        ...

    def setCacheMode(self, mode: Any, cacheSize: Any) -> Any:
        """X.setCacheMode(mode, cacheSize)"""
        ...

    def setCachingEnabled(self, arg__1: bool) -> None:
        """X.setCachingEnabled(arg__1)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCachingEnabled(self, arg__1: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setCachingEnabled"""
        ...

    def setCursor(self, cursor: Any) -> Any:
        """X.setCursor(cursor)"""
        ...

    def setData(self, key: Any, value: Any) -> Any:
        """X.setData(key, value)"""
        ...

    def setElementId(self, id: str) -> None:
        """X.setElementId(id)

Supplemental documentation:
Qt 5 reference:

### void QGraphicsSvgItem::setElementId(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*id*)

Sets the XML ID of the element to *id*.

**Note:** Setter function for property
[elementId](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#elementId).

**See also**
[elementId](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#elementId)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setElementId(self, id: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setElementId"""
        ...

    def setEnabled(self, enabled: Any) -> Any:
        """X.setEnabled(enabled)"""
        ...

    def setExtension(self, extension: Any, variant: Any) -> Any:
        """X.setExtension(extension, variant)"""
        ...

    def setFiltersChildEvents(self, enabled: Any) -> Any:
        """X.setFiltersChildEvents(enabled)"""
        ...

    def setFlag(self, arg0: flag, enabled: Any) -> Any:
        """X.setFlag(flag, enabled)"""
        ...

    def setFlags(self, arg0: flags) -> Any:
        """X.setFlags(flags)"""
        ...

    def setFocus(self, focusReason: Any) -> Any:
        """X.setFocus(focusReason)"""
        ...

    def setFocusProxy(self, item: Any) -> Any:
        """X.setFocusProxy(item)"""
        ...

    def setGraphicsEffect(self, effect: Any) -> Any:
        """X.setGraphicsEffect(effect)"""
        ...

    def setGroup(self, group: Any) -> Any:
        """X.setGroup(group)"""
        ...

    def setHandlesChildEvents(self, enabled: Any) -> Any:
        """X.setHandlesChildEvents(enabled)"""
        ...

    def setInputMethodHints(self, hints: Any) -> Any:
        """X.setInputMethodHints(hints)"""
        ...

    def setMaximumCacheSize(self, size: Any) -> None:
        """X.setMaximumCacheSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGraphicsSvgItem::setMaximumCacheSize(const [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) \\&*size*)

Sets the maximum device coordinate cache size of the item to *size*. If the item is
cached using
[QGraphicsItem::DeviceCoordinateCache](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#CacheMode-enum)
mode, caching is bypassed if the extension of the item in device coordinates is larger
than *size*.

The cache corresponds to the [QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html)
which is used to cache the results of the rendering. Use
[QPixmapCache::setCacheLimit](https://doc.qt.io/archives/qt-5.15/qpixmapcache.html#setCacheLimit)()
to set limitations on the whole cache and use setMaximumCacheSize() when setting cache
size for individual items.

**Note:** Setter function for property
[maximumCacheSize](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#maximumCacheSize).

**See also**
[maximumCacheSize](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#maximumCacheSize)()
and
[QGraphicsItem::cacheMode](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#cacheMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMaximumCacheSize(self, size: PySide2.QtCore.QSize) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setMaximumCacheSize"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setOpacity(self, opacity: Any) -> Any:
        """X.setOpacity(opacity)"""
        ...

    def setPanelModality(self, panelModality: Any) -> Any:
        """X.setPanelModality(panelModality)"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setParentItem(self, parent: Any) -> Any:
        """X.setParentItem(parent)"""
        ...

    def setPos(self, x: Any, y: Any) -> Any:
        """X.setPos(x, y)"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setRotation(self, angle: Any) -> Any:
        """X.setRotation(angle)"""
        ...

    def setScale(self, scale: Any) -> Any:
        """X.setScale(scale)"""
        ...

    def setSelected(self, selected: Any) -> Any:
        """X.setSelected(selected)"""
        ...

    def setSharedRenderer(self, renderer: Any) -> None:
        """X.setSharedRenderer(renderer)

Supplemental documentation:
Qt 5 reference:

### void QGraphicsSvgItem::setSharedRenderer([QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) \\**renderer*)

Sets *renderer* to be a shared
[QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) on the item. By
using this method one can share the same
[QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) on a number of
items. This means that the SVG file will be parsed only once.
[QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) passed to this
method has to exist for as long as this item is used.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSharedRenderer(self, renderer: PySide2.QtSvg.QSvgRenderer) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setSharedRenderer"""
        ...

    def setToolTip(self, toolTip: Any) -> Any:
        """X.setToolTip(toolTip)"""
        ...

    def setTransform(self, matrix: Any, combine: Any) -> Any:
        """X.setTransform(matrix, combine)"""
        ...

    def setTransformOriginPoint(self, ax: Any, ay: Any) -> Any:
        """X.setTransformOriginPoint(ax, ay)"""
        ...

    def setTransformations(self, transformations: Any) -> Any:
        """X.setTransformations(transformations)"""
        ...

    def setVisible(self, visible: Any) -> Any:
        """X.setVisible(visible)"""
        ...

    def setX(self, x: Any) -> Any:
        """X.setX(x)"""
        ...

    def setY(self, y: Any) -> Any:
        """X.setY(y)"""
        ...

    def setZValue(self, z: Any) -> Any:
        """X.setZValue(z)"""
        ...

    def shape(self) -> Any:
        """X.shape() -> PythonQt.QtGui.QPainterPath"""
        ...

    def show(self) -> Any:
        """X.show()"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def stackBefore(self, sibling: Any) -> Any:
        """X.stackBefore(sibling)"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def supportsExtension(self, extension: Any) -> bool:
        """X.supportsExtension(extension) -> bool"""
        ...

    def thread(self) -> Any:
        """X.thread()"""
        ...

    def timerEvent(self, event: Any) -> Any:
        """X.timerEvent(event)"""
        ...

    def toGraphicsObject(self) -> Any:
        """X.toGraphicsObject() -> PythonQt.QtGui.QGraphicsObject"""
        ...

    def toolTip(self) -> str:
        """X.toolTip() -> str"""
        ...

    def topLevelItem(self) -> Any:
        """X.topLevelItem() -> PythonQt.QtGui.QGraphicsItem"""
        ...

    def topLevelWidget(self) -> Any:
        """X.topLevelWidget() -> PythonQt.QtGui.QGraphicsWidget"""
        ...

    def tr(self, text: Any, ambig: Any, n: Any) -> str:
        """X.tr(text, ambig, n) -> str"""
        ...

    def transform(self) -> Any:
        """X.transform() -> PythonQt.QtGui.QTransform"""
        ...

    def transformations(self) -> tuple:
        """X.transformations() -> tuple"""
        ...

    def type(self) -> int:
        """X.type() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` int QGraphicsSvgItem::type() const

Reimplements:
[QGraphicsItem::type](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#type)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
type(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#type"""
        ...

    def ungrabGesture(self, type: Any) -> Any:
        """X.ungrabGesture(type)"""
        ...

    def ungrabKeyboard(self) -> Any:
        """X.ungrabKeyboard()"""
        ...

    def ungrabMouse(self) -> Any:
        """X.ungrabMouse()"""
        ...

    def unsetCursor(self) -> Any:
        """X.unsetCursor()"""
        ...

    def update(self, x: Any, y: Any, width: Any, height: Any) -> Any:
        """X.update(x, y, width, height)"""
        ...

    def updateMicroFocus(self) -> Any:
        """X.updateMicroFocus()"""
        ...

    def visibleChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.visibleChanged; argument details are not documented."""
        ...

    def wheelEvent(self, event: Any) -> Any:
        """X.wheelEvent(event)"""
        ...

    def widthChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.widthChanged; argument details are not documented."""
        ...

    def window(self) -> Any:
        """X.window() -> PythonQt.QtGui.QGraphicsWidget"""
        ...

    def xChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.xChanged; argument details are not documented."""
        ...

    def yChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.yChanged; argument details are not documented."""
        ...

    def zChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QGraphicsSvgItem.zChanged; argument details are not documented."""
        ...

    def zValue(self) -> float:
        """X.zValue() -> float"""
        ...
    CacheMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    DeviceCoordinateCache: Any
    Extension: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    GraphicsItemChange: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    GraphicsItemFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    GraphicsItemFlags: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    ItemAcceptsInputMethod: Any
    ItemChildAddedChange: Any
    ItemChildRemovedChange: Any
    ItemClipsChildrenToShape: Any
    ItemClipsToShape: Any
    ItemContainsChildrenInShape: Any
    ItemCoordinateCache: Any
    ItemCursorChange: Any
    ItemCursorHasChanged: Any
    ItemDoesntPropagateOpacityToChildren: Any
    ItemEnabledChange: Any
    ItemEnabledHasChanged: Any
    ItemFlagsChange: Any
    ItemFlagsHaveChanged: Any
    ItemHasNoContents: Any
    ItemIgnoresParentOpacity: Any
    ItemIgnoresTransformations: Any
    ItemIsFocusScope: Any
    ItemIsFocusable: Any
    ItemIsMovable: Any
    ItemIsPanel: Any
    ItemIsSelectable: Any
    ItemMatrixChange: Any
    ItemNegativeZStacksBehindParent: Any
    ItemOpacityChange: Any
    ItemOpacityHasChanged: Any
    ItemParentChange: Any
    ItemParentHasChanged: Any
    ItemPositionChange: Any
    ItemPositionHasChanged: Any
    ItemRotationChange: Any
    ItemRotationHasChanged: Any
    ItemScaleChange: Any
    ItemScaleHasChanged: Any
    ItemSceneChange: Any
    ItemSceneHasChanged: Any
    ItemScenePositionHasChanged: Any
    ItemSelectedChange: Any
    ItemSelectedHasChanged: Any
    ItemSendsGeometryChanges: Any
    ItemSendsScenePositionChanges: Any
    ItemStacksBehindParent: Any
    ItemStopsClickFocusPropagation: Any
    ItemStopsFocusHandling: Any
    ItemToolTipChange: Any
    ItemToolTipHasChanged: Any
    ItemTransformChange: Any
    ItemTransformHasChanged: Any
    ItemTransformOriginPointChange: Any
    ItemTransformOriginPointHasChanged: Any
    ItemUsesExtendedStyleOption: Any
    ItemVisibleChange: Any
    ItemVisibleHasChanged: Any
    ItemZValueChange: Any
    ItemZValueHasChanged: Any
    NoCache: Any
    NonModal: Any
    PanelModal: Any
    PanelModality: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SceneModal: Any
    Type: Any
    UserExtension: Any
    UserType: Any
    children: Any
    effect: QGraphicsEffect
    elementId: str
    "Qt 5 reference:\n\n### elementId : [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)\n\nThis property holds the element's XML ID.\n\nThis property was introduced in Qt 4.6.\n\n**Access functions:**\n\n| QString | **[elementId](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#elementId)**() const |\n| --- | --- |\n| void | **[setElementId](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setElementId)**(const QString \\&*id*) |\n\n### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QGraphicsSvgItem::elementId() const\n\nReturns the XML ID the element that is currently being rendered. Returns an empty string\nif the whole file is being rendered.\n\n**Note:** Getter function for property elementId.\n\n**See also**\n[setElementId](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setElementId)().\n\nSource: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#elementId"
    enabled: Any
    enum_1: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    height: Any
    maximumCacheSize: QSize
    'Qt 5 reference:\n\n### maximumCacheSize : [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html)\n\nThis property holds the maximum size of the device coordinate cache for this item.\n\nThis property was introduced in Qt 4.6.\n\n**Access functions:**\n\n| QSize | **[maximumCacheSize](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#maximumCacheSize)**() const |\n| --- | --- |\n| void | **[setMaximumCacheSize](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setMaximumCacheSize)**(const QSize \\&*size*) |\n\n### [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) QGraphicsSvgItem::maximumCacheSize() const\n\nReturns the current maximum size of the device coordinate cache for this item. If the\nitem is cached using\n[QGraphicsItem::DeviceCoordinateCache](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#CacheMode-enum)\nmode, caching is bypassed if the extension of the item in device coordinates is larger\nthan the maximum size.\n\nThe default maximum cache size is 1024x768.\n[QPixmapCache::cacheLimit](https://doc.qt.io/archives/qt-5.15/qpixmapcache.html#cacheLimit)()\ngives the cumulative bounds of the whole cache, whereas maximumCacheSize() refers to a\nmaximum cache size for this particular item.\n\n**Note:** Getter function for property maximumCacheSize.\n\n**See also**\n[setMaximumCacheSize](https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#setMaximumCacheSize)()\nand\n[QGraphicsItem::cacheMode](https://doc.qt.io/archives/qt-5.15/qgraphicsitem.html#cacheMode)().\n\nSource: https://doc.qt.io/archives/qt-5.15/qgraphicssvgitem.html#maximumCacheSize'
    objectName: Any
    opacity: Any
    parent: QGraphicsObject
    pos: QPointF
    rotation: Any
    scale: Any
    transformOriginPoint: QPointF
    visible: Any
    width: Any
    x: Any
    y: Any
    z: Any

class QSvgGenerator:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

This paint device represents a Scalable Vector Graphics (SVG) drawing. Like QPrinter, it
is designed as a write-only device that generates output in a specific format.

To write an SVG file, you first need to configure the output by setting the
[fileName](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#fileName-prop) or
[outputDevice](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#outputDevice-prop)
properties. It is usually necessary to specify the size of the drawing by setting the
[size](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#size-prop) property, and in
some cases where the drawing will be included in another, the
[viewBox](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox) property also
needs to be set.

```
    QSvgGenerator generator;
    generator.setFileName(path);
    generator.setSize(QSize(200, 200));
    generator.setViewBox(QRect(0, 0, 200, 200));
    generator.setTitle(tr("SVG Generator Example Drawing"));
    generator.setDescription(tr("An SVG drawing created by the SVG Generator "
                                "Example provided with Qt."));
```

Other meta-data can be specified by setting the *title*, *description* and *resolution*
properties.

As with other [QPaintDevice](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html)
subclasses, a [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) object is
used to paint onto an instance of this class:

```
    QPainter painter;
    painter.begin(&generator);
    ...
    painter.end();
```

Painting is performed in the same way as for any other paint device. However, it is
necessary to use the
[QPainter::begin](https://doc.qt.io/archives/qt-5.15/qpainter.html#begin)() and
[end()](https://doc.qt.io/archives/qt-5.15/qpainter.html#end) to explicitly begin and
end painting on the device.

The [SVG Generator
Example](https://doc.qt.io/archives/qt-5.15/qtsvg-svggenerator-example.html) shows how
the same painting commands can be used for painting a widget and writing an SVG file.

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def colorCount(self) -> int:
        """X.colorCount() -> int"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def depth(self) -> int:
        """X.depth() -> int"""
        ...

    def description(self) -> str:
        """X.description() -> str

Supplemental documentation:
Qt 5 reference:

### description : [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)

This property holds the description of the generated SVG drawing

This property was introduced in Qt 4.5.

**Access functions:**

| QString | **description**() const |
| --- | --- |
| void | **setDescription**(const QString \\&*description*) |

**See also** [title](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#title-prop).

Upstream PySide2 reference signatures (binding differences may apply):

```python
description(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#description"""
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

    def fileName(self) -> str:
        """X.fileName() -> str

Supplemental documentation:
Qt 5 reference:

### fileName : [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)

This property holds the target filename for the generated SVG drawing

This property was introduced in Qt 4.5.

**Access functions:**

| QString | **fileName**() const |
| --- | --- |
| void | **setFileName**(const QString \\&*fileName*) |

**See also**
[outputDevice](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#outputDevice-prop).

Upstream PySide2 reference signatures (binding differences may apply):

```python
fileName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#fileName"""
        ...

    def height(self) -> int:
        """X.height() -> int"""
        ...

    def heightMM(self) -> int:
        """X.heightMM() -> int"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def initPainter(self, painter: Any) -> Any:
        """X.initPainter(painter)"""
        ...

    def logicalDpiX(self) -> int:
        """X.logicalDpiX() -> int"""
        ...

    def logicalDpiY(self) -> int:
        """X.logicalDpiY() -> int"""
        ...

    def metric(self, metric: Any) -> int:
        """X.metric(metric) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` int QSvgGenerator::metric([QPaintDevice::PaintDeviceMetric](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#PaintDeviceMetric-enum) *metric*) const

Reimplements:
[QPaintDevice::metric](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#metric)(QPaintDevice::PaintDeviceMetric
metric) const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#metric"""
        ...

    def outputDevice(self) -> Any:
        """X.outputDevice() -> PythonQt.QtCore.QIODevice

Supplemental documentation:
Qt 5 reference:

### outputDevice : [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html)\\*

This property holds the output device for the generated SVG drawing

If both output device and file name are specified, the output device will have
precedence.

This property was introduced in Qt 4.5.

**Access functions:**

| QIODevice \\* | **outputDevice**() const |
| --- | --- |
| void | **setOutputDevice**(QIODevice \\**outputDevice*) |

**See also**
[fileName](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#fileName-prop).

Upstream PySide2 reference signatures (binding differences may apply):

```python
outputDevice(self) -> PySide2.QtCore.QIODevice
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#outputDevice"""
        ...

    def paintEngine(self) -> Any:
        """X.paintEngine() -> PythonQt.QtGui.QPaintEngine

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [QPaintEngine](https://doc.qt.io/archives/qt-5.15/qpaintengine.html) \\*QSvgGenerator::paintEngine() const

Reimplements:
[QPaintDevice::paintEngine](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#paintEngine)()
const.

Returns the paint engine used to render graphics to be converted to SVG format
information.

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintEngine(self) -> PySide2.QtGui.QPaintEngine
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#paintEngine"""
        ...

    def paintingActive(self) -> bool:
        """X.paintingActive() -> bool"""
        ...

    def physicalDpiX(self) -> int:
        """X.physicalDpiX() -> int"""
        ...

    def physicalDpiY(self) -> int:
        """X.physicalDpiY() -> int"""
        ...

    def redirected(self, offset: Any) -> Any:
        """X.redirected(offset) -> PythonQt.QtGui.QPaintDevice"""
        ...

    def resolution(self) -> int:
        """X.resolution() -> int

Supplemental documentation:
Qt 5 reference:

### resolution : int

This property holds the resolution of the generated output

The resolution is specified in dots per inch, and is used to calculate the physical size
of an SVG drawing.

This property was introduced in Qt 4.5.

**Access functions:**

| int | **resolution**() const |
| --- | --- |
| void | **setResolution**(int *dpi*) |

**See also** [size](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#size-prop) and
[viewBox](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox).

Upstream PySide2 reference signatures (binding differences may apply):

```python
resolution(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#resolution"""
        ...

    def setDescription(self, description: str) -> None:
        """X.setDescription(description)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDescription(self, description: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#setDescription"""
        ...

    def setFileName(self, fileName: str) -> None:
        """X.setFileName(fileName)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setFileName(self, fileName: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#setFileName"""
        ...

    def setOutputDevice(self, outputDevice: Any) -> None:
        """X.setOutputDevice(outputDevice)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setOutputDevice(self, outputDevice: PySide2.QtCore.QIODevice) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#setOutputDevice"""
        ...

    def setResolution(self, dpi: int) -> None:
        """X.setResolution(dpi)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setResolution(self, dpi: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#setResolution"""
        ...

    def setSize(self, size: Any) -> None:
        """X.setSize(size)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSize(self, size: PySide2.QtCore.QSize) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#setSize"""
        ...

    def setTitle(self, title: str) -> None:
        """X.setTitle(title)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setTitle(self, title: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#setTitle"""
        ...

    def setViewBox(self, viewBox: Any) -> None:
        """X.setViewBox(viewBox)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setViewBox(self, viewBox: PySide2.QtCore.QRect) -> None
setViewBox(self, viewBox: PySide2.QtCore.QRectF) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#setViewBox"""
        ...

    def sharedPainter(self) -> Any:
        """X.sharedPainter() -> PythonQt.QtGui.QPainter"""
        ...

    def size(self) -> Any:
        """X.size() -> PythonQt.QtCore.QSize

Supplemental documentation:
Qt 5 reference:

### size : [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html)

This property holds the size of the generated SVG drawing

By default this property is set to `QSize(-1, -1)`, which indicates that the generator
should not output the width and height attributes of the `<svg>` element.

**Note:** It is not possible to change this property while a
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) is active on the generator.

This property was introduced in Qt 4.5.

**Access functions:**

| QSize | **size**() const |
| --- | --- |
| void | **setSize**(const QSize \\&*size*) |

**See also** [viewBox](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox)
and [resolution](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#resolution-prop).

Upstream PySide2 reference signatures (binding differences may apply):

```python
size(self) -> PySide2.QtCore.QSize
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#size"""
        ...

    def title(self) -> str:
        """X.title() -> str

Supplemental documentation:
Qt 5 reference:

### title : [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)

This property holds the title of the generated SVG drawing

This property was introduced in Qt 4.5.

**Access functions:**

| QString | **title**() const |
| --- | --- |
| void | **setTitle**(const QString \\&*title*) |

**See also**
[description](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#description-prop).

Upstream PySide2 reference signatures (binding differences may apply):

```python
title(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#title"""
        ...

    def viewBox(self) -> Any:
        """X.viewBox() -> PythonQt.QtCore.QRect

Supplemental documentation:
Qt 5 reference:

### viewBox : [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html)

This property holds the viewBox of the generated SVG drawing

By default this property is set to `QRect(0, 0, -1, -1)`, which indicates that the
generator should not output the viewBox attribute of the `<svg>` element.

**Note:** It is not possible to change this property while a
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) is active on the generator.

This property was introduced in Qt 4.5.

**Access functions:**

| QRectF | **viewBoxF**() const |
| --- | --- |
| void | **setViewBox**(const QRect \\&*viewBox*) |
| void | **setViewBox**(const QRectF \\&*viewBox*) |

**See also** [viewBox](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox)(),
[size](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#size-prop), and
[resolution](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#resolution-prop).

### [QRect](https://doc.qt.io/archives/qt-5.15/qrect.html) QSvgGenerator::viewBox() const

Returns
[viewBoxF](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox-prop)().toRect().

This function was introduced in Qt 4.5.

**See also**
[setViewBox](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox-prop)() and
[viewBoxF](https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox-prop)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
viewBox(self) -> PySide2.QtCore.QRect
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBox"""
        ...

    def viewBoxF(self) -> Any:
        """X.viewBoxF() -> PythonQt.QtCore.QRectF

Upstream PySide2 reference signatures (binding differences may apply):

```python
viewBoxF(self) -> PySide2.QtCore.QRectF
```

Source: https://doc.qt.io/archives/qt-5.15/qsvggenerator.html#viewBoxF"""
        ...

    def width(self) -> int:
        """X.width() -> int"""
        ...

    def widthMM(self) -> int:
        """X.widthMM() -> int"""
        ...
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

class QSvgRenderer:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Using QSvgRenderer, Scalable Vector Graphics (SVG) can be rendered onto any
[QPaintDevice](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html) subclass, including
[QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html),
[QImage](https://doc.qt.io/archives/qt-5.15/qimage.html), and QGLWidget.

QSvgRenderer provides an API that supports basic features of SVG rendering, such as
loading and rendering of static drawings, and more interactive features like animation.
Since the rendering is performed using
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html), SVG drawings can be
rendered on any subclass of
[QPaintDevice](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html).

SVG drawings are either loaded when an QSvgRenderer is constructed, or loaded later
using the [load](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#load)() functions.
Data is either supplied directly as serialized XML, or indirectly using a file name. If
a valid file has been loaded, either when the renderer is constructed or at some later
time, [isValid](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#isValid)() returns
true; otherwise it returns false. QSvgRenderer provides the
[render](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#render)() slot to render
the current document, or the current frame of an animated document, using a given
painter.

The [defaultSize](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#defaultSize)()
function provides information about the amount of space that is required to render the
currently loaded SVG file. This is useful for paint devices, such as
[QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html), that often need to supply a
size hint to their parent layout. The default size of a drawing may differ from its
visible area, found using the
[viewBox](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#viewBox) property.

Animated SVG drawings are supported, and can be controlled with a simple collection of
functions and properties:

- The [animated](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#animated)() function indicates whether a drawing contains animation information.
- The [framesPerSecond](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#framesPerSecond-prop) property contains the rate at which the animation plays.

Finally, the QSvgRenderer class provides the
[repaintNeeded](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#repaintNeeded)()
signal which is emitted whenever the rendering of the document needs to be updated.

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def animated(self) -> bool:
        """X.animated() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSvgRenderer::animated() const

Returns true if the current document contains animated elements; otherwise returns
false.

**See also**
[framesPerSecond](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#framesPerSecond-prop)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
animated(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#animated"""
        ...

    def animationDuration(self) -> int:
        """X.animationDuration() -> int

Upstream PySide2 reference signatures (binding differences may apply):

```python
animationDuration(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#animationDuration"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def boundsOnElement(self, id: str) -> Any:
        """X.boundsOnElement(id) -> PythonQt.QtCore.QRectF

Supplemental documentation:
Qt 5 reference:

### [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) QSvgRenderer::boundsOnElement(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*id*) const

Returns bounding rectangle of the item with the given *id*. The transformation matrix of
parent elements is not affecting the bounds of the element.

This function was introduced in Qt 4.2.

**See also**
[transformForElement](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#transformForElement)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
boundsOnElement(self, id: str) -> PySide2.QtCore.QRectF
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#boundsOnElement"""
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

    def defaultSize(self) -> Any:
        """X.defaultSize() -> PythonQt.QtCore.QSize

Supplemental documentation:
Qt 5 reference:

### [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) QSvgRenderer::defaultSize() const

Returns the default size of the document contents.

Upstream PySide2 reference signatures (binding differences may apply):

```python
defaultSize(self) -> PySide2.QtCore.QSize
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#defaultSize"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QSvgRenderer.destroyed; argument details are not documented."""
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

    def elementExists(self, id: str) -> bool:
        """X.elementExists(id) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSvgRenderer::elementExists(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*id*) const

Returns true if the element with the given *id* exists in the currently parsed SVG file
and is a renderable element.

Note: this method returns true only for elements that can be rendered. Which implies
that elements that are considered part of the fill/stroke style properties, e.g.
radialGradients even tough marked with "id" attributes will not be found by this method.

This function was introduced in Qt 4.2.

Upstream PySide2 reference signatures (binding differences may apply):

```python
elementExists(self, id: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#elementExists"""
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

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSvgRenderer::isValid() const

Returns true if there is a valid current document; otherwise returns false.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#isValid"""
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

    def load(self, filename: Any) -> bool:
        """X.load(filename) -> bool

Supplemental documentation:
Qt 5 reference:

### `[slot]` bool QSvgRenderer::load([QXmlStreamReader](https://doc.qt.io/archives/qt-5.15/qxmlstreamreader.html) \\**contents*)

Loads the specified SVG in *contents*, returning true if the content was successfully
parsed; otherwise returns false.

The reader will be used from where it currently is positioned. If *contents* is `null`,
behavior is undefined.

This function was introduced in Qt 4.5.

### `[slot]` bool QSvgRenderer::load(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*contents*)

Loads the specified SVG format *contents*, returning true if the content was
successfully parsed; otherwise returns false.

### `[slot]` bool QSvgRenderer::load(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*filename*)

Loads the SVG file specified by *filename*, returning true if the content was
successfully parsed; otherwise returns false.

Upstream PySide2 reference signatures (binding differences may apply):

```python
load(self, contents: PySide2.QtCore.QByteArray) -> bool
load(self, contents: PySide2.QtCore.QXmlStreamReader) -> bool
load(self, filename: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#load"""
        ...

    def matrixForElement(self, id: str) -> Any:
        """X.matrixForElement(id) -> PythonQt.QtGui.QMatrix

Upstream PySide2 reference signatures (binding differences may apply):

```python
matrixForElement(self, id: str) -> PySide2.QtGui.QMatrix
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#matrixForElement"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QSvgRenderer.objectNameChanged; argument details are not documented."""
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

    def render(self, p: Any, elementId: Any, bounds: Any) -> None:
        """X.render(p, elementId, bounds)

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QSvgRenderer::render([QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) \\**painter*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*elementId*, const [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) \\&*bounds* \\= QRectF())

Renders the given element with *elementId* using the given *painter* on the specified
*bounds*. If the bounding rectangle is not specified the SVG element is mapped to the
whole paint device.

### `[slot]` void QSvgRenderer::render([QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) \\**painter*, const [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) \\&*bounds*)

Renders the current document, or the current frame of an animated document, using the
given *painter* on the specified *bounds* within the painter. If *bounds* is not empty,
the output will be scaled to fill it, ignoring any aspect ratio implied by the SVG.

### `[slot]` void QSvgRenderer::render([QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) \\**painter*)

Renders the current document, or the current frame of an animated document, using the
given *painter*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
render(self, p: PySide2.QtGui.QPainter) -> None
render(self, p: PySide2.QtGui.QPainter, bounds: PySide2.QtCore.QRectF) -> None
render(self, p: PySide2.QtGui.QPainter, elementId: str, bounds: PySide2.QtCore.QRectF=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#render"""
        ...

    def repaintNeeded(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QSvgRenderer.repaintNeeded; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSvgRenderer::repaintNeeded()

This signal is emitted whenever the rendering of the document needs to be updated,
usually for the purposes of animation.

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#repaintNeeded"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setCurrentFrame(self, arg__1: int) -> None:
        """X.setCurrentFrame(arg__1)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCurrentFrame(self, arg__1: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#setCurrentFrame"""
        ...

    def setFramesPerSecond(self, num: int) -> None:
        """X.setFramesPerSecond(num)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setFramesPerSecond(self, num: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#setFramesPerSecond"""
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

    def setViewBox(self, viewbox: Any) -> None:
        """X.setViewBox(viewbox)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setViewBox(self, viewbox: PySide2.QtCore.QRect) -> None
setViewBox(self, viewbox: PySide2.QtCore.QRectF) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#setViewBox"""
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

    def tr(self, text: Any, ambig: Any, n: Any) -> str:
        """X.tr(text, ambig, n) -> str"""
        ...

    def viewBoxF(self) -> Any:
        """X.viewBoxF() -> PythonQt.QtCore.QRectF

Upstream PySide2 reference signatures (binding differences may apply):

```python
viewBoxF(self) -> PySide2.QtCore.QRectF
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#viewBoxF"""
        ...
    aspectRatioMode: Any
    'Qt 5 reference:\n\n### aspectRatioMode : [Qt::AspectRatioMode](https://doc.qt.io/archives/qt-5.15/qt.html#AspectRatioMode-enum)\n\nhow rendering adheres to the SVG view box aspect ratio\n\nThe accepted modes are:\n\n- [Qt::IgnoreAspectRatio](https://doc.qt.io/archives/qt-5.15/qt.html#AspectRatioMode-enum) (the default): the aspect ratio is ignored and the rendering is stretched to the target bounds.\n- [Qt::KeepAspectRatio](https://doc.qt.io/archives/qt-5.15/qt.html#AspectRatioMode-enum): rendering is centered and scaled as large as possible within the target bounds while preserving aspect ratio.\n\nThis property was introduced in Qt 5.15.\n\n**Access functions:**\n\n| Qt::AspectRatioMode | **aspectRatioMode**() const |\n| --- | --- |\n| void | **setAspectRatioMode**(Qt::AspectRatioMode *mode*) |\n\nSource: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#aspectRatioMode'
    currentFrame: int
    framesPerSecond: int
    'Qt 5 reference:\n\n### framesPerSecond : int\n\nThis property holds the number of frames per second to be shown\n\nThe number of frames per second is 0 if the current document is not animated.\n\n**Access functions:**\n\n| int | **framesPerSecond**() const |\n| --- | --- |\n| void | **setFramesPerSecond**(int *num*) |\n\n**See also**\n[animated](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#animated)().\n\nSource: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#framesPerSecond'
    objectName: Any
    viewBox: QRectF
    'Qt 5 reference:\n\n### viewBox : [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html)\n\nThis property holds the rectangle specifying the visible area of the document in logical\ncoordinates\n\nThis property was introduced in Qt 4.2.\n\n**Access functions:**\n\n| QRectF | **viewBoxF**() const |\n| --- | --- |\n| void | **setViewBox**(const QRect \\&*viewbox*) |\n| void | **setViewBox**(const QRectF \\&*viewbox*) |\n\n### [QRect](https://doc.qt.io/archives/qt-5.15/qrect.html) QSvgRenderer::viewBox() const\n\nReturns\n[viewBoxF](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#viewBox-prop)().toRect().\n\n**See also**\n[setViewBox](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#viewBox-prop)() and\n[viewBoxF](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#viewBox-prop)().\n\nSource: https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html#viewBox'

class QSvgWidget:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

This class enables developers to display SVG drawings alongside standard widgets, and is
used in much the same way as [QLabel](https://doc.qt.io/archives/qt-5.15/qlabel.html) is
used for displaying text and bitmap images.

Since QSvgWidget is a subclass of
[QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html), SVG drawings are rendered
using the properties of the display. More control can be exercised over the rendering
process with the [QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html)
class, as this can be used to paint onto other paint devices, such as
[QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) and QGLWidget. The renderer
used by the widget can be obtained with the
[renderer](https://doc.qt.io/archives/qt-5.15/qsvgwidget.html#renderer)() function.

Each QSvgWidget can be constructed with the file name of a SVG file, or they can be
constructed without a specific file to render and one can be supplied later. The
[load](https://doc.qt.io/archives/qt-5.15/qsvgwidget.html#load)() functions provide two
different ways to load an SVG file: they accept either the file name of an SVG file or a
[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) containing the
serialized XML representation of an SVG file.

By default, the widget provides a size hint to reflect the size of the drawing that it
displays. If no data has been loaded, the widget provides the default
[QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html) size hint. Subclass this
class and reimplement
[sizeHint](https://doc.qt.io/archives/qt-5.15/qsvgwidget.html#sizeHint)() if you need to
customize this behavior.

Source: https://doc.qt.io/archives/qt-5.15/qsvgwidget.html"""

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
        """Native PythonQt.QtSvg.QSvgWidget.customContextMenuRequested; argument details are not documented."""
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
        """Native PythonQt.QtSvg.QSvgWidget.destroyed; argument details are not documented."""
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

    def load(self, file: Any) -> None:
        """X.load(file)

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QSvgWidget::load(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*contents*)

Loads the specified SVG format *contents* and updates the widget.

### `[slot]` void QSvgWidget::load(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*file*)

Loads the contents of the specified SVG *file* and updates the widget.

Upstream PySide2 reference signatures (binding differences may apply):

```python
load(self, contents: PySide2.QtCore.QByteArray) -> None
load(self, file: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgwidget.html#load"""
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
        """Native PythonQt.QtSvg.QSvgWidget.objectNameChanged; argument details are not documented."""
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

    def paintEvent(self, event: Any) -> None:
        """X.paintEvent(event)

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` void QSvgWidget::paintEvent([QPaintEvent](https://doc.qt.io/archives/qt-5.15/qpaintevent.html) \\**event*)

Reimplements:
[QWidget::paintEvent](https://doc.qt.io/archives/qt-5.15/qwidget.html#paintEvent)(QPaintEvent
\\*event).

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgwidget.html#paintEvent"""
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

    def renderer(self) -> Any:
        """X.renderer() -> PythonQt.QtSvg.QSvgRenderer

Supplemental documentation:
Qt 5 reference:

### [QSvgRenderer](https://doc.qt.io/archives/qt-5.15/qsvgrenderer.html) \\*QSvgWidget::renderer() const

Returns the renderer used to display the contents of the widget.

Upstream PySide2 reference signatures (binding differences may apply):

```python
renderer(self) -> PySide2.QtSvg.QSvgRenderer
```

Source: https://doc.qt.io/archives/qt-5.15/qsvgwidget.html#renderer"""
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
        """Native PythonQt.QtSvg.QSvgWidget.windowIconChanged; argument details are not documented."""
        ...

    def windowIconTextChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QSvgWidget.windowIconTextChanged; argument details are not documented."""
        ...

    def windowRole(self) -> str:
        """X.windowRole() -> str"""
        ...

    def windowState(self) -> Any:
        """X.windowState()"""
        ...

    def windowTitleChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtSvg.QSvgWidget.windowTitleChanged; argument details are not documented."""
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
    'Qt 5 reference:\n\n### `[override virtual]` [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) QSvgWidget::sizeHint() const\n\nReimplements an access function for property:\n[QWidget::sizeHint](https://doc.qt.io/archives/qt-5.15/qwidget.html#sizeHint-prop).\n\nSource: https://doc.qt.io/archives/qt-5.15/qsvgwidget.html#sizeHint'
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
__all__ = ['QGraphicsSvgItem', 'QSvgGenerator', 'QSvgRenderer', 'QSvgWidget']
