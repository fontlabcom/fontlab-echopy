# this_file: src/fontlab_echopy/PythonQt/Debug.pyi
# Generated from native metadata and independent enrichment inputs.
"""Native API for PythonQt.Debug."""
from __future__ import annotations
from typing import Any

def blockSignals(b: Any) -> bool:
    """X.blockSignals(b) -> bool"""
    ...

def childEvent(event: Any) -> Any:
    """X.childEvent(event)"""
    ...

def children() -> tuple:
    """X.children() -> tuple"""
    ...

def className(*args: Any, **kwargs: Any) -> Any:
    """Return the classname of the object"""
    ...

def connect(signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
    """X.connect(signal, receiver, slot, type) -> bool"""
    ...

def customEvent(event: Any) -> Any:
    """X.customEvent(event)"""
    ...

def delete(*args: Any, **kwargs: Any) -> Any:
    """Deletes the C++ object (at your own risk, my friend!)"""
    ...

def deleteLater() -> Any:
    """X.deleteLater()"""
    ...

def destroyed(*args: Any, **kwargs: Any) -> Any:
    """Native PythonQt.Debug.destroyed; argument details are not documented."""
    ...

def disconnect(signal: Any, receiver: Any, slot: Any) -> bool:
    """X.disconnect(signal, receiver, slot) -> bool"""
    ...

def dumpObjectInfo() -> Any:
    """X.dumpObjectInfo()"""
    ...

def dumpObjectTree() -> Any:
    """X.dumpObjectTree()"""
    ...

def dynamicPropertyNames() -> Any:
    """X.dynamicPropertyNames()"""
    ...

def event(event: Any) -> bool:
    """X.event(event) -> bool"""
    ...

def eventFilter(watched: Any, event: Any) -> bool:
    """X.eventFilter(watched, event) -> bool"""
    ...

def findChild(type: Any, name: Any) -> Any:
    """X.findChild(type, name) -> PythonQt.private.QObject"""
    ...

def findChildren(type: Any, name: Any) -> tuple:
    """X.findChildren(type, name) -> tuple"""
    ...

def hasExtraShellRefCount(object: Any) -> bool:
    """X.hasExtraShellRefCount(object) -> bool"""
    ...

def help(*args: Any, **kwargs: Any) -> Any:
    """Shows the help of available methods for this class"""
    ...

def inherits(*args: Any, **kwargs: Any) -> Any:
    """Returns if the class inherits or is of given type name"""
    ...

def installEventFilter(filterObj: Any) -> Any:
    """X.installEventFilter(filterObj)"""
    ...

def isDerivedShellInstance(object: Any) -> bool:
    """X.isDerivedShellInstance(object) -> bool"""
    ...

def isOwnedByPython(object: Any) -> bool:
    """X.isOwnedByPython(object) -> bool"""
    ...

def isPythonQtClassWrapper(object: Any) -> bool:
    """X.isPythonQtClassWrapper(object) -> bool"""
    ...

def isPythonQtInstanceWrapper(object: Any) -> bool:
    """X.isPythonQtInstanceWrapper(object) -> bool"""
    ...

def isSignalConnected(signal: Any) -> bool:
    """X.isSignalConnected(signal) -> bool"""
    ...

def isWidgetType() -> bool:
    """X.isWidgetType() -> bool"""
    ...

def isWindowType() -> bool:
    """X.isWindowType() -> bool"""
    ...

def killTimer(id: Any) -> Any:
    """X.killTimer(id)"""
    ...

def metaObject() -> Any:
    """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
    ...

def moveToThread(thread: Any) -> Any:
    """X.moveToThread(thread)"""
    ...

def objectNameChanged(*args: Any, **kwargs: Any) -> Any:
    """Native PythonQt.Debug.objectNameChanged; argument details are not documented."""
    ...

def parent() -> Any:
    """X.parent() -> PythonQt.private.QObject"""
    ...

def passOwnershipToCPP(object: Any) -> bool:
    """X.passOwnershipToCPP(object) -> bool"""
    ...

def passOwnershipToPython(object: Any) -> bool:
    """X.passOwnershipToPython(object) -> bool"""
    ...

def property(name: Any) -> Any:
    """X.property(name) -> object"""
    ...

def removeEventFilter(obj: Any) -> Any:
    """X.removeEventFilter(obj)"""
    ...

def sender() -> Any:
    """X.sender() -> PythonQt.private.QObject"""
    ...

def senderSignalIndex() -> int:
    """X.senderSignalIndex() -> int"""
    ...

def setObjectName(name: Any) -> Any:
    """X.setObjectName(name)"""
    ...

def setParent(parent: Any) -> Any:
    """X.setParent(parent)"""
    ...

def setProperty(name: Any, value: Any) -> bool:
    """X.setProperty(name, value) -> bool"""
    ...

def signalsBlocked() -> bool:
    """X.signalsBlocked() -> bool"""
    ...

def startTimer(interval: Any, timerType: Any) -> int:
    """X.startTimer(interval, timerType) -> int"""
    ...

def thread() -> Any:
    """X.thread()"""
    ...

def timerEvent(event: Any) -> Any:
    """X.timerEvent(event)"""
    ...

def tr(text: Any, ambig: Any, n: Any) -> str:
    """X.tr(text, ambig, n) -> str"""
    ...
objectName: str
__all__ = ['blockSignals', 'childEvent', 'children', 'className', 'connect', 'customEvent', 'delete', 'deleteLater', 'destroyed', 'disconnect', 'dumpObjectInfo', 'dumpObjectTree', 'dynamicPropertyNames', 'event', 'eventFilter', 'findChild', 'findChildren', 'hasExtraShellRefCount', 'help', 'inherits', 'installEventFilter', 'isDerivedShellInstance', 'isOwnedByPython', 'isPythonQtClassWrapper', 'isPythonQtInstanceWrapper', 'isSignalConnected', 'isWidgetType', 'isWindowType', 'killTimer', 'metaObject', 'moveToThread', 'objectName', 'objectNameChanged', 'parent', 'passOwnershipToCPP', 'passOwnershipToPython', 'property', 'removeEventFilter', 'sender', 'senderSignalIndex', 'setObjectName', 'setParent', 'setProperty', 'signalsBlocked', 'startTimer', 'thread', 'timerEvent', 'tr']
