# this_file: src/fontlab_echopy/PythonQt/QtXmlPatterns.pyi
# Generated from native metadata and independent enrichment inputs.
"""Native API for PythonQt.QtXmlPatterns."""
from __future__ import annotations
from typing import Any

class QAbstractMessageHandler:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QAbstractMessageHandler is an abstract base class that provides a callback interface for
handling messages. For example, class
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) parses and runs an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html). When it detects a
compile or runtime error, it generates an appropriate error message, but rather than
output the message itself, it passes the message to the
[message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)()
function of its QAbstractMessageHandler. See
[QXmlQuery::setMessageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setMessageHandler)().

You create a message handler by subclassing QAbstractMessageHandler and implementing
[handleMessage](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#handleMessage)().
You then pass a pointer to an instance of your subclass to any classes that must
generate messages. The messages are sent to the message handler via the
[message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)()
function, which forwards them to your handleMessge().

A single instance of QAbstractMessageHandler can be called on to handle messages from
multiple sources. Hence, the content of a message, which is the *description* parameter
passed to
[message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)() and
[handleMessage](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#handleMessage)(),
must be interpreted in light of the context that required the message to be sent. That
context is specified by the *identifier* and *sourceLocation* parameters to
[message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)()
[handleMessage](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#handleMessage)().

Source: https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html"""

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

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtXmlPatterns.QAbstractMessageHandler.destroyed; argument details are not documented."""
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

    def handleMessage(self, type: Any, description: str, identifier: Any, sourceLocation: Any) -> None:
        """X.handleMessage(type, description, identifier, sourceLocation)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual protected]` void QAbstractMessageHandler::handleMessage([QtMsgType](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) *type*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*description*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*identifier* \\= QUrl(), const [QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) \\&*sourceLocation* \\= QSourceLocation())

This function must be implemented by the sub-class.
[message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)()
will call this function, passing in its parameters, *type*, *description*, *identifier*
and *sourceLocation* unmodified.

This function can potentially be called from multiple threads. It's the
reimplementation's responsibility to ensure thread safety.

Upstream PySide2 reference signatures (binding differences may apply):

```python
handleMessage(self, type: PySide2.QtCore.QtMsgType, description: str, identifier: PySide2.QtCore.QUrl, sourceLocation: PySide2.QtXmlPatterns.QSourceLocation) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#handleMessage"""
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

    def message(self, type: Any, description: str, identifier: Any, sourceLocation: Any) -> None:
        """X.message(type, description, identifier, sourceLocation)

Supplemental documentation:
Qt 5 reference:

### void QAbstractMessageHandler::message([QtMsgType](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) *type*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*description*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*identifier* \\= QUrl(), const [QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) \\&*sourceLocation* \\= QSourceLocation())

Sends a message to this message handler. *type* is the kind of message being sent.
*description* is the message content. The *identifier* is a URI that identifies the
message and is the key to interpreting the other arguments.

Typically, this class is used for reporting errors, as is the case for
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html), which uses a
[QAbstractMessageHandler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html)
to report compile and runtime
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) errors. Hence, using a
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) as the message *identifier* is was
inspired by the explanation of [error handling in the XQuery
language](http://www.w3.org/TR/xquery/#errors). Because the *identifier* is composed of
a namespace URI and a local part, identifiers with the same local part are unique. The
caller is responsible for ensuring that *identifier* is either a valid
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) or a default constructed
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html).

*sourceLocation* identifies a location in a resource (i.e., file or document) where the
need for reporting a message was detected.

This function unconditionally calls
[handleMessage](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#handleMessage)(),
passing all its parameters unmodified.

**See also** <http://www.w3.org/TR/xquery/#errors>.

Upstream PySide2 reference signatures (binding differences may apply):

```python
message(self, type: PySide2.QtCore.QtMsgType, description: str, identifier: PySide2.QtCore.QUrl=..., sourceLocation: PySide2.QtXmlPatterns.QSourceLocation=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtXmlPatterns.QAbstractMessageHandler.objectNameChanged; argument details are not documented."""
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
    objectName: Any

class QAbstractUriResolver:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

For example, one could write a QAbstractUriResolver subclass that rewrites library ISBN
number URIs as book title URLs, e.g., *urn:isbn:0-345-33973-8* would be rewritten as
*file:///books/returnOfTheKing.doc*. Or a QAbstractUriResolver subclass could be written
for a web browser to let the web browser protect the user's private files by mapping
incoming requests for them to null URIs.

Source: https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html"""

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

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtXmlPatterns.QAbstractUriResolver.destroyed; argument details are not documented."""
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
        """Native PythonQt.QtXmlPatterns.QAbstractUriResolver.objectNameChanged; argument details are not documented."""
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

    def resolve(self, relative: Any, baseURI: Any) -> Any:
        """X.resolve(relative, baseURI) -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QAbstractUriResolver::resolve(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*relative*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*baseURI*) const

Returns the *relative* URI resolved using the *baseURI*.

The caller guarantees that both *relative* and *baseURI* are valid, and that *baseURI*
is absolute. *relative* can be relative, absolute, or empty.

The returned [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) can be a default
constructed [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html). If it is not a default
constructed [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html), it will be absolute
and valid. If a default constructed [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html)
is returned, it means the *relative* URI was not accepted to be resolved.

If the reimplemented resolve() function decides it has nothing to do about resolving the
*relative* URI, it should simply return the *relative* URI resolved against the
*baseURI*, i.e.:

```
return baseURI.resolved(relative);
```

**See also**
[QUrl::isRelative](https://doc.qt.io/archives/qt-5.15/qurl.html#isRelative)() and
[QUrl::isValid](https://doc.qt.io/archives/qt-5.15/qurl.html#isValid)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
resolve(self, relative: PySide2.QtCore.QUrl, baseURI: PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html#resolve"""
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
    objectName: Any

class QAbstractXmlNodeModel:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QAbstractXmlNodeModel specifies the interface that a node model must implement for
that node model be accessible to the query engine for processing
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) queries. A node model
represents data as a structure that can be queried as if the data were XML.

The node model represented by a subclass of QAbstractXmlNodeModel is meant to be
accessed by the Qt XML Patterns query engine. If the API seems a little strange in a few
places, it is because the member functions are called by the query engine as it
evaluates an [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html). They
aren't meant to be used programatically.

### Usage

QAbstractXmlNodeModel bridges the gap between the arbitrary structure of the non-XML
data to be queried and the well-defined structure of XML data understood by
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html).

Consider a chemistry application that reads the file `chemistryData`, which contains
non-XML data that represents a chemical structure composed of molecules and atoms. The
application will query this chemistry data with an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) it reads from file
`queryFile`. We write a custom subclass of QAbstractXmlNodeModel (`ChemistryNodeModel`)
that reads `chemistryData` and builds a data structure, perhaps composed of objects of
our own classes `molecule` and `atom`. Clearly, this data structure is not XML. Our
custom subclass will know how to traverse this non-XML structure and present it through
the [XPath Data Model interface](http://www.w3.org/TR/xpath-datamodel/).

```
QFile queryFile(argv[1]);
QFile chemistryData(argv[2]);
QString moleculeName = argv[3];

QXmlQuery query;
query.setQuery(&queryFile, QUrl::fromLocalFile(queryFile.fileName()));

ChemistryNodeModel myNodeModel(query.namePool(), chemistryData);
QXmlNodeModelIndex startNode = myNodeModel.nodeFor(moleculeName);
query.bindVariable("queryRoot", startNode);

QFile out;
out.open(stdout, QIODevice::WriteOnly);

QXmlSerializer serializer(query, &out);
query.evaluateTo(&serializer);
```

The application first creates an instance of
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) and calls
[setQuery()](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery) to read
`queryFile` containing the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) we want to run. Then it
creates an instance of our custom node model class, `ChemistryNodeModel`, which is a
subclass of QAbstractXmlNodeModel. Its constructor is called with the [name
pool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) obtained from our
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html), and with the
`chemistryFile` containing the structure of molecules and atoms to be queried. The [name
pool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) is required because our
custom node model has the member function
[name()](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#name), which
returns the [name](https://doc.qt.io/archives/qt-5.15/qxmlname.html) of any node in the
model. The [query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) and the custom
node model must use the same name pool for constructing these
[names](https://doc.qt.io/archives/qt-5.15/qxmlname.html). The constructor would then
read `chemistryFile` and build the custom node model structure.

To connect the `query` to the custom node model, we must bind a variable name used in
the query to a node in the model. The variable can then be used in the query as a
starting node. First, an
[index](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) for the desired
starting node is retrieved by calling
[QAbstractXmlNodeModel::createIndex](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#createIndex)().
Then the index is bound to a variable name, in this case `queryRoot`, by passing the
name and the index to
[QXmlQuery::bindVariable](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#bindVariable)().
The query can then use a variable reference `$queryRoot` to refer to the starting node.
Note that if the [query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) uses
multiple variable references, a call to
[QXmlQuery::bindVariable](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#bindVariable)()
is required to bind each different variable name to a node in the model.

The query is executed when the application calls one of the
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) evaluation functions. The
application uses
[QXmlQuery::evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)([QAbstractXmlReceiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html)
\\*), because it then uses a
[serializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) to out the query
result as XML to `stdout`. We could have used
[QXmlQuery::evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)([QXmlResultItems](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html)
\\*) to get a list of result items, or
[QXmlQuery::evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)([QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html)
\\*) if the query evaluated to a sequence of `xs:string` values.

During query execution, the engine iterates over the node model using
[nextFromSimpleAxis](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#nextFromSimpleAxis)()
to get the [index](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) of the
next node to be visited. The engine can get the name of a node by calling
[name](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#name)() with the
node's [index](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html).
[stringValue](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#stringValue)(),
[baseUri](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#baseUri)(),
[documentUri](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#documentUri)()
and [kind](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#kind)() are
also called as needed with a node
[index](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html).

The example demonstrates the standard pattern for using a subclass of
QAbstractXmlNodeModel in combination with
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to perform an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html).

1. Instantiate [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) and give it the [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) to be run;
2. Instantiate a subclass of QAbstractXmlNodeModel or [QSimpleXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html);
3. Retrieve a [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) for the node in the model where the [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) should start the query;
4. Use [QXmlQuery::bindVariable](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#bindVariable)() to bind the [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) to `$variable name`;
5. Call one of the [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) evaluation functions to run the query.

### Subclassing

Because the [XPath Data Model interface](http://www.w3.org/TR/xpath-datamodel/)
presented by QAbstractXmlNodeModel allows
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to operate on non-XML
data as if it were XML, implementing subclasses of QAbstractXmlNodeModel can involve a
significant amount of work. The
[QSimpleXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html) class
is provided to simplify the implementation for many common use cases.

### Thread Safety

Because the node model can be accessed concurrently by threads in the Qt XML Patterns
module, subclasses of QAbstractXmlNodeModel must be written to be
[thread-safe](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#reentrancy-and-thread-safety).
Classes that simplify implementing thread-safety include
[QReadLocker](https://doc.qt.io/archives/qt-5.15/qreadlocker.html) and
[QWriteLocker](https://doc.qt.io/archives/qt-5.15/qwritelocker.html).

See the example [File System
Example](https://doc.qt.io/archives/qt-5.15/qtxmlpatterns-filetree-example.html) for a
demonstration.

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def attributes(self, element: Any) -> tuple:
        """X.attributes(element) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[pure virtual protected]` [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)\\> QAbstractXmlNodeModel::attributes(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*element*) const

Returns the attributes of *element*. The caller guarantees that *element* is an element
in this node model.

Upstream PySide2 reference signatures (binding differences may apply):

```python
attributes(self, element: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.List[PySide2.QtXmlPatterns.QXmlNodeModelIndex]
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#attributes"""
        ...

    def baseUri(self, ni: Any) -> Any:
        """X.baseUri(ni) -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QAbstractXmlNodeModel::baseUri(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*n*) const

Returns the base URI for the node whose index is *n*. The caller guarantees that *n* is
not `null` and that it belongs to a node in this node model.

The base URI of a node can be extracted using the `fn:base-uri()` function. The base URI
is typically used for resolving relative URIs that appear in the node or its children.
It is conformant to just return the document URI, although that might not properly
reflect the underlying data.

This function maps to the `dm:base-uri` accessor, which returns a base URI according to
the following:

- For document nodes, the base URI and the document URI are the same.
- For elements, the base URI is the URI appearing in the element's `xml:base` attribute, if present, or it is resolved to the parent element's base URI.
- Namespace nodes have no base URI.
- The base URI for a processing instruction, comment, attribute, or text node is the base URI of the node's parent element.

The implementation guarantees to return a valid
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html), or a default constructed
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html). If a node has no base URI, as in
the case where a comment has no parent, a default constructed
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) is returned.

**See also** [XQuery 1.0 and XPath 2.0 Data Model (XDM), 5.2 base-uri
Accessor](http://www.w3.org/TR/xpath-datamodel/#dm-base-uri).

Upstream PySide2 reference signatures (binding differences may apply):

```python
baseUri(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#baseUri"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def compareOrder(self, ni1: Any, ni2: Any) -> Any:
        """X.compareOrder(ni1, ni2)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QXmlNodeModelIndex::DocumentOrder](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#DocumentOrder-enum) QAbstractXmlNodeModel::compareOrder(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*ni1*, const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*ni2*) const

This function returns the relative document order for the nodes indexed by *ni1* and
*ni2*. It is used for the `Is` operator and for sorting nodes in document order.

The caller guarantees that *ni1* and *ni2* are not `null` and that both identify nodes
in this node model.

If *ni1* is identical to *ni2*,
[QXmlNodeModelIndex::Is](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#DocumentOrder-enum)
is returned. If *ni1* precedes *ni2* in document order,
[QXmlNodeModelIndex::Precedes](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#DocumentOrder-enum)
is returned. If *ni1* follows *ni2* in document order,
[QXmlNodeModelIndex::Follows](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#DocumentOrder-enum)
is returned.

**See also** [XQuery 1.0 and XPath 2.0 Data Model (XDM), 2.4 Document
Order](http://www.w3.org/TR/xpath-datamodel/#document-order).

Upstream PySide2 reference signatures (binding differences may apply):

```python
compareOrder(self, ni1: PySide2.QtXmlPatterns.QXmlNodeModelIndex, ni2: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#compareOrder"""
        ...

    def createIndex(self, data: Any, additionalData: Any) -> Any:
        """X.createIndex(data, additionalData) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex

Supplemental documentation:
Qt 5 reference:

### `[protected]` [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QAbstractXmlNodeModel::createIndex([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *data*) const

Creates a node index with *data* as its internal data. *data* is not constrained.

### `[protected]` [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QAbstractXmlNodeModel::createIndex(void \\**pointer*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *additionalData* \\= 0\\) const

Creates a node index with *pointer* and *additionalData* as its internal data.

What *pointer* and *additionalData* is, is not constrained.

### `[protected]` [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QAbstractXmlNodeModel::createIndex([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *additionalData*) const

This is an overloaded function.

Creates a
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)
containing *data* and *additionalData*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
createIndex(self, data: int) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
createIndex(self, data: int, additionalData: int) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
createIndex(self, pointer: int, additionalData: int=...) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#createIndex"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def documentUri(self, ni: Any) -> Any:
        """X.documentUri(ni) -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QAbstractXmlNodeModel::documentUri(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*n*) const

Returns the document URI of *n*. The document URI identifies the resource which is the
document. For example, the document could be a regular file, e.g., `file:/`, or it could
be the `http://` URL of the location of a file. The document URI is used for resolving
URIs and to simply know where the document is.

If the node model maps to a URI in a natural way, return that URI. Otherwise, return the
company or product URI. The document URI can be any URI as long as its valid and
absolute.

The caller guarantees that *n* is not `null` and that it belongs to this
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

This function maps to the `dm:document-uri` accessor, which returns a document URI
according to the following:

- If *n* is a document node, return an absolute [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) containing the document URI, or a default constructed [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html). The latter signals that no document URI is available for the document node.
- For all other nodes, return a default constructed [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html).

**See also** [XQuery 1.0 and XPath 2.0 Data Model (XDM), 5.4 document-uri
Accessor](http://www.w3.org/TR/xpath-datamodel/#dm-document-uri),
[QUrl::isValid](https://doc.qt.io/archives/qt-5.15/qurl.html#isValid)(), and
[QUrl::isRelative](https://doc.qt.io/archives/qt-5.15/qurl.html#isRelative)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
documentUri(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#documentUri"""
        ...

    def elementById(self, NCName: Any) -> Any:
        """X.elementById(NCName) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QAbstractXmlNodeModel::elementById(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*id*) const

Returns the index of the element identified as *id*.
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html)'s `id()` function calls
this function.

The node index returned will be the element node whose value is of type `ID` and equals
*id*, or it will be the element node that has an attribute whose typed value is of type
`ID` and equals *id*. If there is no such element, a default constructed
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)
instance is returned. The implementor guarantees that if the returned node index is not
null, it identifies an element.

It is not sufficient for an attribute or element to merely be called `id`. Its value
type must also be `ID`. However, the reserved name `xml:id` is sufficient.

In *id*, the `namespace URI` and the `prefix` are undefined, and the `local name` is the
ID that should be looked up.

**See also** [XQuery 1.0 and XPath 2.0 Functions and Operators, 15.5.2
fn:id](http://www.w3.org/TR/xpath-functions/#func-id).

Upstream PySide2 reference signatures (binding differences may apply):

```python
elementById(self, NCName: PySide2.QtXmlPatterns.QXmlName) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#elementById"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isDeepEqual(self, ni1: Any, ni2: Any) -> bool:
        """X.isDeepEqual(ni1, ni2) -> bool

Upstream PySide2 reference signatures (binding differences may apply):

```python
isDeepEqual(self, ni1: PySide2.QtXmlPatterns.QXmlNodeModelIndex, ni2: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#isDeepEqual"""
        ...

    def kind(self, ni: Any) -> Any:
        """X.kind(ni)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QXmlNodeModelIndex::NodeKind](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#NodeKind-enum) QAbstractXmlNodeModel::kind(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*ni*) const

Returns a value indicating the kind of node identified by *ni*. The caller guarantees
that *ni* is not null and that it identifies a node in this node model. This function
maps to the `dm:node-kind()` accessor.

**See also** [XQuery 1.0 and XPath 2.0 Data Model (XDM), 5.10 node-kind
Accessor](http://www.w3.org/TR/xpath-datamodel/#dm-node-kind).

Upstream PySide2 reference signatures (binding differences may apply):

```python
kind(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#kind"""
        ...

    def name(self, ni: Any) -> Any:
        """X.name(ni) -> PythonQt.QtXmlPatterns.QXmlName

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) QAbstractXmlNodeModel::name(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*ni*) const

Returns the name of *ni*. The caller guarantees that *ni* is not `null` and that it
belongs to this
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

If a node does not have a name, e.g., comment nodes, a null
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) is returned. QXmlNames must
be created with the instance of
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) that is being used for
evaluating queries using this
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

This function maps to the `dm:node-name()` accessor.

If *ni* is a processing instruction, a
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) is returned with the local
name as the target name and the namespace URI and prefix both empty.

**See also** [XQuery 1.0 and XPath 2.0 Data Model (XDM), 5.11 node-name
Accessor](http://www.w3.org/TR/xpath-datamodel/#dm-node-name) and
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlName
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#name"""
        ...

    def namespaceBindings(self, n: Any) -> tuple:
        """X.namespaceBindings(n) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html)\\> QAbstractXmlNodeModel::namespaceBindings(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*n*) const

Returns the in-scope namespaces of *n*. The caller guarantees that *n* is not `null` and
that it belongs to this
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

This function corresponds to the `dm:namespace-nodes` accessor.

The returned vector of namespace declarations includes namespaces of the ancestors of
*n*.

The caller guarantees that *n* is an Element that belongs to this
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
namespaceBindings(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.List[PySide2.QtXmlPatterns.QXmlName]
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#namespaceBindings"""
        ...

    def namespaceForPrefix(self, ni: Any, prefix: Any) -> int:
        """X.namespaceForPrefix(ni, prefix) -> int

Upstream PySide2 reference signatures (binding differences may apply):

```python
namespaceForPrefix(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex, prefix: Missing('PySide2.QtXmlPatterns.QXmlName.PrefixCode')) -> Missing('PySide2.QtXmlPatterns.QXmlName.NamespaceCode')
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#namespaceForPrefix"""
        ...

    def nextFromSimpleAxis(self, axis: Any, origin: Any) -> Any:
        """X.nextFromSimpleAxis(axis, origin) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex

Supplemental documentation:
Qt 5 reference:

### `[pure virtual protected]` [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QAbstractXmlNodeModel::nextFromSimpleAxis([QAbstractXmlNodeModel::SimpleAxis](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#SimpleAxis-enum) *axis*, const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*origin*) const

When Qt XML Patterns evaluate path expressions, it emulate them through a combination of
calls with
[QSimpleXmlNodeModel::SimpleAxis](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#SimpleAxis-enum)
values. Therefore, the implementation of this function must return the node, if any,
that appears on the *axis* emanating from the *origin*.

If no such node is available, a default constructed
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) is
returned.

[QSimpleXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html)
eliminates the need to handle redundant corner cases by guaranteeing that it will never
ask for:

- Children or siblings for attributes.
- Children for comments, processing instructions, and text nodes.
- Siblings or parents for document nodes.

A typical implementation performs a `switch` on the value of *axis*:

```
QXmlNodeModelIndex MyTreeModel::nextFromSimpleAxis(SimpleAxis axis, const QXmlNodeModelIndex &origin) const
{
  // Convert the QXmlNodeModelIndex to a value that is specific to what we represent.
  const MyValue value = toMyValue(ni);

  switch(axis)
  {
      case Parent:
          return toNodeIndex(value.parent());
      case FirstChild:
      case PreviousSibling:
      case NextSibling:
          // and so on
  }
}
```

Upstream PySide2 reference signatures (binding differences may apply):

```python
nextFromSimpleAxis(self, axis: PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis, origin: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#nextFromSimpleAxis"""
        ...

    def nodesByIdref(self, NCName: Any) -> tuple:
        """X.nodesByIdref(NCName) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)\\> QAbstractXmlNodeModel::nodesByIdref(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*idref*) const

Returns the elements and/or attributes that have an `IDREF` value equal to *idref*.
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html)'s `idref()` function
calls this function.

The implementor guarantees that the nodes identified by the returned indexes are
elements or attributes.

It is not sufficient for an attribute or element to merely be called `idref`. It must
also be of type `IDREF`. Elements must be typed as `xs:IDREF` or `xs:IDREFS`, or, in the
case of attributes, as `IDREF` or `IDREFS` in the schema.

In *idref*, the `namespace URI` and the `prefix` are undefined, and the `local name` is
the ID that should be looked up.

**See also** [XQuery 1.0 and XPath 2.0 Functions and Operators, 15.5.3
fn:idref](http://www.w3.org/TR/xpath-functions/#func-idref).

Upstream PySide2 reference signatures (binding differences may apply):

```python
nodesByIdref(self, NCName: PySide2.QtXmlPatterns.QXmlName) -> typing.List[PySide2.QtXmlPatterns.QXmlNodeModelIndex]
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#nodesByIdref"""
        ...

    def root(self, n: Any) -> Any:
        """X.root(n) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QAbstractXmlNodeModel::root(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*n*) const

Returns the root node of the tree that contains the node whose index is *n*. The caller
guarantees that *n* is not `null` and that it identifies a node in this node model.

If *n* identifies a node that is a direct child of the root, parent() would return the
same [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)
returned by this function.

Upstream PySide2 reference signatures (binding differences may apply):

```python
root(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#root"""
        ...

    def sourceLocation(self, index: Any) -> Any:
        """X.sourceLocation(index) -> PythonQt.QtXmlPatterns.QSourceLocation

Supplemental documentation:
Qt 5 reference:

### [QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) QAbstractXmlNodeModel::sourceLocation(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*index*) const

Returns the source location for the object with the given *index* or a default
constructed [QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html)
in case no location information is available.

This function was introduced in Qt 4.6.

Upstream PySide2 reference signatures (binding differences may apply):

```python
sourceLocation(self, index: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QSourceLocation
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#sourceLocation"""
        ...

    def stringValue(self, n: Any) -> str:
        """X.stringValue(n) -> str

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QAbstractXmlNodeModel::stringValue(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*n*) const

Returns the string value for node *n*.

The caller guarantees that *n* is not `null` and that it belong to this
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
instance.

This function maps to the `dm:string-value()` accessor, which the specification
completely specifies. Here's a summary:

- For processing instructions, the string value is the data section(excluding any whitespace appearing between the name and the data).
- For text nodes, the string value equals the text node.
- For comments, the content of the comment
- For elements, the concatenation of all text nodes that are descendants. Note, this is not only the children, but the childrens' childrens' text nodes, and so forth.
- For document nodes, the concatenation of all text nodes in the document.

**See also** [XQuery 1.0 and XPath 2.0 Data Model (XDM), 5.13 string-value
Accessor](http://www.w3.org/TR/xpath-datamodel/#dm-string-value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
stringValue(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#stringValue"""
        ...

    def typedValue(self, n: Any) -> Any:
        """X.typedValue(n) -> object

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QAbstractXmlNodeModel::typedValue(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*node*) const

Returns the typed value for node *node*.

The typed value is an atomic value, which an element or attribute contains.

The caller guarantees that *node* is either an element or an attribute. The implementor
guarantees that the returned
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) has a value which is
supported in [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html). It cannot
be an arbitrary [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) value. The
implementor also guarantees that
[stringValue](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#stringValue)()
returns a lexical representation of typedValue() (this is guaranteed by
[QSimpleXmlNodeModel::stringValue](https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html#stringValue)()).

If the return [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) is a default
constructed variant, it signals that *node* has no typed value.

Upstream PySide2 reference signatures (binding differences may apply):

```python
typedValue(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#typedValue"""
        ...
    FirstChild: Any
    InheritNamespaces: Any
    NextSibling: Any
    NodeCopySetting: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Parent: Any
    PreserveNamespaces: Any
    PreviousSibling: Any
    SimpleAxis: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"

class QAbstractXmlReceiver:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QAbstractXmlReceiver is an abstract base class that provides a callback interface for
receiving an [XQuery
sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence),
usually the output of an [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html),
and transforming that sequence into a structure of your choosing, usually XML. Consider
the example:

```
QXmlQuery query;
query.setQuery("doc('index.html')/html/body/p[1]");

QXmlSerializer serializer(query, myOutputDevice);
query.evaluateTo(&serializer);
```

First it constructs a [query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) that
gets the first paragraph from document `index.html`. Then it constructs an [XML
serializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) with the
[query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) and
[myOutputDevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) (Note the
[serializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) is an *XML
receiver*, ie a subclass of QAbstractXmlReceiver). Finally, it
[evaluates](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo) the
[query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html), producing an ordered
sequence of calls to the
[serializer's](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) callback
functions. The sequence of callbacks transforms the query output to XML and writes it to
[myOutputDevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html).

Although the example uses [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html)
to produce the sequence of callbacks to functions in QAbstractXmlReceiver, you can call
the callback functions directly as long as your sequence of calls represents a valid
[XQuery
sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).

### XQuery Sequences

An [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) *sequence* is an
ordered collection of zero, one, or many *items*. Each *item* is either an *atomic
value* or a *node*. An *atomic value* is a simple data value.

There are six kinds of *nodes*.

- An *Element Node* represents an XML element.
- An *Attribute Node* represents an XML attribute.
- A *Document Node* represents an entire XML document.
- A *Text Node* represents character data (element content).
- A *Processing Instruction Node* represents an XML processing instruction, which is used in an XML document to tell the application reading the document to perform some action. A typical example is to use a processing instruction to tell the application to use a particular XSLT stylesheet to display the document.
- And a *Comment node* represents an XML comment.

The *sequence* of *nodes* and *atomic values* obeys the following rules. Note that
*Namespace Node* refers to a special *Attribute Node* with name *xmlns*.

- Each *node* appears in the *sequence* before its children and their descendants appear.
- A *node*'s descendants appear in the *sequence* before any of its siblings appear.
- A *Document Node* represents an entire document. Zero or more *Document Nodes* can appear in a *sequence*, but they can only be top level items (i.e., a *Document Node* can't be a child of another *node*.
- *Namespace Nodes* immediately follow the *Element Node* with which they are associated.
- *Attribute Nodes* immediately follow the *Namespace Nodes* of the element with which they are associated, or...
- If there are no *Namespace Nodes* following an element, then the *Attribute Nodes* immediately follow the element.
- An *atomic value* can only appear as a top level *item*, i.e., it can't appear as a child of a *node*.
- *Processing Instruction Nodes* do not have children, and their parent is either a *Document Node* or an *Element Node*.
- *Comment Nodes* do not have children, and their parent is either a *Document Node* or an *Element Node*.

The *sequence* of *nodes* and *atomic values* is sent to an QAbstractXmlReceiver
([QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) in the example
above) as a sequence of calls to the receiver's callback functions. The mapping of
callback functions to sequence items is as follows.

- [startDocument](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startDocument)() and [endDocument](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endDocument)() are called for each *Document Node* in the *sequence*. [endDocument](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endDocument)() is not called until all the *Document Node's* children have appeared in the *sequence*.
- [startElement](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startElement)() and [endElement](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endElement)() are called for each *Element Node*. [endElement](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endElement)() is not called until all the *Element Node's* children have appeared in the *sequence*.
- [attribute](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#attribute)() is called for each *Attribute Node*.
- [comment](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#comment)() is called for each *Comment Node*.
- [characters](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#characters)() is called for each *Text Node*.
- [processingInstruction](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#processingInstruction)() is called for each *Processing Instruction Node*.
- [namespaceBinding](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#namespaceBinding)() is called for each *Namespace Node*.
- [atomicValue](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#atomicValue)() is called for each *atomic value*.

For a complete explanation of
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) sequences, visit [XQuery
Data Model](http://www.w3.org/TR/xpath-datamodel/).

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def atomicValue(self, value: Any) -> None:
        """X.atomicValue(value)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::atomicValue(const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

This callback is called when an atomic value appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).
The *value* is a simple [data value](https://doc.qt.io/archives/qt-5.15/qvariant.html).
It is guaranteed to be
[valid](https://doc.qt.io/archives/qt-5.15/qvariant.html#isValid).

Upstream PySide2 reference signatures (binding differences may apply):

```python
atomicValue(self, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#atomicValue"""
        ...

    def attribute(self, name: Any, value: str) -> None:
        """X.attribute(name, value)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::attribute(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, const [QStringRef](https://doc.qt.io/archives/qt-5.15/qstringref.html) \\&*value*)

This callback is called when an attribute node appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).
*name* is the [attribute name](https://doc.qt.io/archives/qt-5.15/qxmlname.html) and the
*value* string contains the attribute value.

Upstream PySide2 reference signatures (binding differences may apply):

```python
attribute(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#attribute"""
        ...

    def characters(self, value: str) -> None:
        """X.characters(value)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::characters(const [QStringRef](https://doc.qt.io/archives/qt-5.15/qstringref.html) \\&*value*)

This callback is called when a text node appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).
The *value* contains the text. Adjacent text nodes may not occur in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence),
i.e., this callback must not be called twice in a row.

Upstream PySide2 reference signatures (binding differences may apply):

```python
characters(self, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#characters"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def comment(self, value: str) -> None:
        """X.comment(value)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::comment(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*value*)

This callback is called when a comment node appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).
The *value* is the comment text, which must not contain the string "--".

Upstream PySide2 reference signatures (binding differences may apply):

```python
comment(self, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#comment"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def endDocument(self) -> None:
        """X.endDocument()

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::endDocument()

This callback is called when the end of a document node appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).

Upstream PySide2 reference signatures (binding differences may apply):

```python
endDocument(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endDocument"""
        ...

    def endElement(self) -> None:
        """X.endElement()

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::endElement()

This callback is called when the end of an element node appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).

Upstream PySide2 reference signatures (binding differences may apply):

```python
endElement(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endElement"""
        ...

    def endOfSequence(self) -> None:
        """X.endOfSequence()

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::endOfSequence()

This callback is called once only, right after the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence)
ends.

Upstream PySide2 reference signatures (binding differences may apply):

```python
endOfSequence(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endOfSequence"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def namespaceBinding(self, name: Any) -> None:
        """X.namespaceBinding(name)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::namespaceBinding(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*)

This callback is called when a namespace binding is in scope of an element. A namespace
is defined by a URI. In the [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html)
*name*, the value of
[QXmlName::namespaceUri](https://doc.qt.io/archives/qt-5.15/qxmlname.html#namespaceUri)()
is that URI. The value of
[QXmlName::prefix](https://doc.qt.io/archives/qt-5.15/qxmlname.html#prefix)() is the
prefix that the URI is bound to. The local name is insignificant and can be an arbitrary
value.

Upstream PySide2 reference signatures (binding differences may apply):

```python
namespaceBinding(self, name: PySide2.QtXmlPatterns.QXmlName) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#namespaceBinding"""
        ...

    def processingInstruction(self, target: Any, value: str) -> None:
        """X.processingInstruction(target, value)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::processingInstruction(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*target*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*value*)

This callback is called when a processing instruction appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).
A processing instruction is used in an XML document to tell the application reading the
document to perform some action. A typical example is to use a processing instruction to
tell the application to use a particular XSLT stylesheet to process the document.

```
<?xml-stylesheet type="test/xsl" href="formatter.xsl"?>
```

*target* is the [name](https://doc.qt.io/archives/qt-5.15/qxmlname.html) of the
processing instruction. Its *prefix* and *namespace URI* must both be empty. Its *local
name* is the target. In the above example, the name is *xml-stylesheet*.

The *value* specifies the action to be taken. Note that the *value* must not contain the
string "?\\>". In the above example, the *value* is *type\\="test/xsl"
href\\="formatter.xsl*.

Generally, use of processing instructions should be avoided, because they are not
namespace aware and in many contexts are stripped out anyway. Processing instructions
can often be replaced with elements from a custom namespace.

Upstream PySide2 reference signatures (binding differences may apply):

```python
processingInstruction(self, target: PySide2.QtXmlPatterns.QXmlName, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#processingInstruction"""
        ...

    def startDocument(self) -> None:
        """X.startDocument()

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::startDocument()

This callback is called when a document node appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).

Upstream PySide2 reference signatures (binding differences may apply):

```python
startDocument(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startDocument"""
        ...

    def startElement(self, name: Any) -> None:
        """X.startElement(name)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::startElement(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*)

This callback is called when a new element node appears in the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence).
*name* is the valid [name](https://doc.qt.io/archives/qt-5.15/qxmlname.html) of the node
element.

Upstream PySide2 reference signatures (binding differences may apply):

```python
startElement(self, name: PySide2.QtXmlPatterns.QXmlName) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startElement"""
        ...

    def startOfSequence(self) -> None:
        """X.startOfSequence()

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractXmlReceiver::startOfSequence()

This callback is called once only, right before the
[sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence)
begins.

Upstream PySide2 reference signatures (binding differences may apply):

```python
startOfSequence(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startOfSequence"""
        ...

    def whitespaceOnly(self, value: str) -> None:
        """X.whitespaceOnly(value)

Upstream PySide2 reference signatures (binding differences may apply):

```python
whitespaceOnly(self, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#whitespaceOnly"""
        ...

class QPatternist:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

class QPatternistSDK:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

class QSimpleXmlNodeModel:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Subclassing
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
can be a significant task, because it requires implementing several, complex member
functions. QSimpleXmlNodeModel provides default implementations of these member
functions that are suitable for a wide range of node models.

Subclasses of QSimpleXmlNodeModel must be thread-safe.

Source: https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def attributes(self, element: Any) -> tuple:
        """X.attributes(element) -> tuple"""
        ...

    def baseUri(self, node: Any) -> Any:
        """X.baseUri(node) -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QSimpleXmlNodeModel::baseUri(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*node*) const

Reimplements:
[QAbstractXmlNodeModel::baseUri](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#baseUri)(const
QXmlNodeModelIndex \\&n) const.

Returns the base URI for *node*. This is always the document URI.

**See also**
[documentUri](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#documentUri)().

Source: https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html#baseUri"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def compareOrder(self, ni1: Any, ni2: Any) -> Any:
        """X.compareOrder(ni1, ni2)"""
        ...

    def createIndex(self, data: Any, additionalData: Any) -> Any:
        """X.createIndex(data, additionalData) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def documentUri(self, ni: Any) -> Any:
        """X.documentUri(ni) -> PythonQt.QtCore.QUrl"""
        ...

    def elementById(self, id: Any) -> Any:
        """X.elementById(id) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QSimpleXmlNodeModel::elementById(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*id*) const

Reimplements:
[QAbstractXmlNodeModel::elementById](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#elementById)(const
QXmlName \\&id) const.

Always returns a default constructed
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)
instance, regardless of *id*.

This effectively means the model has no elements that have an id.

Source: https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html#elementById"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isDeepEqual(self, ni1: Any, ni2: Any) -> bool:
        """X.isDeepEqual(ni1, ni2) -> bool"""
        ...

    def kind(self, ni: Any) -> Any:
        """X.kind(ni)"""
        ...

    def name(self, ni: Any) -> Any:
        """X.name(ni) -> PythonQt.QtXmlPatterns.QXmlName"""
        ...

    def namePool(self) -> Any:
        """X.namePool() -> PythonQt.QtXmlPatterns.QXmlNamePool

Supplemental documentation:
Qt 5 reference:

### [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) \\&QSimpleXmlNodeModel::namePool() const

Returns the name pool associated with this model. The implementation of
[name](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#name)() will use
this name pool to create names.

Source: https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html#namePool"""
        ...

    def namespaceBindings(self, arg__1: Any) -> tuple:
        """X.namespaceBindings(arg__1) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html)\\> QSimpleXmlNodeModel::namespaceBindings(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*node*) const

Reimplements:
[QAbstractXmlNodeModel::namespaceBindings](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#namespaceBindings)(const
QXmlNodeModelIndex \\&n) const.

Always returns an empty [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html). This
signals that no namespace bindings are in scope for *node*.

Source: https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html#namespaceBindings"""
        ...

    def namespaceForPrefix(self, ni: Any, prefix: Any) -> int:
        """X.namespaceForPrefix(ni, prefix) -> int"""
        ...

    def nextFromSimpleAxis(self, axis: Any, origin: Any) -> Any:
        """X.nextFromSimpleAxis(axis, origin) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex"""
        ...

    def nodesByIdref(self, idref: Any) -> tuple:
        """X.nodesByIdref(idref) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)\\> QSimpleXmlNodeModel::nodesByIdref(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*idref*) const

Reimplements:
[QAbstractXmlNodeModel::nodesByIdref](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#nodesByIdref)(const
QXmlName \\&idref) const.

Always returns an empty vector, regardless of *idref*.

This effectively means the model has no elements or attributes of type `IDREF`.

Source: https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html#nodesByIdref"""
        ...

    def root(self, n: Any) -> Any:
        """X.root(n) -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex"""
        ...

    def sourceLocation(self, index: Any) -> Any:
        """X.sourceLocation(index) -> PythonQt.QtXmlPatterns.QSourceLocation"""
        ...

    def stringValue(self, node: Any) -> str:
        """X.stringValue(node) -> str

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSimpleXmlNodeModel::stringValue(const [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) \\&*node*) const

Reimplements:
[QAbstractXmlNodeModel::stringValue](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#stringValue)(const
QXmlNodeModelIndex \\&n) const.

If *node* is an element or attribute,
[typedValue](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#typedValue)()
is called, and the return value converted to a string, as per
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html)'s rules.

If *node* is another type of node, the empty string is returned.

If this function is overridden for comments or processing instructions, it is important
to remember to call it (for elements and attributes having values not of type
`xs:string`) to ensure that the values are formatted according to
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html).

Source: https://doc.qt.io/archives/qt-5.15/qsimplexmlnodemodel.html#stringValue"""
        ...

    def typedValue(self, n: Any) -> Any:
        """X.typedValue(n) -> object"""
        ...
    FirstChild: Any
    InheritNamespaces: Any
    NextSibling: Any
    NodeCopySetting: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Parent: Any
    PreserveNamespaces: Any
    PreviousSibling: Any
    SimpleAxis: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"

class QSourceLocation:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSourceLocation is a simple value based class that has three properties,
[uri](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#uri)(),
[line](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#line)(), and
[column](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#column)(), that, taken
together, identify a certain point in a resource, e.g., a file or an in-memory document.

[line](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#line)() and
[column](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#column)() refer to
character counts (not byte counts), and they both start from 1, as opposed to 0\\.

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def column(self) -> int:
        """X.column() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSourceLocation::column() const

Returns the current column number. The column number refers to the count of characters,
not bytes. The first column is column 1, not 0\\. The default value is -1, indicating the
column number is unknown.

**See also**
[setColumn](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#setColumn)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
column(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#column"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isNull(self) -> bool:
        """X.isNull() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSourceLocation::isNull() const

Returns `true` if this
[QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) doesn't
identify anything.

For a default constructed
[QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html), this
function returns `true`. The same applies for any other
[QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) whose
[uri](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#uri)() is invalid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#isNull"""
        ...

    def line(self) -> int:
        """X.line() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSourceLocation::line() const

Returns the current line number. The first line number is 1, not 0\\. The default value
is -1, indicating the line number is unknown.

**See also**
[setLine](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#setLine)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
line(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#line"""
        ...

    def setColumn(self, newColumn: int) -> None:
        """X.setColumn(newColumn)

Supplemental documentation:
Qt 5 reference:

### void QSourceLocation::setColumn([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *newColumn*)

Sets the column number to *newColumn*. 0 is an invalid column number. The first column
number is 1\\.

**See also** [column](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#column)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setColumn(self, newColumn: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#setColumn"""
        ...

    def setLine(self, newLine: int) -> None:
        """X.setLine(newLine)

Supplemental documentation:
Qt 5 reference:

### void QSourceLocation::setLine([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *newLine*)

Sets the line number to *newLine*. 0 is an invalid line number. The first line number is
1\\.

**See also** [line](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#line)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLine(self, newLine: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#setLine"""
        ...

    def setUri(self, newUri: Any) -> None:
        """X.setUri(newUri)

Supplemental documentation:
Qt 5 reference:

### void QSourceLocation::setUri(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*newUri*)

Sets the URI to *newUri*.

**See also** [uri](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#uri)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUri(self, newUri: PySide2.QtCore.QUrl) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#setUri"""
        ...

    def uri(self) -> Any:
        """X.uri() -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QSourceLocation::uri() const

Returns the resource that this
[QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) refers to.
For example, the resource could be a file in the local file system, if the URI scheme is
`file`.

**See also** [setUri](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#setUri)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
uri(self) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qsourcelocation.html#uri"""
        ...

class QXmlFormatter:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QXmlFormatter is a subclass of
[QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) that formats
the XML output to make it easier for humans to read.

[QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) outputs XML
without adding unnecessary whitespace. In particular, it does not add *newlines* and
indentation. To make the XML output easier to read, QXmlFormatter adds *newlines* and
indentation by adding, removing, and modifying [sequence
nodes](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence)
that only consist of whitespace. It also modifies whitespace in other places where it is
not significant; e.g., between attributes and in the document prologue.

For example, where the base class
[QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) would output
this:

```
<a><b/><c/><p>Some Text</p></a>
```

QXmlFormatter outputs this:

```
<a>
   <b/>
   <c/>
   <p>Some Text</p>
</a>
```

If you just want to serialize your XML in a human-readable format, use QXmlFormatter as
it is. The default indentation level is 4 spaces, but you can set your own indentation
value
[setIndentationDepth](https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#setIndentationDepth)().

The *newlines* and indentation added by QXmlFormatter are suitable for common formats,
such as XHTML, SVG, or Docbook, where whitespace is not significant. However, if your
XML will be used as input where whitespace is significant, then you must write your own
subclass of [QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) or
[QAbstractXmlReceiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html).

Note that using QXmlFormatter instead of
[QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) will increase
computational overhead and document storage size due to the insertion of whitespace.

Note also that the indentation style used by QXmlFormatter remains loosely defined and
may change in future versions of Qt. If a specific indentation style is required then
either use the base class
[QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) directly, or
write your own subclass of
[QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) or
[QAbstractXmlReceiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html).
Alternatively, you can subclass QXmlFormatter and reimplement the callbacks there.

```
QXmlQuery query;
query.setQuery("doc('index.html')/html/body/p[1]");

QXmlFormatter formatter(query, myOutputDevice);
formatter.setIndentationDepth(2);
query.evaluateTo(&formatter);
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def atomicValue(self, value: Any) -> None:
        """X.atomicValue(value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::atomicValue(const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Reimplements:
[QXmlSerializer::atomicValue](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#atomicValue)(const
QVariant \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
atomicValue(self, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#atomicValue"""
        ...

    def attribute(self, name: Any, value: str) -> None:
        """X.attribute(name, value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::attribute(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, const [QStringRef](https://doc.qt.io/archives/qt-5.15/qstringref.html) \\&*value*)

Reimplements:
[QXmlSerializer::attribute](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#attribute)(const
QXmlName \\&name, const QStringRef \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
attribute(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#attribute"""
        ...

    def characters(self, value: str) -> None:
        """X.characters(value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::characters(const [QStringRef](https://doc.qt.io/archives/qt-5.15/qstringref.html) \\&*value*)

Reimplements:
[QXmlSerializer::characters](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#characters)(const
QStringRef \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
characters(self, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#characters"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def codec(self) -> Any:
        """X.codec() -> PythonQt.QtCore.QTextCodec"""
        ...

    def comment(self, value: str) -> None:
        """X.comment(value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::comment(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*value*)

Reimplements:
[QXmlSerializer::comment](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#comment)(const
QString \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
comment(self, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#comment"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def endDocument(self) -> None:
        """X.endDocument()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::endDocument()

Reimplements:
[QXmlSerializer::endDocument](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#endDocument)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
endDocument(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#endDocument"""
        ...

    def endElement(self) -> None:
        """X.endElement()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::endElement()

Reimplements:
[QXmlSerializer::endElement](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#endElement)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
endElement(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#endElement"""
        ...

    def endOfSequence(self) -> None:
        """X.endOfSequence()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::endOfSequence()

Reimplements:
[QXmlSerializer::endOfSequence](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#endOfSequence)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
endOfSequence(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#endOfSequence"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def indentationDepth(self) -> int:
        """X.indentationDepth() -> int

Supplemental documentation:
Qt 5 reference:

### int QXmlFormatter::indentationDepth() const

Returns the number of spaces
[QXmlFormatter](https://doc.qt.io/archives/qt-5.15/qxmlformatter.html) will output for
each indentation level. The default is four.

**See also**
[setIndentationDepth](https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#setIndentationDepth)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
indentationDepth(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#indentationDepth"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def namespaceBinding(self, nb: Any) -> Any:
        """X.namespaceBinding(nb)"""
        ...

    def outputDevice(self) -> Any:
        """X.outputDevice() -> PythonQt.QtCore.QIODevice"""
        ...

    def processingInstruction(self, name: Any, value: str) -> None:
        """X.processingInstruction(name, value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::processingInstruction(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*value*)

Reimplements:
[QXmlSerializer::processingInstruction](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#processingInstruction)(const
QXmlName \\&name, const QString \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
processingInstruction(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#processingInstruction"""
        ...

    def setCodec(self, codec: Any) -> Any:
        """X.setCodec(codec)"""
        ...

    def setIndentationDepth(self, depth: int) -> None:
        """X.setIndentationDepth(depth)

Supplemental documentation:
Qt 5 reference:

### void QXmlFormatter::setIndentationDepth(int *depth*)

Sets *depth* to be the number of spaces
[QXmlFormatter](https://doc.qt.io/archives/qt-5.15/qxmlformatter.html) will output for
level of indentation. The default is four.

**See also**
[indentationDepth](https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#indentationDepth)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setIndentationDepth(self, depth: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#setIndentationDepth"""
        ...

    def startDocument(self) -> None:
        """X.startDocument()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::startDocument()

Reimplements:
[QXmlSerializer::startDocument](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#startDocument)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
startDocument(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#startDocument"""
        ...

    def startElement(self, name: Any) -> None:
        """X.startElement(name)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::startElement(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*)

Reimplements:
[QXmlSerializer::startElement](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#startElement)(const
QXmlName \\&name).

Upstream PySide2 reference signatures (binding differences may apply):

```python
startElement(self, name: PySide2.QtXmlPatterns.QXmlName) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#startElement"""
        ...

    def startOfSequence(self) -> None:
        """X.startOfSequence()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlFormatter::startOfSequence()

Reimplements:
[QXmlSerializer::startOfSequence](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#startOfSequence)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
startOfSequence(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlformatter.html#startOfSequence"""
        ...

    def whitespaceOnly(self, value: Any) -> Any:
        """X.whitespaceOnly(value)"""
        ...

class QXmlItem:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

In [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html), all expressions
evaluate to a sequence of items, where each item is either an XML node or an atomic
value. The query in the following snippet evaluates to sequence of five items.

```
<aNode/>,
xs:base64Binary("FFFF"),
current-date(),
3e3, (: A floating point value :)
attribute {"name"} {()}
```

The five items are: An element, an atomic value (binary data encoded in base64), a date,
a float, and an attribute.

QXmlItem is the class that represents these
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) items in the Qt XML
Patterns API. A non-null instance of QXmlItem is either a node or an atomic value.
Calling [isNode](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNode)() or
[isAtomicValue](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isAtomicValue)() tells
you which it is. Atomic values are represented elsewhere in the Qt API as instances of
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html), and an instance of
QXmlItem that represents an atomic value can be converted to a
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) by calling
[toAtomicValue](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#toAtomicValue)(). A
QXmlItem that wraps a node is represented elsewhere as an instance of
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html). A node
QXmlItem can be converted to a
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) by
calling
[toNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#toNodeModelIndex)().

A default constructed QXmlItem instance is neither a node nor an atomic value. It is
considered null, in which case
[isNull](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNull)() returns true.

An instance of QXmlItem will be left dangling if the [XML node
model](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html) it refers to is
deleted, if it is a
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html).

Source: https://doc.qt.io/archives/qt-5.15/qxmlitem.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isAtomicValue(self) -> bool:
        """X.isAtomicValue() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlItem::isAtomicValue() const

Returns true if this item is an atomic value. Returns false if it is a node or null.

**See also** [isNull](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNull)() and
[isNode](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isAtomicValue(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isAtomicValue"""
        ...

    def isNode(self) -> bool:
        """X.isNode() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlItem::isNode() const

Returns true if this item is a Node. Returns false if it is an atomic value or null.

**See also** [isNull](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNull)() and
[isAtomicValue](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isAtomicValue)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNode(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNode"""
        ...

    def isNull(self) -> bool:
        """X.isNull() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlItem::isNull() const

Returns true if this [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) is
neither a node nor an atomic value. Default constructed instances of
[QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) are null.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNull"""
        ...

    def toAtomicValue(self) -> Any:
        """X.toAtomicValue() -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QXmlItem::toAtomicValue() const

If this [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) represents an
atomic value, it is converted to an appropriate
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) and returned. If this
[QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) is not an atomic value, the
return value is a default constructed
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html). You can call
[isAtomicValue](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isAtomicValue)() to
test whether the item is an atomic value.

**See also**
[isAtomicValue](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isAtomicValue)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
toAtomicValue(self) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlitem.html#toAtomicValue"""
        ...

    def toNodeModelIndex(self) -> Any:
        """X.toNodeModelIndex() -> PythonQt.QtXmlPatterns.QXmlNodeModelIndex

Supplemental documentation:
Qt 5 reference:

### [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) QXmlItem::toNodeModelIndex() const

If this [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) represents a node,
it returns the item as a
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html). If
this [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) is not a node, the
return value is undefined. You can call
[isNode](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNode)() to test whether the
item is a node.

**See also** [isNode](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
toNodeModelIndex(self) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlitem.html#toNodeModelIndex"""
        ...

class QXmlName:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The name of an XML node has three components: The *namespace URI*, the *local name*, and
the *prefix*. To see what these refer to in XML, consider the following snippet.

```
<book xmlns:dc='http://purl.org/dc/elements/1.1'
      xmlns='http://example.com/MyDefault'>
    <dc:title>Mobey Dick</dc:title> ...
</book>
```

For the element named *book*,
[localName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#localName)() returns
*book*, [namespaceUri](https://doc.qt.io/archives/qt-5.15/qxmlname.html#namespaceUri)()
returns *http://example.com/MyDefault*, and
[prefix](https://doc.qt.io/archives/qt-5.15/qxmlname.html#prefix)() returns an empty
string. For the element named *title*,
[localName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#localName)() returns
*title*, [namespaceUri](https://doc.qt.io/archives/qt-5.15/qxmlname.html#namespaceUri)()
returns *http://purl.org/dc/elements/1.1*, and
[prefix](https://doc.qt.io/archives/qt-5.15/qxmlname.html#prefix)() returns *dc*.

To ensure that operations with QXmlName are efficient, e.g., copying names and comparing
them, each instance of QXmlName is associated with a [name
pool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html), which must be specified at
QXmlName construction time. The three components of the QXmlName, i.e., the namespace
URI, the local name, and the prefix, are stored in the name pool mapped to identifiers
so they can be shared. For this reason, the only way to create a valid instance of
QXmlName is to use the class constructor, where the [name
pool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html), local name, namespace URI,
and prefix must all be specified.

Note that QXmlName's default constructor constructs a null instance. It is typically
used for allocating unused entries in collections of QXmlName.

A side effect of associating each instance of QXmlName with a [name
pool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) is that each instance of
QXmlName is tied to the
[QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) with which it was
created. However, the QXmlName class does not keep track of the name pool, so all the
accessor functions, e.g.,
[namespaceUri](https://doc.qt.io/archives/qt-5.15/qxmlname.html#namespaceUri)(),
[prefix](https://doc.qt.io/archives/qt-5.15/qxmlname.html#prefix)(),
[localName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#localName)(), and
[toClarkName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#toClarkName)() require
that the correct name pool be passed to them. Failure to provide the correct name pool
to these accessor functions results in undefined behavior.

Note that a [name pool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) is *not*
an XML namespace. One [name pool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html)
can represent instances of QXmlName from different XML namespaces, and the instances of
QXmlName from one XML namespace can be distributed over multiple [name
pools](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html).

### Comparing QXmlNames

To determine what a QXmlName refers to, the *namespace URI* and the *local name* are
used. The *prefix* is not used because the prefix is simply a shorthand name for use in
place of the normally much longer namespace URI. Nor is the prefix used in name
comparisons. For example, the following two element nodes represent the same element and
compare equal.

```
<svg xmlns="http://www.w3.org/2000/svg"/>
```

```
<x:svg xmlns:x="http://www.w3.org/2000/svg"/>
```

Although the second name has the prefix *x*, the two names compare equal as instances of
QXmlName, because the prefix is not used in the comparison.

A local name can never be an empty string, although the prefix and namespace URI can. If
the prefix is not empty, the namespace URI cannot be empty. Local names and prefixes
must be valid [NCNames](http://www.w3.org/TR/REC-xml-names/#NT-NCName), e.g., *abc.def*
or *abc123*.

QXmlName represents what is sometimes called an *expanded QName*, or simply a QName.

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def fromClarkName(self, clarkName: str, namePool: Any) -> Any:
        """X.fromClarkName(clarkName, namePool) -> PythonQt.QtXmlPatterns.QXmlName

Supplemental documentation:
Qt 5 reference:

### `[static]` [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#QXmlName) QXmlName::fromClarkName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*clarkName*, const [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) \\&*namePool*)

Converts *clarkName* into a
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html), inserts into *namePool*,
and returns it.

A clark name is a way to present a full QName with only one string, where the namespace
cannot contain braces. Here are a couple of examples:

| Clark Name | Description |
| --- | --- |
| `html` | The local name `html`, in no namespace |
| `http://www.w3.org/1999/xhtml`html | The local name `html`, in the XHTML namespace |
| `http://www.w3.org/1999/xhtml`my:html | The local name `html`, in the XHTML namespace, with the prefix `my` |

If the namespace contains braces, the returned value is either invalid or has undefined
content.

If *clarkName* is an invalid name, a default constructed
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) is returned.

This function was introduced in Qt 4.5.

**See also**
[toClarkName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#toClarkName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
fromClarkName(clarkName: str, namePool: PySide2.QtXmlPatterns.QXmlNamePool) -> PySide2.QtXmlPatterns.QXmlName
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html#fromClarkName"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isNCName(self, candidate: str) -> bool:
        """X.isNCName(candidate) -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QXmlName::isNCName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*candidate*)

Returns true if *candidate* is an `NCName`. An `NCName` is a string that can be used as
a name in XML and [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html), e.g.,
the prefix or local name in an element or attribute, or the name of a variable.

**See also** [Namespaces in XML 1.0 (Second Edition), \\[4\\]
NCName](http://www.w3.org/TR/REC-xml-names/#NT-NCName).

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNCName(candidate: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html#isNCName"""
        ...

    def isNull(self) -> bool:
        """X.isNull() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlName::isNull() const

Returns true if this [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) is not
initialized with a valid combination of *namespace URI*, *local name*, and *prefix*.

A valid local name is always required. The prefix and namespace URI can be empty, but if
the prefix is not empty, the namespace URI must not be empty. Local names and prefixes
must be valid [NCNames](http://www.w3.org/TR/REC-xml-names/#NT-NCName), e.g., *abc.def*
or *abc123*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html#isNull"""
        ...

    def localName(self, query: Any) -> str:
        """X.localName(query) -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QXmlName::localName(const [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) \\&*namePool*) const

Returns the local name.

Note that for efficiency, the local name string is not stored in the
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) but in the
[QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) that was passed to
the constructor. Hence, that same *namePool* must be passed to this function, so it can
be used for looking up the local name.

Upstream PySide2 reference signatures (binding differences may apply):

```python
localName(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html#localName"""
        ...

    def namespaceUri(self, query: Any) -> str:
        """X.namespaceUri(query) -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QXmlName::namespaceUri(const [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) \\&*namePool*) const

Returns the namespace URI.

Note that for efficiency, the namespace URI string is not stored in the
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) but in the
[QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) that was passed to
the constructor. Hence, that same *namePool* must be passed to this function, so it can
be used for looking up the namespace URI.

Upstream PySide2 reference signatures (binding differences may apply):

```python
namespaceUri(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html#namespaceUri"""
        ...

    def prefix(self, query: Any) -> str:
        """X.prefix(query) -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QXmlName::prefix(const [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) \\&*namePool*) const

Returns the prefix.

Note that for efficiency, the prefix string is not stored in the
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) but in the
[QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) that was passed to
the constructor. Hence, that same *namePool* must be passed to this function, so it can
be used for looking up the prefix.

Upstream PySide2 reference signatures (binding differences may apply):

```python
prefix(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html#prefix"""
        ...

    def toClarkName(self, query: Any) -> str:
        """X.toClarkName(query) -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QXmlName::toClarkName(const [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) \\&*namePool*) const

Returns this [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) formatted as a
Clark Name. For example, if the local name is `html`, the prefix is `x`, and the
namespace URI is `http://www.w3.org/1999/xhtml/`, then the Clark Name returned is:

```
{http://www.w3.org/1999/xhtml/}x:html.
```

If the local name is *MyWidget* and the namespace is empty, the Clark Name returned is:

```
MyWidget
```

Note that for efficiency, the namespace URI, local name, and prefix strings are not
stored in the [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) but in the
[QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) that was passed to
the constructor. Hence, that same *namePool* must be passed to this function, so it can
be used for looking up the three string components.

This function can be useful for debugging.

**See also** [XML Namespaces, James Clark](http://www.jclark.com/xml/xmlns.htm) and
[fromClarkName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#fromClarkName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
toClarkName(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlname.html#toClarkName"""
        ...

class QXmlNamePool:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QXmlNamePool is used to optimize operations on instances of
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html). An instance of
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) represents an XML name in a
way that allows the XML name to be compared and passed around efficiently. The
efficiency is achieved by storing the strings comprising the XML names in an instance of
QXmlNamePool, where they are mapped to binary identifiers, which are then packed into a
key which is stored in the [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html).

This means that each instance of
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) is tied to the name pool it
was created with, and that name pool should be kept in scope and used to create all
instances of [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) that might be
compared. Note also that the name pool is required if you must reconstitute the
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) as text, or if you must
access any of its component strings, so although instances of
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) can be compared without
reference to a name pool, the name pool must be kept in scope if the name's strings must
be accessed later.

Source: https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

class QXmlNodeModelIndex:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QXmlNodeModelIndex is an index into an [XML node
model](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html). It contains:

- A pointer to an [XML node model](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html), which is returned by [model](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#model)(), and
- Some data, which is returned by [data](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#data)(), [internalPointer](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#internalPointer)(), and [additionalData](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#additionalData)().

Because QXmlNodeModelIndex is intentionally a simple class, it doesn't have member
functions for accessing the properties of nodes. For example, it doesn't have functions
for getting a node's name or its list of attributes or child nodes. If you find that you
need to retrieve this kind of information from your query results, there are two ways to
proceed.

- Send the output of your [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) to an [XML receiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html), or
- Let your [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) do all the work to produce the desired result.

The second case is explained by example. Suppose you want to populate a list widget with
the values of certain attributes from a set of result elements. You could write an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) to return the set of
elements, and then you would write the code to iterate over the result elements, get
their attributes, and extract the desired string values. But the simpler way is to just
augment your [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) to finding
the desired attribute values. Then all you have to do is evaluate the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) using the version of
[QXmlQuery::evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)()
that populates a [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html),
which you can send directly to your widget.

QXmlNodeModelIndex doesn't impose any restrictions on the `data` value an
QXmlNodeModelIndex should contain. The meaning of the data left to the associated [node
model](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html). Because
QXmlNodeModelIndex depends on a particular subclass of
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
for its existence, the only way you can create an instance of QXmlNodeModelIndex is by
asking the node model to create one for you with
[QAbstractXmlNodeModel::createIndex](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#createIndex)().
Since that function is protected, it is usually a good idea to write a public function
that creates a QXmlNodeModelIndex from arguments that are appropriate for your
particular node model.

A default constructed node index is said to be null, i.e.,
[isNull](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#isNull)() returns
true.

QXmlNodeModelIndex and
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
follow the same design pattern used for
[QModelIndex](https://doc.qt.io/archives/qt-5.15/qmodelindex.html) and
[QAbstractItemModel](https://doc.qt.io/archives/qt-5.15/qabstractitemmodel.html).

Source: https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def additionalData(self) -> int:
        """X.additionalData() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QXmlNodeModelIndex::additionalData() const

Returns the second data value. The node index holds two data values.
[data](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#data)() returns the
first one.

**See also** [data](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#data)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
additionalData(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#additionalData"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def data(self) -> int:
        """X.data() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QXmlNodeModelIndex::data() const

Returns the first data value. The node index holds two data values.
[additionalData](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#additionalData)()
returns the second one.

**See also**
[additionalData](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#additionalData)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
data(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#data"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isNull(self) -> bool:
        """X.isNull() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlNodeModelIndex::isNull() const

Returns true if this
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) is a
default constructed value, otherwise false.

A null [QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)
doesn't represent any node and cannot be used in conjunction with
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#isNull"""
        ...

    def model(self) -> Any:
        """X.model() -> PythonQt.QtXmlPatterns.QAbstractXmlNodeModel

Supplemental documentation:
Qt 5 reference:

### const [QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html) \\*QXmlNodeModelIndex::model() const

Returns the
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
that this node index refers to.
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html) does
not own
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
and does not keep track of its lifetime, so this pointer will dangle if the
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
is deallocated first.

There is no setter for the node model because instances of
[QXmlNodeModelIndex](https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html)
instances are only created with
[QAbstractXmlNodeModel::createIndex](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html#createIndex)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
model(self) -> PySide2.QtXmlPatterns.QAbstractXmlNodeModel
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlnodemodelindex.html#model"""
        ...
    Attribute: Any
    Comment: Any
    Document: Any
    DocumentOrder: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Element: Any
    Follows: Any
    Is: Any
    Namespace: Any
    NodeKind: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Precedes: Any
    ProcessingInstruction: Any
    Text: Any

class QXmlQuery:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QXmlQuery class compiles and executes queries written in the [XQuery
language](http://www.w3.org/TR/xquery/). QXmlQuery is typically used to query XML data,
but it can also query non-XML data that has been modeled to look like XML.

Using QXmlQuery to query XML data, as in the snippet below, is simple because it can use
the built-in [XML data
model](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html) as its delegate to
the underlying query engine for traversing the data. The built-in data model is
specified in [XQuery 1.0 and XPath 2.0 Data
Model](http://www.w3.org/TR/xpath-datamodel/).

```
QXmlQuery query;
query.setQuery("doc('index.html')/html/body/p[1]");

QXmlSerializer serializer(query, myOutputDevice);
query.evaluateTo(&serializer);
```

The example uses QXmlQuery to match the first paragraph of an XML document and then
[output the result](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) to a device
as XML.

Using QXmlQuery to query *non-XML* data requires writing a subclass of
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
to use as a replacement for the built-in XML data model. The custom data model will be
able to traverse the non-XML data as required by the
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html)
interface. An instance of this custom data model then becomes the delegate used by the
query engine to traverse the non-XML data. For an example of how to use QXmlQuery to
query non-XML data, see the documentation for
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

### Running XQueries

To run a query set up with QXmlQuery, call one of the evaluation functions.

- [evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)([QAbstractXmlReceiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html) \\*) is called with a pointer to an XML [receiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html), which receives the query results as a sequence of callbacks. The receiver callback class is like the callback class used for translating the output of a SAX parser. [QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html), for example, is a receiver callback class for translating the sequence of callbacks for output as unformatted XML text.

- [evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)([QXmlResultItems](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html) \\*) is called with a pointer to an iterator for an empty sequence of query [result items](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html). The Java-like iterator allows the query results to be accessed sequentially.

- [evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)([QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) \\*) is like [evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)([QXmlResultItems](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html) \\*), but the query must evaluate to a sequence of strings.

### Running XPath Expressions

The XPath language is a subset of the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) language, so running an
XPath expression is the same as running an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) query. Pass the XPath
expression to QXmlQuery using
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)().

### Running XSLT Stylesheets

Running an XSLT stylesheet is like running an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html), except that when you
construct your QXmlQuery, you must pass
[QXmlQuery::XSLT20](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#QueryLanguage-enum)
to tell QXmlQuery to interpret whatever it gets from
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)() as an XSLT
stylesheet instead of as an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html). You must also set the
input document by calling
[setFocus](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setFocus)().

```
    QXmlQuery query(QXmlQuery::XSLT20);
    query.setFocus(QUrl("myInput.xml"));
    query.setQuery(QUrl("myStylesheet.xsl"));
    query.evaluateTo(out);
```

**Note:** Currently,
[setFocus](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setFocus)() must be called
*before* [setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)() when
using XSLT.

Another way to run an XSLT stylesheet is to use the `xmlpatterns` command line utility.

```
xmlpatterns myStylesheet.xsl myInput.xml
```

**Note:** For the current release, XSLT support should be considered experimental. See
section [XSLT
conformance](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html#xslt-2-0) for
details.

Stylesheet parameters are bound using
[bindVariable](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#bindVariable)().

### Binding A Query To A Starting Node

When a query is run on XML data, as in the snippet above, the `doc()` function returns
the node in the built-in data model where the query evaluation will begin. But when a
query is run on a custom node model containing non-XML data, one of the
[bindVariable](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#bindVariable)()
functions must be called to bind a variable name to a starting node in the custom model.
A $variable reference is used in the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) text to access the
starting node in the custom model. It is not necessary to declare the variable name
external in the query. See the example in the documentation for
[QAbstractXmlNodeModel](https://doc.qt.io/archives/qt-5.15/qabstractxmlnodemodel.html).

### Reentrancy and Thread-Safety

QXmlQuery is reentrant but not thread-safe. It is safe to use the QxmlQuery copy
constructor to create a copy of a query and run the same query multiple times. Behind
the scenes, QXmlQuery will reuse resources such as opened files and compiled queries to
the extent possible. But it is not safe to use the same instance of QXmlQuery in
multiple threads.

### Error Handling

Errors can occur during query evaluation. Examples include type errors and file loading
errors. When an error occurs:

- The error message is sent to the [messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#messageHandler)().
- [QXmlResultItems::hasError](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#hasError)() will return `true`, or [evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)() will return `false`;
- The results of the evaluation are undefined.

### Resource Management

When a query runs, it parses documents, allocating internal data structures to hold
them, and it may load other resources over the network. It reuses these allocated
resources when possible, to avoid having to reload and reparse them.

When [setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)() is called,
the query text is compiled into an internal data structure and optimized. The optimized
form can then be reused for multiple evaluations of the query. Since the
compile-and-optimize process can be expensive, repeating it for the same query should be
avoided by using a separate instance of QXmlQuery for each query text.

Once a document has been parsed, its internal representation is maintained in the
QXmlQuery instance and shared among multiple QXmlQuery instances.

An instance of
[QCoreApplication](https://doc.qt.io/archives/qt-5.15/qcoreapplication.html) must exist
before QXmlQuery can be used.

### Event Handling

When QXmlQuery accesses resources (e.g., calling `fn:doc()` to load a file, or accessing
a device via a bound variable), the event loop is used, which means events will be
processed. To avoid processing events when QXmlQuery accesses resources, create your
QXmlQuery instance in a separate thread.

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def bindVariable(self, localName: Any, arg__2: Any) -> None:
        """X.bindVariable(localName, arg__2)

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::bindVariable(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, const [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) \\&*value*)

Binds the variable *name* to the *value* so that $*name* can be used from within the
query to refer to the *value*.

*name* must not be *null*. *name*.isNull() must return false. If *name* has already been
bound by a previous bindVariable() call, its previous binding will be overridden.

If *value* is null so that *value*.isNull() returns true, and *name* already has a
binding, the effect is to remove the existing binding for *name*.

To bind a value of type [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) or
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html), wrap the value in a
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) such that
[QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html)'s
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) constructor is called.

All strings processed by the query must be valid
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) strings, which means
they must contain only XML 1.0 characters. However, this requirement is not checked. If
the query processes an invalid string, the behavior is undefined.

**See also**
[QVariant::isValid](https://doc.qt.io/archives/qt-5.15/qvariant.html#isValid)(), [How
QVariant maps to XQuery's Data
Model](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html#qtxdm), and
[QXmlItem::isNull](https://doc.qt.io/archives/qt-5.15/qxmlitem.html#isNull)().

### void QXmlQuery::bindVariable(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*localName*, const [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) \\&*value*)

This is an overloaded function.

This function constructs a [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html)
from *localName* using the query's
[namespace](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html). The function then
behaves as the overloaded function. It is equivalent to the following snippet.

```
    QXmlNamePool namePool(query.namePool());
    query.bindVariable(QXmlName(namePool, localName), value);
```

### void QXmlQuery::bindVariable(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*)

Binds the variable *name* to the *device* so that $*name* can be used from within the
query to refer to the *device*. The
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) *device* is exposed to
the query as a URI of type `xs:anyURI`, which can be passed to the `fn:doc()` function
to be read. E.g., this function can be used to pass an XML document in memory to
`fn:doc`.

```
    QByteArray myDocument;
    QBuffer buffer(&myDocument); // This is a QIODevice.
    buffer.open(QIODevice::ReadOnly);
    QXmlQuery query;
    query.bindVariable("myDocument", &buffer);
    query.setQuery("doc($myDocument)");
```

The caller must ensure that *device* has been opened with at least
[QIODevice::ReadOnly](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum)
prior to this binding. Otherwise, behavior is undefined.

If the query will access an XML document contained in a
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html), use a
[QBuffer](https://doc.qt.io/archives/qt-5.15/qbuffer.html) as shown in the following
snippet. Suppose *myQString* contains `<document>content</document>`

```
    QBuffer device;
    device.setData(myQString.toUtf8());
    device.open(QIODevice::ReadOnly);

    QXmlQuery query;
    query.setQuery("doc($inputDocument)/query[theDocument]");
    query.bindVariable("inputDocument", &device);
```

*name* must not be *null*. *name*.isNull() must return false. If *name* has already been
bound, its previous binding will be overridden. The URI that *name* evaluates to is
arbitrary and may change.

If the type of the variable binding changes (e.g., if a previous binding by the same
name was a [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html), or if there was
no previous binding),
[isValid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid)() will return
`false`, and recompilation of the query text is required. To recompile the query, call
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)(). For this
reason, bindVariable() should be called before
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)(), if possible.

**Note:** *device* must not be deleted while this
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) exists.

### void QXmlQuery::bindVariable(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*localName*, [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*)

This is an overloaded function.

If *localName* is a valid
[NCName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#isNCName), this function is
equivalent to the following snippet.

```
    QXmlNamePool namePool(query.namePool());
    query.bindVariable(QXmlName(namePool, localName), device);
```

A [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) is constructed from
*localName*, and is passed to the appropriate overload along with *device*.

**See also**
[QXmlName::isNCName](https://doc.qt.io/archives/qt-5.15/qxmlname.html#isNCName)().

### void QXmlQuery::bindVariable(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, const [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#QXmlQuery) \\&*query*)

Binds the result of the query *query*, to a variable by name *name*.

Evaluation of *query* will be commenced when this function is called.

If *query* is invalid, behavior is undefined. *query* will be copied.

This function was introduced in Qt 4.5.

**See also** [isValid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid)().

### void QXmlQuery::bindVariable(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*localName*, const [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#QXmlQuery) \\&*query*)

This is an overloaded function.

Has the same behavior and effects as the function being overloaded, but takes the
variable name *localName* as a
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html). *query* is used as in the
overloaded function.

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bindVariable(self, localName: str, arg__2: PySide2.QtCore.QIODevice) -> None
bindVariable(self, localName: str, query: PySide2.QtXmlPatterns.QXmlQuery) -> None
bindVariable(self, localName: str, value: PySide2.QtXmlPatterns.QXmlItem) -> None
bindVariable(self, name: PySide2.QtXmlPatterns.QXmlName, arg__2: PySide2.QtCore.QIODevice) -> None
bindVariable(self, name: PySide2.QtXmlPatterns.QXmlName, query: PySide2.QtXmlPatterns.QXmlQuery) -> None
bindVariable(self, name: PySide2.QtXmlPatterns.QXmlName, value: PySide2.QtXmlPatterns.QXmlItem) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#bindVariable"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def evaluateTo(self, target: Any) -> bool:
        """X.evaluateTo(target) -> bool

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::evaluateTo([QXmlResultItems](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html) \\**result*) const

Starts the evaluation and makes it available in *result*. If *result* is null, the
behavior is undefined. The evaluation takes place incrementally (lazy evaluation), as
the caller uses
[QXmlResultItems::next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)()
to get the next result.

**See also**
[QXmlResultItems::next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)().

### bool QXmlQuery::evaluateTo([QAbstractXmlReceiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html) \\**callback*) const

Evaluates this query and sends the result as a sequence of callbacks to the
[receiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html) *callback*.
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) does not take ownership
of *callback*.

If an error occurs during the evaluation, error messages are sent to
[messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#messageHandler)() and
`false` is returned.

If this query [is invalid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid),
`false` is returned and the behavior is undefined. If *callback* is null, behavior is
undefined.

**See also**
[QAbstractXmlReceiver](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html) and
[isValid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid)().

### bool QXmlQuery::evaluateTo([QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) \\**target*) const

Attempts to evaluate the query and returns the results in the *target* [string
list](https://doc.qt.io/archives/qt-5.15/qstringlist.html).

If the query [is valid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid) and
the evaluation succeeds, true is returned. Otherwise, false is returned and the contents
of *target* are undefined.

The query must evaluate to a sequence of `xs:string` values. If the query does not
evaluate to a sequence of strings, the values can often be converted by adding a call to
`string()` at the end of the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html).

If *target* is null, the behavior is undefined.

### bool QXmlQuery::evaluateTo([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**target*) const

Evaluates the query or stylesheet, and writes the output to *target*.

[QXmlSerializer](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html) is used to
write the output to *target*. In a future release, it is expected that this function
will be changed to respect serialization options set in the stylesheet.

If an error occurs during the evaluation, error messages are sent to
[messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#messageHandler)() and
`false` is returned.

If *target* is `null`, or is not opened in at least
[QIODevice::WriteOnly](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum)
mode, the behavior is undefined.
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) does not take ownership
of *target*.

This is an overloaded function.

This function was introduced in Qt 4.5.

### bool QXmlQuery::evaluateTo([QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\**output*) const

Evaluates the query, and serializes the output as XML to *output*.

If an error occurs during the evaluation, error messages are sent to
[messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#messageHandler)(),
the content of *output* is undefined and `false` is returned, otherwise `true` is
returned.

If *output* is `null` behavior is undefined.
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) does not take ownership
of *output*.

Internally, the class
[QXmlFormatter](https://doc.qt.io/archives/qt-5.15/qxmlformatter.html) is used for this.

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
evaluateTo(self, callback: PySide2.QtXmlPatterns.QAbstractXmlReceiver) -> bool
evaluateTo(self, result: PySide2.QtXmlPatterns.QXmlResultItems) -> None
evaluateTo(self, target: PySide2.QtCore.QIODevice) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def initialTemplateName(self) -> Any:
        """X.initialTemplateName() -> PythonQt.QtXmlPatterns.QXmlName

Supplemental documentation:
Qt 5 reference:

### [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) QXmlQuery::initialTemplateName() const

Returns the name of the XSL-T stylesheet template that the processor will call first
when running an XSL-T stylesheet. This function only applies when using
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to process XSL-T
stylesheets. By default, no initial template is set. In that case, a default constructed
[QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) is returned.

This function was introduced in Qt 4.5.

**See also**
[setInitialTemplateName](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setInitialTemplateName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
initialTemplateName(self) -> PySide2.QtXmlPatterns.QXmlName
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#initialTemplateName"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlQuery::isValid() const

Returns true if this query is valid. Examples of invalid queries are ones that contain
syntax errors or that have not had
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)() called for them
yet.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid"""
        ...

    def messageHandler(self) -> Any:
        """X.messageHandler() -> PythonQt.QtXmlPatterns.QAbstractMessageHandler

Supplemental documentation:
Qt 5 reference:

### [QAbstractMessageHandler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) \\*QXmlQuery::messageHandler() const

Returns the message handler that handles compile and runtime messages for this
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html).

**See also**
[setMessageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setMessageHandler)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#messageHandler"""
        ...

    def namePool(self) -> Any:
        """X.namePool() -> PythonQt.QtXmlPatterns.QXmlNamePool

Supplemental documentation:
Qt 5 reference:

### [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) QXmlQuery::namePool() const

Returns the name pool used by this
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) for constructing
[names](https://doc.qt.io/archives/qt-5.15/qxmlname.html). There is no setter for the
name pool, because mixing name pools causes errors due to name confusion.

Upstream PySide2 reference signatures (binding differences may apply):

```python
namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#namePool"""
        ...

    def networkAccessManager(self) -> Any:
        """X.networkAccessManager() -> PythonQt.QtNetwork.QNetworkAccessManager

Supplemental documentation:
Qt 5 reference:

### QNetworkAccessManager \\*QXmlQuery::networkAccessManager() const

Returns the network manager, or 0 if it has not been set.

This function was introduced in Qt 4.5.

**See also**
[setNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setNetworkAccessManager)().

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#networkAccessManager"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtXmlPatterns.QXmlQuery"""
        ...

    def queryLanguage(self) -> Any:
        """X.queryLanguage()

Supplemental documentation:
Qt 5 reference:

### [QXmlQuery::QueryLanguage](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#QueryLanguage-enum) QXmlQuery::queryLanguage() const

Returns a value indicating what this
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) is being used for. The
default is
[QXmlQuery::XQuery10](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#QueryLanguage-enum),
which means the [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) is being
used for running [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) and
XPath queries.
[QXmlQuery::XSLT20](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#QueryLanguage-enum)
can also be returned, which indicates the
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) is for running XSL-T
spreadsheets.

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
queryLanguage(self) -> PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#queryLanguage"""
        ...

    def setFocus(self, document: Any) -> bool:
        """X.setFocus(document) -> bool

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::setFocus(const [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) \\&*item*)

Sets the focus to *item*. The focus is the set of items that the context item expression
and path expressions navigate from. For example, in the expression *p/span*, the element
that *p* evaluates to is the focus for the following expression, *span*.

The focus can be accessed using the context item expression, i.e., dot (".").

By default, the focus is not set and is undefined. It will therefore result in a dynamic
error, `XPDY0002`, if the focus is attempted to be accessed. The focus must be set
before the query is set with
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)().

There is no behavior defined for setting an item which is null.

### bool QXmlQuery::setFocus(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*documentURI*)

This is an overloaded function.

Sets the focus to be the document located at *documentURI* and returns true. If
*documentURI* cannot be loaded, false is returned. It is undefined at what time the
document may be loaded. When loading the document, the message handler and URI resolver
set on this [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) are used.

If *documentURI* is empty or is not a valid URI, the behavior of this function is
undefined.

This function was introduced in Qt 4.5.

### bool QXmlQuery::setFocus([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**document*)

Sets the focus to be the *document* read from the
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) and returns true. If
*document* cannot be loaded, false is returned.

[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) does not take ownership
of *document*. The user guarantees that a document is available from the *document*
device and that the document is not empty. The device must be opened in at least
read-only mode. *document* must stay in scope as long as the current query is active.

This is an overloaded function.

This function was introduced in Qt 4.5.

### bool QXmlQuery::setFocus(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*focus*)

This function behaves identically to calling the setFocus() overload with a
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) whose content is *focus*
encoded as UTF-8. That is, *focus* is treated as if it contained an XML document.

Returns the same result as the overload.

This is an overloaded function.

This function was introduced in Qt 4.6.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setFocus(self, document: PySide2.QtCore.QIODevice) -> bool
setFocus(self, documentURI: PySide2.QtCore.QUrl) -> bool
setFocus(self, focus: str) -> bool
setFocus(self, item: PySide2.QtXmlPatterns.QXmlItem) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setFocus"""
        ...

    def setInitialTemplateName(self, name: Any) -> None:
        """X.setInitialTemplateName(name)

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::setInitialTemplateName(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*)

Sets the *name* of the initial template. The initial template is the one the processor
calls first, instead of attempting to match a template to the context node (if any). If
an initial template is not set, the standard order of template invocation will be used.

This function only applies when using
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to process XSL-T
stylesheets. The name becomes part of the compiled stylesheet. Therefore, this function
must be called before calling
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)().

If the stylesheet has no template named *name*, the processor will use the standard
order of template invocation.

This function was introduced in Qt 4.5.

**See also**
[initialTemplateName](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#initialTemplateName)().

### void QXmlQuery::setInitialTemplateName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*localName*)

This is an overloaded function.

Sets the name of the initial template to *localName*, which must be a valid [local
name](https://doc.qt.io/archives/qt-5.15/qxmlname.html#localName). The initial template
is the one the processor calls first, instead of attempting to match a template to the
context node (if any). If an initial template is not set, the standard order of template
invocation will be used.

This function only applies when using
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to process XSL-T
stylesheets. The name becomes part of the compiled stylesheet. Therefore, this function
must be called before calling
[setQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery)().

If *localName* is not a valid [local
name](https://doc.qt.io/archives/qt-5.15/qxmlname.html#localName), the effect is
undefined. If the stylesheet has no template named *localName*, the processor will use
the standard order of template invocation.

This function was introduced in Qt 4.5.

**See also**
[initialTemplateName](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#initialTemplateName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setInitialTemplateName(self, name: PySide2.QtXmlPatterns.QXmlName) -> None
setInitialTemplateName(self, name: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setInitialTemplateName"""
        ...

    def setMessageHandler(self, messageHandler: Any) -> None:
        """X.setMessageHandler(messageHandler)

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::setMessageHandler([QAbstractMessageHandler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) \\**aMessageHandler*)

Changes the [message
handler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) for this
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to *aMessageHandler*. The
query sends all compile and runtime messages to this message handler.
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) does not take ownership
of *aMessageHandler*.

Normally, the default message handler is sufficient. It writes compile and runtime
messages to *stderr*. The default message handler includes color codes if *stderr* can
render colors.

Note that changing the message handler after the query has been compiled has no effect,
i.e. the query uses the same message handler at runtime that it uses at compile time.

When [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) calls
[QAbstractMessageHandler::message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)(),
the arguments are as follows:

| message() argument | Semantics |
| --- | --- |
| [QtMsgType](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) type | Only [QtWarningMsg](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) and [QtFatalMsg](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) are used. The former identifies a compile or runtime warning, while the latter identifies a dynamic or static error. |
| const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\& description | An XHTML document which is the actual message. It is translated into the current language. |
| const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&identifier | Identifies the error with a URI, where the fragment is the error code, and the rest of the URI is the error namespace. |
| const [QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) \\& sourceLocation | Identifies where the error occurred. |

**See also**
[messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#messageHandler)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMessageHandler(self, messageHandler: PySide2.QtXmlPatterns.QAbstractMessageHandler) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setMessageHandler"""
        ...

    def setNetworkAccessManager(self, newManager: Any) -> Any:
        """X.setNetworkAccessManager(newManager)

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::setNetworkAccessManager(QNetworkAccessManager \\**newManager*)

Sets the network manager to *newManager*.
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) does not take ownership
of *newManager*.

This function was introduced in Qt 4.5.

**See also**
[networkAccessManager](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#networkAccessManager)().

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setNetworkAccessManager"""
        ...

    def setQuery(self, sourceCode: Any, documentURI: Any) -> None:
        """X.setQuery(sourceCode, documentURI)

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::setQuery([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**sourceCode*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*documentURI* \\= QUrl())

Sets this [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to an
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) read from the
*sourceCode* device. The device must have been opened with at least
[QIODevice::ReadOnly](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum).

*documentURI* represents the query obtained from the *sourceCode* device. It is the base
URI of the static context, as defined in the [XQuery
language](http://www.w3.org/TR/xquery/). It is used internally to resolve relative URIs
that appear in the query, and for message reporting. *documentURI* can be empty. If it
is empty, the [application file
path](https://doc.qt.io/archives/qt-5.15/qcoreapplication.html#applicationFilePath) is
used. If it is not empty, it may be either relative or absolute. If it is relative, it
is resolved itself against the [application file
path](https://doc.qt.io/archives/qt-5.15/qcoreapplication.html#applicationFilePath)
before it is used. If *documentURI* is neither a valid URI nor empty, the result is
undefined.

If the query contains a static error (e.g. syntax error), an error message is sent to
the
[messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#messageHandler)(),
and [isValid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid)() will return
*false*.

Variables must be bound before setQuery() is called.

The encoding of the [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) in
*sourceCode* is detected internally using the rules for setting and detecting encoding
of [XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) files, which are
explained in the [XQuery language](http://www.w3.org/TR/xquery/).

If *sourceCode* is `null` or not readable, or if *documentURI* is not a valid URI,
behavior is undefined.

**See also** [isValid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid)().

### void QXmlQuery::setQuery(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*sourceCode*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*documentURI* \\= QUrl())

This is an overloaded function.

The behavior and requirements of this function are the same as for
setQuery([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html)\\*, const
[QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html)\\&), after the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) has been read from the
IO device into a string. Because *sourceCode* is already a Unicode string, detection of
its encoding is unnecessary.

### void QXmlQuery::setQuery(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*queryURI*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*baseURI* \\= QUrl())

Sets this [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) to the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) read from the
*queryURI*. Use [isValid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid)()
after calling this function. If an error occurred reading *queryURI*, e.g., the query
does not exist, cannot be read, or is invalid,
[isValid](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#isValid)() will return
*false*.

The supported URI schemes are the same as those in the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) function `fn:doc`,
except that queryURI can be the object of a variable binding.

*baseURI* is the Base URI of the static context, as defined in the [XQuery
language](http://www.w3.org/TR/xquery/). It is used internally to resolve relative URIs
that appear in the query, and for message reporting. If *baseURI* is empty, *queryURI*
is used. Otherwise, *baseURI* is used, and it is resolved against the [application file
path](https://doc.qt.io/archives/qt-5.15/qcoreapplication.html#applicationFilePath) if
it is relative.

If *queryURI* is empty or invalid, or if *baseURI* is invalid, the behavior of this
function is undefined.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setQuery(self, queryURI: PySide2.QtCore.QUrl, baseURI: PySide2.QtCore.QUrl=...) -> None
setQuery(self, sourceCode: PySide2.QtCore.QIODevice, documentURI: PySide2.QtCore.QUrl=...) -> None
setQuery(self, sourceCode: str, documentURI: PySide2.QtCore.QUrl=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setQuery"""
        ...

    def setUriResolver(self, resolver: Any) -> None:
        """X.setUriResolver(resolver)

Supplemental documentation:
Qt 5 reference:

### void QXmlQuery::setUriResolver(const [QAbstractUriResolver](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html) \\**resolver*)

Sets the URI resolver to *resolver*.
[QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) does not take ownership
of *resolver*.

**See also**
[uriResolver](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#uriResolver)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUriResolver(self, resolver: PySide2.QtXmlPatterns.QAbstractUriResolver) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setUriResolver"""
        ...

    def uriResolver(self) -> Any:
        """X.uriResolver() -> PythonQt.QtXmlPatterns.QAbstractUriResolver

Supplemental documentation:
Qt 5 reference:

### const [QAbstractUriResolver](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html) \\*QXmlQuery::uriResolver() const

Returns the query's URI resolver. If no URI resolver has been set, Qt XML Patterns will
use the URIs in queries as they are.

The URI resolver provides a level of abstraction, or *polymorphic URIs*. A resolver can
rewrite *logical* URIs to physical ones, or it can translate obsolete or invalid URIs to
valid ones.

Qt XML Patterns calls the URI resolver for all URIs it encounters, except for
namespaces. Specifically, all builtin functions that deal with URIs (`fn:doc()`, and
`fn:doc-available()`).

In the case of `fn:doc()`, the absolute URI is the base URI in the static context (which
most likely is the location of the query). Rather than use the URI the user specified,
the return value of
[QAbstractUriResolver::resolve](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html#resolve)()
will be used.

When Qt XML Patterns calls
[QAbstractUriResolver::resolve](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html#resolve)()
the absolute URI is the URI mandated by the
[XQuery](https://doc.qt.io/archives/qt-5.15/xmlprocessing.html) language, and the
relative URI is the URI specified by the user.

**See also**
[setUriResolver](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#setUriResolver)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlquery.html#uriResolver"""
        ...
    QueryLanguage: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    XPath20: QueryLanguage
    XQuery10: QueryLanguage
    XSLT20: QueryLanguage
    XmlSchema11IdentityConstraintField: QueryLanguage
    XmlSchema11IdentityConstraintSelector: QueryLanguage

class QXmlResultItems:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QXmlResultItems presents the evaluation of an associated query as a sequence of
[QXmlItems](https://doc.qt.io/archives/qt-5.15/qxmlitem.html). The sequence is traversed
by repeatedly calling
[next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)(), which actually
produces the sequence by lazy evaluation of the query.

```
QXmlQuery query;
query.setQuery("<e/>, 1, 'two'");
QXmlResultItems result;

if (query.isValid()) {
    query.evaluateTo(&result);
    QXmlItem item(result.next());
    while (!item.isNull()) {
        // use item
        item = result.next();
    }
    if (result.hasError()) {
        /* Runtime error! */
    }
}
```

An effect of letting
[next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)() produce the
sequence by lazy evaluation is that a query error can occur on any call to
[next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)(). If an error
occurs, both [next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)() and
[current](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#current)() will return
the null [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html), and
[hasError](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#hasError)() will
return true.

QXmlResultItems can be thought of as an "iterator" that traverses the sequence of query
results once, in the forward direction. Each call to
[next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)() advances the
iterator to the next [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) in the
sequence and returns it, and
[current](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#current)() always
returns the [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) that
[next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)() returned the last
time it was called.

**Note:** When using the QXmlResultItems overload of
[QXmlQuery::evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)()
to execute a query, it is advisable to create a new instance of this class for each new
set of results rather than reusing an old instance.

Source: https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def current(self) -> Any:
        """X.current() -> PythonQt.QtXmlPatterns.QXmlItem

Supplemental documentation:
Qt 5 reference:

### [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) QXmlResultItems::current() const

Returns the current item. The current item is the last item that was produced and
returned by [next](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next)().

Returns a null [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) if there is
no associated [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
current(self) -> PySide2.QtXmlPatterns.QXmlItem
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#current"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def hasError(self) -> bool:
        """X.hasError() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlResultItems::hasError() const

If an error occurred during evaluation of the query, true is returned.

Returns false if query evaluation has been done.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasError(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#hasError"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def next(self) -> Any:
        """X.next() -> PythonQt.QtXmlPatterns.QXmlItem

Supplemental documentation:
Qt 5 reference:

### [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) QXmlResultItems::next()

Returns the next result in the sequence produced by lazy evaluation of the associated
query. When the returned [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) is
null, either the evaluation terminated normally without producing another result, or an
error occurred. Call
[hasError](https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#hasError)() to
determine whether the null item was caused by normal termination or by an error.

Returns a null [QXmlItem](https://doc.qt.io/archives/qt-5.15/qxmlitem.html) if there is
no associated [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
next(self) -> PySide2.QtXmlPatterns.QXmlItem
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlresultitems.html#next"""
        ...

class QXmlSchema:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QXmlSchema class loads, compiles and validates W3C XML Schema files that can be used
further for validation of XML instance documents via
[QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html).

The following example shows how to load a XML Schema file from the network and test
whether it is a valid schema document:

```
    QUrl url("http://www.schema-example.org/myschema.xsd");

    QXmlSchema schema;
    if (schema.load(url) == true)
        qDebug() << "schema is valid";
    else
        qDebug() << "schema is invalid";
```

### XML Schema Version

This class is used to represent schemas that conform to the [XML
Schema](http://www.w3.org/XML/Schema) 1.0 specification.

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def documentUri(self) -> Any:
        """X.documentUri() -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QXmlSchema::documentUri() const

Returns the document URI of the schema or an empty URI if no schema has been set.

Upstream PySide2 reference signatures (binding differences may apply):

```python
documentUri(self) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#documentUri"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlSchema::isValid() const

Returns true if this schema is valid. Examples of invalid schemas are ones that contain
syntax errors or that do not conform the W3C XML Schema specification.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid"""
        ...

    def load(self, source: Any, documentUri: Any) -> bool:
        """X.load(source, documentUri) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlSchema::load(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*source*)

Sets this [QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) to a schema
loaded from the *source* URI.

If the schema [is invalid](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid),
`false` is returned and the behavior is undefined.

Example:

```
    QUrl url("http://www.schema-example.org/myschema.xsd");

    QXmlSchema schema;
    if (schema.load(url) == true)
        qDebug() << "schema is valid";
    else
        qDebug() << "schema is invalid";
```

**See also** [isValid](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid)().

### bool QXmlSchema::load([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**source*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*documentUri* \\= QUrl())

Sets this [QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) to a schema
read from the *source* device. The device must have been opened with at least
[QIODevice::ReadOnly](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum).

*documentUri* represents the schema obtained from the *source* device. It is the base
URI of the schema, that is used internally to resolve relative URIs that appear in the
schema, and for message reporting.

If *source* is `null` or not readable, or if *documentUri* is not a valid URI, behavior
is undefined.

If the schema [is invalid](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid),
`false` is returned and the behavior is undefined.

Example:

```
    QFile file("myschema.xsd");
    file.open(QIODevice::ReadOnly);

    QXmlSchema schema;
    schema.load(&file, QUrl::fromLocalFile(file.fileName()));

    if (schema.isValid())
        qDebug() << "schema is valid";
    else
        qDebug() << "schema is invalid";
```

**See also** [isValid](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid)().

### bool QXmlSchema::load(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*data*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*documentUri* \\= QUrl())

Sets this [QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) to a schema
read from the *data*

*documentUri* represents the schema obtained from the *data*. It is the base URI of the
schema, that is used internally to resolve relative URIs that appear in the schema, and
for message reporting.

If *documentUri* is not a valid URI, behavior is undefined.

If the schema [is invalid](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid),
`false` is returned and the behavior is undefined.

Example:

```
    QByteArray data( "<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>"
                     "<xsd:schema"
                     "        xmlns:xsd=\\"http://www.w3.org/2001/XMLSchema\\""
                     "        xmlns=\\"http://www.qt-project.org/xmlschematest\\""
                     "        targetNamespace=\\"http://www.qt-project.org/xmlschematest\\""
                     "        version=\\"1.0\\""
                     "        elementFormDefault=\\"qualified\\">"
                     "</xsd:schema>" );

    QXmlSchema schema;
    schema.load(data);

    if (schema.isValid())
        qDebug() << "schema is valid";
    else
        qDebug() << "schema is invalid";
```

**See also** [isValid](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid)() and
[isValid](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#isValid)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
load(self, data: PySide2.QtCore.QByteArray, documentUri: PySide2.QtCore.QUrl=...) -> bool
load(self, source: PySide2.QtCore.QIODevice, documentUri: PySide2.QtCore.QUrl=...) -> bool
load(self, source: PySide2.QtCore.QUrl) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#load"""
        ...

    def messageHandler(self) -> Any:
        """X.messageHandler() -> PythonQt.QtXmlPatterns.QAbstractMessageHandler

Supplemental documentation:
Qt 5 reference:

### [QAbstractMessageHandler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) \\*QXmlSchema::messageHandler() const

Returns the message handler that handles compile and validation messages for this
[QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html).

**See also**
[setMessageHandler](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#setMessageHandler)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#messageHandler"""
        ...

    def namePool(self) -> Any:
        """X.namePool() -> PythonQt.QtXmlPatterns.QXmlNamePool

Supplemental documentation:
Qt 5 reference:

### [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) QXmlSchema::namePool() const

Returns the name pool used by this
[QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) for constructing
[names](https://doc.qt.io/archives/qt-5.15/qxmlname.html). There is no setter for the
name pool, because mixing name pools causes errors due to name confusion.

Upstream PySide2 reference signatures (binding differences may apply):

```python
namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#namePool"""
        ...

    def networkAccessManager(self) -> Any:
        """X.networkAccessManager() -> PythonQt.QtNetwork.QNetworkAccessManager

Supplemental documentation:
Qt 5 reference:

### QNetworkAccessManager \\*QXmlSchema::networkAccessManager() const

Returns the network manager, or 0 if it has not been set.

**See also**
[setNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#setNetworkAccessManager)().

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#networkAccessManager"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtXmlPatterns.QXmlSchema"""
        ...

    def setMessageHandler(self, handler: Any) -> None:
        """X.setMessageHandler(handler)

Supplemental documentation:
Qt 5 reference:

### void QXmlSchema::setMessageHandler([QAbstractMessageHandler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) \\**handler*)

Changes the [message
handler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) for this
[QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) to *handler*. The
schema sends all compile and validation messages to this message handler.
[QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) does not take ownership
of *handler*.

Normally, the default message handler is sufficient. It writes compile and validation
messages to *stderr*. The default message handler includes color codes if *stderr* can
render colors.

When [QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) calls
[QAbstractMessageHandler::message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)(),
the arguments are as follows:

| message() argument | Semantics |
| --- | --- |
| [QtMsgType](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) type | Only [QtWarningMsg](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) and [QtFatalMsg](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) are used. The former identifies a warning, while the latter identifies an error. |
| const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\& description | An XHTML document which is the actual message. It is translated into the current language. |
| const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&identifier | Identifies the error with a URI, where the fragment is the error code, and the rest of the URI is the error namespace. |
| const [QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) \\& sourceLocation | Identifies where the error occurred. |

**See also**
[messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#messageHandler)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMessageHandler(self, handler: PySide2.QtXmlPatterns.QAbstractMessageHandler) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#setMessageHandler"""
        ...

    def setNetworkAccessManager(self, networkmanager: Any) -> Any:
        """X.setNetworkAccessManager(networkmanager)

Supplemental documentation:
Qt 5 reference:

### void QXmlSchema::setNetworkAccessManager(QNetworkAccessManager \\**manager*)

Sets the network manager to *manager*.
[QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) does not take ownership
of *manager*.

**See also**
[networkAccessManager](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#networkAccessManager)().

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#setNetworkAccessManager"""
        ...

    def setUriResolver(self, resolver: Any) -> None:
        """X.setUriResolver(resolver)

Supplemental documentation:
Qt 5 reference:

### void QXmlSchema::setUriResolver(const [QAbstractUriResolver](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html) \\**resolver*)

Sets the URI resolver to *resolver*.
[QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) does not take ownership
of *resolver*.

**See also**
[uriResolver](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#uriResolver)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUriResolver(self, resolver: PySide2.QtXmlPatterns.QAbstractUriResolver) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#setUriResolver"""
        ...

    def uriResolver(self) -> Any:
        """X.uriResolver() -> PythonQt.QtXmlPatterns.QAbstractUriResolver

Supplemental documentation:
Qt 5 reference:

### const [QAbstractUriResolver](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html) \\*QXmlSchema::uriResolver() const

Returns the schema's URI resolver. If no URI resolver has been set, Qt XML Patterns will
use the URIs in schemas as they are.

The URI resolver provides a level of abstraction, or *polymorphic URIs*. A resolver can
rewrite *logical* URIs to physical ones, or it can translate obsolete or invalid URIs to
valid ones.

When Qt XML Patterns calls
[QAbstractUriResolver::resolve](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html#resolve)()
the absolute URI is the URI mandated by the schema specification, and the relative URI
is the URI specified by the user.

**See also**
[setUriResolver](https://doc.qt.io/archives/qt-5.15/qxmlschema.html#setUriResolver)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschema.html#uriResolver"""
        ...

class QXmlSchemaValidator:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QXmlSchemaValidator class loads, parses an XML instance document and validates it
against a W3C XML Schema that has been compiled with
[QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html).

The following example shows how to load a XML Schema from a local file, check whether it
is a valid schema document and use it for validation of an XML instance document:

```
    QUrl schemaUrl("file:///home/user/schema.xsd");

    QXmlSchema schema;
    schema.load(schemaUrl);

    if (schema.isValid()) {
        QFile file("test.xml");
        file.open(QIODevice::ReadOnly);

        QXmlSchemaValidator validator(schema);
        if (validator.validate(&file, QUrl::fromLocalFile(file.fileName())))
            qDebug() << "instance document is valid";
        else
            qDebug() << "instance document is invalid";
    }
```

### XML Schema Version

This class implements schema validation according to the [XML
Schema](http://www.w3.org/XML/Schema) 1.0 specification.

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def messageHandler(self) -> Any:
        """X.messageHandler() -> PythonQt.QtXmlPatterns.QAbstractMessageHandler

Supplemental documentation:
Qt 5 reference:

### [QAbstractMessageHandler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) \\*QXmlSchemaValidator::messageHandler() const

Returns the message handler that handles parsing and validation messages for this
[QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html).

**See also**
[setMessageHandler](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#setMessageHandler)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#messageHandler"""
        ...

    def namePool(self) -> Any:
        """X.namePool() -> PythonQt.QtXmlPatterns.QXmlNamePool

Supplemental documentation:
Qt 5 reference:

### [QXmlNamePool](https://doc.qt.io/archives/qt-5.15/qxmlnamepool.html) QXmlSchemaValidator::namePool() const

Returns the name pool used by this
[QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html) for
constructing [names](https://doc.qt.io/archives/qt-5.15/qxmlname.html). There is no
setter for the name pool, because mixing name pools causes errors due to name confusion.

Upstream PySide2 reference signatures (binding differences may apply):

```python
namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#namePool"""
        ...

    def networkAccessManager(self) -> Any:
        """X.networkAccessManager() -> PythonQt.QtNetwork.QNetworkAccessManager

Supplemental documentation:
Qt 5 reference:

### QNetworkAccessManager \\*QXmlSchemaValidator::networkAccessManager() const

Returns the network manager, or 0 if it has not been set.

**See also**
[setNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#setNetworkAccessManager)().

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#networkAccessManager"""
        ...

    def setMessageHandler(self, handler: Any) -> None:
        """X.setMessageHandler(handler)

Supplemental documentation:
Qt 5 reference:

### void QXmlSchemaValidator::setMessageHandler([QAbstractMessageHandler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) \\**handler*)

Changes the [message
handler](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html) for this
[QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html) to
*handler*. The schema validator sends all parsing and validation messages to this
message handler.
[QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html) does
not take ownership of *handler*.

Normally, the default message handler is sufficient. It writes compile and validation
messages to *stderr*. The default message handler includes color codes if *stderr* can
render colors.

When [QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html)
calls
[QAbstractMessageHandler::message](https://doc.qt.io/archives/qt-5.15/qabstractmessagehandler.html#message)(),
the arguments are as follows:

| message() argument | Semantics |
| --- | --- |
| [QtMsgType](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) type | Only [QtWarningMsg](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) and [QtFatalMsg](https://doc.qt.io/archives/qt-5.15/qtglobal.html#QtMsgType-enum) are used. The former identifies a warning, while the latter identifies an error. |
| const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\& description | An XHTML document which is the actual message. It is translated into the current language. |
| const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&identifier | Identifies the error with a URI, where the fragment is the error code, and the rest of the URI is the error namespace. |
| const [QSourceLocation](https://doc.qt.io/archives/qt-5.15/qsourcelocation.html) \\& sourceLocation | Identifies where the error occurred. |

**See also**
[messageHandler](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#messageHandler)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMessageHandler(self, handler: PySide2.QtXmlPatterns.QAbstractMessageHandler) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#setMessageHandler"""
        ...

    def setNetworkAccessManager(self, networkmanager: Any) -> Any:
        """X.setNetworkAccessManager(networkmanager)

Supplemental documentation:
Qt 5 reference:

### void QXmlSchemaValidator::setNetworkAccessManager(QNetworkAccessManager \\**manager*)

Sets the network manager to *manager*.
[QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html) does
not take ownership of *manager*.

**See also**
[networkAccessManager](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#networkAccessManager)().

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#setNetworkAccessManager"""
        ...

    def setSchema(self, schema: Any) -> None:
        """X.setSchema(schema)

Supplemental documentation:
Qt 5 reference:

### void QXmlSchemaValidator::setSchema(const [QXmlSchema](https://doc.qt.io/archives/qt-5.15/qxmlschema.html) \\&*schema*)

Sets the *schema* that shall be used for further validation. If the schema is empty, the
schema used for validation must be referenced in the XML instance document via the
`xsi:schemaLocation` or `xsi:noNamespaceSchemaLocation` attribute.

**See also**
[schema](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#schema)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSchema(self, schema: PySide2.QtXmlPatterns.QXmlSchema) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#setSchema"""
        ...

    def setUriResolver(self, resolver: Any) -> None:
        """X.setUriResolver(resolver)

Supplemental documentation:
Qt 5 reference:

### void QXmlSchemaValidator::setUriResolver(const [QAbstractUriResolver](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html) \\**resolver*)

Sets the URI resolver to *resolver*.
[QXmlSchemaValidator](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html) does
not take ownership of *resolver*.

**See also**
[uriResolver](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#uriResolver)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUriResolver(self, resolver: PySide2.QtXmlPatterns.QAbstractUriResolver) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#setUriResolver"""
        ...

    def uriResolver(self) -> Any:
        """X.uriResolver() -> PythonQt.QtXmlPatterns.QAbstractUriResolver

Supplemental documentation:
Qt 5 reference:

### const [QAbstractUriResolver](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html) \\*QXmlSchemaValidator::uriResolver() const

Returns the schema's URI resolver. If no URI resolver has been set, Qt XML Patterns will
use the URIs in instance documents as they are.

The URI resolver provides a level of abstraction, or *polymorphic URIs*. A resolver can
rewrite *logical* URIs to physical ones, or it can translate obsolete or invalid URIs to
valid ones.

When Qt XML Patterns calls
[QAbstractUriResolver::resolve](https://doc.qt.io/archives/qt-5.15/qabstracturiresolver.html#resolve)()
the absolute URI is the URI mandated by the schema specification, and the relative URI
is the URI specified by the user.

**See also**
[setUriResolver](https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#setUriResolver)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#uriResolver"""
        ...

    def validate(self, source: Any, documentUri: Any) -> bool:
        """X.validate(source, documentUri) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QXmlSchemaValidator::validate(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*source*) const

Validates the XML instance document read from *source* against the schema.

Returns `true` if the XML instance document is valid according to the schema, `false`
otherwise.

Example:

```
    const QXmlSchema schema = getSchema();

    const QUrl url("http://www.schema-example.org/test.xml");

    QXmlSchemaValidator validator(schema);
    if (validator.validate(url))
        qDebug() << "instance document is valid";
    else
        qDebug() << "instance document is invalid";
```

### bool QXmlSchemaValidator::validate([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**source*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*documentUri* \\= QUrl()) const

Validates the XML instance document read from *source* with the given *documentUri*
against the schema.

Returns `true` if the XML instance document is valid according to the schema, `false`
otherwise.

Example:

```
    const QXmlSchema schema = getSchema();

    QFile file("test.xml");
    file.open(QIODevice::ReadOnly);

    QXmlSchemaValidator validator(schema);
    if (validator.validate(&file, QUrl::fromLocalFile(file.fileName())))
        qDebug() << "instance document is valid";
    else
        qDebug() << "instance document is invalid";
```

### bool QXmlSchemaValidator::validate(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*data*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*documentUri* \\= QUrl()) const

Validates the XML instance document read from *data* with the given *documentUri*
against the schema.

Returns `true` if the XML instance document is valid according to the schema, `false`
otherwise.

Example:

```
    const QXmlSchema schema = getSchema();

    QByteArray data("<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>"
                    "<test></test>");

    QBuffer buffer(&data);
    buffer.open(QIODevice::ReadOnly);

    QXmlSchemaValidator validator(schema);
    if (validator.validate(&buffer))
        qDebug() << "instance document is valid";
    else
        qDebug() << "instance document is invalid";
```

Upstream PySide2 reference signatures (binding differences may apply):

```python
validate(self, data: PySide2.QtCore.QByteArray, documentUri: PySide2.QtCore.QUrl=...) -> bool
validate(self, source: PySide2.QtCore.QIODevice, documentUri: PySide2.QtCore.QUrl=...) -> bool
validate(self, source: PySide2.QtCore.QUrl) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlschemavalidator.html#validate"""
        ...

class QXmlSerializer:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QXmlSerializer translates an [XQuery
sequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#xquery-sequence),
usually the output of an [QXmlQuery](https://doc.qt.io/archives/qt-5.15/qxmlquery.html),
into XML. Consider the example:

```
QXmlQuery query;
query.setQuery("doc('index.html')/html/body/p[1]");

QXmlSerializer serializer(query, myOutputDevice);
query.evaluateTo(&serializer);
```

First it constructs a [query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) that
gets the first paragraph from document `index.html`. Then it constructs an instance of
this class with the [query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html) and
[myOutputDevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html). Finally, it
[evaluates](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo) the
[query](https://doc.qt.io/archives/qt-5.15/qxmlquery.html), producing an ordered
sequence of calls to the serializer's callback functions. The sequence of callbacks
transforms the query output to XML and writes it to
[myOutputDevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html).

QXmlSerializer will:

- Declare namespaces when needed,
- Use appropriate escaping, when characters can't be represented in the XML,
- Handle line endings appropriately,
- Report errors, when it can't serialize the content, e.g., when asked to serialize an attribute that is a top-level node, or when more than one top-level element is encountered.

If an error occurs during serialization, result is undefined unless the serializer is
driven through a call to
[QXmlQuery::evaluateTo](https://doc.qt.io/archives/qt-5.15/qxmlquery.html#evaluateTo)().

If the generated XML should be indented and formatted for reading, use
[QXmlFormatter](https://doc.qt.io/archives/qt-5.15/qxmlformatter.html).

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def atomicValue(self, value: Any) -> None:
        """X.atomicValue(value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::atomicValue(const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Reimplements:
[QAbstractXmlReceiver::atomicValue](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#atomicValue)(const
QVariant \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
atomicValue(self, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#atomicValue"""
        ...

    def attribute(self, name: Any, value: str) -> None:
        """X.attribute(name, value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::attribute(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, const [QStringRef](https://doc.qt.io/archives/qt-5.15/qstringref.html) \\&*value*)

Reimplements:
[QAbstractXmlReceiver::attribute](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#attribute)(const
QXmlName \\&name, const QStringRef \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
attribute(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#attribute"""
        ...

    def characters(self, value: str) -> None:
        """X.characters(value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::characters(const [QStringRef](https://doc.qt.io/archives/qt-5.15/qstringref.html) \\&*value*)

Reimplements:
[QAbstractXmlReceiver::characters](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#characters)(const
QStringRef \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
characters(self, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#characters"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def codec(self) -> Any:
        """X.codec() -> PythonQt.QtCore.QTextCodec

Supplemental documentation:
Qt 5 reference:

### const [QTextCodec](https://doc.qt.io/archives/qt-5.15/qtextcodec.html) \\*QXmlSerializer::codec() const

Returns the codec being used by the serializer for encoding its XML output.

**See also**
[setCodec](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#setCodec)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
codec(self) -> PySide2.QtCore.QTextCodec
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#codec"""
        ...

    def comment(self, value: str) -> None:
        """X.comment(value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::comment(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*value*)

Reimplements:
[QAbstractXmlReceiver::comment](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#comment)(const
QString \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
comment(self, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#comment"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def endDocument(self) -> None:
        """X.endDocument()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::endDocument()

Reimplements:
[QAbstractXmlReceiver::endDocument](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endDocument)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
endDocument(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#endDocument"""
        ...

    def endElement(self) -> None:
        """X.endElement()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::endElement()

Reimplements:
[QAbstractXmlReceiver::endElement](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endElement)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
endElement(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#endElement"""
        ...

    def endOfSequence(self) -> None:
        """X.endOfSequence()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::endOfSequence()

Reimplements:
[QAbstractXmlReceiver::endOfSequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#endOfSequence)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
endOfSequence(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#endOfSequence"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def namespaceBinding(self, nb: Any) -> None:
        """X.namespaceBinding(nb)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::namespaceBinding(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*nb*)

Reimplements:
[QAbstractXmlReceiver::namespaceBinding](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#namespaceBinding)(const
QXmlName \\&name).

Upstream PySide2 reference signatures (binding differences may apply):

```python
namespaceBinding(self, nb: PySide2.QtXmlPatterns.QXmlName) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#namespaceBinding"""
        ...

    def outputDevice(self) -> Any:
        """X.outputDevice() -> PythonQt.QtCore.QIODevice

Supplemental documentation:
Qt 5 reference:

### [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\*QXmlSerializer::outputDevice() const

Returns a pointer to the output device. There is no corresponding function to *set* the
output device, because the output device must be passed to the constructor. The
serializer does not take ownership of its IO device.

Upstream PySide2 reference signatures (binding differences may apply):

```python
outputDevice(self) -> PySide2.QtCore.QIODevice
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#outputDevice"""
        ...

    def processingInstruction(self, name: Any, value: str) -> None:
        """X.processingInstruction(name, value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::processingInstruction(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*value*)

Reimplements:
[QAbstractXmlReceiver::processingInstruction](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#processingInstruction)(const
QXmlName \\&target, const QString \\&value).

Upstream PySide2 reference signatures (binding differences may apply):

```python
processingInstruction(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#processingInstruction"""
        ...

    def setCodec(self, codec: Any) -> None:
        """X.setCodec(codec)

Supplemental documentation:
Qt 5 reference:

### void QXmlSerializer::setCodec(const [QTextCodec](https://doc.qt.io/archives/qt-5.15/qtextcodec.html) \\**outputCodec*)

Sets the codec the serializer will use for encoding its XML output. The output codec is
set to *outputCodec*. By default, the output codec is set to the one for `UTF-8`. The
serializer does not take ownership of the codec.

**See also** [codec](https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#codec)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCodec(self, codec: PySide2.QtCore.QTextCodec) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#setCodec"""
        ...

    def startDocument(self) -> None:
        """X.startDocument()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::startDocument()

Reimplements:
[QAbstractXmlReceiver::startDocument](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startDocument)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
startDocument(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#startDocument"""
        ...

    def startElement(self, name: Any) -> None:
        """X.startElement(name)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::startElement(const [QXmlName](https://doc.qt.io/archives/qt-5.15/qxmlname.html) \\&*name*)

Reimplements:
[QAbstractXmlReceiver::startElement](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startElement)(const
QXmlName \\&name).

Upstream PySide2 reference signatures (binding differences may apply):

```python
startElement(self, name: PySide2.QtXmlPatterns.QXmlName) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#startElement"""
        ...

    def startOfSequence(self) -> None:
        """X.startOfSequence()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QXmlSerializer::startOfSequence()

Reimplements:
[QAbstractXmlReceiver::startOfSequence](https://doc.qt.io/archives/qt-5.15/qabstractxmlreceiver.html#startOfSequence)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
startOfSequence(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qxmlserializer.html#startOfSequence"""
        ...

    def whitespaceOnly(self, value: Any) -> Any:
        """X.whitespaceOnly(value)"""
        ...
__all__ = ['QAbstractMessageHandler', 'QAbstractUriResolver', 'QAbstractXmlNodeModel', 'QAbstractXmlReceiver', 'QPatternist', 'QPatternistSDK', 'QSimpleXmlNodeModel', 'QSourceLocation', 'QXmlFormatter', 'QXmlItem', 'QXmlName', 'QXmlNamePool', 'QXmlNodeModelIndex', 'QXmlQuery', 'QXmlResultItems', 'QXmlSchema', 'QXmlSchemaValidator', 'QXmlSerializer']
