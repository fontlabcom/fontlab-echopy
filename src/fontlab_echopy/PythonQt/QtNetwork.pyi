# this_file: src/fontlab_echopy/PythonQt/QtNetwork.pyi
# Generated from native metadata and independent enrichment inputs.
"""Native API for PythonQt.QtNetwork."""
from __future__ import annotations
from typing import Any

class QAbstractNetworkCache:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QAbstractNetworkCache is the base class for every standard cache that is used by
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).
QAbstractNetworkCache is an abstract class and cannot be instantiated.

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def cacheSize(self) -> int:
        """X.cacheSize() -> int

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QAbstractNetworkCache::cacheSize() const

Returns the current size taken up by the cache. Depending upon the cache implementation
this might be disk or memory size.

In the base class this is a pure virtual function.

**See also**
[clear](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#clear)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
cacheSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#cacheSize"""
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

    def clear(self) -> None:
        """X.clear()

Supplemental documentation:
Qt 5 reference:

### `[pure virtual slot]` void QAbstractNetworkCache::clear()

Removes all items from the cache. Unless there was failures clearing the cache
[cacheSize](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#cacheSize)()
should return 0 after a call to clear.

In the base class this is a pure virtual function.

**See also**
[cacheSize](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#cacheSize)()
and [remove](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#remove)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
clear(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#clear"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def data(self, url: Any) -> Any:
        """X.data(url) -> PythonQt.QtCore.QIODevice

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\*QAbstractNetworkCache::data(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Returns the data associated with *url*.

It is up to the application that requests the data to delete the
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) when done with it.

If there is no cache for *url*, the url is invalid, or if there is an internal cache
error `nullptr` is returned.

In the base class this is a pure virtual function.

**See also**
[metaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#metaData)() and
[prepare](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#prepare)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
data(self, url: PySide2.QtCore.QUrl) -> PySide2.QtCore.QIODevice
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#data"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractNetworkCache.destroyed; argument details are not documented."""
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

    def insert(self, device: Any) -> None:
        """X.insert(device)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractNetworkCache::insert([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*)

Inserts the data in *device* and the prepared meta data into the cache. After this
function is called the data and meta data should be retrievable using
[data](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#data)() and
[metaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#metaData)().

To cancel a prepared inserted call
[remove](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#remove)() on the
metadata's url.

In the base class this is a pure virtual function.

**See also**
[prepare](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#prepare)() and
[remove](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#remove)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
insert(self, device: PySide2.QtCore.QIODevice) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#insert"""
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

    def metaData(self, url: Any) -> Any:
        """X.metaData(url) -> PythonQt.QtNetwork.QNetworkCacheMetaData

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html) QAbstractNetworkCache::metaData(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Returns the meta data for the url *url*.

If the url is valid and the cache contains the data for url, a valid
[QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html)
is returned.

In the base class this is a pure virtual function.

**See also**
[updateMetaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#updateMetaData)()
and [data](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#data)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
metaData(self, url: PySide2.QtCore.QUrl) -> PySide2.QtNetwork.QNetworkCacheMetaData
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#metaData"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractNetworkCache.objectNameChanged; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def prepare(self, metaData: Any) -> Any:
        """X.prepare(metaData) -> PythonQt.QtCore.QIODevice

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\*QAbstractNetworkCache::prepare(const [QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html) \\&*metaData*)

Returns the device that should be populated with the data for the cache item *metaData*.
When all of the data has been written
[insert](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#insert)() should
be called. If
[metaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#metaData) is
invalid or the url in the metadata is invalid `nullptr` is returned.

The cache owns the device and will take care of deleting it when it is inserted or
removed.

To cancel a prepared inserted call
[remove](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#remove)() on the
metadata's url.

In the base class this is a pure virtual function.

**See also**
[remove](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#remove)(),
[updateMetaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#updateMetaData)(),
and [insert](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#insert)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
prepare(self, metaData: PySide2.QtNetwork.QNetworkCacheMetaData) -> PySide2.QtCore.QIODevice
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#prepare"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def remove(self, url: Any) -> bool:
        """X.remove(url) -> bool

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` bool QAbstractNetworkCache::remove(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Removes the cache entry for *url*, returning true if success otherwise false.

In the base class this is a pure virtual function.

**See also**
[clear](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#clear)() and
[prepare](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#prepare)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
remove(self, url: PySide2.QtCore.QUrl) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#remove"""
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

    def updateMetaData(self, metaData: Any) -> None:
        """X.updateMetaData(metaData)

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` void QAbstractNetworkCache::updateMetaData(const [QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html) \\&*metaData*)

Updates the cache meta date for the
[metaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#metaData)'s url
to *metaData*

If the cache does not contains a cache item for the url then no action is taken.

In the base class this is a pure virtual function.

**See also**
[metaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#metaData)() and
[prepare](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#prepare)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
updateMetaData(self, metaData: PySide2.QtNetwork.QNetworkCacheMetaData) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#updateMetaData"""
        ...
    objectName: Any

class QAbstractSocket:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QAbstractSocket is the base class for
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) and
[QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html) and contains all common
functionality of these two classes. If you need a socket, you have two options:

- Instantiate [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) or [QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html).
- Create a native socket descriptor, instantiate QAbstractSocket, and call [setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketDescriptor)() to wrap the native socket.

TCP (Transmission Control Protocol) is a reliable, stream-oriented, connection-oriented
transport protocol. UDP (User Datagram Protocol) is an unreliable, datagram-oriented,
connectionless protocol. In practice, this means that TCP is better suited for
continuous transmission of data, whereas the more lightweight UDP can be used when
reliability isn't important.

QAbstractSocket's API unifies most of the differences between the two protocols. For
example, although UDP is connectionless,
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
establishes a virtual connection for UDP sockets, enabling you to use QAbstractSocket in
more or less the same way regardless of the underlying protocol. Internally,
QAbstractSocket remembers the address and port passed to
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)(),
and functions like [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)() and
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() use these values.

At any time, QAbstractSocket has a state (returned by
[state](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#state)()). The initial
state is
[UnconnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).
After calling
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)(),
the socket first enters
[HostLookupState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).
If the host is found, QAbstractSocket enters
[ConnectingState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
and emits the
[hostFound](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#hostFound)() signal.
When the connection has been established, it enters
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
and emits
[connected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connected)(). If an
error occurs at any stage,
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#errorOccurred)()
is emitted. Whenever the state changes,
[stateChanged](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#stateChanged)()
is emitted. For convenience,
[isValid](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#isValid)() returns
`true` if the socket is ready for reading and writing, but note that the socket's state
must be
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
before reading and writing can occur.

Read or write data by calling
[read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)() or
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)(), or use the
convenience functions
[readLine](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readLine)() and
[readAll](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readAll)(). QAbstractSocket
also inherits [getChar](https://doc.qt.io/archives/qt-5.15/qiodevice.html#getChar)(),
[putChar](https://doc.qt.io/archives/qt-5.15/qiodevice.html#putChar)(), and
[ungetChar](https://doc.qt.io/archives/qt-5.15/qiodevice.html#ungetChar)() from
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html), which work on single
bytes. The
[bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)() signal
is emitted when data has been written to the socket. Note that Qt does not limit the
write buffer size. You can monitor its size by listening to this signal.

The [readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)() signal is
emitted every time a new chunk of data has arrived.
[bytesAvailable](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesAvailable)()
then returns the number of bytes that are available for reading. Typically, you would
connect the [readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)()
signal to a slot and read all available data there. If you don't read all the data at
once, the remaining data will still be available later, and any new incoming data will
be appended to QAbstractSocket's internal read buffer. To limit the size of the read
buffer, call
[setReadBufferSize](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setReadBufferSize)().

To close the socket, call
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)().
QAbstractSocket enters
[QAbstractSocket::ClosingState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).
After all pending data has been written to the socket, QAbstractSocket actually closes
the socket, enters
[QAbstractSocket::UnconnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
and emits
[disconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnected)().
If you want to abort a connection immediately, discarding all pending data, call
[abort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#abort)() instead. If the
remote host closes the connection, QAbstractSocket will emit
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#errorOccurred)([QAbstractSocket::RemoteHostClosedError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum)),
during which the socket state will still be
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
and then the
[disconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnected)()
signal will be emitted.

The port and address of the connected peer is fetched by calling
[peerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort)() and
[peerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress)().
[peerName](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerName)() returns
the host name of the peer, as passed to
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)().
[localPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localPort)() and
[localAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress)()
return the port and address of the local socket.

QAbstractSocket provides a set of functions that suspend the calling thread until
certain signals are emitted. These functions can be used to implement blocking sockets:

- [waitForConnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForConnected)() blocks until a connection has been established.
- [waitForReadyRead](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForReadyRead)() blocks until new data is available for reading.
- [waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForBytesWritten)() blocks until one payload of data has been written to the socket.
- [waitForDisconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForDisconnected)() blocks until the connection has closed.

We show an example:

```
    int numRead = 0, numReadTotal = 0;
    char buffer[50];

    forever {
        numRead  = socket.read(buffer, 50);

        // do whatever with array

        numReadTotal += numRead;
        if (numRead == 0 && !socket.waitForReadyRead())
            break;
    }
```

If
[waitForReadyRead()](https://doc.qt.io/archives/qt-5.15/qiodevice.html#waitForReadyRead)
returns `false`, the connection has been closed or an error has occurred.

Programming with a blocking socket is radically different from programming with a
non-blocking socket. A blocking socket doesn't require an event loop and typically leads
to simpler code. However, in a GUI application, blocking sockets should only be used in
non-GUI threads, to avoid freezing the user interface. See the
[fortuneclient](https://doc.qt.io/archives/qt-5.15/qtnetwork-fortuneclient-example.html)
and
[blockingfortuneclient](https://doc.qt.io/archives/qt-5.15/qtnetwork-blockingfortuneclient-example.html)
examples for an overview of both approaches.

**Note:** We discourage the use of the blocking functions together with signals. One of
the two possibilities should be used.

QAbstractSocket can be used with
[QTextStream](https://doc.qt.io/archives/qt-5.15/qtextstream.html) and
[QDataStream](https://doc.qt.io/archives/qt-5.15/qdatastream.html)'s stream operators
(operator\\<\\<() and operator\\>\\>()). There is one issue to be aware of, though: You must
make sure that enough data is available before attempting to read it using
operator\\>\\>().

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abort(self) -> None:
        """X.abort()

Supplemental documentation:
Qt 5 reference:

### void QAbstractSocket::abort()

Aborts the current connection and resets the socket. Unlike
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)(),
this function immediately closes the socket, discarding any pending data in the write
buffer.

**See also**
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)()
and [close](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
abort(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#abort"""
        ...

    def aboutToClose(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.aboutToClose; argument details are not documented."""
        ...

    def atEnd(self) -> bool:
        """X.atEnd() -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QAbstractSocket::atEnd() const

Reimplements:
[QIODevice::atEnd](https://doc.qt.io/archives/qt-5.15/qiodevice.html#atEnd)() const.

Returns `true` if no more data is currently available for reading; otherwise returns
`false`.

This function is most commonly used when reading data from the socket in a loop. For
example:

```
 // This slot is connected to QAbstractSocket::readyRead()
 void SocketClass::readyReadSlot()
 {
     while (!socket.atEnd()) {
         QByteArray data = socket.read(100);
         ....
     }
 }
```

**See also**
[bytesAvailable](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesAvailable)()
and [readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
atEnd(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#atEnd"""
        ...

    def bind(self, address: Any, port: int, mode: Any) -> bool:
        """X.bind(address, port, mode) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QAbstractSocket::bind(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*address*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port* \\= 0, [QAbstractSocket::BindMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum) *mode* \\= ...)

Binds to *address* on port *port*, using the
[BindMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum)
*mode*.

For UDP sockets, after binding, the signal
[QUdpSocket::readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)()
is emitted whenever a UDP datagram arrives on the specified address and port. Thus, this
function is useful to write UDP servers.

For TCP sockets, this function may be used to specify which interface to use for an
outgoing connection, which is useful in case of multiple network interfaces.

By default, the socket is bound using the
[DefaultForPlatform](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum)
[BindMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum). If a
port is not specified, a random port is chosen.

On success, the function returns `true` and the socket enters
[BoundState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum);
otherwise it returns `false`.

This function was introduced in Qt 5.0.

### bool QAbstractSocket::bind([quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port* \\= 0, [QAbstractSocket::BindMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum) *mode* \\= DefaultForPlatform)

This is an overloaded function.

Binds to [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html):Any on
port *port*, using the
[BindMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum)
*mode*.

By default, the socket is bound using the
[DefaultForPlatform](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum)
[BindMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#BindFlag-enum). If a
port is not specified, a random port is chosen.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bind(self, address: PySide2.QtNetwork.QHostAddress, port: int=..., mode: PySide2.QtNetwork.QAbstractSocket.BindMode=...) -> bool
bind(self, port: int=..., mode: PySide2.QtNetwork.QAbstractSocket.BindMode=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def bytesAvailable(self) -> int:
        """X.bytesAvailable() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QAbstractSocket::bytesAvailable() const

Reimplements:
[QIODevice::bytesAvailable](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesAvailable)()
const.

Returns the number of incoming bytes that are waiting to be read.

**See also**
[bytesToWrite](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesToWrite)()
and [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesAvailable(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesAvailable"""
        ...

    def bytesToWrite(self) -> int:
        """X.bytesToWrite() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QAbstractSocket::bytesToWrite() const

Reimplements:
[QIODevice::bytesToWrite](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesToWrite)()
const.

Returns the number of bytes that are waiting to be written. The bytes are written when
control goes back to the event loop or when
[flush](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#flush)() is called.

**See also**
[bytesAvailable](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesAvailable)()
and [flush](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#flush)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesToWrite(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesToWrite"""
        ...

    def bytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.bytesWritten; argument details are not documented."""
        ...

    def canReadLine(self) -> bool:
        """X.canReadLine() -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QAbstractSocket::canReadLine() const

Reimplements:
[QIODevice::canReadLine](https://doc.qt.io/archives/qt-5.15/qiodevice.html#canReadLine)()
const.

Returns `true` if a line of data can be read from the socket; otherwise returns `false`.

**See also** [readLine](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readLine)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
canReadLine(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#canReadLine"""
        ...

    def channelBytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.channelBytesWritten; argument details are not documented."""
        ...

    def channelReadyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.channelReadyRead; argument details are not documented."""
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

    def close(self) -> None:
        """X.close()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QAbstractSocket::close()

Reimplements:
[QIODevice::close](https://doc.qt.io/archives/qt-5.15/qiodevice.html#close)().

Closes the I/O device for the socket and calls
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)()
to close the socket's connection.

See [QIODevice::close](https://doc.qt.io/archives/qt-5.15/qiodevice.html#close)() for a
description of the actions that occur when an I/O device is closed.

**See also** [abort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#abort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
close(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#close"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def connectToHost(self, hostName: Any, port: int, mode: Any, protocol: Any) -> None:
        """X.connectToHost(hostName, port, mode, protocol)

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QAbstractSocket::connectToHost(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite, [QAbstractSocket::NetworkLayerProtocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum) *protocol* \\= AnyIPProtocol)

Attempts to make a connection to *hostName* on the given *port*. The *protocol*
parameter can be used to specify which network protocol to use (eg. IPv4 or IPv6).

The socket is opened in the given *openMode* and first enters
[HostLookupState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
then performs a host name lookup of *hostName*. If the lookup succeeds,
[hostFound](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#hostFound)() is
emitted and [QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html)
enters
[ConnectingState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).
It then attempts to connect to the address or addresses returned by the lookup. Finally,
if a connection is established,
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) enters
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
and emits
[connected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connected)().

At any point, the socket can emit
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#errorOccurred)()
to signal that an error occurred.

*hostName* may be an IP address in string form (e.g., "43.195.83.32"), or it may be a
host name (e.g., "example.com").
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) will do a
lookup only if required. *port* is in native byte order.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#state)(),
[peerName](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerName)(),
[peerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress)(),
[peerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort)(), and
[waitForConnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForConnected)().

### `[virtual]` void QAbstractSocket::connectToHost(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*address*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite)

This is an overloaded function.

Attempts to make a connection to *address* on port *port*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
connectToHost(self, address: PySide2.QtNetwork.QHostAddress, port: int, mode: PySide2.QtCore.QIODevice.OpenMode=...) -> None
connectToHost(self, hostName: str, port: int, mode: PySide2.QtCore.QIODevice.OpenMode=..., protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost"""
        ...

    def connected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.connected; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QAbstractSocket::connected()

This signal is emitted after
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
has been called and a connection has been successfully established.

**Note:** On some operating systems the connected() signal may be directly emitted from
the
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
call for connections to the localhost.

**See also**
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
and
[disconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnected)().

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connected"""
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
        """Native PythonQt.QtNetwork.QAbstractSocket.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def disconnectFromHost(self) -> None:
        """X.disconnectFromHost()

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QAbstractSocket::disconnectFromHost()

Attempts to close the socket. If there is pending data waiting to be written,
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) will enter
[ClosingState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
and wait until all data has been written. Eventually, it will enter
[UnconnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
and emit the
[disconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnected)()
signal.

**See also**
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
disconnectFromHost(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost"""
        ...

    def disconnected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.disconnected; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QAbstractSocket::disconnected()

This signal is emitted when the socket has been disconnected.

**Warning:** If you need to delete the
[sender](https://doc.qt.io/archives/qt-5.15/qobject.html#sender)() of this signal in a
slot connected to it, use the
[deleteLater()](https://doc.qt.io/archives/qt-5.15/qobject.html#deleteLater) function.

**See also**
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)(),
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)(),
and [abort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#abort)().

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnected"""
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

    def error(self) -> Any:
        """X.error()

Supplemental documentation:
Qt 5 reference:

### [QAbstractSocket::SocketError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum) QAbstractSocket::error() const

Returns the type of error that last occurred.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#state)()
and [errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
error(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#error"""
        ...

    def errorOccurred(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.errorOccurred; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QAbstractSocket::errorOccurred([QAbstractSocket::SocketError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum) *socketError*)

This signal is emitted after an error occurred. The *socketError* parameter describes
the type of error that occurred.

When this signal is emitted, the socket may not be ready for a reconnect attempt. In
that case, attempts to reconnect should be done from the event loop. For example, use a
[QTimer::singleShot](https://doc.qt.io/archives/qt-5.15/qtimer.html#singleShot)() with 0
as the timeout.

[QAbstractSocket::SocketError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum)
is not a registered metatype, so for queued connections, you will have to register it
with
[Q\\_DECLARE\\_METATYPE](https://doc.qt.io/archives/qt-5.15/qmetatype.html#Q_DECLARE_METATYPE)()
and
[qRegisterMetaType](https://doc.qt.io/archives/qt-5.15/qmetatype.html#qRegisterMetaType-1)().

This function was introduced in Qt 5.15.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#error)(),
[errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)(), and
[Creating Custom Qt Types](https://doc.qt.io/archives/qt-5.15/custom-types.html).

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#errorOccurred"""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str"""
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

    def flush(self) -> bool:
        """X.flush() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QAbstractSocket::flush()

This function writes as much as possible from the internal write buffer to the
underlying network socket, without blocking. If any data was written, this function
returns `true`; otherwise false is returned.

Call this function if you need
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) to start
sending buffered data immediately. The number of bytes successfully written depends on
the operating system. In most cases, you do not need to call this function, because
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) will start
sending data automatically once control goes back to the event loop. In the absence of
an event loop, call
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForBytesWritten)()
instead.

**See also** [write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() and
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForBytesWritten)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
flush(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#flush"""
        ...

    def getChar(self, c: Any) -> bool:
        """X.getChar(c) -> bool"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hostFound(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.hostFound; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QAbstractSocket::hostFound()

This signal is emitted after
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
has been called and the host lookup has succeeded.

**Note:** Since Qt 4.6.3
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) may emit
hostFound() directly from the
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
call since a DNS result could have been cached.

**See also**
[connected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connected)().

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#hostFound"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isOpen(self) -> bool:
        """X.isOpen() -> bool"""
        ...

    def isReadable(self) -> bool:
        """X.isReadable() -> bool"""
        ...

    def isSequential(self) -> bool:
        """X.isSequential() -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QAbstractSocket::isSequential() const

Reimplements:
[QIODevice::isSequential](https://doc.qt.io/archives/qt-5.15/qiodevice.html#isSequential)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSequential(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#isSequential"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isTextModeEnabled(self) -> bool:
        """X.isTextModeEnabled() -> bool"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QAbstractSocket::isValid() const

Returns `true` if the socket is valid and ready for use; otherwise returns `false`.

**Note:** The socket's state must be
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
before reading and writing can occur.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#state)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#isValid"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def isWritable(self) -> bool:
        """X.isWritable() -> bool"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def localAddress(self) -> Any:
        """X.localAddress() -> PythonQt.QtNetwork.QHostAddress

Supplemental documentation:
Qt 5 reference:

### [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) QAbstractSocket::localAddress() const

Returns the host address of the local socket if available; otherwise returns
[QHostAddress::Null](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum).

This is normally the main IP address of the host, but can be
[QHostAddress::LocalHost](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum)
(127.0.0.1) for connections to the local host.

**See also**
[localPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localPort)(),
[peerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress)(),
and
[setLocalAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalAddress)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localAddress(self) -> PySide2.QtNetwork.QHostAddress
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress"""
        ...

    def localPort(self) -> int:
        """X.localPort() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QAbstractSocket::localPort() const

Returns the host port number (in native byte order) of the local socket if available;
otherwise returns 0\\.

**See also**
[localAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress)(),
[peerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort)(), and
[setLocalPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localPort(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localPort"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.objectNameChanged; argument details are not documented."""
        ...

    def open(self, mode: Any) -> bool:
        """X.open(mode) -> bool"""
        ...

    def openMode(self) -> Any:
        """X.openMode()"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def pauseMode(self) -> Any:
        """X.pauseMode()

Supplemental documentation:
Qt 5 reference:

### [QAbstractSocket::PauseModes](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#PauseMode-enum) QAbstractSocket::pauseMode() const

Returns the pause mode of this socket.

This function was introduced in Qt 5.0.

**See also**
[setPauseMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPauseMode)()
and [resume](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#resume)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
pauseMode(self) -> PySide2.QtNetwork.QAbstractSocket.PauseModes
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#pauseMode"""
        ...

    def peek(self, maxlen: Any) -> Any:
        """X.peek(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def peerAddress(self) -> Any:
        """X.peerAddress() -> PythonQt.QtNetwork.QHostAddress

Supplemental documentation:
Qt 5 reference:

### [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) QAbstractSocket::peerAddress() const

Returns the address of the connected peer if the socket is in
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum);
otherwise returns
[QHostAddress::Null](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum).

**See also**
[peerName](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerName)(),
[peerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort)(),
[localAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress)(),
and
[setPeerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerAddress)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerAddress(self) -> PySide2.QtNetwork.QHostAddress
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress"""
        ...

    def peerName(self) -> str:
        """X.peerName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QAbstractSocket::peerName() const

Returns the name of the peer as specified by
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)(),
or an empty [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) if
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
has not been called.

**See also**
[peerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress)(),
[peerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort)(), and
[setPeerName](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerName"""
        ...

    def peerPort(self) -> int:
        """X.peerPort() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QAbstractSocket::peerPort() const

Returns the port of the connected peer if the socket is in
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum);
otherwise returns 0\\.

**See also**
[peerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress)(),
[localPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localPort)(), and
[setPeerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerPort(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort"""
        ...

    def pos(self) -> int:
        """X.pos() -> int"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def proxy(self) -> Any:
        """X.proxy() -> PythonQt.QtNetwork.QNetworkProxy

Supplemental documentation:
Qt 5 reference:

### [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) QAbstractSocket::proxy() const

Returns the network proxy for this socket. By default
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
is used, which means this socket will query the default proxy settings for the
application.

This function was introduced in Qt 4.1.

**See also**
[setProxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setProxy)(),
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html), and
[QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
proxy(self) -> PySide2.QtNetwork.QNetworkProxy
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#proxy"""
        ...

    def proxyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.proxyAuthenticationRequired; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QAbstractSocket::proxyAuthenticationRequired(const [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) \\&*proxy*, [QAuthenticator](https://doc.qt.io/archives/qt-5.15/qauthenticator.html) \\**authenticator*)

This signal can be emitted when a *proxy* that requires authentication is used. The
*authenticator* object can then be filled in with the required details to allow
authentication and continue the connection.

**Note:** It is not possible to use a QueuedConnection to connect to this signal, as the
connection will fail if the authenticator has not been filled in with new information
when the signal returns.

This function was introduced in Qt 4.3.

**See also** [QAuthenticator](https://doc.qt.io/archives/qt-5.15/qauthenticator.html)
and [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html).

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#proxyAuthenticationRequired"""
        ...

    def putChar(self, c: Any) -> bool:
        """X.putChar(c) -> bool"""
        ...

    def read(self, maxlen: Any) -> Any:
        """X.read(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readAll(self) -> Any:
        """X.readAll() -> PythonQt.QtCore.QByteArray"""
        ...

    def readBufferSize(self) -> int:
        """X.readBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QAbstractSocket::readBufferSize() const

Returns the size of the internal read buffer. This limits the amount of data that the
client can receive before you call
[read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)() or
[readAll](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readAll)().

A read buffer size of 0 (the default) means that the buffer has no size limit, ensuring
that no data is lost.

**See also**
[setReadBufferSize](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setReadBufferSize)()
and [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
readBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#readBufferSize"""
        ...

    def readChannelFinished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.readChannelFinished; argument details are not documented."""
        ...

    def readData(self, data: str, maxlen: int) -> int:
        """X.readData(data, maxlen) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QAbstractSocket::readData(char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *maxSize*)

Reimplements:
[QIODevice::readData](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readData)(char
\\*data, qint64 maxSize).

Upstream PySide2 reference signatures (binding differences may apply):

```python
readData(self, data: str, maxlen: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#readData"""
        ...

    def readLine(self, maxlen: Any) -> Any:
        """X.readLine(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readLineData(self, data: str, maxlen: int) -> int:
        """X.readLineData(data, maxlen) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QAbstractSocket::readLineData(char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *maxlen*)

Reimplements:
[QIODevice::readLineData](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readLineData)(char
\\*data, qint64 maxSize).

Upstream PySide2 reference signatures (binding differences may apply):

```python
readLineData(self, data: str, maxlen: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#readLineData"""
        ...

    def readyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.readyRead; argument details are not documented."""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def reset(self) -> bool:
        """X.reset() -> bool"""
        ...

    def resume(self) -> None:
        """X.resume()

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QAbstractSocket::resume()

Continues data transfer on the socket. This method should only be used after the socket
has been set to pause upon notifications and a notification has been received. The only
notification currently supported is QSslSocket::sslErrors(). Calling this method if the
socket is not paused results in undefined behavior.

This function was introduced in Qt 5.0.

**See also**
[pauseMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#pauseMode)() and
[setPauseMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPauseMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
resume(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#resume"""
        ...

    def seek(self, pos: Any) -> bool:
        """X.seek(pos) -> bool"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setErrorString(self, errorString: Any) -> Any:
        """X.setErrorString(errorString)"""
        ...

    def setLocalAddress(self, address: Any) -> None:
        """X.setLocalAddress(address)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QAbstractSocket::setLocalAddress(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*address*)

Sets the address on the local side of a connection to *address*.

You can call this function in a subclass of
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) to change the
return value of the
[localAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress)()
function after a connection has been established. This feature is commonly used by proxy
connections for virtual connection settings.

Note that this function does not bind the local address of the socket prior to a
connection (e.g.,
[QAbstractSocket::bind](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind)()).

This function was introduced in Qt 4.1.

**See also**
[localAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress)(),
[setLocalPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalPort)(),
and
[setPeerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerAddress)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLocalAddress(self, address: PySide2.QtNetwork.QHostAddress) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalAddress"""
        ...

    def setLocalPort(self, port: int) -> None:
        """X.setLocalPort(port)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QAbstractSocket::setLocalPort([quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*)

Sets the port on the local side of a connection to *port*.

You can call this function in a subclass of
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) to change the
return value of the
[localPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localPort)()
function after a connection has been established. This feature is commonly used by proxy
connections for virtual connection settings.

Note that this function does not bind the local port of the socket prior to a connection
(e.g.,
[QAbstractSocket::bind](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind)()).

This function was introduced in Qt 4.1.

**See also**
[localPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localPort)(),
[localAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress)(),
[setLocalAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalAddress)(),
and
[setPeerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLocalPort(self, port: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalPort"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setOpenMode(self, openMode: Any) -> Any:
        """X.setOpenMode(openMode)"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setPauseMode(self, pauseMode: Any) -> None:
        """X.setPauseMode(pauseMode)

Supplemental documentation:
Qt 5 reference:

### void QAbstractSocket::setPauseMode([QAbstractSocket::PauseModes](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#PauseMode-enum) *pauseMode*)

Controls whether to pause upon receiving a notification. The *pauseMode* parameter
specifies the conditions in which the socket should be paused. The only notification
currently supported is QSslSocket::sslErrors(). If set to
[PauseOnSslErrors](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#PauseMode-enum),
data transfer on the socket will be paused and needs to be enabled explicitly again by
calling [resume](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#resume)(). By
default this option is set to
[PauseNever](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#PauseMode-enum).
This option must be called before connecting to the server, otherwise it will result in
undefined behavior.

This function was introduced in Qt 5.0.

**See also**
[pauseMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#pauseMode)() and
[resume](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#resume)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPauseMode(self, pauseMode: PySide2.QtNetwork.QAbstractSocket.PauseModes) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPauseMode"""
        ...

    def setPeerAddress(self, address: Any) -> None:
        """X.setPeerAddress(address)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QAbstractSocket::setPeerAddress(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*address*)

Sets the address of the remote side of the connection to *address*.

You can call this function in a subclass of
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) to change the
return value of the
[peerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress)()
function after a connection has been established. This feature is commonly used by proxy
connections for virtual connection settings.

This function was introduced in Qt 4.1.

**See also**
[peerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerAddress)(),
[setPeerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerPort)(),
and
[setLocalAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalAddress)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerAddress(self, address: PySide2.QtNetwork.QHostAddress) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerAddress"""
        ...

    def setPeerName(self, name: str) -> None:
        """X.setPeerName(name)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QAbstractSocket::setPeerName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Sets the host name of the remote peer to *name*.

You can call this function in a subclass of
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) to change the
return value of the
[peerName](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerName)() function
after a connection has been established. This feature is commonly used by proxy
connections for virtual connection settings.

This function was introduced in Qt 4.1.

**See also**
[peerName](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerName(self, name: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerName"""
        ...

    def setPeerPort(self, port: int) -> None:
        """X.setPeerPort(port)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QAbstractSocket::setPeerPort([quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*)

Sets the port of the remote side of the connection to *port*.

You can call this function in a subclass of
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) to change the
return value of the
[peerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort)() function
after a connection has been established. This feature is commonly used by proxy
connections for virtual connection settings.

This function was introduced in Qt 4.1.

**See also**
[peerPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#peerPort)(),
[setPeerAddress](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerAddress)(),
and
[setLocalPort](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setLocalPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerPort(self, port: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPeerPort"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setProxy(self, networkProxy: Any) -> None:
        """X.setProxy(networkProxy)

Supplemental documentation:
Qt 5 reference:

### void QAbstractSocket::setProxy(const [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) \\&*networkProxy*)

Sets the explicit network proxy for this socket to *networkProxy*.

To disable the use of a proxy for this socket, use the
[QNetworkProxy::NoProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
proxy type:

```
socket->setProxy(QNetworkProxy::NoProxy);
```

The default value for the proxy is
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum),
which means the socket will use the application settings: if a proxy is set with
[QNetworkProxy::setApplicationProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setApplicationProxy),
it will use that; otherwise, if a factory is set with
[QNetworkProxyFactory::setApplicationProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#setApplicationProxyFactory),
it will query that factory with type
[QNetworkProxyQuery::TcpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum).

This function was introduced in Qt 4.1.

**See also** [proxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#proxy)(),
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html), and
[QNetworkProxyFactory::queryProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#queryProxy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProxy(self, networkProxy: PySide2.QtNetwork.QNetworkProxy) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setProxy"""
        ...

    def setReadBufferSize(self, size: int) -> None:
        """X.setReadBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QAbstractSocket::setReadBufferSize([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *size*)

Sets the size of
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html)'s internal
read buffer to be *size* bytes.

If the buffer size is limited to a certain size,
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) won't buffer
more than this size of data. Exceptionally, a buffer size of 0 means that the read
buffer is unlimited and all incoming data is buffered. This is the default.

This option is useful if you only read the data at certain points in time (e.g., in a
real-time streaming application) or if you want to protect your socket against receiving
too much data, which may eventually cause your application to run out of memory.

Only [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) uses
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html)'s internal
buffer; [QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html) does not use
any buffering at all, but rather relies on the implicit buffering provided by the
operating system. Because of this, calling this function on
[QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html) has no effect.

**See also**
[readBufferSize](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#readBufferSize)()
and [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setReadBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setReadBufferSize"""
        ...

    def setSocketDescriptor(self, socketDescriptor: int, state: Any, openMode: Any) -> bool:
        """X.setSocketDescriptor(socketDescriptor, state, openMode) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QAbstractSocket::setSocketDescriptor([qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) *socketDescriptor*, [QAbstractSocket::SocketState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum) *socketState* \\= ConnectedState, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite)

Initializes [QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html)
with the native socket descriptor *socketDescriptor*. Returns `true` if
*socketDescriptor* is accepted as a valid socket descriptor; otherwise returns `false`.
The socket is opened in the mode specified by *openMode*, and enters the socket state
specified by *socketState*. Read and write buffers are cleared, discarding any pending
data.

**Note:** It is not possible to initialize two abstract sockets with the same native
socket descriptor.

**See also**
[socketDescriptor](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketDescriptor)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketDescriptor(self, socketDescriptor: int, state: PySide2.QtNetwork.QAbstractSocket.SocketState=..., openMode: PySide2.QtCore.QIODevice.OpenMode=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketDescriptor"""
        ...

    def setSocketError(self, socketError: Any) -> None:
        """X.setSocketError(socketError)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QAbstractSocket::setSocketError([QAbstractSocket::SocketError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum) *socketError*)

Sets the type of error that last occurred to *socketError*.

**See also**
[setSocketState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketState)()
and
[setErrorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#setErrorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketError(self, socketError: PySide2.QtNetwork.QAbstractSocket.SocketError) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketError"""
        ...

    def setSocketOption(self, option: Any, value: Any) -> None:
        """X.setSocketOption(option, value)

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QAbstractSocket::setSocketOption([QAbstractSocket::SocketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketOption-enum) *option*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the given *option* to the value described by *value*.

**Note:** On Windows Runtime,
[QAbstractSocket::KeepAliveOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketOption-enum)
must be set before the socket is connected.

This function was introduced in Qt 4.6.

**See also**
[socketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketOption"""
        ...

    def setSocketState(self, state: Any) -> None:
        """X.setSocketState(state)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QAbstractSocket::setSocketState([QAbstractSocket::SocketState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum) *state*)

Sets the state of the socket to *state*.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#state)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketState(self, state: PySide2.QtNetwork.QAbstractSocket.SocketState) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketState"""
        ...

    def setTextModeEnabled(self, enabled: Any) -> Any:
        """X.setTextModeEnabled(enabled)"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def size(self) -> int:
        """X.size() -> int"""
        ...

    def socketDescriptor(self) -> int:
        """X.socketDescriptor() -> int

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) QAbstractSocket::socketDescriptor() const

Returns the native socket descriptor of the
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) object if
this is available; otherwise returns -1.

If the socket is using
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html), the returned
descriptor may not be usable with native socket functions.

The socket descriptor is not available when
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) is in
[UnconnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).

**See also**
[setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketDescriptor)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
socketDescriptor(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketDescriptor"""
        ...

    def socketOption(self, option: Any) -> Any:
        """X.socketOption(option) -> object

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QAbstractSocket::socketOption([QAbstractSocket::SocketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketOption-enum) *option*)

Returns the value of the *option* option.

This function was introduced in Qt 4.6.

**See also**
[setSocketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
socketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketOption"""
        ...

    def socketType(self) -> Any:
        """X.socketType()

Supplemental documentation:
Qt 5 reference:

### [QAbstractSocket::SocketType](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketType-enum) QAbstractSocket::socketType() const

Returns the socket type (TCP, UDP, or other).

**See also** [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) and
[QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
socketType(self) -> PySide2.QtNetwork.QAbstractSocket.SocketType
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketType"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def state(self) -> Any:
        """X.state()

Supplemental documentation:
Qt 5 reference:

### [QAbstractSocket::SocketState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum) QAbstractSocket::state() const

Returns the state of the socket.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#error)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
state(self) -> PySide2.QtNetwork.QAbstractSocket.SocketState
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#state"""
        ...

    def stateChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QAbstractSocket.stateChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QAbstractSocket::stateChanged([QAbstractSocket::SocketState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum) *socketState*)

This signal is emitted whenever
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html)'s state
changes. The *socketState* parameter is the new state.

[QAbstractSocket::SocketState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
is not a registered metatype, so for queued connections, you will have to register it
with
[Q\\_DECLARE\\_METATYPE](https://doc.qt.io/archives/qt-5.15/qmetatype.html#Q_DECLARE_METATYPE)()
and
[qRegisterMetaType](https://doc.qt.io/archives/qt-5.15/qmetatype.html#qRegisterMetaType-1)().

**See also** [state](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#state)()
and [Creating Custom Qt Types](https://doc.qt.io/archives/qt-5.15/custom-types.html).

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#stateChanged"""
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

    def ungetChar(self, c: Any) -> Any:
        """X.ungetChar(c)"""
        ...

    def waitForBytesWritten(self, msecs: int) -> bool:
        """X.waitForBytesWritten(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QAbstractSocket::waitForBytesWritten(int *msecs* \\= 30000\\)

Reimplements:
[QIODevice::waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#waitForBytesWritten)(int
msecs).

This function blocks until at least one byte has been written on the socket and the
[bytesWritten()](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten) signal
has been emitted. The function will timeout after *msecs* milliseconds; the default
timeout is 30000 milliseconds.

The function returns `true` if the
[bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)() signal
is emitted; otherwise it returns `false` (if an error occurred or the operation timed
out).

**Note:** This function may fail randomly on Windows. Consider using the event loop and
the [bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)()
signal if your software will run on Windows.

**See also**
[waitForReadyRead](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForReadyRead)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForBytesWritten(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForBytesWritten"""
        ...

    def waitForConnected(self, msecs: int) -> bool:
        """X.waitForConnected(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QAbstractSocket::waitForConnected(int *msecs* \\= 30000\\)

Waits until the socket is connected, up to *msecs* milliseconds. If the connection has
been established, this function returns `true`; otherwise it returns `false`. In the
case where it returns `false`, you can call
[error](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#error)() to determine
the cause of the error.

The following example waits up to one second for a connection to be established:

```
socket->connectToHost("imap", 143);
if (socket->waitForConnected(1000))
    qDebug("Connected!");
```

If msecs is -1, this function will not time out.

**Note:** This function may wait slightly longer than *msecs*, depending on the time it
takes to complete the host lookup.

**Note:** Multiple calls to this functions do not accumulate the time. If the function
times out, the connecting process will be aborted.

**Note:** This function may fail randomly on Windows. Consider using the event loop and
the [connected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connected)()
signal if your software will run on Windows.

**See also**
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
and [connected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connected)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForConnected(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForConnected"""
        ...

    def waitForDisconnected(self, msecs: int) -> bool:
        """X.waitForDisconnected(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QAbstractSocket::waitForDisconnected(int *msecs* \\= 30000\\)

Waits until the socket has disconnected, up to *msecs* milliseconds. If the connection
was successfully disconnected, this function returns `true`; otherwise it returns
`false` (if the operation timed out, if an error occurred, or if this
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) is already
disconnected). In the case where it returns `false`, you can call
[error](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#error)() to determine
the cause of the error.

The following example waits up to one second for a connection to be closed:

```
socket->disconnectFromHost();
if (socket->state() == QAbstractSocket::UnconnectedState
    || socket->waitForDisconnected(1000)) {
        qDebug("Disconnected!");
}
```

If msecs is -1, this function will not time out.

**Note:** This function may fail randomly on Windows. Consider using the event loop and
the
[disconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnected)()
signal if your software will run on Windows.

**See also**
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)()
and [close](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForDisconnected(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForDisconnected"""
        ...

    def waitForReadyRead(self, msecs: int) -> bool:
        """X.waitForReadyRead(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QAbstractSocket::waitForReadyRead(int *msecs* \\= 30000\\)

Reimplements:
[QIODevice::waitForReadyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#waitForReadyRead)(int
msecs).

This function blocks until new data is available for reading and the
[readyRead()](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead) signal has
been emitted. The function will timeout after *msecs* milliseconds; the default timeout
is 30000 milliseconds.

The function returns `true` if the
[readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)() signal is
emitted and there is new data available for reading; otherwise it returns `false` (if an
error occurred or the operation timed out).

**Note:** This function may fail randomly on Windows. Consider using the event loop and
the [readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)() signal if
your software will run on Windows.

**See also**
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForBytesWritten)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForReadyRead(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForReadyRead"""
        ...

    def write(self, data: Any) -> int:
        """X.write(data) -> int"""
        ...

    def writeData(self, data: str, len: int) -> int:
        """X.writeData(data, len) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QAbstractSocket::writeData(const char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *size*)

Reimplements:
[QIODevice::writeData](https://doc.qt.io/archives/qt-5.15/qiodevice.html#writeData)(const
char \\*data, qint64 maxSize).

Upstream PySide2 reference signatures (binding differences may apply):

```python
writeData(self, data: str, len: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#writeData"""
        ...
    AddressInUseError: Any
    AnyIPProtocol: Any
    Append: Any
    BindFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BindMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BoundState: Any
    ClosingState: Any
    ConnectedState: Any
    ConnectingState: Any
    ConnectionRefusedError: Any
    DatagramTooLargeError: Any
    DefaultForPlatform: Any
    DontShareAddress: Any
    HostLookupState: Any
    HostNotFoundError: Any
    IPv4Protocol: Any
    IPv6Protocol: Any
    KeepAliveOption: Any
    ListeningState: Any
    LowDelayOption: Any
    MulticastLoopbackOption: Any
    MulticastTtlOption: Any
    NetworkError: Any
    NetworkLayerProtocol: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NotOpen: Any
    OpenMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenModeFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OperationError: Any
    PathMtuSocketOption: Any
    PauseMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseModes: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseNever: Any
    PauseOnSslErrors: Any
    ProxyAuthenticationRequiredError: Any
    ProxyConnectionClosedError: Any
    ProxyConnectionRefusedError: Any
    ProxyConnectionTimeoutError: Any
    ProxyNotFoundError: Any
    ProxyProtocolError: Any
    ReadOnly: Any
    ReadWrite: Any
    ReceiveBufferSizeSocketOption: Any
    RemoteHostClosedError: Any
    ReuseAddressHint: Any
    SctpSocket: Any
    SendBufferSizeSocketOption: Any
    ShareAddress: Any
    SocketAccessError: Any
    SocketAddressNotAvailableError: Any
    SocketError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketOption: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketResourceError: Any
    SocketState: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketTimeoutError: Any
    SocketType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslHandshakeFailedError: Any
    SslInternalError: Any
    SslInvalidUserDataError: Any
    TcpSocket: Any
    TemporaryError: Any
    Text: Any
    Truncate: Any
    TypeOfServiceOption: Any
    UdpSocket: Any
    Unbuffered: Any
    UnconnectedState: Any
    UnfinishedSocketOperationError: Any
    UnknownNetworkLayerProtocol: Any
    UnknownSocketError: Any
    UnknownSocketType: Any
    UnsupportedSocketOperationError: Any
    WriteOnly: Any
    objectName: Any

class QAuthenticator:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QAuthenticator class is usually used in the
[authenticationRequired()](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#authenticationRequired)
and
[proxyAuthenticationRequired()](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyAuthenticationRequired)
signals of
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
and [QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html). The
class provides a way to pass back the required authentication information to the socket
when accessing services that require authentication.

QAuthenticator supports the following authentication methods:

- Basic
- NTLM version 2
- Digest-MD5
- SPNEGO/Negotiate

### Options

In addition to the username and password required for authentication, a QAuthenticator
object can also contain additional options. The
[options](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#options)() function can
be used to query incoming options sent by the server; the
[setOption](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setOption)() function
can be used to set outgoing options, to be processed by the authenticator calculation.
The options accepted and provided depend on the authentication type (see method()).

The following tables list known incoming options as well as accepted outgoing options.
The list of incoming options is not exhaustive, since servers may include additional
information at any time. The list of outgoing options is exhaustive, however, and no
unknown options will be treated or sent back to the server.

#### Basic

| Option | Direction | Type | Description |
| --- | --- | --- | --- |
| `realm` | Incoming | [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) | Contains the realm of the authentication, the same as [realm](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#realm)() |

The Basic authentication mechanism supports no outgoing options.

#### NTLM version 2

The NTLM authentication mechanism currently supports no incoming or outgoing options. On
Windows, if no *user* has been set, domain\\\\user credentials will be searched for on the
local system to enable Single-Sign-On functionality.

#### Digest-MD5

| Option | Direction | Type | Description |
| --- | --- | --- | --- |
| `realm` | Incoming | [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) | Contains the realm of the authentication, the same as [realm](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#realm)() |

The Digest-MD5 authentication mechanism supports no outgoing options.

#### SPNEGO/Negotiate

This authentication mechanism currently supports no incoming or outgoing options.

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html"""

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

    def isNull(self) -> bool:
        """X.isNull() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QAuthenticator::isNull() const

Returns `true` if the object has not been initialized. Returns `false` if non-const
member functions have been called, or the content was constructed or copied from another
initialized [QAuthenticator](https://doc.qt.io/archives/qt-5.15/qauthenticator.html)
object.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#isNull"""
        ...

    def option(self, opt: str) -> Any:
        """X.option(opt) -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QAuthenticator::option(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*opt*) const

Returns the value related to option *opt* if it was set by the server. See the [Options
section](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#qauthenticator-options)
for more information on incoming options. If option *opt* isn't found, an invalid
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) will be returned.

This function was introduced in Qt 4.7.

**See also**
[setOption](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setOption)(),
[options](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#options)(), and
[QAuthenticator
options](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#qauthenticator-options).

Upstream PySide2 reference signatures (binding differences may apply):

```python
option(self, opt: str) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#option"""
        ...

    def options(self) -> dict:
        """X.options() -> dict

Supplemental documentation:
Qt 5 reference:

### [QVariantHash](https://doc.qt.io/archives/qt-5.15/qvariant.html#QVariantHash-typedef) QAuthenticator::options() const

Returns all incoming options set in this
[QAuthenticator](https://doc.qt.io/archives/qt-5.15/qauthenticator.html) object by
parsing the server reply. See the [Options
section](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#qauthenticator-options)
for more information on incoming options.

This function was introduced in Qt 4.7.

**See also** [option](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#option)()
and [QAuthenticator
options](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#qauthenticator-options).

Upstream PySide2 reference signatures (binding differences may apply):

```python
options(self) -> typing.Dict[str, typing.Any]
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#options"""
        ...

    def password(self) -> str:
        """X.password() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QAuthenticator::password() const

Returns the password used for authentication.

**See also**
[setPassword](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setPassword)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
password(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#password"""
        ...

    def realm(self) -> str:
        """X.realm() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QAuthenticator::realm() const

Returns the realm requiring authentication.

Upstream PySide2 reference signatures (binding differences may apply):

```python
realm(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#realm"""
        ...

    def setOption(self, opt: str, value: Any) -> None:
        """X.setOption(opt, value)

Supplemental documentation:
Qt 5 reference:

### void QAuthenticator::setOption(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*opt*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the outgoing option *opt* to value *value*. See the [Options
section](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#qauthenticator-options)
for more information on outgoing options.

This function was introduced in Qt 4.7.

**See also**
[options](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#options)(),
[option](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#option)(), and
[QAuthenticator
options](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#qauthenticator-options).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setOption(self, opt: str, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setOption"""
        ...

    def setPassword(self, password: str) -> None:
        """X.setPassword(password)

Supplemental documentation:
Qt 5 reference:

### void QAuthenticator::setPassword(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*password*)

Sets the *password* used for authentication.

**See also**
[password](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#password)() and
[QNetworkAccessManager::authenticationRequired](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#authenticationRequired)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPassword(self, password: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setPassword"""
        ...

    def setRealm(self, realm: str) -> None:
        """X.setRealm(realm)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRealm(self, realm: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setRealm"""
        ...

    def setUser(self, user: str) -> None:
        """X.setUser(user)

Supplemental documentation:
Qt 5 reference:

### void QAuthenticator::setUser(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*user*)

Sets the *user* used for authentication.

**See also** [user](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#user)() and
[QNetworkAccessManager::authenticationRequired](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#authenticationRequired)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUser(self, user: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setUser"""
        ...

    def user(self) -> str:
        """X.user() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QAuthenticator::user() const

Returns the user used for authentication.

**See also**
[setUser](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setUser)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
user(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qauthenticator.html#user"""
        ...

class QDnsDomainNameRecord:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

When performing a name server lookup, zero or more records will be returned. Each record
is represented by a QDnsDomainNameRecord instance.

Source: https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html"""

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

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsDomainNameRecord::name() const

Returns the name for this record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html#name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QDnsDomainNameRecord"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QDnsDomainNameRecord::swap([QDnsDomainNameRecord](https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html#QDnsDomainNameRecord) \\&*other*)

Swaps this domain-name record instance with *other*. This function is very fast and
never fails.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QDnsDomainNameRecord) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html#swap"""
        ...

    def timeToLive(self) -> int:
        """X.timeToLive() -> int

Supplemental documentation:
Qt 5 reference:

### [quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) QDnsDomainNameRecord::timeToLive() const

Returns the duration in seconds for which this record is valid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
timeToLive(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html#timeToLive"""
        ...

    def value(self) -> str:
        """X.value() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsDomainNameRecord::value() const

Returns the value for this domain name record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
value(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html#value"""
        ...

class QDnsHostAddressRecord:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

When performing an address lookup, zero or more records will be returned. Each record is
represented by a QDnsHostAddressRecord instance.

Source: https://doc.qt.io/archives/qt-5.15/qdnshostaddressrecord.html"""

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

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsHostAddressRecord::name() const

Returns the name for this record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnshostaddressrecord.html#name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QDnsHostAddressRecord"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QDnsHostAddressRecord::swap([QDnsHostAddressRecord](https://doc.qt.io/archives/qt-5.15/qdnshostaddressrecord.html#QDnsHostAddressRecord) \\&*other*)

Swaps this host address record instance with *other*. This function is very fast and
never fails.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QDnsHostAddressRecord) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnshostaddressrecord.html#swap"""
        ...

    def timeToLive(self) -> int:
        """X.timeToLive() -> int

Supplemental documentation:
Qt 5 reference:

### [quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) QDnsHostAddressRecord::timeToLive() const

Returns the duration in seconds for which this record is valid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
timeToLive(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnshostaddressrecord.html#timeToLive"""
        ...

    def value(self) -> Any:
        """X.value() -> PythonQt.QtNetwork.QHostAddress

Supplemental documentation:
Qt 5 reference:

### [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) QDnsHostAddressRecord::value() const

Returns the value for this host address record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
value(self) -> PySide2.QtNetwork.QHostAddress
```

Source: https://doc.qt.io/archives/qt-5.15/qdnshostaddressrecord.html#value"""
        ...

class QDnsLookup:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QDnsLookup uses the mechanisms provided by the operating system to perform DNS lookups.
To perform a lookup you need to specify a
[name](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#name-prop) and
[type](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#type-prop) then invoke the
[lookup()](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#lookup) slot. The
[finished()](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#finished) signal will be
emitted upon completion.

For example, you can determine which servers an XMPP chat client should connect to for a
given domain with:

```
void MyObject::lookupServers()
{
    // Create a DNS lookup.
    dns = new QDnsLookup(this);
    connect(dns, SIGNAL(finished()),
            this, SLOT(handleServers()));

    // Find the XMPP servers for gmail.com
    dns->setType(QDnsLookup::SRV);
    dns->setName("_xmpp-client._tcp.gmail.com");
    dns->lookup();
}
```

Once the request finishes you can handle the results with:

```
void MyObject::handleServers()
{
    // Check the lookup succeeded.
    if (dns->error() != QDnsLookup::NoError) {
        qWarning("DNS lookup failed");
        dns->deleteLater();
        return;
    }

    // Handle the results.
    const auto records = dns->serviceRecords();
    for (const QDnsServiceRecord &record : records) {
        ...
    }
    dns->deleteLater();
}
```

**Note:** If you simply want to find the IP address(es) associated with a host name, or
the host name associated with an IP address you should use
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) instead.

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abort(self) -> None:
        """X.abort()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QDnsLookup::abort()

Aborts the DNS lookup operation.

If the lookup is already finished, does nothing.

Upstream PySide2 reference signatures (binding differences may apply):

```python
abort(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#abort"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def canonicalNameRecords(self) -> tuple:
        """X.canonicalNameRecords() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QDnsDomainNameRecord](https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html)\\> QDnsLookup::canonicalNameRecords() const

Returns the list of canonical name records associated with this lookup.

Upstream PySide2 reference signatures (binding differences may apply):

```python
canonicalNameRecords(self) -> typing.List[PySide2.QtNetwork.QDnsDomainNameRecord]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#canonicalNameRecords"""
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
        """Native PythonQt.QtNetwork.QDnsLookup.destroyed; argument details are not documented."""
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

    def finished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QDnsLookup.finished; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QDnsLookup::finished()

This signal is emitted when the reply has finished processing.

**Note:** Notifier signal for property
[error](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#error-prop). Notifier signal
for property
[errorString](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#errorString-prop).

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#finished"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hostAddressRecords(self) -> tuple:
        """X.hostAddressRecords() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QDnsHostAddressRecord](https://doc.qt.io/archives/qt-5.15/qdnshostaddressrecord.html)\\> QDnsLookup::hostAddressRecords() const

Returns the list of host address records associated with this lookup.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hostAddressRecords(self) -> typing.List[PySide2.QtNetwork.QDnsHostAddressRecord]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#hostAddressRecords"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isFinished(self) -> bool:
        """X.isFinished() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QDnsLookup::isFinished() const

Returns whether the reply has finished or was aborted.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isFinished(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#isFinished"""
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

    def lookup(self) -> None:
        """X.lookup()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QDnsLookup::lookup()

Performs the DNS lookup.

The [finished()](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#finished) signal is
emitted upon completion.

Upstream PySide2 reference signatures (binding differences may apply):

```python
lookup(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#lookup"""
        ...

    def mailExchangeRecords(self) -> tuple:
        """X.mailExchangeRecords() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QDnsMailExchangeRecord](https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html)\\> QDnsLookup::mailExchangeRecords() const

Returns the list of mail exchange records associated with this lookup.

The records are sorted according to [RFC
5321](http://www.rfc-editor.org/rfc/rfc5321.txt), so if you use them to connect to
servers, you should try them in the order they are listed.

Upstream PySide2 reference signatures (binding differences may apply):

```python
mailExchangeRecords(self) -> typing.List[PySide2.QtNetwork.QDnsMailExchangeRecord]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#mailExchangeRecords"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def nameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QDnsLookup.nameChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QDnsLookup::nameChanged(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

This signal is emitted when the lookup
[name](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#name-prop) changes. *name* is
the new lookup name.

**Note:** Notifier signal for property
[name](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#name-prop).

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#nameChanged"""
        ...

    def nameServerRecords(self) -> tuple:
        """X.nameServerRecords() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QDnsDomainNameRecord](https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html)\\> QDnsLookup::nameServerRecords() const

Returns the list of name server records associated with this lookup.

Upstream PySide2 reference signatures (binding differences may apply):

```python
nameServerRecords(self) -> typing.List[PySide2.QtNetwork.QDnsDomainNameRecord]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#nameServerRecords"""
        ...

    def nameserverChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QDnsLookup.nameserverChanged; argument details are not documented."""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QDnsLookup.objectNameChanged; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def pointerRecords(self) -> tuple:
        """X.pointerRecords() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QDnsDomainNameRecord](https://doc.qt.io/archives/qt-5.15/qdnsdomainnamerecord.html)\\> QDnsLookup::pointerRecords() const

Returns the list of pointer records associated with this lookup.

Upstream PySide2 reference signatures (binding differences may apply):

```python
pointerRecords(self) -> typing.List[PySide2.QtNetwork.QDnsDomainNameRecord]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#pointerRecords"""
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

    def serviceRecords(self) -> tuple:
        """X.serviceRecords() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QDnsServiceRecord](https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html)\\> QDnsLookup::serviceRecords() const

Returns the list of service records associated with this lookup.

The records are sorted according to [RFC
2782](http://www.rfc-editor.org/rfc/rfc2782.txt), so if you use them to connect to
servers, you should try them in the order they are listed.

Upstream PySide2 reference signatures (binding differences may apply):

```python
serviceRecords(self) -> typing.List[PySide2.QtNetwork.QDnsServiceRecord]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#serviceRecords"""
        ...

    def setName(self, name: str) -> None:
        """X.setName(name)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setName(self, name: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#setName"""
        ...

    def setNameserver(self, nameserver: Any) -> None:
        """X.setNameserver(nameserver)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setNameserver(self, nameserver: PySide2.QtNetwork.QHostAddress) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#setNameserver"""
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

    def setType(self, arg__1: Any) -> None:
        """X.setType(arg__1)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setType(self, arg__1: PySide2.QtNetwork.QDnsLookup.Type) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#setType"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def textRecords(self) -> tuple:
        """X.textRecords() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QDnsTextRecord](https://doc.qt.io/archives/qt-5.15/qdnstextrecord.html)\\> QDnsLookup::textRecords() const

Returns the list of text records associated with this lookup.

Upstream PySide2 reference signatures (binding differences may apply):

```python
textRecords(self) -> typing.List[PySide2.QtNetwork.QDnsTextRecord]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#textRecords"""
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

    def typeChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QDnsLookup.typeChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QDnsLookup::typeChanged([QDnsLookup::Type](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#Type-enum) *type*)

This signal is emitted when the lookup
[type](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#type-prop) changes. *type* is
the new lookup type.

**Note:** Notifier signal for property
[type](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#type-prop).

Source: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#typeChanged"""
        ...
    A: Any
    AAAA: Any
    ANY: Any
    CNAME: Any
    Error: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    InvalidReplyError: Any
    InvalidRequestError: Any
    MX: Any
    NS: Any
    NoError: Any
    NotFoundError: Any
    OperationCancelledError: Any
    PTR: Any
    ResolverError: Any
    SRV: Any
    ServerFailureError: Any
    ServerRefusedError: Any
    TXT: Any
    Type: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    error: Any
    'Qt 5 reference:\n\n### error : const [Error](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#Error-enum)\n\nThis property holds the type of error that occurred if the DNS lookup failed, or\n[NoError](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#Error-enum).\n\n**Access functions:**\n\n| QDnsLookup::Error | **error**() const |\n| --- | --- |\n\n**Notifier signal:**\n\n| void | **[finished](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#finished)**() |\n| --- | --- |\n\nSource: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#error'
    errorString: str
    'Qt 5 reference:\n\n### errorString : const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)\n\nThis property holds a human-readable description of the error if the DNS lookup failed.\n\n**Access functions:**\n\n| QString | **errorString**() const |\n| --- | --- |\n\n**Notifier signal:**\n\n| void | **[finished](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#finished)**() |\n| --- | --- |\n\nSource: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#errorString'
    name: str
    "Qt 5 reference:\n\n### name : [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)\n\nThis property holds the name to lookup.\n\n**Note:** The name will be encoded using IDNA, which means it's unsuitable for querying\nSRV records compatible with the DNS-SD specification.\n\n**Access functions:**\n\n| QString | **name**() const |\n| --- | --- |\n| void | **setName**(const QString \\&*name*) |\n\n**Notifier signal:**\n\n| void | **[nameChanged](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#nameChanged)**(const QString \\&*name*) |\n| --- | --- |\n\nSource: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#name"
    nameserver: QHostAddress
    'Qt 5 reference:\n\n### nameserver : [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html)\n\nThis property holds the nameserver to use for DNS lookup.\n\n**Access functions:**\n\n| QHostAddress | **nameserver**() const |\n| --- | --- |\n| void | **setNameserver**(const QHostAddress \\&*nameserver*) |\n\n**Notifier signal:**\n\n| void | **nameserverChanged**(const QHostAddress \\&*nameserver*) |\n| --- | --- |\n\nSource: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#nameserver'
    objectName: Any
    type: Any
    'Qt 5 reference:\n\n### type : [Type](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#Type-enum)\n\nThis property holds the type of DNS lookup.\n\n**Access functions:**\n\n| QDnsLookup::Type | **type**() const |\n| --- | --- |\n| void | **setType**(*QDnsLookup::Type*) |\n\n**Notifier signal:**\n\n| void | **[typeChanged](https://doc.qt.io/archives/qt-5.15/qdnslookup.html#typeChanged)**(QDnsLookup::Type *type*) |\n| --- | --- |\n\nSource: https://doc.qt.io/archives/qt-5.15/qdnslookup.html#type'

class QDnsMailExchangeRecord:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

When performing a lookup on a service, zero or more records will be returned. Each
record is represented by a QDnsMailExchangeRecord instance.

The meaning of the fields is defined in [RFC
1035](http://www.rfc-editor.org/rfc/rfc1035.txt).

Source: https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def exchange(self) -> str:
        """X.exchange() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsMailExchangeRecord::exchange() const

Returns the domain name of the mail exchange for this record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
exchange(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html#exchange"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsMailExchangeRecord::name() const

Returns the name for this record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html#name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QDnsMailExchangeRecord"""
        ...

    def preference(self) -> int:
        """X.preference() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QDnsMailExchangeRecord::preference() const

Returns the preference for this record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
preference(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html#preference"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QDnsMailExchangeRecord::swap([QDnsMailExchangeRecord](https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html#QDnsMailExchangeRecord) \\&*other*)

Swaps this mail exchange record with *other*. This function is very fast and never
fails.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QDnsMailExchangeRecord) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html#swap"""
        ...

    def timeToLive(self) -> int:
        """X.timeToLive() -> int

Supplemental documentation:
Qt 5 reference:

### [quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) QDnsMailExchangeRecord::timeToLive() const

Returns the duration in seconds for which this record is valid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
timeToLive(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsmailexchangerecord.html#timeToLive"""
        ...

class QDnsServiceRecord:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

When performing a lookup on a service, zero or more records will be returned. Each
record is represented by a QDnsServiceRecord instance.

The meaning of the fields is defined in [RFC
2782](http://www.rfc-editor.org/rfc/rfc2782.txt).

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html"""

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

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsServiceRecord::name() const

Returns the name for this record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QDnsServiceRecord"""
        ...

    def port(self) -> int:
        """X.port() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QDnsServiceRecord::port() const

Returns the port on the target host for this service record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
port(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#port"""
        ...

    def priority(self) -> int:
        """X.priority() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QDnsServiceRecord::priority() const

Returns the priority for this service record.

A client must attempt to contact the target host with the lowest-numbered priority.

Upstream PySide2 reference signatures (binding differences may apply):

```python
priority(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#priority"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QDnsServiceRecord::swap([QDnsServiceRecord](https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#QDnsServiceRecord) \\&*other*)

Swaps this service record instance with *other*. This function is very fast and never
fails.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QDnsServiceRecord) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#swap"""
        ...

    def target(self) -> str:
        """X.target() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsServiceRecord::target() const

Returns the domain name of the target host for this service record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
target(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#target"""
        ...

    def timeToLive(self) -> int:
        """X.timeToLive() -> int

Supplemental documentation:
Qt 5 reference:

### [quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) QDnsServiceRecord::timeToLive() const

Returns the duration in seconds for which this record is valid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
timeToLive(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#timeToLive"""
        ...

    def weight(self) -> int:
        """X.weight() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QDnsServiceRecord::weight() const

Returns the weight for this service record.

The weight field specifies a relative weight for entries with the same priority. Entries
with higher weights should be selected with a higher probability.

Upstream PySide2 reference signatures (binding differences may apply):

```python
weight(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnsservicerecord.html#weight"""
        ...

class QDnsTextRecord:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

When performing a text lookup, zero or more records will be returned. Each record is
represented by a QDnsTextRecord instance.

The meaning of the fields is defined in [RFC
1035](http://www.rfc-editor.org/rfc/rfc1035.txt).

Source: https://doc.qt.io/archives/qt-5.15/qdnstextrecord.html"""

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

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QDnsTextRecord::name() const

Returns the name for this text record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qdnstextrecord.html#name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QDnsTextRecord"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QDnsTextRecord::swap([QDnsTextRecord](https://doc.qt.io/archives/qt-5.15/qdnstextrecord.html#QDnsTextRecord) \\&*other*)

Swaps this text record instance with *other*. This function is very fast and never
fails.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QDnsTextRecord) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qdnstextrecord.html#swap"""
        ...

    def timeToLive(self) -> int:
        """X.timeToLive() -> int

Supplemental documentation:
Qt 5 reference:

### [quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) QDnsTextRecord::timeToLive() const

Returns the duration in seconds for which this record is valid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
timeToLive(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qdnstextrecord.html#timeToLive"""
        ...

    def values(self) -> Any:
        """X.values()

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> QDnsTextRecord::values() const

Returns the values for this text record.

Upstream PySide2 reference signatures (binding differences may apply):

```python
values(self) -> typing.List[PySide2.QtCore.QByteArray]
```

Source: https://doc.qt.io/archives/qt-5.15/qdnstextrecord.html#values"""
        ...

class QHostAddress:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

This class holds an IPv4 or IPv6 address in a platform- and protocol-independent manner.

QHostAddress is normally used with the
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html),
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html), and
[QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html) to connect to a host or
to set up a server.

A host address is set with
[setAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#setAddress)(), and
retrieved with
[toIPv4Address](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toIPv4Address)(),
[toIPv6Address](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toIPv6Address)(),
or [toString](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toString)(). You can
check the type with
[protocol](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#protocol)().

**Note:** Please note that QHostAddress does not do DNS lookups.
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) is needed for that.

The class also supports common predefined addresses:
[Null](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum),
[LocalHost](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum),
[LocalHostIPv6](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum),
[Broadcast](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum),
and [Any](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum).

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def clear(self) -> None:
        """X.clear()

Supplemental documentation:
Qt 5 reference:

### void QHostAddress::clear()

Sets the host address to null and sets the protocol to
[QAbstractSocket::UnknownNetworkLayerProtocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum).

**See also**
[QHostAddress::Null](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
clear(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#clear"""
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

    def isInSubnet(self, subnet: Any, netmask: Any) -> bool:
        """X.isInSubnet(subnet, netmask) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QHostAddress::isInSubnet(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#QHostAddress) \\&*subnet*, int *netmask*) const

Returns `true` if this IP is in the subnet described by the network prefix *subnet* and
netmask *netmask*.

An IP is considered to belong to a subnet if it is contained between the lowest and the
highest address in that subnet. In the case of IP version 4, the lowest address is the
network address, while the highest address is the broadcast address.

The *subnet* argument does not have to be the actual network address (the lowest address
in the subnet). It can be any valid IP belonging to that subnet. In particular, if it is
equal to the IP address held by this object, this function will always return true
(provided the netmask is a valid value).

This function was introduced in Qt 4.5.

**See also**
[parseSubnet](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#parseSubnet)().

### bool QHostAddress::isInSubnet(const [QPair](https://doc.qt.io/archives/qt-5.15/qpair.html)\\<[QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#QHostAddress), int\\> \\&*subnet*) const

This is an overloaded function.

Returns `true` if this IP is in the subnet described by *subnet*. The
[QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) member of *subnet*
contains the network prefix and the int (second) member contains the netmask (prefix
length).

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isInSubnet(self, subnet: PySide2.QtNetwork.QHostAddress, netmask: int) -> bool
isInSubnet(self, subnet: typing.Tuple[PySide2.QtNetwork.QHostAddress, int]) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isInSubnet"""
        ...

    def isLoopback(self) -> bool:
        """X.isLoopback() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QHostAddress::isLoopback() const

returns `true` if the address is the IPv6 loopback address, or any of the IPv4 loopback
addresses.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isLoopback(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isLoopback"""
        ...

    def isMulticast(self) -> bool:
        """X.isMulticast() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QHostAddress::isMulticast() const

Returns `true` if the address is an IPv4 or IPv6 multicast address, `false` otherwise.

This function was introduced in Qt 5.6.

**See also**
[isLoopback](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isLoopback)(),
[isGlobal](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isGlobal)(),
[isLinkLocal](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isLinkLocal)(),
[isSiteLocal](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isSiteLocal)(), and
[isUniqueLocalUnicast](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isUniqueLocalUnicast)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isMulticast(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isMulticast"""
        ...

    def isNull(self) -> bool:
        """X.isNull() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QHostAddress::isNull() const

Returns `true` if this host address is not valid for any host or interface.

The default constructor creates a null address.

**See also**
[QHostAddress::Null](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isNull"""
        ...

    def parseSubnet(self, subnet: str) -> Any:
        """X.parseSubnet(subnet)

Supplemental documentation:
Qt 5 reference:

### `[static]` [QPair](https://doc.qt.io/archives/qt-5.15/qpair.html)\\<[QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#QHostAddress), int\\> QHostAddress::parseSubnet(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*subnet*)

Parses the IP and subnet information contained in *subnet* and returns the network
prefix for that network and its prefix length.

The IP address and the netmask must be separated by a slash (/).

This function supports arguments in the form:

- 123.123.123.123/n where n is any value between 0 and 32
- 123.123.123.123/255.255.255.255
- \\<ipv6-address\\>/n where n is any value between 0 and 128

For IP version 4, this function accepts as well missing trailing components (i.e., less
than 4 octets, like "192.168.1"), followed or not by a dot. If the netmask is also
missing in that case, it is set to the number of octets actually passed (in the example
above, it would be 24, for 3 octets).

This function was introduced in Qt 4.5.

**See also**
[isInSubnet](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#isInSubnet)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
parseSubnet(subnet: str) -> typing.Tuple[PySide2.QtNetwork.QHostAddress, int]
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#parseSubnet"""
        ...

    def protocol(self) -> Any:
        """X.protocol()

Supplemental documentation:
Qt 5 reference:

### [QAbstractSocket::NetworkLayerProtocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum) QHostAddress::protocol() const

Returns the network layer protocol of the host address.

Upstream PySide2 reference signatures (binding differences may apply):

```python
protocol(self) -> PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#protocol"""
        ...

    def readFrom(self, arg__1: Any) -> Any:
        """X.readFrom(arg__1)"""
        ...

    def scopeId(self) -> str:
        """X.scopeId() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QHostAddress::scopeId() const

Returns the scope ID of an IPv6 address. For IPv4 addresses, or if the address does not
contain a scope ID, an empty [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)
is returned.

The IPv6 scope ID specifies the scope of *reachability* for non-global IPv6 addresses,
limiting the area in which the address can be used. All IPv6 addresses are associated
with such a reachability scope. The scope ID is used to disambiguate addresses that are
not guaranteed to be globally unique.

IPv6 specifies the following four levels of reachability:

- Node-local: Addresses that are only used for communicating with services on the same interface (e.g., the loopback interface "::1").
- Link-local: Addresses that are local to the network interface (*link*). There is always one link-local address for each IPv6 interface on your host. Link-local addresses ("fe80...") are generated from the MAC address of the local network adaptor, and are not guaranteed to be unique.
- Global: For globally routable addresses, such as public servers on the Internet.

When using a link-local or site-local address for IPv6 connections, you must specify the
scope ID. The scope ID for a link-local address is usually the same as the interface
name (e.g., "eth0", "en1") or number (e.g., "1", "2").

This function was introduced in Qt 4.1.

**See also**
[setScopeId](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#setScopeId)(),
[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html), and
[QNetworkInterface::interfaceFromName](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#interfaceFromName).

Upstream PySide2 reference signatures (binding differences may apply):

```python
scopeId(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#scopeId"""
        ...

    def setAddress(self, ip6Addr: Any) -> Any:
        """X.setAddress(ip6Addr)

Supplemental documentation:
Qt 5 reference:

### void QHostAddress::setAddress([quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) *ip4Addr*)

Set the IPv4 address specified by *ip4Addr*.

### void QHostAddress::setAddress([quint8](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint8-typedef) \\**ip6Addr*)

This is an overloaded function.

Set the IPv6 address specified by *ip6Addr*.

*ip6Addr* must be an array of 16 bytes in network byte order (high-order byte first).

### void QHostAddress::setAddress(const [quint8](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint8-typedef) \\**ip6Addr*)

This is an overloaded function.

Set the IPv6 address specified by *ip6Addr*.

*ip6Addr* must be an array of 16 bytes in network byte order (high-order byte first).

This function was introduced in Qt 5.5.

### void QHostAddress::setAddress(const Q\\_IPV6ADDR \\&*ip6Addr*)

This is an overloaded function.

Set the IPv6 address specified by *ip6Addr*.

### void QHostAddress::setAddress(const sockaddr \\**sockaddr*)

This is an overloaded function.

Sets the IPv4 or IPv6 address specified by the native structure *sockaddr*. Returns
`true` and sets the address if the address was successfully parsed; otherwise returns
`false`.

### bool QHostAddress::setAddress(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*address*)

This is an overloaded function.

Sets the IPv4 or IPv6 address specified by the string representation specified by
*address* (e.g. "127.0.0.1"). Returns `true` and sets the address if the address was
successfully parsed; otherwise returns `false`.

### void QHostAddress::setAddress([QHostAddress::SpecialAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum) *address*)

This is an overloaded function.

Sets the special address specified by *address*.

This function was introduced in Qt 5.8.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAddress(self, address: PySide2.QtNetwork.QHostAddress.SpecialAddress) -> None
setAddress(self, address: str) -> bool
setAddress(self, ip4Addr: int) -> None
setAddress(self, ip6Addr: PySide2.QtNetwork.QIPv6Address) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#setAddress"""
        ...

    def setScopeId(self, id: str) -> None:
        """X.setScopeId(id)

Supplemental documentation:
Qt 5 reference:

### void QHostAddress::setScopeId(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*id*)

Sets the IPv6 scope ID of the address to *id*. If the address protocol is not IPv6, this
function does nothing. The scope ID may be set as an interface name (such as "eth0" or
"en1") or as an integer representing the interface index. If *id* is an interface name,
[QtNetwork](https://doc.qt.io/archives/qt-5.15/qtnetwork-module.html) will convert to an
interface index using
[QNetworkInterface::interfaceIndexFromName](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#interfaceIndexFromName)()
before calling the operating system networking functions.

This function was introduced in Qt 4.1.

**See also** [scopeId](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#scopeId)(),
[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html), and
[QNetworkInterface::interfaceFromName](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#interfaceFromName).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setScopeId(self, id: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#setScopeId"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QHostAddress::swap([QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#QHostAddress) \\&*other*)

Swaps this host address with *other*. This operation is very fast and never fails.

This function was introduced in Qt 5.6.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QHostAddress) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#swap"""
        ...

    def toIPv4Address(self, ok: Any) -> int:
        """X.toIPv4Address(ok) -> int

Supplemental documentation:
Qt 5 reference:

### [quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) QHostAddress::toIPv4Address() const

Returns the IPv4 address as a number.

For example, if the address is 127.0.0.1, the returned value is 2130706433 (i.e.
0x7f000001).

This value is valid if the
[protocol](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#protocol)() is
[IPv4Protocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum),
or if the protocol is
[IPv6Protocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum),
and the IPv6 address is an IPv4 mapped address. (RFC4291)

**See also**
[toString](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toString)().

### [quint32](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint32-typedef) QHostAddress::toIPv4Address(bool \\**ok*) const

Returns the IPv4 address as a number.

For example, if the address is 127.0.0.1, the returned value is 2130706433 (i.e.
0x7f000001).

This value is valid if the
[protocol](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#protocol)() is
[IPv4Protocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum),
or if the protocol is
[IPv6Protocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum),
and the IPv6 address is an IPv4 mapped address. (RFC4291). In those cases, *ok* will be
set to true. Otherwise, it will be set to false.

**See also**
[toString](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
toIPv4Address(self) -> int
toIPv4Address(self) -> typing.Tuple[int, bool]
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toIPv4Address"""
        ...

    def toIPv6Address(self) -> Any:
        """X.toIPv6Address() -> PythonQt.QtNetwork.QIPv6Address

Supplemental documentation:
Qt 5 reference:

### Q\\_IPV6ADDR QHostAddress::toIPv6Address() const

Returns the IPv6 address as a Q\\_IPV6ADDR structure. The structure consists of 16
unsigned characters.

```
Q_IPV6ADDR addr = hostAddr.toIPv6Address();
// addr contains 16 unsigned characters

for (int i = 0; i < 16; ++i) {
    // process addr[i]
}
```

This value is valid if the
[protocol](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#protocol)() is
[IPv6Protocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum).
If the protocol is
[IPv4Protocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum),
then the address is returned an an IPv4 mapped IPv6 address. (RFC4291)

**See also**
[toString](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
toIPv6Address(self) -> PySide2.QtNetwork.QIPv6Address
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toIPv6Address"""
        ...

    def toString(self) -> str:
        """X.toString() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QHostAddress::toString() const

Returns the address as a string.

For example, if the address is the IPv4 address 127.0.0.1, the returned string is
"127.0.0.1". For IPv6 the string format will follow the RFC5952 recommendation. For
[QHostAddress::Any](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum),
its IPv4 address will be returned ("0.0.0.0")

**See also**
[toIPv4Address](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toIPv4Address)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
toString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qhostaddress.html#toString"""
        ...

    def writeTo(self, arg__1: Any) -> Any:
        """X.writeTo(arg__1)"""
        ...
    Any: Any
    AnyIPv4: Any
    AnyIPv6: Any
    Broadcast: Any
    LocalHost: Any
    LocalHostIPv6: Any
    Null: Any
    SpecialAddress: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"

class QHostInfo:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QHostInfo finds the IP address(es) associated with a host name, or the host name
associated with an IP address. The class provides two static convenience functions: one
that works asynchronously and emits a signal once the host is found, and one that blocks
and returns a QHostInfo object.

To look up a host's IP addresses asynchronously, call
[lookupHost](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupHost)(), which
takes the host name or IP address, a receiver object, and a slot signature as arguments
and returns an ID. You can abort the lookup by calling
[abortHostLookup](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#abortHostLookup)()
with the lookup ID.

Example:

```
// To find the IP address of qt-project.org
QHostInfo::lookupHost("qt-project.org",
                      this, SLOT(printResults(QHostInfo)));

// To find the host name for 4.2.2.1
QHostInfo::lookupHost("4.2.2.1",
                      this, SLOT(printResults(QHostInfo)));
```

The slot is invoked when the results are ready. The results are stored in a QHostInfo
object. Call [addresses](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#addresses)()
to get the list of IP addresses for the host, and
[hostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName)() to get the host
name that was looked up.

If the lookup failed, [error](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error)()
returns the type of error that occurred.
[errorString](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#errorString)() gives a
human-readable description of the lookup error.

If you want a blocking lookup, use the
[QHostInfo::fromName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#fromName)()
function:

```
QHostInfo info = QHostInfo::fromName("qt-project.org");
```

QHostInfo supports Internationalized Domain Names (IDNs) through the IDNA and Punycode
standards.

To retrieve the name of the local host, use the static
[QHostInfo::localHostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#localHostName)()
function.

QHostInfo uses the mechanisms provided by the operating system to perform the lookup. As
per {https://tools.ietf.org/html/rfc6724}{RFC 6724} there is no guarantee that all IP
addresses registered for a domain or host will be returned.

**Note:** Since Qt 4.6.1 QHostInfo is using multiple threads for DNS lookup instead of
one dedicated DNS thread. This improves performance, but also changes the order of
signal emissions when using
[lookupHost](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupHost)() compared to
previous versions of Qt.

**Note:** Since Qt 4.6.3 QHostInfo is using a small internal 60 second DNS cache for
performance improvements.

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abortHostLookup(self, lookupId: int) -> None:
        """X.abortHostLookup(lookupId)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QHostInfo::abortHostLookup(int *id*)

Aborts the host lookup with the ID *id*, as returned by
[lookupHost](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupHost)().

**See also**
[lookupHost](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupHost)() and
[lookupId](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupId)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
abortHostLookup(lookupId: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#abortHostLookup"""
        ...

    def addresses(self) -> tuple:
        """X.addresses() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html)\\> QHostInfo::addresses() const

Returns the list of IP addresses associated with
[hostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName)(). This list may
be empty.

Example:

```
QHostInfo info;
...
if (!info.addresses().isEmpty()) {
    QHostAddress address = info.addresses().first();
    // use the first IP address
}
```

**See also**
[setAddresses](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setAddresses)(),
[hostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName)(), and
[error](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
addresses(self) -> typing.List[PySide2.QtNetwork.QHostAddress]
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#addresses"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def error(self) -> Any:
        """X.error()

Supplemental documentation:
Qt 5 reference:

### [QHostInfo::HostInfoError](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#HostInfoError-enum) QHostInfo::error() const

Returns the type of error that occurred if the host name lookup failed; otherwise
returns [NoError](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#HostInfoError-enum).

**See also** [setError](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setError)()
and [errorString](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
error(self) -> PySide2.QtNetwork.QHostInfo.HostInfoError
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error"""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QHostInfo::errorString() const

If the lookup failed, this function returns a human readable description of the error;
otherwise "Unknown error" is returned.

**See also**
[setErrorString](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setErrorString)() and
[error](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
errorString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#errorString"""
        ...

    def fromName(self, name: str) -> Any:
        """X.fromName(name) -> PythonQt.QtNetwork.QHostInfo

Supplemental documentation:
Qt 5 reference:

### `[static]` [QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#QHostInfo) QHostInfo::fromName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Looks up the IP address(es) for the given host *name*. The function blocks during the
lookup which means that execution of the program is suspended until the results of the
lookup are ready. Returns the result of the lookup in a
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) object.

If you pass a literal IP address to *name* instead of a host name,
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) will search for the
domain name for the IP (i.e.,
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) will perform a *reverse*
lookup). On success, the returned
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) will contain both the
resolved domain name and IP addresses for the host name.

**See also**
[lookupHost](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupHost)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
fromName(name: str) -> PySide2.QtNetwork.QHostInfo
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#fromName"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hostName(self) -> str:
        """X.hostName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QHostInfo::hostName() const

Returns the name of the host whose IP addresses were looked up.

**See also**
[setHostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setHostName)() and
[localHostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#localHostName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hostName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def localDomainName(self) -> str:
        """X.localDomainName() -> str

Supplemental documentation:
Qt 5 reference:

### `[static]` [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QHostInfo::localDomainName()

Returns the DNS domain of this machine.

**Note:** DNS domains are not related to domain names found in Windows networks.

**See also** [hostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localDomainName() -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#localDomainName"""
        ...

    def localHostName(self) -> str:
        """X.localHostName() -> str

Supplemental documentation:
Qt 5 reference:

### `[static]` [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QHostInfo::localHostName()

Returns this machine's host name, if one is configured. Note that hostnames are not
guaranteed to be globally unique, especially if they were configured automatically.

This function does not guarantee the returned host name is a Fully Qualified Domain Name
(FQDN). For that, use
[fromName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#fromName)() to resolve the
returned name to an FQDN.

This function returns the same as
[QSysInfo::machineHostName](https://doc.qt.io/archives/qt-5.15/qsysinfo.html#machineHostName)().

**See also** [hostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName)()
and
[localDomainName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#localDomainName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localHostName() -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#localHostName"""
        ...

    def lookupHost(self, name: Any, receiver: Any, member: Any) -> int:
        """X.lookupHost(name, receiver, member) -> int

Supplemental documentation:
Qt 5 reference:

### `[static]` int QHostInfo::lookupHost(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*, [QObject](https://doc.qt.io/archives/qt-5.15/qobject.html) \\**receiver*, const char \\**member*)

Looks up the IP address(es) associated with host name *name*, and returns an ID for the
lookup. When the result of the lookup is ready, the slot or signal *member* in
*receiver* is called with a
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) argument. The
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) object can then be
inspected to get the results of the lookup.

The lookup is performed by a single function call, for example:

```
QHostInfo::lookupHost("www.kde.org",
                      this, SLOT(lookedUp(QHostInfo)));
```

The implementation of the slot prints basic information about the addresses returned by
the lookup, or reports an error if it failed:

```
void MyWidget::lookedUp(const QHostInfo &host)
{
    if (host.error() != QHostInfo::NoError) {
        qDebug() << "Lookup failed:" << host.errorString();
        return;
    }

    const auto addresses = host.addresses();
    for (const QHostAddress &address : addresses)
        qDebug() << "Found address:" << address.toString();
}
```

If you pass a literal IP address to *name* instead of a host name,
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) will search for the
domain name for the IP (i.e.,
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) will perform a *reverse*
lookup). On success, the resulting
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) will contain both the
resolved domain name and IP addresses for the host name. Example:

```
QHostInfo::lookupHost("4.2.2.1",
                      this, SLOT(lookedUp(QHostInfo)));
```

**Note:** There is no guarantee on the order the signals will be emitted if you start
multiple requests with lookupHost().

**See also**
[abortHostLookup](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#abortHostLookup)(),
[addresses](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#addresses)(),
[error](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error)(), and
[fromName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#fromName)().

### `[static]` template \\<typename Functor\\> int QHostInfo::lookupHost(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*, Functor *functor*)

This is an overloaded function.

Looks up the IP address(es) associated with host name *name*, and returns an ID for the
lookup. When the result of the lookup is ready, the *functor* is called with a
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) argument. The
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) object can then be
inspected to get the results of the lookup.

The *functor* will be run in the thread that makes the call to lookupHost; that thread
must have a running Qt event loop.

**Note:** There is no guarantee on the order the signals will be emitted if you start
multiple requests with lookupHost().

This function was introduced in Qt 5.9.

**See also**
[abortHostLookup](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#abortHostLookup)(),
[addresses](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#addresses)(),
[error](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error)(), and
[fromName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#fromName)().

### `[static]` template \\<typename Functor\\> int QHostInfo::lookupHost(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*, const [QObject](https://doc.qt.io/archives/qt-5.15/qobject.html) \\**context*, Functor *functor*)

This is an overloaded function.

Looks up the IP address(es) associated with host name *name*, and returns an ID for the
lookup. When the result of the lookup is ready, the *functor* is called with a
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) argument. The
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) object can then be
inspected to get the results of the lookup.

If *context* is destroyed before the lookup completes, the *functor* will not be called.
The *functor* will be run in the thread of *context*. The context's thread must have a
running Qt event loop.

Here is an alternative signature for the function:

```
lookupHost(const QString &name, const QObject *receiver, PointerToMemberFunction function)
```

In this case, when the result of the lookup is ready, the slot or signal `function` in
`receiver` is called with a
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) argument. The
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) object can then be
inspected to get the results of the lookup.

**Note:** There is no guarantee on the order the signals will be emitted if you start
multiple requests with lookupHost().

This function was introduced in Qt 5.9.

**See also**
[abortHostLookup](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#abortHostLookup)(),
[addresses](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#addresses)(),
[error](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error)(), and
[fromName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#fromName)().

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupHost"""
        ...

    def lookupId(self) -> int:
        """X.lookupId() -> int

Supplemental documentation:
Qt 5 reference:

### int QHostInfo::lookupId() const

Returns the ID of this lookup.

**See also**
[setLookupId](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setLookupId)(),
[abortHostLookup](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#abortHostLookup)(),
and [hostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
lookupId(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupId"""
        ...

    def setAddresses(self, addresses: Any) -> None:
        """X.setAddresses(addresses)

Supplemental documentation:
Qt 5 reference:

### void QHostInfo::setAddresses(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html)\\> \\&*addresses*)

Sets the list of addresses in this
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) to *addresses*.

**See also** [addresses](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#addresses)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAddresses(self, addresses: typing.Sequence[PySide2.QtNetwork.QHostAddress]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setAddresses"""
        ...

    def setError(self, error: Any) -> None:
        """X.setError(error)

Supplemental documentation:
Qt 5 reference:

### void QHostInfo::setError([QHostInfo::HostInfoError](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#HostInfoError-enum) *error*)

Sets the error type of this
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) to *error*.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#error)() and
[errorString](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setError(self, error: PySide2.QtNetwork.QHostInfo.HostInfoError) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setError"""
        ...

    def setErrorString(self, errorString: str) -> None:
        """X.setErrorString(errorString)

Supplemental documentation:
Qt 5 reference:

### void QHostInfo::setErrorString(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*str*)

Sets the human readable description of the error that occurred to *str* if the lookup
failed.

**See also**
[errorString](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#errorString)() and
[setError](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setError)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setErrorString(self, errorString: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setErrorString"""
        ...

    def setHostName(self, name: str) -> None:
        """X.setHostName(name)

Supplemental documentation:
Qt 5 reference:

### void QHostInfo::setHostName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*)

Sets the host name of this
[QHostInfo](https://doc.qt.io/archives/qt-5.15/qhostinfo.html) to *hostName*.

**See also** [hostName](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#hostName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHostName(self, name: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setHostName"""
        ...

    def setLookupId(self, id: int) -> None:
        """X.setLookupId(id)

Supplemental documentation:
Qt 5 reference:

### void QHostInfo::setLookupId(int *id*)

Sets the ID of this lookup to *id*.

**See also** [lookupId](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupId)()
and [lookupHost](https://doc.qt.io/archives/qt-5.15/qhostinfo.html#lookupHost)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLookupId(self, id: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhostinfo.html#setLookupId"""
        ...
    HostInfoError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    HostNotFound: Any
    NoError: Any
    UnknownError: Any

class QHttpMultiPart:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QHttpMultiPart resembles a MIME multipart message, as described in RFC 2046, which
is to be sent over HTTP. A multipart message consists of an arbitrary number of body
parts (see [QHttpPart](https://doc.qt.io/archives/qt-5.15/qhttppart.html)), which are
separated by a unique boundary. The boundary of the QHttpMultiPart is constructed with
the string "boundary\\_.oOo.[\\_](https://doc.qt.io/archives/qt-5.15/qromancalendar.html)"
followed by random characters, and provides enough uniqueness to make sure it does not
occur inside the parts itself. If desired, the boundary can still be set via
[setBoundary](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#setBoundary)().

As an example, consider the following code snippet, which constructs a multipart message
containing a text part followed by an image part:

```
QHttpMultiPart *multiPart = new QHttpMultiPart(QHttpMultiPart::FormDataType);

QHttpPart textPart;
textPart.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\\"text\\""));
textPart.setBody("my text");

QHttpPart imagePart;
imagePart.setHeader(QNetworkRequest::ContentTypeHeader, QVariant("image/jpeg"));
imagePart.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\\"image\\""));
QFile *file = new QFile("image.jpg");
file->open(QIODevice::ReadOnly);
imagePart.setBodyDevice(file);
file->setParent(multiPart); // we cannot delete the file now, so delete it with the multiPart

multiPart->append(textPart);
multiPart->append(imagePart);

QUrl url("http://my.server.tld");
QNetworkRequest request(url);

QNetworkAccessManager manager;
QNetworkReply *reply = manager.post(request, multiPart);
multiPart->setParent(reply); // delete the multiPart with the reply
// here connect signals etc.
```

Source: https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def append(self, httpPart: Any) -> None:
        """X.append(httpPart)

Supplemental documentation:
Qt 5 reference:

### void QHttpMultiPart::append(const [QHttpPart](https://doc.qt.io/archives/qt-5.15/qhttppart.html) \\&*httpPart*)

Appends *httpPart* to this multipart.

Upstream PySide2 reference signatures (binding differences may apply):

```python
append(self, httpPart: PySide2.QtNetwork.QHttpPart) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#append"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def boundary(self) -> Any:
        """X.boundary() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QHttpMultiPart::boundary() const

returns the boundary.

**See also**
[setBoundary](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#setBoundary)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
boundary(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#boundary"""
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
        """Native PythonQt.QtNetwork.QHttpMultiPart.destroyed; argument details are not documented."""
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
        """Native PythonQt.QtNetwork.QHttpMultiPart.objectNameChanged; argument details are not documented."""
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

    def setBoundary(self, boundary: Any) -> None:
        """X.setBoundary(boundary)

Supplemental documentation:
Qt 5 reference:

### void QHttpMultiPart::setBoundary(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*boundary*)

Sets the boundary to *boundary*.

Usually, you do not need to generate a boundary yourself; upon construction the boundary
is initiated with the string
"boundary\\_.oOo.[\\_](https://doc.qt.io/archives/qt-5.15/qromancalendar.html)" followed
by random characters, and provides enough uniqueness to make sure it does not occur
inside the parts itself.

**See also**
[boundary](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#boundary)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setBoundary(self, boundary: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#setBoundary"""
        ...

    def setContentType(self, contentType: Any) -> None:
        """X.setContentType(contentType)

Supplemental documentation:
Qt 5 reference:

### void QHttpMultiPart::setContentType([QHttpMultiPart::ContentType](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#ContentType-enum) *contentType*)

Sets the content type to *contentType*. The content type will be used in the HTTP header
section when sending the multipart message via
[QNetworkAccessManager::post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)().
In case you want to use a multipart subtype not contained in
[QHttpMultiPart::ContentType](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#ContentType-enum),
you can add the "Content-Type" header field to the
[QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) by hand, and
then use this request together with the multipart message for posting.

**See also**
[QHttpMultiPart::ContentType](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#ContentType-enum)
and
[QNetworkAccessManager::post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setContentType(self, contentType: PySide2.QtNetwork.QHttpMultiPart.ContentType) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html#setContentType"""
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
    AlternativeType: Any
    ContentType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    FormDataType: Any
    MixedType: Any
    RelatedType: Any
    objectName: Any

class QHttpPart:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QHttpPart class holds a body part to be used inside a HTTP multipart MIME message
(which is represented by the
[QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html) class). A
QHttpPart consists of a header block and a data block, which are separated by each other
by two consecutive new lines. An example for one part would be:

```
Content-Type: text/plain
Content-Disposition: form-data; name="text"

here goes the body
```

For setting headers, use
[setHeader](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setHeader)() and
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setRawHeader)(), which
behave exactly like
[QNetworkRequest::setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setHeader)()
and
[QNetworkRequest::setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader)().

For reading small pieces of data, use
[setBody](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBody)(); for larger data
blocks like e.g. images, use
[setBodyDevice](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBodyDevice)(). The
latter method saves memory by not copying the data internally, but reading directly from
the device. This means that the device must be opened and readable at the moment when
the multipart message containing the body part is sent on the network via
[QNetworkAccessManager::post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)().

To construct a QHttpPart with a small body, consider the following snippet (this
produces the data shown in the example above):

```
QHttpPart textPart;
textPart.setHeader(QNetworkRequest::ContentTypeHeader, QVariant("text/plain"));
textPart.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\\"text\\""));
textPart.setBody("here goes the body");
```

To construct a QHttpPart reading from a device (e.g. a file), the following can be
applied:

```
QHttpPart imagePart;
imagePart.setHeader(QNetworkRequest::ContentTypeHeader, QVariant("image/jpeg"));
imagePart.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\\"image\\""));
imagePart.setRawHeader("Content-ID", "my@content.id"); // add any headers you like via setRawHeader()
QFile *file = new QFile("image.jpg");
file->open(QIODevice::ReadOnly);
imagePart.setBodyDevice(file);
```

Be aware that QHttpPart does not take ownership of the device when set, so it is the
developer's responsibility to destroy it when it is not needed anymore. A good idea
might be to set the multipart message as parent object for the device, as documented at
the documentation for
[QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html).

Source: https://doc.qt.io/archives/qt-5.15/qhttppart.html"""

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

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QHttpPart"""
        ...

    def setBody(self, body: Any) -> None:
        """X.setBody(body)

Supplemental documentation:
Qt 5 reference:

### void QHttpPart::setBody(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*body*)

Sets the body of this MIME part to *body*. The body set with this method will be used
unless the device is set via
[setBodyDevice](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBodyDevice)(). For
a large amount of data (e.g. an image), use
[setBodyDevice](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBodyDevice)(),
which will not copy the data internally.

**See also**
[setBodyDevice](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBodyDevice)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setBody(self, body: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBody"""
        ...

    def setBodyDevice(self, device: Any) -> None:
        """X.setBodyDevice(device)

Supplemental documentation:
Qt 5 reference:

### void QHttpPart::setBodyDevice([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*)

Sets the device to read the content from to *device*. For large amounts of data this
method should be preferred over
[setBody](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBody)(), because the
content is not copied when using this method, but read directly from the device.
*device* must be open and readable.
[QHttpPart](https://doc.qt.io/archives/qt-5.15/qhttppart.html) does not take ownership
of *device*, i.e. the device must be closed and destroyed if necessary. if *device* is
sequential (e.g. sockets, but not files),
[QNetworkAccessManager::post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)()
should be called after *device* has emitted finished(). For unsetting the device and
using data set via
[setBody](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBody)(), use
"setBodyDevice(0)".

**See also** [setBody](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBody)() and
[QNetworkAccessManager::post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setBodyDevice(self, device: PySide2.QtCore.QIODevice) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttppart.html#setBodyDevice"""
        ...

    def setHeader(self, header: Any, value: Any) -> None:
        """X.setHeader(header, value)

Supplemental documentation:
Qt 5 reference:

### void QHttpPart::setHeader([QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum) *header*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the value of the known header *header* to be *value*, overriding any previously set
headers.

**See also**
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setRawHeader)(), and
[QNetworkRequest::setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHeader(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttppart.html#setHeader"""
        ...

    def setRawHeader(self, headerName: Any, headerValue: Any) -> None:
        """X.setRawHeader(headerName, headerValue)

Supplemental documentation:
Qt 5 reference:

### void QHttpPart::setRawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerValue*)

Sets the header *headerName* to be of value *headerValue*. If *headerName* corresponds
to a known header (see
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum)),
the raw format will be parsed and the corresponding "cooked" header will be set as well.

**Note:** Setting the same header twice overrides the previous setting. To accomplish
the behaviour of multiple HTTP headers of the same name, you should concatenate the two
values, separating them with a comma (",") and set one single raw header.

**See also**
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[setHeader](https://doc.qt.io/archives/qt-5.15/qhttppart.html#setHeader)(), and
[QNetworkRequest::setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRawHeader(self, headerName: PySide2.QtCore.QByteArray, headerValue: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttppart.html#setRawHeader"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QHttpPart::swap([QHttpPart](https://doc.qt.io/archives/qt-5.15/qhttppart.html#QHttpPart) \\&*other*)

Swaps this HTTP part with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QHttpPart) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qhttppart.html#swap"""
        ...

class QIPv6Address:
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

class QLocalServer:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

This class makes it possible to accept incoming local socket connections.

Call [listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)() to have the
server start listening for incoming connections on a specified key. The
[newConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#newConnection)()
signal is then emitted each time a client connects to the server.

Call
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#nextPendingConnection)()
to accept the pending connection as a connected
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html). The function
returns a pointer to a
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) that can be used
for communicating with the client.

If an error occurs,
[serverError](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverError)()
returns the type of error, and
[errorString](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#errorString)() can be
called to get a human readable description of what happened.

When listening for connections, the name which the server is listening on is available
through [serverName](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverName)().

Calling [close](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#close)() makes
QLocalServer stop listening for incoming connections.

Although QLocalServer is designed for use with an event loop, it's possible to use it
without one. In that case, you must use
[waitForNewConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#waitForNewConnection)(),
which blocks until either a connection is available or a timeout expires.

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html"""

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

    def close(self) -> None:
        """X.close()

Supplemental documentation:
Qt 5 reference:

### void QLocalServer::close()

Stop listening for incoming connections. Existing connections are not affected, but any
new connections will be refused.

**See also**
[isListening](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#isListening)() and
[listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
close(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#close"""
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
        """Native PythonQt.QtNetwork.QLocalServer.destroyed; argument details are not documented."""
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

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QLocalServer::errorString() const

Returns the human-readable message appropriate to the current error reported by
[serverError](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverError)(). If no
suitable string is available, an empty string is returned.

**See also**
[serverError](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverError)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
errorString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#errorString"""
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

    def fullServerName(self) -> str:
        """X.fullServerName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QLocalServer::fullServerName() const

Returns the full path that the server is listening on.

Note: This is platform specific

**See also** [listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)() and
[serverName](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
fullServerName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#fullServerName"""
        ...

    def hasPendingConnections(self) -> bool:
        """X.hasPendingConnections() -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QLocalServer::hasPendingConnections() const

Returns `true` if the server has a pending connection; otherwise returns `false`.

**See also**
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#nextPendingConnection)()
and
[setMaxPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#setMaxPendingConnections)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasPendingConnections(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#hasPendingConnections"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def incomingConnection(self, socketDescriptor: int) -> None:
        """X.incomingConnection(socketDescriptor)

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QLocalServer::incomingConnection([quintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quintptr-typedef) *socketDescriptor*)

This virtual function is called by
[QLocalServer](https://doc.qt.io/archives/qt-5.15/qlocalserver.html) when a new
connection is available. *socketDescriptor* is the native socket descriptor for the
accepted connection.

The base implementation creates a
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html), sets the socket
descriptor and then stores the
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) in an internal list
of pending connections. Finally
[newConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#newConnection)() is
emitted.

Reimplement this function to alter the server's behavior when a connection is available.

**See also**
[newConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#newConnection)(),
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#nextPendingConnection)(),
and
[QLocalSocket::setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setSocketDescriptor)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
incomingConnection(self, socketDescriptor: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#incomingConnection"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isListening(self) -> bool:
        """X.isListening() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalServer::isListening() const

Returns `true` if the server is listening for incoming connections otherwise false.

**See also** [listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)() and
[close](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isListening(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#isListening"""
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

    def listen(self, name: Any) -> bool:
        """X.listen(name) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalServer::listen(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Tells the server to listen for incoming connections on *name*. If the server is
currently listening then it will return false. Return true on success otherwise false.

*name* can be a single name and
[QLocalServer](https://doc.qt.io/archives/qt-5.15/qlocalserver.html) will determine the
correct platform specific path.
[serverName](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverName)() will
return the name that is passed into listen.

Usually you would just pass in a name like "foo", but on Unix this could also be a path
such as "/temporary/foo" and on Windows this could be a pipe path such as
"\\\\\\\\.\\\\pipe\\\\foo"

**Note:** On Unix if the server crashes without closing listen will fail with
AddressInUseError. To create a new server the file should be removed. On Windows two
local servers can listen to the same pipe at the same time, but any connections will go
to one of the server.

**See also**
[serverName](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverName)(),
[isListening](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#isListening)(), and
[close](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#close)().

### bool QLocalServer::listen([qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) *socketDescriptor*)

Instructs the server to listen for incoming connections on *socketDescriptor*. The
property returns `false` if the server is currently listening. It returns `true` on
success; otherwise, it returns `false`. The socket must be ready to accept new
connections with no extra platform-specific functions called. The socket is set into
non-blocking mode.

[serverName](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverName)(),
[fullServerName](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#fullServerName)()
may return a string with a name if this option is supported by the platform; otherwise,
they return an empty [QString](https://doc.qt.io/archives/qt-5.15/qstring.html).

This function was introduced in Qt 5.0.

**See also**
[isListening](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#isListening)() and
[close](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
listen(self, name: str) -> bool
listen(self, socketDescriptor: int) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen"""
        ...

    def maxPendingConnections(self) -> int:
        """X.maxPendingConnections() -> int

Supplemental documentation:
Qt 5 reference:

### int QLocalServer::maxPendingConnections() const

Returns the maximum number of pending accepted connections. The default is 30\\.

**See also**
[setMaxPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#setMaxPendingConnections)()
and
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#hasPendingConnections)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
maxPendingConnections(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#maxPendingConnections"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def newConnection(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalServer.newConnection; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QLocalServer::newConnection()

This signal is emitted every time a new connection is available.

**See also**
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#hasPendingConnections)()
and
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#nextPendingConnection)().

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#newConnection"""
        ...

    def nextPendingConnection(self) -> Any:
        """X.nextPendingConnection() -> PythonQt.QtNetwork.QLocalSocket

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) \\*QLocalServer::nextPendingConnection()

Returns the next pending connection as a connected
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) object.

The socket is created as a child of the server, which means that it is automatically
deleted when the [QLocalServer](https://doc.qt.io/archives/qt-5.15/qlocalserver.html)
object is destroyed. It is still a good idea to delete the object explicitly when you
are done with it, to avoid wasting memory.

`nullptr` is returned if this function is called when there are no pending connections.

**See also**
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#hasPendingConnections)(),
[newConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#newConnection)(),
and
[incomingConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#incomingConnection)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
nextPendingConnection(self) -> PySide2.QtNetwork.QLocalSocket
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#nextPendingConnection"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalServer.objectNameChanged; argument details are not documented."""
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

    def removeServer(self, name: str) -> bool:
        """X.removeServer(name) -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QLocalServer::removeServer(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Removes any server instance that might cause a call to
[listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)() to fail and
returns `true` if successful; otherwise returns `false`. This function is meant to
recover from a crash, when the previous server instance has not been cleaned up.

On Windows, this function does nothing; on Unix, it removes the socket file given by
*name*.

**Warning:** Be careful to avoid removing sockets of running instances.

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
removeServer(name: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#removeServer"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def serverError(self) -> Any:
        """X.serverError()

Supplemental documentation:
Qt 5 reference:

### [QAbstractSocket::SocketError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum) QLocalServer::serverError() const

Returns the type of error that occurred last or
[NoError](https://doc.qt.io/archives/qt-5.15/qdtls.html#QDtlsError-enum).

**See also**
[errorString](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
serverError(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverError"""
        ...

    def serverName(self) -> str:
        """X.serverName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QLocalServer::serverName() const

Returns the server name if the server is listening for connections; otherwise returns
QString()

**See also** [listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)() and
[fullServerName](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#fullServerName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
serverName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#serverName"""
        ...

    def setMaxPendingConnections(self, numConnections: int) -> None:
        """X.setMaxPendingConnections(numConnections)

Supplemental documentation:
Qt 5 reference:

### void QLocalServer::setMaxPendingConnections(int *numConnections*)

Sets the maximum number of pending accepted connections to *numConnections*.
[QLocalServer](https://doc.qt.io/archives/qt-5.15/qlocalserver.html) will accept no more
than *numConnections* incoming connections before
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#nextPendingConnection)()
is called.

Note: Even though [QLocalServer](https://doc.qt.io/archives/qt-5.15/qlocalserver.html)
will stop accepting new connections after it has reached its maximum number of pending
connections, the operating system may still keep them in queue which will result in
clients signaling that it is connected.

**See also**
[maxPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#maxPendingConnections)()
and
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#hasPendingConnections)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMaxPendingConnections(self, numConnections: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#setMaxPendingConnections"""
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

    def setSocketOptions(self, options: Any) -> None:
        """X.setSocketOptions(options)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketOptions(self, options: PySide2.QtNetwork.QLocalServer.SocketOptions) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#setSocketOptions"""
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

    def waitForNewConnection(self, msec: int, timedOut: Any) -> bool:
        """X.waitForNewConnection(msec, timedOut) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalServer::waitForNewConnection(int *msec* \\= 0, bool \\**timedOut* \\= nullptr)

Waits for at most *msec* milliseconds or until an incoming connection is available.
Returns `true` if a connection is available; otherwise returns `false`. If the operation
timed out and *timedOut* is not `nullptr`, \\*timedOut will be set to true.

This is a blocking function call. Its use is ill-advised in a single-threaded GUI
application, since the whole application will stop responding until the function
returns. waitForNewConnection() is mostly useful when there is no event loop available.

The non-blocking alternative is to connect to the
[newConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#newConnection)()
signal.

If msec is -1, this function will not time out.

**See also**
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#hasPendingConnections)()
and
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#nextPendingConnection)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForNewConnection(self, msec: int) -> typing.Tuple[bool, bool]
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#waitForNewConnection"""
        ...
    GroupAccessOption: Any
    NoOptions: Any
    OtherAccessOption: Any
    SocketOption: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketOptions: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    UserAccessOption: Any
    WorldAccessOption: Any
    objectName: Any
    socketOptions: Any
    'Qt 5 reference:\n\n### socketOptions : [SocketOptions](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#SocketOption-enum)\n\nThe setSocketOptions method controls how the socket operates. For example the socket may\nrestrict access to what user ids can connect to the socket.\n\nThese options must be set before\n[listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)() is called.\n\nIn some cases, such as with Unix domain sockets on Linux, the access to the socket will\nbe determined by file system permissions, and are created based on the umask. Setting\nthe access flags will override this and will restrict or permit access as specified.\n\nOther Unix-based operating systems, such as macOS, do not honor file permissions for\nUnix domain sockets and by default have WorldAccess and these permission flags will have\nno effect.\n\nOn Windows,\n[UserAccessOption](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#SocketOption-enum)\nis sufficient to allow a non elevated process to connect to a local server created by an\nelevated process run by the same user.\n[GroupAccessOption](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#SocketOption-enum)\nrefers to the primary group of the process (see TokenPrimaryGroup in the Windows\ndocumentation).\n[OtherAccessOption](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#SocketOption-enum)\nrefers to the well known "Everyone" group.\n\nBy default none of the flags are set, access permissions are the platform default.\n\nThis property was introduced in Qt 5.0.\n\n**Access functions:**\n\n| QLocalServer::SocketOptions | **[socketOptions](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#socketOptions)**() const |\n| --- | --- |\n| void | **setSocketOptions**(QLocalServer::SocketOptions *options*) |\n\n**See also** [listen](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#listen)().\n\n### [QLocalServer::SocketOptions](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#SocketOption-enum) QLocalServer::socketOptions() const\n\nReturns the socket options set on the socket.\n\n**Note:** Getter function for property socketOptions.\n\nThis function was introduced in Qt 5.0.\n\n**See also**\n[setSocketOptions](https://doc.qt.io/archives/qt-5.15/qlocalserver.html#socketOptions-prop)().\n\nSource: https://doc.qt.io/archives/qt-5.15/qlocalserver.html#socketOptions'

class QLocalSocket:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

On Windows this is a named pipe and on Unix this is a local domain socket.

If an error occurs,
[error](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#error)() returns the type
of error, and
[errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)() can be
called to get a human readable description of what happened.

Although QLocalSocket is designed for use with an event loop, it's possible to use it
without one. In that case, you must use
[waitForConnected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForConnected)(),
[waitForReadyRead](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForReadyRead)(),
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForBytesWritten)(),
and
[waitForDisconnected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForDisconnected)()
which blocks until the operation is complete or the timeout expires.

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abort(self) -> None:
        """X.abort()

Supplemental documentation:
Qt 5 reference:

### void QLocalSocket::abort()

Aborts the current connection and resets the socket. Unlike
[disconnectFromServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#disconnectFromServer)(),
this function immediately closes the socket, clearing any pending data in the write
buffer.

**See also**
[disconnectFromServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#disconnectFromServer)()
and [close](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
abort(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#abort"""
        ...

    def aboutToClose(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.aboutToClose; argument details are not documented."""
        ...

    def atEnd(self) -> bool:
        """X.atEnd() -> bool"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def bytesAvailable(self) -> int:
        """X.bytesAvailable() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QLocalSocket::bytesAvailable() const

Reimplements:
[QIODevice::bytesAvailable](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesAvailable)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesAvailable(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#bytesAvailable"""
        ...

    def bytesToWrite(self) -> int:
        """X.bytesToWrite() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QLocalSocket::bytesToWrite() const

Reimplements:
[QIODevice::bytesToWrite](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesToWrite)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesToWrite(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#bytesToWrite"""
        ...

    def bytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.bytesWritten; argument details are not documented."""
        ...

    def canReadLine(self) -> bool:
        """X.canReadLine() -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QLocalSocket::canReadLine() const

Reimplements:
[QIODevice::canReadLine](https://doc.qt.io/archives/qt-5.15/qiodevice.html#canReadLine)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
canReadLine(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#canReadLine"""
        ...

    def channelBytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.channelBytesWritten; argument details are not documented."""
        ...

    def channelReadyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.channelReadyRead; argument details are not documented."""
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

    def close(self) -> None:
        """X.close()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QLocalSocket::close()

Reimplements:
[QIODevice::close](https://doc.qt.io/archives/qt-5.15/qiodevice.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
close(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#close"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def connectToServer(self, name: Any, openMode: Any) -> None:
        """X.connectToServer(name, openMode)

Supplemental documentation:
Qt 5 reference:

### void QLocalSocket::connectToServer([QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite)

Attempts to make a connection to
[serverName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#serverName)().
[setServerName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setServerName)()
must be called before you open the connection. Alternatively you can use
connectToServer(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&name,
[OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum)
[openMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#openMode));

The socket is opened in the given *openMode* and first enters
[ConnectingState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum).
If a connection is established,
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) enters
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum)
and emits [connected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connected)().

After calling this function, the socket can emit
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#errorOccurred)() to
signal that an error occurred.

This function was introduced in Qt 5.1.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#state)(),
[serverName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#serverName)(), and
[waitForConnected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForConnected)().

### void QLocalSocket::connectToServer(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite)

This is an overloaded function.

Set the server *name* and attempts to make a connection to it.

The socket is opened in the given *openMode* and first enters
[ConnectingState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum).
If a connection is established,
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) enters
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum)
and emits [connected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connected)().

After calling this function, the socket can emit
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#errorOccurred)() to
signal that an error occurred.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#state)(),
[serverName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#serverName)(), and
[waitForConnected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForConnected)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
connectToServer(self, name: str, openMode: PySide2.QtCore.QIODevice.OpenMode=...) -> None
connectToServer(self, openMode: PySide2.QtCore.QIODevice.OpenMode=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer"""
        ...

    def connected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.connected; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QLocalSocket::connected()

This signal is emitted after
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)()
has been called and a connection has been successfully established.

**See also**
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)()
and [disconnected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#disconnected)().

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connected"""
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
        """Native PythonQt.QtNetwork.QLocalSocket.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def disconnectFromServer(self) -> None:
        """X.disconnectFromServer()

Supplemental documentation:
Qt 5 reference:

### void QLocalSocket::disconnectFromServer()

Attempts to close the socket. If there is pending data waiting to be written,
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) will enter
[ClosingState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum)
and wait until all data has been written. Eventually, it will enter
[UnconnectedState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum)
and emit the disconnectedFromServer() signal.

**See also**
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
disconnectFromServer(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#disconnectFromServer"""
        ...

    def disconnected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.disconnected; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QLocalSocket::disconnected()

This signal is emitted when the socket has been disconnected.

**See also**
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)(),
[disconnectFromServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#disconnectFromServer)(),
[abort](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#abort)(), and
[connected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connected)().

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#disconnected"""
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

    def error(self) -> Any:
        """X.error()

Supplemental documentation:
Qt 5 reference:

### [QLocalSocket::LocalSocketError](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketError-enum) QLocalSocket::error() const

Returns the type of error that last occurred.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#state)() and
[errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
error(self) -> PySide2.QtNetwork.QLocalSocket.LocalSocketError
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#error"""
        ...

    def errorOccurred(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.errorOccurred; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QLocalSocket::errorOccurred([QLocalSocket::LocalSocketError](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketError-enum) *socketError*)

This signal is emitted after an error occurred. The *socketError* parameter describes
the type of error that occurred.

[QLocalSocket::LocalSocketError](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketError-enum)
is not a registered metatype, so for queued connections, you will have to register it
with
[Q\\_DECLARE\\_METATYPE](https://doc.qt.io/archives/qt-5.15/qmetatype.html#Q_DECLARE_METATYPE)()
and
[qRegisterMetaType](https://doc.qt.io/archives/qt-5.15/qmetatype.html#qRegisterMetaType-1)().

This function was introduced in Qt 5.15.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#error)(),
[errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)(), and
[Creating Custom Qt Types](https://doc.qt.io/archives/qt-5.15/custom-types.html).

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#errorOccurred"""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str"""
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

    def flush(self) -> bool:
        """X.flush() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalSocket::flush()

This function writes as much as possible from the internal write buffer to the socket,
without blocking. If any data was written, this function returns `true`; otherwise false
is returned.

Call this function if you need
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) to start sending
buffered data immediately. The number of bytes successfully written depends on the
operating system. In most cases, you do not need to call this function, because
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) will start sending
data automatically once control goes back to the event loop. In the absence of an event
loop, call
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForBytesWritten)()
instead.

**See also** [write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() and
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForBytesWritten)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
flush(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#flush"""
        ...

    def fullServerName(self) -> str:
        """X.fullServerName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QLocalSocket::fullServerName() const

Returns the server path that the socket is connected to.

**Note:** The return value of this function is platform specific.

**See also**
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)()
and [serverName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#serverName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
fullServerName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#fullServerName"""
        ...

    def getChar(self, c: Any) -> bool:
        """X.getChar(c) -> bool"""
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

    def isOpen(self) -> bool:
        """X.isOpen() -> bool"""
        ...

    def isReadable(self) -> bool:
        """X.isReadable() -> bool"""
        ...

    def isSequential(self) -> bool:
        """X.isSequential() -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QLocalSocket::isSequential() const

Reimplements:
[QIODevice::isSequential](https://doc.qt.io/archives/qt-5.15/qiodevice.html#isSequential)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSequential(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#isSequential"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isTextModeEnabled(self) -> bool:
        """X.isTextModeEnabled() -> bool"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalSocket::isValid() const

Returns `true` if the socket is valid and ready for use; otherwise returns `false`.

**Note:** The socket's state must be
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum)
before reading and writing can occur.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#state)() and
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#isValid"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def isWritable(self) -> bool:
        """X.isWritable() -> bool"""
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
        """Native PythonQt.QtNetwork.QLocalSocket.objectNameChanged; argument details are not documented."""
        ...

    def open(self, openMode: Any) -> bool:
        """X.open(openMode) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QLocalSocket::open([QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite)

Reimplements:
[QIODevice::open](https://doc.qt.io/archives/qt-5.15/qiodevice.html#open)(QIODevice::OpenMode
mode).

Equivalent to
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)([OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum)
mode). The socket is opened in the given *openMode* to the server defined by
[setServerName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setServerName)().

Note that unlike in most other
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) subclasses, open() may
not open the device directly. The function return false if the socket was already
connected or if the server to connect to was not defined and true in any other case. The
[connected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connected)() or
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#errorOccurred)()
signals will be emitted once the device is actually open (or the connection failed).

See
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)()
for more details.

Upstream PySide2 reference signatures (binding differences may apply):

```python
open(self, openMode: PySide2.QtCore.QIODevice.OpenMode=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#open"""
        ...

    def openMode(self) -> Any:
        """X.openMode()"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def peek(self, maxlen: Any) -> Any:
        """X.peek(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def pos(self) -> int:
        """X.pos() -> int"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def putChar(self, c: Any) -> bool:
        """X.putChar(c) -> bool"""
        ...

    def read(self, maxlen: Any) -> Any:
        """X.read(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readAll(self) -> Any:
        """X.readAll() -> PythonQt.QtCore.QByteArray"""
        ...

    def readBufferSize(self) -> int:
        """X.readBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QLocalSocket::readBufferSize() const

Returns the size of the internal read buffer. This limits the amount of data that the
client can receive before you call
[read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)() or
[readAll](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readAll)(). A read buffer
size of 0 (the default) means that the buffer has no size limit, ensuring that no data
is lost.

**See also**
[setReadBufferSize](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setReadBufferSize)()
and [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
readBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#readBufferSize"""
        ...

    def readChannelFinished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.readChannelFinished; argument details are not documented."""
        ...

    def readData(self, arg__1: str, arg__2: int) -> int:
        """X.readData(arg__1, arg__2) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QLocalSocket::readData(char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *c*)

Reimplements:
[QIODevice::readData](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readData)(char
\\*data, qint64 maxSize).

Upstream PySide2 reference signatures (binding differences may apply):

```python
readData(self, arg__1: str, arg__2: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#readData"""
        ...

    def readLine(self, maxlen: Any) -> Any:
        """X.readLine(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readLineData(self, data: Any, maxlen: Any) -> int:
        """X.readLineData(data, maxlen) -> int"""
        ...

    def readyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.readyRead; argument details are not documented."""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def reset(self) -> bool:
        """X.reset() -> bool"""
        ...

    def seek(self, pos: Any) -> bool:
        """X.seek(pos) -> bool"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def serverName(self) -> str:
        """X.serverName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QLocalSocket::serverName() const

Returns the name of the peer as specified by
[setServerName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setServerName)(),
or an empty [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) if
[setServerName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setServerName)()
has not been called or
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)()
failed.

**See also**
[setServerName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setServerName)(),
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)(),
and
[fullServerName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#fullServerName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
serverName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#serverName"""
        ...

    def setErrorString(self, errorString: Any) -> Any:
        """X.setErrorString(errorString)"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setOpenMode(self, openMode: Any) -> Any:
        """X.setOpenMode(openMode)"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setReadBufferSize(self, size: int) -> None:
        """X.setReadBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QLocalSocket::setReadBufferSize([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *size*)

Sets the size of [QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html)'s
internal read buffer to be *size* bytes.

If the buffer size is limited to a certain size,
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) won't buffer more
than this size of data. Exceptionally, a buffer size of 0 means that the read buffer is
unlimited and all incoming data is buffered. This is the default.

This option is useful if you only read the data at certain points in time (e.g., in a
real-time streaming application) or if you want to protect your socket against receiving
too much data, which may eventually cause your application to run out of memory.

**See also**
[readBufferSize](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#readBufferSize)()
and [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setReadBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setReadBufferSize"""
        ...

    def setServerName(self, name: str) -> None:
        """X.setServerName(name)

Supplemental documentation:
Qt 5 reference:

### void QLocalSocket::setServerName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Set the *name* of the peer to connect to. On Windows name is the name of a named pipe;
on Unix name is the name of a local domain socket.

This function must be called when the socket is not connected.

This function was introduced in Qt 5.1.

**See also**
[serverName](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#serverName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setServerName(self, name: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setServerName"""
        ...

    def setSocketDescriptor(self, socketDescriptor: int, socketState: Any, openMode: Any) -> bool:
        """X.setSocketDescriptor(socketDescriptor, socketState, openMode) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalSocket::setSocketDescriptor([qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) *socketDescriptor*, [QLocalSocket::LocalSocketState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum) *socketState* \\= ConnectedState, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite)

Initializes [QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) with
the native socket descriptor *socketDescriptor*. Returns `true` if
[socketDescriptor](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#socketDescriptor)
is accepted as a valid socket descriptor; otherwise returns `false`. The socket is
opened in the mode specified by *openMode*, and enters the socket state specified by
*socketState*.

**Note:** It is not possible to initialize two local sockets with the same native socket
descriptor.

**See also**
[socketDescriptor](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#socketDescriptor)(),
[state](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#state)(), and
[openMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#openMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketDescriptor(self, socketDescriptor: int, socketState: PySide2.QtNetwork.QLocalSocket.LocalSocketState=..., openMode: PySide2.QtCore.QIODevice.OpenMode=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setSocketDescriptor"""
        ...

    def setTextModeEnabled(self, enabled: Any) -> Any:
        """X.setTextModeEnabled(enabled)"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def size(self) -> int:
        """X.size() -> int"""
        ...

    def socketDescriptor(self) -> int:
        """X.socketDescriptor() -> int

Supplemental documentation:
Qt 5 reference:

### [qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) QLocalSocket::socketDescriptor() const

Returns the native socket descriptor of the
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) object if this is
available; otherwise returns -1.

The socket descriptor is not available when
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) is in
[UnconnectedState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum).
The type of the descriptor depends on the platform:

- On Windows, the returned value is a [Winsock 2 Socket Handle](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740522(v=vs.85).aspx).
- With WinRT and on INTEGRITY, the returned value is the [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) socket descriptor and the type is defined by [socketDescriptor](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketDescriptor).
- On all other UNIX-like operating systems, the type is a file descriptor representing a socket.

**See also**
[setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#setSocketDescriptor)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
socketDescriptor(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#socketDescriptor"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def state(self) -> Any:
        """X.state()

Supplemental documentation:
Qt 5 reference:

### [QLocalSocket::LocalSocketState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum) QLocalSocket::state() const

Returns the state of the socket.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#error)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
state(self) -> PySide2.QtNetwork.QLocalSocket.LocalSocketState
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#state"""
        ...

    def stateChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QLocalSocket.stateChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QLocalSocket::stateChanged([QLocalSocket::LocalSocketState](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#LocalSocketState-enum) *socketState*)

This signal is emitted whenever
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html)'s state changes.
The *socketState* parameter is the new state.

QLocalSocket::SocketState is not a registered metatype, so for queued connections, you
will have to register it with
[Q\\_DECLARE\\_METATYPE](https://doc.qt.io/archives/qt-5.15/qmetatype.html#Q_DECLARE_METATYPE)()
and
[qRegisterMetaType](https://doc.qt.io/archives/qt-5.15/qmetatype.html#qRegisterMetaType-1)().

**See also** [state](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#state)() and
[Creating Custom Qt Types](https://doc.qt.io/archives/qt-5.15/custom-types.html).

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#stateChanged"""
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

    def ungetChar(self, c: Any) -> Any:
        """X.ungetChar(c)"""
        ...

    def waitForBytesWritten(self, msecs: int) -> bool:
        """X.waitForBytesWritten(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QLocalSocket::waitForBytesWritten(int *msecs* \\= 30000\\)

Reimplements:
[QIODevice::waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#waitForBytesWritten)(int
msecs).

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForBytesWritten(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForBytesWritten"""
        ...

    def waitForConnected(self, msecs: int) -> bool:
        """X.waitForConnected(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalSocket::waitForConnected(int *msecs* \\= 30000\\)

Waits until the socket is connected, up to *msecs* milliseconds. If the connection has
been established, this function returns `true`; otherwise it returns `false`. In the
case where it returns `false`, you can call
[error](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#error)() to determine the
cause of the error.

The following example waits up to one second for a connection to be established:

```
socket->connectToServer("market");
if (socket->waitForConnected(1000))
    qDebug("Connected!");
```

If *msecs* is -1, this function will not time out.

**See also**
[connectToServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connectToServer)()
and [connected](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#connected)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForConnected(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForConnected"""
        ...

    def waitForDisconnected(self, msecs: int) -> bool:
        """X.waitForDisconnected(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QLocalSocket::waitForDisconnected(int *msecs* \\= 30000\\)

Waits until the socket has disconnected, up to *msecs* milliseconds. If the connection
was successfully disconnected, this function returns `true`; otherwise it returns
`false` (if the operation timed out, if an error occurred, or if this
[QLocalSocket](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html) is already
disconnected). In the case where it returns `false`, you can call
[error](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#error)() to determine the
cause of the error.

The following example waits up to one second for a connection to be closed:

```
socket->disconnectFromServer();
if (socket->state() == QLocalSocket::UnconnectedState
    || socket->waitForDisconnected(1000)) {
    qDebug("Disconnected!");
}
```

If *msecs* is -1, this function will not time out.

**See also**
[disconnectFromServer](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#disconnectFromServer)()
and [close](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForDisconnected(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForDisconnected"""
        ...

    def waitForReadyRead(self, msecs: int) -> bool:
        """X.waitForReadyRead(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QLocalSocket::waitForReadyRead(int *msecs* \\= 30000\\)

Reimplements:
[QIODevice::waitForReadyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#waitForReadyRead)(int
msecs).

This function blocks until data is available for reading and the
[readyRead()](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead) signal has
been emitted. The function will timeout after *msecs* milliseconds; the default timeout
is 30000 milliseconds.

The function returns `true` if data is available for reading; otherwise it returns
`false` (if an error occurred or the operation timed out).

**See also**
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForBytesWritten)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForReadyRead(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#waitForReadyRead"""
        ...

    def write(self, data: Any) -> int:
        """X.write(data) -> int"""
        ...

    def writeData(self, arg__1: str, arg__2: int) -> int:
        """X.writeData(arg__1, arg__2) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QLocalSocket::writeData(const char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *c*)

Reimplements:
[QIODevice::writeData](https://doc.qt.io/archives/qt-5.15/qiodevice.html#writeData)(const
char \\*data, qint64 maxSize).

Upstream PySide2 reference signatures (binding differences may apply):

```python
writeData(self, arg__1: str, arg__2: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qlocalsocket.html#writeData"""
        ...
    Append: Any
    ClosingState: Any
    ConnectedState: Any
    ConnectingState: Any
    ConnectionError: Any
    ConnectionRefusedError: Any
    DatagramTooLargeError: Any
    LocalSocketError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    LocalSocketState: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NotOpen: Any
    OpenMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenModeFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OperationError: Any
    PeerClosedError: Any
    ReadOnly: Any
    ReadWrite: Any
    ServerNotFoundError: Any
    SocketAccessError: Any
    SocketResourceError: Any
    SocketTimeoutError: Any
    Text: Any
    Truncate: Any
    Unbuffered: Any
    UnconnectedState: Any
    UnknownSocketError: Any
    UnsupportedSocketOperationError: Any
    WriteOnly: Any
    objectName: Any

class QNetworkAccessManager:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The Network Access API is constructed around one QNetworkAccessManager object, which
holds the common configuration and settings for the requests it sends. It contains the
proxy and cache configuration, as well as the signals related to such issues, and reply
signals that can be used to monitor the progress of a network operation. One
QNetworkAccessManager instance should be enough for the whole Qt application. Since
QNetworkAccessManager is based on
[QObject](https://doc.qt.io/archives/qt-5.15/qobject.html), it can only be used from the
thread it belongs to.

Once a QNetworkAccessManager object has been created, the application can use it to send
requests over the network. A group of standard functions are supplied that take a
request and optional data, and each return a
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object. The
returned object is used to obtain any data returned in response to the corresponding
request.

A simple download off the network could be accomplished with:

```
QNetworkAccessManager *manager = new QNetworkAccessManager(this);
connect(manager, &QNetworkAccessManager::finished,
        this, &MyClass::replyFinished);

manager->get(QNetworkRequest(QUrl("http://qt-project.org")));
```

QNetworkAccessManager has an asynchronous API. When the `replyFinished` slot above is
called, the parameter it takes is the
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object containing
the downloaded data as well as meta-data (headers, etc.).

**Note:** After the request has finished, it is the responsibility of the user to delete
the [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object at an
appropriate time. Do not directly delete it inside the slot connected to
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished)().
You can use the
[deleteLater](https://doc.qt.io/archives/qt-5.15/qobject.html#deleteLater)() function.

**Note:** QNetworkAccessManager queues the requests it receives. The number of requests
executed in parallel is dependent on the protocol. Currently, for the HTTP protocol on
desktop platforms, 6 requests are executed in parallel for one host/port combination.

A more involved example, assuming the manager is already existent, can be:

```
QNetworkRequest request;
request.setUrl(QUrl("http://qt-project.org"));
request.setRawHeader("User-Agent", "MyOwnBrowser 1.0");

QNetworkReply *reply = manager->get(request);
connect(reply, &QIODevice::readyRead, this, &MyClass::slotReadyRead);
connect(reply, &QNetworkReply::errorOccurred,
        this, &MyClass::slotError);
connect(reply, &QNetworkReply::sslErrors,
        this, &MyClass::slotSslErrors);
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def activeConfiguration(self) -> Any:
        """X.activeConfiguration() -> PythonQt.QtNetwork.QNetworkConfiguration

Upstream PySide2 reference signatures (binding differences may apply):

```python
activeConfiguration(self) -> PySide2.QtNetwork.QNetworkConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#activeConfiguration"""
        ...

    def authenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.authenticationRequired; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkAccessManager::authenticationRequired([QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\**reply*, [QAuthenticator](https://doc.qt.io/archives/qt-5.15/qauthenticator.html) \\**authenticator*)

This signal is emitted whenever a final server requests authentication before it
delivers the requested contents. The slot connected to this signal should fill the
credentials for the contents (which can be determined by inspecting the *reply* object)
in the *authenticator* object.

[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
will cache the credentials internally and will send the same values if the server
requires authentication again, without emitting the authenticationRequired() signal. If
it rejects the credentials, this signal will be emitted again.

**Note:** To have the request not send credentials you must not call setUser() or
setPassword() on the *authenticator* object. This will result in the
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished)()
signal being emitted with a
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) with error
[AuthenticationRequiredError](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#NetworkError-enum).

**Note:** It is not possible to use a QueuedConnection to connect to this signal, as the
connection will fail if the authenticator has not been filled in with new information
when the signal returns.

**See also**
[proxyAuthenticationRequired](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyAuthenticationRequired)(),
[QAuthenticator::setUser](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setUser)(),
and
[QAuthenticator::setPassword](https://doc.qt.io/archives/qt-5.15/qauthenticator.html#setPassword)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#authenticationRequired"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def cache(self) -> Any:
        """X.cache() -> PythonQt.QtNetwork.QAbstractNetworkCache

Supplemental documentation:
Qt 5 reference:

### [QAbstractNetworkCache](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html) \\*QNetworkAccessManager::cache() const

Returns the cache that is used to store data obtained from the network.

This function was introduced in Qt 4.5.

**See also**
[setCache](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setCache)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
cache(self) -> PySide2.QtNetwork.QAbstractNetworkCache
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#cache"""
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

    def clearAccessCache(self) -> None:
        """X.clearAccessCache()

Supplemental documentation:
Qt 5 reference:

### void QNetworkAccessManager::clearAccessCache()

Flushes the internal cache of authentication data and network connections.

This function is useful for doing auto tests.

This function was introduced in Qt 5.0.

**See also**
[clearConnectionCache](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#clearConnectionCache)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
clearAccessCache(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#clearAccessCache"""
        ...

    def configuration(self) -> Any:
        """X.configuration() -> PythonQt.QtNetwork.QNetworkConfiguration

Upstream PySide2 reference signatures (binding differences may apply):

```python
configuration(self) -> PySide2.QtNetwork.QNetworkConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#configuration"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def connectToHost(self, hostName: str, port: int) -> None:
        """X.connectToHost(hostName, port)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAccessManager::connectToHost(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port* \\= 80\\)

Initiates a connection to the host given by *hostName* at port *port*. This function is
useful to complete the TCP handshake to a host before the HTTP request is made,
resulting in a lower network latency.

**Note:** This function has no possibility to report errors.

This function was introduced in Qt 5.2.

**See also**
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#connectToHostEncrypted)(),
[get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)(),
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)(),
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)(), and
[deleteResource](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
connectToHost(self, hostName: str, port: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#connectToHost"""
        ...

    def connectToHostEncrypted(self, hostName: str, port: int, sslConfiguration: Any) -> None:
        """X.connectToHostEncrypted(hostName, port, sslConfiguration)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAccessManager::connectToHostEncrypted(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port* \\= 443, const [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) \\&*sslConfiguration* \\= QSslConfiguration::defaultConfiguration())

Initiates a connection to the host given by *hostName* at port *port*, using
*sslConfiguration*. This function is useful to complete the TCP and SSL handshake to a
host before the HTTPS request is made, resulting in a lower network latency.

**Note:** Preconnecting a SPDY connection can be done by calling
setAllowedNextProtocols() on *sslConfiguration* with
[QSslConfiguration::NextProtocolSpdy3\\_0](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolSpdy3_0-var)
contained in the list of allowed protocols. When using SPDY, one single connection per
host is enough, i.e. calling this method multiple times per host will not result in
faster network transactions.

**Note:** This function has no possibility to report errors.

This function was introduced in Qt 5.2.

**See also**
[connectToHost](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#connectToHost)(),
[get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)(),
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)(),
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)(), and
[deleteResource](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource)().

### void QNetworkAccessManager::connectToHostEncrypted(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*, const [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) \\&*sslConfiguration*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*peerName*)

This is an overloaded function.

Initiates a connection to the host given by *hostName* at port *port*, using
*sslConfiguration* with *peerName* set to be the hostName used for certificate
validation. This function is useful to complete the TCP and SSL handshake to a host
before the HTTPS request is made, resulting in a lower network latency.

**Note:** Preconnecting a SPDY connection can be done by calling
setAllowedNextProtocols() on *sslConfiguration* with
[QSslConfiguration::NextProtocolSpdy3\\_0](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolSpdy3_0-var)
contained in the list of allowed protocols. When using SPDY, one single connection per
host is enough, i.e. calling this method multiple times per host will not result in
faster network transactions.

**Note:** This function has no possibility to report errors.

This function was introduced in Qt 5.13.

**See also**
[connectToHost](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#connectToHost)(),
[get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)(),
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)(),
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)(), and
[deleteResource](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
connectToHostEncrypted(self, hostName: str, port: int, sslConfiguration: PySide2.QtNetwork.QSslConfiguration, peerName: str) -> None
connectToHostEncrypted(self, hostName: str, port: int=..., sslConfiguration: PySide2.QtNetwork.QSslConfiguration=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#connectToHostEncrypted"""
        ...

    def cookieJar(self) -> Any:
        """X.cookieJar() -> PythonQt.QtNetwork.QNetworkCookieJar

Supplemental documentation:
Qt 5 reference:

### [QNetworkCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html) \\*QNetworkAccessManager::cookieJar() const

Returns the
[QNetworkCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html) that is
used to store cookies obtained from the network as well as cookies that are about to be
sent.

**See also**
[setCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setCookieJar)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
cookieJar(self) -> PySide2.QtNetwork.QNetworkCookieJar
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#cookieJar"""
        ...

    def createRequest(self, op: Any, request: Any, outgoingData: Any) -> Any:
        """X.createRequest(op, request, outgoingData) -> PythonQt.QtNetwork.QNetworkReply

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::createRequest([QNetworkAccessManager::Operation](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#Operation-enum) *op*, const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*originalReq*, [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**outgoingData* \\= nullptr)

Returns a new [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html)
object to handle the operation *op* and request *originalReq*. The device *outgoingData*
is always 0 for Get and Head requests, but is the value passed to
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)() and
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)() in those
operations (the [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)
variants will pass a [QBuffer](https://doc.qt.io/archives/qt-5.15/qbuffer.html) object).

The default implementation calls
[QNetworkCookieJar::cookiesForUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#cookiesForUrl)()
on the cookie jar set with
[setCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setCookieJar)()
to obtain the cookies to be sent to the remote server.

The returned object must be in an open state.

Upstream PySide2 reference signatures (binding differences may apply):

```python
createRequest(self, op: PySide2.QtNetwork.QNetworkAccessManager.Operation, request: PySide2.QtNetwork.QNetworkRequest, outgoingData: typing.Optional[PySide2.QtCore.QIODevice]=...) -> PySide2.QtNetwork.QNetworkReply
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#createRequest"""
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

    def deleteResource(self, request: Any) -> Any:
        """X.deleteResource(request) -> PythonQt.QtNetwork.QNetworkReply

Supplemental documentation:
Qt 5 reference:

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::deleteResource(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*)

Sends a request to delete the resource identified by the URL of *request*.

**Note:** This feature is currently available for HTTP only, performing an HTTP DELETE
request.

This function was introduced in Qt 4.6.

**See also** [get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)(),
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)(),
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)(), and
[sendCustomRequest](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#sendCustomRequest)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
deleteResource(self, request: PySide2.QtNetwork.QNetworkRequest) -> PySide2.QtNetwork.QNetworkReply
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.destroyed; argument details are not documented."""
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

    def encrypted(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.encrypted; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkAccessManager::encrypted([QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\**reply*)

This signal is emitted when an SSL/TLS session has successfully completed the initial
handshake. At this point, no user data has been transmitted. The signal can be used to
perform additional checks on the certificate chain, for example to notify users when the
certificate for a website has changed. The *reply* parameter specifies which network
reply is responsible. If the reply does not match the expected criteria then it should
be aborted by calling
[QNetworkReply::abort](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#abort)() by
a slot connected to this signal. The SSL configuration in use can be inspected using the
[QNetworkReply::sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)()
method.

Internally,
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
may open multiple connections to a server, in order to allow it process requests in
parallel. These connections may be reused, which means that the encrypted() signal would
not be emitted. This means that you are only guaranteed to receive this signal for the
first connection to a site in the lifespan of the
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).

This function was introduced in Qt 5.1.

**See also**
[QSslSocket::encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)()
and
[QNetworkReply::encrypted](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#encrypted)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#encrypted"""
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

    def finished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.finished; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkAccessManager::finished([QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\**reply*)

This signal is emitted whenever a pending network reply is finished. The *reply*
parameter will contain a pointer to the reply that has just finished. This signal is
emitted in tandem with the
[QNetworkReply::finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)()
signal.

See
[QNetworkReply::finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)()
for information on the status that the object will be in.

**Note:** Do not delete the *reply* object in the slot connected to this signal. Use
[deleteLater](https://doc.qt.io/archives/qt-5.15/qobject.html#deleteLater)().

**See also**
[QNetworkReply::finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)()
and
[QNetworkReply::error](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#error)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished"""
        ...

    def get(self, request: Any) -> Any:
        """X.get(request) -> PythonQt.QtNetwork.QNetworkReply

Supplemental documentation:
Qt 5 reference:

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::get(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*)

Posts a request to obtain the contents of the target *request* and returns a new
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object opened for
reading which emits the
[readyRead()](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead) signal
whenever new data arrives.

The contents as well as associated headers will be downloaded.

**See also**
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)(),
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)(),
[deleteResource](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource)(),
and
[sendCustomRequest](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#sendCustomRequest)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
get(self, request: PySide2.QtNetwork.QNetworkRequest) -> PySide2.QtNetwork.QNetworkReply
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get"""
        ...

    def head(self, request: Any) -> Any:
        """X.head(request) -> PythonQt.QtNetwork.QNetworkReply

Supplemental documentation:
Qt 5 reference:

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::head(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*)

Posts a request to obtain the network headers for *request* and returns a new
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object which will
contain such headers.

The function is named after the HTTP request associated (HEAD).

Upstream PySide2 reference signatures (binding differences may apply):

```python
head(self, request: PySide2.QtNetwork.QNetworkRequest) -> PySide2.QtNetwork.QNetworkReply
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#head"""
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

    def networkAccessibleChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.networkAccessibleChanged; argument details are not documented."""
        ...

    def networkSessionConnected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.networkSessionConnected; argument details are not documented."""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.objectNameChanged; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def post(self, request: Any, multiPart: Any) -> Any:
        """X.post(request, multiPart) -> PythonQt.QtNetwork.QNetworkReply

Supplemental documentation:
Qt 5 reference:

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::post(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**data*)

Sends an HTTP POST request to the destination specified by *request* and returns a new
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object opened for
reading that will contain the reply sent by the server. The contents of the *data*
device will be uploaded to the server.

*data* must be open for reading and must remain valid until the
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished)()
signal is emitted for this reply.

**Note:** Sending a POST request on protocols other than HTTP and HTTPS is undefined and
will probably fail.

**See also** [get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)(),
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)(),
[deleteResource](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource)(),
and
[sendCustomRequest](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#sendCustomRequest)().

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::post(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*data*)

This is an overloaded function.

Sends the contents of the *data* byte array to the destination specified by *request*.

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::post(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, [QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html) \\**multiPart*)

This is an overloaded function.

Sends the contents of the *multiPart* message to the destination specified by *request*.

This can be used for sending MIME multipart messages over HTTP.

This function was introduced in Qt 4.8.

**See also** [QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html),
[QHttpPart](https://doc.qt.io/archives/qt-5.15/qhttppart.html), and
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
post(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QByteArray) -> PySide2.QtNetwork.QNetworkReply
post(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QIODevice) -> PySide2.QtNetwork.QNetworkReply
post(self, request: PySide2.QtNetwork.QNetworkRequest, multiPart: PySide2.QtNetwork.QHttpMultiPart) -> PySide2.QtNetwork.QNetworkReply
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post"""
        ...

    def preSharedKeyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.preSharedKeyAuthenticationRequired; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkAccessManager::preSharedKeyAuthenticationRequired([QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\**reply*, [QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html) \\**authenticator*)

This signal is emitted if the SSL/TLS handshake negotiates a PSK ciphersuite, and
therefore a PSK authentication is then required. The *reply* object is the
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) that is
negotiating such ciphersuites.

When using PSK, the client must send to the server a valid identity and a valid pre
shared key, in order for the SSL handshake to continue. Applications can provide this
information in a slot connected to this signal, by filling in the passed *authenticator*
object according to their needs.

**Note:** Ignoring this signal, or failing to provide the required credentials, will
cause the handshake to fail, and therefore the connection to be aborted.

**Note:** The *authenticator* object is owned by the reply and must not be deleted by
the application.

This function was introduced in Qt 5.5.

**See also**
[QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html).

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#preSharedKeyAuthenticationRequired"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def proxy(self) -> Any:
        """X.proxy() -> PythonQt.QtNetwork.QNetworkProxy

Supplemental documentation:
Qt 5 reference:

### [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) QNetworkAccessManager::proxy() const

Returns the [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) that
the requests sent using this
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
object will use. The default value for the proxy is
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum).

**See also**
[setProxy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxy)(),
[setProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxyFactory)(),
and
[proxyAuthenticationRequired](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyAuthenticationRequired)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
proxy(self) -> PySide2.QtNetwork.QNetworkProxy
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxy"""
        ...

    def proxyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.proxyAuthenticationRequired; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkAccessManager::proxyAuthenticationRequired(const [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) \\&*proxy*, [QAuthenticator](https://doc.qt.io/archives/qt-5.15/qauthenticator.html) \\**authenticator*)

This signal is emitted whenever a proxy requests authentication and
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
cannot find a valid, cached credential. The slot connected to this signal should fill in
the credentials for the proxy *proxy* in the *authenticator* object.

[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
will cache the credentials internally. The next time the proxy requests authentication,
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
will automatically send the same credential without emitting the
proxyAuthenticationRequired signal again.

If the proxy rejects the credentials,
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
will emit the signal again.

**See also**
[proxy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxy)(),
[setProxy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxy)(),
and
[authenticationRequired](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#authenticationRequired)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyAuthenticationRequired"""
        ...

    def proxyFactory(self) -> Any:
        """X.proxyFactory() -> PythonQt.QtNetwork.QNetworkProxyFactory

Supplemental documentation:
Qt 5 reference:

### [QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html) \\*QNetworkAccessManager::proxyFactory() const

Returns the proxy factory that this
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
object is using to determine the proxies to be used for requests.

Note that the pointer returned by this function is managed by
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
and could be deleted at any time.

This function was introduced in Qt 4.5.

**See also**
[setProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxyFactory)()
and [proxy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
proxyFactory(self) -> PySide2.QtNetwork.QNetworkProxyFactory
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyFactory"""
        ...

    def put(self, request: Any, multiPart: Any) -> Any:
        """X.put(request, multiPart) -> PythonQt.QtNetwork.QNetworkReply

Supplemental documentation:
Qt 5 reference:

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::put(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**data*)

Uploads the contents of *data* to the destination *request* and returns a new
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object that will
be open for reply.

*data* must be opened for reading when this function is called and must remain valid
until the
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished)()
signal is emitted for this reply.

Whether anything will be available for reading from the returned object is protocol
dependent. For HTTP, the server may send a small HTML page indicating the upload was
successful (or not). Other protocols will probably have content in their replies.

**Note:** For HTTP, this request will send a PUT request, which most servers do not
allow. Form upload mechanisms, including that of uploading files through HTML forms, use
the POST mechanism.

**See also** [get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)(),
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)(),
[deleteResource](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource)(),
and
[sendCustomRequest](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#sendCustomRequest)().

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::put(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*data*)

This is an overloaded function.

Sends the contents of the *data* byte array to the destination specified by *request*.

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::put(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, [QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html) \\**multiPart*)

This is an overloaded function.

Sends the contents of the *multiPart* message to the destination specified by *request*.

This can be used for sending MIME multipart messages over HTTP.

This function was introduced in Qt 4.8.

**See also** [QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html),
[QHttpPart](https://doc.qt.io/archives/qt-5.15/qhttppart.html), and
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
put(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QByteArray) -> PySide2.QtNetwork.QNetworkReply
put(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QIODevice) -> PySide2.QtNetwork.QNetworkReply
put(self, request: PySide2.QtNetwork.QNetworkRequest, multiPart: PySide2.QtNetwork.QHttpMultiPart) -> PySide2.QtNetwork.QNetworkReply
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put"""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def sendCustomRequest(self, request: Any, verb: Any, data: Any) -> Any:
        """X.sendCustomRequest(request, verb, data) -> PythonQt.QtNetwork.QNetworkReply

Supplemental documentation:
Qt 5 reference:

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::sendCustomRequest(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*verb*, [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**data* \\= nullptr)

Sends a custom request to the server identified by the URL of *request*.

It is the user's responsibility to send a *verb* to the server that is valid according
to the HTTP specification.

This method provides means to send verbs other than the common ones provided via
[get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)() or
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)() etc., for
instance sending an HTTP OPTIONS command.

If *data* is not empty, the contents of the *data* device will be uploaded to the
server; in that case, data must be open for reading and must remain valid until the
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished)()
signal is emitted for this reply.

**Note:** This feature is currently available for HTTP(S) only.

This function was introduced in Qt 4.7.

**See also** [get](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#get)(),
[post](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#post)(),
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)(), and
[deleteResource](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#deleteResource)().

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::sendCustomRequest(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*verb*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*data*)

This is an overloaded function.

Sends the contents of the *data* byte array to the destination specified by *request*.

This function was introduced in Qt 5.8.

### [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\*QNetworkAccessManager::sendCustomRequest(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*verb*, [QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html) \\**multiPart*)

This is an overloaded function.

Sends a custom request to the server identified by the URL of *request*.

Sends the contents of the *multiPart* message to the destination specified by *request*.

This can be used for sending MIME multipart messages for custom verbs.

This function was introduced in Qt 5.8.

**See also** [QHttpMultiPart](https://doc.qt.io/archives/qt-5.15/qhttpmultipart.html),
[QHttpPart](https://doc.qt.io/archives/qt-5.15/qhttppart.html), and
[put](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#put)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sendCustomRequest(self, request: PySide2.QtNetwork.QNetworkRequest, verb: PySide2.QtCore.QByteArray, data: PySide2.QtCore.QByteArray) -> PySide2.QtNetwork.QNetworkReply
sendCustomRequest(self, request: PySide2.QtNetwork.QNetworkRequest, verb: PySide2.QtCore.QByteArray, data: typing.Optional[PySide2.QtCore.QIODevice]=...) -> PySide2.QtNetwork.QNetworkReply
sendCustomRequest(self, request: PySide2.QtNetwork.QNetworkRequest, verb: PySide2.QtCore.QByteArray, multiPart: PySide2.QtNetwork.QHttpMultiPart) -> PySide2.QtNetwork.QNetworkReply
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#sendCustomRequest"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setCache(self, cache: Any) -> None:
        """X.setCache(cache)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAccessManager::setCache([QAbstractNetworkCache](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html) \\**cache*)

Sets the manager's network cache to be the *cache* specified. The cache is used for all
requests dispatched by the manager.

Use this function to set the network cache object to a class that implements additional
features, like saving the cookies to permanent storage.

**Note:**
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
takes ownership of the *cache* object.

[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
by default does not have a set cache. Qt provides a simple disk cache,
[QNetworkDiskCache](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html), which
can be used.

This function was introduced in Qt 4.5.

**See also**
[cache](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#cache)() and
[QNetworkRequest::CacheLoadControl](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#CacheLoadControl-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCache(self, cache: PySide2.QtNetwork.QAbstractNetworkCache) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setCache"""
        ...

    def setConfiguration(self, config: Any) -> None:
        """X.setConfiguration(config)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setConfiguration(self, config: PySide2.QtNetwork.QNetworkConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setConfiguration"""
        ...

    def setCookieJar(self, cookieJar: Any) -> None:
        """X.setCookieJar(cookieJar)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAccessManager::setCookieJar([QNetworkCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html) \\**cookieJar*)

Sets the manager's cookie jar to be the *cookieJar* specified. The cookie jar is used by
all requests dispatched by the manager.

Use this function to set the cookie jar object to a class that implements additional
features, like saving the cookies to permanent storage.

**Note:**
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
takes ownership of the *cookieJar* object.

If *cookieJar* is in the same thread as this
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html),
it will set the parent of the *cookieJar* so that the cookie jar is deleted when this
object is deleted as well. If you want to share cookie jars between different
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
objects, you may want to set the cookie jar's parent to 0 after calling this function.

[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
by default does not implement any cookie policy of its own: it accepts all cookies sent
by the server, as long as they are well formed and meet the minimum security
requirements (cookie domain matches the request's and cookie path matches the
request's). In order to implement your own security policy, override the
[QNetworkCookieJar::cookiesForUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#cookiesForUrl)()
and
[QNetworkCookieJar::setCookiesFromUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setCookiesFromUrl)()
virtual functions. Those functions are called by
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
when it detects a new cookie.

**See also**
[cookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#cookieJar)(),
[QNetworkCookieJar::cookiesForUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#cookiesForUrl)(),
and
[QNetworkCookieJar::setCookiesFromUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setCookiesFromUrl)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCookieJar(self, cookieJar: PySide2.QtNetwork.QNetworkCookieJar) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setCookieJar"""
        ...

    def setNetworkAccessible(self, accessible: Any) -> None:
        """X.setNetworkAccessible(accessible)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setNetworkAccessible(self, accessible: PySide2.QtNetwork.QNetworkAccessManager.NetworkAccessibility) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setNetworkAccessible"""
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

    def setProxy(self, proxy: Any) -> None:
        """X.setProxy(proxy)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAccessManager::setProxy(const [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) \\&*proxy*)

Sets the proxy to be used in future requests to be *proxy*. This does not affect
requests that have already been sent. The
[proxyAuthenticationRequired](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyAuthenticationRequired)()
signal will be emitted if the proxy requests authentication.

A proxy set with this function will be used for all requests issued by
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).
In some cases, it might be necessary to select different proxies depending on the type
of request being sent or the destination host. If that's the case, you should consider
using
[setProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxyFactory)().

**See also**
[proxy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxy)() and
[proxyAuthenticationRequired](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyAuthenticationRequired)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProxy(self, proxy: PySide2.QtNetwork.QNetworkProxy) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxy"""
        ...

    def setProxyFactory(self, factory: Any) -> None:
        """X.setProxyFactory(factory)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAccessManager::setProxyFactory([QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html) \\**factory*)

Sets the proxy factory for this class to be *factory*. A proxy factory is used to
determine a more specific list of proxies to be used for a given request, instead of
trying to use the same proxy value for all requests.

All queries sent by
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
will have type
[QNetworkProxyQuery::UrlRequest](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum).

For example, a proxy factory could apply the following rules:

- if the target address is in the local network (for example, if the hostname contains no dots or if it's an IP address in the organization's range), return [QNetworkProxy::NoProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
- if the request is FTP, return an FTP proxy
- if the request is HTTP or HTTPS, then return an HTTP proxy
- otherwise, return a SOCKSv5 proxy server

The lifetime of the object *factory* will be managed by
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).
It will delete the object when necessary.

**Note:** If a specific proxy is set with
[setProxy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxy)(),
the factory will not be used.

This function was introduced in Qt 4.5.

**See also**
[proxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#proxyFactory)(),
[setProxy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxy)(),
and [QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProxyFactory(self, factory: PySide2.QtNetwork.QNetworkProxyFactory) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setProxyFactory"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def sslErrors(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkAccessManager.sslErrors; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkAccessManager::sslErrors([QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) \\**reply*, const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html)\\> \\&*errors*)

This signal is emitted if the SSL/TLS session encountered errors during the set up,
including certificate verification errors. The *errors* parameter contains the list of
errors and *reply* is the
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) that is
encountering these errors.

To indicate that the errors are not fatal and that the connection should proceed, the
[QNetworkReply::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)()
function should be called from the slot connected to this signal. If it is not called,
the SSL session will be torn down before any data is exchanged (including the URL).

This signal can be used to display an error message to the user indicating that security
may be compromised and display the SSL settings (see sslConfiguration() to obtain it).
If the user decides to proceed after analyzing the remote certificate, the slot should
call ignoreSslErrors().

**See also**
[QSslSocket::sslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#sslErrors)(),
[QNetworkReply::sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)(),
[QNetworkReply::sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)(),
and
[QNetworkReply::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#sslErrors"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def supportedSchemes(self) -> tuple:
        """X.supportedSchemes() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QNetworkAccessManager::supportedSchemes() const

Lists all the URL schemes supported by the access manager.

This function was introduced in Qt 5.2.

**See also**
[supportedSchemesImplementation](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#supportedSchemesImplementation)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
supportedSchemes(self) -> typing.List[str]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#supportedSchemes"""
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
    Accessible: Any
    CustomOperation: Any
    DeleteOperation: Any
    GetOperation: Any
    HeadOperation: Any
    NetworkAccessibility: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NotAccessible: Any
    Operation: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PostOperation: Any
    PutOperation: Any
    UnknownAccessibility: Any
    UnknownOperation: Any
    networkAccessible: Any
    objectName: Any

class QNetworkAddressEntry:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Each network interface can contain zero or more IP addresses, which in turn can be
associated with a netmask and/or a broadcast address (depending on support from the
operating system).

This class represents one such group.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def broadcast(self) -> Any:
        """X.broadcast() -> PythonQt.QtNetwork.QHostAddress

Supplemental documentation:
Qt 5 reference:

### [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) QNetworkAddressEntry::broadcast() const

Returns the broadcast address associated with the IPv4 address and netmask. It can
usually be derived from those two by setting to 1 the bits of the IP address where the
netmask contains a 0\\. (In other words, by bitwise-OR'ing the IP address with the
inverse of the netmask)

This member is always empty for IPv6 addresses, since the concept of broadcast has been
abandoned in that system in favor of multicast. In particular, the group of hosts
corresponding to all the nodes in the local network can be reached by the "all-nodes"
special multicast group (address FF02::1).

**See also**
[setBroadcast](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setBroadcast)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
broadcast(self) -> PySide2.QtNetwork.QHostAddress
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#broadcast"""
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

    def ip(self) -> Any:
        """X.ip() -> PythonQt.QtNetwork.QHostAddress

Supplemental documentation:
Qt 5 reference:

### [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) QNetworkAddressEntry::ip() const

This function returns one IPv4 or IPv6 address found, that was found in a network
interface.

**See also**
[setIp](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setIp)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
ip(self) -> PySide2.QtNetwork.QHostAddress
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#ip"""
        ...

    def netmask(self) -> Any:
        """X.netmask() -> PythonQt.QtNetwork.QHostAddress

Supplemental documentation:
Qt 5 reference:

### [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) QNetworkAddressEntry::netmask() const

Returns the netmask associated with the IP address. The netmask is expressed in the form
of an IP address, such as 255.255.0.0.

For IPv6 addresses, the prefix length is converted to an address where the number of
bits set to 1 is equal to the prefix length. For a prefix length of 64 bits (the most
common value), the netmask will be expressed as a
[QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) holding the address
FFFF:FFFF:FFFF:FFFF::

**See also**
[setNetmask](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setNetmask)()
and
[prefixLength](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#prefixLength)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
netmask(self) -> PySide2.QtNetwork.QHostAddress
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#netmask"""
        ...

    def prefixLength(self) -> int:
        """X.prefixLength() -> int

Supplemental documentation:
Qt 5 reference:

### int QNetworkAddressEntry::prefixLength() const

Returns the prefix length of this IP address. The prefix length matches the number of
bits set to 1 in the netmask (see
[netmask](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#netmask)()). For
IPv4 addresses, the value is between 0 and 32\\. For IPv6 addresses, it's contained
between 0 and 128 and is the preferred form of representing addresses.

This function returns -1 if the prefix length could not be determined (i.e.,
[netmask](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#netmask)()
returns a null QHostAddress()).

This function was introduced in Qt 4.5.

**See also**
[setPrefixLength](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setPrefixLength)()
and [netmask](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#netmask)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
prefixLength(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#prefixLength"""
        ...

    def setBroadcast(self, newBroadcast: Any) -> None:
        """X.setBroadcast(newBroadcast)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAddressEntry::setBroadcast(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*newBroadcast*)

Sets the broadcast IP address of this
[QNetworkAddressEntry](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html)
object to *newBroadcast*.

**See also**
[broadcast](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#broadcast)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setBroadcast(self, newBroadcast: PySide2.QtNetwork.QHostAddress) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setBroadcast"""
        ...

    def setIp(self, newIp: Any) -> None:
        """X.setIp(newIp)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAddressEntry::setIp(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*newIp*)

Sets the IP address the
[QNetworkAddressEntry](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html)
object contains to *newIp*.

**See also** [ip](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#ip)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setIp(self, newIp: PySide2.QtNetwork.QHostAddress) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setIp"""
        ...

    def setNetmask(self, newNetmask: Any) -> None:
        """X.setNetmask(newNetmask)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAddressEntry::setNetmask(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*newNetmask*)

Sets the netmask that this
[QNetworkAddressEntry](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html)
object contains to *newNetmask*. Setting the netmask also sets the prefix length to
match the new netmask.

**See also**
[netmask](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#netmask)() and
[setPrefixLength](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setPrefixLength)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setNetmask(self, newNetmask: PySide2.QtNetwork.QHostAddress) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setNetmask"""
        ...

    def setPrefixLength(self, length: int) -> None:
        """X.setPrefixLength(length)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAddressEntry::setPrefixLength(int *length*)

Sets the prefix length of this IP address to *length*. The value of *length* must be
valid for this type of IP address: between 0 and 32 for IPv4 addresses, between 0 and
128 for IPv6 addresses. Setting to any invalid value is equivalent to setting to -1,
which means "no prefix length".

Setting the prefix length also sets the netmask (see
[netmask](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#netmask)()).

This function was introduced in Qt 4.5.

**See also**
[prefixLength](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#prefixLength)()
and
[setNetmask](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setNetmask)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPrefixLength(self, length: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#setPrefixLength"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkAddressEntry::swap([QNetworkAddressEntry](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#QNetworkAddressEntry) \\&*other*)

Swaps this network address entry instance with *other*. This function is very fast and
never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkAddressEntry) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#swap"""
        ...

class QNetworkCacheMetaData:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkCacheMetaData provides information about a cache file including the url, when it
was last modified, when the cache file was created, headers for file and if the file
should be saved onto a disk.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def attributes(self) -> dict:
        """X.attributes() -> dict

Supplemental documentation:
Qt 5 reference:

### [QNetworkCacheMetaData::AttributesMap](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#AttributesMap-typedef) QNetworkCacheMetaData::attributes() const

Returns all the attributes stored with this cache item.

This function was introduced in Qt 4.6.

**See also**
[setAttributes](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setAttributes)()
and
[QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
attributes(self) -> typing.Dict[PySide2.QtNetwork.QNetworkRequest.Attribute, typing.Any]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#attributes"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def expirationDate(self) -> Any:
        """X.expirationDate() -> PythonQt.QtCore.QDateTime

Supplemental documentation:
Qt 5 reference:

### [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) QNetworkCacheMetaData::expirationDate() const

Returns the date and time when the meta data expires.

**See also**
[setExpirationDate](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setExpirationDate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
expirationDate(self) -> PySide2.QtCore.QDateTime
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#expirationDate"""
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

### bool QNetworkCacheMetaData::isValid() const

Returns `true` if this network cache meta data has attributes that have been set
otherwise false.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#isValid"""
        ...

    def lastModified(self) -> Any:
        """X.lastModified() -> PythonQt.QtCore.QDateTime

Supplemental documentation:
Qt 5 reference:

### [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) QNetworkCacheMetaData::lastModified() const

Returns the date and time when the meta data was last modified.

**See also**
[setLastModified](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setLastModified)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
lastModified(self) -> PySide2.QtCore.QDateTime
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#lastModified"""
        ...

    def rawHeaders(self) -> tuple:
        """X.rawHeaders() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QNetworkCacheMetaData::RawHeaderList](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#RawHeaderList-typedef) QNetworkCacheMetaData::rawHeaders() const

Returns a list of all raw headers that are set in this meta data. The list is in the
same order that the headers were set.

**See also**
[setRawHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setRawHeaders)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeaders(self) -> typing.List[typing.Tuple[PySide2.QtCore.QByteArray, PySide2.QtCore.QByteArray]]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#rawHeaders"""
        ...

    def readFrom(self, arg__1: Any) -> Any:
        """X.readFrom(arg__1)"""
        ...

    def saveToDisk(self) -> bool:
        """X.saveToDisk() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkCacheMetaData::saveToDisk() const

Returns is this cache should be allowed to be stored on disk.

Some cache implementations can keep these cache items in memory for performance reasons,
but for security reasons they should not be written to disk.

Specifically with http, documents with Cache-control set to no-store or any https
document that doesn't have "Cache-control: public" set will set the saveToDisk to false.

**See also**
[setSaveToDisk](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setSaveToDisk)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
saveToDisk(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#saveToDisk"""
        ...

    def setAttributes(self, attributes: Any) -> None:
        """X.setAttributes(attributes)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCacheMetaData::setAttributes(const [QNetworkCacheMetaData::AttributesMap](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#AttributesMap-typedef) \\&*attributes*)

Sets all attributes of this cache item to be the map *attributes*.

This function was introduced in Qt 4.6.

**See also**
[attributes](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#attributes)()
and
[QNetworkRequest::setAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setAttribute)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAttributes(self, attributes: typing.Dict[PySide2.QtNetwork.QNetworkRequest.Attribute, typing.Any]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setAttributes"""
        ...

    def setExpirationDate(self, dateTime: Any) -> None:
        """X.setExpirationDate(dateTime)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCacheMetaData::setExpirationDate(const [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) \\&*dateTime*)

Sets the date and time when the meta data expires to *dateTime*.

**See also**
[expirationDate](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#expirationDate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setExpirationDate(self, dateTime: PySide2.QtCore.QDateTime) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setExpirationDate"""
        ...

    def setLastModified(self, dateTime: Any) -> None:
        """X.setLastModified(dateTime)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCacheMetaData::setLastModified(const [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) \\&*dateTime*)

Sets the date and time when the meta data was last modified to *dateTime*.

**See also**
[lastModified](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#lastModified)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLastModified(self, dateTime: PySide2.QtCore.QDateTime) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setLastModified"""
        ...

    def setRawHeaders(self, headers: Any) -> None:
        """X.setRawHeaders(headers)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCacheMetaData::setRawHeaders(const [QNetworkCacheMetaData::RawHeaderList](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#RawHeaderList-typedef) \\&*list*)

Sets the raw headers to *list*.

**See also**
[rawHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#rawHeaders)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRawHeaders(self, headers: typing.Sequence[typing.Tuple[PySide2.QtCore.QByteArray, PySide2.QtCore.QByteArray]]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setRawHeaders"""
        ...

    def setSaveToDisk(self, allow: bool) -> None:
        """X.setSaveToDisk(allow)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCacheMetaData::setSaveToDisk(bool *allow*)

Sets whether this network cache meta data and associated content should be allowed to be
stored on disk to *allow*.

**See also**
[saveToDisk](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#saveToDisk)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSaveToDisk(self, allow: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setSaveToDisk"""
        ...

    def setUrl(self, url: Any) -> None:
        """X.setUrl(url)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCacheMetaData::setUrl(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Sets the URL this network cache meta data to be *url*.

The password and fragment are removed from the url.

**See also** [url](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#url)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUrl(self, url: PySide2.QtCore.QUrl) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setUrl"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCacheMetaData::swap([QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#QNetworkCacheMetaData) \\&*other*)

Swaps this metadata instance with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkCacheMetaData) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#swap"""
        ...

    def url(self) -> Any:
        """X.url() -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QNetworkCacheMetaData::url() const

Returns the URL this network cache meta data is referring to.

**See also**
[setUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#setUrl)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
url(self) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html#url"""
        ...

    def writeTo(self, arg__1: Any) -> Any:
        """X.writeTo(arg__1)"""
        ...

class QNetworkConfiguration:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkConfiguration encapsulates a single access point or service network. In most
cases a single access point configuration can be mapped to one network interface.
However a single network interface may not always map to only one access point
configuration. Multiple configurations for the same network device may enable multiple
access points. An example device that could exhibit such a configuration might be a
Smartphone which allows the user to manage multiple WLAN configurations while the device
itself has only one WLAN network device.

The QNetworkConfiguration also supports the concept of service networks. This concept
allows the grouping of multiple access point configurations into one entity. Such a
group is called service network and can be beneficial in cases whereby a network session
to a particular destination network is required (e.g. a company network). When using a
service network the user doesn't usually care which one of the connectivity options is
chosen (e.g. corporate WLAN or VPN via GPRS) as long as he can reach the company's
target server. Depending on the current position and time some of the access points that
make up the service network may not even be available. Furthermore automated access
point roaming can be enabled which enables the device to change the network interface
configuration dynamically while maintaining the applications connection to the target
network. It allows adaption to the changing environment and may enable optimization with
regards to cost, speed or other network parameters.

Special configurations of type
[UserChoice](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum)
provide a placeholder configuration which is resolved to an actual network configuration
by the platform when a
[session](https://doc.qt.io/archives/qt-5.15/qnetworksession.html) is
[opened](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open). Not all
platforms support the concept of a user choice configuration.

### Configuration States

The list of available configurations can be obtained via
[QNetworkConfigurationManager::allConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#allConfigurations)().
A configuration can have multiple states. The
[Defined](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
configuration state indicates that the configuration is stored on the device. However
the configuration is not yet ready to be activated as e.g. a WLAN may not be available
at the current time.

The
[Discovered](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
state implies that the configuration is
[Defined](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
and the outside conditions are such that the configuration can be used immediately to
open a new network session. An example of such an outside condition may be that the
Ethernet cable is actually connected to the device or that the WLAN with the specified
SSID is in range.

The
[Active](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
state implies that the configuration is
[Discovered](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum).
A configuration in this state is currently being used by an application. The underlying
network interface has a valid IP configuration and can transfer IP packets between the
device and the target network.

The
[Undefined](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
state indicates that the system has knowledge of possible target networks but cannot
actually use that knowledge to connect to it. An example for such a state could be an
encrypted WLAN that has been discovered but the user hasn't actually saved a
configuration including the required password which would allow the device to connect to
it.

Depending on the type of configuration some states are transient in nature. A GPRS/UMTS
connection may almost always be
[Discovered](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
if the GSM/UMTS network is available. However if the GSM/UMTS network loses the
connection the associated configuration may change its state from
[Discovered](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
to
[Defined](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
as well. A similar use case might be triggered by WLAN availability.
[QNetworkConfigurationManager::updateConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateConfigurations)()
can be used to manually trigger updates of states. Note that some platforms do not
require such updates as they implicitly change the state once it has been discovered. If
the state of a configuration changes all related QNetworkConfiguration instances change
their state automatically.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def bearerType(self) -> Any:
        """X.bearerType()

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration::BearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) QNetworkConfiguration::bearerType() const

Returns the type of bearer used by this network configuration.

If the bearer type is
[unknown](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum)
the
[bearerTypeName](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerTypeName)()
function can be used to retrieve a textural type name for the bearer.

An invalid network configuration always returns the
[BearerUnknown](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum)
value.

**See also**
[bearerTypeName](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerTypeName)()
and
[bearerTypeFamily](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerTypeFamily)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bearerType(self) -> PySide2.QtNetwork.QNetworkConfiguration.BearerType
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerType"""
        ...

    def bearerTypeFamily(self) -> Any:
        """X.bearerTypeFamily()

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration::BearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) QNetworkConfiguration::bearerTypeFamily() const

Returns the bearer type family used by this network configuration. The following table
lists how
[bearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerType)()
values map to bearerTypeFamily() values:

| bearer type | bearer type family |
| --- | --- |
| [BearerUnknown](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [Bearer2G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [BearerEthernet](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [BearerWLAN](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [BearerBluetooth](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | (same type) |
| [BearerCDMA2000](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [BearerEVDO](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [BearerWCDMA](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [BearerHSPA](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [Bearer3G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | [Bearer3G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) |
| [BearerWiMAX](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [BearerLTE](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum), [Bearer4G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | [Bearer4G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) |

An invalid network configuration always returns the
[BearerUnknown](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum)
value.

This function was introduced in Qt 5.2.

**See also**
[bearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerType)()
and
[bearerTypeName](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerTypeName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bearerTypeFamily(self) -> PySide2.QtNetwork.QNetworkConfiguration.BearerType
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerTypeFamily"""
        ...

    def bearerTypeName(self) -> str:
        """X.bearerTypeName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkConfiguration::bearerTypeName() const

Returns the type of bearer used by this network configuration as a string.

The string is not translated and therefore cannot be shown to the user. The subsequent
table shows the fixed mappings between
[BearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum)
and the bearer type name for known types. If the
[BearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum)
is unknown this function may return additional information if it is available; otherwise
an empty string will be returned.

| [BearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | Value |
| --- | --- |
| [BearerUnknown](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | The session is based on an unknown or unspecified bearer type. The value of the string returned describes the bearer type. |
| [BearerEthernet](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | Ethernet |
| [BearerWLAN](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | WLAN |
| [Bearer2G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | 2G |
| [Bearer3G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | 3G |
| [Bearer4G](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | 4G |
| [BearerCDMA2000](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | CDMA2000 |
| [BearerWCDMA](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | WCDMA |
| [BearerHSPA](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | HSPA |
| [BearerBluetooth](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | Bluetooth |
| [BearerWiMAX](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | WiMAX |
| [BearerEVDO](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | EVDO |
| [BearerLTE](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#BearerType-enum) | LTE |

This function returns an empty string if this is an invalid configuration, a network
configuration of type
[QNetworkConfiguration::ServiceNetwork](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum)
or
[QNetworkConfiguration::UserChoice](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum).

**See also**
[bearerType](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerType)()
and
[bearerTypeFamily](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerTypeFamily)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bearerTypeName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#bearerTypeName"""
        ...

    def children(self) -> tuple:
        """X.children() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#QNetworkConfiguration)\\> QNetworkConfiguration::children() const

Returns all sub configurations of this network configuration in priority order. The
first sub configuration in the list has the highest priority.

Only network configurations of type
[ServiceNetwork](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum)
can have children. Otherwise this function returns an empty list.

Upstream PySide2 reference signatures (binding differences may apply):

```python
children(self) -> typing.List[PySide2.QtNetwork.QNetworkConfiguration]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#children"""
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

    def identifier(self) -> str:
        """X.identifier() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkConfiguration::identifier() const

Returns the unique and platform specific identifier for this network configuration;
otherwise an empty string.

Upstream PySide2 reference signatures (binding differences may apply):

```python
identifier(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#identifier"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isRoamingAvailable(self) -> bool:
        """X.isRoamingAvailable() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkConfiguration::isRoamingAvailable() const

Returns `true` if this configuration supports roaming; otherwise false.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isRoamingAvailable(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#isRoamingAvailable"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkConfiguration::isValid() const

Returns `true` if this
[QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html)
object is valid. A configuration may become invalid if the user deletes the
configuration or the configuration was default-constructed.

The addition and removal of configurations can be monitored via the
QNetworkConfigurationManager.

**See also**
[QNetworkConfigurationManager](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#isValid"""
        ...

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkConfiguration::name() const

Returns the user visible name of this configuration.

The name may either be the name of the underlying access point or the name for service
network that this configuration represents.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QNetworkConfiguration"""
        ...

    def purpose(self) -> Any:
        """X.purpose()

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration::Purpose](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Purpose-enum) QNetworkConfiguration::purpose() const

Returns the purpose of this configuration.

The purpose field may be used to programmatically determine the purpose of a
configuration. Such information is usually part of the access point or service network
meta data.

Upstream PySide2 reference signatures (binding differences may apply):

```python
purpose(self) -> PySide2.QtNetwork.QNetworkConfiguration.Purpose
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#purpose"""
        ...

    def state(self) -> Any:
        """X.state()

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration::StateFlags](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum) QNetworkConfiguration::state() const

Returns the current state of the configuration.

Upstream PySide2 reference signatures (binding differences may apply):

```python
state(self) -> PySide2.QtNetwork.QNetworkConfiguration.StateFlags
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#state"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkConfiguration::swap([QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#QNetworkConfiguration) \\&*other*)

Swaps this network configuration with *other*. This function is very fast and never
fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#swap"""
        ...

    def type(self) -> Any:
        """X.type()

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration::Type](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum) QNetworkConfiguration::type() const

Returns the type of the configuration.

A configuration can represent a single access point configuration or a set of access
point configurations. Such a set is called service network. A configuration that is
based on a service network can potentially support roaming of network sessions.

Upstream PySide2 reference signatures (binding differences may apply):

```python
type(self) -> PySide2.QtNetwork.QNetworkConfiguration.Type
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#type"""
        ...
    Active: Any
    Bearer2G: Any
    Bearer3G: Any
    Bearer4G: Any
    BearerBluetooth: Any
    BearerCDMA2000: Any
    BearerEVDO: Any
    BearerEthernet: Any
    BearerHSPA: Any
    BearerLTE: Any
    BearerType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BearerUnknown: Any
    BearerWCDMA: Any
    BearerWLAN: Any
    BearerWiMAX: Any
    Defined: Any
    Discovered: Any
    InternetAccessPoint: Any
    Invalid: Any
    PrivatePurpose: Any
    PublicPurpose: Any
    Purpose: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    ServiceNetwork: Any
    ServiceSpecificPurpose: Any
    StateFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    StateFlags: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Type: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Undefined: Any
    UnknownPurpose: Any
    UserChoice: Any

class QNetworkConfigurationManager:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkConfigurationManager provides access to the network configurations known to the
system and enables applications to detect the system capabilities (with regards to
network sessions) at runtime.

A [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html)
abstracts a set of configuration options describing how a network interface has to be
configured to connect to a particular target network. QNetworkConfigurationManager
maintains and updates the global list of QNetworkConfigurations. Applications can access
and filter this list via
[allConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#allConfigurations)().
If a new configuration is added or an existing one is removed or changed the
[configurationAdded](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationAdded)(),
[configurationRemoved](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationRemoved)()
and
[configurationChanged](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationChanged)()
signals are emitted respectively.

The
[defaultConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#defaultConfiguration)()
can be used when intending to immediately create a new network session without caring
about the particular configuration. It returns a
[QNetworkConfiguration::Discovered](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum)
configuration. If there are not any discovered ones an invalid configuration is
returned.

Some configuration updates may require some time to perform updates. A WLAN scan is such
an example. Unless the platform performs internal updates it may be required to manually
trigger configuration updates via
[QNetworkConfigurationManager::updateConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateConfigurations)().
The completion of the update process is indicated by emitting the
[updateCompleted](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateCompleted)()
signal. The update process ensures that every existing
[QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html)
instance is updated. There is no need to ask for a renewed configuration list via
[allConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#allConfigurations)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def allConfigurations(self, arg0: flags) -> tuple:
        """X.allConfigurations(flags) -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html)\\> QNetworkConfigurationManager::allConfigurations([QNetworkConfiguration::StateFlags](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum) *filter* \\= QNetworkConfiguration::StateFlags()) const

Returns the list of configurations which comply with the given *filter*.

By default this function returns all (defined and undefined) configurations.

A wireless network with a particular SSID may only be accessible in a certain area
despite the fact that the system has a valid configuration for it. Therefore the filter
flag may be used to limit the list to discovered and possibly connected configurations
only.

If *filter* is set to zero this function returns all possible configurations.

Note that this function returns the states for all configurations as they are known at
the time of this function call. If for instance a configuration of type WLAN is defined
the system may have to perform a WLAN scan in order to determine whether it is actually
available. To obtain the most accurate state
[updateConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateConfigurations)()
should be used to update each configuration's state. Note that such an update may
require some time. It's completion is signalled by
[updateCompleted](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateCompleted)().
In the absence of a configuration update this function returns the best estimate at the
time of the call. Therefore, if WLAN configurations are of interest, it is recommended
that
[updateConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateConfigurations)()
is called once after
[QNetworkConfigurationManager](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html)
instantiation (WLAN scans are too time consuming to perform in constructor). After this
the data is kept automatically up-to-date as the system reports any changes.

Upstream PySide2 reference signatures (binding differences may apply):

```python
allConfigurations(self, flags: PySide2.QtNetwork.QNetworkConfiguration.StateFlags=...) -> typing.List[PySide2.QtNetwork.QNetworkConfiguration]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#allConfigurations"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def capabilities(self) -> Any:
        """X.capabilities()

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfigurationManager::Capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#Capability-enum) QNetworkConfigurationManager::capabilities() const

Returns the capabilities supported by the current platform.

Upstream PySide2 reference signatures (binding differences may apply):

```python
capabilities(self) -> PySide2.QtNetwork.QNetworkConfigurationManager.Capabilities
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#capabilities"""
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

    def configurationAdded(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkConfigurationManager.configurationAdded; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkConfigurationManager::configurationAdded(const [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html) \\&*config*)

This signal is emitted whenever a new network configuration is added to the system. The
new configuration is specified by *config*.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationAdded"""
        ...

    def configurationChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkConfigurationManager.configurationChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkConfigurationManager::configurationChanged(const [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html) \\&*config*)

This signal is emitted when the
[state](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#state) of *config*
changes.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationChanged"""
        ...

    def configurationFromIdentifier(self, identifier: str) -> Any:
        """X.configurationFromIdentifier(identifier) -> PythonQt.QtNetwork.QNetworkConfiguration

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html) QNetworkConfigurationManager::configurationFromIdentifier(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*identifier*) const

Returns the QNetworkConfiguration for *identifier*; otherwise returns an invalid
QNetworkConfiguration.

**See also**
[QNetworkConfiguration::identifier](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#identifier)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
configurationFromIdentifier(self, identifier: str) -> PySide2.QtNetwork.QNetworkConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationFromIdentifier"""
        ...

    def configurationRemoved(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkConfigurationManager.configurationRemoved; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkConfigurationManager::configurationRemoved(const [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html) \\&*config*)

This signal is emitted when a configuration is about to be removed from the system. The
removed configuration, specified by *config*, is invalid but retains name and
identifier.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationRemoved"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def defaultConfiguration(self) -> Any:
        """X.defaultConfiguration() -> PythonQt.QtNetwork.QNetworkConfiguration

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html) QNetworkConfigurationManager::defaultConfiguration() const

Returns the default configuration to be used. This function always returns a discovered
configuration; otherwise an invalid configuration.

In some cases it may be required to call
[updateConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateConfigurations)()
and wait for the
[updateCompleted](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateCompleted)()
signal before calling this function.

**See also**
[allConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#allConfigurations)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
defaultConfiguration(self) -> PySide2.QtNetwork.QNetworkConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#defaultConfiguration"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkConfigurationManager.destroyed; argument details are not documented."""
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

    def isOnline(self) -> bool:
        """X.isOnline() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkConfigurationManager::isOnline() const

Returns `true` if the system is considered to be connected to another device via an
active network interface; otherwise returns `false`.

This is equivalent to the following code snippet:

```
QNetworkConfigurationManager mgr;
QList<QNetworkConfiguration> activeConfigs = mgr.allConfigurations(QNetworkConfiguration::Active);
if (activeConfigs.count() > 0)
    Q_ASSERT(mgr.isOnline());
else
    Q_ASSERT(!mgr.isOnline());
```

**See also**
[onlineStateChanged](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#onlineStateChanged)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isOnline(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#isOnline"""
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
        """Native PythonQt.QtNetwork.QNetworkConfigurationManager.objectNameChanged; argument details are not documented."""
        ...

    def onlineStateChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkConfigurationManager.onlineStateChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkConfigurationManager::onlineStateChanged(bool *isOnline*)

This signal is emitted when the device changes from online to offline mode or vice
versa. *isOnline* represents the new state of the device.

The state is considered to be online for as long as
[allConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#allConfigurations)([QNetworkConfiguration::Active](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#StateFlag-enum))
returns a list with at least one entry.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#onlineStateChanged"""
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

    def updateCompleted(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkConfigurationManager.updateCompleted; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkConfigurationManager::updateCompleted()

This signal is emitted when the configuration update has been completed. Such an update
can be initiated via
[updateConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateConfigurations)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateCompleted"""
        ...

    def updateConfigurations(self) -> None:
        """X.updateConfigurations()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkConfigurationManager::updateConfigurations()

Initiates an update of all configurations. This may be used to initiate WLAN scans or
other time consuming updates which may be required to obtain the correct state for
configurations.

This call is asynchronous. On completion of this update the
[updateCompleted](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateCompleted)()
signal is emitted. If new configurations are discovered or old ones were removed or
changed the update process may trigger the emission of one or multiple
[configurationAdded](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationAdded)(),
[configurationRemoved](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationRemoved)()
and
[configurationChanged](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#configurationChanged)()
signals.

If a configuration state changes as a result of this update all existing
QNetworkConfiguration instances are updated automatically.

**See also**
[allConfigurations](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#allConfigurations)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
updateConfigurations(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#updateConfigurations"""
        ...
    ApplicationLevelRoaming: Any
    CanStartAndStopInterfaces: Any
    Capabilities: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Capability: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    DataStatistics: Any
    DirectConnectionRouting: Any
    ForcedRoaming: Any
    NetworkSessionRequired: Any
    SystemSessionSupport: Any
    objectName: Any

class QNetworkCookie:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Cookies are small bits of information that stateless protocols like HTTP use to maintain
some persistent information across requests.

A cookie is set by a remote server when it replies to a request and it expects the same
cookie to be sent back when further requests are sent.

QNetworkCookie holds one such cookie as received from the network. A cookie has a name
and a value, but those are opaque to the application (that is, the information stored in
them has no meaning to the application). A cookie has an associated path name and
domain, which indicate when the cookie should be sent again to the server.

A cookie can also have an expiration date, indicating its validity. If the expiration
date is not present, the cookie is considered a "session cookie" and should be discarded
when the application exits (or when its concept of session is over).

QNetworkCookie provides a way of parsing a cookie from the HTTP header format using the
[QNetworkCookie::parseCookies](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#parseCookies)()
function. However, when received in a
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html), the cookie is
already parsed.

This class implements cookies as described by the [initial cookie specification by
Netscape](http://cgi.netscape.com/newsref/std/cookie_spec.html), which is somewhat
similar to the [RFC 2109](http://www.rfc-editor.org/rfc/rfc2109.txt) specification, plus
the ["HttpOnly"
extension](http://msdn.microsoft.com/en-us/library/ms533046(VS.85).aspx). The more
recent [RFC 2965](http://www.rfc-editor.org/rfc/rfc2965.txt) specification (which uses
the Set-Cookie2 header) is not supported.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def domain(self) -> str:
        """X.domain() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkCookie::domain() const

Returns the domain this cookie is associated with. This corresponds to the "domain"
field of the cookie string.

Note that the domain here may start with a dot, which is not a valid hostname. However,
it means this cookie matches all hostnames ending with that domain name.

**See also**
[setDomain](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setDomain)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
domain(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#domain"""
        ...

    def expirationDate(self) -> Any:
        """X.expirationDate() -> PythonQt.QtCore.QDateTime

Supplemental documentation:
Qt 5 reference:

### [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) QNetworkCookie::expirationDate() const

Returns the expiration date for this cookie. If this cookie is a session cookie, the
[QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) returned will not be
valid. If the date is in the past, this cookie has already expired and should not be
sent again back to a remote server.

The expiration date corresponds to the parameters of the "expires" entry in the cookie
string.

**See also**
[isSessionCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isSessionCookie)()
and
[setExpirationDate](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setExpirationDate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
expirationDate(self) -> PySide2.QtCore.QDateTime
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#expirationDate"""
        ...

    def hasSameIdentifier(self, other: Any) -> bool:
        """X.hasSameIdentifier(other) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkCookie::hasSameIdentifier(const [QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#QNetworkCookie) \\&*other*) const

Returns `true` if this cookie has the same identifier tuple as *other*. The identifier
tuple is composed of the name, domain and path.

**See also**
[operator\\=\\=](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#operator-eq-eq)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasSameIdentifier(self, other: PySide2.QtNetwork.QNetworkCookie) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#hasSameIdentifier"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isHttpOnly(self) -> bool:
        """X.isHttpOnly() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkCookie::isHttpOnly() const

Returns `true` if the "HttpOnly" flag is enabled for this cookie.

A cookie that is "HttpOnly" is only set and retrieved by the network requests and
replies; i.e., the HTTP protocol. It is not accessible from scripts running on browsers.

This function was introduced in Qt 4.5.

**See also**
[isSecure](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isSecure)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isHttpOnly(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isHttpOnly"""
        ...

    def isSecure(self) -> bool:
        """X.isSecure() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkCookie::isSecure() const

Returns `true` if the "secure" option was specified in the cookie string, false
otherwise.

Secure cookies may contain private information and should not be resent over unencrypted
connections.

**See also**
[setSecure](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setSecure)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSecure(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isSecure"""
        ...

    def isSessionCookie(self) -> bool:
        """X.isSessionCookie() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkCookie::isSessionCookie() const

Returns `true` if this cookie is a session cookie. A session cookie is a cookie which
has no expiration date, which means it should be discarded when the application's
concept of session is over (usually, when the application exits).

**See also**
[expirationDate](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#expirationDate)()
and
[setExpirationDate](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setExpirationDate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSessionCookie(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isSessionCookie"""
        ...

    def name(self) -> Any:
        """X.name() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QNetworkCookie::name() const

Returns the name of this cookie. The only mandatory field of a cookie is its name,
without which it is not considered valid.

**See also** [setName](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setName)()
and [value](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#value)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#name"""
        ...

    def normalize(self, url: Any) -> None:
        """X.normalize(url)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::normalize(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

This functions normalizes the path and domain of the cookie if they were previously
empty. The *url* parameter is used to determine the correct domain and path.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
normalize(self, url: PySide2.QtCore.QUrl) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#normalize"""
        ...

    def parseCookies(self, cookieString: Any) -> tuple:
        """X.parseCookies(cookieString) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#QNetworkCookie)\\> QNetworkCookie::parseCookies(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*cookieString*)

Parses the cookie string *cookieString* as received from a server response in the
"Set-Cookie:" header. If there's a parsing error, this function returns an empty list.

Since the HTTP header can set more than one cookie at the same time, this function
returns a
[QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html)\\>,
one for each cookie that is parsed.

**See also**
[toRawForm](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#toRawForm)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
parseCookies(cookieString: PySide2.QtCore.QByteArray) -> typing.List[PySide2.QtNetwork.QNetworkCookie]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#parseCookies"""
        ...

    def path(self) -> str:
        """X.path() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkCookie::path() const

Returns the path associated with this cookie. This corresponds to the "path" field of
the cookie string.

**See also**
[setPath](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setPath)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
path(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#path"""
        ...

    def setDomain(self, domain: str) -> None:
        """X.setDomain(domain)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::setDomain(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*domain*)

Sets the domain associated with this cookie to be *domain*.

**See also** [domain](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#domain)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDomain(self, domain: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setDomain"""
        ...

    def setExpirationDate(self, date: Any) -> None:
        """X.setExpirationDate(date)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::setExpirationDate(const [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) \\&*date*)

Sets the expiration date of this cookie to *date*. Setting an invalid expiration date to
this cookie will mean it's a session cookie.

**See also**
[isSessionCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isSessionCookie)()
and
[expirationDate](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#expirationDate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setExpirationDate(self, date: PySide2.QtCore.QDateTime) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setExpirationDate"""
        ...

    def setHttpOnly(self, enable: bool) -> None:
        """X.setHttpOnly(enable)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::setHttpOnly(bool *enable*)

Sets this cookie's "HttpOnly" flag to *enable*.

This function was introduced in Qt 4.5.

**See also**
[isHttpOnly](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isHttpOnly)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHttpOnly(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setHttpOnly"""
        ...

    def setName(self, cookieName: Any) -> None:
        """X.setName(cookieName)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::setName(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*cookieName*)

Sets the name of this cookie to be *cookieName*. Note that setting a cookie name to an
empty [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) will make this
cookie invalid.

**See also** [name](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#name)() and
[value](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#value)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setName(self, cookieName: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setName"""
        ...

    def setPath(self, path: str) -> None:
        """X.setPath(path)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::setPath(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*path*)

Sets the path associated with this cookie to be *path*.

**See also** [path](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#path)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPath(self, path: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setPath"""
        ...

    def setSecure(self, enable: bool) -> None:
        """X.setSecure(enable)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::setSecure(bool *enable*)

Sets the secure flag of this cookie to *enable*.

Secure cookies may contain private information and should not be resent over unencrypted
connections.

**See also**
[isSecure](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#isSecure)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSecure(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setSecure"""
        ...

    def setValue(self, value: Any) -> None:
        """X.setValue(value)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::setValue(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*value*)

Sets the value of this cookie to be *value*.

**See also** [value](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#value)() and
[name](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#name)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setValue(self, value: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setValue"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkCookie::swap([QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#QNetworkCookie) \\&*other*)

Swaps this cookie with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkCookie) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#swap"""
        ...

    def toRawForm(self, form: Any) -> Any:
        """X.toRawForm(form) -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QNetworkCookie::toRawForm([QNetworkCookie::RawForm](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#RawForm-enum) *form* \\= Full) const

Returns the raw form of this
[QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html). The
[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) returned by this
function is suitable for an HTTP header, either in a server response (the Set-Cookie
header) or the client request (the Cookie header). You can choose from one of two
formats, using *form*.

**See also**
[parseCookies](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#parseCookies)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
toRawForm(self, form: PySide2.QtNetwork.QNetworkCookie.RawForm=...) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#toRawForm"""
        ...

    def value(self) -> Any:
        """X.value() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QNetworkCookie::value() const

Returns this cookies value, as specified in the cookie string. Note that a cookie is
still valid if its value is empty.

Cookie name-value pairs are considered opaque to the application: that is, their values
don't mean anything.

**See also**
[setValue](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#setValue)() and
[name](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#name)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
value(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#value"""
        ...
    Full: Any
    NameAndValueOnly: Any
    RawForm: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"

class QNetworkCookieJar:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Cookies are small bits of information that stateless protocols like HTTP use to maintain
some persistent information across requests.

A cookie is set by a remote server when it replies to a request and it expects the same
cookie to be sent back when further requests are sent.

The cookie jar is the object that holds all cookies set in previous requests. Web
browsers save their cookie jars to disk in order to conserve permanent cookies across
invocations of the application.

QNetworkCookieJar does not implement permanent storage: it only keeps the cookies in
memory. Once the QNetworkCookieJar object is deleted, all cookies it held will be
discarded as well. If you want to save the cookies, you should derive from this class
and implement the saving to disk to your own storage format.

This class implements only the basic security recommended by the cookie specifications
and does not implement any cookie acceptance policy (it accepts all cookies set by any
requests). In order to override those rules, you should reimplement the
[cookiesForUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#cookiesForUrl)()
and
[setCookiesFromUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setCookiesFromUrl)()
virtual functions. They are called by
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) and
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
when they detect new cookies and when they require cookies.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def allCookies(self) -> tuple:
        """X.allCookies() -> tuple

Supplemental documentation:
Qt 5 reference:

### `[protected]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html)\\> QNetworkCookieJar::allCookies() const

Returns all cookies stored in this cookie jar. This function is suitable for derived
classes to save cookies to disk, as well as to implement cookie expiration and other
policies.

**See also**
[setAllCookies](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setAllCookies)()
and
[cookiesForUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#cookiesForUrl)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
allCookies(self) -> typing.List[PySide2.QtNetwork.QNetworkCookie]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#allCookies"""
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

    def cookiesForUrl(self, url: Any) -> tuple:
        """X.cookiesForUrl(url) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html)\\> QNetworkCookieJar::cookiesForUrl(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*) const

Returns the cookies to be added to when a request is sent to *url*. This function is
called by the default
[QNetworkAccessManager::createRequest](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#createRequest)(),
which adds the cookies returned by this function to the request being sent.

If more than one cookie with the same name is found, but with differing paths, the one
with longer path is returned before the one with shorter path. In other words, this
function returns cookies sorted decreasingly by path length.

The default
[QNetworkCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html) class
implements only a very basic security policy (it makes sure that the cookies' domain and
path match the reply's). To enhance the security policy with your own algorithms,
override cookiesForUrl().

**See also**
[setCookiesFromUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setCookiesFromUrl)()
and
[QNetworkAccessManager::setCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setCookieJar)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
cookiesForUrl(self, url: PySide2.QtCore.QUrl) -> typing.List[PySide2.QtNetwork.QNetworkCookie]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#cookiesForUrl"""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteCookie(self, cookie: Any) -> bool:
        """X.deleteCookie(cookie) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QNetworkCookieJar::deleteCookie(const [QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html) \\&*cookie*)

Deletes from cookie jar the cookie found to have the same identifier as *cookie*.

Returns `true` if a cookie was deleted, false otherwise.

This function was introduced in Qt 5.0.

**See also**
[QNetworkCookie::hasSameIdentifier](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#hasSameIdentifier)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
deleteCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#deleteCookie"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkCookieJar.destroyed; argument details are not documented."""
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

    def insertCookie(self, cookie: Any) -> bool:
        """X.insertCookie(cookie) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QNetworkCookieJar::insertCookie(const [QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html) \\&*cookie*)

Adds *cookie* to this cookie jar.

Returns `true` if *cookie* was added, false otherwise.

If a cookie with the same identifier already exists in the cookie jar, it will be
overridden.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
insertCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#insertCookie"""
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
        """Native PythonQt.QtNetwork.QNetworkCookieJar.objectNameChanged; argument details are not documented."""
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

    def setAllCookies(self, cookieList: Any) -> None:
        """X.setAllCookies(cookieList)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkCookieJar::setAllCookies(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html)\\> \\&*cookieList*)

Sets the internal list of cookies held by this cookie jar to be *cookieList*. This
function is suitable for derived classes to implement loading cookies from permanent
storage, or their own cookie acceptance policies by reimplementing
[setCookiesFromUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setCookiesFromUrl)().

**See also**
[allCookies](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#allCookies)() and
[setCookiesFromUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setCookiesFromUrl)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAllCookies(self, cookieList: typing.Sequence[PySide2.QtNetwork.QNetworkCookie]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setAllCookies"""
        ...

    def setCookiesFromUrl(self, cookieList: Any, url: Any) -> bool:
        """X.setCookiesFromUrl(cookieList, url) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QNetworkCookieJar::setCookiesFromUrl(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html)\\> \\&*cookieList*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Adds the cookies in the list *cookieList* to this cookie jar. Before being inserted
cookies are normalized.

Returns `true` if one or more cookies are set for *url*, otherwise false.

If a cookie already exists in the cookie jar, it will be overridden by those in
*cookieList*.

The default
[QNetworkCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html) class
implements only a very basic security policy (it makes sure that the cookies' domain and
path match the reply's). To enhance the security policy with your own algorithms,
override setCookiesFromUrl().

Also, [QNetworkCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html)
does not have a maximum cookie jar size. Reimplement this function to discard older
cookies to create room for new ones.

**See also**
[cookiesForUrl](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#cookiesForUrl)(),
[QNetworkAccessManager::setCookieJar](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setCookieJar)(),
and
[QNetworkCookie::normalize](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#normalize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCookiesFromUrl(self, cookieList: typing.Sequence[PySide2.QtNetwork.QNetworkCookie], url: PySide2.QtCore.QUrl) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#setCookiesFromUrl"""
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

    def updateCookie(self, cookie: Any) -> bool:
        """X.updateCookie(cookie) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QNetworkCookieJar::updateCookie(const [QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html) \\&*cookie*)

If a cookie with the same identifier as *cookie* exists in this cookie jar it will be
updated. This function uses
[insertCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#insertCookie)().

Returns `true` if *cookie* was updated, false if no cookie in the jar matches the
identifier of *cookie*.

This function was introduced in Qt 5.0.

**See also**
[QNetworkCookie::hasSameIdentifier](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html#hasSameIdentifier)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
updateCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#updateCookie"""
        ...

    def validateCookie(self, cookie: Any, url: Any) -> bool:
        """X.validateCookie(cookie, url) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` bool QNetworkCookieJar::validateCookie(const [QNetworkCookie](https://doc.qt.io/archives/qt-5.15/qnetworkcookie.html) \\&*cookie*, const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*) const

Returns `true` if the domain and path of *cookie* are valid, false otherwise. The *url*
parameter is used to determine if the domain specified in the cookie is allowed.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
validateCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie, url: PySide2.QtCore.QUrl) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkcookiejar.html#validateCookie"""
        ...
    objectName: Any

class QNetworkDiskCache:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkDiskCache stores each url in its own file inside of the
[cacheDirectory](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#cacheDirectory)
using [QDataStream](https://doc.qt.io/archives/qt-5.15/qdatastream.html). Files with a
text MimeType are compressed using
[qCompress](https://doc.qt.io/archives/qt-5.15/qbytearray.html#qCompress). Data is
written to disk only in
[insert](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#insert)() and
[updateMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#updateMetaData)().

Currently you cannot share the same cache files with more than one disk cache.

QNetworkDiskCache by default limits the amount of space that the cache will use on the
system to 50MB.

Note you have to set the cache directory before it will work.

A network disk cache can be enabled by:

```
QNetworkAccessManager *manager = new QNetworkAccessManager(this);
QNetworkDiskCache *diskCache = new QNetworkDiskCache(this);
diskCache->setCacheDirectory("cacheDir");
manager->setCache(diskCache);
```

When sending requests, to control the preference of when to use the cache and when to
use the network, consider the following:

```
// do a normal request (preferred from network, as this is the default)
QNetworkRequest request(QUrl(QString("http://qt-project.org")));
manager->get(request);

// do a request preferred from cache
QNetworkRequest request2(QUrl(QString("http://qt-project.org")));
request2.setAttribute(QNetworkRequest::CacheLoadControlAttribute, QNetworkRequest::PreferCache);
manager->get(request2);
```

To check whether the response came from the cache or from the network, the following can
be applied:

```
void replyFinished(QNetworkReply *reply) {
    QVariant fromCache = reply->attribute(QNetworkRequest::SourceIsFromCacheAttribute);
    qDebug() << "page from cache?" << fromCache.toBool();
}
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def cacheDirectory(self) -> str:
        """X.cacheDirectory() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkDiskCache::cacheDirectory() const

Returns the location where cached files will be stored.

**See also**
[setCacheDirectory](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#setCacheDirectory)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
cacheDirectory(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#cacheDirectory"""
        ...

    def cacheSize(self) -> int:
        """X.cacheSize() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QNetworkDiskCache::cacheSize() const

Reimplements:
[QAbstractNetworkCache::cacheSize](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#cacheSize)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
cacheSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#cacheSize"""
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

    def clear(self) -> None:
        """X.clear()

Supplemental documentation:
Qt 5 reference:

### `[override virtual slot]` void QNetworkDiskCache::clear()

Reimplements:
[QAbstractNetworkCache::clear](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#clear)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
clear(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#clear"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def data(self, url: Any) -> Any:
        """X.data(url) -> PythonQt.QtCore.QIODevice

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\*QNetworkDiskCache::data(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Reimplements:
[QAbstractNetworkCache::data](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#data)(const
QUrl \\&url).

Upstream PySide2 reference signatures (binding differences may apply):

```python
data(self, url: PySide2.QtCore.QUrl) -> PySide2.QtCore.QIODevice
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#data"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkDiskCache.destroyed; argument details are not documented."""
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

    def expire(self) -> int:
        """X.expire() -> int

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QNetworkDiskCache::expire()

Cleans the cache so that its size is under the maximum cache size. Returns the current
size of the cache.

When the current size of the cache is greater than the
[maximumCacheSize](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#maximumCacheSize)()
older cache files are removed until the total size is less then 90% of
[maximumCacheSize](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#maximumCacheSize)()
starting with the oldest ones first using the file creation date to determine how old a
cache file is.

Subclasses can reimplement this function to change the order that cache files are
removed taking into account information in the application knows about that
[QNetworkDiskCache](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html) does not,
for example the number of times a cache is accessed.

**Note:**
[cacheSize](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#cacheSize)() calls
expire if the current cache size is unknown.

**See also**
[maximumCacheSize](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#maximumCacheSize)()
and
[fileMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#fileMetaData)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
expire(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#expire"""
        ...

    def fileMetaData(self, fileName: str) -> Any:
        """X.fileMetaData(fileName) -> PythonQt.QtNetwork.QNetworkCacheMetaData

Supplemental documentation:
Qt 5 reference:

### [QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html) QNetworkDiskCache::fileMetaData(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*fileName*) const

Returns the
[QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html)
for the cache file *fileName*.

If *fileName* is not a cache file
[QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html)
will be invalid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
fileMetaData(self, fileName: str) -> PySide2.QtNetwork.QNetworkCacheMetaData
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#fileMetaData"""
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

    def insert(self, device: Any) -> None:
        """X.insert(device)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QNetworkDiskCache::insert([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*)

Reimplements:
[QAbstractNetworkCache::insert](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#insert)(QIODevice
\\*device).

Upstream PySide2 reference signatures (binding differences may apply):

```python
insert(self, device: PySide2.QtCore.QIODevice) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#insert"""
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

    def maximumCacheSize(self) -> int:
        """X.maximumCacheSize() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QNetworkDiskCache::maximumCacheSize() const

Returns the current maximum size for the disk cache.

**See also**
[setMaximumCacheSize](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#setMaximumCacheSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
maximumCacheSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#maximumCacheSize"""
        ...

    def metaData(self, url: Any) -> Any:
        """X.metaData(url) -> PythonQt.QtNetwork.QNetworkCacheMetaData

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html) QNetworkDiskCache::metaData(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Reimplements:
[QAbstractNetworkCache::metaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#metaData)(const
QUrl \\&url).

Upstream PySide2 reference signatures (binding differences may apply):

```python
metaData(self, url: PySide2.QtCore.QUrl) -> PySide2.QtNetwork.QNetworkCacheMetaData
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#metaData"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkDiskCache.objectNameChanged; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def prepare(self, metaData: Any) -> Any:
        """X.prepare(metaData) -> PythonQt.QtCore.QIODevice

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\*QNetworkDiskCache::prepare(const [QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html) \\&*metaData*)

Reimplements:
[QAbstractNetworkCache::prepare](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#prepare)(const
QNetworkCacheMetaData \\&metaData).

Upstream PySide2 reference signatures (binding differences may apply):

```python
prepare(self, metaData: PySide2.QtNetwork.QNetworkCacheMetaData) -> PySide2.QtCore.QIODevice
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#prepare"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def remove(self, url: Any) -> bool:
        """X.remove(url) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QNetworkDiskCache::remove(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Reimplements:
[QAbstractNetworkCache::remove](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#remove)(const
QUrl \\&url).

Upstream PySide2 reference signatures (binding differences may apply):

```python
remove(self, url: PySide2.QtCore.QUrl) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#remove"""
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

    def setCacheDirectory(self, cacheDir: str) -> None:
        """X.setCacheDirectory(cacheDir)

Supplemental documentation:
Qt 5 reference:

### void QNetworkDiskCache::setCacheDirectory(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*cacheDir*)

Sets the directory where cached files will be stored to *cacheDir*

[QNetworkDiskCache](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html) will
create this directory if it does not exists.

Prepared cache items will be stored in the new cache directory when they are inserted.

**See also**
[cacheDirectory](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#cacheDirectory)()
and
[QDesktopServices::CacheLocation](https://doc.qt.io/archives/qt-5.15/qdesktopservices-obsolete.html#StandardLocation-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCacheDirectory(self, cacheDir: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#setCacheDirectory"""
        ...

    def setMaximumCacheSize(self, size: int) -> None:
        """X.setMaximumCacheSize(size)

Supplemental documentation:
Qt 5 reference:

### void QNetworkDiskCache::setMaximumCacheSize([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *size*)

Sets the maximum size of the disk cache to be *size*.

If the new size is smaller then the current cache size then the cache will call
[expire](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#expire)().

**See also**
[maximumCacheSize](https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#maximumCacheSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMaximumCacheSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#setMaximumCacheSize"""
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

    def updateMetaData(self, metaData: Any) -> None:
        """X.updateMetaData(metaData)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QNetworkDiskCache::updateMetaData(const [QNetworkCacheMetaData](https://doc.qt.io/archives/qt-5.15/qnetworkcachemetadata.html) \\&*metaData*)

Reimplements:
[QAbstractNetworkCache::updateMetaData](https://doc.qt.io/archives/qt-5.15/qabstractnetworkcache.html#updateMetaData)(const
QNetworkCacheMetaData \\&metaData).

Upstream PySide2 reference signatures (binding differences may apply):

```python
updateMetaData(self, metaData: PySide2.QtNetwork.QNetworkCacheMetaData) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkdiskcache.html#updateMetaData"""
        ...
    objectName: Any

class QNetworkInterface:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkInterface represents one network interface attached to the host where the
program is being run. Each network interface may contain zero or more IP addresses, each
of which is optionally associated with a netmask and/or a broadcast address. The list of
such trios can be obtained with
[addressEntries](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#addressEntries)().
Alternatively, when the netmask or the broadcast addresses or other information aren't
necessary, use the
[allAddresses](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#allAddresses)()
convenience function to obtain just the IP addresses of the active interfaces.

QNetworkInterface also reports the interface's hardware address with
[hardwareAddress](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#hardwareAddress)().

Not all operating systems support reporting all features. Only the IPv4 addresses are
guaranteed to be listed by this class in all platforms. In particular, IPv6 address
listing is only supported on Windows, Linux, macOS and the BSDs.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addressEntries(self) -> tuple:
        """X.addressEntries() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkAddressEntry](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html)\\> QNetworkInterface::addressEntries() const

Returns the list of IP addresses that this interface possesses along with their
associated netmasks and broadcast addresses.

If the netmask or broadcast address or other information is not necessary, you can call
the
[allAddresses](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#allAddresses)()
function to obtain just the IP addresses of the active interfaces.

Upstream PySide2 reference signatures (binding differences may apply):

```python
addressEntries(self) -> typing.List[PySide2.QtNetwork.QNetworkAddressEntry]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#addressEntries"""
        ...

    def allAddresses(self) -> tuple:
        """X.allAddresses() -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html)\\> QNetworkInterface::allAddresses()

This convenience function returns all IP addresses found on the host machine. It is
equivalent to calling
[addressEntries](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#addressEntries)()
on all the objects returned by
[allInterfaces](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#allInterfaces)()
that are in the
[QNetworkInterface::IsUp](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#InterfaceFlag-enum)
state to obtain lists of
[QNetworkAddressEntry](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html)
objects then calling
[QNetworkAddressEntry::ip](https://doc.qt.io/archives/qt-5.15/qnetworkaddressentry.html#ip)()
on each of these.

Upstream PySide2 reference signatures (binding differences may apply):

```python
allAddresses() -> typing.List[PySide2.QtNetwork.QHostAddress]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#allAddresses"""
        ...

    def allInterfaces(self) -> tuple:
        """X.allInterfaces() -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#QNetworkInterface)\\> QNetworkInterface::allInterfaces()

Returns a listing of all the network interfaces found on the host machine. In case of
failure it returns a list with zero elements.

Upstream PySide2 reference signatures (binding differences may apply):

```python
allInterfaces() -> typing.List[PySide2.QtNetwork.QNetworkInterface]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#allInterfaces"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def flags(self) -> Any:
        """X.flags()

Supplemental documentation:
Qt 5 reference:

### [QNetworkInterface::InterfaceFlags](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#InterfaceFlag-enum) QNetworkInterface::flags() const

Returns the flags associated with this network interface.

Upstream PySide2 reference signatures (binding differences may apply):

```python
flags(self) -> PySide2.QtNetwork.QNetworkInterface.InterfaceFlags
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#flags"""
        ...

    def hardwareAddress(self) -> str:
        """X.hardwareAddress() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkInterface::hardwareAddress() const

Returns the low-level hardware address for this interface. On Ethernet interfaces, this
will be a MAC address in string representation, separated by colons.

Other interface types may have other types of hardware addresses. Implementations should
not depend on this function returning a valid MAC address.

**See also** [type](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#type)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hardwareAddress(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#hardwareAddress"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def humanReadableName(self) -> str:
        """X.humanReadableName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkInterface::humanReadableName() const

Returns the human-readable name of this network interface on Windows, such as "Local
Area Connection", if the name could be determined. If it couldn't, this function returns
the same as [name](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#name)().
The human-readable name is a name that the user can modify in the Windows Control Panel,
so it may change during the execution of the program.

On Unix, this function currently always returns the same as
[name](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#name)(), since Unix
systems don't store a configuration for human-readable names.

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
humanReadableName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#humanReadableName"""
        ...

    def index(self) -> int:
        """X.index() -> int

Supplemental documentation:
Qt 5 reference:

### int QNetworkInterface::index() const

Returns the interface system index, if known. This is an integer assigned by the
operating system to identify this interface and it generally doesn't change. It matches
the scope ID field in IPv6 addresses.

If the index isn't known, this function returns 0\\.

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
index(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#index"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def interfaceFromIndex(self, index: int) -> Any:
        """X.interfaceFromIndex(index) -> PythonQt.QtNetwork.QNetworkInterface

Supplemental documentation:
Qt 5 reference:

### `[static]` [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#QNetworkInterface) QNetworkInterface::interfaceFromIndex(int *index*)

Returns a [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html)
object for the interface whose internal ID is *index*. Network interfaces have a unique
identifier called the "interface index" to distinguish it from other interfaces on the
system. Often, this value is assigned progressively and interfaces being removed and
then added again get a different value every time.

This index is also found in the IPv6 address' scope ID field.

Upstream PySide2 reference signatures (binding differences may apply):

```python
interfaceFromIndex(index: int) -> PySide2.QtNetwork.QNetworkInterface
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#interfaceFromIndex"""
        ...

    def interfaceFromName(self, name: str) -> Any:
        """X.interfaceFromName(name) -> PythonQt.QtNetwork.QNetworkInterface

Supplemental documentation:
Qt 5 reference:

### `[static]` [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#QNetworkInterface) QNetworkInterface::interfaceFromName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Returns a [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html)
object for the interface named *name*. If no such interface exists, this function
returns an invalid
[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) object.

The string *name* may be either an actual interface name (such as "eth0" or "en1") or an
interface index in string form ("1", "2", etc.).

**See also** [name](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#name)()
and [isValid](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#isValid)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
interfaceFromName(name: str) -> PySide2.QtNetwork.QNetworkInterface
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#interfaceFromName"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkInterface::isValid() const

Returns `true` if this
[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) object
contains valid information about a network interface.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#isValid"""
        ...

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkInterface::name() const

Returns the name of this network interface. On Unix systems, this is a string containing
the type of the interface and optionally a sequence number, such as "eth0", "lo" or
"pcn0". On Windows, it's an internal ID that cannot be changed by the user.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#name"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkInterface::swap([QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#QNetworkInterface) \\&*other*)

Swaps this network interface instance with *other*. This function is very fast and never
fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkInterface) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html#swap"""
        ...
    CanBroadcast: Any
    CanMulticast: Any
    InterfaceFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    InterfaceFlags: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    IsLoopBack: Any
    IsPointToPoint: Any
    IsRunning: Any
    IsUp: Any

class QNetworkProxy:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkProxy provides the method for configuring network layer proxy support to the Qt
network classes. The currently supported classes are
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html),
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html),
[QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html),
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html) and
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).
The proxy support is designed to be as transparent as possible. This means that existing
network-enabled applications that you have written should automatically support network
proxy using the following code.

```
QNetworkProxy proxy;
proxy.setType(QNetworkProxy::Socks5Proxy);
proxy.setHostName("proxy.example.com");
proxy.setPort(1080);
proxy.setUser("username");
proxy.setPassword("password");
QNetworkProxy::setApplicationProxy(proxy);
```

An alternative to setting an application wide proxy is to specify the proxy for
individual sockets using
[QAbstractSocket::setProxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setProxy)()
and
[QTcpServer::setProxy](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setProxy)().
In this way, it is possible to disable the use of a proxy for specific sockets using the
following code:

```
serverSocket->setProxy(QNetworkProxy::NoProxy);
```

Network proxy is not used if the address used in
[connectToHost()](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost),
[bind()](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind) or
[listen()](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen) is equivalent to
[QHostAddress::LocalHost](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum)
or
[QHostAddress::LocalHostIPv6](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum).

Each type of proxy support has certain restrictions associated with it. You should read
the [ProxyType](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
documentation carefully before selecting a proxy type to use.

**Note:** Changes made to currently connected sockets do not take effect. If you need to
change a connected socket, you should reconnect it.

### SOCKS5

The SOCKS5 support since Qt 4 is based on [RFC
1928](http://www.rfc-editor.org/rfc/rfc1928.txt) and [RFC
1929](http://www.rfc-editor.org/rfc/rfc1929.txt). The supported authentication methods
are no authentication and username/password authentication. Both IPv4 and IPv6 are
supported. Domain names are resolved through the SOCKS5 server if the
[QNetworkProxy::HostNameLookupCapability](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#Capability-enum)
is enabled, otherwise they are resolved locally and the IP address is sent to the
server. There are several things to remember when using SOCKS5 with
[QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html) and
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html):

With [QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html), a call to
[bind()](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind) may fail with a
timeout error. If a port number other than 0 is passed to
[bind()](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind), it is not
guaranteed that it is the specified port that will be used. Use
[localPort()](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localPort) and
[localAddress()](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#localAddress)
to get the actual address and port number in use. Because proxied UDP goes through two
UDP connections, it is more likely that packets will be dropped.

With [QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html) a call to
[listen()](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen) may fail with a
timeout error. If a port number other than 0 is passed to
[listen()](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen), then it is not
guaranteed that it is the specified port that will be used. Use
[serverPort()](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverPort) and
[serverAddress()](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverAddress) to
get the actual address and port used to listen for connections. SOCKS5 only supports one
accepted connection per call to
[listen()](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen), and each call is
likely to result in a different
[serverPort()](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverPort) being
used.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def applicationProxy(self) -> Any:
        """X.applicationProxy() -> PythonQt.QtNetwork.QNetworkProxy

Supplemental documentation:
Qt 5 reference:

### `[static]` [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#QNetworkProxy) QNetworkProxy::applicationProxy()

Returns the application level network proxying.

If a [QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) or
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) has the
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
type, then the [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html)
returned by this function is used.

**See also**
[QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html),
[setApplicationProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setApplicationProxy)(),
[QAbstractSocket::proxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#proxy)(),
and [QTcpServer::proxy](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#proxy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
applicationProxy() -> PySide2.QtNetwork.QNetworkProxy
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#applicationProxy"""
        ...

    def capabilities(self) -> Any:
        """X.capabilities()

Supplemental documentation:
Qt 5 reference:

### [QNetworkProxy::Capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#Capability-enum) QNetworkProxy::capabilities() const

Returns the capabilities of this proxy server.

This function was introduced in Qt 4.5.

**See also**
[setCapabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setCapabilities)()
and [type](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#type)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
capabilities(self) -> PySide2.QtNetwork.QNetworkProxy.Capabilities
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#capabilities"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def hasRawHeader(self, headerName: Any) -> bool:
        """X.hasRawHeader(headerName) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkProxy::hasRawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*) const

Returns `true` if the raw header *headerName* is in use for this proxy. Returns `false`
if the proxy is not of type
[HttpProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum) or
[HttpCachingProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum).

This function was introduced in Qt 5.0.

**See also**
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#rawHeader)() and
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setRawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasRawHeader(self, headerName: PySide2.QtCore.QByteArray) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hasRawHeader"""
        ...

    def header(self, header: Any) -> Any:
        """X.header(header) -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QNetworkProxy::header([QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum) *header*) const

Returns the value of the known network header *header* if it is in use for this proxy.
If it is not present, returns QVariant() (i.e., an invalid variant).

This function was introduced in Qt 5.0.

**See also**
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#rawHeader)(), and
[setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
header(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#header"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hostName(self) -> str:
        """X.hostName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkProxy::hostName() const

Returns the host name of the proxy host.

**See also**
[setHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHostName)(),
[setPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPort)(), and
[port](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#port)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hostName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hostName"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isCachingProxy(self) -> bool:
        """X.isCachingProxy() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkProxy::isCachingProxy() const

Returns `true` if this proxy supports the
[QNetworkProxy::CachingCapability](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#Capability-enum)
capability.

In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5 it is possible to
remove the capability of caching from a proxy by calling
[setCapabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setCapabilities)().

This function was introduced in Qt 4.4.

**See also**
[capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#capabilities)(),
[type](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#type)(), and
[isTransparentProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#isTransparentProxy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isCachingProxy(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#isCachingProxy"""
        ...

    def isTransparentProxy(self) -> bool:
        """X.isTransparentProxy() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkProxy::isTransparentProxy() const

Returns `true` if this proxy supports transparent tunneling of TCP connections. This
matches the
[QNetworkProxy::TunnelingCapability](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#Capability-enum)
capability.

In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5 it is possible to
remove the capability of caching from a proxy by calling
[setCapabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setCapabilities)().

This function was introduced in Qt 4.4.

**See also**
[capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#capabilities)(),
[type](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#type)(), and
[isCachingProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#isCachingProxy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isTransparentProxy(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#isTransparentProxy"""
        ...

    def password(self) -> str:
        """X.password() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkProxy::password() const

Returns the password used for authentication.

**See also** [user](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#user)(),
[setPassword](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPassword)(), and
[setUser](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setUser)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
password(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#password"""
        ...

    def port(self) -> int:
        """X.port() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QNetworkProxy::port() const

Returns the port of the proxy host.

**See also**
[setHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHostName)(),
[setPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPort)(), and
[hostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hostName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
port(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#port"""
        ...

    def rawHeader(self, headerName: Any) -> Any:
        """X.rawHeader(headerName) -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QNetworkProxy::rawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*) const

Returns the raw form of header *headerName*. If no such header is present or the proxy
is not of type
[HttpProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum) or
[HttpCachingProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum),
an empty [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) is returned,
which may be indistinguishable from a header that is present but has no content (use
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hasRawHeader)() to
find out if the header exists or not).

Raw headers can be set with
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setRawHeader)() or
with [setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHeader)().

This function was introduced in Qt 5.0.

**See also** [header](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#header)()
and
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setRawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeader(self, headerName: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#rawHeader"""
        ...

    def rawHeaderList(self) -> Any:
        """X.rawHeaderList()

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> QNetworkProxy::rawHeaderList() const

Returns a list of all raw headers that are set in this network proxy. The list is in the
order that the headers were set.

If the proxy is not of type
[HttpProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum) or
[HttpCachingProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
an empty [QList](https://doc.qt.io/archives/qt-5.15/qlist.html) is returned.

This function was introduced in Qt 5.0.

**See also**
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hasRawHeader)() and
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#rawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeaderList(self) -> typing.List[PySide2.QtCore.QByteArray]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#rawHeaderList"""
        ...

    def setApplicationProxy(self, proxy: Any) -> None:
        """X.setApplicationProxy(proxy)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QNetworkProxy::setApplicationProxy(const [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#QNetworkProxy) \\&*networkProxy*)

Sets the application level network proxying to be *networkProxy*.

If a [QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) or
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) has the
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
type, then the [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html)
set with this function is used. If you want more flexibility in determining which proxy
is used, use the
[QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html)
class.

Setting a default proxy value with this function will override the application proxy
factory set with
[QNetworkProxyFactory::setApplicationProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#setApplicationProxyFactory),
and disable the use of a system proxy.

**See also**
[QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html),
[applicationProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#applicationProxy)(),
[QAbstractSocket::setProxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setProxy)(),
and
[QTcpServer::setProxy](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setProxy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setApplicationProxy(proxy: PySide2.QtNetwork.QNetworkProxy) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setApplicationProxy"""
        ...

    def setCapabilities(self, capab: Any) -> None:
        """X.setCapabilities(capab)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setCapabilities([QNetworkProxy::Capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#Capability-enum) *capabilities*)

Sets the capabilities of this proxy to *capabilities*.

This function was introduced in Qt 4.5.

**See also** [setType](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setType)()
and
[capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#capabilities)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCapabilities(self, capab: PySide2.QtNetwork.QNetworkProxy.Capabilities) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setCapabilities"""
        ...

    def setHeader(self, header: Any, value: Any) -> None:
        """X.setHeader(header, value)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setHeader([QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum) *header*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the value of the known header *header* to be *value*, overriding any previously set
headers. This operation also sets the equivalent raw HTTP header.

If the proxy is not of type
[HttpProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum) or
[HttpCachingProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
this has no effect.

This function was introduced in Qt 5.0.

**See also**
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setRawHeader)(),
and [header](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#header)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHeader(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHeader"""
        ...

    def setHostName(self, hostName: str) -> None:
        """X.setHostName(hostName)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setHostName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*)

Sets the host name of the proxy host to be *hostName*.

**See also**
[hostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hostName)(),
[setPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPort)(), and
[port](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#port)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHostName(self, hostName: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHostName"""
        ...

    def setPassword(self, password: str) -> None:
        """X.setPassword(password)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setPassword(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*password*)

Sets the password for proxy authentication to be *password*.

**See also** [user](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#user)(),
[setUser](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setUser)(), and
[password](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#password)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPassword(self, password: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPassword"""
        ...

    def setPort(self, port: int) -> None:
        """X.setPort(port)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setPort([quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*)

Sets the port of the proxy host to be *port*.

**See also**
[hostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hostName)(),
[setHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHostName)(), and
[port](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#port)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPort(self, port: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPort"""
        ...

    def setRawHeader(self, headerName: Any, value: Any) -> None:
        """X.setRawHeader(headerName, value)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setRawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerValue*)

Sets the header *headerName* to be of value *headerValue*. If *headerName* corresponds
to a known header (see
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum)),
the raw format will be parsed and the corresponding "cooked" header will be set as well.

For example:

```
request.setRawHeader(QByteArray("Last-Modified"), QByteArray("Sun, 06 Nov 1994 08:49:37 GMT"));
```

will also set the known header LastModifiedHeader to be the
[QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) object of the parsed
date.

**Note:** Setting the same header twice overrides the previous setting. To accomplish
the behaviour of multiple HTTP headers of the same name, you should concatenate the two
values, separating them with a comma (",") and set one single raw header.

If the proxy is not of type
[HttpProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum) or
[HttpCachingProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
this has no effect.

This function was introduced in Qt 5.0.

**See also**
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setHeader)(),
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#hasRawHeader)(),
and [rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#rawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRawHeader(self, headerName: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setRawHeader"""
        ...

    def setType(self, type: Any) -> None:
        """X.setType(type)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setType([QNetworkProxy::ProxyType](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum) *type*)

Sets the proxy type for this instance to be *type*.

Note that changing the type of a proxy does not change the set of capabilities this
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) object holds if
any capabilities have been set with
[setCapabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setCapabilities)().

**See also** [type](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#type)() and
[setCapabilities](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setCapabilities)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setType(self, type: PySide2.QtNetwork.QNetworkProxy.ProxyType) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setType"""
        ...

    def setUser(self, userName: str) -> None:
        """X.setUser(userName)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::setUser(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*user*)

Sets the user name for proxy authentication to be *user*.

**See also** [user](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#user)(),
[setPassword](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPassword)(), and
[password](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#password)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUser(self, userName: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setUser"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxy::swap([QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#QNetworkProxy) \\&*other*)

Swaps this network proxy instance with *other*. This function is very fast and never
fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkProxy) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#swap"""
        ...

    def type(self) -> Any:
        """X.type()

Supplemental documentation:
Qt 5 reference:

### [QNetworkProxy::ProxyType](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum) QNetworkProxy::type() const

Returns the proxy type for this instance.

**See also** [setType](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setType)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
type(self) -> PySide2.QtNetwork.QNetworkProxy.ProxyType
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#type"""
        ...

    def user(self) -> str:
        """X.user() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkProxy::user() const

Returns the user name used for authentication.

**See also** [setUser](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setUser)(),
[setPassword](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setPassword)(), and
[password](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#password)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
user(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#user"""
        ...
    CachingCapability: Any
    Capabilities: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Capability: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    DefaultProxy: Any
    FtpCachingProxy: Any
    HostNameLookupCapability: Any
    HttpCachingProxy: Any
    HttpProxy: Any
    ListeningCapability: Any
    NoProxy: Any
    ProxyType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Socks5Proxy: Any
    TunnelingCapability: Any
    UdpTunnelingCapability: Any

class QNetworkProxyFactory:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkProxyFactory is an extension to
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html), allowing
applications to have a more fine-grained control over which proxy servers are used,
depending on the socket requesting the proxy. This allows an application to apply
different settings, according to the protocol or destination hostname, for instance.

QNetworkProxyFactory can be set globally for an application, in which case it will
override any global proxies set with
[QNetworkProxy::setApplicationProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setApplicationProxy)().
If set globally, any sockets created with Qt will query the factory to determine the
proxy to be used.

A factory can also be set in certain frameworks that support multiple connections, such
as
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).
When set on such object, the factory will be queried for sockets created by that
framework only.

### System Proxies

You can configure a factory to use the system proxy's settings. Call the
[setUseSystemConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#setUseSystemConfiguration)()
function with true to enable this behavior, or false to disable it.

Similarly, you can use a factory to make queries directly to the system proxy by calling
its
[systemProxyForQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#systemProxyForQuery)()
function.

**Warning:** Depending on the configuration of the user's system, the use of system
proxy features on certain platforms may be subject to limitations. The
[systemProxyForQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#systemProxyForQuery)()
documentation contains a list of these limitations for those platforms that are
affected.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html"""

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

    def proxyForQuery(self, query: Any) -> tuple:
        """X.proxyForQuery(query) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html)\\> QNetworkProxyFactory::proxyForQuery(const [QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html) \\&*query*)

This function takes the query request, *query*, examines the details of the type of
socket or request and returns a list of
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) objects that
indicate the proxy servers to be used, in order of preference.

Upstream PySide2 reference signatures (binding differences may apply):

```python
proxyForQuery(query: PySide2.QtNetwork.QNetworkProxyQuery) -> typing.List[PySide2.QtNetwork.QNetworkProxy]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#proxyForQuery"""
        ...

    def queryProxy(self, query: Any) -> tuple:
        """X.queryProxy(query) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[pure virtual]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html)\\> QNetworkProxyFactory::queryProxy(const [QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html) \\&*query* \\= QNetworkProxyQuery())

This function takes the query request, *query*, examines the details of the type of
socket or request and returns a list of
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) objects that
indicate the proxy servers to be used, in order of preference.

When reimplementing this class, take care to return at least one element.

If you cannot determine a better proxy alternative, use
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum),
which tells the code querying for a proxy to use a higher alternative. For example, if
this factory is set to a
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
object, DefaultProxy will tell it to query the application-level proxy settings.

If this factory is set as the application proxy factory, DefaultProxy and NoProxy will
have the same meaning.

Upstream PySide2 reference signatures (binding differences may apply):

```python
queryProxy(self, query: PySide2.QtNetwork.QNetworkProxyQuery=...) -> typing.List[PySide2.QtNetwork.QNetworkProxy]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#queryProxy"""
        ...

    def setApplicationProxyFactory(self, factory: Any) -> None:
        """X.setApplicationProxyFactory(factory)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QNetworkProxyFactory::setApplicationProxyFactory([QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#QNetworkProxyFactory) \\**factory*)

Sets the application-wide proxy factory to be *factory*. This function will take
ownership of that object and will delete it when necessary.

The application-wide proxy is used as a last-resort when all other proxy selection
requests returned
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum).
For example, [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) objects
can have a proxy set with
[QTcpSocket::setProxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setProxy),
but if none is set, the proxy factory class set with this function will be queried.

If you set a proxy factory with this function, any application level proxies set with
[QNetworkProxy::setApplicationProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setApplicationProxy)
will be overridden, and
[usesSystemConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#usesSystemConfiguration)()
will return `false`.

**See also**
[QNetworkProxy::setApplicationProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#setApplicationProxy)(),
[QAbstractSocket::proxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#proxy)(),
and
[QAbstractSocket::setProxy](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setProxy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setApplicationProxyFactory(factory: PySide2.QtNetwork.QNetworkProxyFactory) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#setApplicationProxyFactory"""
        ...

    def setUseSystemConfiguration(self, enable: bool) -> None:
        """X.setUseSystemConfiguration(enable)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QNetworkProxyFactory::setUseSystemConfiguration(bool *enable*)

Enables the use of the platform-specific proxy settings, and only those. See
[systemProxyForQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#systemProxyForQuery)()
for more information.

Calling this function with *enable* set to `true` resets any proxy or
[QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html)
that is already set.

**Note:** See the
[systemProxyForQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#systemProxyForQuery)()
documentation for a list of limitations related to the use of system proxies.

This function was introduced in Qt 4.6.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUseSystemConfiguration(enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#setUseSystemConfiguration"""
        ...

    def systemProxyForQuery(self, query: Any) -> tuple:
        """X.systemProxyForQuery(query) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html)\\> QNetworkProxyFactory::systemProxyForQuery(const [QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html) \\&*query* \\= QNetworkProxyQuery())

This function takes the query request, *query*, examines the details of the type of
socket or request and returns a list of
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) objects that
indicate the proxy servers to be used, in order of preference.

This function can be used to determine the platform-specific proxy settings. This
function will use the libraries provided by the operating system to determine the proxy
for a given connection, if such libraries exist. If they don't, this function will just
return a [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) of type
[QNetworkProxy::NoProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum).

On Windows, this function will use the WinHTTP DLL functions. Despite its name,
Microsoft suggests using it for all applications that require network connections, not
just HTTP. This will respect the proxy settings set on the registry with the
proxycfg.exe tool. If those settings are not found, this function will attempt to obtain
Internet Explorer's settings and use them.

On macOS, this function will obtain the proxy settings using the SystemConfiguration
framework from Apple. It will apply the FTP, HTTP and HTTPS proxy configurations for
queries that contain the protocol tag "ftp", "http" and "https", respectively. If the
SOCKS proxy is enabled in that configuration, this function will use the SOCKS server
for all queries. If SOCKS isn't enabled, it will use the HTTPS proxy for all TcpSocket
and UrlRequest queries.

On other systems, this function will pick up proxy settings from the "http\\_proxy"
environment variable. This variable must be a URL using one of the following schemes:
"http", "socks5" or "socks5h".



#### Limitations

These are the limitations for the current version of this function. Future versions of
Qt may lift some of the limitations listed here.

- On macOS, this function will ignore the Proxy Auto Configuration settings, since it cannot execute the associated ECMAScript code.
- On Windows platforms, this function may take several seconds to execute depending on the configuration of the user's system.

Upstream PySide2 reference signatures (binding differences may apply):

```python
systemProxyForQuery(query: PySide2.QtNetwork.QNetworkProxyQuery=...) -> typing.List[PySide2.QtNetwork.QNetworkProxy]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html#systemProxyForQuery"""
        ...

class QNetworkProxyQuery:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkProxyQuery holds the details of a socket being created or request being made. It
is used by [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) and
[QNetworkProxyFactory](https://doc.qt.io/archives/qt-5.15/qnetworkproxyfactory.html) to
allow applications to have a more fine-grained control over which proxy servers are
used, depending on the details of the query. This allows an application to apply
different settings, according to the protocol or destination hostname, for instance.

QNetworkProxyQuery supports the following criteria for selecting the proxy:

- the type of query
- the local port number to use
- the destination host name
- the destination port number
- the protocol name, such as "http" or "ftp"
- the URL being requested

The destination host name is the host in the connection in the case of outgoing
connection sockets. It is the `hostName` parameter passed to
[QTcpSocket::connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
or the host component of a URL requested with
[QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html).

The destination port number is the requested port to connect to in the case of outgoing
sockets, while the local port number is the port the socket wishes to use locally before
attempting the external connection. In most cases, the local port number is used by
listening sockets only
([QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html)) or by datagram
sockets ([QUdpSocket](https://doc.qt.io/archives/qt-5.15/qudpsocket.html)).

The protocol name is an arbitrary string that indicates the type of connection being
attempted. For example, it can match the scheme of a URL, like "http", "https" and
"ftp". In most cases, the proxy selection will not change depending on the protocol, but
this information is provided in case a better choice can be made, like choosing an
caching HTTP proxy for HTTP-based connections, but a more powerful SOCKSv5 proxy for all
others.

Some of the criteria may not make sense in all of the types of query. The following
table lists the criteria that are most commonly used, according to the type of query.

| Query type | Description |
| --- | --- |
| [TcpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) | Normal sockets requesting a connection to a remote server, like [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html). The peer hostname and peer port match the values passed to [QTcpSocket::connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)(). The local port is usually -1, indicating the socket has no preference in which port should be used. The URL component is not used. |
| [UdpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) | Datagram-based sockets, which can both send and receive. The local port, remote host or remote port fields can all be used or be left unused, depending on the characteristics of the socket. The URL component is not used. |
| [SctpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) | Message-oriented sockets requesting a connection to a remote server. The peer hostname and peer port match the values passed to [QSctpSocket::connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)(). The local port is usually -1, indicating the socket has no preference in which port should be used. The URL component is not used. |
| [TcpServer](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) | Passive server sockets that listen on a port and await incoming connections from the network. Normally, only the local port is used, but the remote address could be used in specific circumstances, for example to indicate which remote host a connection is expected from. The URL component is not used. |
| [UrlRequest](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) | A more high-level request, such as those coming from [QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html). These requests will inevitably use an outgoing TCP socket, but the this query type is provided to indicate that more detailed information is present in the URL component. For ease of implementation, the URL's host and port are set as the destination address. |
| [SctpServer](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) | Passive server sockets that listen on an SCTP port and await incoming connections from the network. Normally, only the local port is used, but the remote address could be used in specific circumstances, for example to indicate which remote host a connection is expected from. The URL component is not used. |

It should be noted that any of the criteria may be missing or unknown (an empty
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html) for the hostname or protocol
name, -1 for the port numbers). If that happens, the functions executing the query
should make their best guess or apply some implementation-defined default values.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html"""

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

    def localPort(self) -> int:
        """X.localPort() -> int

Supplemental documentation:
Qt 5 reference:

### int QNetworkProxyQuery::localPort() const

Returns the port number of the socket that will accept incoming packets from remote
servers or -1 if the port is not known.

**See also**
[peerPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerPort)(),
[peerHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerHostName)(),
and
[setLocalPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setLocalPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localPort(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#localPort"""
        ...

    def networkConfiguration(self) -> Any:
        """X.networkConfiguration() -> PythonQt.QtNetwork.QNetworkConfiguration

Upstream PySide2 reference signatures (binding differences may apply):

```python
networkConfiguration(self) -> PySide2.QtNetwork.QNetworkConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#networkConfiguration"""
        ...

    def peerHostName(self) -> str:
        """X.peerHostName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkProxyQuery::peerHostName() const

Returns the host name or IP address being of the outgoing connection being requested, or
an empty string if the remote hostname is not known.

If the query type is
[QNetworkProxyQuery::UrlRequest](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum),
this function returns the host component of the URL being requested.

**See also**
[peerPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerPort)(),
[localPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#localPort)(), and
[setPeerHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerHostName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerHostName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerHostName"""
        ...

    def peerPort(self) -> int:
        """X.peerPort() -> int

Supplemental documentation:
Qt 5 reference:

### int QNetworkProxyQuery::peerPort() const

Returns the port number for the outgoing request or -1 if the port number is not known.

If the query type is
[QNetworkProxyQuery::UrlRequest](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum),
this function returns the port number of the URL being requested. In general, frameworks
will fill in the port number from their default values.

**See also**
[peerHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerHostName)(),
[localPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#localPort)(), and
[setPeerPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerPort(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerPort"""
        ...

    def protocolTag(self) -> str:
        """X.protocolTag() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkProxyQuery::protocolTag() const

Returns the protocol tag for this
[QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html) object,
or an empty [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) in case the
protocol tag is unknown.

In the case of queries of type
[QNetworkProxyQuery::UrlRequest](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum),
this function returns the value of the scheme component of the URL.

**See also**
[setProtocolTag](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setProtocolTag)()
and [url](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#url)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
protocolTag(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#protocolTag"""
        ...

    def queryType(self) -> Any:
        """X.queryType()

Supplemental documentation:
Qt 5 reference:

### [QNetworkProxyQuery::QueryType](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) QNetworkProxyQuery::queryType() const

Returns the query type.

**See also**
[setQueryType](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setQueryType)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
queryType(self) -> PySide2.QtNetwork.QNetworkProxyQuery.QueryType
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#queryType"""
        ...

    def setLocalPort(self, port: int) -> None:
        """X.setLocalPort(port)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxyQuery::setLocalPort(int *port*)

Sets the port number that the socket wishes to use locally to accept incoming packets
from remote servers to *port*. The local port is most often used with the
[QNetworkProxyQuery::TcpServer](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum)
and
[QNetworkProxyQuery::UdpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum)
query types.

Valid values are 0 to 65535 (with 0 indicating that any port number will be acceptable)
or -1, which means the local port number is unknown or not applicable.

In some circumstances, for special protocols, it's the local port number can also be
used with a query of type
[QNetworkProxyQuery::TcpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum).
When that happens, the socket is indicating it wishes to use the port number *port* when
connecting to a remote host.

**See also**
[localPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#localPort)(),
[setPeerPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerPort)(),
and
[setPeerHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerHostName)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLocalPort(self, port: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setLocalPort"""
        ...

    def setNetworkConfiguration(self, networkConfiguration: Any) -> None:
        """X.setNetworkConfiguration(networkConfiguration)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setNetworkConfiguration(self, networkConfiguration: PySide2.QtNetwork.QNetworkConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setNetworkConfiguration"""
        ...

    def setPeerHostName(self, hostname: str) -> None:
        """X.setPeerHostName(hostname)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxyQuery::setPeerHostName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostname*)

Sets the hostname of the outgoing connection being requested to *hostname*. An empty
hostname can be used to indicate that the remote host is unknown.

The peer host name can also be used to indicate the expected source address of an
incoming connection in the case of
[QNetworkProxyQuery::UdpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum)
or
[QNetworkProxyQuery::TcpServer](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum)
query types.

**See also**
[peerHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerHostName)(),
[setPeerPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerPort)(),
and
[setLocalPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setLocalPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerHostName(self, hostname: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerHostName"""
        ...

    def setPeerPort(self, port: int) -> None:
        """X.setPeerPort(port)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxyQuery::setPeerPort(int *port*)

Sets the requested port number for the outgoing connection to be *port*. Valid values
are 1 to 65535, or -1 to indicate that the remote port number is unknown.

The peer port number can also be used to indicate the expected port number of an
incoming connection in the case of
[QNetworkProxyQuery::UdpSocket](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum)
or
[QNetworkProxyQuery::TcpServer](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum)
query types.

**See also**
[peerPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerPort)(),
[setPeerHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerHostName)(),
and
[setLocalPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setLocalPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerPort(self, port: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setPeerPort"""
        ...

    def setProtocolTag(self, protocolTag: str) -> None:
        """X.setProtocolTag(protocolTag)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxyQuery::setProtocolTag(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*protocolTag*)

Sets the protocol tag for this
[QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html) object
to be *protocolTag*.

The protocol tag is an arbitrary string that indicates which protocol is being talked
over the socket, such as "http", "xmpp", "telnet", etc. The protocol tag is used by the
backend to return a request that is more specific to the protocol in question: for
example, a HTTP connection could be use a caching HTTP proxy server, while all other
connections use a more powerful SOCKSv5 proxy server.

**See also**
[protocolTag](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#protocolTag)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProtocolTag(self, protocolTag: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setProtocolTag"""
        ...

    def setQueryType(self, type: Any) -> None:
        """X.setQueryType(type)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxyQuery::setQueryType([QNetworkProxyQuery::QueryType](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum) *type*)

Sets the query type of this object to be *type*.

**See also**
[queryType](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#queryType)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setQueryType(self, type: PySide2.QtNetwork.QNetworkProxyQuery.QueryType) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setQueryType"""
        ...

    def setUrl(self, url: Any) -> None:
        """X.setUrl(url)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxyQuery::setUrl(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Sets the URL component of this
[QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html) object
to be *url*. Setting the URL will also set the protocol tag, the remote host name and
port number. This is done so as to facilitate the implementation of the code that
determines the proxy server to be used.

**See also** [url](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#url)(),
[peerHostName](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerHostName)(),
and [peerPort](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#peerPort)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUrl(self, url: PySide2.QtCore.QUrl) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setUrl"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkProxyQuery::swap([QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QNetworkProxyQuery) \\&*other*)

Swaps this network proxy query instance with *other*. This function is very fast and
never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkProxyQuery) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#swap"""
        ...

    def url(self) -> Any:
        """X.url() -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QNetworkProxyQuery::url() const

Returns the URL component of this
[QNetworkProxyQuery](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html) object
in case of a query of type
[QNetworkProxyQuery::UrlRequest](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#QueryType-enum).

**See also**
[setUrl](https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#setUrl)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
url(self) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkproxyquery.html#url"""
        ...
    QueryType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    TcpServer: QueryType
    TcpSocket: QueryType
    UdpSocket: QueryType
    UrlRequest: QueryType

class QNetworkReply:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QNetworkReply class contains the data and meta data related to a request posted with
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).
Like [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html), it
contains a URL and headers (both in parsed and raw form), some information about the
reply's state and the contents of the reply itself.

QNetworkReply is a sequential-access
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html), which means that once
data is read from the object, it is no longer kept by the device. It is therefore the
application's responsibility to keep this data if it needs to. Whenever more data is
received from the network and processed, the
[readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)() signal is
emitted.

The
[downloadProgress](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#downloadProgress)()
signal is also emitted when data is received, but the number of bytes contained in it
may not represent the actual bytes received, if any transformation is done to the
contents (for example, decompressing and removing the protocol overhead).

Even though QNetworkReply is a
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) connected to the contents
of the reply, it also emits the
[uploadProgress](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#uploadProgress)()
signal, which indicates the progress of the upload for operations that have such
content.

**Note:** Do not delete the object in the slot connected to the
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#errorOccurred)()
or [finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)() signal.
Use [deleteLater](https://doc.qt.io/archives/qt-5.15/qobject.html#deleteLater)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abort(self) -> None:
        """X.abort()

Supplemental documentation:
Qt 5 reference:

### `[pure virtual slot]` void QNetworkReply::abort()

Aborts the operation immediately and close down any network connections still open.
Uploads still in progress are also aborted.

The [finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)() signal
will also be emitted.

**See also** [close](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#close)() and
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
abort(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#abort"""
        ...

    def aboutToClose(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.aboutToClose; argument details are not documented."""
        ...

    def atEnd(self) -> bool:
        """X.atEnd() -> bool"""
        ...

    def attribute(self, code: Any) -> Any:
        """X.attribute(code) -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QNetworkReply::attribute([QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum) *code*) const

Returns the attribute associated with the code *code*. If the attribute has not been
set, it returns an invalid [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html)
(type
[QMetaType::UnknownType](https://doc.qt.io/archives/qt-5.15/qmetatype.html#Type-enum)).

You can expect the default values listed in
[QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum)
to be applied to the values returned by this function.

**See also**
[setAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setAttribute)() and
[QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
attribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#attribute"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def bytesAvailable(self) -> int:
        """X.bytesAvailable() -> int"""
        ...

    def bytesToWrite(self) -> int:
        """X.bytesToWrite() -> int"""
        ...

    def bytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.bytesWritten; argument details are not documented."""
        ...

    def canReadLine(self) -> bool:
        """X.canReadLine() -> bool"""
        ...

    def channelBytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.channelBytesWritten; argument details are not documented."""
        ...

    def channelReadyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.channelReadyRead; argument details are not documented."""
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

    def close(self) -> None:
        """X.close()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QNetworkReply::close()

Reimplements:
[QIODevice::close](https://doc.qt.io/archives/qt-5.15/qiodevice.html#close)().

Closes this device for reading. Unread data is discarded, but the network resources are
not discarded until they are finished. In particular, if any upload is in progress, it
will continue until it is done.

The [finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)() signal
is emitted when all operations are over and the network resources are freed.

**See also** [abort](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#abort)() and
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
close(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#close"""
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
        """Native PythonQt.QtNetwork.QNetworkReply.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def downloadProgress(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.downloadProgress; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::downloadProgress([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *bytesReceived*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *bytesTotal*)

This signal is emitted to indicate the progress of the download part of this network
request, if there's any. If there's no download associated with this request, this
signal will be emitted once with 0 as the value of both *bytesReceived* and
*bytesTotal*.

The *bytesReceived* parameter indicates the number of bytes received, while *bytesTotal*
indicates the total number of bytes expected to be downloaded. If the number of bytes to
be downloaded is not known, *bytesTotal* will be -1.

The download is finished when *bytesReceived* is equal to *bytesTotal*. At that time,
*bytesTotal* will not be -1.

Note that the values of both *bytesReceived* and *bytesTotal* may be different from
[size](https://doc.qt.io/archives/qt-5.15/qiodevice.html#size)(), the total number of
bytes obtained through [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)()
or [readAll](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readAll)(), or the value
of the header(ContentLengthHeader). The reason for that is that there may be protocol
overhead or the data may be compressed during the download.

**See also**
[uploadProgress](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#uploadProgress)()
and
[bytesAvailable](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesAvailable)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#downloadProgress"""
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

    def encrypted(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.encrypted; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::encrypted()

This signal is emitted when an SSL/TLS session has successfully completed the initial
handshake. At this point, no user data has been transmitted. The signal can be used to
perform additional checks on the certificate chain, for example to notify users when the
certificate for a website has changed. If the reply does not match the expected criteria
then it should be aborted by calling
[QNetworkReply::abort](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#abort)() by
a slot connected to this signal. The SSL configuration in use can be inspected using the
[QNetworkReply::sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)()
method.

Internally,
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
may open multiple connections to a server, in order to allow it process requests in
parallel. These connections may be reused, which means that the encrypted() signal would
not be emitted. This means that you are only guaranteed to receive this signal for the
first connection to a site in the lifespan of the
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html).

This function was introduced in Qt 5.1.

**See also**
[QSslSocket::encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)()
and
[QNetworkAccessManager::encrypted](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#encrypted)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#encrypted"""
        ...

    def error(self) -> Any:
        """X.error()

Supplemental documentation:
Qt 5 reference:

### [QNetworkReply::NetworkError](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#NetworkError-enum) QNetworkReply::error() const

Returns the error that was found during the processing of this request. If no error was
found, returns
[NoError](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#NetworkError-enum).

**See also**
[setError](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setError)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
error(self) -> PySide2.QtNetwork.QNetworkReply.NetworkError
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#error"""
        ...

    def errorOccurred(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.errorOccurred; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::errorOccurred([QNetworkReply::NetworkError](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#NetworkError-enum) *code*)

This signal is emitted when the reply detects an error in processing. The
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)() signal will
probably follow, indicating that the connection is over.

The *code* parameter contains the code of the error that was detected. Call
[errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)() to obtain
a textual representation of the error condition.

**Note:** Do not delete the object in the slot connected to this signal. Use
[deleteLater](https://doc.qt.io/archives/qt-5.15/qobject.html#deleteLater)().

This function was introduced in Qt 5.15.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#error)() and
[errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#errorOccurred"""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str"""
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

    def finished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.finished; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::finished()

This signal is emitted when the reply has finished processing. After this signal is
emitted, there will be no more updates to the reply's data or metadata.

Unless [close](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#close)() or
[abort](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#abort)() have been called,
the reply will still be opened for reading, so the data can be retrieved by calls to
[read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)() or
[readAll](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readAll)(). In particular,
if no calls to [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)() were
made as a result of
[readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)(), a call to
[readAll](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readAll)() will retrieve the
full contents in a [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html).

This signal is emitted in tandem with
[QNetworkAccessManager::finished](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished)()
where that signal's reply parameter is this object.

**Note:** Do not delete the object in the slot connected to this signal. Use
[deleteLater](https://doc.qt.io/archives/qt-5.15/qobject.html#deleteLater)().

You can also use
[isFinished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isFinished)() to
check if a [QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) has
finished even before you receive the finished() signal.

**See also**
[setFinished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setFinished)(),
[QNetworkAccessManager::finished](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#finished)(),
and [isFinished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isFinished)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished"""
        ...

    def getChar(self, c: Any) -> bool:
        """X.getChar(c) -> bool"""
        ...

    def hasRawHeader(self, headerName: Any) -> bool:
        """X.hasRawHeader(headerName) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkReply::hasRawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*) const

Returns `true` if the raw header of name *headerName* was sent by the remote server

**See also**
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasRawHeader(self, headerName: PySide2.QtCore.QByteArray) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#hasRawHeader"""
        ...

    def header(self, header: Any) -> Any:
        """X.header(header) -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QNetworkReply::header([QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum) *header*) const

Returns the value of the known header *header*, if that header was sent by the remote
server. If the header was not sent, returns an invalid
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html).

**See also**
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeader)(),
[setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setHeader)(), and
[QNetworkRequest::header](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#header)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
header(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#header"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def ignoreSslErrors(self) -> None:
        """X.ignoreSslErrors()

Supplemental documentation:
Qt 5 reference:

### `[virtual slot]` void QNetworkReply::ignoreSslErrors()

If this function is called, SSL errors related to network connection will be ignored,
including certificate validation errors.

**Warning:** Be sure to always let the user inspect the errors reported by the
[sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)() signal,
and only call this method upon confirmation from the user that proceeding is ok. If
there are unexpected errors, the reply should be aborted. Calling this method without
inspecting the actual errors will most likely pose a security risk for your application.
Use it with great care!

This function can be called from the slot connected to the
[sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)() signal,
which indicates which errors were found.

**Note:** If HTTP Strict Transport Security is enabled for
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html),
this function has no effect.

**See also**
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)(),
[sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)(), and
[QSslSocket::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)().

### void QNetworkReply::ignoreSslErrors(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html)\\> \\&*errors*)

This is an overloaded function.

If this function is called, the SSL errors given in *errors* will be ignored.

**Note:** Because most SSL errors are associated with a certificate, for most of them
you must set the expected certificate this SSL error is related to. If, for instance,
you want to issue a request to a server that uses a self-signed certificate, consider
the following snippet:

```
QList<QSslCertificate> cert = QSslCertificate::fromPath(QLatin1String("server-certificate.pem"));
QSslError error(QSslError::SelfSignedCertificate, cert.at(0));
QList<QSslError> expectedSslErrors;
expectedSslErrors.append(error);

QNetworkReply *reply = manager.get(QNetworkRequest(QUrl("https://server.tld/index.html")));
reply->ignoreSslErrors(expectedSslErrors);
// here connect signals etc.
```

Multiple calls to this function will replace the list of errors that were passed in
previous calls. You can clear the list of errors you want to ignore by calling this
function with an empty list.

**Note:** If HTTP Strict Transport Security is enabled for
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html),
this function has no effect.

This function was introduced in Qt 4.6.

**See also**
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)(),
[sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)(),
[QSslSocket::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)(),
and
[QNetworkAccessManager::setStrictTransportSecurityEnabled](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setStrictTransportSecurityEnabled)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
ignoreSslErrors(self) -> None
ignoreSslErrors(self, errors: typing.Sequence[PySide2.QtNetwork.QSslError]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors"""
        ...

    def ignoreSslErrorsImplementation(self, arg__1: Any) -> None:
        """X.ignoreSslErrorsImplementation(arg__1)

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QNetworkReply::ignoreSslErrorsImplementation(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html)\\> \\&*errors*)

This virtual method is provided to enable overriding the behavior of
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)().
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)()
is a public wrapper for this method. *errors* contains the errors the user wishes
ignored.

This function was introduced in Qt 5.0.

**See also**
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
ignoreSslErrorsImplementation(self, arg__1: typing.Sequence[PySide2.QtNetwork.QSslError]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrorsImplementation"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isFinished(self) -> bool:
        """X.isFinished() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkReply::isFinished() const

Returns `true` when the reply has finished or was aborted.

This function was introduced in Qt 4.6.

**See also**
[isRunning](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isRunning)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isFinished(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isFinished"""
        ...

    def isOpen(self) -> bool:
        """X.isOpen() -> bool"""
        ...

    def isReadable(self) -> bool:
        """X.isReadable() -> bool"""
        ...

    def isRunning(self) -> bool:
        """X.isRunning() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkReply::isRunning() const

Returns `true` when the request is still processing and the reply has not finished or
was aborted yet.

This function was introduced in Qt 4.6.

**See also**
[isFinished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isFinished)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isRunning(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isRunning"""
        ...

    def isSequential(self) -> bool:
        """X.isSequential() -> bool

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSequential(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isSequential"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isTextModeEnabled(self) -> bool:
        """X.isTextModeEnabled() -> bool"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def isWritable(self) -> bool:
        """X.isWritable() -> bool"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def manager(self) -> Any:
        """X.manager() -> PythonQt.QtNetwork.QNetworkAccessManager

Supplemental documentation:
Qt 5 reference:

### [QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html) \\*QNetworkReply::manager() const

Returns the
[QNetworkAccessManager](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html)
that was used to create this
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) object.
Initially, it is also the parent object.

Upstream PySide2 reference signatures (binding differences may apply):

```python
manager(self) -> PySide2.QtNetwork.QNetworkAccessManager
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#manager"""
        ...

    def metaDataChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.metaDataChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::metaDataChanged()

This signal is emitted whenever the metadata in this reply changes. metadata is any
information that is not the content (data) itself, including the network headers. In the
majority of cases, the metadata will be known fully by the time the first byte of data
is received. However, it is possible to receive updates of headers or other metadata
during the processing of the data.

**See also** [header](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#header)(),
[rawHeaderList](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeaderList)(),
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeader)(), and
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#hasRawHeader)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#metaDataChanged"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.objectNameChanged; argument details are not documented."""
        ...

    def open(self, mode: Any) -> bool:
        """X.open(mode) -> bool"""
        ...

    def openMode(self) -> Any:
        """X.openMode()"""
        ...

    def operation(self) -> Any:
        """X.operation()

Supplemental documentation:
Qt 5 reference:

### [QNetworkAccessManager::Operation](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#Operation-enum) QNetworkReply::operation() const

Returns the operation that was posted for this reply.

**See also**
[setOperation](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setOperation)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
operation(self) -> PySide2.QtNetwork.QNetworkAccessManager.Operation
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#operation"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def peek(self, maxlen: Any) -> Any:
        """X.peek(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def pos(self) -> int:
        """X.pos() -> int"""
        ...

    def preSharedKeyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.preSharedKeyAuthenticationRequired; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::preSharedKeyAuthenticationRequired([QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html) \\**authenticator*)

This signal is emitted if the SSL/TLS handshake negotiates a PSK ciphersuite, and
therefore a PSK authentication is then required.

When using PSK, the client must send to the server a valid identity and a valid pre
shared key, in order for the SSL handshake to continue. Applications can provide this
information in a slot connected to this signal, by filling in the passed *authenticator*
object according to their needs.

**Note:** Ignoring this signal, or failing to provide the required credentials, will
cause the handshake to fail, and therefore the connection to be aborted.

**Note:** The *authenticator* object is owned by the reply and must not be deleted by
the application.

This function was introduced in Qt 5.5.

**See also**
[QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html).

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#preSharedKeyAuthenticationRequired"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def putChar(self, c: Any) -> bool:
        """X.putChar(c) -> bool"""
        ...

    def rawHeader(self, headerName: Any) -> Any:
        """X.rawHeader(headerName) -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QNetworkReply::rawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*) const

Returns the raw contents of the header *headerName* as sent by the remote server. If
there is no such header, returns an empty byte array, which may be indistinguishable
from an empty header. Use
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#hasRawHeader)() to
verify if the server sent such header field.

**See also**
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setRawHeader)(),
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#hasRawHeader)(),
and [header](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#header)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeader(self, headerName: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeader"""
        ...

    def rawHeaderList(self) -> Any:
        """X.rawHeaderList()

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> QNetworkReply::rawHeaderList() const

Returns a list of headers fields that were sent by the remote server, in the order that
they were sent. Duplicate headers are merged together and take place of the latter
duplicate.

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeaderList(self) -> typing.List[PySide2.QtCore.QByteArray]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeaderList"""
        ...

    def rawHeaderPairs(self) -> tuple:
        """X.rawHeaderPairs() -> tuple

Supplemental documentation:
Qt 5 reference:

### const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QNetworkReply::RawHeaderPair](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#RawHeaderPair-typedef)\\> \\&QNetworkReply::rawHeaderPairs() const

Returns a list of raw header pairs.

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeaderPairs(self) -> typing.List[typing.Tuple[PySide2.QtCore.QByteArray, PySide2.QtCore.QByteArray]]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeaderPairs"""
        ...

    def read(self, maxlen: Any) -> Any:
        """X.read(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readAll(self) -> Any:
        """X.readAll() -> PythonQt.QtCore.QByteArray"""
        ...

    def readBufferSize(self) -> int:
        """X.readBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QNetworkReply::readBufferSize() const

Returns the size of the read buffer, in bytes.

**See also**
[setReadBufferSize](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setReadBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
readBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#readBufferSize"""
        ...

    def readChannelFinished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.readChannelFinished; argument details are not documented."""
        ...

    def readData(self, data: Any, maxlen: Any) -> int:
        """X.readData(data, maxlen) -> int"""
        ...

    def readLine(self, maxlen: Any) -> Any:
        """X.readLine(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readLineData(self, data: Any, maxlen: Any) -> int:
        """X.readLineData(data, maxlen) -> int"""
        ...

    def readyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.readyRead; argument details are not documented."""
        ...

    def redirectAllowed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.redirectAllowed; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::redirectAllowed()

When client code handling the
[redirected](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#redirected)() signal
has verified the new URL, it emits this signal to allow the redirect to go ahead. This
protocol applies to network requests whose redirects policy is set to
[QNetworkRequest::UserVerifiedRedirectPolicy](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#RedirectPolicy-enum)

This function was introduced in Qt 5.9.

**See also**
[QNetworkRequest::UserVerifiedRedirectPolicy](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#RedirectPolicy-enum),
[QNetworkAccessManager::setRedirectPolicy](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#setRedirectPolicy)(),
and
[QNetworkRequest::RedirectPolicyAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum).

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#redirectAllowed"""
        ...

    def redirected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.redirected; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::redirected(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

This signal is emitted if the
[QNetworkRequest::FollowRedirectsAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum)
was set in the request and the server responded with a 3xx status (specifically 301,
302, 303, 305, 307 or 308 status code) with a valid url in the location header,
indicating a HTTP redirect. The *url* parameter contains the new redirect url as
returned by the server in the location header.

This function was introduced in Qt 5.6.

**See also**
[QNetworkRequest::FollowRedirectsAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum).

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#redirected"""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def request(self) -> Any:
        """X.request() -> PythonQt.QtNetwork.QNetworkRequest

Supplemental documentation:
Qt 5 reference:

### [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) QNetworkReply::request() const

Returns the request that was posted for this reply. In special, note that the URL for
the request may be different than that of the reply.

**See also**
[QNetworkRequest::url](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#url)(),
[url](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#url)(), and
[setRequest](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setRequest)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
request(self) -> PySide2.QtNetwork.QNetworkRequest
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#request"""
        ...

    def reset(self) -> bool:
        """X.reset() -> bool"""
        ...

    def seek(self, pos: Any) -> bool:
        """X.seek(pos) -> bool"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setAttribute(self, code: Any, value: Any) -> None:
        """X.setAttribute(code, value)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setAttribute([QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum) *code*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the attribute *code* to have value *value*. If *code* was previously set, it will
be overridden. If *value* is an invalid
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html), the attribute will be
unset.

**See also**
[attribute](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#attribute)() and
[QNetworkRequest::setAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setAttribute)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAttribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setAttribute"""
        ...

    def setError(self, errorCode: Any, errorString: str) -> None:
        """X.setError(errorCode, errorString)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setError([QNetworkReply::NetworkError](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#NetworkError-enum) *errorCode*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*errorString*)

Sets the error condition to be *errorCode*. The human-readable message is set with
*errorString*.

Calling setError() does not emit the
[errorOccurred](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#errorOccurred)([QNetworkReply::NetworkError](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#NetworkError-enum))
signal.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#error)() and
[errorString](https://doc.qt.io/archives/qt-5.15/qiodevice.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setError(self, errorCode: PySide2.QtNetwork.QNetworkReply.NetworkError, errorString: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setError"""
        ...

    def setErrorString(self, errorString: Any) -> Any:
        """X.setErrorString(errorString)"""
        ...

    def setFinished(self, arg__1: bool) -> None:
        """X.setFinished(arg__1)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setFinished(bool *finished*)

Sets the reply as *finished*.

After having this set the replies data must not change.

This function was introduced in Qt 4.8.

**See also**
[finished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#finished)() and
[isFinished](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#isFinished)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setFinished(self, arg__1: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setFinished"""
        ...

    def setHeader(self, header: Any, value: Any) -> None:
        """X.setHeader(header, value)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setHeader([QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum) *header*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the known header *header* to be of value *value*. The corresponding raw form of the
header will be set as well.

**See also** [header](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#header)(),
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setRawHeader)(),
and
[QNetworkRequest::setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHeader(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setHeader"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setOpenMode(self, openMode: Any) -> Any:
        """X.setOpenMode(openMode)"""
        ...

    def setOperation(self, operation: Any) -> None:
        """X.setOperation(operation)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setOperation([QNetworkAccessManager::Operation](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#Operation-enum) *operation*)

Sets the associated operation for this object to be *operation*. This value will be
returned by
[operation](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#operation)().

**Note:** The operation should be set when this object is created and not changed again.

**See also**
[operation](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#operation)() and
[setRequest](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setRequest)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setOperation(self, operation: PySide2.QtNetwork.QNetworkAccessManager.Operation) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setOperation"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setRawHeader(self, headerName: Any, value: Any) -> None:
        """X.setRawHeader(headerName, value)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setRawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*value*)

Sets the raw header *headerName* to be of value *value*. If *headerName* was previously
set, it is overridden. Multiple HTTP headers of the same name are functionally
equivalent to one single header with the values concatenated, separated by commas.

If *headerName* matches a known header, the value *value* will be parsed and the
corresponding parsed form will also be set.

**See also**
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#rawHeader)(),
[header](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#header)(),
[setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setHeader)(), and
[QNetworkRequest::setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRawHeader(self, headerName: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setRawHeader"""
        ...

    def setReadBufferSize(self, size: int) -> None:
        """X.setReadBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QNetworkReply::setReadBufferSize([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *size*)

Sets the size of the read buffer to be *size* bytes. The read buffer is the buffer that
holds data that is being downloaded off the network, before it is read with
[QIODevice::read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)(). Setting the
buffer size to 0 will make the buffer unlimited in size.

[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) will try to stop
reading from the network once this buffer is full (i.e.,
[bytesAvailable](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesAvailable)()
returns *size* or more), thus causing the download to throttle down as well. If the
buffer is not limited in size,
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) will try to
download as fast as possible from the network.

Unlike
[QAbstractSocket::setReadBufferSize](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setReadBufferSize)(),
[QNetworkReply](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html) cannot guarantee
precision in the read buffer size. That is,
[bytesAvailable](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesAvailable)() can
return more than *size*.

**See also**
[readBufferSize](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#readBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setReadBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setReadBufferSize"""
        ...

    def setRequest(self, request: Any) -> None:
        """X.setRequest(request)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setRequest(const [QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html) \\&*request*)

Sets the associated request for this object to be *request*. This value will be returned
by [request](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#request)().

**Note:** The request should be set when this object is created and not changed again.

**See also** [request](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#request)()
and
[setOperation](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setOperation)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRequest(self, request: PySide2.QtNetwork.QNetworkRequest) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setRequest"""
        ...

    def setSslConfigurationImplementation(self, arg__1: Any) -> None:
        """X.setSslConfigurationImplementation(arg__1)

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QNetworkReply::setSslConfigurationImplementation(const [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) \\&*configuration*)

This virtual method is provided to enable overriding the behavior of
[setSslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setSslConfiguration)().
[setSslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setSslConfiguration)()
is a public wrapper for this method. If you override this method use *configuration* to
set the SSL configuration.

This function was introduced in Qt 5.0.

**See also**
[sslConfigurationImplementation](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfigurationImplementation)()
and
[setSslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setSslConfiguration)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSslConfigurationImplementation(self, arg__1: PySide2.QtNetwork.QSslConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setSslConfigurationImplementation"""
        ...

    def setTextModeEnabled(self, enabled: Any) -> Any:
        """X.setTextModeEnabled(enabled)"""
        ...

    def setUrl(self, url: Any) -> None:
        """X.setUrl(url)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QNetworkReply::setUrl(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Sets the URL being processed to be *url*. Normally, the URL matches that of the request
that was posted, but for a variety of reasons it can be different (for example, a file
path being made absolute or canonical).

**See also** [url](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#url)(),
[request](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#request)(), and
[QNetworkRequest::url](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#url)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUrl(self, url: PySide2.QtCore.QUrl) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setUrl"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def size(self) -> int:
        """X.size() -> int"""
        ...

    def sslConfigurationImplementation(self, arg__1: Any) -> None:
        """X.sslConfigurationImplementation(arg__1)

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QNetworkReply::sslConfigurationImplementation([QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) \\&*configuration*) const

This virtual method is provided to enable overriding the behavior of
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)().
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)()
is a public wrapper for this method. The configuration will be returned in
*configuration*.

This function was introduced in Qt 5.0.

**See also**
[setSslConfigurationImplementation](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setSslConfigurationImplementation)()
and
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sslConfigurationImplementation(self, arg__1: PySide2.QtNetwork.QSslConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfigurationImplementation"""
        ...

    def sslErrors(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.sslErrors; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::sslErrors(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html)\\> \\&*errors*)

This signal is emitted if the SSL/TLS session encountered errors during the set up,
including certificate verification errors. The *errors* parameter contains the list of
errors.

To indicate that the errors are not fatal and that the connection should proceed, the
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)()
function should be called from the slot connected to this signal. If it is not called,
the SSL session will be torn down before any data is exchanged (including the URL).

This signal can be used to display an error message to the user indicating that security
may be compromised and display the SSL settings (see
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)()
to obtain it). If the user decides to proceed after analyzing the remote certificate,
the slot should call
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)().

**See also**
[QSslSocket::sslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#sslErrors)(),
[QNetworkAccessManager::sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkaccessmanager.html#sslErrors)(),
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslConfiguration)(),
and
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors"""
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

    def ungetChar(self, c: Any) -> Any:
        """X.ungetChar(c)"""
        ...

    def uploadProgress(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkReply.uploadProgress; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkReply::uploadProgress([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *bytesSent*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *bytesTotal*)

This signal is emitted to indicate the progress of the upload part of this network
request, if there's any. If there's no upload associated with this request, this signal
will not be emitted.

The *bytesSent* parameter indicates the number of bytes uploaded, while *bytesTotal*
indicates the total number of bytes to be uploaded. If the number of bytes to be
uploaded could not be determined, *bytesTotal* will be -1.

The upload is finished when *bytesSent* is equal to *bytesTotal*. At that time,
*bytesTotal* will not be -1.

**See also**
[downloadProgress](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#downloadProgress)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#uploadProgress"""
        ...

    def url(self) -> Any:
        """X.url() -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QNetworkReply::url() const

Returns the URL of the content downloaded or uploaded. Note that the URL may be
different from that of the original request. If the
[QNetworkRequest::FollowRedirectsAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum)
was set in the request, then this function returns the current url that the network API
is accessing, i.e the url emitted in the
[QNetworkReply::redirected](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#redirected)
signal.

**See also** [request](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#request)(),
[setUrl](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#setUrl)(),
[QNetworkRequest::url](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#url)(),
and [redirected](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#redirected)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
url(self) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#url"""
        ...

    def waitForBytesWritten(self, msecs: Any) -> bool:
        """X.waitForBytesWritten(msecs) -> bool"""
        ...

    def waitForReadyRead(self, msecs: Any) -> bool:
        """X.waitForReadyRead(msecs) -> bool"""
        ...

    def write(self, data: Any) -> int:
        """X.write(data) -> int"""
        ...

    def writeData(self, data: str, len: int) -> int:
        """X.writeData(data, len) -> int

Upstream PySide2 reference signatures (binding differences may apply):

```python
writeData(self, data: str, len: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#writeData"""
        ...
    Append: Any
    AuthenticationRequiredError: Any
    BackgroundRequestNotAllowedError: Any
    ConnectionRefusedError: Any
    ContentAccessDenied: Any
    ContentConflictError: Any
    ContentGoneError: Any
    ContentNotFoundError: Any
    ContentOperationNotPermittedError: Any
    ContentReSendError: Any
    HostNotFoundError: Any
    InsecureRedirectError: Any
    InternalServerError: Any
    NetworkError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NetworkSessionFailedError: Any
    NoError: Any
    NotOpen: Any
    OpenMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenModeFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OperationCanceledError: Any
    OperationNotImplementedError: Any
    ProtocolFailure: Any
    ProtocolInvalidOperationError: Any
    ProtocolUnknownError: Any
    ProxyAuthenticationRequiredError: Any
    ProxyConnectionClosedError: Any
    ProxyConnectionRefusedError: Any
    ProxyNotFoundError: Any
    ProxyTimeoutError: Any
    ReadOnly: Any
    ReadWrite: Any
    RemoteHostClosedError: Any
    ServiceUnavailableError: Any
    SslHandshakeFailedError: Any
    TemporaryNetworkFailureError: Any
    Text: Any
    TimeoutError: Any
    TooManyRedirectsError: Any
    Truncate: Any
    Unbuffered: Any
    UnknownContentError: Any
    UnknownNetworkError: Any
    UnknownProxyError: Any
    UnknownServerError: Any
    WriteOnly: Any
    objectName: Any

class QNetworkRequest:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QNetworkRequest is part of the Network Access API and is the class holding the
information necessary to send a request over the network. It contains a URL and some
ancillary information that can be used to modify the request.

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def attribute(self, code: Any, defaultValue: Any) -> Any:
        """X.attribute(code, defaultValue) -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QNetworkRequest::attribute([QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum) *code*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*defaultValue* \\= QVariant()) const

Returns the attribute associated with the code *code*. If the attribute has not been
set, it returns *defaultValue*.

**Note:** This function does not apply the defaults listed in
[QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum).

**See also**
[setAttribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setAttribute)()
and
[QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
attribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute, defaultValue: typing.Any=...) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#attribute"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def hasRawHeader(self, headerName: Any) -> bool:
        """X.hasRawHeader(headerName) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkRequest::hasRawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*) const

Returns `true` if the raw header *headerName* is present in this network request.

**See also**
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#rawHeader)() and
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasRawHeader(self, headerName: PySide2.QtCore.QByteArray) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#hasRawHeader"""
        ...

    def header(self, header: Any) -> Any:
        """X.header(header) -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QNetworkRequest::header([QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum) *header*) const

Returns the value of the known network header *header* if it is present in this request.
If it is not present, returns QVariant() (i.e., an invalid variant).

**See also**
[KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#rawHeader)(), and
[setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
header(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#header"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def maximumRedirectsAllowed(self) -> int:
        """X.maximumRedirectsAllowed() -> int

Supplemental documentation:
Qt 5 reference:

### int QNetworkRequest::maximumRedirectsAllowed() const

Returns the maximum number of redirects allowed to be followed for this request.

This function was introduced in Qt 5.6.

**See also**
[setMaximumRedirectsAllowed](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setMaximumRedirectsAllowed)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
maximumRedirectsAllowed(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#maximumRedirectsAllowed"""
        ...

    def originatingObject(self) -> Any:
        """X.originatingObject() -> PythonQt.private.QObject

Supplemental documentation:
Qt 5 reference:

### [QObject](https://doc.qt.io/archives/qt-5.15/qobject.html) \\*QNetworkRequest::originatingObject() const

Returns a reference to the object that initiated this network request; returns `nullptr`
if not set or the object has been destroyed.

This function was introduced in Qt 4.6.

**See also**
[setOriginatingObject](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setOriginatingObject)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
originatingObject(self) -> PySide2.QtCore.QObject
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#originatingObject"""
        ...

    def priority(self) -> Any:
        """X.priority()

Supplemental documentation:
Qt 5 reference:

### [QNetworkRequest::Priority](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Priority-enum) QNetworkRequest::priority() const

Return the priority of this request.

This function was introduced in Qt 4.7.

**See also**
[setPriority](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setPriority)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
priority(self) -> PySide2.QtNetwork.QNetworkRequest.Priority
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#priority"""
        ...

    def rawHeader(self, headerName: Any) -> Any:
        """X.rawHeader(headerName) -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QNetworkRequest::rawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*) const

Returns the raw form of header *headerName*. If no such header is present, an empty
[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) is returned, which may
be indistinguishable from a header that is present but has no content (use
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#hasRawHeader)()
to find out if the header exists or not).

Raw headers can be set with
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader)()
or with
[setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setHeader)().

**See also** [header](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#header)()
and
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeader(self, headerName: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#rawHeader"""
        ...

    def rawHeaderList(self) -> Any:
        """X.rawHeaderList()

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> QNetworkRequest::rawHeaderList() const

Returns a list of all raw headers that are set in this network request. The list is in
the order that the headers were set.

**See also**
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#hasRawHeader)()
and [rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#rawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
rawHeaderList(self) -> typing.List[PySide2.QtCore.QByteArray]
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#rawHeaderList"""
        ...

    def setAttribute(self, code: Any, value: Any) -> None:
        """X.setAttribute(code, value)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::setAttribute([QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum) *code*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the attribute associated with code *code* to be value *value*. If the attribute is
already set, the previous value is discarded. In special, if *value* is an invalid
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html), the attribute is unset.

**See also**
[attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#attribute)() and
[QNetworkRequest::Attribute](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Attribute-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAttribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setAttribute"""
        ...

    def setHeader(self, header: Any, value: Any) -> None:
        """X.setHeader(header, value)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::setHeader([QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum) *header*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the value of the known header *header* to be *value*, overriding any previously set
headers. This operation also sets the equivalent raw HTTP header.

**See also**
[KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[setRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader)(),
and [header](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#header)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHeader(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setHeader"""
        ...

    def setMaximumRedirectsAllowed(self, maximumRedirectsAllowed: int) -> None:
        """X.setMaximumRedirectsAllowed(maximumRedirectsAllowed)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::setMaximumRedirectsAllowed(int *maxRedirectsAllowed*)

Sets the maximum number of redirects allowed to be followed for this request to
*maxRedirectsAllowed*.

This function was introduced in Qt 5.6.

**See also**
[maximumRedirectsAllowed](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#maximumRedirectsAllowed)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMaximumRedirectsAllowed(self, maximumRedirectsAllowed: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setMaximumRedirectsAllowed"""
        ...

    def setOriginatingObject(self, object: Any) -> None:
        """X.setOriginatingObject(object)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::setOriginatingObject([QObject](https://doc.qt.io/archives/qt-5.15/qobject.html) \\**object*)

Allows setting a reference to the *object* initiating the request.

For example Qt WebKit sets the originating object to the QWebFrame that initiated the
request.

This function was introduced in Qt 4.6.

**See also**
[originatingObject](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#originatingObject)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setOriginatingObject(self, object: PySide2.QtCore.QObject) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setOriginatingObject"""
        ...

    def setPriority(self, priority: Any) -> None:
        """X.setPriority(priority)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::setPriority([QNetworkRequest::Priority](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#Priority-enum) *priority*)

Set the priority of this request to *priority*.

**Note:** The *priority* is only a hint to the network access manager. It can use it or
not. Currently it is used for HTTP to decide which request should be sent first to a
server.

This function was introduced in Qt 4.7.

**See also**
[priority](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#priority)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPriority(self, priority: PySide2.QtNetwork.QNetworkRequest.Priority) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setPriority"""
        ...

    def setRawHeader(self, headerName: Any, value: Any) -> None:
        """X.setRawHeader(headerName, value)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::setRawHeader(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerName*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*headerValue*)

Sets the header *headerName* to be of value *headerValue*. If *headerName* corresponds
to a known header (see
[QNetworkRequest::KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum)),
the raw format will be parsed and the corresponding "cooked" header will be set as well.

For example:

```
request.setRawHeader(QByteArray("Last-Modified"), QByteArray("Sun, 06 Nov 1994 08:49:37 GMT"));
```

will also set the known header
[LastModifiedHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum)
to be the [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) object of the
parsed date.

**Note:** Setting the same header twice overrides the previous setting. To accomplish
the behaviour of multiple HTTP headers of the same name, you should concatenate the two
values, separating them with a comma (",") and set one single raw header.

**See also**
[KnownHeaders](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#KnownHeaders-enum),
[setHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setHeader)(),
[hasRawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#hasRawHeader)(),
and [rawHeader](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#rawHeader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRawHeader(self, headerName: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setRawHeader"""
        ...

    def setUrl(self, url: Any) -> None:
        """X.setUrl(url)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::setUrl(const [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) \\&*url*)

Sets the URL this network request is referring to be *url*.

**See also** [url](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#url)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUrl(self, url: PySide2.QtCore.QUrl) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setUrl"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QNetworkRequest::swap([QNetworkRequest](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#QNetworkRequest) \\&*other*)

Swaps this network request with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QNetworkRequest) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#swap"""
        ...

    def url(self) -> Any:
        """X.url() -> PythonQt.QtCore.QUrl

Supplemental documentation:
Qt 5 reference:

### [QUrl](https://doc.qt.io/archives/qt-5.15/qurl.html) QNetworkRequest::url() const

Returns the URL this network request is referring to.

**See also** [setUrl](https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#setUrl)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
url(self) -> PySide2.QtCore.QUrl
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworkrequest.html#url"""
        ...
    AlwaysCache: Any
    AlwaysNetwork: Any
    Attribute: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    AuthenticationReuseAttribute: Any
    Automatic: Any
    BackgroundRequestAttribute: Any
    CacheLoadControl: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    CacheLoadControlAttribute: Any
    CacheSaveControlAttribute: Any
    ConnectionEncryptedAttribute: Any
    ContentDispositionHeader: Any
    ContentLengthHeader: Any
    ContentTypeHeader: Any
    CookieHeader: Any
    CookieLoadControlAttribute: Any
    CookieSaveControlAttribute: Any
    CustomVerbAttribute: Any
    DoNotBufferUploadDataAttribute: Any
    DownloadBufferAttribute: Any
    EmitAllUploadProgressSignalsAttribute: Any
    FollowRedirectsAttribute: Any
    HighPriority: Any
    HttpPipeliningAllowedAttribute: Any
    HttpPipeliningWasUsedAttribute: Any
    HttpReasonPhraseAttribute: Any
    HttpStatusCodeAttribute: Any
    KnownHeaders: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    LastModifiedHeader: Any
    LoadControl: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    LocationHeader: Any
    LowPriority: Any
    Manual: Any
    MaximumDownloadBufferSizeAttribute: Any
    NormalPriority: Any
    PreferCache: Any
    PreferNetwork: Any
    Priority: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    RedirectionTargetAttribute: Any
    ServerHeader: Any
    SetCookieHeader: Any
    SourceIsFromCacheAttribute: Any
    SpdyAllowedAttribute: Any
    SpdyWasUsedAttribute: Any
    SynchronousRequestAttribute: Any
    User: Any
    UserAgentHeader: Any
    UserMax: Any

class QNetworkSession:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

A QNetworkSession enables control over the system's network interfaces. The session's
configuration parameter are determined via the
[QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html)
object to which it is bound. Depending on the type of the session (single access point
or service network) a session may be linked to one or more network interfaces. By means
of [opening](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open) and
[closing](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#close) of network
sessions a developer can start and stop the systems network interfaces. If the
configuration represents multiple access points (see
[QNetworkConfiguration::ServiceNetwork](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum))
more advanced features such as roaming may be supported.

QNetworkSession supports session management within the same process and depending on the
platform's capabilities may support out-of-process sessions. If the same network
configuration is used by multiple open sessions the underlying network interface is only
terminated once the last session has been closed.

### Roaming

Applications may connect to the
[preferredConfigurationChanged](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#preferredConfigurationChanged)()
signal in order to receive notifications when a more suitable access point becomes
available. In response to this signal the application must either initiate the roaming
via [migrate](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#migrate)() or
[ignore](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#ignore)() the new
access point. Once the session has roamed the
[newConfigurationActivated](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#newConfigurationActivated)()
signal is emitted. The application may now test the carrier and must either
[accept](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept)() or
[reject](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#reject)() it. The
session will return to the previous access point if the roaming was rejected. The
subsequent state diagram depicts the required state transitions.

![](https://doc.qt.io/archives/qt-5.15/images/roaming-states.png)

Some platforms may distinguish forced roaming and application level roaming (ALR). ALR
implies that the application controls (via
[migrate](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#migrate)(),
[ignore](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#ignore)(),
[accept](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept)() and
[reject](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#reject)()) whether a
network session can roam from one access point to the next. Such control is useful if
the application maintains stateful socket connections and wants to control the
transition from one interface to the next. Forced roaming implies that the system
automatically roams to the next network without consulting the application. This has the
advantage that the application can make use of roaming features without actually being
aware of it. It is expected that the application detects that the underlying socket is
broken and automatically reconnects via the new network link.

If the platform supports both modes of roaming, an application indicates its preference
by connecting to the
[preferredConfigurationChanged](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#preferredConfigurationChanged)()
signal. Connecting to this signal means that the application wants to take control over
the roaming behavior and therefore implies application level roaming. If the client does
not connect to the
[preferredConfigurationChanged](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#preferredConfigurationChanged)(),
forced roaming is used. If forced roaming is not supported the network session will not
roam by default.

Some applications may want to suppress any form of roaming altogether. Possible use
cases may be high priority downloads or remote services which cannot handle a roaming
enabled client. Clients can suppress roaming by connecting to the
[preferredConfigurationChanged](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#preferredConfigurationChanged)()
signal and answer each signal emission with
[ignore](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#ignore)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def accept(self) -> None:
        """X.accept()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkSession::accept()

Instructs the session to permanently accept the new access point. Once this function has
been called the session may not return to the old access point.

The old access point may be closed in the process if there are no other network sessions
for it. Therefore any open socket that still uses the old access point may become
unusable and should be closed before completing the migration.

Upstream PySide2 reference signatures (binding differences may apply):

```python
accept(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept"""
        ...

    def activeTime(self) -> int:
        """X.activeTime() -> int

Supplemental documentation:
Qt 5 reference:

### [quint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint64-typedef) QNetworkSession::activeTime() const

Returns the number of seconds that the session has been active.

Upstream PySide2 reference signatures (binding differences may apply):

```python
activeTime(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#activeTime"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def bytesReceived(self) -> int:
        """X.bytesReceived() -> int

Supplemental documentation:
Qt 5 reference:

### [quint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint64-typedef) QNetworkSession::bytesReceived() const

Returns the amount of data received in bytes; otherwise 0\\.

This field value includes the usage across all open network sessions which use the same
network interface.

If the session is based on a service network configuration the number of sent bytes
across all active member configurations are returned.

This function may not always be supported on all platforms and returns 0\\. The platform
capability can be detected via
[QNetworkConfigurationManager::DataStatistics](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#Capability-enum).

**Note:** On some platforms this function may run the main event loop.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesReceived(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#bytesReceived"""
        ...

    def bytesWritten(self) -> int:
        """X.bytesWritten() -> int

Supplemental documentation:
Qt 5 reference:

### [quint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint64-typedef) QNetworkSession::bytesWritten() const

Returns the amount of data sent in bytes; otherwise 0\\.

This field value includes the usage across all open network sessions which use the same
network interface.

If the session is based on a service network configuration the number of sent bytes
across all active member configurations are returned.

This function may not always be supported on all platforms and returns 0\\. The platform
capability can be detected via
[QNetworkConfigurationManager::DataStatistics](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#Capability-enum).

**Note:** On some platforms this function may run the main event loop.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesWritten(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#bytesWritten"""
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

    def close(self) -> None:
        """X.close()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkSession::close()

Decreases the session counter on the associated network configuration. If the session
counter reaches zero the active network interface is shut down. This also means that
[state](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#state)() will only
change from
[Connected](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#State-enum) to
[Disconnected](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#State-enum) if
the current session was the last open session.

If the platform does not support out-of-process sessions calling this function does not
stop the interface. In this case
[stop](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stop)() has to be used to
force a shut down. The platform capabilities can be detected via
[QNetworkConfigurationManager::capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#capabilities)().

Note that this call is asynchronous. Depending on the outcome of this call the results
can be enquired by connecting to the
[stateChanged](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stateChanged)(),
[opened](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#opened)() or
[error](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error)() signals.

**See also** [open](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open)(),
[stop](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stop)(), and
[isOpen](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#isOpen)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
close(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#close"""
        ...

    def closed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkSession.closed; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkSession::closed()

This signal is emitted when the network session has been closed.

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#closed"""
        ...

    def configuration(self) -> Any:
        """X.configuration() -> PythonQt.QtNetwork.QNetworkConfiguration

Supplemental documentation:
Qt 5 reference:

### [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html) QNetworkSession::configuration() const

Returns the QNetworkConfiguration that this network session object is based on.

**See also**
[QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
configuration(self) -> PySide2.QtNetwork.QNetworkConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#configuration"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def connectNotify(self, signal: Any) -> None:
        """X.connectNotify(signal)

Upstream PySide2 reference signatures (binding differences may apply):

```python
connectNotify(self, signal: PySide2.QtCore.QMetaMethod) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#connectNotify"""
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
        """Native PythonQt.QtNetwork.QNetworkSession.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def disconnectNotify(self, signal: Any) -> None:
        """X.disconnectNotify(signal)

Upstream PySide2 reference signatures (binding differences may apply):

```python
disconnectNotify(self, signal: PySide2.QtCore.QMetaMethod) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#disconnectNotify"""
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

    def error(self) -> Any:
        """X.error()

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkSession::error([QNetworkSession::SessionError](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#SessionError-enum) *error*)

This signal is emitted after an error occurred. The *error* parameter describes the
error that occurred.

**Note:** Signal *error* is overloaded in this class. To connect to this signal by using
the function pointer syntax, Qt provides a convenient helper for obtaining the function
pointer as shown in this example:

```
connect(networkSession, QOverload<QNetworkSession::SessionError>::of(&QNetworkSession::error),
    [=](QNetworkSession::SessionError error){ /* ... */ });
```

**See also** [error](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error)()
and
[errorString](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#errorString)().

### [QNetworkSession::SessionError](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#SessionError-enum) QNetworkSession::error() const

Returns the type of error that last occurred.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#state)()
and
[errorString](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
error(self) -> PySide2.QtNetwork.QNetworkSession.SessionError
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error"""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QNetworkSession::errorString() const

Returns a human-readable description of the last device error that occurred.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
errorString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#errorString"""
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

    def ignore(self) -> None:
        """X.ignore()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkSession::ignore()

This function indicates that the application does not wish to roam the session.

**See also**
[migrate](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#migrate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
ignore(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#ignore"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def interface(self) -> Any:
        """X.interface() -> PythonQt.QtNetwork.QNetworkInterface

Supplemental documentation:
Qt 5 reference:

### [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) QNetworkSession::interface() const

Returns the network interface that is used by this session.

This function only returns a valid
[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) when this
session is
[Connected](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#State-enum).

The returned interface may change as a result of a roaming process.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#state)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
interface(self) -> PySide2.QtNetwork.QNetworkInterface
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#interface"""
        ...

    def isOpen(self) -> bool:
        """X.isOpen() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkSession::isOpen() const

Returns `true` if this session is open. If the number of all open sessions is greater
than zero the underlying network interface will remain connected/up.

The session can be controlled via
[open](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open)() and
[close](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isOpen(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#isOpen"""
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

    def migrate(self) -> None:
        """X.migrate()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkSession::migrate()

Instructs the session to roam to the new access point. The old access point remains
active until the application calls
[accept](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept)().

The
[newConfigurationActivated](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#newConfigurationActivated)()
signal is emitted once roaming has been completed.

**See also** [accept](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
migrate(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#migrate"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def newConfigurationActivated(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkSession.newConfigurationActivated; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkSession::newConfigurationActivated()

This signal is emitted once the session has roamed to the new access point. The
application may reopen its socket and test the suitability of the new network link.
Subsequently it must either
[accept](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept)() or
[reject](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#reject)() the new
access point.

**See also** [accept](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept)()
and [reject](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#reject)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#newConfigurationActivated"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkSession.objectNameChanged; argument details are not documented."""
        ...

    def open(self) -> None:
        """X.open()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkSession::open()

Creates an open session which increases the session counter on the underlying network
interface. The system will not terminate a network interface until the session reference
counter reaches zero. Therefore an open session allows an application to register its
use of the interface.

As a result of calling open() the interface will be started if it is not connected/up
yet. Some platforms may not provide support for out-of-process sessions. On such
platforms the session counter ignores any sessions held by another process. The platform
capabilities can be detected via
[QNetworkConfigurationManager::capabilities](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#capabilities)().

Note that this call is asynchronous. Depending on the outcome of this call the results
can be enquired by connecting to the
[stateChanged](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stateChanged)(),
[opened](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#opened)() or
[error](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error)() signals.

It is not a requirement to open a session in order to monitor the underlying network
interface.

**See also** [close](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#close)(),
[stop](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stop)(), and
[isOpen](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#isOpen)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
open(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open"""
        ...

    def opened(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkSession.opened; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkSession::opened()

This signal is emitted when the network session has been opened.

The underlying network interface will not be shut down as long as the session remains
open. Note that this feature is dependent on [system wide session
support](https://doc.qt.io/archives/qt-5.15/qnetworkconfigurationmanager.html#Capability-enum).

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#opened"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def preferredConfigurationChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkSession.preferredConfigurationChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkSession::preferredConfigurationChanged(const [QNetworkConfiguration](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html) \\&*config*, bool *isSeamless*)

This signal is emitted when the preferred configuration/access point for the session
changes. Only sessions which are based on service network configurations may emit this
signal. *config* can be used to determine access point specific details such as proxy
settings and *isSeamless* indicates whether roaming will break the sessions IP address.

As a consequence to this signal the application must either start the roaming process by
calling [migrate](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#migrate)() or
choose to [ignore](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#ignore)() the
new access point.

If the roaming process is non-seamless the IP address will change which means that a
socket becomes invalid. However seamless mobility can ensure that the local IP address
does not change. This is achieved by using a virtual IP address which is bound to the
actual link address. During the roaming process the virtual address is attached to the
new link address.

Some platforms may support the concept of Forced Roaming and Application Level Roaming
(ALR). Forced roaming implies that the platform may simply roam to a new configuration
without consulting applications. It is up to the application to detect the link layer
loss and reestablish its sockets. In contrast ALR provides the opportunity to prevent
the system from roaming. If this session is based on a configuration that supports
roaming the application can choose whether it wants to be consulted (ALR use case) by
connecting to this signal. For as long as this signal connection remains the session
remains registered as a roaming stakeholder; otherwise roaming will be enforced by the
platform.

**See also**
[migrate](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#migrate)(),
[ignore](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#ignore)(), and
[QNetworkConfiguration::isRoamingAvailable](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#isRoamingAvailable)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#preferredConfigurationChanged"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def reject(self) -> None:
        """X.reject()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkSession::reject()

The new access point is not suitable for the application. By calling this function the
session returns to the previous access point/configuration. This action may invalidate
any socket that has been created via the not desired access point.

**See also** [accept](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#accept)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
reject(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#reject"""
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

    def sessionProperty(self, key: str) -> Any:
        """X.sessionProperty(key) -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QNetworkSession::sessionProperty(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*key*) const

Returns the value for property *key*.

A network session can have properties attached which may describe the session in more
details. This function can be used to gain access to those properties.

The following property keys are guaranteed to be specified on all platforms:

| Key | Description |
| --- | --- |
| ActiveConfiguration | If the session [isOpen](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#isOpen)() this property returns the identifier of the QNetworkConfiguration that is used by this session; otherwise an empty string. The main purpose of this key is to determine which Internet access point is used if the session is based on a [ServiceNetwork](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum). The following code snippet highlights the difference:  ```     QNetworkConfigurationManager mgr;     QNetworkConfiguration ap = mgr.defaultConfiguration();     QNetworkSession *session = new QNetworkSession(ap);     ... //code activates session      QString ident = session->sessionProperty("ActiveConfiguration").toString();     if ( ap.type() == QNetworkConfiguration::ServiceNetwork ) {         Q_ASSERT( ap.identifier() != ident );         Q_ASSERT( ap.children().contains( mgr.configurationFromIdentifier(ident) ) );     } else if ( ap.type() == QNetworkConfiguration::InternetAccessPoint ) {         Q_ASSERT( ap.identifier() == ident );     }                 \\endcode ``` |
| UserChoiceConfiguration | If the session [isOpen](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#isOpen)() and is bound to a QNetworkConfiguration of type UserChoice, this property returns the identifier of the QNetworkConfiguration that the configuration resolved to when [open](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open)() was called; otherwise an empty string. The purpose of this key is to determine the real QNetworkConfiguration that the session is using. This key is different from *ActiveConfiguration* in that this key may return an identifier for either a [service network](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum) or a [Internet access points](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum) configurations, whereas *ActiveConfiguration* always returns identifiers to [Internet access points](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum) configurations. |
| ConnectInBackground | Setting this property to *true* before calling [open](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open)() implies that the connection attempt is made but if no connection can be established, the user is not connsulted and asked to select a suitable connection. This property is not set by default and support for it depends on the platform. |
| AutoCloseSessionTimeout | If the session requires polling to keep its state up to date, this property holds the timeout in milliseconds before the session will automatically close. If the value of this property is -1 the session will not automatically close. This property is set to -1 by default. The purpose of this property is to minimize resource use on platforms that use polling to update the state of the session. Applications can set the value of this property to the desired timeout before the session is closed. In response to the [closed](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#closed)() signal the network session should be deleted to ensure that all polling is stopped. The session can then be recreated once it is required again. This property has no effect for sessions that do not require polling. |

**See also**
[setSessionProperty](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#setSessionProperty)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sessionProperty(self, key: str) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#sessionProperty"""
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

    def setSessionProperty(self, key: str, value: Any) -> None:
        """X.setSessionProperty(key, value)

Supplemental documentation:
Qt 5 reference:

### void QNetworkSession::setSessionProperty(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*key*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Sets the property *value* on the session. The property is identified using *key*.
Removing an already set property can be achieved by passing an invalid
[QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html).

Note that the *UserChoiceConfiguration* and *ActiveConfiguration* properties are read
only and cannot be changed using this method.

**See also**
[sessionProperty](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#sessionProperty)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSessionProperty(self, key: str, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#setSessionProperty"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def state(self) -> Any:
        """X.state()

Supplemental documentation:
Qt 5 reference:

### [QNetworkSession::State](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#State-enum) QNetworkSession::state() const

Returns the state of the session.

If the session is based on a single access point configuration the state of the session
is the same as the state of the associated network interface. Therefore a network
session object can be used to monitor network interfaces.

A
[QNetworkConfiguration::ServiceNetwork](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#Type-enum)
based session summarizes the state of all its children and therefore returns the
[Connected](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#State-enum) state if
at least one of the service network's
[children()](https://doc.qt.io/archives/qt-5.15/qnetworkconfiguration.html#children)
configurations is active.

Note that it is not required to hold an open session in order to obtain the network
interface state. A connected but closed session may be used to monitor network
interfaces whereas an open and connected session object may prevent the network
interface from being shut down.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error)()
and
[stateChanged](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stateChanged)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
state(self) -> PySide2.QtNetwork.QNetworkSession.State
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#state"""
        ...

    def stateChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkSession.stateChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkSession::stateChanged([QNetworkSession::State](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#State-enum) *state*)

This signal is emitted whenever the state of the network session changes. The *state*
parameter is the new state.

**See also** [state](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#state)().

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stateChanged"""
        ...

    def stop(self) -> None:
        """X.stop()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QNetworkSession::stop()

Invalidates all open sessions against the network interface and therefore stops the
underlying network interface. This function always changes the session's
[state](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#state)() flag to
[Disconnected](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#State-enum).

**See also** [open](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open)() and
[close](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
stop(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#stop"""
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

    def usagePolicies(self) -> Any:
        """X.usagePolicies()

Supplemental documentation:
Qt 5 reference:

### [QNetworkSession::UsagePolicies](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#UsagePolicy-enum) QNetworkSession::usagePolicies() const

Returns the network usage policies currently in force by the system.

Upstream PySide2 reference signatures (binding differences may apply):

```python
usagePolicies(self) -> PySide2.QtNetwork.QNetworkSession.UsagePolicies
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#usagePolicies"""
        ...

    def usagePoliciesChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QNetworkSession.usagePoliciesChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QNetworkSession::usagePoliciesChanged([QNetworkSession::UsagePolicies](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#UsagePolicy-enum) *usagePolicies*)

This signal is emitted when the *usagePolicies* in force are changed by the system.

This function was introduced in Qt 5.0.

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#usagePoliciesChanged"""
        ...

    def waitForOpened(self, msecs: int) -> bool:
        """X.waitForOpened(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QNetworkSession::waitForOpened(int *msecs* \\= 30000\\)

Waits until the session has been opened, up to *msecs* milliseconds. If the session has
been opened, this function returns `true`; otherwise it returns `false`. In the case
where it returns `false`, you can call
[error](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error)() to determine
the cause of the error.

The following example waits up to one second for the session to be opened:

```
    session->open();
    if (session->waitForOpened(1000))
        qDebug("Open!");
```

If *msecs* is -1, this function will not time out.

**See also** [open](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#open)() and
[error](https://doc.qt.io/archives/qt-5.15/qnetworksession.html#error)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForOpened(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qnetworksession.html#waitForOpened"""
        ...
    Closing: Any
    Connected: Any
    Connecting: Any
    Disconnected: Any
    Invalid: Any
    InvalidConfigurationError: Any
    NoBackgroundTrafficPolicy: Any
    NoPolicy: Any
    NotAvailable: Any
    OperationNotSupportedError: Any
    Roaming: Any
    RoamingError: Any
    SessionAbortedError: Any
    SessionError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    State: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    UnknownSessionError: Any
    UsagePolicies: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    UsagePolicy: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    objectName: Any

class QSsl:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Source: https://doc.qt.io/archives/qt-5.15/qssl.html"""

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
    AlternativeNameEntryType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    AnyProtocol: Any
    Der: Any
    DnsEntry: Any
    Dsa: Any
    Ec: Any
    EmailEntry: Any
    EncodingFormat: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    KeyAlgorithm: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    KeyType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Opaque: Any
    Pem: Any
    PrivateKey: Any
    PublicKey: Any
    Rsa: Any
    SecureProtocols: Any
    SslOption: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslOptionDisableCompression: Any
    SslOptionDisableEmptyFragments: Any
    SslOptionDisableLegacyRenegotiation: Any
    SslOptionDisableServerCipherPreference: Any
    SslOptionDisableServerNameIndication: Any
    SslOptionDisableSessionPersistence: Any
    SslOptionDisableSessionSharing: Any
    SslOptionDisableSessionTickets: Any
    SslOptions: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslProtocol: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslV2: Any
    SslV3: Any
    TlsV1SslV3: Any
    TlsV1_0: Any
    TlsV1_0OrLater: Any
    TlsV1_1: Any
    TlsV1_1OrLater: Any
    TlsV1_2: Any
    TlsV1_2OrLater: Any
    UnknownProtocol: Any

class QSslCertificate:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSslCertificate stores an X509 certificate, and is commonly used to verify the identity
and store information about the local host, a remotely connected peer, or a trusted
third party Certificate Authority.

There are many ways to construct a QSslCertificate. The most common way is to call
[QSslSocket::peerCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificate)(),
which returns a QSslCertificate object, or
[QSslSocket::peerCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificateChain)(),
which returns a list of them. You can also load certificates from a DER (binary) or PEM
(Base64) encoded bundle, typically stored as one or more local files, or in a Qt
Resource.

You can call [isNull](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#isNull)()
to check if your certificate is null. By default, QSslCertificate constructs a null
certificate. A null certificate is invalid, but an invalid certificate is not
necessarily null. If you want to reset all contents in a certificate, call
[clear](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#clear)().

After loading a certificate, you can find information about the certificate, its
subject, and its issuer, by calling one of the many accessor functions, including
[version](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#version)(),
[serialNumber](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#serialNumber)(),
[issuerInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#issuerInfo)() and
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)().
You can call
[effectiveDate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#effectiveDate)()
and [expiryDate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#expiryDate)()
to check when the certificate starts being effective and when it expires. The
[publicKey](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#publicKey)()
function returns the certificate subject's public key as a
[QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html). You can call
[issuerInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#issuerInfo)() or
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)() to
get detailed information about the certificate issuer and its subject.

Internally, QSslCertificate is stored as an X509 structure. You can access this handle
by calling [handle](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#handle)(),
but the results are likely to not be portable.

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def clear(self) -> None:
        """X.clear()

Supplemental documentation:
Qt 5 reference:

### void QSslCertificate::clear()

Clears the contents of this certificate, making it a null certificate.

**See also** [isNull](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#isNull)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
clear(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#clear"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def digest(self, algorithm: Any) -> Any:
        """X.digest(algorithm) -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslCertificate::digest([QCryptographicHash::Algorithm](https://doc.qt.io/archives/qt-5.15/qcryptographichash.html#Algorithm-enum) *algorithm* \\= QCryptographicHash::Md5) const

Returns a cryptographic digest of this certificate. By default, an MD5 digest will be
generated, but you can also specify a custom *algorithm*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
digest(self, algorithm: PySide2.QtCore.QCryptographicHash.Algorithm=...) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#digest"""
        ...

    def effectiveDate(self) -> Any:
        """X.effectiveDate() -> PythonQt.QtCore.QDateTime

Supplemental documentation:
Qt 5 reference:

### [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) QSslCertificate::effectiveDate() const

Returns the date-time that the certificate becomes valid, or an empty
[QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) if this is a null
certificate.

**See also**
[expiryDate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#expiryDate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
effectiveDate(self) -> PySide2.QtCore.QDateTime
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#effectiveDate"""
        ...

    def expiryDate(self) -> Any:
        """X.expiryDate() -> PythonQt.QtCore.QDateTime

Supplemental documentation:
Qt 5 reference:

### [QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) QSslCertificate::expiryDate() const

Returns the date-time that the certificate expires, or an empty
[QDateTime](https://doc.qt.io/archives/qt-5.15/qdatetime.html) if this is a null
certificate.

**See also**
[effectiveDate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#effectiveDate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
expiryDate(self) -> PySide2.QtCore.QDateTime
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#expiryDate"""
        ...

    def extensions(self) -> tuple:
        """X.extensions() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificateExtension](https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html)\\> QSslCertificate::extensions() const

Returns a list containing the X509 extensions of this certificate.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
extensions(self) -> typing.List[PySide2.QtNetwork.QSslCertificateExtension]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#extensions"""
        ...

    def fromData(self, data: Any, format: Any) -> tuple:
        """X.fromData(data, format) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#QSslCertificate)\\> QSslCertificate::fromData(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*data*, [QSsl::EncodingFormat](https://doc.qt.io/archives/qt-5.15/qssl.html#EncodingFormat-enum) *format* \\= QSsl::Pem)

Searches for and parses all certificates in *data* that are encoded in the specified
*format* and returns them in a list of certificates.

**See also**
[fromDevice](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#fromDevice)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
fromData(data: PySide2.QtCore.QByteArray, format: PySide2.QtNetwork.QSsl.EncodingFormat=...) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#fromData"""
        ...

    def fromDevice(self, device: Any, format: Any) -> tuple:
        """X.fromDevice(device, format) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#QSslCertificate)\\> QSslCertificate::fromDevice([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*, [QSsl::EncodingFormat](https://doc.qt.io/archives/qt-5.15/qssl.html#EncodingFormat-enum) *format* \\= QSsl::Pem)

Searches for and parses all certificates in *device* that are encoded in the specified
*format* and returns them in a list of certificates.

**See also**
[fromData](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#fromData)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
fromDevice(device: PySide2.QtCore.QIODevice, format: PySide2.QtNetwork.QSsl.EncodingFormat=...) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#fromDevice"""
        ...

    def fromPath(self, path: str, format: Any, syntax: Any) -> tuple:
        """X.fromPath(path, format, syntax) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#QSslCertificate)\\> QSslCertificate::fromPath(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*path*, [QSsl::EncodingFormat](https://doc.qt.io/archives/qt-5.15/qssl.html#EncodingFormat-enum) *format* \\= QSsl::Pem, [QSslCertificate::PatternSyntax](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#PatternSyntax-enum) *syntax* \\= PatternSyntax::FixedString)

Searches all files in the *path* for certificates encoded in the specified *format* and
returns them in a list. *path* must be a file or a pattern matching one or more files,
as specified by *syntax*.

Example:

```
const auto certs = QSslCertificate::fromPath("C:/ssl/certificate.*.pem",
                                             QSsl::Pem, QSslCertificate::Wildcard);
for (const QSslCertificate &cert : certs) {
    qDebug() << cert.issuerInfo(QSslCertificate::Organization);
}
```

This function was introduced in Qt 5.15.

**See also**
[fromData](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#fromData)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
fromPath(path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat, syntax: PySide2.QtCore.QRegExp.PatternSyntax) -> typing.List[PySide2.QtNetwork.QSslCertificate]
fromPath(path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat=..., syntax: PySide2.QtNetwork.QSslCertificate.PatternSyntax=...) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#fromPath"""
        ...

    def handle(self) -> int:
        """X.handle()

Supplemental documentation:
Qt 5 reference:

### [Qt::HANDLE](https://doc.qt.io/archives/qt-5.15/qt.html#HANDLE-typedef) QSslCertificate::handle() const

Returns a pointer to the native certificate handle, if there is one, else `nullptr`.

You can use this handle, together with the native API, to access extended information
about the certificate.

**Warning:** Use of this function has a high probability of being non-portable, and its
return value may vary from platform to platform or change from minor release to minor
release.

Upstream PySide2 reference signatures (binding differences may apply):

```python
handle(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#handle"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def importPkcs12(self, device: Any, key: Any, cert: Any, caCertificates: Any, passPhrase: Any) -> bool:
        """X.importPkcs12(device, key, cert, caCertificates, passPhrase) -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QSslCertificate::importPkcs12([QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) \\**device*, [QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html) \\**key*, [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#QSslCertificate) \\**certificate*, [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#QSslCertificate)\\> \\**caCertificates* \\= nullptr, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*passPhrase* \\= QByteArray())

Imports a PKCS#12 (pfx) file from the specified *device*. A PKCS#12 file is a bundle
that can contain a number of certificates and keys. This method reads a single *key*,
its *certificate* and any associated *caCertificates* from the bundle. If a *passPhrase*
is specified then this will be used to decrypt the bundle. Returns `true` if the PKCS#12
file was successfully loaded.

**Note:** The *device* must be open and ready to be read from.

This function was introduced in Qt 5.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
importPkcs12(device: PySide2.QtCore.QIODevice, key: PySide2.QtNetwork.QSslKey, cert: PySide2.QtNetwork.QSslCertificate, caCertificates: typing.Optional[typing.Sequence[PySide2.QtNetwork.QSslCertificate]]=..., passPhrase: PySide2.QtCore.QByteArray=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#importPkcs12"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isBlacklisted(self) -> bool:
        """X.isBlacklisted() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslCertificate::isBlacklisted() const

Returns `true` if this certificate is blacklisted; otherwise returns `false`.

**See also** [isNull](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#isNull)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isBlacklisted(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#isBlacklisted"""
        ...

    def isNull(self) -> bool:
        """X.isNull() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslCertificate::isNull() const

Returns `true` if this is a null certificate (i.e., a certificate with no contents);
otherwise returns `false`.

By default, [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)
constructs a null certificate.

**See also** [clear](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#clear)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#isNull"""
        ...

    def isSelfSigned(self) -> bool:
        """X.isSelfSigned() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslCertificate::isSelfSigned() const

Returns `true` if this certificate is self signed; otherwise returns `false`.

A certificate is considered self-signed its issuer and subject are identical.

This function was introduced in Qt 5.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSelfSigned(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#isSelfSigned"""
        ...

    def issuerInfo(self, info: Any) -> tuple:
        """X.issuerInfo(info) -> tuple

Supplemental documentation:
Qt 5 reference:

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QSslCertificate::issuerInfo([QSslCertificate::SubjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#SubjectInfo-enum) *subject*) const

Returns the issuer information for the *subject* from the certificate, or an empty list
if there is no information for *subject* in the certificate. There can be more than one
entry of each type.

**See also**
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)().

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QSslCertificate::issuerInfo(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*attribute*) const

Returns the issuer information for *attribute* from the certificate, or an empty list if
there is no information for *attribute* in the certificate. There can be more than one
entry for an attribute.

**See also**
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
issuerInfo(self, attribute: PySide2.QtCore.QByteArray) -> typing.List[str]
issuerInfo(self, info: PySide2.QtNetwork.QSslCertificate.SubjectInfo) -> typing.List[str]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#issuerInfo"""
        ...

    def issuerInfoAttributes(self) -> Any:
        """X.issuerInfoAttributes()

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> QSslCertificate::issuerInfoAttributes() const

Returns a list of the attributes that have values in the issuer information of this
certificate. The information associated with a given attribute can be accessed using the
[issuerInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#issuerInfo)()
method. Note that this list may include the OIDs for any elements that are not known by
the SSL backend.

This function was introduced in Qt 5.0.

**See also**
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
issuerInfoAttributes(self) -> typing.List[PySide2.QtCore.QByteArray]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#issuerInfoAttributes"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QSslCertificate"""
        ...

    def publicKey(self) -> Any:
        """X.publicKey() -> PythonQt.QtNetwork.QSslKey

Supplemental documentation:
Qt 5 reference:

### [QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html) QSslCertificate::publicKey() const

Returns the certificate subject's public key.

Upstream PySide2 reference signatures (binding differences may apply):

```python
publicKey(self) -> PySide2.QtNetwork.QSslKey
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#publicKey"""
        ...

    def serialNumber(self) -> Any:
        """X.serialNumber() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslCertificate::serialNumber() const

Returns the certificate's serial number string in hexadecimal format.

Upstream PySide2 reference signatures (binding differences may apply):

```python
serialNumber(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#serialNumber"""
        ...

    def subjectAlternativeNames(self) -> Any:
        """X.subjectAlternativeNames()

Supplemental documentation:
Qt 5 reference:

### [QMultiMap](https://doc.qt.io/archives/qt-5.15/qmultimap.html)\\<[QSsl::AlternativeNameEntryType](https://doc.qt.io/archives/qt-5.15/qssl.html#AlternativeNameEntryType-enum), [QString](https://doc.qt.io/archives/qt-5.15/qstring.html)\\> QSslCertificate::subjectAlternativeNames() const

Returns the list of alternative subject names for this certificate. The alternative
names typically contain host names, optionally with wildcards, that are valid for this
certificate.

These names are tested against the connected peer's host name, if either the subject
information for
[CommonName](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#SubjectInfo-enum)
doesn't define a valid host name, or the subject info name doesn't match the peer's host
name.

**See also**
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
subjectAlternativeNames(self) -> typing.Dict[PySide2.QtNetwork.QSsl.AlternativeNameEntryType, typing.List[str]]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectAlternativeNames"""
        ...

    def subjectInfo(self, info: Any) -> tuple:
        """X.subjectInfo(info) -> tuple

Supplemental documentation:
Qt 5 reference:

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QSslCertificate::subjectInfo([QSslCertificate::SubjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#SubjectInfo-enum) *subject*) const

Returns the information for the *subject*, or an empty list if there is no information
for *subject* in the certificate. There can be more than one entry of each type.

**See also**
[issuerInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#issuerInfo)().

### [QStringList](https://doc.qt.io/archives/qt-5.15/qstringlist.html) QSslCertificate::subjectInfo(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*attribute*) const

Returns the subject information for *attribute*, or an empty list if there is no
information for *attribute* in the certificate. There can be more than one entry for an
attribute.

**See also**
[issuerInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#issuerInfo)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
subjectInfo(self, attribute: PySide2.QtCore.QByteArray) -> typing.List[str]
subjectInfo(self, info: PySide2.QtNetwork.QSslCertificate.SubjectInfo) -> typing.List[str]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo"""
        ...

    def subjectInfoAttributes(self) -> Any:
        """X.subjectInfoAttributes()

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> QSslCertificate::subjectInfoAttributes() const

Returns a list of the attributes that have values in the subject information of this
certificate. The information associated with a given attribute can be accessed using the
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)()
method. Note that this list may include the OIDs for any elements that are not known by
the SSL backend.

This function was introduced in Qt 5.0.

**See also**
[subjectInfo](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfo)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
subjectInfoAttributes(self) -> typing.List[PySide2.QtCore.QByteArray]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#subjectInfoAttributes"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QSslCertificate::swap([QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#QSslCertificate) \\&*other*)

Swaps this certificate instance with *other*. This function is very fast and never
fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QSslCertificate) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#swap"""
        ...

    def toDer(self) -> Any:
        """X.toDer() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslCertificate::toDer() const

Returns this certificate converted to a DER (binary) encoded representation.

Upstream PySide2 reference signatures (binding differences may apply):

```python
toDer(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#toDer"""
        ...

    def toPem(self) -> Any:
        """X.toPem() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslCertificate::toPem() const

Returns this certificate converted to a PEM (Base64) encoded representation.

Upstream PySide2 reference signatures (binding differences may apply):

```python
toPem(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#toPem"""
        ...

    def toText(self) -> str:
        """X.toText() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCertificate::toText() const

Returns this certificate converted to a human-readable text representation.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
toText(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#toText"""
        ...

    def verify(self, certificateChain: Any, hostName: str) -> tuple:
        """X.verify(certificateChain, hostName) -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html)\\> QSslCertificate::verify([QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#QSslCertificate)\\> *certificateChain*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName* \\= QString())

Verifies a certificate chain. The chain to be verified is passed in the
*certificateChain* parameter. The first certificate in the list should be the leaf
certificate of the chain to be verified. If *hostName* is specified then the certificate
is also checked to see if it is valid for the specified host name.

Note that the root (CA) certificate should not be included in the list to be verified,
this will be looked up automatically using the CA list specified in the default
[QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html), and, in
addition, if possible, CA certificates loaded on demand on Unix and Windows.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
verify(certificateChain: typing.Sequence[PySide2.QtNetwork.QSslCertificate], hostName: str=...) -> typing.List[PySide2.QtNetwork.QSslError]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#verify"""
        ...

    def version(self) -> Any:
        """X.version() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslCertificate::version() const

Returns the certificate's version string.

Upstream PySide2 reference signatures (binding differences may apply):

```python
version(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificate.html#version"""
        ...
    CommonName: Any
    CountryName: Any
    DistinguishedNameQualifier: Any
    EmailAddress: Any
    LocalityName: Any
    Organization: Any
    OrganizationalUnitName: Any
    SerialNumber: Any
    StateOrProvinceName: Any
    SubjectInfo: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"

class QSslCertificateExtension:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSslCertificateExtension provides access to an extension stored in an X509 certificate.
The information available depends on the type of extension being accessed.

All X509 certificate extensions have the following properties:

| Property | Description |
| --- | --- |
| name | The human readable name of the extension, eg. 'basicConstraints'. |
| criticality | This is a boolean value indicating if the extension is critical to correctly interpreting the certificate. |
| oid | The ASN.1 object identifier that specifies which extension this is. |
| supported | If this is true the structure of the extension's value will not change between Qt versions. |
| value | A [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) with a structure dependent on the type of extension. |

Whilst this class provides access to any type of extension, only some are guaranteed to
be returned in a format that will remain unchanged between releases. The
[isSupported](https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#isSupported)()
method returns `true` for extensions where this is the case.

The extensions currently supported, and the structure of the value returned are as
follows:

| Name | OID | Details |
| --- | --- | --- |
| basicConstraints | 2.5.29.19 | Returned as a [QVariantMap](https://doc.qt.io/archives/qt-5.15/qvariant.html#QVariantMap-typedef). The key 'ca' contains a boolean value, the optional key 'pathLenConstraint' contains an integer. |
| authorityInfoAccess | 1.3.6.1.5.5.7.1.1 | Returned as a [QVariantMap](https://doc.qt.io/archives/qt-5.15/qvariant.html#QVariantMap-typedef). There is a key for each access method, with the value being a URI. |
| subjectKeyIdentifier | 2.5.29.14 | Returned as a [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) containing a [QString](https://doc.qt.io/archives/qt-5.15/qstring.html). The string is the key identifier. |
| authorityKeyIdentifier | 2.5.29.35 | Returned as a [QVariantMap](https://doc.qt.io/archives/qt-5.15/qvariant.html#QVariantMap-typedef). The optional key 'keyid' contains the key identifier as a hex string stored in a [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html). The optional key 'serial' contains the authority key serial number as a qlonglong. Currently there is no support for the general names field of this extension. |

In addition to the supported extensions above, many other common extensions will be
returned in a reasonably structured way. Extensions that the SSL backend has no support
for at all will be returned as a
[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html).

Further information about the types of extensions certificates can contain can be found
in RFC 5280\\.

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html"""

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

    def isCritical(self) -> bool:
        """X.isCritical() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslCertificateExtension::isCritical() const

Returns the criticality of the extension.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isCritical(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#isCritical"""
        ...

    def isSupported(self) -> bool:
        """X.isSupported() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslCertificateExtension::isSupported() const

Returns the true if this extension is supported. In this case, supported simply means
that the structure of the [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html)
returned by the
[value](https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#value)()
accessor will remain unchanged between versions. Unsupported extensions can be freely
used, however there is no guarantee that the returned data will have the same structure
between versions.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSupported(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#isSupported"""
        ...

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCertificateExtension::name() const

Returns the name of the extension. If no name is known for the extension then the OID
will be returned.

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#name"""
        ...

    def oid(self) -> str:
        """X.oid() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCertificateExtension::oid() const

Returns the ASN.1 OID of this extension.

Upstream PySide2 reference signatures (binding differences may apply):

```python
oid(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#oid"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QSslCertificateExtension"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QSslCertificateExtension::swap([QSslCertificateExtension](https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#QSslCertificateExtension) \\&*other*)

Swaps this certificate extension instance with *other*. This function is very fast and
never fails.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QSslCertificateExtension) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#swap"""
        ...

    def value(self) -> Any:
        """X.value() -> object

Supplemental documentation:
Qt 5 reference:

### [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QSslCertificateExtension::value() const

Returns the value of the extension. The structure of the value returned depends on the
extension type.

Upstream PySide2 reference signatures (binding differences may apply):

```python
value(self) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcertificateextension.html#value"""
        ...

class QSslCipher:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSslCipher stores information about one cryptographic cipher. It is most commonly used
with [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html), either for
configuring which ciphers the socket can use, or for displaying the socket's ciphers to
the user.

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def authenticationMethod(self) -> str:
        """X.authenticationMethod() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCipher::authenticationMethod() const

Returns the cipher's authentication method as a
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
authenticationMethod(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#authenticationMethod"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def encryptionMethod(self) -> str:
        """X.encryptionMethod() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCipher::encryptionMethod() const

Returns the cipher's encryption method as a
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
encryptionMethod(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#encryptionMethod"""
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

### bool QSslCipher::isNull() const

Returns `true` if this is a null cipher; otherwise returns `false`.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#isNull"""
        ...

    def keyExchangeMethod(self) -> str:
        """X.keyExchangeMethod() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCipher::keyExchangeMethod() const

Returns the cipher's key exchange method as a
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
keyExchangeMethod(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#keyExchangeMethod"""
        ...

    def name(self) -> str:
        """X.name() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCipher::name() const

Returns the name of the cipher, or an empty
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html) if this is a null cipher.

**See also** [isNull](https://doc.qt.io/archives/qt-5.15/qsslcipher.html#isNull)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
name(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QSslCipher"""
        ...

    def protocol(self) -> Any:
        """X.protocol()

Supplemental documentation:
Qt 5 reference:

### [QSsl::SslProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum) QSslCipher::protocol() const

Returns the cipher's protocol type, or
[QSsl::UnknownProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum)
if [QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html) is unable to
determine the protocol
([protocolString](https://doc.qt.io/archives/qt-5.15/qsslcipher.html#protocolString)()
may contain more information).

**See also**
[protocolString](https://doc.qt.io/archives/qt-5.15/qsslcipher.html#protocolString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
protocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#protocol"""
        ...

    def protocolString(self) -> str:
        """X.protocolString() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslCipher::protocolString() const

Returns the cipher's protocol as a
[QString](https://doc.qt.io/archives/qt-5.15/qstring.html).

**See also** [protocol](https://doc.qt.io/archives/qt-5.15/qsslcipher.html#protocol)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
protocolString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#protocolString"""
        ...

    def supportedBits(self) -> int:
        """X.supportedBits() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslCipher::supportedBits() const

Returns the number of bits supported by the cipher.

**See also** [usedBits](https://doc.qt.io/archives/qt-5.15/qsslcipher.html#usedBits)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
supportedBits(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#supportedBits"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QSslCipher::swap([QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html#QSslCipher) \\&*other*)

Swaps this cipher instance with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QSslCipher) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#swap"""
        ...

    def usedBits(self) -> int:
        """X.usedBits() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslCipher::usedBits() const

Returns the number of bits used by the cipher.

**See also**
[supportedBits](https://doc.qt.io/archives/qt-5.15/qsslcipher.html#supportedBits)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
usedBits(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslcipher.html#usedBits"""
        ...

class QSslConfiguration:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSslConfiguration is used by Qt networking classes to relay information about an open
SSL connection and to allow the application to control certain features of that
connection.

The settings that QSslConfiguration currently supports are:

- The SSL/TLS protocol to be used
- The certificate to be presented to the peer during connection and its associated private key
- The ciphers allowed to be used for encrypting the connection
- The list of Certificate Authorities certificates that are used to validate the peer's certificate

These settings are applied only during the connection handshake. Setting them after the
connection has been established has no effect.

The state that QSslConfiguration supports are:

- The certificate the peer presented during handshake, along with the chain leading to a CA certificate
- The cipher used to encrypt this session

The state can only be obtained once the SSL connection starts, but not necessarily
before it's done. Some settings may change during the course of the SSL connection
without need to restart it (for instance, the cipher can be changed over time).

State in QSslConfiguration objects cannot be changed.

QSslConfiguration can be used with
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) and the Network Access
API.

Note that changing settings in QSslConfiguration is not enough to change the settings in
the related SSL connection. You must call setSslConfiguration on a modified
QSslConfiguration object to achieve that. The following example illustrates how to
change the protocol to TLSv1\\_0 in a
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) object:

```
QSslConfiguration config = sslSocket.sslConfiguration();
config.setProtocol(QSsl::TlsV1_0);
sslSocket.setSslConfiguration(config);
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def allowedNextProtocols(self) -> Any:
        """X.allowedNextProtocols()

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> QSslConfiguration::allowedNextProtocols() const

This function returns the allowed protocols to be negotiated with the server through the
Next Protocol Negotiation (NPN) or Application-Layer Protocol Negotiation (ALPN) TLS
extension, as set by
[setAllowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setAllowedNextProtocols)().

This function was introduced in Qt 5.3.

**See also**
[nextNegotiatedProtocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextNegotiatedProtocol)(),
[nextProtocolNegotiationStatus](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextProtocolNegotiationStatus)(),
[setAllowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setAllowedNextProtocols)(),
[QSslConfiguration::NextProtocolSpdy3\\_0](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolSpdy3_0-var),
and
[QSslConfiguration::NextProtocolHttp1\\_1](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolHttp1_1-var).

Upstream PySide2 reference signatures (binding differences may apply):

```python
allowedNextProtocols(self) -> typing.List[PySide2.QtCore.QByteArray]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#allowedNextProtocols"""
        ...

    def caCertificates(self) -> tuple:
        """X.caCertificates() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> QSslConfiguration::caCertificates() const

Returns this connection's CA certificate database. The CA certificate database is used
by the socket during the handshake phase to validate the peer's certificate. It can be
modified prior to the handshake with
[setCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCaCertificates)(),
or with
[addCaCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificate)()
and
[addCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificates)().

**See also**
[setCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCaCertificates)(),
[addCaCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificate)(),
and
[addCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificates)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
caCertificates(self) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#caCertificates"""
        ...

    def ciphers(self) -> tuple:
        """X.ciphers() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html)\\> QSslConfiguration::ciphers() const

Returns this connection's current cryptographic cipher suite. This list is used during
the handshake phase for choosing a session cipher. The returned list of ciphers is
ordered by descending preference. (i.e., the first cipher in the list is the most
preferred cipher). The session cipher will be the first one in the list that is also
supported by the peer.

By default, the handshake phase can choose any of the ciphers supported by this system's
SSL libraries, which may vary from system to system. The list of ciphers supported by
this system's SSL libraries is returned by QSslSocket::supportedCiphers(). You can
restrict the list of ciphers used for choosing the session cipher for this socket by
calling
[setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)()
with a subset of the supported ciphers. You can revert to using the entire set by
calling
[setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)()
with the list returned by QSslSocket::supportedCiphers().

**Note:** This is not currently supported in the Schannel backend.

**See also**
[setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)() and
[QSslSocket::supportedCiphers](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#supportedCiphers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
ciphers(self) -> typing.List[PySide2.QtNetwork.QSslCipher]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ciphers"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def defaultConfiguration(self) -> Any:
        """X.defaultConfiguration() -> PythonQt.QtNetwork.QSslConfiguration

Supplemental documentation:
Qt 5 reference:

### `[static]` [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#QSslConfiguration) QSslConfiguration::defaultConfiguration()

Returns the default SSL configuration to be used in new SSL connections.

The default SSL configuration consists of:

- no local certificate and no private key
- protocol [SecureProtocols](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum)
- the system's default CA certificate list
- the cipher list equal to the list of the SSL libraries' supported SSL ciphers that are 128 bits or more

**See also**
[QSslSocket::supportedCiphers](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#supportedCiphers)()
and
[setDefaultConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setDefaultConfiguration)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
defaultConfiguration() -> PySide2.QtNetwork.QSslConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#defaultConfiguration"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def ellipticCurves(self) -> tuple:
        """X.ellipticCurves() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html)\\> QSslConfiguration::ellipticCurves() const

Returns this connection's current list of elliptic curves. This list is used during the
handshake phase for choosing an elliptic curve (when using an elliptic curve cipher).
The returned list of curves is ordered by descending preference (i.e., the first curve
in the list is the most preferred one).

By default, the handshake phase can choose any of the curves supported by this system's
SSL libraries, which may vary from system to system. The list of curves supported by
this system's SSL libraries is returned by QSslSocket::supportedEllipticCurves().

You can restrict the list of curves used for choosing the session cipher for this socket
by calling
[setEllipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setEllipticCurves)()
with a subset of the supported ciphers. You can revert to using the entire set by
calling
[setEllipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setEllipticCurves)()
with the list returned by QSslSocket::supportedEllipticCurves().

This function was introduced in Qt 5.5.

**See also**
[setEllipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setEllipticCurves).

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ellipticCurves"""
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

### bool QSslConfiguration::isNull() const

Returns `true` if this is a null
[QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) object.

A [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) object
is null if it has been default-constructed and no setter methods have been called.

**See also**
[setProtocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setProtocol)(),
[setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificate)(),
[setPrivateKey](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPrivateKey)(),
[setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)(),
and
[setCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCaCertificates)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#isNull"""
        ...

    def localCertificate(self) -> Any:
        """X.localCertificate() -> PythonQt.QtNetwork.QSslCertificate

Supplemental documentation:
Qt 5 reference:

### [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) QSslConfiguration::localCertificate() const

Returns the certificate to be presented to the peer during the SSL handshake process.

**See also**
[setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localCertificate(self) -> PySide2.QtNetwork.QSslCertificate
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#localCertificate"""
        ...

    def localCertificateChain(self) -> tuple:
        """X.localCertificateChain() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> QSslConfiguration::localCertificateChain() const

Returns the certificate chain to be presented to the peer during the SSL handshake
process.

This function was introduced in Qt 5.1.

**See also**
[setLocalCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificateChain)()
and
[localCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#localCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#localCertificateChain"""
        ...

    def nextNegotiatedProtocol(self) -> Any:
        """X.nextNegotiatedProtocol() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslConfiguration::nextNegotiatedProtocol() const

This function returns the protocol negotiated with the server if the Next Protocol
Negotiation (NPN) or Application-Layer Protocol Negotiation (ALPN) TLS extension was
enabled. In order for the NPN/ALPN extension to be enabled,
[setAllowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setAllowedNextProtocols)()
needs to be called explicitly before connecting to the server.

If no protocol could be negotiated or the extension was not enabled, this function
returns a [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) which is
null.

This function was introduced in Qt 5.3.

**See also**
[setAllowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setAllowedNextProtocols)()
and
[nextProtocolNegotiationStatus](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextProtocolNegotiationStatus)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
nextNegotiatedProtocol(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextNegotiatedProtocol"""
        ...

    def nextProtocolNegotiationStatus(self) -> Any:
        """X.nextProtocolNegotiationStatus()

Supplemental documentation:
Qt 5 reference:

### [QSslConfiguration::NextProtocolNegotiationStatus](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolNegotiationStatus-enum) QSslConfiguration::nextProtocolNegotiationStatus() const

This function returns the status of the Next Protocol Negotiation (NPN) or
Application-Layer Protocol Negotiation (ALPN). If the feature has not been enabled
through
[setAllowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setAllowedNextProtocols)(),
this function returns
[NextProtocolNegotiationNone](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolNegotiationStatus-enum).
The status will be set before emitting the encrypted() signal.

This function was introduced in Qt 5.3.

**See also**
[setAllowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setAllowedNextProtocols)(),
[allowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#allowedNextProtocols)(),
[nextNegotiatedProtocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextNegotiatedProtocol)(),
and
[QSslConfiguration::NextProtocolNegotiationStatus](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolNegotiationStatus-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
nextProtocolNegotiationStatus(self) -> PySide2.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextProtocolNegotiationStatus"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QSslConfiguration"""
        ...

    def peerCertificate(self) -> Any:
        """X.peerCertificate() -> PythonQt.QtNetwork.QSslCertificate

Supplemental documentation:
Qt 5 reference:

### [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) QSslConfiguration::peerCertificate() const

Returns the peer's digital certificate (i.e., the immediate certificate of the host you
are connected to), or a null certificate, if the peer has not assigned a certificate.

The peer certificate is checked automatically during the handshake phase, so this
function is normally used to fetch the certificate for display or for connection
diagnostic purposes. It contains information about the peer, including its host name,
the certificate issuer, and the peer's public key.

Because the peer certificate is set during the handshake phase, it is safe to access the
peer certificate from a slot connected to the QSslSocket::sslErrors() signal,
[QNetworkReply::sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)()
signal, or the
[QSslSocket::encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)()
signal.

If a null certificate is returned, it can mean the SSL handshake failed, or it can mean
the host you are connected to doesn't have a certificate, or it can mean there is no
connection.

If you want to check the peer's complete chain of certificates, use
[peerCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerCertificateChain)()
to get them all at once.

**See also**
[peerCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerCertificateChain)(),
[QSslSocket::sslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#sslErrors)(),
[QSslSocket::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)(),
[QNetworkReply::sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)(),
and
[QNetworkReply::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerCertificate(self) -> PySide2.QtNetwork.QSslCertificate
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerCertificate"""
        ...

    def peerCertificateChain(self) -> tuple:
        """X.peerCertificateChain() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> QSslConfiguration::peerCertificateChain() const

Returns the peer's chain of digital certificates, starting with the peer's immediate
certificate and ending with the CA's certificate.

Peer certificates are checked automatically during the handshake phase. This function is
normally used to fetch certificates for display, or for performing connection
diagnostics. Certificates contain information about the peer and the certificate
issuers, including host name, issuer names, and issuer public keys.

Because the peer certificate is set during the handshake phase, it is safe to access the
peer certificate from a slot connected to the QSslSocket::sslErrors() signal,
[QNetworkReply::sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)()
signal, or the
[QSslSocket::encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)()
signal.

If an empty list is returned, it can mean the SSL handshake failed, or it can mean the
host you are connected to doesn't have a certificate, or it can mean there is no
connection.

If you want to get only the peer's immediate certificate, use
[peerCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerCertificate)().

**See also**
[peerCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerCertificate)(),
[QSslSocket::sslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#sslErrors)(),
[QSslSocket::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)(),
[QNetworkReply::sslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#sslErrors)(),
and
[QNetworkReply::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qnetworkreply.html#ignoreSslErrors)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerCertificateChain"""
        ...

    def peerVerifyDepth(self) -> int:
        """X.peerVerifyDepth() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslConfiguration::peerVerifyDepth() const

Returns the maximum number of certificates in the peer's certificate chain to be checked
during the SSL handshake phase, or 0 (the default) if no maximum depth has been set,
indicating that the whole certificate chain should be checked.

The certificates are checked in issuing order, starting with the peer's own certificate,
then its issuer's certificate, and so on.

**See also**
[setPeerVerifyDepth](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPeerVerifyDepth)()
and
[peerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerVerifyMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerVerifyDepth(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerVerifyDepth"""
        ...

    def peerVerifyMode(self) -> Any:
        """X.peerVerifyMode()

Supplemental documentation:
Qt 5 reference:

### [QSslSocket::PeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) QSslConfiguration::peerVerifyMode() const

Returns the verify mode. This mode decides whether
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) should request a
certificate from the peer (i.e., the client requests a certificate from the server, or a
server requesting a certificate from the client), and whether it should require that
this certificate is valid.

The default mode is AutoVerifyPeer, which tells
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to use VerifyPeer for
clients, QueryPeer for servers.

**See also**
[setPeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPeerVerifyMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerVerifyMode(self) -> PySide2.QtNetwork.QSslSocket.PeerVerifyMode
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerVerifyMode"""
        ...

    def privateKey(self) -> Any:
        """X.privateKey() -> PythonQt.QtNetwork.QSslKey

Supplemental documentation:
Qt 5 reference:

### [QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html) QSslConfiguration::privateKey() const

Returns the [SSL key](https://doc.qt.io/archives/qt-5.15/qsslkey.html) assigned to this
connection or a null key if none has been assigned yet.

**See also**
[setPrivateKey](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPrivateKey)()
and
[localCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#localCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
privateKey(self) -> PySide2.QtNetwork.QSslKey
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#privateKey"""
        ...

    def protocol(self) -> Any:
        """X.protocol()

Supplemental documentation:
Qt 5 reference:

### [QSsl::SslProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum) QSslConfiguration::protocol() const

Returns the protocol setting for this SSL configuration.

**See also**
[setProtocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setProtocol)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
protocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#protocol"""
        ...

    def sessionCipher(self) -> Any:
        """X.sessionCipher() -> PythonQt.QtNetwork.QSslCipher

Supplemental documentation:
Qt 5 reference:

### [QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html) QSslConfiguration::sessionCipher() const

Returns the socket's cryptographic
[cipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html), or a null cipher if the
connection isn't encrypted. The socket's cipher for the session is set during the
handshake phase. The cipher is used to encrypt and decrypt data transmitted through the
socket.

The SSL infrastructure also provides functions for setting the ordered list of ciphers
from which the handshake phase will eventually select the session cipher. This ordered
list must be in place before the handshake phase begins.

**See also**
[ciphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ciphers)(),
[setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)(),
and
[QSslSocket::supportedCiphers](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#supportedCiphers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sessionCipher(self) -> PySide2.QtNetwork.QSslCipher
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionCipher"""
        ...

    def sessionProtocol(self) -> Any:
        """X.sessionProtocol()

Supplemental documentation:
Qt 5 reference:

### [QSsl::SslProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum) QSslConfiguration::sessionProtocol() const

Returns the socket's SSL/TLS protocol or UnknownProtocol if the connection isn't
encrypted. The socket's protocol for the session is set during the handshake phase.

This function was introduced in Qt 5.4.

**See also**
[protocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#protocol)() and
[setProtocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setProtocol)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sessionProtocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionProtocol"""
        ...

    def sessionTicket(self) -> Any:
        """X.sessionTicket() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslConfiguration::sessionTicket() const

If
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum)
was turned off, this function returns the session ticket used in the SSL handshake in
ASN.1 format, suitable to e.g. be persisted to disk. If no session ticket was used or
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum)
was not turned off, this function returns an empty
[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html).

**Note:** When persisting the session ticket to disk or similar, be careful not to
expose the session to a potential attacker, as knowledge of the session allows for
eavesdropping on data encrypted with the session parameters.

This function was introduced in Qt 5.2.

**See also**
[setSessionTicket](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setSessionTicket)(),
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum),
[setSslOption](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setSslOption)(),
and
[QSslSocket::newSessionTicketReceived](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#newSessionTicketReceived)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sessionTicket(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionTicket"""
        ...

    def sessionTicketLifeTimeHint(self) -> int:
        """X.sessionTicketLifeTimeHint() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslConfiguration::sessionTicketLifeTimeHint() const

If
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum)
was turned off, this function returns the session ticket life time hint sent by the
server (which might be 0). If the server did not send a session ticket (e.g. when
resuming a session or when the server does not support it) or
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum)
was not turned off, this function returns -1.

This function was introduced in Qt 5.2.

**See also**
[sessionTicket](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionTicket)(),
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum),
[setSslOption](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setSslOption)(),
and
[QSslSocket::newSessionTicketReceived](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#newSessionTicketReceived)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sessionTicketLifeTimeHint(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionTicketLifeTimeHint"""
        ...

    def setAllowedNextProtocols(self, protocols: Any) -> None:
        """X.setAllowedNextProtocols(protocols)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setAllowedNextProtocols([QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html)\\> *protocols*)

This function sets the allowed *protocols* to be negotiated with the server through the
Next Protocol Negotiation (NPN) or Application-Layer Protocol Negotiation (ALPN) TLS
extension; each element in *protocols* must define one allowed protocol. The function
must be called explicitly before connecting to send the NPN/ALPN extension in the SSL
handshake. Whether or not the negotiation succeeded can be queried through
[nextProtocolNegotiationStatus](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextProtocolNegotiationStatus)().

This function was introduced in Qt 5.3.

**See also**
[nextNegotiatedProtocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextNegotiatedProtocol)(),
[nextProtocolNegotiationStatus](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#nextProtocolNegotiationStatus)(),
[allowedNextProtocols](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#allowedNextProtocols)(),
[QSslConfiguration::NextProtocolSpdy3\\_0](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolSpdy3_0-var),
and
[QSslConfiguration::NextProtocolHttp1\\_1](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#NextProtocolHttp1_1-var).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAllowedNextProtocols(self, protocols: typing.Sequence[PySide2.QtCore.QByteArray]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setAllowedNextProtocols"""
        ...

    def setCaCertificates(self, certificates: Any) -> None:
        """X.setCaCertificates(certificates)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setCaCertificates(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> \\&*certificates*)

Sets this socket's CA certificate database to be *certificates*. The certificate
database must be set prior to the SSL handshake. The CA certificate database is used by
the socket during the handshake phase to validate the peer's certificate.

**Note:** The default configuration uses the system CA certificate database. If that is
not available (as is commonly the case on iOS), the default database is empty.

**See also**
[caCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#caCertificates)(),
[addCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificates)(),
and
[addCaCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCaCertificates(self, certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCaCertificates"""
        ...

    def setCiphers(self, ciphers: Any) -> None:
        """X.setCiphers(ciphers)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setCiphers(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html)\\> \\&*ciphers*)

Sets the cryptographic cipher suite for this socket to *ciphers*, which must contain a
subset of the ciphers in the list returned by
[supportedCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#supportedCiphers)().

Restricting the cipher suite must be done before the handshake phase, where the session
cipher is chosen.

**Note:** This is not currently supported in the Schannel backend.

**See also**
[ciphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ciphers)() and
[QSslSocket::supportedCiphers](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#supportedCiphers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCiphers(self, ciphers: typing.Sequence[PySide2.QtNetwork.QSslCipher]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers"""
        ...

    def setDefaultConfiguration(self, configuration: Any) -> None:
        """X.setDefaultConfiguration(configuration)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QSslConfiguration::setDefaultConfiguration(const [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#QSslConfiguration) \\&*configuration*)

Sets the default SSL configuration to be used in new SSL connections to be
*configuration*. Existing connections are not affected by this call.

**See also**
[QSslSocket::supportedCiphers](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#supportedCiphers)()
and
[defaultConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#defaultConfiguration)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDefaultConfiguration(configuration: PySide2.QtNetwork.QSslConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setDefaultConfiguration"""
        ...

    def setEllipticCurves(self, curves: Any) -> Any:
        """X.setEllipticCurves(curves)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setEllipticCurves(const [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html)\\> \\&*curves*)

Sets the list of elliptic curves to be used by this socket to *curves*, which must
contain a subset of the curves in the list returned by
[supportedEllipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#supportedEllipticCurves)().

Restricting the elliptic curves must be done before the handshake phase, where the
session cipher is chosen.

This function was introduced in Qt 5.5.

**See also**
[ellipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ellipticCurves).

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setEllipticCurves"""
        ...

    def setLocalCertificate(self, certificate: Any) -> None:
        """X.setLocalCertificate(certificate)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setLocalCertificate(const [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) \\&*certificate*)

Sets the certificate to be presented to the peer during SSL handshake to be
*certificate*.

Setting the certificate once the connection has been established has no effect.

A certificate is the means of identification used in the SSL process. The local
certificate is used by the remote end to verify the local user's identity against its
list of Certification Authorities. In most cases, such as in HTTP web browsing, only
servers identify to the clients, so the client does not send a certificate.

**See also**
[localCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#localCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLocalCertificate(self, certificate: PySide2.QtNetwork.QSslCertificate) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificate"""
        ...

    def setLocalCertificateChain(self, localChain: Any) -> None:
        """X.setLocalCertificateChain(localChain)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setLocalCertificateChain(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> \\&*localChain*)

Sets the certificate chain to be presented to the peer during the SSL handshake to be
*localChain*.

Setting the certificate chain once the connection has been established has no effect.

A certificate is the means of identification used in the SSL process. The local
certificate is used by the remote end to verify the local user's identity against its
list of Certification Authorities. In most cases, such as in HTTP web browsing, only
servers identify to the clients, so the client does not send a certificate.

Unlike
[QSslConfiguration::setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificate)()
this method allows you to specify any intermediate certificates required in order to
validate your certificate. The first item in the list must be the leaf certificate.

This function was introduced in Qt 5.1.

**See also**
[localCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#localCertificateChain)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLocalCertificateChain(self, localChain: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificateChain"""
        ...

    def setPeerVerifyDepth(self, depth: int) -> None:
        """X.setPeerVerifyDepth(depth)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setPeerVerifyDepth(int *depth*)

Sets the maximum number of certificates in the peer's certificate chain to be checked
during the SSL handshake phase, to *depth*. Setting a depth of 0 means that no maximum
depth is set, indicating that the whole certificate chain should be checked.

The certificates are checked in issuing order, starting with the peer's own certificate,
then its issuer's certificate, and so on.

**See also**
[peerVerifyDepth](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerVerifyDepth)()
and
[setPeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPeerVerifyMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerVerifyDepth(self, depth: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPeerVerifyDepth"""
        ...

    def setPeerVerifyMode(self, mode: Any) -> None:
        """X.setPeerVerifyMode(mode)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setPeerVerifyMode([QSslSocket::PeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) *mode*)

Sets the verify mode to *mode*. This mode decides whether
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) should request a
certificate from the peer (i.e., the client requests a certificate from the server, or a
server requesting a certificate from the client), and whether it should require that
this certificate is valid.

The default mode is AutoVerifyPeer, which tells
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to use VerifyPeer for
clients, QueryPeer for servers.

**See also**
[peerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#peerVerifyMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerVerifyMode(self, mode: PySide2.QtNetwork.QSslSocket.PeerVerifyMode) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPeerVerifyMode"""
        ...

    def setPrivateKey(self, key: Any) -> None:
        """X.setPrivateKey(key)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setPrivateKey(const [QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html) \\&*key*)

Sets the connection's private [key](https://doc.qt.io/archives/qt-5.15/qsslkey.html) to
*key*. The private key and the local
[certificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) are used by
clients and servers that must prove their identity to SSL peers.

Both the key and the local certificate are required if you are creating an SSL server
socket. If you are creating an SSL client socket, the key and local certificate are
required if your client must identify itself to an SSL server.

**See also**
[privateKey](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#privateKey)() and
[setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPrivateKey(self, key: PySide2.QtNetwork.QSslKey) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setPrivateKey"""
        ...

    def setProtocol(self, protocol: Any) -> None:
        """X.setProtocol(protocol)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setProtocol([QSsl::SslProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum) *protocol*)

Sets the protocol setting for this configuration to be *protocol*.

Setting the protocol once the connection has already been established has no effect.

**See also**
[protocol](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#protocol)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProtocol(self, protocol: PySide2.QtNetwork.QSsl.SslProtocol) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setProtocol"""
        ...

    def setSessionTicket(self, sessionTicket: Any) -> None:
        """X.setSessionTicket(sessionTicket)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setSessionTicket(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*sessionTicket*)

Sets the session ticket to be used in an SSL handshake.
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum)
must be turned off for this to work, and *sessionTicket* must be in ASN.1 format as
returned by
[sessionTicket](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionTicket)().

This function was introduced in Qt 5.2.

**See also**
[sessionTicket](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionTicket)(),
[QSsl::SslOptionDisableSessionPersistence](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum),
[setSslOption](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setSslOption)(),
and
[QSslSocket::newSessionTicketReceived](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#newSessionTicketReceived)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSessionTicket(self, sessionTicket: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setSessionTicket"""
        ...

    def setSslOption(self, option: Any, on: bool) -> None:
        """X.setSslOption(option, on)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::setSslOption([QSsl::SslOption](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum) *option*, bool *on*)

Enables or disables an SSL compatibility *option*. If *on* is true, the *option* is
enabled. If *on* is false, the *option* is disabled.

**See also**
[testSslOption](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#testSslOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSslOption(self, option: PySide2.QtNetwork.QSsl.SslOption, on: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setSslOption"""
        ...

    def supportedCiphers(self) -> tuple:
        """X.supportedCiphers() -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html)\\> QSslConfiguration::supportedCiphers()

Returns the list of cryptographic ciphers supported by this system. This list is set by
the system's SSL libraries and may vary from system to system.

This function was introduced in Qt 5.5.

**See also**
[ciphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ciphers)() and
[setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
supportedCiphers() -> typing.List[PySide2.QtNetwork.QSslCipher]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#supportedCiphers"""
        ...

    def supportedEllipticCurves(self) -> tuple:
        """X.supportedEllipticCurves() -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QVector](https://doc.qt.io/archives/qt-5.15/qvector.html)\\<[QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html)\\> QSslConfiguration::supportedEllipticCurves()

Returns the list of elliptic curves supported by this system. This list is set by the
system's SSL libraries and may vary from system to system.

This function was introduced in Qt 5.5.

**See also**
[ellipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ellipticCurves)()
and
[setEllipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setEllipticCurves)().

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#supportedEllipticCurves"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QSslConfiguration::swap([QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#QSslConfiguration) \\&*other*)

Swaps this SSL configuration instance with *other*. This function is very fast and never
fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QSslConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#swap"""
        ...

    def systemCaCertificates(self) -> tuple:
        """X.systemCaCertificates() -> tuple

Supplemental documentation:
Qt 5 reference:

### `[static]` [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> QSslConfiguration::systemCaCertificates()

This function provides the CA certificate database provided by the operating system. The
CA certificate database returned by this function is used to initialize the database
returned by
[caCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#caCertificates)()
on the default
[QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html).

This function was introduced in Qt 5.5.

**See also**
[caCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#caCertificates)(),
[setCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCaCertificates)(),
[defaultConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#defaultConfiguration)(),
[addCaCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificate)(),
and
[addCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificates)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
systemCaCertificates() -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#systemCaCertificates"""
        ...

    def testSslOption(self, option: Any) -> bool:
        """X.testSslOption(option) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslConfiguration::testSslOption([QSsl::SslOption](https://doc.qt.io/archives/qt-5.15/qssl.html#SslOption-enum) *option*) const

Returns `true` if the specified SSL compatibility *option* is enabled.

This function was introduced in Qt 4.8.

**See also**
[setSslOption](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setSslOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
testSslOption(self, option: PySide2.QtNetwork.QSsl.SslOption) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#testSslOption"""
        ...
    NextProtocolNegotiationNegotiated: Any
    NextProtocolNegotiationNone: Any
    NextProtocolNegotiationStatus: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NextProtocolNegotiationUnsupported: Any

class QSslEllipticCurve:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The class QSslEllipticCurve represents an elliptic curve for use by elliptic-curve
cipher algorithms.

Elliptic curves can be constructed from a "short name" (SN)
([fromShortName](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#fromShortName)()),
and by a call to
[QSslConfiguration::supportedEllipticCurves](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#supportedEllipticCurves)().

QSslEllipticCurve instances can be compared for equality and can be used as keys in
[QHash](https://doc.qt.io/archives/qt-5.15/qhash-proxy.html) and
[QSet](https://doc.qt.io/archives/qt-5.15/qset.html). They cannot be used as key in a
[QMap](https://doc.qt.io/archives/qt-5.15/qmap.html).

**Note:** This class is currently only supported in OpenSSL.

Source: https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def fromLongName(self, name: Any) -> Any:
        """X.fromLongName(name) -> PythonQt.QtNetwork.QSslEllipticCurve

Supplemental documentation:
Qt 5 reference:

### `[static]` [QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#QSslEllipticCurve) QSslEllipticCurve::fromLongName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Returns an
[QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html) instance
representing the named curve *name*. The *name* is a long name for the curve, whose
exact spelling depends on the SSL implementation.

If the given *name* is not supported, returns an invalid
[QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html) instance.

**Note:** The OpenSSL implementation of this function treats the name case-sensitively.

**See also**
[longName](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#longName)().

Source: https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#fromLongName"""
        ...

    def fromShortName(self, name: Any) -> Any:
        """X.fromShortName(name) -> PythonQt.QtNetwork.QSslEllipticCurve

Supplemental documentation:
Qt 5 reference:

### `[static]` [QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#QSslEllipticCurve) QSslEllipticCurve::fromShortName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*)

Returns an
[QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html) instance
representing the named curve *name*. The *name* is the conventional short name for the
curve, as represented by RFC 4492 (for instance `secp521r1`), or as NIST short names
(for instance `P-256`). The actual set of recognized names depends on the SSL
implementation.

If the given *name* is not supported, returns an invalid
[QSslEllipticCurve](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html) instance.

**Note:** The OpenSSL implementation of this function treats the name case-sensitively.

**See also**
[shortName](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#shortName)().

Source: https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#fromShortName"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isTlsNamedCurve(self) -> bool:
        """X.isTlsNamedCurve() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslEllipticCurve::isTlsNamedCurve() const

Returns true if this elliptic curve is one of the named curves that can be used in the
key exchange when using an elliptic curve cipher with TLS; false otherwise.

Source: https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#isTlsNamedCurve"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslEllipticCurve::isValid() const

Returns true if this elliptic curve is a valid curve, false otherwise.

Source: https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#isValid"""
        ...

    def longName(self) -> str:
        """X.longName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslEllipticCurve::longName() const

Returns the conventional long name for this curve. If this curve is invalid, returns an
empty string.

**See also**
[shortName](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#shortName)().

Source: https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#longName"""
        ...

    def shortName(self) -> str:
        """X.shortName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslEllipticCurve::shortName() const

Returns the conventional short name for this curve. If this curve is invalid, returns an
empty string.

**See also**
[longName](https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#longName)().

Source: https://doc.qt.io/archives/qt-5.15/qsslellipticcurve.html#shortName"""
        ...

class QSslError:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSslError provides a simple API for managing errors during
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html)'s SSL handshake.

Source: https://doc.qt.io/archives/qt-5.15/qsslerror.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def certificate(self) -> Any:
        """X.certificate() -> PythonQt.QtNetwork.QSslCertificate

Supplemental documentation:
Qt 5 reference:

### [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) QSslError::certificate() const

Returns the certificate associated with this error, or a null certificate if the error
does not relate to any certificate.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qsslerror.html#error)() and
[errorString](https://doc.qt.io/archives/qt-5.15/qsslerror.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
certificate(self) -> PySide2.QtNetwork.QSslCertificate
```

Source: https://doc.qt.io/archives/qt-5.15/qsslerror.html#certificate"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def error(self) -> Any:
        """X.error()

Supplemental documentation:
Qt 5 reference:

### [QSslError::SslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html#SslError-enum) QSslError::error() const

Returns the type of the error.

**See also**
[errorString](https://doc.qt.io/archives/qt-5.15/qsslerror.html#errorString)() and
[certificate](https://doc.qt.io/archives/qt-5.15/qsslerror.html#certificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
error(self) -> PySide2.QtNetwork.QSslError.SslError
```

Source: https://doc.qt.io/archives/qt-5.15/qsslerror.html#error"""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslError::errorString() const

Returns a short localized human-readable description of the error.

**See also** [error](https://doc.qt.io/archives/qt-5.15/qsslerror.html#error)() and
[certificate](https://doc.qt.io/archives/qt-5.15/qsslerror.html#certificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
errorString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslerror.html#errorString"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QSslError"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QSslError::swap([QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html#QSslError) \\&*other*)

Swaps this error instance with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QSslError) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslerror.html#swap"""
        ...
    AuthorityIssuerSerialNumberMismatch: Any
    CertificateBlacklisted: Any
    CertificateExpired: Any
    CertificateNotYetValid: Any
    CertificateRejected: Any
    CertificateRevoked: Any
    CertificateSignatureFailed: Any
    CertificateUntrusted: Any
    HostNameMismatch: Any
    InvalidCaCertificate: Any
    InvalidNotAfterField: Any
    InvalidNotBeforeField: Any
    InvalidPurpose: Any
    NoError: Any
    NoPeerCertificate: Any
    NoSslSupport: Any
    PathLengthExceeded: Any
    SelfSignedCertificate: Any
    SelfSignedCertificateInChain: Any
    SslError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SubjectIssuerMismatch: Any
    UnableToDecodeIssuerPublicKey: Any
    UnableToDecryptCertificateSignature: Any
    UnableToGetIssuerCertificate: Any
    UnableToGetLocalIssuerCertificate: Any
    UnableToVerifyFirstCertificate: Any
    UnspecifiedError: Any

class QSslKey:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSslKey provides a simple API for managing keys.

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def algorithm(self) -> Any:
        """X.algorithm()

Supplemental documentation:
Qt 5 reference:

### [QSsl::KeyAlgorithm](https://doc.qt.io/archives/qt-5.15/qssl.html#KeyAlgorithm-enum) QSslKey::algorithm() const

Returns the key algorithm.

Upstream PySide2 reference signatures (binding differences may apply):

```python
algorithm(self) -> PySide2.QtNetwork.QSsl.KeyAlgorithm
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#algorithm"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def clear(self) -> None:
        """X.clear()

Supplemental documentation:
Qt 5 reference:

### void QSslKey::clear()

Clears the contents of this key, making it a null key.

**See also** [isNull](https://doc.qt.io/archives/qt-5.15/qsslkey.html#isNull)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
clear(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#clear"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def handle(self) -> int:
        """X.handle()

Supplemental documentation:
Qt 5 reference:

### [Qt::HANDLE](https://doc.qt.io/archives/qt-5.15/qt.html#HANDLE-typedef) QSslKey::handle() const

Returns a pointer to the native key handle, if there is one, else `nullptr`.

You can use this handle together with the native API to access extended information
about the key.

**Warning:** Use of this function has a high probability of being non-portable, and its
return value may vary across platforms, and between minor Qt releases.

Upstream PySide2 reference signatures (binding differences may apply):

```python
handle(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#handle"""
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

### bool QSslKey::isNull() const

Returns `true` if this is a null key; otherwise false.

**See also** [clear](https://doc.qt.io/archives/qt-5.15/qsslkey.html#clear)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isNull(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#isNull"""
        ...

    def length(self) -> int:
        """X.length() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslKey::length() const

Returns the length of the key in bits, or -1 if the key is null.

Upstream PySide2 reference signatures (binding differences may apply):

```python
length(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#length"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtNetwork.QSslKey"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QSslKey::swap([QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html#QSslKey) \\&*other*)

Swaps this ssl key with *other*. This function is very fast and never fails.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QSslKey) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#swap"""
        ...

    def toDer(self, passPhrase: Any) -> Any:
        """X.toDer(passPhrase) -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslKey::toDer(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*passPhrase* \\= QByteArray()) const

Returns the key in DER encoding.

The *passPhrase* argument should be omitted as DER cannot be encrypted. It will be
removed in a future version of Qt.

Upstream PySide2 reference signatures (binding differences may apply):

```python
toDer(self, passPhrase: PySide2.QtCore.QByteArray=...) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#toDer"""
        ...

    def toPem(self, passPhrase: Any) -> Any:
        """X.toPem(passPhrase) -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslKey::toPem(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*passPhrase* \\= QByteArray()) const

Returns the key in PEM encoding. The result is encrypted with *passPhrase* if the key is
a private key and *passPhrase* is non-empty.

Upstream PySide2 reference signatures (binding differences may apply):

```python
toPem(self, passPhrase: PySide2.QtCore.QByteArray=...) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#toPem"""
        ...

    def type(self) -> Any:
        """X.type()

Supplemental documentation:
Qt 5 reference:

### [QSsl::KeyType](https://doc.qt.io/archives/qt-5.15/qssl.html#KeyType-enum) QSslKey::type() const

Returns the type of the key (i.e., PublicKey or PrivateKey).

Upstream PySide2 reference signatures (binding differences may apply):

```python
type(self) -> PySide2.QtNetwork.QSsl.KeyType
```

Source: https://doc.qt.io/archives/qt-5.15/qsslkey.html#type"""
        ...

class QSslPreSharedKeyAuthenticator:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QSslPreSharedKeyAuthenticator class is used by an SSL socket to provide the required
authentication data in a pre shared key (PSK) ciphersuite.

In a PSK handshake, the client must derive a key, which must match the key set on the
server. The exact algorithm of deriving the key depends on the application; however, for
this purpose, the server may send an *identity hint* to the client. This hint, combined
with other information (for instance a passphrase), is then used by the client to
construct the shared key.

The QSslPreSharedKeyAuthenticator provides means to client applications for completing
the PSK handshake. The client application needs to connect a slot to the
[QSslSocket::preSharedKeyAuthenticationRequired](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#preSharedKeyAuthenticationRequired)()
signal:

```
    connect(socket, &QSslSocket::preSharedKeyAuthenticationRequired,
            this, &AuthManager::handlePreSharedKeyAuthentication);
```

The signal carries a QSslPreSharedKeyAuthenticator object containing the identity hint
the server sent to the client, and which must be filled with the corresponding client
identity and the derived key:

```
    void AuthManager::handlePreSharedKeyAuthentication(QSslPreSharedKeyAuthenticator *authenticator)
    {
        authenticator->setIdentity("My Qt App");

        const QByteArray key = deriveKey(authenticator->identityHint(), passphrase);
        authenticator->setPreSharedKey(key);
    }
```

**Note:** PSK ciphersuites are supported only when using OpenSSL 1.0.1 (or greater) as
the SSL backend.

**Note:** PSK is currently only supported in OpenSSL.

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html"""

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

    def identity(self) -> Any:
        """X.identity() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslPreSharedKeyAuthenticator::identity() const

Returns the PSK client identity.

**See also**
[setIdentity](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#setIdentity)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
identity(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#identity"""
        ...

    def identityHint(self) -> Any:
        """X.identityHint() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslPreSharedKeyAuthenticator::identityHint() const

Returns the PSK identity hint as provided by the server. The interpretation of this hint
is left to the application.

Upstream PySide2 reference signatures (binding differences may apply):

```python
identityHint(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#identityHint"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def maximumIdentityLength(self) -> int:
        """X.maximumIdentityLength() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslPreSharedKeyAuthenticator::maximumIdentityLength() const

Returns the maximum length, in bytes, of the PSK client identity.

**Note:** it is possible to set an identity whose length is greater than
maximumIdentityLength(); in this case, only the first maximumIdentityLength() bytes will
be actually sent to the server.

**See also**
[setIdentity](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#setIdentity)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
maximumIdentityLength(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumIdentityLength"""
        ...

    def maximumPreSharedKeyLength(self) -> int:
        """X.maximumPreSharedKeyLength() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslPreSharedKeyAuthenticator::maximumPreSharedKeyLength() const

Returns the maximum length, in bytes, of the pre shared key.

**Note:** it is possible to set a key whose length is greater than the
maximumPreSharedKeyLength(); in this case, only the first maximumPreSharedKeyLength()
bytes will be actually sent to the server.

**See also**
[setPreSharedKey](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#setPreSharedKey)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
maximumPreSharedKeyLength(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumPreSharedKeyLength"""
        ...

    def operator_assign(self, authenticator: Any) -> Any:
        """X.operator_assign(authenticator) -> PythonQt.QtNetwork.QSslPreSharedKeyAuthenticator"""
        ...

    def preSharedKey(self) -> Any:
        """X.preSharedKey() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QSslPreSharedKeyAuthenticator::preSharedKey() const

Returns the pre shared key.

**See also**
[setPreSharedKey](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#setPreSharedKey)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
preSharedKey(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#preSharedKey"""
        ...

    def setIdentity(self, identity: Any) -> None:
        """X.setIdentity(identity)

Supplemental documentation:
Qt 5 reference:

### void QSslPreSharedKeyAuthenticator::setIdentity(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*identity*)

Sets the PSK client identity (to be advised to the server) to *identity*.

**Note:** it is possible to set an identity whose length is greater than
[maximumIdentityLength](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumIdentityLength)();
in this case, only the first
[maximumIdentityLength](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumIdentityLength)()
bytes will be actually sent to the server.

**See also**
[identity](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#identity)()
and
[maximumIdentityLength](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumIdentityLength)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setIdentity(self, identity: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#setIdentity"""
        ...

    def setPreSharedKey(self, preSharedKey: Any) -> None:
        """X.setPreSharedKey(preSharedKey)

Supplemental documentation:
Qt 5 reference:

### void QSslPreSharedKeyAuthenticator::setPreSharedKey(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*preSharedKey*)

Sets the pre shared key to *preSharedKey*.

**Note:** it is possible to set a key whose length is greater than the
[maximumPreSharedKeyLength](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumPreSharedKeyLength)();
in this case, only the first
[maximumPreSharedKeyLength](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumPreSharedKeyLength)()
bytes will be actually sent to the server.

**See also**
[preSharedKey](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#preSharedKey)(),
[maximumPreSharedKeyLength](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#maximumPreSharedKeyLength)(),
and [QByteArray::fromHex](https://doc.qt.io/archives/qt-5.15/qbytearray.html#fromHex)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPreSharedKey(self, preSharedKey: PySide2.QtCore.QByteArray) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#setPreSharedKey"""
        ...

    def swap(self, other: Any) -> None:
        """X.swap(other)

Supplemental documentation:
Qt 5 reference:

### void QSslPreSharedKeyAuthenticator::swap([QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#QSslPreSharedKeyAuthenticator) \\&*authenticator*)

Swaps the
[QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html)
object *authenticator* with this object. This operation is very fast and never fails.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swap(self, other: PySide2.QtNetwork.QSslPreSharedKeyAuthenticator) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html#swap"""
        ...

class QSslSocket:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QSslSocket establishes a secure, encrypted TCP connection you can use for transmitting
encrypted data. It can operate in both client and server mode, and it supports modern
SSL protocols, including SSL 3 and TLS 1.2. By default, QSslSocket uses only SSL
protocols which are considered to be secure
([QSsl::SecureProtocols](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum)),
but you can change the SSL protocol by calling
[setProtocol](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setProtocol)() as long
as you do it before the handshake has started.

SSL encryption operates on top of the existing TCP stream after the socket enters the
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).
There are two simple ways to establish a secure connection using QSslSocket: With an
immediate SSL handshake, or with a delayed SSL handshake occurring after the connection
has been established in unencrypted mode.

The most common way to use QSslSocket is to construct an object and start a secure
connection by calling
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)().
This method starts an immediate SSL handshake once the connection has been established.

```
QSslSocket *socket = new QSslSocket(this);
connect(socket, SIGNAL(encrypted()), this, SLOT(ready()));

socket->connectToHostEncrypted("imap.example.com", 993);
```

As with a plain [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html),
QSslSocket enters the
[HostLookupState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
[ConnectingState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
and finally the
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
if the connection is successful. The handshake then starts automatically, and if it
succeeds, the
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() signal is
emitted to indicate the socket has entered the encrypted state and is ready for use.

Note that data can be written to the socket immediately after the return from
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)()
(i.e., before the
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() signal is
emitted). The data is queued in QSslSocket until after the
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() signal is
emitted.

An example of using the delayed SSL handshake to secure an existing connection is the
case where an SSL server secures an incoming connection. Suppose you create an SSL
server class as a subclass of
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html). You would override
[QTcpServer::incomingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#incomingConnection)()
with something like the example below, which first constructs an instance of QSslSocket
and then calls
[setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setSocketDescriptor)()
to set the new socket's descriptor to the existing one passed in. It then initiates the
SSL handshake by calling
[startServerEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startServerEncryption)().

```
void SslServer::incomingConnection(qintptr socketDescriptor)
{
    QSslSocket *serverSocket = new QSslSocket;
    if (serverSocket->setSocketDescriptor(socketDescriptor)) {
        addPendingConnection(serverSocket);
        connect(serverSocket, &QSslSocket::encrypted, this, &SslServer::ready);
        serverSocket->startServerEncryption();
    } else {
        delete serverSocket;
    }
}
```

If an error occurs, QSslSocket emits the sslErrors() signal. In this case, if no action
is taken to ignore the error(s), the connection is dropped. To continue, despite the
occurrence of an error, you can call
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)(),
either from within this slot after the error occurs, or any time after construction of
the QSslSocket and before the connection is attempted. This will allow QSslSocket to
ignore the errors it encounters when establishing the identity of the peer. Ignoring
errors during an SSL handshake should be used with caution, since a fundamental
characteristic of secure connections is that they should be established with a
successful handshake.

Once encrypted, you use QSslSocket as a regular
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html). When
[readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)() is emitted,
you can call [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)(),
[canReadLine](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#canReadLine)() and
[readLine](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readLine)(), or
[getChar](https://doc.qt.io/archives/qt-5.15/qiodevice.html#getChar)() to read decrypted
data from QSslSocket's internal buffer, and you can call
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() or
[putChar](https://doc.qt.io/archives/qt-5.15/qiodevice.html#putChar)() to write data
back to the peer. QSslSocket will automatically encrypt the written data for you, and
emit
[encryptedBytesWritten](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encryptedBytesWritten)()
once the data has been written to the peer.

As a convenience, QSslSocket supports
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html)'s blocking functions
[waitForConnected](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForConnected)(),
[waitForReadyRead](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForReadyRead)(),
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForBytesWritten)(),
and
[waitForDisconnected](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForDisconnected)().
It also provides
[waitForEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForEncrypted)(),
which will block the calling thread until an encrypted connection has been established.

```
QSslSocket socket;
socket.connectToHostEncrypted("http.example.com", 443);
if (!socket.waitForEncrypted()) {
    qDebug() << socket.errorString();
    return false;
}

socket.write("GET / HTTP/1.0\\r\\n\\r\\n");
while (socket.waitForReadyRead())
    qDebug() << socket.readAll().data();
```

QSslSocket provides an extensive, easy-to-use API for handling cryptographic ciphers,
private keys, and local, peer, and Certification Authority (CA) certificates. It also
provides an API for handling errors that occur during the handshake phase.

The following features can also be customized:

- The socket's cryptographic cipher suite can be customized before the handshake phase with [QSslConfiguration::setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)() and QSslConfiguration::setDefaultCiphers().
- The socket's local certificate and private key can be customized before the handshake phase with [setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificate)() and [setPrivateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPrivateKey)().
- The CA certificate database can be extended and customized with [QSslConfiguration::addCaCertificate](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificate)(), [QSslConfiguration::addCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#addCaCertificates)().

To extend the list of *default* CA certificates used by the SSL sockets during the SSL
handshake you must update the default configuration, as in the snippet below:

```
QList<QSslCertificate> certificates = getCertificates();
QSslConfiguration configuration = QSslConfiguration::defaultConfiguration();
configuration.addCaCertificates(certificates);
QSslConfiguration::setDefaultConfiguration(configuration);
```

**Note:** If available, root certificates on Unix (excluding macOS) will be loaded on
demand from the standard certificate directories. If you do not want to load root
certificates on demand, you need to call either
[QSslConfiguration::defaultConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#defaultConfiguration)().setCaCertificates()
before the first SSL handshake is made in your application (for example, via passing
QSslSocket::systemCaCertificates() to it), or call
[QSslConfiguration::defaultConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#defaultConfiguration)()::setCaCertificates()
on your QSslSocket instance prior to the SSL handshake.

For more information about ciphers and certificates, refer to
[QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html) and
[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html).

This product includes software developed by the OpenSSL Project for use in the OpenSSL
Toolkit (<http://www.openssl.org/>).

**Note:** Be aware of the difference between the
[bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)() signal
and the
[encryptedBytesWritten](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encryptedBytesWritten)()
signal. For a [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html),
[bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)() will
get emitted as soon as data has been written to the TCP socket. For a QSslSocket,
[bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)() will
get emitted when the data is being encrypted and
[encryptedBytesWritten](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encryptedBytesWritten)()
will get emitted as soon as data has been written to the TCP socket.

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abort(self) -> None:
        """X.abort()

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::abort()

Aborts the current connection and resets the socket. Unlike
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)(),
this function immediately closes the socket, clearing any pending data in the write
buffer.

**See also**
[disconnectFromHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnectFromHost)()
and [close](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
abort(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#abort"""
        ...

    def aboutToClose(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.aboutToClose; argument details are not documented."""
        ...

    def addCaCertificate(self, certificate: Any) -> None:
        """X.addCaCertificate(certificate)

Upstream PySide2 reference signatures (binding differences may apply):

```python
addCaCertificate(self, certificate: PySide2.QtNetwork.QSslCertificate) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#addCaCertificate"""
        ...

    def addCaCertificates(self, path: Any, format: Any, syntax: Any) -> Any:
        """X.addCaCertificates(path, format, syntax)

Upstream PySide2 reference signatures (binding differences may apply):

```python
addCaCertificates(self, certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
addCaCertificates(self, path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat=..., syntax: PySide2.QtCore.QRegExp.PatternSyntax=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#addCaCertificates"""
        ...

    def addDefaultCaCertificate(self, certificate: Any) -> None:
        """X.addDefaultCaCertificate(certificate)

Upstream PySide2 reference signatures (binding differences may apply):

```python
addDefaultCaCertificate(certificate: PySide2.QtNetwork.QSslCertificate) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#addDefaultCaCertificate"""
        ...

    def addDefaultCaCertificates(self, path: Any, format: Any, syntax: Any) -> Any:
        """X.addDefaultCaCertificates(path, format, syntax)

Upstream PySide2 reference signatures (binding differences may apply):

```python
addDefaultCaCertificates(certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
addDefaultCaCertificates(path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat=..., syntax: PySide2.QtCore.QRegExp.PatternSyntax=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#addDefaultCaCertificates"""
        ...

    def atEnd(self) -> bool:
        """X.atEnd() -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QSslSocket::atEnd() const

Reimplements:
[QAbstractSocket::atEnd](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#atEnd)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
atEnd(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#atEnd"""
        ...

    def bind(self, address: Any, port: Any, mode: Any) -> bool:
        """X.bind(address, port, mode) -> bool"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def bytesAvailable(self) -> int:
        """X.bytesAvailable() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSslSocket::bytesAvailable() const

Reimplements:
[QAbstractSocket::bytesAvailable](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesAvailable)()
const.

Returns the number of decrypted bytes that are immediately available for reading.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesAvailable(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#bytesAvailable"""
        ...

    def bytesToWrite(self) -> int:
        """X.bytesToWrite() -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSslSocket::bytesToWrite() const

Reimplements:
[QAbstractSocket::bytesToWrite](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bytesToWrite)()
const.

Returns the number of unencrypted bytes that are waiting to be encrypted and written to
the network.

Upstream PySide2 reference signatures (binding differences may apply):

```python
bytesToWrite(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#bytesToWrite"""
        ...

    def bytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.bytesWritten; argument details are not documented."""
        ...

    def caCertificates(self) -> tuple:
        """X.caCertificates() -> tuple

Upstream PySide2 reference signatures (binding differences may apply):

```python
caCertificates(self) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#caCertificates"""
        ...

    def canReadLine(self) -> bool:
        """X.canReadLine() -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QSslSocket::canReadLine() const

Reimplements:
[QAbstractSocket::canReadLine](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#canReadLine)()
const.

Returns `true` if you can read one while line (terminated by a single ASCII '\\\\n'
character) of decrypted characters; otherwise, false is returned.

Upstream PySide2 reference signatures (binding differences may apply):

```python
canReadLine(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#canReadLine"""
        ...

    def channelBytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.channelBytesWritten; argument details are not documented."""
        ...

    def channelReadyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.channelReadyRead; argument details are not documented."""
        ...

    def childEvent(self, event: Any) -> Any:
        """X.childEvent(event)"""
        ...

    def children(self) -> tuple:
        """X.children() -> tuple"""
        ...

    def ciphers(self) -> tuple:
        """X.ciphers() -> tuple

Upstream PySide2 reference signatures (binding differences may apply):

```python
ciphers(self) -> typing.List[PySide2.QtNetwork.QSslCipher]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ciphers"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def close(self) -> None:
        """X.close()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QSslSocket::close()

Reimplements:
[QAbstractSocket::close](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#close)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
close(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#close"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def connectToHost(self, hostName: Any, port: int, openMode: Any, protocol: Any) -> None:
        """X.connectToHost(hostName, port, openMode, protocol)

Upstream PySide2 reference signatures (binding differences may apply):

```python
connectToHost(self, address: PySide2.QtNetwork.QHostAddress, port: int, mode: PySide2.QtCore.QIODevice.OpenMode=...) -> None
connectToHost(self, hostName: str, port: int, openMode: PySide2.QtCore.QIODevice.OpenMode=..., protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHost"""
        ...

    def connectToHostEncrypted(self, hostName: str, port: int, sslPeerName: Any, mode: Any, protocol: Any) -> None:
        """X.connectToHostEncrypted(hostName, port, sslPeerName, mode, protocol)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::connectToHostEncrypted(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *mode* \\= ReadWrite, [QAbstractSocket::NetworkLayerProtocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum) *protocol* \\= AnyIPProtocol)

Starts an encrypted connection to the device *hostName* on *port*, using *mode* as the
[OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum). This is
equivalent to calling
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
to establish the connection, followed by a call to
[startClientEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startClientEncryption)().
The *protocol* parameter can be used to specify which network protocol to use (eg. IPv4
or IPv6).

[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) first enters the
[HostLookupState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).
Then, after entering either the event loop or one of the waitFor...() functions, it
enters the
[ConnectingState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
emits [connected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connected)(),
and then initiates the SSL client handshake. At each state change,
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) emits signal
[stateChanged](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#stateChanged)().

After initiating the SSL client handshake, if the identity of the peer can't be
established, signal sslErrors() is emitted. If you want to ignore the errors and
continue connecting, you must call
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)(),
either from inside a slot function connected to the sslErrors() signal, or prior to
entering encrypted mode. If
[ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)()
is not called, the connection is dropped, signal
[disconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#disconnected)()
is emitted, and [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) returns
to the
[UnconnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum).

If the SSL handshake is successful,
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) emits
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)().

```
QSslSocket socket;
connect(&socket, SIGNAL(encrypted()), receiver, SLOT(socketEncrypted()));

socket.connectToHostEncrypted("imap", 993);
socket->write("1 CAPABILITY\\r\\n");
```

**Note:** The example above shows that text can be written to the socket immediately
after requesting the encrypted connection, before the
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() signal has
been emitted. In such cases, the text is queued in the object and written to the socket
*after* the connection is established and the
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() signal has
been emitted.

The default for *mode* is
[ReadWrite](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum).

If you want to create a [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html)
on the server side of a connection, you should instead call
[startServerEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startServerEncryption)()
upon receiving the incoming connection through
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html).

**See also**
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)(),
[startClientEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startClientEncryption)(),
[waitForConnected](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForConnected)(),
and
[waitForEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForEncrypted)().

### void QSslSocket::connectToHostEncrypted(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*sslPeerName*, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *mode* \\= ReadWrite, [QAbstractSocket::NetworkLayerProtocol](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#NetworkLayerProtocol-enum) *protocol* \\= AnyIPProtocol)

This is an overloaded function.

In addition to the original behaviour of connectToHostEncrypted, this overloaded method
enables the usage of a different hostname (*sslPeerName*) for the certificate validation
instead of the one used for the TCP connection (*hostName*).

This function was introduced in Qt 4.6.

**See also**
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
connectToHostEncrypted(self, hostName: str, port: int, mode: PySide2.QtCore.QIODevice.OpenMode=..., protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol=...) -> None
connectToHostEncrypted(self, hostName: str, port: int, sslPeerName: str, mode: PySide2.QtCore.QIODevice.OpenMode=..., protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted"""
        ...

    def connected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.connected; argument details are not documented."""
        ...

    def customEvent(self, event: Any) -> Any:
        """X.customEvent(event)"""
        ...

    def defaultCaCertificates(self) -> tuple:
        """X.defaultCaCertificates() -> tuple

Upstream PySide2 reference signatures (binding differences may apply):

```python
defaultCaCertificates() -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#defaultCaCertificates"""
        ...

    def defaultCiphers(self) -> tuple:
        """X.defaultCiphers() -> tuple

Upstream PySide2 reference signatures (binding differences may apply):

```python
defaultCiphers() -> typing.List[PySide2.QtNetwork.QSslCipher]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#defaultCiphers"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteLater(self) -> Any:
        """X.deleteLater()"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def disconnectFromHost(self) -> None:
        """X.disconnectFromHost()

Upstream PySide2 reference signatures (binding differences may apply):

```python
disconnectFromHost(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#disconnectFromHost"""
        ...

    def disconnected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.disconnected; argument details are not documented."""
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

    def encrypted(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.encrypted; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSslSocket::encrypted()

This signal is emitted when
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) enters encrypted mode.
After this signal has been emitted,
[QSslSocket::isEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#isEncrypted)()
will return true, and all further transmissions on the socket will be encrypted.

**See also**
[QSslSocket::connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)()
and
[QSslSocket::isEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#isEncrypted)().

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted"""
        ...

    def encryptedBytesAvailable(self) -> int:
        """X.encryptedBytesAvailable() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSslSocket::encryptedBytesAvailable() const

Returns the number of encrypted bytes that are awaiting decryption. Normally, this
function will return 0 because
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) decrypts its incoming
data as soon as it can.

This function was introduced in Qt 4.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
encryptedBytesAvailable(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encryptedBytesAvailable"""
        ...

    def encryptedBytesToWrite(self) -> int:
        """X.encryptedBytesToWrite() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSslSocket::encryptedBytesToWrite() const

Returns the number of encrypted bytes that are waiting to be written to the network.

This function was introduced in Qt 4.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
encryptedBytesToWrite(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encryptedBytesToWrite"""
        ...

    def encryptedBytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.encryptedBytesWritten; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSslSocket::encryptedBytesWritten([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *written*)

This signal is emitted when
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) writes its encrypted
data to the network. The *written* parameter contains the number of bytes that were
successfully written.

This function was introduced in Qt 4.4.

**See also**
[QIODevice::bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)().

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encryptedBytesWritten"""
        ...

    def error(self) -> Any:
        """X.error()"""
        ...

    def errorOccurred(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.errorOccurred; argument details are not documented."""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str"""
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

    def flush(self) -> bool:
        """X.flush() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslSocket::flush()

This function writes as much as possible from the internal write buffer to the
underlying network socket, without blocking. If any data was written, this function
returns `true`; otherwise false is returned.

Call this function if you need
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to start sending
buffered data immediately. The number of bytes successfully written depends on the
operating system. In most cases, you do not need to call this function, because
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) will start
sending data automatically once control goes back to the event loop. In the absence of
an event loop, call
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForBytesWritten)()
instead.

**See also** [write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() and
[waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForBytesWritten)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
flush(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#flush"""
        ...

    def getChar(self, c: Any) -> bool:
        """X.getChar(c) -> bool"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hostFound(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.hostFound; argument details are not documented."""
        ...

    def ignoreSslErrors(self, errors: Any) -> None:
        """X.ignoreSslErrors(errors)

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QSslSocket::ignoreSslErrors()

This slot tells [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to
ignore errors during [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html)'s
handshake phase and continue connecting. If you want to continue with the connection
even if errors occur during the handshake phase, then you must call this slot, either
from a slot connected to sslErrors(), or before the handshake phase. If you don't call
this slot, either in response to errors or before the handshake, the connection will be
dropped after the sslErrors() signal has been emitted.

If there are no errors during the SSL handshake phase (i.e., the identity of the peer is
established with no problems),
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) will not emit the
sslErrors() signal, and it is unnecessary to call this function.

**Warning:** Be sure to always let the user inspect the errors reported by the
sslErrors() signal, and only call this method upon confirmation from the user that
proceeding is ok. If there are unexpected errors, the connection should be aborted.
Calling this method without inspecting the actual errors will most likely pose a
security risk for your application. Use it with great care!

**See also**
[sslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#sslErrors)().

### void QSslSocket::ignoreSslErrors(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html)\\> \\&*errors*)

This is an overloaded function.

This method tells [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to
ignore only the errors given in *errors*.

**Note:** Because most SSL errors are associated with a certificate, for most of them
you must set the expected certificate this SSL error is related to. If, for instance,
you want to connect to a server that uses a self-signed certificate, consider the
following snippet:

```
QList<QSslCertificate> cert = QSslCertificate::fromPath(QLatin1String("server-certificate.pem"));
QSslError error(QSslError::SelfSignedCertificate, cert.at(0));
QList<QSslError> expectedSslErrors;
expectedSslErrors.append(error);

QSslSocket socket;
socket.ignoreSslErrors(expectedSslErrors);
socket.connectToHostEncrypted("server.tld", 443);
```

Multiple calls to this function will replace the list of errors that were passed in
previous calls. You can clear the list of errors you want to ignore by calling this
function with an empty list.

This function was introduced in Qt 4.6.

**See also**
[sslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#sslErrors)() and
[sslHandshakeErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslHandshakeErrors)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
ignoreSslErrors(self) -> None
ignoreSslErrors(self, errors: typing.Sequence[PySide2.QtNetwork.QSslError]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isEncrypted(self) -> bool:
        """X.isEncrypted() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslSocket::isEncrypted() const

Returns `true` if the socket is encrypted; otherwise, false is returned.

An encrypted socket encrypts all data that is written by calling
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() or
[putChar](https://doc.qt.io/archives/qt-5.15/qiodevice.html#putChar)() before the data
is written to the network, and decrypts all incoming data as the data is received from
the network, before you call
[read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)(),
[readLine](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readLine)() or
[getChar](https://doc.qt.io/archives/qt-5.15/qiodevice.html#getChar)().

[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) emits
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() when it
enters encrypted mode.

You can call
[sessionCipher](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sessionCipher)() to
find which cryptographic cipher is used to encrypt and decrypt your data.

**See also** [mode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#mode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isEncrypted(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#isEncrypted"""
        ...

    def isOpen(self) -> bool:
        """X.isOpen() -> bool"""
        ...

    def isReadable(self) -> bool:
        """X.isReadable() -> bool"""
        ...

    def isSequential(self) -> bool:
        """X.isSequential() -> bool"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isTextModeEnabled(self) -> bool:
        """X.isTextModeEnabled() -> bool"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def isWritable(self) -> bool:
        """X.isWritable() -> bool"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def localAddress(self) -> Any:
        """X.localAddress() -> PythonQt.QtNetwork.QHostAddress"""
        ...

    def localCertificate(self) -> Any:
        """X.localCertificate() -> PythonQt.QtNetwork.QSslCertificate

Supplemental documentation:
Qt 5 reference:

### [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) QSslSocket::localCertificate() const

Returns the socket's local
[certificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html), or an empty
certificate if no local certificate has been assigned.

**See also**
[setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificate)()
and [privateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#privateKey)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localCertificate(self) -> PySide2.QtNetwork.QSslCertificate
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#localCertificate"""
        ...

    def localCertificateChain(self) -> tuple:
        """X.localCertificateChain() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> QSslSocket::localCertificateChain() const

Returns the socket's local
[certificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) chain, or an
empty list if no local certificates have been assigned.

This function was introduced in Qt 5.1.

**See also**
[setLocalCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificateChain)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
localCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#localCertificateChain"""
        ...

    def localPort(self) -> int:
        """X.localPort() -> int"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def mode(self) -> Any:
        """X.mode()

Supplemental documentation:
Qt 5 reference:

### [QSslSocket::SslMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum) QSslSocket::mode() const

Returns the current mode for the socket; either
[UnencryptedMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum),
where [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) behaves
identially to [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html), or one
of [SslClientMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum) or
[SslServerMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum), where
the client is either negotiating or in encrypted mode.

When the mode changes, [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html)
emits [modeChanged](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#modeChanged)()

**See also** [SslMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum).

Upstream PySide2 reference signatures (binding differences may apply):

```python
mode(self) -> PySide2.QtNetwork.QSslSocket.SslMode
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#mode"""
        ...

    def modeChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.modeChanged; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSslSocket::modeChanged([QSslSocket::SslMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum) *mode*)

This signal is emitted when
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) changes from
[QSslSocket::UnencryptedMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum)
to either
[QSslSocket::SslClientMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum)
or
[QSslSocket::SslServerMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum).
*mode* is the new mode.

**See also**
[QSslSocket::mode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#mode)().

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#modeChanged"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def newSessionTicketReceived(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.newSessionTicketReceived; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSslSocket::newSessionTicketReceived()

If TLS 1.3 protocol was negotiated during a handshake,
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) emits this signal after
receiving NewSessionTicket message. Session and session ticket's lifetime hint are
updated in the socket's configuration. The session can be used for session resumption
(and a shortened handshake) in future TLS connections.

**Note:** This functionality enabled only with OpenSSL backend and requires OpenSSL v
1.1.1 or above.

This function was introduced in Qt 5.15.

**See also**
[QSslSocket::sslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslConfiguration)(),
[QSslConfiguration::sessionTicket](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionTicket)(),
and
[QSslConfiguration::sessionTicketLifeTimeHint](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#sessionTicketLifeTimeHint)().

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#newSessionTicketReceived"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.objectNameChanged; argument details are not documented."""
        ...

    def open(self, mode: Any) -> bool:
        """X.open(mode) -> bool"""
        ...

    def openMode(self) -> Any:
        """X.openMode()"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def pauseMode(self) -> Any:
        """X.pauseMode()"""
        ...

    def peek(self, maxlen: Any) -> Any:
        """X.peek(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def peerAddress(self) -> Any:
        """X.peerAddress() -> PythonQt.QtNetwork.QHostAddress"""
        ...

    def peerCertificate(self) -> Any:
        """X.peerCertificate() -> PythonQt.QtNetwork.QSslCertificate

Supplemental documentation:
Qt 5 reference:

### [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) QSslSocket::peerCertificate() const

Returns the peer's digital certificate (i.e., the immediate certificate of the host you
are connected to), or a null certificate, if the peer has not assigned a certificate.

The peer certificate is checked automatically during the handshake phase, so this
function is normally used to fetch the certificate for display or for connection
diagnostic purposes. It contains information about the peer, including its host name,
the certificate issuer, and the peer's public key.

Because the peer certificate is set during the handshake phase, it is safe to access the
peer certificate from a slot connected to the sslErrors() signal or the
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() signal.

If a null certificate is returned, it can mean the SSL handshake failed, or it can mean
the host you are connected to doesn't have a certificate, or it can mean there is no
connection.

If you want to check the peer's complete chain of certificates, use
[peerCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificateChain)()
to get them all at once.

**See also**
[peerCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificateChain)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerCertificate(self) -> PySide2.QtNetwork.QSslCertificate
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificate"""
        ...

    def peerCertificateChain(self) -> tuple:
        """X.peerCertificateChain() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> QSslSocket::peerCertificateChain() const

Returns the peer's chain of digital certificates, or an empty list of certificates.

Peer certificates are checked automatically during the handshake phase. This function is
normally used to fetch certificates for display, or for performing connection
diagnostics. Certificates contain information about the peer and the certificate
issuers, including host name, issuer names, and issuer public keys.

The peer certificates are set in
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) during the handshake
phase, so it is safe to call this function from a slot connected to the sslErrors()
signal or the
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() signal.

If an empty list is returned, it can mean the SSL handshake failed, or it can mean the
host you are connected to doesn't have a certificate, or it can mean there is no
connection.

If you want to get only the peer's immediate certificate, use
[peerCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificate)().

**See also**
[peerCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificateChain"""
        ...

    def peerName(self) -> str:
        """X.peerName() -> str"""
        ...

    def peerPort(self) -> int:
        """X.peerPort() -> int"""
        ...

    def peerVerifyDepth(self) -> int:
        """X.peerVerifyDepth() -> int

Supplemental documentation:
Qt 5 reference:

### int QSslSocket::peerVerifyDepth() const

Returns the maximum number of certificates in the peer's certificate chain to be checked
during the SSL handshake phase, or 0 (the default) if no maximum depth has been set,
indicating that the whole certificate chain should be checked.

The certificates are checked in issuing order, starting with the peer's own certificate,
then its issuer's certificate, and so on.

This function was introduced in Qt 4.4.

**See also**
[setPeerVerifyDepth](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyDepth)()
and
[peerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerVerifyDepth(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyDepth"""
        ...

    def peerVerifyError(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.peerVerifyError; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSslSocket::peerVerifyError(const [QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html) \\&*error*)

[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) can emit this signal
several times during the SSL handshake, before encryption has been established, to
indicate that an error has occurred while establishing the identity of the peer. The
*error* is usually an indication that
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) is unable to securely
identify the peer.

This signal provides you with an early indication when something's wrong. By connecting
to this signal, you can manually choose to tear down the connection from inside the
connected slot before the handshake has completed. If no action is taken,
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) will proceed to
emitting QSslSocket::sslErrors().

This function was introduced in Qt 4.4.

**See also**
[sslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket-obsolete.html#sslErrors)().

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyError"""
        ...

    def peerVerifyMode(self) -> Any:
        """X.peerVerifyMode()

Supplemental documentation:
Qt 5 reference:

### [QSslSocket::PeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) QSslSocket::peerVerifyMode() const

Returns the socket's verify mode. This mode decides whether
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) should request a
certificate from the peer (i.e., the client requests a certificate from the server, or a
server requesting a certificate from the client), and whether it should require that
this certificate is valid.

The default mode is
[AutoVerifyPeer](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum),
which tells [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to use
[VerifyPeer](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) for
clients and
[QueryPeer](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) for
servers.

This function was introduced in Qt 4.4.

**See also**
[setPeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyMode)(),
[peerVerifyDepth](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyDepth)(),
and [mode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#mode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerVerifyMode(self) -> PySide2.QtNetwork.QSslSocket.PeerVerifyMode
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyMode"""
        ...

    def peerVerifyName(self) -> str:
        """X.peerVerifyName() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslSocket::peerVerifyName() const

Returns the different hostname for the certificate validation, as set by
[setPeerVerifyName](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyName)
or by
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted).

This function was introduced in Qt 4.8.

**See also**
[setPeerVerifyName](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyName)()
and
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
peerVerifyName(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyName"""
        ...

    def pos(self) -> int:
        """X.pos() -> int"""
        ...

    def preSharedKeyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.preSharedKeyAuthenticationRequired; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSslSocket::preSharedKeyAuthenticationRequired([QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html) \\**authenticator*)

[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) emits this signal when
it negotiates a PSK ciphersuite, and therefore a PSK authentication is then required.

When using PSK, the client must send to the server a valid identity and a valid pre
shared key, in order for the SSL handshake to continue. Applications can provide this
information in a slot connected to this signal, by filling in the passed *authenticator*
object according to their needs.

**Note:** Ignoring this signal, or failing to provide the required credentials, will
cause the handshake to fail, and therefore the connection to be aborted.

**Note:** The *authenticator* object is owned by the socket and must not be deleted by
the application.

This function was introduced in Qt 5.5.

**See also**
[QSslPreSharedKeyAuthenticator](https://doc.qt.io/archives/qt-5.15/qsslpresharedkeyauthenticator.html).

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#preSharedKeyAuthenticationRequired"""
        ...

    def privateKey(self) -> Any:
        """X.privateKey() -> PythonQt.QtNetwork.QSslKey

Supplemental documentation:
Qt 5 reference:

### [QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html) QSslSocket::privateKey() const

Returns this socket's private key.

**See also**
[setPrivateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPrivateKey)() and
[localCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#localCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
privateKey(self) -> PySide2.QtNetwork.QSslKey
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#privateKey"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def protocol(self) -> Any:
        """X.protocol()

Supplemental documentation:
Qt 5 reference:

### [QSsl::SslProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum) QSslSocket::protocol() const

Returns the socket's SSL protocol. By default,
[QSsl::SecureProtocols](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum)
is used.

**See also**
[setProtocol](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setProtocol)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
protocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#protocol"""
        ...

    def proxy(self) -> Any:
        """X.proxy() -> PythonQt.QtNetwork.QNetworkProxy"""
        ...

    def proxyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.proxyAuthenticationRequired; argument details are not documented."""
        ...

    def putChar(self, c: Any) -> bool:
        """X.putChar(c) -> bool"""
        ...

    def read(self, maxlen: Any) -> Any:
        """X.read(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readAll(self) -> Any:
        """X.readAll() -> PythonQt.QtCore.QByteArray"""
        ...

    def readBufferSize(self) -> int:
        """X.readBufferSize() -> int"""
        ...

    def readChannelFinished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.readChannelFinished; argument details are not documented."""
        ...

    def readData(self, data: str, maxlen: int) -> int:
        """X.readData(data, maxlen) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSslSocket::readData(char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *maxlen*)

Reimplements:
[QAbstractSocket::readData](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#readData)(char
\\*data, qint64 maxSize).

Upstream PySide2 reference signatures (binding differences may apply):

```python
readData(self, data: str, maxlen: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#readData"""
        ...

    def readLine(self, maxlen: Any) -> Any:
        """X.readLine(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readLineData(self, data: Any, maxlen: Any) -> int:
        """X.readLineData(data, maxlen) -> int"""
        ...

    def readyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.readyRead; argument details are not documented."""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def reset(self) -> bool:
        """X.reset() -> bool"""
        ...

    def resume(self) -> None:
        """X.resume()

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QSslSocket::resume()

Reimplements:
[QAbstractSocket::resume](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#resume)().

Continues data transfer on the socket after it has been paused. If
"[setPauseMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPauseMode)([QAbstractSocket::PauseOnSslErrors](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#PauseMode-enum));"
has been called on this socket and a sslErrors() signal is received, calling this method
is necessary for the socket to continue.

This function was introduced in Qt 5.0.

**See also**
[QAbstractSocket::pauseMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#pauseMode)()
and
[QAbstractSocket::setPauseMode](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setPauseMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
resume(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#resume"""
        ...

    def seek(self, pos: Any) -> bool:
        """X.seek(pos) -> bool"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def sessionCipher(self) -> Any:
        """X.sessionCipher() -> PythonQt.QtNetwork.QSslCipher

Supplemental documentation:
Qt 5 reference:

### [QSslCipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html) QSslSocket::sessionCipher() const

Returns the socket's cryptographic
[cipher](https://doc.qt.io/archives/qt-5.15/qsslcipher.html), or a null cipher if the
connection isn't encrypted. The socket's cipher for the session is set during the
handshake phase. The cipher is used to encrypt and decrypt data transmitted through the
socket.

[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) also provides functions
for setting the ordered list of ciphers from which the handshake phase will eventually
select the session cipher. This ordered list must be in place before the handshake phase
begins.

**See also**
[QSslConfiguration::ciphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ciphers)(),
[QSslConfiguration::setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)(),
[QSslConfiguration::setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)(),
[QSslConfiguration::ciphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ciphers)(),
and
[QSslConfiguration::supportedCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#supportedCiphers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sessionCipher(self) -> PySide2.QtNetwork.QSslCipher
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sessionCipher"""
        ...

    def sessionProtocol(self) -> Any:
        """X.sessionProtocol()

Supplemental documentation:
Qt 5 reference:

### [QSsl::SslProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum) QSslSocket::sessionProtocol() const

Returns the socket's SSL/TLS protocol or UnknownProtocol if the connection isn't
encrypted. The socket's protocol for the session is set during the handshake phase.

This function was introduced in Qt 5.4.

**See also** [protocol](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#protocol)()
and [setProtocol](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setProtocol)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sessionProtocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sessionProtocol"""
        ...

    def setCaCertificates(self, certificates: Any) -> None:
        """X.setCaCertificates(certificates)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCaCertificates(self, certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setCaCertificates"""
        ...

    def setCiphers(self, ciphers: Any) -> None:
        """X.setCiphers(ciphers)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setCiphers(self, ciphers: typing.Sequence[PySide2.QtNetwork.QSslCipher]) -> None
setCiphers(self, ciphers: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setCiphers"""
        ...

    def setDefaultCaCertificates(self, certificates: Any) -> None:
        """X.setDefaultCaCertificates(certificates)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDefaultCaCertificates(certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setDefaultCaCertificates"""
        ...

    def setDefaultCiphers(self, ciphers: Any) -> None:
        """X.setDefaultCiphers(ciphers)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDefaultCiphers(ciphers: typing.Sequence[PySide2.QtNetwork.QSslCipher]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setDefaultCiphers"""
        ...

    def setErrorString(self, errorString: Any) -> Any:
        """X.setErrorString(errorString)"""
        ...

    def setLocalAddress(self, address: Any) -> Any:
        """X.setLocalAddress(address)"""
        ...

    def setLocalCertificate(self, fileName: Any, format: Any) -> None:
        """X.setLocalCertificate(fileName, format)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setLocalCertificate(const [QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) \\&*certificate*)

Sets the socket's local certificate to *certificate*. The local certificate is necessary
if you need to confirm your identity to the peer. It is used together with the private
key; if you set the local certificate, you must also set the private key.

The local certificate and private key are always necessary for server sockets, but are
also rarely used by client sockets if the server requires the client to authenticate.

**Note:** Secure Transport SSL backend on macOS may update the default keychain (the
default is probably your login keychain) by importing your local certificates and keys.
This can also result in system dialogs showing up and asking for permission when your
application is using these private keys. If such behavior is undesired, set the
QT\\_SSL\\_USE\\_TEMPORARY\\_KEYCHAIN environment variable to a non-zero value; this will
prompt [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to use its own
temporary keychain.

**See also**
[localCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#localCertificate)()
and [setPrivateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPrivateKey)().

### void QSslSocket::setLocalCertificate(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*path*, [QSsl::EncodingFormat](https://doc.qt.io/archives/qt-5.15/qssl.html#EncodingFormat-enum) *format* \\= QSsl::Pem)

This is an overloaded function.

Sets the socket's local
[certificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) to the first one
found in file *path*, which is parsed according to the specified *format*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLocalCertificate(self, certificate: PySide2.QtNetwork.QSslCertificate) -> None
setLocalCertificate(self, fileName: str, format: PySide2.QtNetwork.QSsl.EncodingFormat=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificate"""
        ...

    def setLocalCertificateChain(self, localChain: Any) -> None:
        """X.setLocalCertificateChain(localChain)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setLocalCertificateChain(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslCertificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html)\\> \\&*localChain*)

Sets the certificate chain to be presented to the peer during the SSL handshake to be
*localChain*.

This function was introduced in Qt 5.1.

**See also**
[localCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#localCertificateChain)()
and
[QSslConfiguration::setLocalCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setLocalCertificateChain)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setLocalCertificateChain(self, localChain: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificateChain"""
        ...

    def setLocalPort(self, port: Any) -> Any:
        """X.setLocalPort(port)"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setOpenMode(self, openMode: Any) -> Any:
        """X.setOpenMode(openMode)"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setPauseMode(self, pauseMode: Any) -> Any:
        """X.setPauseMode(pauseMode)"""
        ...

    def setPeerAddress(self, address: Any) -> Any:
        """X.setPeerAddress(address)"""
        ...

    def setPeerName(self, name: Any) -> Any:
        """X.setPeerName(name)"""
        ...

    def setPeerPort(self, port: Any) -> Any:
        """X.setPeerPort(port)"""
        ...

    def setPeerVerifyDepth(self, depth: int) -> None:
        """X.setPeerVerifyDepth(depth)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setPeerVerifyDepth(int *depth*)

Sets the maximum number of certificates in the peer's certificate chain to be checked
during the SSL handshake phase, to *depth*. Setting a depth of 0 means that no maximum
depth is set, indicating that the whole certificate chain should be checked.

The certificates are checked in issuing order, starting with the peer's own certificate,
then its issuer's certificate, and so on.

This function was introduced in Qt 4.4.

**See also**
[peerVerifyDepth](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyDepth)()
and
[setPeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyMode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerVerifyDepth(self, depth: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyDepth"""
        ...

    def setPeerVerifyMode(self, mode: Any) -> None:
        """X.setPeerVerifyMode(mode)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setPeerVerifyMode([QSslSocket::PeerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) *mode*)

Sets the socket's verify mode to *mode*. This mode decides whether
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) should request a
certificate from the peer (i.e., the client requests a certificate from the server, or a
server requesting a certificate from the client), and whether it should require that
this certificate is valid.

The default mode is
[AutoVerifyPeer](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum),
which tells [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) to use
[VerifyPeer](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) for
clients and
[QueryPeer](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#PeerVerifyMode-enum) for
servers.

Setting this mode after encryption has started has no effect on the current connection.

This function was introduced in Qt 4.4.

**See also**
[peerVerifyMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyMode)(),
[setPeerVerifyDepth](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyDepth)(),
and [mode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#mode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerVerifyMode(self, mode: PySide2.QtNetwork.QSslSocket.PeerVerifyMode) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyMode"""
        ...

    def setPeerVerifyName(self, hostName: str) -> None:
        """X.setPeerVerifyName(hostName)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setPeerVerifyName(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*hostName*)

Sets a different host name, given by *hostName*, for the certificate validation instead
of the one used for the TCP connection.

This function was introduced in Qt 4.8.

**See also**
[peerVerifyName](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyName)()
and
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPeerVerifyName(self, hostName: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPeerVerifyName"""
        ...

    def setPrivateKey(self, fileName: Any, algorithm: Any, format: Any, passPhrase: Any) -> None:
        """X.setPrivateKey(fileName, algorithm, format, passPhrase)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setPrivateKey(const [QSslKey](https://doc.qt.io/archives/qt-5.15/qsslkey.html) \\&*key*)

Sets the socket's private [key](https://doc.qt.io/archives/qt-5.15/qsslkey.html) to
*key*. The private key and the local
[certificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) are used by
clients and servers that must prove their identity to SSL peers.

Both the key and the local certificate are required if you are creating an SSL server
socket. If you are creating an SSL client socket, the key and local certificate are
required if your client must identify itself to an SSL server.

**See also**
[privateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#privateKey)() and
[setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificate)().

### void QSslSocket::setPrivateKey(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*fileName*, [QSsl::KeyAlgorithm](https://doc.qt.io/archives/qt-5.15/qssl.html#KeyAlgorithm-enum) *algorithm* \\= QSsl::Rsa, [QSsl::EncodingFormat](https://doc.qt.io/archives/qt-5.15/qssl.html#EncodingFormat-enum) *format* \\= QSsl::Pem, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*passPhrase* \\= QByteArray())

This is an overloaded function.

Reads the string in file *fileName* and decodes it using a specified *algorithm* and
encoding *format* to construct an [SSL
key](https://doc.qt.io/archives/qt-5.15/qsslkey.html). If the encoded key is encrypted,
*passPhrase* is used to decrypt it.

The socket's private key is set to the constructed key. The private key and the local
[certificate](https://doc.qt.io/archives/qt-5.15/qsslcertificate.html) are used by
clients and servers that must prove their identity to SSL peers.

Both the key and the local certificate are required if you are creating an SSL server
socket. If you are creating an SSL client socket, the key and local certificate are
required if your client must identify itself to an SSL server.

**See also**
[privateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#privateKey)() and
[setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPrivateKey(self, fileName: str, algorithm: PySide2.QtNetwork.QSsl.KeyAlgorithm=..., format: PySide2.QtNetwork.QSsl.EncodingFormat=..., passPhrase: PySide2.QtCore.QByteArray=...) -> None
setPrivateKey(self, key: PySide2.QtNetwork.QSslKey) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPrivateKey"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setProtocol(self, protocol: Any) -> None:
        """X.setProtocol(protocol)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setProtocol([QSsl::SslProtocol](https://doc.qt.io/archives/qt-5.15/qssl.html#SslProtocol-enum) *protocol*)

Sets the socket's SSL protocol to *protocol*. This will affect the next initiated
handshake; calling this function on an already-encrypted socket will not affect the
socket's protocol.

**See also** [protocol](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#protocol)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProtocol(self, protocol: PySide2.QtNetwork.QSsl.SslProtocol) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setProtocol"""
        ...

    def setProxy(self, networkProxy: Any) -> Any:
        """X.setProxy(networkProxy)"""
        ...

    def setReadBufferSize(self, size: int) -> None:
        """X.setReadBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QSslSocket::setReadBufferSize([qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *size*)

Reimplements:
[QAbstractSocket::setReadBufferSize](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setReadBufferSize)(qint64
size).

Sets the size of [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html)'s
internal read buffer to be *size* bytes.

This function was introduced in Qt 4.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setReadBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setReadBufferSize"""
        ...

    def setSocketDescriptor(self, socketDescriptor: int, state: Any, openMode: Any) -> bool:
        """X.setSocketDescriptor(socketDescriptor, state, openMode) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QSslSocket::setSocketDescriptor([qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) *socketDescriptor*, [QAbstractSocket::SocketState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum) *state* \\= ConnectedState, [QIODevice::OpenMode](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum) *openMode* \\= ReadWrite)

Reimplements:
[QAbstractSocket::setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketDescriptor)(qintptr
socketDescriptor, QAbstractSocket::SocketState socketState, QIODevice::OpenMode
openMode).

Initializes [QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) with the
native socket descriptor *socketDescriptor*. Returns `true` if *socketDescriptor* is
accepted as a valid socket descriptor; otherwise returns `false`. The socket is opened
in the mode specified by *openMode*, and enters the socket state specified by *state*.

**Note:** It is not possible to initialize two sockets with the same native socket
descriptor.

**See also**
[socketDescriptor](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketDescriptor)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketDescriptor(self, socketDescriptor: int, state: PySide2.QtNetwork.QAbstractSocket.SocketState=..., openMode: PySide2.QtCore.QIODevice.OpenMode=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setSocketDescriptor"""
        ...

    def setSocketError(self, socketError: Any) -> Any:
        """X.setSocketError(socketError)"""
        ...

    def setSocketOption(self, option: Any, value: Any) -> None:
        """X.setSocketOption(option, value)

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` void QSslSocket::setSocketOption([QAbstractSocket::SocketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketOption-enum) *option*, const [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) \\&*value*)

Reimplements:
[QAbstractSocket::setSocketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketOption)(QAbstractSocket::SocketOption
option, const QVariant \\&value).

Sets the given *option* to the value described by *value*.

This function was introduced in Qt 4.6.

**See also**
[socketOption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#socketOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption, value: typing.Any) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setSocketOption"""
        ...

    def setSocketState(self, state: Any) -> Any:
        """X.setSocketState(state)"""
        ...

    def setSslConfiguration(self, config: Any) -> None:
        """X.setSslConfiguration(config)

Supplemental documentation:
Qt 5 reference:

### void QSslSocket::setSslConfiguration(const [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) \\&*configuration*)

Sets the socket's SSL configuration to be the contents of *configuration*. This function
sets the local certificate, the ciphers, the private key and the CA certificates to
those stored in *configuration*.

It is not possible to set the SSL-state related fields.

This function was introduced in Qt 4.4.

**See also**
[sslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslConfiguration)(),
[setLocalCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setLocalCertificate)(),
[setPrivateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setPrivateKey)(),
[QSslConfiguration::setCaCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCaCertificates)(),
and
[QSslConfiguration::setCiphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#setCiphers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSslConfiguration(self, config: PySide2.QtNetwork.QSslConfiguration) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setSslConfiguration"""
        ...

    def setTextModeEnabled(self, enabled: Any) -> Any:
        """X.setTextModeEnabled(enabled)"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def size(self) -> int:
        """X.size() -> int"""
        ...

    def socketDescriptor(self) -> int:
        """X.socketDescriptor() -> int"""
        ...

    def socketOption(self, option: Any) -> Any:
        """X.socketOption(option) -> object

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QVariant](https://doc.qt.io/archives/qt-5.15/qvariant.html) QSslSocket::socketOption([QAbstractSocket::SocketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketOption-enum) *option*)

Reimplements:
[QAbstractSocket::socketOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#socketOption)(QAbstractSocket::SocketOption
option).

Returns the value of the *option* option.

This function was introduced in Qt 4.6.

**See also**
[setSocketOption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setSocketOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
socketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption) -> typing.Any
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#socketOption"""
        ...

    def socketType(self) -> Any:
        """X.socketType()"""
        ...

    def sslConfiguration(self) -> Any:
        """X.sslConfiguration() -> PythonQt.QtNetwork.QSslConfiguration

Supplemental documentation:
Qt 5 reference:

### [QSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html) QSslSocket::sslConfiguration() const

Returns the socket's SSL configuration state. The default SSL configuration of a socket
is to use the default ciphers, default CA certificates, no local private key or
certificate.

The SSL configuration also contains fields that can change with time without notice.

This function was introduced in Qt 4.4.

**See also**
[setSslConfiguration](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setSslConfiguration)(),
[localCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#localCertificate)(),
[peerCertificate](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificate)(),
[peerCertificateChain](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerCertificateChain)(),
[sessionCipher](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sessionCipher)(),
[privateKey](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#privateKey)(),
[QSslConfiguration::ciphers](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#ciphers)(),
and
[QSslConfiguration::caCertificates](https://doc.qt.io/archives/qt-5.15/qsslconfiguration.html#caCertificates)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sslConfiguration(self) -> PySide2.QtNetwork.QSslConfiguration
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslConfiguration"""
        ...

    def sslErrors(self) -> tuple:
        """X.sslErrors() -> tuple

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QSslSocket::sslErrors(const [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QSslError](https://doc.qt.io/archives/qt-5.15/qsslerror.html)\\> \\&*errors*)

[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) emits this signal after
the SSL handshake to indicate that one or more errors have occurred while establishing
the identity of the peer. The errors are usually an indication that
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) is unable to securely
identify the peer. Unless any action is taken, the connection will be dropped after this
signal has been emitted.

If you want to continue connecting despite the errors that have occurred, you must call
[QSslSocket::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)()
from inside a slot connected to this signal. If you need to access the error list at a
later point, you can call
[sslHandshakeErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslHandshakeErrors)().

*errors* contains one or more errors that prevent
[QSslSocket](https://doc.qt.io/archives/qt-5.15/qsslsocket.html) from verifying the
identity of the peer.

**Note:** You cannot use
[Qt::QueuedConnection](https://doc.qt.io/archives/qt-5.15/qt.html#ConnectionType-enum)
when connecting to this signal, or calling
[QSslSocket::ignoreSslErrors](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#ignoreSslErrors)()
will have no effect.

**Note:** Signal *sslErrors* is overloaded in this class. To connect to this signal by
using the function pointer syntax, Qt provides a convenient helper for obtaining the
function pointer as shown in this example:

```
connect(sslSocket, QOverload<const QList<QSslError> &>::of(&QSslSocket::sslErrors),
    [=](const QList<QSslError> &errors){ /* ... */ });
```

**See also**
[peerVerifyError](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#peerVerifyError)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sslErrors(self) -> typing.List[PySide2.QtNetwork.QSslError]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslErrors"""
        ...

    def sslLibraryBuildVersionNumber(self) -> int:
        """X.sslLibraryBuildVersionNumber() -> int

Supplemental documentation:
Qt 5 reference:

### `[static]` long QSslSocket::sslLibraryBuildVersionNumber()

Returns the version number of the SSL library in use at compile time. If no SSL support
is available then this will return an undefined value.

This function was introduced in Qt 5.4.

**See also**
[sslLibraryVersionNumber](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslLibraryVersionNumber)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sslLibraryBuildVersionNumber() -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslLibraryBuildVersionNumber"""
        ...

    def sslLibraryBuildVersionString(self) -> str:
        """X.sslLibraryBuildVersionString() -> str

Supplemental documentation:
Qt 5 reference:

### `[static]` [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslSocket::sslLibraryBuildVersionString()

Returns the version string of the SSL library in use at compile time. If no SSL support
is available then this will return an empty value.

This function was introduced in Qt 5.4.

**See also**
[sslLibraryVersionString](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslLibraryVersionString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sslLibraryBuildVersionString() -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslLibraryBuildVersionString"""
        ...

    def sslLibraryVersionNumber(self) -> int:
        """X.sslLibraryVersionNumber() -> int

Supplemental documentation:
Qt 5 reference:

### `[static]` long QSslSocket::sslLibraryVersionNumber()

Returns the version number of the SSL library in use. Note that this is the version of
the library in use at run-time not compile time. If no SSL support is available then
this will return an undefined value.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
sslLibraryVersionNumber() -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslLibraryVersionNumber"""
        ...

    def sslLibraryVersionString(self) -> str:
        """X.sslLibraryVersionString() -> str

Supplemental documentation:
Qt 5 reference:

### `[static]` [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QSslSocket::sslLibraryVersionString()

Returns the version string of the SSL library in use. Note that this is the version of
the library in use at run-time not compile time. If no SSL support is available then
this will return an empty value.

This function was introduced in Qt 5.0.

Upstream PySide2 reference signatures (binding differences may apply):

```python
sslLibraryVersionString() -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#sslLibraryVersionString"""
        ...

    def startClientEncryption(self) -> None:
        """X.startClientEncryption()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QSslSocket::startClientEncryption()

Starts a delayed SSL handshake for a client connection. This function can be called when
the socket is in the
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
but still in the
[UnencryptedMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum). If
it is not yet connected, or if it is already encrypted, this function has no effect.

Clients that implement STARTTLS functionality often make use of delayed SSL handshakes.
Most other clients can avoid calling this function directly by using
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)()
instead, which automatically performs the handshake.

**See also**
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)()
and
[startServerEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startServerEncryption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
startClientEncryption(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startClientEncryption"""
        ...

    def startServerEncryption(self) -> None:
        """X.startServerEncryption()

Supplemental documentation:
Qt 5 reference:

### `[slot]` void QSslSocket::startServerEncryption()

Starts a delayed SSL handshake for a server connection. This function can be called when
the socket is in the
[ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
but still in
[UnencryptedMode](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#SslMode-enum). If
it is not connected or it is already encrypted, the function has no effect.

For server sockets, calling this function is the only way to initiate the SSL handshake.
Most servers will call this function immediately upon receiving a connection, or as a
result of having received a protocol-specific command to enter SSL mode (e.g, the server
may respond to receiving the string "STARTTLS\\\\r\\\\n" by calling this function).

The most common way to implement an SSL server is to create a subclass of
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html) and reimplement
[QTcpServer::incomingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#incomingConnection)().
The returned socket descriptor is then passed to
[QSslSocket::setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#setSocketDescriptor)().

**See also**
[connectToHostEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#connectToHostEncrypted)()
and
[startClientEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startClientEncryption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
startServerEncryption(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startServerEncryption"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def state(self) -> Any:
        """X.state()"""
        ...

    def stateChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QSslSocket.stateChanged; argument details are not documented."""
        ...

    def supportedCiphers(self) -> tuple:
        """X.supportedCiphers() -> tuple

Upstream PySide2 reference signatures (binding differences may apply):

```python
supportedCiphers() -> typing.List[PySide2.QtNetwork.QSslCipher]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#supportedCiphers"""
        ...

    def supportsSsl(self) -> bool:
        """X.supportsSsl() -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QSslSocket::supportsSsl()

Returns `true` if this platform supports SSL; otherwise, returns false. If the platform
doesn't support SSL, the socket will fail in the connection phase.

Upstream PySide2 reference signatures (binding differences may apply):

```python
supportsSsl() -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#supportsSsl"""
        ...

    def systemCaCertificates(self) -> tuple:
        """X.systemCaCertificates() -> tuple

Upstream PySide2 reference signatures (binding differences may apply):

```python
systemCaCertificates() -> typing.List[PySide2.QtNetwork.QSslCertificate]
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#systemCaCertificates"""
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

    def ungetChar(self, c: Any) -> Any:
        """X.ungetChar(c)"""
        ...

    def waitForBytesWritten(self, msecs: int) -> bool:
        """X.waitForBytesWritten(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QSslSocket::waitForBytesWritten(int *msecs* \\= 30000\\)

Reimplements:
[QAbstractSocket::waitForBytesWritten](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForBytesWritten)(int
msecs).

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForBytesWritten(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForBytesWritten"""
        ...

    def waitForConnected(self, msecs: int) -> bool:
        """X.waitForConnected(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QSslSocket::waitForConnected(int *msecs* \\= 30000\\)

Reimplements:
[QAbstractSocket::waitForConnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForConnected)(int
msecs).

Waits until the socket is connected, or *msecs* milliseconds, whichever happens first.
If the connection has been established, this function returns `true`; otherwise it
returns `false`.

**See also**
[QAbstractSocket::waitForConnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForConnected)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForConnected(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForConnected"""
        ...

    def waitForDisconnected(self, msecs: int) -> bool:
        """X.waitForDisconnected(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QSslSocket::waitForDisconnected(int *msecs* \\= 30000\\)

Reimplements:
[QAbstractSocket::waitForDisconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForDisconnected)(int
msecs).

Waits until the socket has disconnected or *msecs* milliseconds, whichever comes first.
If the connection has been disconnected, this function returns `true`; otherwise it
returns `false`.

**See also**
[QAbstractSocket::waitForDisconnected](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForDisconnected)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForDisconnected(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForDisconnected"""
        ...

    def waitForEncrypted(self, msecs: int) -> bool:
        """X.waitForEncrypted(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QSslSocket::waitForEncrypted(int *msecs* \\= 30000\\)

Waits until the socket has completed the SSL handshake and has emitted
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)(), or *msecs*
milliseconds, whichever comes first. If
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)() has been
emitted, this function returns true; otherwise (e.g., the socket is disconnected, or the
SSL handshake fails), false is returned.

The following example waits up to one second for the socket to be encrypted:

```
socket->connectToHostEncrypted("imap", 993);
if (socket->waitForEncrypted(1000))
    qDebug("Encrypted!");
```

If msecs is -1, this function will not time out.

**See also**
[startClientEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startClientEncryption)(),
[startServerEncryption](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#startServerEncryption)(),
[encrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#encrypted)(), and
[isEncrypted](https://doc.qt.io/archives/qt-5.15/qsslsocket.html#isEncrypted)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForEncrypted(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForEncrypted"""
        ...

    def waitForReadyRead(self, msecs: int) -> bool:
        """X.waitForReadyRead(msecs) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` bool QSslSocket::waitForReadyRead(int *msecs* \\= 30000\\)

Reimplements:
[QAbstractSocket::waitForReadyRead](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#waitForReadyRead)(int
msecs).

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForReadyRead(self, msecs: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#waitForReadyRead"""
        ...

    def write(self, data: Any) -> int:
        """X.write(data) -> int"""
        ...

    def writeData(self, data: str, len: int) -> int:
        """X.writeData(data, len) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QSslSocket::writeData(const char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *len*)

Reimplements:
[QAbstractSocket::writeData](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#writeData)(const
char \\*data, qint64 size).

Upstream PySide2 reference signatures (binding differences may apply):

```python
writeData(self, data: str, len: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qsslsocket.html#writeData"""
        ...
    AddressInUseError: Any
    AnyIPProtocol: Any
    Append: Any
    AutoVerifyPeer: Any
    BindFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BindMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BoundState: Any
    ClosingState: Any
    ConnectedState: Any
    ConnectingState: Any
    ConnectionRefusedError: Any
    DatagramTooLargeError: Any
    DefaultForPlatform: Any
    DontShareAddress: Any
    HostLookupState: Any
    HostNotFoundError: Any
    IPv4Protocol: Any
    IPv6Protocol: Any
    KeepAliveOption: Any
    ListeningState: Any
    LowDelayOption: Any
    MulticastLoopbackOption: Any
    MulticastTtlOption: Any
    NetworkError: Any
    NetworkLayerProtocol: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NotOpen: Any
    OpenMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenModeFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OperationError: Any
    PathMtuSocketOption: Any
    PauseMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseModes: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseNever: Any
    PauseOnSslErrors: Any
    PeerVerifyMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    ProxyAuthenticationRequiredError: Any
    ProxyConnectionClosedError: Any
    ProxyConnectionRefusedError: Any
    ProxyConnectionTimeoutError: Any
    ProxyNotFoundError: Any
    ProxyProtocolError: Any
    QueryPeer: Any
    ReadOnly: Any
    ReadWrite: Any
    ReceiveBufferSizeSocketOption: Any
    RemoteHostClosedError: Any
    ReuseAddressHint: Any
    SctpSocket: Any
    SendBufferSizeSocketOption: Any
    ShareAddress: Any
    SocketAccessError: Any
    SocketAddressNotAvailableError: Any
    SocketError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketOption: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketResourceError: Any
    SocketState: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketTimeoutError: Any
    SocketType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslClientMode: Any
    SslHandshakeFailedError: Any
    SslInternalError: Any
    SslInvalidUserDataError: Any
    SslMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslServerMode: Any
    TcpSocket: Any
    TemporaryError: Any
    Text: Any
    Truncate: Any
    TypeOfServiceOption: Any
    UdpSocket: Any
    Unbuffered: Any
    UnconnectedState: Any
    UnencryptedMode: Any
    UnfinishedSocketOperationError: Any
    UnknownNetworkLayerProtocol: Any
    UnknownSocketError: Any
    UnknownSocketType: Any
    UnsupportedSocketOperationError: Any
    VerifyNone: Any
    VerifyPeer: Any
    WriteOnly: Any
    objectName: Any

class QTcpServer:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

This class makes it possible to accept incoming TCP connections. You can specify the
port or have QTcpServer pick one automatically. You can listen on a specific address or
on all the machine's addresses.

Call [listen](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen)() to have the
server listen for incoming connections. The
[newConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#newConnection)()
signal is then emitted each time a client connects to the server.

Call
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#nextPendingConnection)()
to accept the pending connection as a connected
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html). The function returns a
pointer to a [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) in
[QAbstractSocket::ConnectedState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum)
that you can use for communicating with the client.

If an error occurs,
[serverError](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverError)() returns
the type of error, and
[errorString](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#errorString)() can be
called to get a human readable description of what happened.

When listening for connections, the address and port on which the server is listening
are available as
[serverAddress](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverAddress)() and
[serverPort](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverPort)().

Calling [close](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#close)() makes
QTcpServer stop listening for incoming connections.

Although QTcpServer is mostly designed for use with an event loop, it's possible to use
it without one. In that case, you must use
[waitForNewConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#waitForNewConnection)(),
which blocks until either a connection is available or a timeout expires.

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def acceptError(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpServer.acceptError; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QTcpServer::acceptError([QAbstractSocket::SocketError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum) *socketError*)

This signal is emitted when accepting a new connection results in an error. The
*socketError* parameter describes the type of error that occurred.

This function was introduced in Qt 5.0.

**See also**
[pauseAccepting](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#pauseAccepting)()
and
[resumeAccepting](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#resumeAccepting)().

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#acceptError"""
        ...

    def addPendingConnection(self, socket: Any) -> None:
        """X.addPendingConnection(socket)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QTcpServer::addPendingConnection([QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) \\**socket*)

This function is called by
[QTcpServer::incomingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#incomingConnection)()
to add the *socket* to the list of pending incoming connections.

**Note:** Don't forget to call this member from reimplemented
[incomingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#incomingConnection)()
if you do not want to break the Pending Connections mechanism.

This function was introduced in Qt 4.7.

**See also**
[incomingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#incomingConnection)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
addPendingConnection(self, socket: PySide2.QtNetwork.QTcpSocket) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#addPendingConnection"""
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

    def close(self) -> None:
        """X.close()

Supplemental documentation:
Qt 5 reference:

### void QTcpServer::close()

Closes the server. The server will no longer listen for incoming connections.

**See also** [listen](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
close(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#close"""
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
        """Native PythonQt.QtNetwork.QTcpServer.destroyed; argument details are not documented."""
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

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QTcpServer::errorString() const

Returns a human readable description of the last error that occurred.

**See also**
[serverError](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverError)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
errorString(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#errorString"""
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

    def hasPendingConnections(self) -> bool:
        """X.hasPendingConnections() -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QTcpServer::hasPendingConnections() const

Returns `true` if the server has a pending connection; otherwise returns `false`.

**See also**
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#nextPendingConnection)()
and
[setMaxPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setMaxPendingConnections)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasPendingConnections(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#hasPendingConnections"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def incomingConnection(self, handle: int) -> None:
        """X.incomingConnection(handle)

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QTcpServer::incomingConnection([qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) *socketDescriptor*)

This virtual function is called by
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html) when a new connection
is available. The *socketDescriptor* argument is the native socket descriptor for the
accepted connection.

The base implementation creates a
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html), sets the socket
descriptor and then stores the
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) in an internal list of
pending connections. Finally
[newConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#newConnection)() is
emitted.

Reimplement this function to alter the server's behavior when a connection is available.

If this server is using
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) then the
*socketDescriptor* may not be usable with native socket functions, and should only be
used with
[QTcpSocket::setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#setSocketDescriptor)().

**Note:** If another socket is created in the reimplementation of this method, it needs
to be added to the Pending Connections mechanism by calling
[addPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#addPendingConnection)().

**Note:** If you want to handle an incoming connection as a new
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) object in another
thread you have to pass the
[socketDescriptor](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#socketDescriptor)
to the other thread and create the
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) object there and use
its
[setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setSocketDescriptor)()
method.

**See also**
[newConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#newConnection)(),
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#nextPendingConnection)(),
and
[addPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#addPendingConnection)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
incomingConnection(self, handle: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#incomingConnection"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isListening(self) -> bool:
        """X.isListening() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QTcpServer::isListening() const

Returns `true` if the server is currently listening for incoming connections; otherwise
returns `false`.

**See also** [listen](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isListening(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#isListening"""
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

    def listen(self, address: Any, port: int) -> bool:
        """X.listen(address, port) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QTcpServer::listen(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*address* \\= QHostAddress::Any, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port* \\= 0\\)

Tells the server to listen for incoming connections on address *address* and port
*port*. If *port* is 0, a port is chosen automatically. If *address* is
[QHostAddress::Any](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum),
the server will listen on all network interfaces.

Returns `true` on success; otherwise returns `false`.

**See also**
[isListening](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#isListening)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
listen(self, address: PySide2.QtNetwork.QHostAddress=..., port: int=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen"""
        ...

    def maxPendingConnections(self) -> int:
        """X.maxPendingConnections() -> int

Supplemental documentation:
Qt 5 reference:

### int QTcpServer::maxPendingConnections() const

Returns the maximum number of pending accepted connections. The default is 30\\.

**See also**
[setMaxPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setMaxPendingConnections)()
and
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#hasPendingConnections)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
maxPendingConnections(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#maxPendingConnections"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def newConnection(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpServer.newConnection; argument details are not documented.

Supplemental documentation:
Qt 5 reference:

### `[signal]` void QTcpServer::newConnection()

This signal is emitted every time a new connection is available.

**See also**
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#hasPendingConnections)()
and
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#nextPendingConnection)().

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#newConnection"""
        ...

    def nextPendingConnection(self) -> Any:
        """X.nextPendingConnection() -> PythonQt.QtNetwork.QTcpSocket

Supplemental documentation:
Qt 5 reference:

### `[virtual]` [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) \\*QTcpServer::nextPendingConnection()

Returns the next pending connection as a connected
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) object.

The socket is created as a child of the server, which means that it is automatically
deleted when the [QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html) object
is destroyed. It is still a good idea to delete the object explicitly when you are done
with it, to avoid wasting memory.

`nullptr` is returned if this function is called when there are no pending connections.

**Note:** The returned [QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html)
object cannot be used from another thread. If you want to use an incoming connection
from another thread, you need to override
[incomingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#incomingConnection)().

**See also**
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#hasPendingConnections)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
nextPendingConnection(self) -> PySide2.QtNetwork.QTcpSocket
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#nextPendingConnection"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpServer.objectNameChanged; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def pauseAccepting(self) -> None:
        """X.pauseAccepting()

Supplemental documentation:
Qt 5 reference:

### void QTcpServer::pauseAccepting()

Pauses accepting new connections. Queued connections will remain in queue.

This function was introduced in Qt 5.0.

**See also**
[resumeAccepting](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#resumeAccepting)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
pauseAccepting(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#pauseAccepting"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def proxy(self) -> Any:
        """X.proxy() -> PythonQt.QtNetwork.QNetworkProxy

Supplemental documentation:
Qt 5 reference:

### [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) QTcpServer::proxy() const

Returns the network proxy for this socket. By default
[QNetworkProxy::DefaultProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
is used.

This function was introduced in Qt 4.1.

**See also** [setProxy](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setProxy)()
and [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
proxy(self) -> PySide2.QtNetwork.QNetworkProxy
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#proxy"""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def resumeAccepting(self) -> None:
        """X.resumeAccepting()

Supplemental documentation:
Qt 5 reference:

### void QTcpServer::resumeAccepting()

Resumes accepting new connections.

This function was introduced in Qt 5.0.

**See also**
[pauseAccepting](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#pauseAccepting)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
resumeAccepting(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#resumeAccepting"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def serverAddress(self) -> Any:
        """X.serverAddress() -> PythonQt.QtNetwork.QHostAddress

Supplemental documentation:
Qt 5 reference:

### [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) QTcpServer::serverAddress() const

Returns the server's address if the server is listening for connections; otherwise
returns
[QHostAddress::Null](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum).

**See also**
[serverPort](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverPort)() and
[listen](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
serverAddress(self) -> PySide2.QtNetwork.QHostAddress
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverAddress"""
        ...

    def serverError(self) -> Any:
        """X.serverError()

Supplemental documentation:
Qt 5 reference:

### [QAbstractSocket::SocketError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum) QTcpServer::serverError() const

Returns an error code for the last error that occurred.

**See also**
[errorString](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#errorString)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
serverError(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverError"""
        ...

    def serverPort(self) -> int:
        """X.serverPort() -> int

Supplemental documentation:
Qt 5 reference:

### [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) QTcpServer::serverPort() const

Returns the server's port if the server is listening for connections; otherwise returns
0\\.

**See also**
[serverAddress](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverAddress)() and
[listen](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#listen)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
serverPort(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#serverPort"""
        ...

    def setMaxPendingConnections(self, numConnections: int) -> None:
        """X.setMaxPendingConnections(numConnections)

Supplemental documentation:
Qt 5 reference:

### void QTcpServer::setMaxPendingConnections(int *numConnections*)

Sets the maximum number of pending accepted connections to *numConnections*.
[QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html) will accept no more
than *numConnections* incoming connections before
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#nextPendingConnection)()
is called. By default, the limit is 30 pending connections.

Clients may still able to connect after the server has reached its maximum number of
pending connections (i.e.,
[QTcpSocket](https://doc.qt.io/archives/qt-5.15/qtcpsocket.html) can still emit the
connected() signal). [QTcpServer](https://doc.qt.io/archives/qt-5.15/qtcpserver.html)
will stop accepting the new connections, but the operating system may still keep them in
queue.

**See also**
[maxPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#maxPendingConnections)()
and
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#hasPendingConnections)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMaxPendingConnections(self, numConnections: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setMaxPendingConnections"""
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

    def setProxy(self, networkProxy: Any) -> None:
        """X.setProxy(networkProxy)

Supplemental documentation:
Qt 5 reference:

### void QTcpServer::setProxy(const [QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html) \\&*networkProxy*)

Sets the explicit network proxy for this socket to *networkProxy*.

To disable the use of a proxy for this socket, use the
[QNetworkProxy::NoProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html#ProxyType-enum)
proxy type:

```
server->setProxy(QNetworkProxy::NoProxy);
```

This function was introduced in Qt 4.1.

**See also** [proxy](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#proxy)() and
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProxy(self, networkProxy: PySide2.QtNetwork.QNetworkProxy) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setProxy"""
        ...

    def setSocketDescriptor(self, socketDescriptor: int) -> bool:
        """X.setSocketDescriptor(socketDescriptor) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QTcpServer::setSocketDescriptor([qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) *socketDescriptor*)

Sets the socket descriptor this server should use when listening for incoming
connections to *socketDescriptor*. Returns `true` if the socket is set successfully;
otherwise returns `false`.

The socket is assumed to be in listening state.

**See also**
[socketDescriptor](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#socketDescriptor)()
and [isListening](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#isListening)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSocketDescriptor(self, socketDescriptor: int) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setSocketDescriptor"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def socketDescriptor(self) -> int:
        """X.socketDescriptor() -> int

Supplemental documentation:
Qt 5 reference:

### [qintptr](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qintptr-typedef) QTcpServer::socketDescriptor() const

Returns the native socket descriptor the server uses to listen for incoming
instructions, or -1 if the server is not listening.

If the server is using
[QNetworkProxy](https://doc.qt.io/archives/qt-5.15/qnetworkproxy.html), the returned
descriptor may not be usable with native socket functions.

**See also**
[setSocketDescriptor](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#setSocketDescriptor)()
and [isListening](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#isListening)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
socketDescriptor(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#socketDescriptor"""
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

    def waitForNewConnection(self, msec: int, timedOut: Any) -> bool:
        """X.waitForNewConnection(msec, timedOut) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QTcpServer::waitForNewConnection(int *msec* \\= 0, bool \\**timedOut* \\= nullptr)

Waits for at most *msec* milliseconds or until an incoming connection is available.
Returns `true` if a connection is available; otherwise returns `false`. If the operation
timed out and *timedOut* is not `nullptr`, \\**timedOut* will be set to true.

This is a blocking function call. Its use is disadvised in a single-threaded GUI
application, since the whole application will stop responding until the function
returns. waitForNewConnection() is mostly useful when there is no event loop available.

The non-blocking alternative is to connect to the
[newConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#newConnection)()
signal.

If msec is -1, this function will not time out.

**See also**
[hasPendingConnections](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#hasPendingConnections)()
and
[nextPendingConnection](https://doc.qt.io/archives/qt-5.15/qtcpserver.html#nextPendingConnection)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
waitForNewConnection(self, msec: int) -> typing.Tuple[bool, bool]
```

Source: https://doc.qt.io/archives/qt-5.15/qtcpserver.html#waitForNewConnection"""
        ...
    objectName: Any

class QTcpSocket:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

TCP (Transmission Control Protocol) is a reliable, stream-oriented, connection-oriented
transport protocol. It is especially well suited for continuous transmission of data.

QTcpSocket is a convenience subclass of
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) that allows
you to establish a TCP connection and transfer streams of data. See the
[QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html) documentation
for details.

**Note:** TCP sockets cannot be opened in
[QIODevice::Unbuffered](https://doc.qt.io/archives/qt-5.15/qiodevice.html#OpenModeFlag-enum)
mode.

Source: https://doc.qt.io/archives/qt-5.15/qtcpsocket.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abort(self) -> Any:
        """X.abort()"""
        ...

    def aboutToClose(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.aboutToClose; argument details are not documented."""
        ...

    def atEnd(self) -> bool:
        """X.atEnd() -> bool"""
        ...

    def bind(self, address: Any, port: Any, mode: Any) -> bool:
        """X.bind(address, port, mode) -> bool"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def bytesAvailable(self) -> int:
        """X.bytesAvailable() -> int"""
        ...

    def bytesToWrite(self) -> int:
        """X.bytesToWrite() -> int"""
        ...

    def bytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.bytesWritten; argument details are not documented."""
        ...

    def canReadLine(self) -> bool:
        """X.canReadLine() -> bool"""
        ...

    def channelBytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.channelBytesWritten; argument details are not documented."""
        ...

    def channelReadyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.channelReadyRead; argument details are not documented."""
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

    def close(self) -> Any:
        """X.close()"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def connectToHost(self, hostName: Any, port: Any, mode: Any, protocol: Any) -> Any:
        """X.connectToHost(hostName, port, mode, protocol)"""
        ...

    def connected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.connected; argument details are not documented."""
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
        """Native PythonQt.QtNetwork.QTcpSocket.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def disconnectFromHost(self) -> Any:
        """X.disconnectFromHost()"""
        ...

    def disconnected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.disconnected; argument details are not documented."""
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

    def error(self) -> Any:
        """X.error()"""
        ...

    def errorOccurred(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.errorOccurred; argument details are not documented."""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str"""
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

    def flush(self) -> bool:
        """X.flush() -> bool"""
        ...

    def getChar(self, c: Any) -> bool:
        """X.getChar(c) -> bool"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hostFound(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.hostFound; argument details are not documented."""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isOpen(self) -> bool:
        """X.isOpen() -> bool"""
        ...

    def isReadable(self) -> bool:
        """X.isReadable() -> bool"""
        ...

    def isSequential(self) -> bool:
        """X.isSequential() -> bool"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isTextModeEnabled(self) -> bool:
        """X.isTextModeEnabled() -> bool"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def isWritable(self) -> bool:
        """X.isWritable() -> bool"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def localAddress(self) -> Any:
        """X.localAddress() -> PythonQt.QtNetwork.QHostAddress"""
        ...

    def localPort(self) -> int:
        """X.localPort() -> int"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.objectNameChanged; argument details are not documented."""
        ...

    def open(self, mode: Any) -> bool:
        """X.open(mode) -> bool"""
        ...

    def openMode(self) -> Any:
        """X.openMode()"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def pauseMode(self) -> Any:
        """X.pauseMode()"""
        ...

    def peek(self, maxlen: Any) -> Any:
        """X.peek(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def peerAddress(self) -> Any:
        """X.peerAddress() -> PythonQt.QtNetwork.QHostAddress"""
        ...

    def peerName(self) -> str:
        """X.peerName() -> str"""
        ...

    def peerPort(self) -> int:
        """X.peerPort() -> int"""
        ...

    def pos(self) -> int:
        """X.pos() -> int"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def proxy(self) -> Any:
        """X.proxy() -> PythonQt.QtNetwork.QNetworkProxy"""
        ...

    def proxyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.proxyAuthenticationRequired; argument details are not documented."""
        ...

    def putChar(self, c: Any) -> bool:
        """X.putChar(c) -> bool"""
        ...

    def read(self, maxlen: Any) -> Any:
        """X.read(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readAll(self) -> Any:
        """X.readAll() -> PythonQt.QtCore.QByteArray"""
        ...

    def readBufferSize(self) -> int:
        """X.readBufferSize() -> int"""
        ...

    def readChannelFinished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.readChannelFinished; argument details are not documented."""
        ...

    def readData(self, data: Any, maxlen: Any) -> int:
        """X.readData(data, maxlen) -> int"""
        ...

    def readLine(self, maxlen: Any) -> Any:
        """X.readLine(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readLineData(self, data: Any, maxlen: Any) -> int:
        """X.readLineData(data, maxlen) -> int"""
        ...

    def readyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.readyRead; argument details are not documented."""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def reset(self) -> bool:
        """X.reset() -> bool"""
        ...

    def resume(self) -> Any:
        """X.resume()"""
        ...

    def seek(self, pos: Any) -> bool:
        """X.seek(pos) -> bool"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setErrorString(self, errorString: Any) -> Any:
        """X.setErrorString(errorString)"""
        ...

    def setLocalAddress(self, address: Any) -> Any:
        """X.setLocalAddress(address)"""
        ...

    def setLocalPort(self, port: Any) -> Any:
        """X.setLocalPort(port)"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setOpenMode(self, openMode: Any) -> Any:
        """X.setOpenMode(openMode)"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setPauseMode(self, pauseMode: Any) -> Any:
        """X.setPauseMode(pauseMode)"""
        ...

    def setPeerAddress(self, address: Any) -> Any:
        """X.setPeerAddress(address)"""
        ...

    def setPeerName(self, name: Any) -> Any:
        """X.setPeerName(name)"""
        ...

    def setPeerPort(self, port: Any) -> Any:
        """X.setPeerPort(port)"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setProxy(self, networkProxy: Any) -> Any:
        """X.setProxy(networkProxy)"""
        ...

    def setReadBufferSize(self, size: Any) -> Any:
        """X.setReadBufferSize(size)"""
        ...

    def setSocketDescriptor(self, socketDescriptor: Any, state: Any, openMode: Any) -> bool:
        """X.setSocketDescriptor(socketDescriptor, state, openMode) -> bool"""
        ...

    def setSocketError(self, socketError: Any) -> Any:
        """X.setSocketError(socketError)"""
        ...

    def setSocketOption(self, option: Any, value: Any) -> Any:
        """X.setSocketOption(option, value)"""
        ...

    def setSocketState(self, state: Any) -> Any:
        """X.setSocketState(state)"""
        ...

    def setTextModeEnabled(self, enabled: Any) -> Any:
        """X.setTextModeEnabled(enabled)"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def size(self) -> int:
        """X.size() -> int"""
        ...

    def socketDescriptor(self) -> int:
        """X.socketDescriptor() -> int"""
        ...

    def socketOption(self, option: Any) -> Any:
        """X.socketOption(option) -> object"""
        ...

    def socketType(self) -> Any:
        """X.socketType()"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def state(self) -> Any:
        """X.state()"""
        ...

    def stateChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QTcpSocket.stateChanged; argument details are not documented."""
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

    def ungetChar(self, c: Any) -> Any:
        """X.ungetChar(c)"""
        ...

    def waitForBytesWritten(self, msecs: Any) -> bool:
        """X.waitForBytesWritten(msecs) -> bool"""
        ...

    def waitForConnected(self, msecs: Any) -> bool:
        """X.waitForConnected(msecs) -> bool"""
        ...

    def waitForDisconnected(self, msecs: Any) -> bool:
        """X.waitForDisconnected(msecs) -> bool"""
        ...

    def waitForReadyRead(self, msecs: Any) -> bool:
        """X.waitForReadyRead(msecs) -> bool"""
        ...

    def write(self, data: Any) -> int:
        """X.write(data) -> int"""
        ...

    def writeData(self, data: Any, len: Any) -> int:
        """X.writeData(data, len) -> int"""
        ...
    AddressInUseError: Any
    AnyIPProtocol: Any
    Append: Any
    BindFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BindMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BoundState: Any
    ClosingState: Any
    ConnectedState: Any
    ConnectingState: Any
    ConnectionRefusedError: Any
    DatagramTooLargeError: Any
    DefaultForPlatform: Any
    DontShareAddress: Any
    HostLookupState: Any
    HostNotFoundError: Any
    IPv4Protocol: Any
    IPv6Protocol: Any
    KeepAliveOption: Any
    ListeningState: Any
    LowDelayOption: Any
    MulticastLoopbackOption: Any
    MulticastTtlOption: Any
    NetworkError: Any
    NetworkLayerProtocol: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NotOpen: Any
    OpenMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenModeFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OperationError: Any
    PathMtuSocketOption: Any
    PauseMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseModes: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseNever: Any
    PauseOnSslErrors: Any
    ProxyAuthenticationRequiredError: Any
    ProxyConnectionClosedError: Any
    ProxyConnectionRefusedError: Any
    ProxyConnectionTimeoutError: Any
    ProxyNotFoundError: Any
    ProxyProtocolError: Any
    ReadOnly: Any
    ReadWrite: Any
    ReceiveBufferSizeSocketOption: Any
    RemoteHostClosedError: Any
    ReuseAddressHint: Any
    SctpSocket: Any
    SendBufferSizeSocketOption: Any
    ShareAddress: Any
    SocketAccessError: Any
    SocketAddressNotAvailableError: Any
    SocketError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketOption: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketResourceError: Any
    SocketState: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketTimeoutError: Any
    SocketType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslHandshakeFailedError: Any
    SslInternalError: Any
    SslInvalidUserDataError: Any
    TcpSocket: Any
    TemporaryError: Any
    Text: Any
    Truncate: Any
    TypeOfServiceOption: Any
    UdpSocket: Any
    Unbuffered: Any
    UnconnectedState: Any
    UnfinishedSocketOperationError: Any
    UnknownNetworkLayerProtocol: Any
    UnknownSocketError: Any
    UnknownSocketType: Any
    UnsupportedSocketOperationError: Any
    WriteOnly: Any
    objectName: Any

class QUdpSocket:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

UDP (User Datagram Protocol) is a lightweight, unreliable, datagram-oriented,
connectionless protocol. It can be used when reliability isn't important. QUdpSocket is
a subclass of [QAbstractSocket](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html)
that allows you to send and receive UDP datagrams.

The most common way to use this class is to bind to an address and port using
[bind](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind)(), then call
[writeDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#writeDatagram)() and
[readDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#readDatagram)() /
[receiveDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#receiveDatagram)()
to transfer data. If you want to use the standard
[QIODevice](https://doc.qt.io/archives/qt-5.15/qiodevice.html) functions
[read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)(),
[readLine](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readLine)(),
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)(), etc., you must first
connect the socket directly to a peer by calling
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)().

The socket emits the
[bytesWritten](https://doc.qt.io/archives/qt-5.15/qiodevice.html#bytesWritten)() signal
every time a datagram is written to the network. If you just want to send datagrams, you
don't need to call
[bind](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#bind)().

The [readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)() signal is
emitted whenever datagrams arrive. In that case,
[hasPendingDatagrams](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#hasPendingDatagrams)()
returns `true`. Call
[pendingDatagramSize](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#pendingDatagramSize)()
to obtain the size of the first pending datagram, and
[readDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#readDatagram)() or
[receiveDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#receiveDatagram)()
to read it.

**Note:** An incoming datagram should be read when you receive the
[readyRead](https://doc.qt.io/archives/qt-5.15/qiodevice.html#readyRead)() signal,
otherwise this signal will not be emitted for the next datagram.

Example:

```
void Server::initSocket()
{
    udpSocket = new QUdpSocket(this);
    udpSocket->bind(QHostAddress::LocalHost, 7755);

    connect(udpSocket, &QUdpSocket::readyRead,
            this, &Server::readPendingDatagrams);
}

void Server::readPendingDatagrams()
{
    while (udpSocket->hasPendingDatagrams()) {
        QNetworkDatagram datagram = udpSocket->receiveDatagram();
        processTheDatagram(datagram);
    }
}
```

QUdpSocket also supports UDP multicast. Use
[joinMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#joinMulticastGroup)()
and
[leaveMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#leaveMulticastGroup)()
to control group membership, and
[QAbstractSocket::MulticastTtlOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketOption-enum)
and
[QAbstractSocket::MulticastLoopbackOption](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketOption-enum)
to set the TTL and loopback socket options. Use
[setMulticastInterface](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#setMulticastInterface)()
to control the outgoing interface for multicast datagrams, and
[multicastInterface](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#multicastInterface)()
to query it.

With QUdpSocket, you can also establish a virtual connection to a UDP server using
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)()
and then use [read](https://doc.qt.io/archives/qt-5.15/qiodevice.html#read)() and
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() to exchange datagrams
without specifying the receiver for each datagram.

The [Broadcast
Sender](https://doc.qt.io/archives/qt-5.15/qtnetwork-broadcastsender-example.html),
[Broadcast
Receiver](https://doc.qt.io/archives/qt-5.15/qtnetwork-broadcastreceiver-example.html),
[Multicast
Sender](https://doc.qt.io/archives/qt-5.15/qtnetwork-multicastsender-example.html), and
[Multicast
Receiver](https://doc.qt.io/archives/qt-5.15/qtnetwork-multicastreceiver-example.html)
examples illustrate how to use QUdpSocket in applications.

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def abort(self) -> Any:
        """X.abort()"""
        ...

    def aboutToClose(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.aboutToClose; argument details are not documented."""
        ...

    def atEnd(self) -> bool:
        """X.atEnd() -> bool"""
        ...

    def bind(self, address: Any, port: Any, mode: Any) -> bool:
        """X.bind(address, port, mode) -> bool"""
        ...

    def blockSignals(self, b: Any) -> bool:
        """X.blockSignals(b) -> bool"""
        ...

    def bytesAvailable(self) -> int:
        """X.bytesAvailable() -> int"""
        ...

    def bytesToWrite(self) -> int:
        """X.bytesToWrite() -> int"""
        ...

    def bytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.bytesWritten; argument details are not documented."""
        ...

    def canReadLine(self) -> bool:
        """X.canReadLine() -> bool"""
        ...

    def channelBytesWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.channelBytesWritten; argument details are not documented."""
        ...

    def channelReadyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.channelReadyRead; argument details are not documented."""
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

    def close(self) -> Any:
        """X.close()"""
        ...

    def connect(self, signal: Any, receiver: Any, slot: Any, type: Any) -> bool:
        """X.connect(signal, receiver, slot, type) -> bool"""
        ...

    def connectToHost(self, hostName: Any, port: Any, mode: Any, protocol: Any) -> Any:
        """X.connectToHost(hostName, port, mode, protocol)"""
        ...

    def connected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.connected; argument details are not documented."""
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
        """Native PythonQt.QtNetwork.QUdpSocket.destroyed; argument details are not documented."""
        ...

    def disconnect(self, signal: Any, receiver: Any, slot: Any) -> bool:
        """X.disconnect(signal, receiver, slot) -> bool"""
        ...

    def disconnectFromHost(self) -> Any:
        """X.disconnectFromHost()"""
        ...

    def disconnected(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.disconnected; argument details are not documented."""
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

    def error(self) -> Any:
        """X.error()"""
        ...

    def errorOccurred(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.errorOccurred; argument details are not documented."""
        ...

    def errorString(self) -> str:
        """X.errorString() -> str"""
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

    def flush(self) -> bool:
        """X.flush() -> bool"""
        ...

    def getChar(self, c: Any) -> bool:
        """X.getChar(c) -> bool"""
        ...

    def hasPendingDatagrams(self) -> bool:
        """X.hasPendingDatagrams() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QUdpSocket::hasPendingDatagrams() const

Returns `true` if at least one datagram is waiting to be read; otherwise returns
`false`.

**See also**
[pendingDatagramSize](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#pendingDatagramSize)()
and [readDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#readDatagram)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasPendingDatagrams(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#hasPendingDatagrams"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def hostFound(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.hostFound; argument details are not documented."""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def installEventFilter(self, filterObj: Any) -> Any:
        """X.installEventFilter(filterObj)"""
        ...

    def isOpen(self) -> bool:
        """X.isOpen() -> bool"""
        ...

    def isReadable(self) -> bool:
        """X.isReadable() -> bool"""
        ...

    def isSequential(self) -> bool:
        """X.isSequential() -> bool"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isTextModeEnabled(self) -> bool:
        """X.isTextModeEnabled() -> bool"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool"""
        ...

    def isWidgetType(self) -> bool:
        """X.isWidgetType() -> bool"""
        ...

    def isWindowType(self) -> bool:
        """X.isWindowType() -> bool"""
        ...

    def isWritable(self) -> bool:
        """X.isWritable() -> bool"""
        ...

    def joinMulticastGroup(self, groupAddress: Any, iface: Any) -> bool:
        """X.joinMulticastGroup(groupAddress, iface) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QUdpSocket::joinMulticastGroup(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*groupAddress*)

Joins the multicast group specified by *groupAddress* on the default interface chosen by
the operating system. The socket must be in
[BoundState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
otherwise an error occurs.

Note that if you are attempting to join an IPv4 group, your socket must not be bound
using IPv6 (or in dual mode, using
[QHostAddress::Any](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum)).
You must use
[QHostAddress::AnyIPv4](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#SpecialAddress-enum)
instead.

This function returns `true` if successful; otherwise it returns `false` and sets the
socket error accordingly.

**Note:** Joining IPv6 multicast groups without an interface selection is not supported
in all operating systems. Consider using the overload where the interface is specified.

This function was introduced in Qt 4.8.

**See also**
[leaveMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#leaveMulticastGroup)().

### bool QUdpSocket::joinMulticastGroup(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*groupAddress*, const [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) \\&*iface*)

This is an overloaded function.

Joins the multicast group address *groupAddress* on the interface *iface*.

This function was introduced in Qt 4.8.

**See also**
[leaveMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#leaveMulticastGroup)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
joinMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress) -> bool
joinMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress, iface: PySide2.QtNetwork.QNetworkInterface) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#joinMulticastGroup"""
        ...

    def killTimer(self, id: Any) -> Any:
        """X.killTimer(id)"""
        ...

    def leaveMulticastGroup(self, groupAddress: Any, iface: Any) -> bool:
        """X.leaveMulticastGroup(groupAddress, iface) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QUdpSocket::leaveMulticastGroup(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*groupAddress*)

Leaves the multicast group specified by *groupAddress* on the default interface chosen
by the operating system. The socket must be in
[BoundState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
otherwise an error occurs.

This function returns `true` if successful; otherwise it returns `false` and sets the
socket error accordingly.

**Note:** This function should be called with the same arguments as were passed to
[joinMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#joinMulticastGroup)().

This function was introduced in Qt 4.8.

**See also**
[joinMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#joinMulticastGroup)().

### bool QUdpSocket::leaveMulticastGroup(const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*groupAddress*, const [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) \\&*iface*)

This is an overloaded function.

Leaves the multicast group specified by *groupAddress* on the interface *iface*.

**Note:** This function should be called with the same arguments as were passed to
[joinMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#joinMulticastGroup)().

This function was introduced in Qt 4.8.

**See also**
[joinMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#joinMulticastGroup)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
leaveMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress) -> bool
leaveMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress, iface: PySide2.QtNetwork.QNetworkInterface) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#leaveMulticastGroup"""
        ...

    def localAddress(self) -> Any:
        """X.localAddress() -> PythonQt.QtNetwork.QHostAddress"""
        ...

    def localPort(self) -> int:
        """X.localPort() -> int"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def multicastInterface(self) -> Any:
        """X.multicastInterface() -> PythonQt.QtNetwork.QNetworkInterface

Supplemental documentation:
Qt 5 reference:

### [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) QUdpSocket::multicastInterface() const

Returns the interface for the outgoing interface for multicast datagrams. This
corresponds to the IP\\_MULTICAST\\_IF socket option for IPv4 sockets and the
IPV6\\_MULTICAST\\_IF socket option for IPv6 sockets. If no interface has been previously
set, this function returns an invalid
[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html). The
socket must be in
[BoundState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
otherwise an invalid
[QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) is
returned.

This function was introduced in Qt 4.8.

**See also**
[setMulticastInterface](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#setMulticastInterface)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
multicastInterface(self) -> PySide2.QtNetwork.QNetworkInterface
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#multicastInterface"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.objectNameChanged; argument details are not documented."""
        ...

    def open(self, mode: Any) -> bool:
        """X.open(mode) -> bool"""
        ...

    def openMode(self) -> Any:
        """X.openMode()"""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def pauseMode(self) -> Any:
        """X.pauseMode()"""
        ...

    def peek(self, maxlen: Any) -> Any:
        """X.peek(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def peerAddress(self) -> Any:
        """X.peerAddress() -> PythonQt.QtNetwork.QHostAddress"""
        ...

    def peerName(self) -> str:
        """X.peerName() -> str"""
        ...

    def peerPort(self) -> int:
        """X.peerPort() -> int"""
        ...

    def pendingDatagramSize(self) -> int:
        """X.pendingDatagramSize() -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QUdpSocket::pendingDatagramSize() const

Returns the size of the first pending UDP datagram. If there is no datagram available,
this function returns -1.

**See also**
[hasPendingDatagrams](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#hasPendingDatagrams)()
and [readDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#readDatagram)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
pendingDatagramSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#pendingDatagramSize"""
        ...

    def pos(self) -> int:
        """X.pos() -> int"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def proxy(self) -> Any:
        """X.proxy() -> PythonQt.QtNetwork.QNetworkProxy"""
        ...

    def proxyAuthenticationRequired(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.proxyAuthenticationRequired; argument details are not documented."""
        ...

    def putChar(self, c: Any) -> bool:
        """X.putChar(c) -> bool"""
        ...

    def read(self, maxlen: Any) -> Any:
        """X.read(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readAll(self) -> Any:
        """X.readAll() -> PythonQt.QtCore.QByteArray"""
        ...

    def readBufferSize(self) -> int:
        """X.readBufferSize() -> int"""
        ...

    def readChannelFinished(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.readChannelFinished; argument details are not documented."""
        ...

    def readData(self, data: Any, maxlen: Any) -> int:
        """X.readData(data, maxlen) -> int"""
        ...

    def readDatagram(self, data: str, maxlen: int, host: Any, port: Any) -> int:
        """X.readDatagram(data, maxlen, host, port) -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QUdpSocket::readDatagram(char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *maxSize*, [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\**address* \\= nullptr, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) \\**port* \\= nullptr)

Receives a datagram no larger than *maxSize* bytes and stores it in *data*. The sender's
host address and port is stored in \\**address* and \\**port* (unless the pointers are
`nullptr`).

Returns the size of the datagram on success; otherwise returns -1.

If *maxSize* is too small, the rest of the datagram will be lost. To avoid loss of data,
call
[pendingDatagramSize](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#pendingDatagramSize)()
to determine the size of the pending datagram before attempting to read it. If *maxSize*
is 0, the datagram will be discarded.

**See also**
[writeDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#writeDatagram)(),
[hasPendingDatagrams](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#hasPendingDatagrams)(),
and
[pendingDatagramSize](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#pendingDatagramSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
readDatagram(self, data: str, maxlen: int, host: PySide2.QtNetwork.QHostAddress) -> typing.Tuple[int, int]
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#readDatagram"""
        ...

    def readLine(self, maxlen: Any) -> Any:
        """X.readLine(maxlen) -> PythonQt.QtCore.QByteArray"""
        ...

    def readLineData(self, data: Any, maxlen: Any) -> int:
        """X.readLineData(data, maxlen) -> int"""
        ...

    def readyRead(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.readyRead; argument details are not documented."""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def reset(self) -> bool:
        """X.reset() -> bool"""
        ...

    def resume(self) -> Any:
        """X.resume()"""
        ...

    def seek(self, pos: Any) -> bool:
        """X.seek(pos) -> bool"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setErrorString(self, errorString: Any) -> Any:
        """X.setErrorString(errorString)"""
        ...

    def setLocalAddress(self, address: Any) -> Any:
        """X.setLocalAddress(address)"""
        ...

    def setLocalPort(self, port: Any) -> Any:
        """X.setLocalPort(port)"""
        ...

    def setMulticastInterface(self, iface: Any) -> None:
        """X.setMulticastInterface(iface)

Supplemental documentation:
Qt 5 reference:

### void QUdpSocket::setMulticastInterface(const [QNetworkInterface](https://doc.qt.io/archives/qt-5.15/qnetworkinterface.html) \\&*iface*)

Sets the outgoing interface for multicast datagrams to the interface *iface*. This
corresponds to the IP\\_MULTICAST\\_IF socket option for IPv4 sockets and the
IPV6\\_MULTICAST\\_IF socket option for IPv6 sockets. The socket must be in
[BoundState](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketState-enum),
otherwise this function does nothing.

This function was introduced in Qt 4.8.

**See also**
[multicastInterface](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#multicastInterface)(),
[joinMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#joinMulticastGroup)(),
and
[leaveMulticastGroup](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#leaveMulticastGroup)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMulticastInterface(self, iface: PySide2.QtNetwork.QNetworkInterface) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#setMulticastInterface"""
        ...

    def setObjectName(self, name: Any) -> Any:
        """X.setObjectName(name)"""
        ...

    def setOpenMode(self, openMode: Any) -> Any:
        """X.setOpenMode(openMode)"""
        ...

    def setParent(self, parent: Any) -> Any:
        """X.setParent(parent)"""
        ...

    def setPauseMode(self, pauseMode: Any) -> Any:
        """X.setPauseMode(pauseMode)"""
        ...

    def setPeerAddress(self, address: Any) -> Any:
        """X.setPeerAddress(address)"""
        ...

    def setPeerName(self, name: Any) -> Any:
        """X.setPeerName(name)"""
        ...

    def setPeerPort(self, port: Any) -> Any:
        """X.setPeerPort(port)"""
        ...

    def setProperty(self, name: Any, value: Any) -> bool:
        """X.setProperty(name, value) -> bool"""
        ...

    def setProxy(self, networkProxy: Any) -> Any:
        """X.setProxy(networkProxy)"""
        ...

    def setReadBufferSize(self, size: Any) -> Any:
        """X.setReadBufferSize(size)"""
        ...

    def setSocketDescriptor(self, socketDescriptor: Any, state: Any, openMode: Any) -> bool:
        """X.setSocketDescriptor(socketDescriptor, state, openMode) -> bool"""
        ...

    def setSocketError(self, socketError: Any) -> Any:
        """X.setSocketError(socketError)"""
        ...

    def setSocketOption(self, option: Any, value: Any) -> Any:
        """X.setSocketOption(option, value)"""
        ...

    def setSocketState(self, state: Any) -> Any:
        """X.setSocketState(state)"""
        ...

    def setTextModeEnabled(self, enabled: Any) -> Any:
        """X.setTextModeEnabled(enabled)"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def size(self) -> int:
        """X.size() -> int"""
        ...

    def socketDescriptor(self) -> int:
        """X.socketDescriptor() -> int"""
        ...

    def socketOption(self, option: Any) -> Any:
        """X.socketOption(option) -> object"""
        ...

    def socketType(self) -> Any:
        """X.socketType()"""
        ...

    def startTimer(self, interval: Any, timerType: Any) -> int:
        """X.startTimer(interval, timerType) -> int"""
        ...

    def state(self) -> Any:
        """X.state()"""
        ...

    def stateChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtNetwork.QUdpSocket.stateChanged; argument details are not documented."""
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

    def ungetChar(self, c: Any) -> Any:
        """X.ungetChar(c)"""
        ...

    def waitForBytesWritten(self, msecs: Any) -> bool:
        """X.waitForBytesWritten(msecs) -> bool"""
        ...

    def waitForConnected(self, msecs: Any) -> bool:
        """X.waitForConnected(msecs) -> bool"""
        ...

    def waitForDisconnected(self, msecs: Any) -> bool:
        """X.waitForDisconnected(msecs) -> bool"""
        ...

    def waitForReadyRead(self, msecs: Any) -> bool:
        """X.waitForReadyRead(msecs) -> bool"""
        ...

    def write(self, data: Any) -> int:
        """X.write(data) -> int"""
        ...

    def writeData(self, data: Any, len: Any) -> int:
        """X.writeData(data, len) -> int"""
        ...

    def writeDatagram(self, datagram: Any, host: Any, port: Any) -> int:
        """X.writeDatagram(datagram, host, port) -> int

Supplemental documentation:
Qt 5 reference:

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QUdpSocket::writeDatagram(const char \\**data*, [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) *size*, const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*address*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*)

Sends the datagram at *data* of size *size* to the host address *address* at port
*port*. Returns the number of bytes sent on success; otherwise returns -1.

Datagrams are always written as one block. The maximum size of a datagram is highly
platform-dependent, but can be as low as 8192 bytes. If the datagram is too large, this
function will return -1 and
[error](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#error)() will return
[DatagramTooLargeError](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#SocketError-enum).

Sending datagrams larger than 512 bytes is in general disadvised, as even if they are
sent successfully, they are likely to be fragmented by the IP layer before arriving at
their final destination.

**Warning:** Calling this function on a connected UDP socket may result in an error and
no packet being sent. If you are using a connected socket, use
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() to send datagrams.

**See also**
[readDatagram](https://doc.qt.io/archives/qt-5.15/qudpsocket.html#readDatagram)() and
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)().

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QUdpSocket::writeDatagram(const [QNetworkDatagram](https://doc.qt.io/archives/qt-5.15/qnetworkdatagram.html) \\&*datagram*)

This is an overloaded function.

Sends the datagram *datagram* to the host address and port numbers contained in
*datagram*, using the network interface and hop count limits also set there. If the
destination address and port numbers are unset, this function will send to the address
that was passed to
[connectToHost](https://doc.qt.io/archives/qt-5.15/qabstractsocket.html#connectToHost)().

If the destination address is IPv6 with a non-empty [scope
id](https://doc.qt.io/archives/qt-5.15/qhostaddress.html#scopeId) but differs from the
interface index in *datagram*, it is undefined which interface the operating system will
choose to send on.

The function returns the number of bytes sent if it succeeded or -1 if it encountered an
error.

**Warning:** Calling this function on a connected UDP socket may result in an error and
no packet being sent. If you are using a connected socket, use
[write](https://doc.qt.io/archives/qt-5.15/qiodevice.html#write)() to send datagrams.

This function was introduced in Qt 5.8.

**See also**
[QNetworkDatagram::setDestination](https://doc.qt.io/archives/qt-5.15/qnetworkdatagram.html#setDestination)(),
[QNetworkDatagram::setHopLimit](https://doc.qt.io/archives/qt-5.15/qnetworkdatagram.html#setHopLimit)(),
and
[QNetworkDatagram::setInterfaceIndex](https://doc.qt.io/archives/qt-5.15/qnetworkdatagram.html#setInterfaceIndex)().

### [qint64](https://doc.qt.io/archives/qt-5.15/qtglobal.html#qint64-typedef) QUdpSocket::writeDatagram(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*datagram*, const [QHostAddress](https://doc.qt.io/archives/qt-5.15/qhostaddress.html) \\&*host*, [quint16](https://doc.qt.io/archives/qt-5.15/qtglobal.html#quint16-typedef) *port*)

This is an overloaded function.

Sends the datagram *datagram* to the host address *host* and at port *port*.

The function returns the number of bytes sent if it succeeded or -1 if it encountered an
error.

Upstream PySide2 reference signatures (binding differences may apply):

```python
writeDatagram(self, datagram: PySide2.QtCore.QByteArray, host: PySide2.QtNetwork.QHostAddress, port: int) -> int
writeDatagram(self, datagram: PySide2.QtNetwork.QNetworkDatagram) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qudpsocket.html#writeDatagram"""
        ...
    AddressInUseError: Any
    AnyIPProtocol: Any
    Append: Any
    BindFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BindMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BoundState: Any
    ClosingState: Any
    ConnectedState: Any
    ConnectingState: Any
    ConnectionRefusedError: Any
    DatagramTooLargeError: Any
    DefaultForPlatform: Any
    DontShareAddress: Any
    HostLookupState: Any
    HostNotFoundError: Any
    IPv4Protocol: Any
    IPv6Protocol: Any
    KeepAliveOption: Any
    ListeningState: Any
    LowDelayOption: Any
    MulticastLoopbackOption: Any
    MulticastTtlOption: Any
    NetworkError: Any
    NetworkLayerProtocol: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    NotOpen: Any
    OpenMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenModeFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OperationError: Any
    PathMtuSocketOption: Any
    PauseMode: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseModes: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    PauseNever: Any
    PauseOnSslErrors: Any
    ProxyAuthenticationRequiredError: Any
    ProxyConnectionClosedError: Any
    ProxyConnectionRefusedError: Any
    ProxyConnectionTimeoutError: Any
    ProxyNotFoundError: Any
    ProxyProtocolError: Any
    ReadOnly: Any
    ReadWrite: Any
    ReceiveBufferSizeSocketOption: Any
    RemoteHostClosedError: Any
    ReuseAddressHint: Any
    SctpSocket: Any
    SendBufferSizeSocketOption: Any
    ShareAddress: Any
    SocketAccessError: Any
    SocketAddressNotAvailableError: Any
    SocketError: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketOption: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketResourceError: Any
    SocketState: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SocketTimeoutError: Any
    SocketType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    SslHandshakeFailedError: Any
    SslInternalError: Any
    SslInvalidUserDataError: Any
    TcpSocket: Any
    TemporaryError: Any
    Text: Any
    Truncate: Any
    TypeOfServiceOption: Any
    UdpSocket: Any
    Unbuffered: Any
    UnconnectedState: Any
    UnfinishedSocketOperationError: Any
    UnknownNetworkLayerProtocol: Any
    UnknownSocketError: Any
    UnknownSocketType: Any
    UnsupportedSocketOperationError: Any
    WriteOnly: Any
    objectName: Any
__all__ = ['QAbstractNetworkCache', 'QAbstractSocket', 'QAuthenticator', 'QDnsDomainNameRecord', 'QDnsHostAddressRecord', 'QDnsLookup', 'QDnsMailExchangeRecord', 'QDnsServiceRecord', 'QDnsTextRecord', 'QHostAddress', 'QHostInfo', 'QHttpMultiPart', 'QHttpPart', 'QIPv6Address', 'QLocalServer', 'QLocalSocket', 'QNetworkAccessManager', 'QNetworkAddressEntry', 'QNetworkCacheMetaData', 'QNetworkConfiguration', 'QNetworkConfigurationManager', 'QNetworkCookie', 'QNetworkCookieJar', 'QNetworkDiskCache', 'QNetworkInterface', 'QNetworkProxy', 'QNetworkProxyFactory', 'QNetworkProxyQuery', 'QNetworkReply', 'QNetworkRequest', 'QNetworkSession', 'QSsl', 'QSslCertificate', 'QSslCertificateExtension', 'QSslCipher', 'QSslConfiguration', 'QSslEllipticCurve', 'QSslError', 'QSslKey', 'QSslPreSharedKeyAuthenticator', 'QSslSocket', 'QTcpServer', 'QTcpSocket', 'QUdpSocket']
