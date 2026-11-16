# this_file: src/fontlab_echopy/PythonQt/QtUiTools.pyi
# Generated from native metadata and independent enrichment inputs.
"""Native API for PythonQt.QtUiTools."""
from __future__ import annotations
from typing import Any

class QUiLoader:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

In addition, you can customize or create your own user interface by deriving your own
loader class.

If you have a custom component or an application that embeds *Qt Designer*, you can also
use the [QFormBuilder](https://doc.qt.io/archives/qt-5.15/qformbuilder.html) class
provided by the [QtDesigner](https://doc.qt.io/archives/qt-5.15/qtdesigner-module.html)
module to create user interfaces from UI files.

The QUiLoader class provides a collection of functions allowing you to create widgets
based on the information stored in UI files (created with *Qt Designer*) or available in
the specified plugin paths. The specified plugin paths can be retrieved using the
[pluginPaths](https://doc.qt.io/archives/qt-5.15/quiloader.html#pluginPaths)() function.
Similarly, the contents of a UI file can be retrieved using the
[load](https://doc.qt.io/archives/qt-5.15/quiloader.html#load)() function. For example:

```
MyWidget::MyWidget(QWidget *parent)
    : QWidget(parent)
{
    QUiLoader loader;
    QFile file(":/forms/myform.ui");
    file.open(QFile::ReadOnly);
    QWidget *myWidget = loader.load(&file, this);
    file.close();

    QVBoxLayout *layout = new QVBoxLayout;
    layout->addWidget(myWidget);
    setLayout(layout);
}
```

By including the user interface in the form's resources (`myform.qrc`), we ensure that
it will be present at run-time:

```
<!DOCTYPE RCC><RCC version="1.0">
<qresource prefix="/forms">
<file>myform.ui</file>
</qresource>
</RCC>
```

The
[availableWidgets](https://doc.qt.io/archives/qt-5.15/quiloader.html#availableWidgets)()
function returns a [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html)
with the class names of the widgets available in the specified plugin paths. To create
these widgets, simply use the
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)()
function. For example:

```
QWidget *loadCustomWidget(QWidget *parent)
{
    QUiLoader loader;
    QWidget *myWidget;

    QStringList availableWidgets = loader.availableWidgets();

    if (availableWidgets.contains("AnalogClock"))
        myWidget = loader.createWidget("AnalogClock", parent);

    return myWidget;
}
```

To make a custom widget available to the loader, you can use the
[addPluginPath](https://doc.qt.io/archives/qt-5.15/quiloader.html#addPluginPath)()
function; to remove all available widgets, you can call the
[clearPluginPaths](https://doc.qt.io/archives/qt-5.15/quiloader.html#clearPluginPaths)()
function.

The [createAction](https://doc.qt.io/archives/qt-5.15/quiloader.html#createAction)(),
[createActionGroup](https://doc.qt.io/archives/qt-5.15/quiloader.html#createActionGroup)(),
[createLayout](https://doc.qt.io/archives/qt-5.15/quiloader.html#createLayout)(), and
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)()
functions are used internally by the QUiLoader class whenever it has to create an
action, action group, layout, or widget respectively. For that reason, you can subclass
the QUiLoader class and reimplement these functions to intervene the process of
constructing a user interface. For example, you might want to have a list of the actions
created when loading a form or creating a custom widget.

For a complete example using the QUiLoader class, see the [Calculator Builder
Example](https://doc.qt.io/archives/qt-5.15/qtdesigner-calculatorbuilder-example.html).

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addPluginPath(self, path: str) -> None:
        """X.addPluginPath(path)

Supplemental documentation:
Qt 5 reference:

### void QUiLoader::addPluginPath(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*path*)

Adds the given *path* to the list of paths in which the loader will search when locating
plugins.

**See also**
[pluginPaths](https://doc.qt.io/archives/qt-5.15/quiloader.html#pluginPaths)() and
[clearPluginPaths](https://doc.qt.io/archives/qt-5.15/quiloader.html#clearPluginPaths)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
addPluginPath(self, path: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#addPluginPath"""
        ...

    def availableLayouts(self) -> tuple:
        """X.availableLayouts() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QUiLoader::availableLayouts() const

Returns a list naming all available layouts that can be built using the
[createLayout](https://doc.qt.io/archives/qt-5.15/quiloader.html#createLayout)()
function

This function was introduced in Qt 4.5.

**See also**
[createLayout](https://doc.qt.io/archives/qt-5.15/quiloader.html#createLayout)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
availableLayouts(self) -> typing.List[str]
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#availableLayouts"""
        ...

    def availableWidgets(self) -> tuple:
        """X.availableWidgets() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QUiLoader::availableWidgets() const

Returns a list naming all available widgets that can be built using the
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)()
function, i.e all the widgets specified within the given plugin paths.

**See also**
[pluginPaths](https://doc.qt.io/archives/qt-5.15/quiloader.html#pluginPaths)() and
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
availableWidgets(self) -> typing.List[str]
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#availableWidgets"""
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

    def clearPluginPaths(self) -> None:
        """X.clearPluginPaths()

Supplemental documentation:
Qt 5 reference:

### void QUiLoader::clearPluginPaths()

Clears the list of paths in which the loader will search when locating plugins.

**See also**
[addPluginPath](https://doc.qt.io/archives/qt-5.15/quiloader.html#addPluginPath)() and
[pluginPaths](https://doc.qt.io/archives/qt-5.15/quiloader.html#pluginPaths)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
clearPluginPaths(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#clearPluginPaths"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def createAction(self, parent: Any, name: str) -> Any:
        """X.createAction(parent, name) -> PythonQt.QtGui.QAction

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QAction](https://doc.qt.io/archives/qt-5.15/qaction.html) \\*QUiLoader::createAction([QObject](https://doc.qt.io/archives/qt-5.15/qobject.html#QObject) \\**parent* \\= nullptr, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name* \\= QString())

Creates a new action with the given *parent* and *name*.

The function is also used internally by the
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) class whenever it creates
a widget. Hence, you can subclass
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) and reimplement this
function to intervene process of constructing a user interface or widget. However, in
your implementation, ensure that you call
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html)'s version first.

**See also**
[createActionGroup](https://doc.qt.io/archives/qt-5.15/quiloader.html#createActionGroup)(),
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)(), and
[load](https://doc.qt.io/archives/qt-5.15/quiloader.html#load)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
createAction(self, parent: typing.Optional[PySide2.QtCore.QObject]=..., name: str=...) -> PySide2.QtWidgets.QAction
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#createAction"""
        ...

    def createActionGroup(self, parent: Any, name: str) -> Any:
        """X.createActionGroup(parent, name) -> PythonQt.QtGui.QActionGroup

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QActionGroup](https://doc.qt.io/archives/qt-5.15/qactiongroup.html) \\*QUiLoader::createActionGroup([QObject](https://doc.qt.io/archives/qt-5.15/qobject.html#QObject) \\**parent* \\= nullptr, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name* \\= QString())

Creates a new action group with the given *parent* and *name*.

The function is also used internally by the
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) class whenever it creates
a widget. Hence, you can subclass
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) and reimplement this
function to intervene process of constructing a user interface or widget. However, in
your implementation, ensure that you call
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html)'s version first.

**See also**
[createAction](https://doc.qt.io/archives/qt-5.15/quiloader.html#createAction)(),
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)(), and
[load](https://doc.qt.io/archives/qt-5.15/quiloader.html#load)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
createActionGroup(self, parent: typing.Optional[PySide2.QtCore.QObject]=..., name: str=...) -> PySide2.QtWidgets.QActionGroup
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#createActionGroup"""
        ...

    def createLayout(self, className: str, parent: Any, name: str) -> Any:
        """X.createLayout(className, parent, name) -> PythonQt.QtGui.QLayout

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QLayout](https://doc.qt.io/archives/qt-5.15/qlayout.html) \\*QUiLoader::createLayout(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*className*, [QObject](https://doc.qt.io/archives/qt-5.15/qobject.html#QObject) \\**parent* \\= nullptr, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name* \\= QString())

Creates a new layout with the given *parent* and *name* using the class specified by
*className*.

The function is also used internally by the
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) class whenever it creates
a widget. Hence, you can subclass
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) and reimplement this
function to intervene process of constructing a user interface or widget. However, in
your implementation, ensure that you call
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html)'s version first.

**See also**
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)() and
[load](https://doc.qt.io/archives/qt-5.15/quiloader.html#load)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
createLayout(self, className: str, parent: typing.Optional[PySide2.QtCore.QObject]=..., name: str=...) -> PySide2.QtWidgets.QLayout
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#createLayout"""
        ...

    def createWidget(self, className: str, parent: Any, name: str) -> Any:
        """X.createWidget(className, parent, name) -> PythonQt.QtGui.QWidget

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html) \\*QUiLoader::createWidget(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*className*, [QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html) \\**parent* \\= nullptr, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name* \\= QString())

Creates a new widget with the given *parent* and *name* using the class specified by
*className*. You can use this function to create any of the widgets returned by the
[availableWidgets](https://doc.qt.io/archives/qt-5.15/quiloader.html#availableWidgets)()
function.

The function is also used internally by the
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) class whenever it creates
a widget. Hence, you can subclass
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html) and reimplement this
function to intervene process of constructing a user interface or widget. However, in
your implementation, ensure that you call
[QUiLoader](https://doc.qt.io/archives/qt-5.15/quiloader.html)'s version first.

**See also**
[availableWidgets](https://doc.qt.io/archives/qt-5.15/quiloader.html#availableWidgets)()
and [load](https://doc.qt.io/archives/qt-5.15/quiloader.html#load)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
createWidget(self, className: str, parent: typing.Optional[PySide2.QtWidgets.QWidget]=..., name: str=...) -> PySide2.QtWidgets.QWidget
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget"""
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

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtUiTools.QUiLoader.destroyed; argument details are not documented."""
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

    def errorString(self) -> str:
        """X.errorString() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QUiLoader::errorString() const

Returns a human-readable description of the last error occurred in
[load](https://doc.qt.io/archives/qt-5.15/quiloader.html#load)().

This function was introduced in Qt 5.0.

**See also** [load](https://doc.qt.io/archives/qt-5.15/quiloader.html#load)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
errorString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#errorString"""
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

    def isLanguageChangeEnabled(self) -> bool:
        """X.isLanguageChangeEnabled() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QUiLoader::isLanguageChangeEnabled() const

Returns true if dynamic retranslation on language change is enabled; returns false
otherwise.

This function was introduced in Qt 4.5.

**See also**
[setLanguageChangeEnabled](https://doc.qt.io/archives/qt-5.15/quiloader.html#setLanguageChangeEnabled)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isLanguageChangeEnabled(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#isLanguageChangeEnabled"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isTranslationEnabled(self) -> bool:
        """X.isTranslationEnabled() -> bool

Upstream PySide2 reference signatures (binding differences may apply):

```python
isTranslationEnabled(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#isTranslationEnabled"""
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

    def load(self, device: Any, parentWidget: Any) -> Any:
        """X.load(device, parentWidget) -> PythonQt.QtGui.QWidget

Supplemental documentation:
Qt 5 reference:

### [QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html) \\*QUiLoader::load([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*, [QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html) \\**parentWidget* \\= nullptr)

Loads a form from the given *device* and creates a new widget with the given
*parentWidget* to hold its contents.

**See also**
[createWidget](https://doc.qt.io/archives/qt-5.15/quiloader.html#createWidget)() and
[errorString](https://doc.qt.io/archives/qt-5.15/quiloader.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
load(self, arg__1: str, parentWidget: typing.Optional[PySide2.QtWidgets.QWidget]=...) -> PySide2.QtWidgets.QWidget
load(self, device: PySide2.QtCore.QIODevice, parentWidget: typing.Optional[PySide2.QtWidgets.QWidget]=...) -> PySide2.QtWidgets.QWidget
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#load"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtUiTools.QUiLoader.objectNameChanged; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def pluginPaths(self) -> tuple:
        """X.pluginPaths() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QUiLoader::pluginPaths() const

Returns a list naming the paths in which the loader will search when locating custom
widget plugins.

**See also**
[addPluginPath](https://doc.qt.io/archives/qt-5.15/quiloader.html#addPluginPath)() and
[clearPluginPaths](https://doc.qt.io/archives/qt-5.15/quiloader.html#clearPluginPaths)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
pluginPaths(self) -> typing.List[str]
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#pluginPaths"""
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

    def setLanguageChangeEnabled(self, enabled: bool) -> None:
        """X.setLanguageChangeEnabled(enabled)

Supplemental documentation:
Qt 5 reference:

### void QUiLoader::setLanguageChangeEnabled(bool *enabled*)

If *enabled* is true, user interfaces loaded by this loader will automatically
retranslate themselves upon receiving a language change event. Otherwise, the user
interfaces will not be retranslated.

This function was introduced in Qt 4.5.

**See also**
[isLanguageChangeEnabled](https://doc.qt.io/archives/qt-5.15/quiloader.html#isLanguageChangeEnabled)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLanguageChangeEnabled(self, enabled: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#setLanguageChangeEnabled"""
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

    def setTranslationEnabled(self, enabled: bool) -> None:
        """X.setTranslationEnabled(enabled)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setTranslationEnabled(self, enabled: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#setTranslationEnabled"""
        ...

    def setWorkingDirectory(self, dir: Any) -> None:
        """X.setWorkingDirectory(dir)

Supplemental documentation:
Qt 5 reference:

### void QUiLoader::setWorkingDirectory(const [QDir](https://doc.qt.io/archives/qt-5.15/qdir.html) \\&*dir*)

Sets the working directory of the loader to *dir*. The loader will look for other
resources, such as icons and resource files, in paths relative to this directory.

**See also**
[workingDirectory](https://doc.qt.io/archives/qt-5.15/quiloader.html#workingDirectory)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setWorkingDirectory(self, dir: PySide2.QtCore.QDir) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#setWorkingDirectory"""
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

    def workingDirectory(self) -> Any:
        """X.workingDirectory() -> PythonQt.QtCore.QDir

Supplemental documentation:
Qt 5 reference:

### [QDir](https://doc.qt.io/archives/qt-5.15/qdir.html) QUiLoader::workingDirectory() const

Returns the working directory of the loader.

**See also**
[setWorkingDirectory](https://doc.qt.io/archives/qt-5.15/quiloader.html#setWorkingDirectory)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
workingDirectory(self) -> PySide2.QtCore.QDir
```

Source: https://doc.qt.io/archives/qt-5.15/quiloader.html#workingDirectory"""
        ...
    objectName: Any
__all__ = ['QUiLoader']
