# this_file: src/fontlab_echopy/PythonQt/QtOpenGL.pyi
# Generated from native metadata and independent enrichment inputs.
"""Native API for PythonQt.QtOpenGL."""
from __future__ import annotations
from typing import Any

class QGLBuffer:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Buffer objects are created in the GL server so that the client application can avoid
uploading vertices, indices, texture image data, etc every time they are needed.

QGLBuffer objects can be copied around as a reference to the underlying GL buffer
object:

```
    QGLBuffer buffer1(QGLBuffer::IndexBuffer);
    buffer1.create();

    QGLBuffer buffer2 = buffer1;
```

QGLBuffer performs a shallow copy when objects are copied in this manner, but does not
implement copy-on-write semantics. The original object will be affected whenever the
copy is modified.

**Note:** This class has been deprecated in favor of
[QOpenGLBuffer](https://doc.qt.io/archives/qt-5.15/qopenglbuffer.html).

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def allocate(self, data: Any, count: int) -> None:
        """X.allocate(data, count)

Supplemental documentation:
Qt 5 reference:

### void QGLBuffer::allocate(const void \\**data*, int *count*)

Allocates *count* bytes of space to the buffer, initialized to the contents of *data*.
Any previous contents will be removed.

It is assumed that [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)()
has been called on this buffer and that it has been bound to the current context.

**See also** [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)(),
[read](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#read)(), and
[write](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#write)().

### void QGLBuffer::allocate(int *count*)

This is an overloaded function.

Allocates *count* bytes of space to the buffer. Any previous contents will be removed.

It is assumed that [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)()
has been called on this buffer and that it has been bound to the current context.

**See also** [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)() and
[write](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#write)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
allocate(self, count: int) -> None
allocate(self, data: int, count: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#allocate"""
        ...

    def bind(self) -> bool:
        """X.bind() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLBuffer::bind()

Binds the buffer associated with this object to the current GL context. Returns `false`
if binding was not possible, usually because
[type](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#type)() is not supported on
this GL implementation.

The buffer must be bound to the same QGLContext current when
[create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)() was called, or to
another QGLContext that is sharing with it. Otherwise, false will be returned from this
function.

**See also** [release](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#release)() and
[create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bind(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#bind"""
        ...

    def bufferId(self) -> int:
        """X.bufferId() -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLBuffer::bufferId() const

Returns the GL identifier associated with this buffer; zero if the buffer has not been
created.

**See also** [isCreated](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#isCreated)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bufferId(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#bufferId"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def create(self) -> bool:
        """X.create() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLBuffer::create()

Creates the buffer object in the GL server. Returns `true` if the object was created;
false otherwise.

This function must be called with a current QGLContext. The buffer will be bound to and
can only be used in that context (or any other context that is shared with it).

This function will return false if the GL implementation does not support buffers, or
there is no current QGLContext.

**See also** [isCreated](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#isCreated)(),
[allocate](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#allocate)(),
[write](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#write)(), and
[destroy](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#destroy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
create(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def destroy(self) -> None:
        """X.destroy()

Supplemental documentation:
Qt 5 reference:

### void QGLBuffer::destroy()

Destroys this buffer object, including the storage being used in the GL server. All
references to the buffer will become invalid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
destroy(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#destroy"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isCreated(self) -> bool:
        """X.isCreated() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLBuffer::isCreated() const

Returns `true` if this buffer has been created; false otherwise.

**See also** [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)() and
[destroy](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#destroy)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isCreated(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#isCreated"""
        ...

    def map(self, access: Any) -> int:
        """X.map(access)

Supplemental documentation:
Qt 5 reference:

### void \\*QGLBuffer::map([QGLBuffer::Access](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#Access-enum) *access*)

Maps the contents of this buffer into the application's memory space and returns a
pointer to it. Returns null if memory mapping is not possible. The *access* parameter
indicates the type of access to be performed.

It is assumed that [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)()
has been called on this buffer and that it has been bound to the current context.

This function is only supported under OpenGL/ES if the `GL_OES_mapbuffer` extension is
present.

**See also** [unmap](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#unmap)(),
[create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)(), and
[bind](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#bind)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
map(self, access: PySide2.QtOpenGL.QGLBuffer.Access) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#map"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtOpenGL.QGLBuffer"""
        ...

    def read(self, offset: int, data: int, count: int) -> bool:
        """X.read(offset, data, count) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLBuffer::read(int *offset*, void \\**data*, int *count*)

Reads the *count* bytes in this buffer starting at *offset* into *data*. Returns `true`
on success; false if reading from the buffer is not supported. Buffer reading is not
supported under OpenGL/ES.

It is assumed that this buffer has been bound to the current context.

**See also** [write](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#write)() and
[bind](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#bind)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
read(self, offset: int, data: int, count: int) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#read"""
        ...

    def release(self) -> None:
        """X.release()

Supplemental documentation:
Qt 5 reference:

### void QGLBuffer::release()

Releases the buffer associated with this object from the current GL context.

This function must be called with the same QGLContext current as when
[bind](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#bind)() was called on the
buffer.

**See also** [bind](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#bind)().

### `[static]` void QGLBuffer::release([QGLBuffer::Type](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#Type-enum) *type*)

Releases the buffer associated with *type* in the current QGLContext.

This function is a direct call to `glBindBuffer(type, 0)` for use when the caller does
not know which [QGLBuffer](https://doc.qt.io/archives/qt-5.15/qglbuffer.html) has been
bound to the context but wants to make sure that it is released.

```
    QGLBuffer::release(QGLBuffer::VertexBuffer);
```

Upstream PySide2 reference signatures (binding differences may apply):

```python
release(self) -> None
release(type: PySide2.QtOpenGL.QGLBuffer.Type) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#release"""
        ...

    def setUsagePattern(self, value: Any) -> None:
        """X.setUsagePattern(value)

Supplemental documentation:
Qt 5 reference:

### void QGLBuffer::setUsagePattern([QGLBuffer::UsagePattern](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#UsagePattern-enum) *value*)

Sets the usage pattern for this buffer object to *value*. This function must be called
before [allocate](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#allocate)() or
[write](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#write)().

**See also**
[usagePattern](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#usagePattern)(),
[allocate](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#allocate)(), and
[write](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#write)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUsagePattern(self, value: PySide2.QtOpenGL.QGLBuffer.UsagePattern) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#setUsagePattern"""
        ...

    def size(self) -> int:
        """X.size() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLBuffer::size() const

Returns the size of the data in this buffer, for reading operations. Returns -1 if
fetching the buffer size is not supported, or the buffer has not been created.

It is assumed that this buffer has been bound to the current context.

**See also** [isCreated](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#isCreated)()
and [bind](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#bind)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
size(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#size"""
        ...

    def type(self) -> Any:
        """X.type()

Supplemental documentation:
Qt 5 reference:

### [QGLBuffer::Type](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#Type-enum) QGLBuffer::type() const

Returns the type of buffer represented by this object.

Upstream PySide2 reference signatures (binding differences may apply):

```python
type(self) -> PySide2.QtOpenGL.QGLBuffer.Type
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#type"""
        ...

    def unmap(self) -> bool:
        """X.unmap() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLBuffer::unmap()

Unmaps the buffer after it was mapped into the application's memory space with a
previous call to [map](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#map)(). Returns
`true` if the unmap succeeded; false otherwise.

It is assumed that this buffer has been bound to the current context, and that it was
previously mapped with [map](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#map)().

This function is only supported under OpenGL/ES if the `GL_OES_mapbuffer` extension is
present.

**See also** [map](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#map)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
unmap(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#unmap"""
        ...

    def usagePattern(self) -> Any:
        """X.usagePattern()

Supplemental documentation:
Qt 5 reference:

### [QGLBuffer::UsagePattern](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#UsagePattern-enum) QGLBuffer::usagePattern() const

Returns the usage pattern for this buffer object. The default value is
[StaticDraw](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#UsagePattern-enum).

**See also**
[setUsagePattern](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#setUsagePattern)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
usagePattern(self) -> PySide2.QtOpenGL.QGLBuffer.UsagePattern
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#usagePattern"""
        ...

    def write(self, offset: int, data: int, count: int) -> None:
        """X.write(offset, data, count)

Supplemental documentation:
Qt 5 reference:

### void QGLBuffer::write(int *offset*, const void \\**data*, int *count*)

Replaces the *count* bytes of this buffer starting at *offset* with the contents of
*data*. Any other bytes in the buffer will be left unmodified.

It is assumed that [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)()
has been called on this buffer and that it has been bound to the current context.

**See also** [create](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#create)(),
[read](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#read)(), and
[allocate](https://doc.qt.io/archives/qt-5.15/qglbuffer.html#allocate)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
write(self, offset: int, data: int, count: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglbuffer.html#write"""
        ...
    Access: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    DynamicCopy: Any
    DynamicDraw: Any
    DynamicRead: Any
    IndexBuffer: Any
    PixelPackBuffer: Any
    PixelUnpackBuffer: Any
    ReadOnly: Any
    ReadWrite: Any
    StaticCopy: Any
    StaticDraw: Any
    StaticRead: Any
    StreamCopy: Any
    StreamDraw: Any
    StreamRead: Any
    Type: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    UsagePattern: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    VertexBuffer: Any
    WriteOnly: Any

class QGLColormap:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QGLColormap provides a platform independent way of specifying and installing indexed
colormaps for a [QGLWidget](https://doc.qt.io/archives/qt-5.15/qglwidget.html).
QGLColormap is especially useful when using the OpenGL color-index mode.

Under X11 you must use an X server that supports either a `PseudoColor` or `DirectColor`
visual class. If your X server currently only provides a `GrayScale`, `TrueColor`,
`StaticColor` or `StaticGray` visual, you will not be able to allocate colorcells for
writing. If this is the case, try setting your X server to 8 bit mode. It should then
provide you with at least a `PseudoColor` visual. Note that you may experience colormap
flashing if your X server is running in 8 bit mode.

The [size](https://doc.qt.io/archives/qt-5.15/qglcolormap.html#size)() of the colormap
is always set to 256 colors. Note that under Windows you can also install colormaps in
child widgets.

This class uses [implicit
sharing](https://doc.qt.io/archives/qt-5.15/implicit-sharing.html) as a memory and speed
optimization.

Example of use:

```
#include <QApplication>
#include <QGLColormap>

int main()
{
    QApplication app(argc, argv);

    MySuperGLWidget widget;     // a QGLWidget in color-index mode
    QGLColormap colormap;

    // This will fill the colormap with colors ranging from
    // black to white.
    for (int i = 0; i < colormap.size(); i++)
        colormap.setEntry(i, qRgb(i, i, i));

    widget.setColormap(colormap);
    widget.show();
    return app.exec();
}
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def entryColor(self, idx: int) -> Any:
        """X.entryColor(idx) -> PythonQt.QtGui.QColor

Supplemental documentation:
Qt 5 reference:

### [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) QGLColormap::entryColor(int *idx*) const

Returns the [QRgb](https://doc.qt.io/archives/qt-5.15/qcolor.html#QRgb-typedef) value in
the colorcell with index *idx*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
entryColor(self, idx: int) -> PySide2.QtGui.QColor
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#entryColor"""
        ...

    def entryRgb(self, idx: int) -> int:
        """X.entryRgb(idx) -> int

Supplemental documentation:
Qt 5 reference:

### [QRgb](https://doc.qt.io/archives/qt-5.15/qcolor.html#QRgb-typedef) QGLColormap::entryRgb(int *idx*) const

Returns the [QRgb](https://doc.qt.io/archives/qt-5.15/qcolor.html#QRgb-typedef) value in
the colorcell with index *idx*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
entryRgb(self, idx: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#entryRgb"""
        ...

    def find(self, color: int) -> int:
        """X.find(color) -> int

Supplemental documentation:
Qt 5 reference:

### int QGLColormap::find([QRgb](https://doc.qt.io/archives/qt-5.15/qcolor.html#QRgb-typedef) *color*) const

Returns the index of the color *color*. If *color* is not in the map, -1 is returned.

Upstream PySide2 reference signatures (binding differences may apply):

```python
find(self, color: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#find"""
        ...

    def findNearest(self, color: int) -> int:
        """X.findNearest(color) -> int

Supplemental documentation:
Qt 5 reference:

### int QGLColormap::findNearest([QRgb](https://doc.qt.io/archives/qt-5.15/qcolor.html#QRgb-typedef) *color*) const

Returns the index of the color that is the closest match to color *color*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
findNearest(self, color: int) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#findNearest"""
        ...

    def handle(self) -> int:
        """X.handle()

Upstream PySide2 reference signatures (binding differences may apply):

```python
handle(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#handle"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def isEmpty(self) -> bool:
        """X.isEmpty() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLColormap::isEmpty() const

Returns `true` if the colormap is empty or it is not in use by a QGLWidget; otherwise
returns `false`.

A colormap with no color values set is considered to be empty. For historical reasons, a
colormap that has color values set but which is not in use by a QGLWidget is also
considered empty.

Compare [size](https://doc.qt.io/archives/qt-5.15/qglcolormap.html#size)() with zero to
determine if the colormap is empty regardless of whether it is in use by a QGLWidget or
not.

**See also** [size](https://doc.qt.io/archives/qt-5.15/qglcolormap.html#size)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isEmpty(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#isEmpty"""
        ...

    def setEntry(self, idx: int, color: Any) -> None:
        """X.setEntry(idx, color)

Supplemental documentation:
Qt 5 reference:

### void QGLColormap::setEntry(int *idx*, [QRgb](https://doc.qt.io/archives/qt-5.15/qcolor.html#QRgb-typedef) *color*)

Set cell at index *idx* in the colormap to color *color*.

### void QGLColormap::setEntry(int *idx*, const [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) \\&*color*)

This is an overloaded function.

Set the cell with index *idx* in the colormap to color *color*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
setEntry(self, idx: int, color: PySide2.QtGui.QColor) -> None
setEntry(self, idx: int, color: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#setEntry"""
        ...

    def setHandle(self, ahandle: int) -> None:
        """X.setHandle(ahandle)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setHandle(self, ahandle: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#setHandle"""
        ...

    def size(self) -> int:
        """X.size() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLColormap::size() const

Returns the number of colorcells in the colormap.

Upstream PySide2 reference signatures (binding differences may apply):

```python
size(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcolormap.html#size"""
        ...

class QGLContext:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

An OpenGL rendering context is a complete set of OpenGL state variables. The rendering
context's [format](https://doc.qt.io/archives/qt-5.15/qgl.html#FormatOption-enum) is set
in the constructor, but it can also be set later with
[setFormat](https://doc.qt.io/archives/qt-5.15/qglcontext.html#setFormat)(). The format
options that are actually set are returned by
[format](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format)(); the options you
asked for are returned by
[requestedFormat](https://doc.qt.io/archives/qt-5.15/qglcontext.html#requestedFormat)().
Note that after a QGLContext object has been constructed, the actual OpenGL context must
be created by explicitly calling the
[create](https://doc.qt.io/archives/qt-5.15/qglcontext.html#create)() function. The
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglcontext.html#makeCurrent)() function
makes this context the current rendering context. You can make *no* context current
using [doneCurrent](https://doc.qt.io/archives/qt-5.15/qglcontext.html#doneCurrent)().
The [reset](https://doc.qt.io/archives/qt-5.15/qglcontext.html#reset)() function will
reset the context and make it invalid.

You can examine properties of the context with, e.g.
[isValid](https://doc.qt.io/archives/qt-5.15/qglcontext.html#isValid)(),
[isSharing](https://doc.qt.io/archives/qt-5.15/qglcontext.html#isSharing)(),
[initialized](https://doc.qt.io/archives/qt-5.15/qglcontext.html#initialized)(),
[windowCreated](https://doc.qt.io/archives/qt-5.15/qglcontext.html#windowCreated)() and
[overlayTransparentColor](https://doc.qt.io/archives/qt-5.15/qglcontext.html#overlayTransparentColor)().

If you're using double buffering you can swap the screen contents with the off-screen
buffer using
[swapBuffers](https://doc.qt.io/archives/qt-5.15/qglcontext.html#swapBuffers)().

Please note that QGLContext is not thread safe.

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def areSharing(self, context1: Any, context2: Any) -> bool:
        """X.areSharing(context1, context2) -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLContext::areSharing(const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext-obsolete.html#QGLContext) \\**context1*, const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext-obsolete.html#QGLContext) \\**context2*)

Returns `true` if *context1* and *context2* are sharing their GL resources such as
textures, shader programs, etc; otherwise returns `false`.

This function was introduced in Qt 4.6.

Upstream PySide2 reference signatures (binding differences may apply):

```python
areSharing(context1: PySide2.QtOpenGL.QGLContext, context2: PySide2.QtOpenGL.QGLContext) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#areSharing"""
        ...

    def bindTexture(self, image: Any, target: Any, format: Any, options: Any) -> int:
        """X.bindTexture(image, target, format, options) -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLContext::bindTexture(const [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) \\&*image*, GLenum *target*, GLint *format*, [QGLContext::BindOptions](https://doc.qt.io/archives/qt-5.15/qglcontext.html#BindOption-enum) *options*)

Generates and binds a 2D GL texture to the current context, based on *image*. The
generated texture id is returned and can be used in later `glBindTexture()` calls.

The *target* parameter specifies the texture target. The default target is
`GL_TEXTURE_2D`.

The *format* parameter sets the internal format for the texture. The default format is
`GL_RGBA`.

The binding *options* are a set of options used to decide how to bind the texture to the
context.

The texture that is generated is cached, so multiple calls to bindTexture() with the
same [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) will return the same
texture id.

Note that we assume default values for the glPixelStore() and glPixelTransfer()
parameters.

This function was introduced in Qt 4.6.

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#deleteTexture)().

### GLuint QGLContext::bindTexture(const [QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html) \\&*pixmap*, GLenum *target*, GLint *format*, [QGLContext::BindOptions](https://doc.qt.io/archives/qt-5.15/qglcontext.html#BindOption-enum) *options*)

This is an overloaded function.

Generates and binds a 2D GL texture to the current context, based on *pixmap*.

This function was introduced in Qt 4.6.

### GLuint QGLContext::bindTexture(const [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) \\&*image*, GLenum *target* \\= GL\\_TEXTURE\\_2D, GLint *format* \\= GL\\_RGBA)

Generates and binds a 2D GL texture to the current context, based on *image*. The
generated texture id is returned and can be used in later `glBindTexture()` calls.

This is an overloaded function.

### GLuint QGLContext::bindTexture(const [QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html) \\&*pixmap*, GLenum *target* \\= GL\\_TEXTURE\\_2D, GLint *format* \\= GL\\_RGBA)

This is an overloaded function.

Generates and binds a 2D GL texture based on *pixmap*.

### GLuint QGLContext::bindTexture(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*fileName*)

This is an overloaded function.

Reads the compressed texture file *fileName* and generates a 2D GL texture from it.

This function can load DirectDrawSurface (DDS) textures in the DXT1, DXT3 and DXT5 DDS
formats if the `GL_ARB_texture_compression` and `GL_EXT_texture_compression_s3tc`
extensions are supported.

Since 4.6.1, textures in the ETC1 format can be loaded if the
`GL_OES_compressed_ETC1_RGB8_texture` extension is supported and the ETC1 texture has
been encapsulated in the PVR container format. Also, textures in the PVRTC2 and PVRTC4
formats can be loaded if the `GL_IMG_texture_compression_pvrtc` extension is supported.

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#deleteTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bindTexture(self, fileName: str) -> int
bindTexture(self, image: PySide2.QtGui.QImage, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
bindTexture(self, image: PySide2.QtGui.QImage, target: int=..., format: int=...) -> int
bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int=..., format: int=...) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#bindTexture"""
        ...

    def chooseContext(self, shareContext: Any) -> bool:
        """X.chooseContext(shareContext) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` bool QGLContext::chooseContext(const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext-obsolete.html#QGLContext) \\**shareContext* \\= 0\\)

This semi-internal function is called by
[create](https://doc.qt.io/archives/qt-5.15/qglcontext.html#create)(). It creates a
system-dependent OpenGL handle that matches the
[format](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format)() of *shareContext*
as closely as possible, returning true if successful or false if a suitable handle could
not be found.

On Windows, it calls the virtual function choosePixelFormat(), which finds a matching
pixel format identifier. On X11, it calls the virtual function chooseVisual() which
finds an appropriate X visual. On other platforms it may work differently.

Upstream PySide2 reference signatures (binding differences may apply):

```python
chooseContext(self, shareContext: typing.Optional[PySide2.QtOpenGL.QGLContext]=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#chooseContext"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def colorIndex(self, c: Any) -> int:
        """X.colorIndex(c) -> int

Upstream PySide2 reference signatures (binding differences may apply):

```python
colorIndex(self, c: PySide2.QtGui.QColor) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#colorIndex"""
        ...

    def contextHandle(self) -> Any:
        """X.contextHandle() -> PythonQt.QtGui.QOpenGLContext

Supplemental documentation:
Qt 5 reference:

### [QOpenGLContext](https://doc.qt.io/archives/qt-5.15/qopenglcontext.html) \\*QGLContext::contextHandle() const

Returns the OpenGL context handle.

Upstream PySide2 reference signatures (binding differences may apply):

```python
contextHandle(self) -> PySide2.QtGui.QOpenGLContext
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#contextHandle"""
        ...

    def create(self, shareContext: Any) -> bool:
        """X.create(shareContext) -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QGLContext::create(const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext-obsolete.html#QGLContext) \\**shareContext* \\= nullptr)

Creates the GL context. Returns `true` if it was successful in creating a valid GL
rendering context on the paint device specified in the constructor; otherwise returns
`false` (i.e. the context is invalid).

If the OpenGL implementation on your system does not support the requested version of
OpenGL context, then [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html)
will try to create the closest matching version. The actual created context properties
can be queried using the QGLFormat returned by the
[format](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format)() function. For
example, if you request a context that supports OpenGL 4.3 Core profile but the driver
and/or hardware only supports version 3.2 Core profile contexts then you will get a 3.2
Core profile context.

After successful creation,
[format](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format)() returns the set of
features of the created GL rendering context.

If *shareContext* points to a valid
[QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html), this method will try
to establish OpenGL display list and texture object sharing between this context and the
*shareContext*. Note that this may fail if the two contexts have different
[formats](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format). Use
[isSharing](https://doc.qt.io/archives/qt-5.15/qglcontext.html#isSharing)() to see if
sharing is in effect.

**Warning:** Implementation note: initialization of C\\+\\+ class members usually takes
place in the class constructor.
[QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) is an exception because
it must be simple to customize. The virtual functions
[chooseContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html#chooseContext)() (and
chooseVisual() for X11) can be reimplemented in a subclass to select a particular
context. The problem is that virtual functions are not properly called during
construction (even though this is correct C\\+\\+) because C\\+\\+ constructs class
hierarchies from the bottom up. For this reason we need a create() function.

**See also**
[chooseContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html#chooseContext)(),
[format](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format)(), and
[isValid](https://doc.qt.io/archives/qt-5.15/qglcontext.html#isValid)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
create(self, shareContext: typing.Optional[PySide2.QtOpenGL.QGLContext]=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#create"""
        ...

    def currentContext(self) -> Any:
        """X.currentContext() -> PythonQt.QtOpenGL.QGLContext

Supplemental documentation:
Qt 5 reference:

### `[static]` const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext-obsolete.html#QGLContext) \\*QGLContext::currentContext()

Returns the current context, i.e. the context to which any OpenGL commands will
currently be directed. Returns 0 if no context is current.

**See also**
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglcontext.html#makeCurrent)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
currentContext() -> PySide2.QtOpenGL.QGLContext
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#currentContext"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteTexture(self, tx_id: int) -> None:
        """X.deleteTexture(tx_id)

Supplemental documentation:
Qt 5 reference:

### void QGLContext::deleteTexture(GLuint *id*)

Removes the texture identified by *id* from the texture cache, and calls
glDeleteTextures() to delete the texture from the context.

**See also**
[bindTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#bindTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
deleteTexture(self, tx_id: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#deleteTexture"""
        ...

    def device(self) -> Any:
        """X.device() -> PythonQt.QtGui.QPaintDevice

Supplemental documentation:
Qt 5 reference:

### [QPaintDevice](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html) \\*QGLContext::device() const

Returns the paint device set for this context.

**See also**
[QGLContext::QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext-obsolete.html#QGLContext)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
device(self) -> PySide2.QtGui.QPaintDevice
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#device"""
        ...

    def deviceIsPixmap(self) -> bool:
        """X.deviceIsPixmap() -> bool

Supplemental documentation:
Qt 5 reference:

### `[protected]` bool QGLContext::deviceIsPixmap() const

Returns `true` if the paint device of this context is a pixmap; otherwise returns
`false`.

Since Qt 5 the paint device is never actually a pixmap. renderPixmap() is however still
simulated using framebuffer objects and readbacks, and this function will return `true`
in this case.

Upstream PySide2 reference signatures (binding differences may apply):

```python
deviceIsPixmap(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#deviceIsPixmap"""
        ...

    def doneCurrent(self) -> None:
        """X.doneCurrent()

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QGLContext::doneCurrent()

Makes no GL context the current context. Normally, you do not need to call this
function; [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) calls it as
necessary.

Upstream PySide2 reference signatures (binding differences may apply):

```python
doneCurrent(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#doneCurrent"""
        ...

    def drawTexture(self, point: Any, textureId: int, textureTarget: int) -> None:
        """X.drawTexture(point, textureId, textureTarget)

Supplemental documentation:
Qt 5 reference:

### void QGLContext::drawTexture(const [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) \\&*target*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

This function supports the following use cases:

- On OpenGL and OpenGL ES 1.x it draws the given texture, *textureId*, to the given target rectangle, *target*, in OpenGL model space. The *textureTarget* should be a 2D texture target.
- On OpenGL and OpenGL ES 2.x, if a painter is active, not inside a beginNativePainting / endNativePainting block, and uses the engine with type [QPaintEngine::OpenGL2](https://doc.qt.io/archives/qt-5.15/qpaintengine.html#Type-enum), the function will draw the given texture, *textureId*, to the given target rectangle, *target*, respecting the current painter state. This will let you draw a texture with the clip, transform, render hints, and composition mode set by the painter. Note that the texture target needs to be GL\\_TEXTURE\\_2D for this use case, and that this is the only supported use case under OpenGL ES 2.x.

This function was introduced in Qt 4.4.

### void QGLContext::drawTexture(const [QPointF](https://doc.qt.io/archives/qt-5.15/qpointf.html) \\&*point*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

This function supports the following use cases:

- By default it draws the given texture, *textureId*, at the given *point* in OpenGL model space. The *textureTarget* should be a 2D texture target.
- If a painter is active, not inside a beginNativePainting / endNativePainting block, and uses the engine with type [QPaintEngine::OpenGL2](https://doc.qt.io/archives/qt-5.15/qpaintengine.html#Type-enum), the function will draw the given texture, *textureId*, at the given *point*, respecting the current painter state. This will let you draw a texture with the clip, transform, render hints, and composition mode set by the painter. Note that the texture target needs to be GL\\_TEXTURE\\_2D for this use case.

**Note:** This function is not supported under any version of OpenGL ES.

This function was introduced in Qt 4.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int=...) -> None
drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#drawTexture"""
        ...

    def format(self) -> Any:
        """X.format() -> PythonQt.QtOpenGL.QGLFormat

Supplemental documentation:
Qt 5 reference:

### [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) QGLContext::format() const

Returns the frame buffer format that was obtained (this may be a subset of what was
requested).

**See also** [setFormat](https://doc.qt.io/archives/qt-5.15/qglcontext.html#setFormat)()
and
[requestedFormat](https://doc.qt.io/archives/qt-5.15/qglcontext.html#requestedFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
format(self) -> PySide2.QtOpenGL.QGLFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#format"""
        ...

    def fromOpenGLContext(self, platformContext: Any) -> Any:
        """X.fromOpenGLContext(platformContext) -> PythonQt.QtOpenGL.QGLContext

Supplemental documentation:
Qt 5 reference:

### `[static]` [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext-obsolete.html#QGLContext) \\*QGLContext::fromOpenGLContext([QOpenGLContext](https://doc.qt.io/archives/qt-5.15/qopenglcontext.html) \\**context*)

Returns an OpenGL context for the window context specified by the *context* parameter.

Upstream PySide2 reference signatures (binding differences may apply):

```python
fromOpenGLContext(platformContext: PySide2.QtGui.QOpenGLContext) -> PySide2.QtOpenGL.QGLContext
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#fromOpenGLContext"""
        ...

    def functions(self) -> Any:
        """X.functions() -> PythonQt.QtOpenGL.QGLFunctions

Supplemental documentation:
Qt 5 reference:

### [QGLFunctions](https://doc.qt.io/archives/qt-5.15/qglfunctions.html) \\*QGLContext::functions() const

Returns a QGLFunctions object that is initialized for this context.

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#functions"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def initialized(self) -> bool:
        """X.initialized() -> bool

Supplemental documentation:
Qt 5 reference:

### `[protected]` bool QGLContext::initialized() const

Returns `true` if this context has been initialized, i.e. if
[QGLWidget::initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)()
has been performed on it; otherwise returns `false`.

**See also**
[setInitialized](https://doc.qt.io/archives/qt-5.15/qglcontext.html#setInitialized)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
initialized(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#initialized"""
        ...

    def isSharing(self) -> bool:
        """X.isSharing() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLContext::isSharing() const

Returns `true` if this context is sharing its GL context with another
[QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html), otherwise false is
returned. Note that context sharing might not be supported between contexts with
different formats.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSharing(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#isSharing"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLContext::isValid() const

Returns `true` if a GL rendering context has been successfully created; otherwise
returns `false`.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#isValid"""
        ...

    def makeCurrent(self) -> None:
        """X.makeCurrent()

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QGLContext::makeCurrent()

Makes this context the current OpenGL rendering context. All GL functions you call
operate on this context until another context is made current.

In some very rare cases the underlying call may fail. If this occurs an error message is
output to stderr.

If you call this from a thread other than the main UI thread, make sure you've first
pushed the context to the relevant thread from the UI thread using
[moveToThread](https://doc.qt.io/archives/qt-5.15/qglcontext.html#moveToThread)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
makeCurrent(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#makeCurrent"""
        ...

    def moveToThread(self, thread: Any) -> None:
        """X.moveToThread(thread)

Supplemental documentation:
Qt 5 reference:

### void QGLContext::moveToThread([QThread](https://doc.qt.io/archives/qt-5.15/qthread.html) \\**thread*)

Moves the [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) to the given
*thread*.

Enables calling
[swapBuffers](https://doc.qt.io/archives/qt-5.15/qglcontext.html#swapBuffers)() and
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglcontext.html#makeCurrent)() on the
context in the given thread.

Upstream PySide2 reference signatures (binding differences may apply):

```python
moveToThread(self, thread: PySide2.QtCore.QThread) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#moveToThread"""
        ...

    def overlayTransparentColor(self) -> Any:
        """X.overlayTransparentColor() -> PythonQt.QtGui.QColor

Supplemental documentation:
Qt 5 reference:

### [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) QGLContext::overlayTransparentColor() const

If this context is a valid context in an overlay plane, returns the plane's transparent
color. Otherwise returns an
[invalid](https://doc.qt.io/archives/qt-5.15/qcolor.html#isValid) color.

The returned color's [pixel](https://doc.qt.io/archives/qt-5.15/qcolormap.html#pixel)
value is the index of the transparent color in the colormap of the overlay plane.
(Naturally, the color's RGB values are meaningless.)

The returned [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) object will
generally work as expected only when passed as the argument to
[QGLWidget::qglColor](https://doc.qt.io/archives/qt-5.15/qglwidget.html#qglColor)() or
[QGLWidget::qglClearColor](https://doc.qt.io/archives/qt-5.15/qglwidget.html#qglClearColor)().
Under certain circumstances it can also be used to draw transparent graphics with a
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
overlayTransparentColor(self) -> PySide2.QtGui.QColor
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#overlayTransparentColor"""
        ...

    def requestedFormat(self) -> Any:
        """X.requestedFormat() -> PythonQt.QtOpenGL.QGLFormat

Supplemental documentation:
Qt 5 reference:

### [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) QGLContext::requestedFormat() const

Returns the frame buffer format that was originally requested in the constructor or
[setFormat](https://doc.qt.io/archives/qt-5.15/qglcontext.html#setFormat)().

**See also** [format](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
requestedFormat(self) -> PySide2.QtOpenGL.QGLFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#requestedFormat"""
        ...

    def reset(self) -> None:
        """X.reset()

Supplemental documentation:
Qt 5 reference:

### void QGLContext::reset()

Resets the context and makes it invalid.

**See also** [create](https://doc.qt.io/archives/qt-5.15/qglcontext.html#create)() and
[isValid](https://doc.qt.io/archives/qt-5.15/qglcontext.html#isValid)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
reset(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#reset"""
        ...

    def setFormat(self, format: Any) -> None:
        """X.setFormat(format)

Supplemental documentation:
Qt 5 reference:

### void QGLContext::setFormat(const [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) \\&*format*)

Sets a *format* for this context. The context is
[reset](https://doc.qt.io/archives/qt-5.15/qglcontext.html#reset).

Call [create](https://doc.qt.io/archives/qt-5.15/qglcontext.html#create)() to create a
new GL context that tries to match the new format.

```
QGLContext *cx;
//  ...
QGLFormat f;
f.setStereo(true);
cx->setFormat(f);
if (!cx->create())
    exit(); // no OpenGL support, or cannot render on the specified paintdevice
if (!cx->format().stereo())
    exit(); // could not create stereo context
```

**See also** [format](https://doc.qt.io/archives/qt-5.15/qglcontext.html#format)(),
[reset](https://doc.qt.io/archives/qt-5.15/qglcontext.html#reset)(), and
[create](https://doc.qt.io/archives/qt-5.15/qglcontext.html#create)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setFormat(self, format: PySide2.QtOpenGL.QGLFormat) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#setFormat"""
        ...

    def setInitialized(self, on: bool) -> None:
        """X.setInitialized(on)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QGLContext::setInitialized(bool *on*)

If *on* is true the context has been initialized, i.e. QGLContext::setInitialized() has
been called on it. If *on* is false the context has not been initialized.

**See also**
[initialized](https://doc.qt.io/archives/qt-5.15/qglcontext.html#initialized)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setInitialized(self, on: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#setInitialized"""
        ...

    def setTextureCacheLimit(self, size: int) -> None:
        """X.setTextureCacheLimit(size)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QGLContext::setTextureCacheLimit(int *size*)

This function sets the limit for the texture cache to *size*, expressed in kilobytes.

By default, the cache limit is approximately 64 MB.

**See also**
[textureCacheLimit](https://doc.qt.io/archives/qt-5.15/qglcontext.html#textureCacheLimit)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setTextureCacheLimit(size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#setTextureCacheLimit"""
        ...

    def setValid(self, valid: bool) -> None:
        """X.setValid(valid)

Upstream PySide2 reference signatures (binding differences may apply):

```python
setValid(self, valid: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#setValid"""
        ...

    def setWindowCreated(self, on: bool) -> None:
        """X.setWindowCreated(on)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QGLContext::setWindowCreated(bool *on*)

If *on* is true the context has had a window created for it. If *on* is false no window
has been created for the context.

**See also**
[windowCreated](https://doc.qt.io/archives/qt-5.15/qglcontext.html#windowCreated)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setWindowCreated(self, on: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#setWindowCreated"""
        ...

    def swapBuffers(self) -> None:
        """X.swapBuffers()

Supplemental documentation:
Qt 5 reference:

### `[virtual]` void QGLContext::swapBuffers() const

Call this to finish a frame of OpenGL rendering, and make sure to call
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglcontext.html#makeCurrent)() again
before issuing any further OpenGL commands, for example as part of a new frame.

Upstream PySide2 reference signatures (binding differences may apply):

```python
swapBuffers(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#swapBuffers"""
        ...

    def textureCacheLimit(self) -> int:
        """X.textureCacheLimit() -> int

Supplemental documentation:
Qt 5 reference:

### `[static]` int QGLContext::textureCacheLimit()

Returns the current texture cache limit in kilobytes.

**See also**
[setTextureCacheLimit](https://doc.qt.io/archives/qt-5.15/qglcontext.html#setTextureCacheLimit)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
textureCacheLimit() -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#textureCacheLimit"""
        ...

    def windowCreated(self) -> bool:
        """X.windowCreated() -> bool

Supplemental documentation:
Qt 5 reference:

### `[protected]` bool QGLContext::windowCreated() const

Returns `true` if a window has been created for this context; otherwise returns `false`.

**See also**
[setWindowCreated](https://doc.qt.io/archives/qt-5.15/qglcontext.html#setWindowCreated)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
windowCreated(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglcontext.html#windowCreated"""
        ...
    BindOption: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    BindOptions: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    CanFlipNativePixmapBindOption: Any
    DefaultBindOption: Any
    InternalBindOption: Any
    InvertedYBindOption: Any
    LinearFilteringBindOption: Any
    MemoryManagedBindOption: Any
    MipmapBindOption: Any
    NoBindOption: Any
    PremultipliedAlphaBindOption: Any
    TemporarilyCachedBindOption: Any

class QGLFormat:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

A display format has several characteristics:

- [Double or single buffering.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDoubleBuffer)
- [Depth buffer.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepth)
- [RGBA or color index mode.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRgba)
- [Alpha channel.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlpha)
- [Accumulation buffer.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccum)
- [Stencil buffer.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencil)
- [Stereo buffers.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStereo)
- [Direct rendering.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDirectRendering)
- [Presence of an overlay.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setOverlay)
- [Plane of an overlay.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setPlane)
- [Multisample buffers.](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSampleBuffers)

You can also specify preferred bit depths for the color buffer, depth buffer, alpha
buffer, accumulation buffer and the stencil buffer with the functions:
[setRedBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRedBufferSize)(),
[setGreenBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setGreenBufferSize)(),
[setBlueBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setBlueBufferSize)(),
[setDepthBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepthBufferSize)(),
[setAlphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize)(),
[setAccumBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccumBufferSize)()
and
[setStencilBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencilBufferSize)().

Note that even if you specify that you prefer a 32 bit depth buffer (e.g. with
[setDepthBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepthBufferSize)(32)),
the format that is chosen may not have a 32 bit depth buffer, even if there is a format
available with a 32 bit depth buffer. The main reason for this is how the system
dependant picking algorithms work on the different platforms, and some format options
may have higher precedence than others.

You create and tell a QGLFormat object what rendering options you want from an OpenGL
rendering context.

OpenGL drivers or accelerated hardware may or may not support advanced features such as
alpha channel or stereographic viewing. If you request some features that the
driver/hardware does not provide when you create a
[QGLWidget](https://doc.qt.io/archives/qt-5.15/qglwidget.html), you will get a rendering
context with the nearest subset of features.

There are different ways to define the display characteristics of a rendering context.
One is to create a QGLFormat and make it the default for the entire application:

```
QGLFormat fmt;
fmt.setAlpha(true);
fmt.setStereo(true);
QGLFormat::setDefaultFormat(fmt);
```

Or you can specify the desired format when creating an object of your
[QGLWidget](https://doc.qt.io/archives/qt-5.15/qglwidget.html) subclass:

```
QGLFormat fmt;
fmt.setDoubleBuffer(false);                 // single buffer
fmt.setDirectRendering(false);              // software rendering
MyGLWidget* myWidget = new MyGLWidget(fmt, ...);
```

After the widget has been created, you can find out which of the requested features the
system was able to provide:

```
QGLFormat fmt;
fmt.setOverlay(true);
fmt.setStereo(true);
MyGLWidget* myWidget = new MyGLWidget(fmt, ...);
if (!myWidget->format().stereo()) {
    // ok, goggles off
    if (!myWidget->format().hasOverlay()) {
        qFatal("Cool hardware required");
    }
}
```

OpenGL is a trademark of Silicon Graphics, Inc. in the United States and other
countries.

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def accum(self) -> bool:
        """X.accum() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::accum() const

Returns `true` if the accumulation buffer is enabled; otherwise returns `false`. The
accumulation buffer is disabled by default.

**See also** [setAccum](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccum)()
and
[setAccumBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccumBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
accum(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#accum"""
        ...

    def accumBufferSize(self) -> int:
        """X.accumBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::accumBufferSize() const

Returns the accumulation buffer size.

**See also**
[setAccumBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccumBufferSize)(),
[accum](https://doc.qt.io/archives/qt-5.15/qglformat.html#accum)(), and
[setAccum](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccum)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
accumBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#accumBufferSize"""
        ...

    def alpha(self) -> bool:
        """X.alpha() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::alpha() const

Returns `true` if the alpha buffer in the framebuffer is enabled; otherwise returns
`false`. The alpha buffer is disabled by default.

**See also** [setAlpha](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlpha)()
and
[setAlphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
alpha(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#alpha"""
        ...

    def alphaBufferSize(self) -> int:
        """X.alphaBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::alphaBufferSize() const

Returns the alpha buffer size.

**See also** [alpha](https://doc.qt.io/archives/qt-5.15/qglformat.html#alpha)(),
[setAlpha](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlpha)(), and
[setAlphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
alphaBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#alphaBufferSize"""
        ...

    def blueBufferSize(self) -> int:
        """X.blueBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::blueBufferSize() const

Returns the blue buffer size.

This function was introduced in Qt 4.2.

**See also**
[setBlueBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setBlueBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
blueBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#blueBufferSize"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def defaultFormat(self) -> Any:
        """X.defaultFormat() -> PythonQt.QtOpenGL.QGLFormat

Supplemental documentation:
Qt 5 reference:

### `[static]` [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#QGLFormat) QGLFormat::defaultFormat()

Returns the default [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) for
the application. All QGLWidget objects that are created use this format unless another
format is specified, e.g. when they are constructed.

If no special default format has been set using
[setDefaultFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDefaultFormat)(),
the default format is the same as that created with
[QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#QGLFormat)().

**See also**
[setDefaultFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDefaultFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
defaultFormat() -> PySide2.QtOpenGL.QGLFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#defaultFormat"""
        ...

    def defaultOverlayFormat(self) -> Any:
        """X.defaultOverlayFormat() -> PythonQt.QtOpenGL.QGLFormat

Supplemental documentation:
Qt 5 reference:

### `[static]` [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#QGLFormat) QGLFormat::defaultOverlayFormat()

Returns the default [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) for
overlay contexts.

The default overlay format is:

- [Double buffer:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDoubleBuffer) Disabled.
- [Depth buffer:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepth) Disabled.
- [RGBA:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRgba) Disabled (i.e., color index enabled).
- [Alpha channel:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlpha) Disabled.
- [Accumulator buffer:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccum) Disabled.
- [Stencil buffer:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencil) Disabled.
- [Stereo:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStereo) Disabled.
- [Direct rendering:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDirectRendering) Enabled.
- [Overlay:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setOverlay) Disabled.
- [Multisample buffers:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSampleBuffers) Disabled.
- [Plane:](https://doc.qt.io/archives/qt-5.15/qglformat.html#setPlane) 1 (i.e., first overlay plane).

**See also**
[setDefaultOverlayFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDefaultOverlayFormat)()
and
[setDefaultFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDefaultFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
defaultOverlayFormat() -> PySide2.QtOpenGL.QGLFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#defaultOverlayFormat"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def depth(self) -> bool:
        """X.depth() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::depth() const

Returns `true` if the depth buffer is enabled; otherwise returns false. The depth buffer
is enabled by default.

**See also** [setDepth](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepth)()
and
[setDepthBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepthBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
depth(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#depth"""
        ...

    def depthBufferSize(self) -> int:
        """X.depthBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::depthBufferSize() const

Returns the depth buffer size.

**See also** [depth](https://doc.qt.io/archives/qt-5.15/qglformat.html#depth)(),
[setDepth](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepth)(), and
[setDepthBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepthBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
depthBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#depthBufferSize"""
        ...

    def directRendering(self) -> bool:
        """X.directRendering() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::directRendering() const

Returns `true` if direct rendering is enabled; otherwise returns false.

Direct rendering is enabled by default.

**See also**
[setDirectRendering](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDirectRendering)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
directRendering(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#directRendering"""
        ...

    def doubleBuffer(self) -> bool:
        """X.doubleBuffer() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::doubleBuffer() const

Returns `true` if double buffering is enabled; otherwise returns false. Double buffering
is enabled by default.

**See also**
[setDoubleBuffer](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDoubleBuffer)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
doubleBuffer(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#doubleBuffer"""
        ...

    def fromSurfaceFormat(self, format: Any) -> Any:
        """X.fromSurfaceFormat(format) -> PythonQt.QtOpenGL.QGLFormat

Supplemental documentation:
Qt 5 reference:

### `[static]` [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#QGLFormat) QGLFormat::fromSurfaceFormat(const [QSurfaceFormat](https://doc.qt.io/archives/qt-5.15/qsurfaceformat.html) \\&*format*)

Returns an OpenGL format for the window format specified by *format*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
fromSurfaceFormat(format: PySide2.QtGui.QSurfaceFormat) -> PySide2.QtOpenGL.QGLFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#fromSurfaceFormat"""
        ...

    def greenBufferSize(self) -> int:
        """X.greenBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::greenBufferSize() const

Returns the green buffer size.

This function was introduced in Qt 4.2.

**See also**
[setGreenBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setGreenBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
greenBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#greenBufferSize"""
        ...

    def hasOpenGL(self) -> bool:
        """X.hasOpenGL() -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLFormat::hasOpenGL()

Returns `true` if the window system has any OpenGL support; otherwise returns `false`.

**Warning:** This function must not be called until the
[QApplication](https://doc.qt.io/archives/qt-5.15/qapplication.html) object has been
created.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOpenGL() -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOpenGL"""
        ...

    def hasOpenGLOverlays(self) -> bool:
        """X.hasOpenGLOverlays() -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLFormat::hasOpenGLOverlays()

Returns `true` if the window system supports OpenGL overlays; otherwise returns `false`.

**Warning:** This function must not be called until the
[QApplication](https://doc.qt.io/archives/qt-5.15/qapplication.html) object has been
created.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOpenGLOverlays() -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOpenGLOverlays"""
        ...

    def hasOverlay(self) -> bool:
        """X.hasOverlay() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::hasOverlay() const

Returns `true` if overlay plane is enabled; otherwise returns `false`.

Overlay is disabled by default.

**See also**
[setOverlay](https://doc.qt.io/archives/qt-5.15/qglformat.html#setOverlay)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOverlay(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOverlay"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def majorVersion(self) -> int:
        """X.majorVersion() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::majorVersion() const

Returns the OpenGL major version.

This function was introduced in Qt 4.7.

**See also**
[setVersion](https://doc.qt.io/archives/qt-5.15/qglformat.html#setVersion)() and
[minorVersion](https://doc.qt.io/archives/qt-5.15/qglformat.html#minorVersion)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
majorVersion(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#majorVersion"""
        ...

    def minorVersion(self) -> int:
        """X.minorVersion() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::minorVersion() const

Returns the OpenGL minor version.

This function was introduced in Qt 4.7.

**See also**
[setVersion](https://doc.qt.io/archives/qt-5.15/qglformat.html#setVersion)() and
[majorVersion](https://doc.qt.io/archives/qt-5.15/qglformat.html#majorVersion)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
minorVersion(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#minorVersion"""
        ...

    def openGLVersionFlags(self) -> Any:
        """X.openGLVersionFlags()

Supplemental documentation:
Qt 5 reference:

### `[static]` [QGLFormat::OpenGLVersionFlags](https://doc.qt.io/archives/qt-5.15/qglformat.html#OpenGLVersionFlag-enum) QGLFormat::openGLVersionFlags()

Identifies, at runtime, which OpenGL versions that are supported by the current
platform.

Note that if OpenGL version 1.5 is supported, its predecessors (i.e., version 1.4 and
lower) are also supported. To identify the support of a particular feature, like multi
texturing, test for the version in which the feature was first introduced (i.e., version
1.3 in the case of multi texturing) to adapt to the largest possible group of runtime
platforms.

This function needs a valid current OpenGL context to work; otherwise it will return
[OpenGL\\_Version\\_None](https://doc.qt.io/archives/qt-5.15/qglformat.html#OpenGLVersionFlag-enum).

This function was introduced in Qt 4.2.

**See also** [hasOpenGL](https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOpenGL)()
and
[hasOpenGLOverlays](https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOpenGLOverlays)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
openGLVersionFlags() -> PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlags
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#openGLVersionFlags"""
        ...

    def plane(self) -> int:
        """X.plane() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::plane() const

Returns the plane of this format. The default for normal formats is 0, which means the
normal plane. The default for overlay formats is 1, which is the first overlay plane.

**See also** [setPlane](https://doc.qt.io/archives/qt-5.15/qglformat.html#setPlane)()
and
[defaultOverlayFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#defaultOverlayFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
plane(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#plane"""
        ...

    def profile(self) -> Any:
        """X.profile()

Supplemental documentation:
Qt 5 reference:

### [QGLFormat::OpenGLContextProfile](https://doc.qt.io/archives/qt-5.15/qglformat.html#OpenGLContextProfile-enum) QGLFormat::profile() const

Returns the OpenGL context profile.

This function was introduced in Qt 4.7.

**See also**
[setProfile](https://doc.qt.io/archives/qt-5.15/qglformat.html#setProfile)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
profile(self) -> PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#profile"""
        ...

    def redBufferSize(self) -> int:
        """X.redBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::redBufferSize() const

Returns the red buffer size.

This function was introduced in Qt 4.2.

**See also**
[setRedBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRedBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
redBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#redBufferSize"""
        ...

    def rgba(self) -> bool:
        """X.rgba() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::rgba() const

Returns `true` if RGBA color mode is set. Returns `false` if color index mode is set.
The default color mode is RGBA.

**See also** [setRgba](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRgba)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
rgba(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#rgba"""
        ...

    def sampleBuffers(self) -> bool:
        """X.sampleBuffers() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::sampleBuffers() const

Returns `true` if multisample buffer support is enabled; otherwise returns `false`.

The multisample buffer is disabled by default.

**See also**
[setSampleBuffers](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSampleBuffers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sampleBuffers(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#sampleBuffers"""
        ...

    def samples(self) -> int:
        """X.samples() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::samples() const

Returns the number of samples per pixel when multisampling is enabled. By default, the
highest number of samples that is available is used.

**See also**
[setSampleBuffers](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSampleBuffers)(),
[sampleBuffers](https://doc.qt.io/archives/qt-5.15/qglformat.html#sampleBuffers)(), and
[setSamples](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSamples)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
samples(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#samples"""
        ...

    def setAccum(self, enable: bool) -> None:
        """X.setAccum(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setAccum(bool *enable*)

If *enable* is true enables the accumulation buffer; otherwise disables the accumulation
buffer.

The accumulation buffer is disabled by default.

The accumulation buffer is used to create blur effects and multiple exposures.

**See also** [accum](https://doc.qt.io/archives/qt-5.15/qglformat.html#accum)() and
[setAccumBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccumBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAccum(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccum"""
        ...

    def setAccumBufferSize(self, size: int) -> None:
        """X.setAccumBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setAccumBufferSize(int *size*)

Set the preferred accumulation buffer size, where *size* is the bit depth for each RGBA
component.

**See also** [accum](https://doc.qt.io/archives/qt-5.15/qglformat.html#accum)(),
[setAccum](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccum)(), and
[accumBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#accumBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAccumBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setAccumBufferSize"""
        ...

    def setAlpha(self, enable: bool) -> None:
        """X.setAlpha(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setAlpha(bool *enable*)

If *enable* is true enables the alpha buffer; otherwise disables the alpha buffer.

The alpha buffer is disabled by default.

The alpha buffer is typically used for implementing transparency or translucency. The A
in RGBA specifies the transparency of a pixel.

**See also** [alpha](https://doc.qt.io/archives/qt-5.15/qglformat.html#alpha)() and
[setAlphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAlpha(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlpha"""
        ...

    def setAlphaBufferSize(self, size: int) -> None:
        """X.setAlphaBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setAlphaBufferSize(int *size*)

Set the preferred alpha buffer size to *size*. This function implicitly enables the
alpha channel.

**See also**
[setRedBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRedBufferSize)(),
[setGreenBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setGreenBufferSize)(),
and
[alphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#alphaBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAlphaBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize"""
        ...

    def setBlueBufferSize(self, size: int) -> None:
        """X.setBlueBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setBlueBufferSize(int *size*)

Set the preferred blue buffer size to *size*.

This function was introduced in Qt 4.2.

**See also**
[blueBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#blueBufferSize)(),
[setRedBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRedBufferSize)(),
[setGreenBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setGreenBufferSize)(),
and
[setAlphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setBlueBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setBlueBufferSize"""
        ...

    def setDefaultFormat(self, f: Any) -> None:
        """X.setDefaultFormat(f)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QGLFormat::setDefaultFormat(const [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#QGLFormat) \\&*f*)

Sets a new default [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) for
the application to *f*. For example, to set single buffering as the default instead of
double buffering, your main() might contain code like this:

```
QApplication a(argc, argv);
QGLFormat f;
f.setDoubleBuffer(false);
QGLFormat::setDefaultFormat(f);
```

**See also**
[defaultFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#defaultFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDefaultFormat(f: PySide2.QtOpenGL.QGLFormat) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setDefaultFormat"""
        ...

    def setDefaultOverlayFormat(self, f: Any) -> None:
        """X.setDefaultOverlayFormat(f)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QGLFormat::setDefaultOverlayFormat(const [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#QGLFormat) \\&*f*)

Sets a new default [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) for
overlay contexts to *f*. This format is used whenever a QGLWidget is created with a
format that [hasOverlay](https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOverlay)()
enabled.

For example, to get a double buffered overlay context (if available), use code like
this:

```
QGLFormat f = QGLFormat::defaultOverlayFormat();
f.setDoubleBuffer(true);
QGLFormat::setDefaultOverlayFormat(f);
```

As usual, you can find out after widget creation whether the underlying OpenGL system
was able to provide the requested specification:

```
// ...continued from above
MyGLWidget* myWidget = new MyGLWidget(QGLFormat(QGL::HasOverlay), ...);
if (myWidget->format().hasOverlay()) {
    // Yes, we got an overlay, let's check _its_ format:
    QGLContext* olContext = myWidget->overlayContext();
    if (olContext->format().doubleBuffer())
        ; // yes, we got a double buffered overlay
    else
        ; // no, only single buffered overlays are available
}
```

**See also**
[defaultOverlayFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#defaultOverlayFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDefaultOverlayFormat(f: PySide2.QtOpenGL.QGLFormat) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setDefaultOverlayFormat"""
        ...

    def setDepth(self, enable: bool) -> None:
        """X.setDepth(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setDepth(bool *enable*)

If *enable* is true enables the depth buffer; otherwise disables the depth buffer.

The depth buffer is enabled by default.

The purpose of a depth buffer (or Z-buffering) is to remove hidden surfaces. Pixels are
assigned Z values based on the distance to the viewer. A pixel with a high Z value is
closer to the viewer than a pixel with a low Z value. This information is used to decide
whether to draw a pixel or not.

**See also** [depth](https://doc.qt.io/archives/qt-5.15/qglformat.html#depth)() and
[setDepthBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepthBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDepth(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepth"""
        ...

    def setDepthBufferSize(self, size: int) -> None:
        """X.setDepthBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setDepthBufferSize(int *size*)

Set the minimum depth buffer size to *size*.

**See also**
[depthBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#depthBufferSize)(),
[setDepth](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepth)(), and
[depth](https://doc.qt.io/archives/qt-5.15/qglformat.html#depth)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDepthBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setDepthBufferSize"""
        ...

    def setDirectRendering(self, enable: bool) -> None:
        """X.setDirectRendering(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setDirectRendering(bool *enable*)

If *enable* is true enables direct rendering; otherwise disables direct rendering.

Direct rendering is enabled by default.

Enabling this option will make OpenGL bypass the underlying window system and render
directly from hardware to the screen, if this is supported by the system.

**See also**
[directRendering](https://doc.qt.io/archives/qt-5.15/qglformat.html#directRendering)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDirectRendering(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setDirectRendering"""
        ...

    def setDoubleBuffer(self, enable: bool) -> None:
        """X.setDoubleBuffer(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setDoubleBuffer(bool *enable*)

If *enable* is true sets double buffering; otherwise sets single buffering.

Double buffering is enabled by default.

Double buffering is a technique where graphics are rendered on an off-screen buffer and
not directly to the screen. When the drawing has been completed, the program calls a
swapBuffers() function to exchange the screen contents with the buffer. The result is
flicker-free drawing and often better performance.

Note that single buffered contexts are currently not supported with EGL.

**See also**
[doubleBuffer](https://doc.qt.io/archives/qt-5.15/qglformat.html#doubleBuffer)(),
[QGLContext::swapBuffers](https://doc.qt.io/archives/qt-5.15/qglcontext.html#swapBuffers)(),
and
[QGLWidget::swapBuffers](https://doc.qt.io/archives/qt-5.15/qglwidget.html#swapBuffers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setDoubleBuffer(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setDoubleBuffer"""
        ...

    def setGreenBufferSize(self, size: int) -> None:
        """X.setGreenBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setGreenBufferSize(int *size*)

Set the preferred green buffer size to *size*.

This function was introduced in Qt 4.2.

**See also**
[greenBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#greenBufferSize)(),
[setRedBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setRedBufferSize)(),
[setBlueBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setBlueBufferSize)(),
and
[setAlphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setGreenBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setGreenBufferSize"""
        ...

    def setOption(self, opt: Any) -> None:
        """X.setOption(opt)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setOption([QGL::FormatOptions](https://doc.qt.io/archives/qt-5.15/qgl.html#FormatOption-enum) *opt*)

Sets the format option to *opt*.

**See also**
[testOption](https://doc.qt.io/archives/qt-5.15/qglformat.html#testOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setOption(self, opt: PySide2.QtOpenGL.QGL.FormatOptions) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setOption"""
        ...

    def setOverlay(self, enable: bool) -> None:
        """X.setOverlay(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setOverlay(bool *enable*)

If *enable* is true enables an overlay plane; otherwise disables the overlay plane.

Enabling the overlay plane will cause QGLWidget to create an additional context in an
overlay plane. See the QGLWidget documentation for further information.

**See also**
[hasOverlay](https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOverlay)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setOverlay(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setOverlay"""
        ...

    def setPlane(self, plane: int) -> None:
        """X.setPlane(plane)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setPlane(int *plane*)

Sets the requested plane to *plane*. 0 is the normal plane, 1 is the first overlay
plane, 2 is the second overlay plane, etc.; -1, -2, etc. are underlay planes.

Note that in contrast to other format specifications, the plane specifications will be
matched exactly. This means that if you specify a plane that the underlying OpenGL
system cannot provide, an
[invalid](https://doc.qt.io/archives/qt-5.15/qglwidget.html#isValid) QGLWidget will be
created.

**See also** [plane](https://doc.qt.io/archives/qt-5.15/qglformat.html#plane)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setPlane(self, plane: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setPlane"""
        ...

    def setProfile(self, profile: Any) -> None:
        """X.setProfile(profile)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setProfile([QGLFormat::OpenGLContextProfile](https://doc.qt.io/archives/qt-5.15/qglformat.html#OpenGLContextProfile-enum) *profile*)

Set the OpenGL context profile to *profile*. The *profile* is ignored if the requested
OpenGL version is less than 3.2.

This function was introduced in Qt 4.7.

**See also** [profile](https://doc.qt.io/archives/qt-5.15/qglformat.html#profile)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setProfile(self, profile: PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setProfile"""
        ...

    def setRedBufferSize(self, size: int) -> None:
        """X.setRedBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setRedBufferSize(int *size*)

Set the preferred red buffer size to *size*.

This function was introduced in Qt 4.2.

**See also**
[redBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#redBufferSize)(),
[setGreenBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setGreenBufferSize)(),
[setBlueBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setBlueBufferSize)(),
and
[setAlphaBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setAlphaBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRedBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setRedBufferSize"""
        ...

    def setRgba(self, enable: bool) -> None:
        """X.setRgba(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setRgba(bool *enable*)

If *enable* is true sets RGBA mode. If *enable* is false sets color index mode.

The default color mode is RGBA.

RGBA is the preferred mode for most OpenGL applications. In RGBA color mode you specify
colors as red \\+ green \\+ blue \\+ alpha quadruplets.

In color index mode you specify an index into a color lookup table.

**See also** [rgba](https://doc.qt.io/archives/qt-5.15/qglformat.html#rgba)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setRgba(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setRgba"""
        ...

    def setSampleBuffers(self, enable: bool) -> None:
        """X.setSampleBuffers(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setSampleBuffers(bool *enable*)

If *enable* is true, a GL context with multisample buffer support is picked; otherwise
ignored.

**See also**
[sampleBuffers](https://doc.qt.io/archives/qt-5.15/qglformat.html#sampleBuffers)(),
[setSamples](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSamples)(), and
[samples](https://doc.qt.io/archives/qt-5.15/qglformat.html#samples)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSampleBuffers(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setSampleBuffers"""
        ...

    def setSamples(self, numSamples: int) -> None:
        """X.setSamples(numSamples)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setSamples(int *numSamples*)

Set the preferred number of samples per pixel when multisampling is enabled to
*numSamples*. By default, the highest number of samples available is used.

**See also**
[setSampleBuffers](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSampleBuffers)(),
[sampleBuffers](https://doc.qt.io/archives/qt-5.15/qglformat.html#sampleBuffers)(), and
[samples](https://doc.qt.io/archives/qt-5.15/qglformat.html#samples)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSamples(self, numSamples: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setSamples"""
        ...

    def setStencil(self, enable: bool) -> None:
        """X.setStencil(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setStencil(bool *enable*)

If *enable* is true enables the stencil buffer; otherwise disables the stencil buffer.

The stencil buffer is enabled by default.

The stencil buffer masks certain parts of the drawing area so that masked parts are not
drawn on.

**See also** [stencil](https://doc.qt.io/archives/qt-5.15/qglformat.html#stencil)() and
[setStencilBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencilBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setStencil(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencil"""
        ...

    def setStencilBufferSize(self, size: int) -> None:
        """X.setStencilBufferSize(size)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setStencilBufferSize(int *size*)

Set the preferred stencil buffer size to *size*.

**See also**
[stencilBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#stencilBufferSize)(),
[setStencil](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencil)(), and
[stencil](https://doc.qt.io/archives/qt-5.15/qglformat.html#stencil)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setStencilBufferSize(self, size: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencilBufferSize"""
        ...

    def setStereo(self, enable: bool) -> None:
        """X.setStereo(enable)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setStereo(bool *enable*)

If *enable* is true enables stereo buffering; otherwise disables stereo buffering.

Stereo buffering is disabled by default.

Stereo buffering provides extra color buffers to generate left-eye and right-eye images.

**See also** [stereo](https://doc.qt.io/archives/qt-5.15/qglformat.html#stereo)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setStereo(self, enable: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setStereo"""
        ...

    def setSwapInterval(self, interval: int) -> None:
        """X.setSwapInterval(interval)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setSwapInterval(int *interval*)

Set the preferred swap interval. This can be used to sync the GL drawing into a system
window to the vertical refresh of the screen. Setting an *interval* value of 0 will turn
the vertical refresh syncing off, any value higher than 0 will turn the vertical syncing
on.

Under Windows and under X11, where the `WGL_EXT_swap_control` and `GLX_SGI_video_sync`
extensions are used, the *interval* parameter can be used to set the minimum number of
video frames that are displayed before a buffer swap will occur. In effect, setting the
*interval* to 10, means there will be 10 vertical retraces between every buffer swap.

Under Windows the `WGL_EXT_swap_control` extension has to be present, and under X11 the
`GLX_SGI_video_sync` extension has to be present.

This function was introduced in Qt 4.2.

**See also**
[swapInterval](https://doc.qt.io/archives/qt-5.15/qglformat.html#swapInterval)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSwapInterval(self, interval: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setSwapInterval"""
        ...

    def setVersion(self, major: int, minor: int) -> None:
        """X.setVersion(major, minor)

Supplemental documentation:
Qt 5 reference:

### void QGLFormat::setVersion(int *major*, int *minor*)

Set the OpenGL version to the *major* and *minor* numbers. If a context compatible with
the requested OpenGL version cannot be created, a context compatible with version 1.x is
created instead.

This function was introduced in Qt 4.7.

**See also**
[majorVersion](https://doc.qt.io/archives/qt-5.15/qglformat.html#majorVersion)() and
[minorVersion](https://doc.qt.io/archives/qt-5.15/qglformat.html#minorVersion)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setVersion(self, major: int, minor: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#setVersion"""
        ...

    def stencil(self) -> bool:
        """X.stencil() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::stencil() const

Returns `true` if the stencil buffer is enabled; otherwise returns false. The stencil
buffer is enabled by default.

**See also**
[setStencil](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencil)() and
[setStencilBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencilBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
stencil(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#stencil"""
        ...

    def stencilBufferSize(self) -> int:
        """X.stencilBufferSize() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::stencilBufferSize() const

Returns the stencil buffer size.

**See also** [stencil](https://doc.qt.io/archives/qt-5.15/qglformat.html#stencil)(),
[setStencil](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencil)(), and
[setStencilBufferSize](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStencilBufferSize)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
stencilBufferSize(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#stencilBufferSize"""
        ...

    def stereo(self) -> bool:
        """X.stereo() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::stereo() const

Returns `true` if stereo buffering is enabled; otherwise returns false. Stereo buffering
is disabled by default.

**See also** [setStereo](https://doc.qt.io/archives/qt-5.15/qglformat.html#setStereo)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
stereo(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#stereo"""
        ...

    def swapInterval(self) -> int:
        """X.swapInterval() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFormat::swapInterval() const

Returns the currently set swap interval. -1 is returned if setting the swap interval
isn't supported in the system GL implementation.

This function was introduced in Qt 4.2.

**See also**
[setSwapInterval](https://doc.qt.io/archives/qt-5.15/qglformat.html#setSwapInterval)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
swapInterval(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#swapInterval"""
        ...

    def testOption(self, opt: Any) -> bool:
        """X.testOption(opt) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFormat::testOption([QGL::FormatOptions](https://doc.qt.io/archives/qt-5.15/qgl.html#FormatOption-enum) *opt*) const

Returns `true` if format option *opt* is set; otherwise returns `false`.

**See also** [setOption](https://doc.qt.io/archives/qt-5.15/qglformat.html#setOption)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
testOption(self, opt: PySide2.QtOpenGL.QGL.FormatOptions) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#testOption"""
        ...

    def toSurfaceFormat(self, format: Any) -> Any:
        """X.toSurfaceFormat(format) -> PythonQt.QtGui.QSurfaceFormat

Supplemental documentation:
Qt 5 reference:

### `[static]` [QSurfaceFormat](https://doc.qt.io/archives/qt-5.15/qsurfaceformat.html) QGLFormat::toSurfaceFormat(const [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html#QGLFormat) \\&*format*)

Returns a window format for the OpenGL format specified by *format*.

Upstream PySide2 reference signatures (binding differences may apply):

```python
toSurfaceFormat(format: PySide2.QtOpenGL.QGLFormat) -> PySide2.QtGui.QSurfaceFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglformat.html#toSurfaceFormat"""
        ...
    CompatibilityProfile: Any
    CoreProfile: Any
    NoProfile: Any
    OpenGLContextProfile: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenGLVersionFlag: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenGLVersionFlags: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenGL_ES_CommonLite_Version_1_0: Any
    OpenGL_ES_CommonLite_Version_1_1: Any
    OpenGL_ES_Common_Version_1_0: Any
    OpenGL_ES_Common_Version_1_1: Any
    OpenGL_ES_Version_2_0: Any
    OpenGL_Version_1_1: Any
    OpenGL_Version_1_2: Any
    OpenGL_Version_1_3: Any
    OpenGL_Version_1_4: Any
    OpenGL_Version_1_5: Any
    OpenGL_Version_2_0: Any
    OpenGL_Version_2_1: Any
    OpenGL_Version_3_0: Any
    OpenGL_Version_3_1: Any
    OpenGL_Version_3_2: Any
    OpenGL_Version_3_3: Any
    OpenGL_Version_4_0: Any
    OpenGL_Version_4_1: Any
    OpenGL_Version_4_2: Any
    OpenGL_Version_4_3: Any
    OpenGL_Version_None: Any

class QGLFramebufferObject:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

The QGLFramebufferObject class encapsulates an OpenGL framebuffer object, defined by the
`GL_EXT_framebuffer_object` extension. In addition it provides a rendering surface that
can be painted on with a [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html),
rendered to using native GL calls, or both. This surface can be bound and used as a
regular texture in your own GL drawing code. By default, the QGLFramebufferObject class
generates a 2D GL texture (using the `GL_TEXTURE_2D` target), which is used as the
internal rendering target.

**It is important to have a current GL context when creating a QGLFramebufferObject,
otherwise initialization will fail.**

OpenGL framebuffer objects and pbuffers (see
[QGLPixelBuffer](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html)) can both be
used to render to offscreen surfaces, but there are a number of advantages with using
framebuffer objects instead of pbuffers:

1. A framebuffer object does not require a separate rendering context, so no context switching will occur when switching rendering targets. There is an overhead involved in switching targets, but in general it is cheaper than a context switch to a pbuffer.
2. Rendering to dynamic textures (i.e. render-to-texture functionality) works on all platforms. No need to do explicit copy calls from a render buffer into a texture, as was necessary on systems that did not support the `render_texture` extension.
3. It is possible to attach several rendering buffers (or texture objects) to the same framebuffer object, and render to all of them without doing a context switch.
4. The OpenGL framebuffer extension is a pure GL extension with no system dependant WGL, CGL, or GLX parts. This makes using framebuffer objects more portable.

When using a [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) to paint to a
QGLFramebufferObject you should take care that the QGLFramebufferObject is created with
the
[CombinedDepthStencil](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#Attachment-enum)
attachment for [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) to be able
to render correctly. Note that you need to create a QGLFramebufferObject with more than
one sample per pixel for primitives to be antialiased when drawing using a
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html). To create a multisample
framebuffer object you should use one of the constructors that take a
[QGLFramebufferObjectFormat](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html)
parameter, and set the
[QGLFramebufferObjectFormat::samples](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#samples)()
property to a non-zero value.

When painting to a QGLFramebufferObject using
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html), the state of the current
GL context will be altered by the paint engine to reflect its needs. Applications should
not rely upon the GL state being reset to its original conditions, particularly the
current shader program, GL viewport, texture units, and drawing modes.

For multisample framebuffer objects a color render buffer is created, otherwise a
texture with the specified texture target is created. The color render buffer or texture
will have the specified internal format, and will be bound to the `GL_COLOR_ATTACHMENT0`
attachment in the framebuffer object.

If you want to use a framebuffer object with multisampling enabled as a texture, you
first need to copy from it to a regular framebuffer object using
QGLContext::blitFramebuffer().

### Threading

As of Qt 4.8, it's possible to draw into a QGLFramebufferObject using a
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) in a separate thread. Note
that OpenGL 2.0 or OpenGL ES 2.0 is required for this to work.

**Note:** This class has been deprecated in favor of
[QOpenGLFramebufferObject](https://doc.qt.io/archives/qt-5.15/qopenglframebufferobject.html).

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def attachment(self) -> Any:
        """X.attachment()

Supplemental documentation:
Qt 5 reference:

### [QGLFramebufferObject::Attachment](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#Attachment-enum) QGLFramebufferObject::attachment() const

Returns the status of the depth and stencil buffers attached to this framebuffer object.

Upstream PySide2 reference signatures (binding differences may apply):

```python
attachment(self) -> PySide2.QtOpenGL.QGLFramebufferObject.Attachment
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#attachment"""
        ...

    def bind(self) -> bool:
        """X.bind() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFramebufferObject::bind()

Switches rendering from the default, windowing system provided framebuffer to this
framebuffer object. Returns `true` upon success, false otherwise.

**See also**
[release](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#release)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bind(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#bind"""
        ...

    def bindDefault(self) -> bool:
        """X.bindDefault() -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLFramebufferObject::bindDefault()

Switches rendering back to the default, windowing system provided framebuffer. Returns
`true` upon success, false otherwise.

**See also** [bind](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#bind)()
and [release](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#release)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bindDefault() -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#bindDefault"""
        ...

    def blitFramebuffer(self, target: Any, targetRect: Any, source: Any, sourceRect: Any, buffers: int, filter: int) -> None:
        """X.blitFramebuffer(target, targetRect, source, sourceRect, buffers, filter)

Supplemental documentation:
Qt 5 reference:

### `[static]` void QGLFramebufferObject::blitFramebuffer([QGLFramebufferObject](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#QGLFramebufferObject) \\**target*, const [QRect](https://doc.qt.io/archives/qt-5.15/qrect.html) \\&*targetRect*, [QGLFramebufferObject](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#QGLFramebufferObject) \\**source*, const [QRect](https://doc.qt.io/archives/qt-5.15/qrect.html) \\&*sourceRect*, GLbitfield *buffers* \\= GL\\_COLOR\\_BUFFER\\_BIT, GLenum *filter* \\= GL\\_NEAREST)

Blits from the *sourceRect* rectangle in the *source* framebuffer object to the
*targetRect* rectangle in the *target* framebuffer object.

If *source* or *target* is `nullptr`, the default framebuffer will be used instead of a
framebuffer object as source or target respectively.

The *buffers* parameter should be a mask consisting of any combination of
`GL_COLOR_BUFFER_BIT`, `GL_DEPTH_BUFFER_BIT`, and `GL_STENCIL_BUFFER_BIT`. Any buffer
type that is not present both in the source and target buffers is ignored.

The *sourceRect* and *targetRect* rectangles may have different sizes; in this case
*buffers* should not contain `GL_DEPTH_BUFFER_BIT` or `GL_STENCIL_BUFFER_BIT`. The
*filter* parameter should be set to `GL_LINEAR` or `GL_NEAREST`, and specifies whether
linear or nearest interpolation should be used when scaling is performed.

If *source* equals *target* a copy is performed within the same buffer. Results are
undefined if the source and target rectangles overlap and have different sizes. The
sizes must also be the same if any of the framebuffer objects are multisample
framebuffers.

Note that the scissor test will restrict the blit area if enabled.

This function will have no effect unless
[hasOpenGLFramebufferBlit](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#hasOpenGLFramebufferBlit)()
returns true.

This function was introduced in Qt 4.6.

**See also**
[hasOpenGLFramebufferBlit](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#hasOpenGLFramebufferBlit)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
blitFramebuffer(target: PySide2.QtOpenGL.QGLFramebufferObject, targetRect: PySide2.QtCore.QRect, source: PySide2.QtOpenGL.QGLFramebufferObject, sourceRect: PySide2.QtCore.QRect, buffers: int=..., filter: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#blitFramebuffer"""
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

    def devType(self) -> int:
        """X.devType() -> int

Upstream PySide2 reference signatures (binding differences may apply):

```python
devType(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#devType"""
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

    def drawTexture(self, point: Any, textureId: int, textureTarget: int) -> None:
        """X.drawTexture(point, textureId, textureTarget)

Supplemental documentation:
Qt 5 reference:

### void QGLFramebufferObject::drawTexture(const [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) \\&*target*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

Draws the given texture, *textureId*, to the given target rectangle, *target*, in OpenGL
model space. The *textureTarget* should be a 2D texture target.

The framebuffer object should be bound when calling this function.

Equivalent to the corresponding
[QGLContext::drawTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#drawTexture)().

This function was introduced in Qt 4.4.

### void QGLFramebufferObject::drawTexture(const [QPointF](https://doc.qt.io/archives/qt-5.15/qpointf.html) \\&*point*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

Draws the given texture, *textureId*, at the given *point* in OpenGL model space. The
*textureTarget* should be a 2D texture target.

The framebuffer object should be bound when calling this function.

Equivalent to the corresponding
[QGLContext::drawTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#drawTexture)().

This function was introduced in Qt 4.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int=...) -> None
drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#drawTexture"""
        ...

    def format(self) -> Any:
        """X.format() -> PythonQt.QtOpenGL.QGLFramebufferObjectFormat

Supplemental documentation:
Qt 5 reference:

### [QGLFramebufferObjectFormat](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html) QGLFramebufferObject::format() const

Returns the format of this framebuffer object.

Upstream PySide2 reference signatures (binding differences may apply):

```python
format(self) -> PySide2.QtOpenGL.QGLFramebufferObjectFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#format"""
        ...

    def handle(self) -> int:
        """X.handle() -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLFramebufferObject::handle() const

Returns the GL framebuffer object handle for this framebuffer object (returned by the
`glGenFrameBuffersEXT()` function). This handle can be used to attach new images or
buffers to the framebuffer. The user is responsible for cleaning up and destroying these
objects.

Upstream PySide2 reference signatures (binding differences may apply):

```python
handle(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#handle"""
        ...

    def hasOpenGLFramebufferBlit(self) -> bool:
        """X.hasOpenGLFramebufferBlit() -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLFramebufferObject::hasOpenGLFramebufferBlit()

Returns `true` if the OpenGL `GL_EXT_framebuffer_blit` extension is present on this
system; otherwise returns `false`.

This function was introduced in Qt 4.6.

**See also**
[blitFramebuffer](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#blitFramebuffer)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOpenGLFramebufferBlit() -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#hasOpenGLFramebufferBlit"""
        ...

    def hasOpenGLFramebufferObjects(self) -> bool:
        """X.hasOpenGLFramebufferObjects() -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLFramebufferObject::hasOpenGLFramebufferObjects()

Returns `true` if the OpenGL `GL_EXT_framebuffer_object` extension is present on this
system; otherwise returns `false`.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOpenGLFramebufferObjects() -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#hasOpenGLFramebufferObjects"""
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

    def isBound(self) -> bool:
        """X.isBound() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFramebufferObject::isBound() const

Returns `true` if the framebuffer object is currently bound to a context, otherwise
false is returned.

This function was introduced in Qt 4.5.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isBound(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#isBound"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFramebufferObject::isValid() const

Returns `true` if the framebuffer object is valid.

The framebuffer can become invalid if the initialization process fails, the user
attaches an invalid buffer to the framebuffer object, or a non-power of two width/height
is specified as the texture size if the texture target is `GL_TEXTURE_2D`. The non-power
of two limitation does not apply if the OpenGL version is 2.0 or higher, or if the
GL\\_ARB\\_texture\\_non\\_power\\_of\\_two extension is present.

The framebuffer can also become invalid if the QGLContext that the framebuffer was
created within is destroyed and there are no other shared contexts that can take over
ownership of the framebuffer.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#isValid"""
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

### `[override virtual protected]` int QGLFramebufferObject::metric([QPaintDevice::PaintDeviceMetric](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#PaintDeviceMetric-enum) *metric*) const

Reimplements:
[QPaintDevice::metric](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#metric)(QPaintDevice::PaintDeviceMetric
metric) const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#metric"""
        ...

    def paintEngine(self) -> Any:
        """X.paintEngine() -> PythonQt.QtGui.QPaintEngine

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QPaintEngine](https://doc.qt.io/archives/qt-5.15/qpaintengine.html) \\*QGLFramebufferObject::paintEngine() const

Reimplements:
[QPaintDevice::paintEngine](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#paintEngine)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintEngine(self) -> PySide2.QtGui.QPaintEngine
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#paintEngine"""
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

    def release(self) -> bool:
        """X.release() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFramebufferObject::release()

Switches rendering back to the default, windowing system provided framebuffer. Returns
`true` upon success, false otherwise.

**See also**
[bind](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#bind)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
release(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#release"""
        ...

    def sharedPainter(self) -> Any:
        """X.sharedPainter() -> PythonQt.QtGui.QPainter"""
        ...

    def size(self) -> Any:
        """X.size() -> PythonQt.QtCore.QSize

Supplemental documentation:
Qt 5 reference:

### [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) QGLFramebufferObject::size() const

Returns the size of the texture attached to this framebuffer object.

Upstream PySide2 reference signatures (binding differences may apply):

```python
size(self) -> PySide2.QtCore.QSize
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#size"""
        ...

    def texture(self) -> int:
        """X.texture() -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLFramebufferObject::texture() const

Returns the texture id for the texture attached as the default rendering target in this
framebuffer object. This texture id can be bound as a normal texture in your own GL
code.

If a multisample framebuffer object is used then the value returned from this function
will be invalid.

Upstream PySide2 reference signatures (binding differences may apply):

```python
texture(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#texture"""
        ...

    def toImage(self) -> Any:
        """X.toImage() -> PythonQt.QtGui.QImage

Supplemental documentation:
Qt 5 reference:

### [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) QGLFramebufferObject::toImage() const

Returns the contents of this framebuffer object as a
[QImage](https://doc.qt.io/archives/qt-5.15/qimage.html).

The returned image has a format of premultiplied ARGB32 or RGB32. The latter is used
only when internalTextureFormat() is set to `GL_RGB`.

If the rendering in the framebuffer was not done with premultiplied alpha in mind,
create a wrapper [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) with a
non-premultiplied format. This is necessary before performing operations like
[QImage::save](https://doc.qt.io/archives/qt-5.15/qimage.html#save)() because otherwise
the image data would get unpremultiplied, even though it was not premultiplied in the
first place. To create such a wrapper without performing a copy of the pixel data, do
the following:

```
QImage fboImage(fbo.toImage());
QImage image(fboImage.constBits(), fboImage.width(), fboImage.height(), QImage::Format_ARGB32);
```

On QNX the back buffer is not preserved when a buffer swap occures. So this function
might return old content.

Upstream PySide2 reference signatures (binding differences may apply):

```python
toImage(self) -> PySide2.QtGui.QImage
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#toImage"""
        ...

    def width(self) -> int:
        """X.width() -> int"""
        ...

    def widthMM(self) -> int:
        """X.widthMM() -> int"""
        ...
    Attachment: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    CombinedDepthStencil: Any
    Depth: Any
    NoAttachment: Any
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

class QGLFramebufferObjectFormat:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

A framebuffer object has several characteristics:

- [Number of samples per pixels.](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setSamples)
- [Depth and/or stencil attachments.](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setAttachment)
- [Texture target.](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setTextureTarget)
- [Internal texture format.](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setInternalTextureFormat)

Note that the desired attachments or number of samples per pixels might not be supported
by the hardware driver. Call
[QGLFramebufferObject::format](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#format)()
after creating a
[QGLFramebufferObject](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html) to
find the exact format that was used to create the frame buffer object.

**Note:** This class has been deprecated in favor of
[QOpenGLFramebufferObjectFormat](https://doc.qt.io/archives/qt-5.15/qopenglframebufferobjectformat.html).

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def attachment(self) -> Any:
        """X.attachment()

Supplemental documentation:
Qt 5 reference:

### [QGLFramebufferObject::Attachment](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#Attachment-enum) QGLFramebufferObjectFormat::attachment() const

Returns the configuration of the depth and stencil buffers attached to a framebuffer
object. The default is
[QGLFramebufferObject::NoAttachment](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#Attachment-enum).

**See also**
[setAttachment](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setAttachment)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
attachment(self) -> PySide2.QtOpenGL.QGLFramebufferObject.Attachment
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#attachment"""
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

    def internalTextureFormat(self) -> int:
        """X.internalTextureFormat() -> int

Supplemental documentation:
Qt 5 reference:

### GLenum QGLFramebufferObjectFormat::internalTextureFormat() const

Returns the internal format of a framebuffer object's texture or multisample framebuffer
object's color buffer. The default is `GL_RGBA8` on desktop OpenGL systems, and
`GL_RGBA` on OpenGL/ES systems.

**See also**
[setInternalTextureFormat](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setInternalTextureFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
internalTextureFormat(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#internalTextureFormat"""
        ...

    def mipmap(self) -> bool:
        """X.mipmap() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFramebufferObjectFormat::mipmap() const

Returns `true` if mipmapping is enabled.

This function was introduced in Qt 4.8.

**See also**
[setMipmap](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setMipmap)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
mipmap(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#mipmap"""
        ...

    def operator_assign(self, other: Any) -> Any:
        """X.operator_assign(other) -> PythonQt.QtOpenGL.QGLFramebufferObjectFormat"""
        ...

    def samples(self) -> int:
        """X.samples() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFramebufferObjectFormat::samples() const

Returns the number of samples per pixel if a framebuffer object is a multisample
framebuffer object. Otherwise, returns 0\\. The default value is 0\\.

**See also**
[setSamples](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setSamples)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
samples(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#samples"""
        ...

    def setAttachment(self, attachment: Any) -> None:
        """X.setAttachment(attachment)

Supplemental documentation:
Qt 5 reference:

### void QGLFramebufferObjectFormat::setAttachment([QGLFramebufferObject::Attachment](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#Attachment-enum) *attachment*)

Sets the attachment configuration of a framebuffer object to *attachment*.

**See also**
[attachment](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#attachment)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAttachment(self, attachment: PySide2.QtOpenGL.QGLFramebufferObject.Attachment) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setAttachment"""
        ...

    def setInternalTextureFormat(self, internalTextureFormat: int) -> None:
        """X.setInternalTextureFormat(internalTextureFormat)

Supplemental documentation:
Qt 5 reference:

### void QGLFramebufferObjectFormat::setInternalTextureFormat(GLenum *internalTextureFormat*)

Sets the internal format of a framebuffer object's texture or multisample framebuffer
object's color buffer to *internalTextureFormat*.

**See also**
[internalTextureFormat](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#internalTextureFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setInternalTextureFormat(self, internalTextureFormat: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setInternalTextureFormat"""
        ...

    def setMipmap(self, enabled: bool) -> None:
        """X.setMipmap(enabled)

Supplemental documentation:
Qt 5 reference:

### void QGLFramebufferObjectFormat::setMipmap(bool *enabled*)

Enables mipmapping if *enabled* is true; otherwise disables it.

Mipmapping is disabled by default.

If mipmapping is enabled, additional memory will be allocated for the mipmap levels. The
mipmap levels can be updated by binding the texture and calling glGenerateMipmap().
Mipmapping cannot be enabled for multisampled framebuffer objects.

This function was introduced in Qt 4.8.

**See also**
[mipmap](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#mipmap)()
and
[QGLFramebufferObject::texture](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#texture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setMipmap(self, enabled: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setMipmap"""
        ...

    def setSamples(self, samples: int) -> None:
        """X.setSamples(samples)

Supplemental documentation:
Qt 5 reference:

### void QGLFramebufferObjectFormat::setSamples(int *samples*)

Sets the number of samples per pixel for a multisample framebuffer object to *samples*.
The default sample count of 0 represents a regular non-multisample framebuffer object.

If the desired amount of samples per pixel is not supported by the hardware then the
maximum number of samples per pixel will be used. Note that multisample framebuffer
objects cannot be bound as textures. Also, the `GL_EXT_framebuffer_multisample`
extension is required to create a framebuffer with more than one sample per pixel.

**See also**
[samples](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#samples)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setSamples(self, samples: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setSamples"""
        ...

    def setTextureTarget(self, target: int) -> None:
        """X.setTextureTarget(target)

Supplemental documentation:
Qt 5 reference:

### void QGLFramebufferObjectFormat::setTextureTarget(GLenum *target*)

Sets the texture target of the texture attached to a framebuffer object to *target*.
Ignored for multisample framebuffer objects.

**See also**
[textureTarget](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#textureTarget)()
and
[samples](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#samples)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setTextureTarget(self, target: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setTextureTarget"""
        ...

    def textureTarget(self) -> int:
        """X.textureTarget() -> int

Supplemental documentation:
Qt 5 reference:

### GLenum QGLFramebufferObjectFormat::textureTarget() const

Returns the texture target of the texture attached to a framebuffer object. Ignored for
multisample framebuffer objects. The default is `GL_TEXTURE_2D`.

**See also**
[setTextureTarget](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#setTextureTarget)()
and
[samples](https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#samples)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
textureTarget(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglframebufferobjectformat.html#textureTarget"""
        ...

class QGLFunctions:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

OpenGL ES 2.0 defines a subset of the OpenGL specification that is common across many
desktop and embedded OpenGL implementations. However, it can be difficult to use the
functions from that subset because they need to be resolved manually on desktop systems.

QGLFunctions provides a guaranteed API that is available on all OpenGL systems and takes
care of function resolution on systems that need it. The recommended way to use
QGLFunctions is by direct inheritance:

```
    class MyGLWidget : public QGLWidget, protected QGLFunctions
    {
        Q_OBJECT
    public:
        MyGLWidget(QWidget *parent = 0) : QGLWidget(parent) {}

    protected:
        void initializeGL();
        void paintGL();
    };

    void MyGLWidget::initializeGL()
    {
        initializeGLFunctions();
    }
```

The `paintGL()` function can then use any of the OpenGL ES 2.0 functions without
explicit resolution, such as
[glActiveTexture](https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glActiveTexture)()
in the following example:

```
    void MyGLWidget::paintGL()
    {
        glActiveTexture(GL_TEXTURE1);
        glBindTexture(GL_TEXTURE_2D, textureId);
        ...
    }
```

QGLFunctions can also be used directly for ad-hoc invocation of OpenGL ES 2.0 functions
on all platforms:

```
    QGLFunctions glFuncs(QGLContext::currentContext());
    glFuncs.glActiveTexture(GL_TEXTURE1);
```

QGLFunctions provides wrappers for all OpenGL ES 2.0 functions, except those like
`glDrawArrays()`, `glViewport()`, and `glBindTexture()` that don't have portability
issues.

Including the header for QGLFunctions will also define all of the OpenGL ES 2.0 macro
constants that are not already defined by the system's OpenGL headers, such as
`GL_TEXTURE1` above.

The
[hasOpenGLFeature](https://doc.qt.io/archives/qt-5.15/qglfunctions.html#hasOpenGLFeature)()
and
[openGLFeatures](https://doc.qt.io/archives/qt-5.15/qglfunctions.html#openGLFeatures)()
functions can be used to determine if the OpenGL implementation has a major OpenGL ES
2.0 feature. For example, the following checks if non power of two textures are
available:

```
    QGLFunctions funcs(QGLContext::currentContext());
    bool npot = funcs.hasOpenGLFeature(QGLFunctions::NPOTTextures);
```

**Note:** This class has been deprecated in favor of
[QOpenGLFunctions](https://doc.qt.io/archives/qt-5.15/qopenglfunctions.html).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def glActiveTexture(self, texture: Any) -> Any:
        """X.glActiveTexture(texture)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glActiveTexture(GLenum *texture*)

Convenience function that calls glActiveTexture(*texture*).

For more information, see the OpenGL ES 2.0 documentation for
[glActiveTexture()](http://www.khronos.org/opengles/sdk/docs/man/glActiveTexture.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glActiveTexture"""
        ...

    def glAttachShader(self, program: Any, shader: Any) -> Any:
        """X.glAttachShader(program, shader)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glAttachShader(GLuint *program*, GLuint *shader*)

Convenience function that calls glAttachShader(*program*, *shader*).

For more information, see the OpenGL ES 2.0 documentation for
[glAttachShader()](http://www.khronos.org/opengles/sdk/docs/man/glAttachShader.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glAttachShader"""
        ...

    def glBindAttribLocation(self, program: Any, index: Any, name: Any) -> Any:
        """X.glBindAttribLocation(program, index, name)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBindAttribLocation(GLuint *program*, GLuint *index*, const char \\**name*)

Convenience function that calls glBindAttribLocation(*program*, *index*, *name*).

For more information, see the OpenGL ES 2.0 documentation for
[glBindAttribLocation()](http://www.khronos.org/opengles/sdk/docs/man/glBindAttribLocation.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBindAttribLocation"""
        ...

    def glBindBuffer(self, target: Any, buffer: Any) -> Any:
        """X.glBindBuffer(target, buffer)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBindBuffer(GLenum *target*, GLuint *buffer*)

Convenience function that calls glBindBuffer(*target*, *buffer*).

For more information, see the OpenGL ES 2.0 documentation for
[glBindBuffer()](http://www.khronos.org/opengles/sdk/docs/man/glBindBuffer.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBindBuffer"""
        ...

    def glBindFramebuffer(self, target: Any, framebuffer: Any) -> Any:
        """X.glBindFramebuffer(target, framebuffer)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBindFramebuffer(GLenum *target*, GLuint *framebuffer*)

Convenience function that calls glBindFramebuffer(*target*, *framebuffer*).

Note that Qt will translate a *framebuffer* argument of 0 to the currently bound
[QOpenGLContext](https://doc.qt.io/archives/qt-5.15/qopenglcontext.html)'s
defaultFramebufferObject().

For more information, see the OpenGL ES 2.0 documentation for
[glBindFramebuffer()](http://www.khronos.org/opengles/sdk/docs/man/glBindFramebuffer.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBindFramebuffer"""
        ...

    def glBindRenderbuffer(self, target: Any, renderbuffer: Any) -> Any:
        """X.glBindRenderbuffer(target, renderbuffer)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBindRenderbuffer(GLenum *target*, GLuint *renderbuffer*)

Convenience function that calls glBindRenderbuffer(*target*, *renderbuffer*).

For more information, see the OpenGL ES 2.0 documentation for
[glBindRenderbuffer()](http://www.khronos.org/opengles/sdk/docs/man/glBindRenderbuffer.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBindRenderbuffer"""
        ...

    def glBlendColor(self, red: Any, green: Any, blue: Any, alpha: Any) -> Any:
        """X.glBlendColor(red, green, blue, alpha)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBlendColor(GLclampf *red*, GLclampf *green*, GLclampf *blue*, GLclampf *alpha*)

Convenience function that calls glBlendColor(*red*, *green*, *blue*, *alpha*).

For more information, see the OpenGL ES 2.0 documentation for
[glBlendColor()](http://www.khronos.org/opengles/sdk/docs/man/glBlendColor.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBlendColor"""
        ...

    def glBlendEquation(self, mode: Any) -> Any:
        """X.glBlendEquation(mode)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBlendEquation(GLenum *mode*)

Convenience function that calls glBlendEquation(*mode*).

For more information, see the OpenGL ES 2.0 documentation for
[glBlendEquation()](http://www.khronos.org/opengles/sdk/docs/man/glBlendEquation.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBlendEquation"""
        ...

    def glBlendEquationSeparate(self, modeRGB: Any, modeAlpha: Any) -> Any:
        """X.glBlendEquationSeparate(modeRGB, modeAlpha)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBlendEquationSeparate(GLenum *modeRGB*, GLenum *modeAlpha*)

Convenience function that calls glBlendEquationSeparate(*modeRGB*, *modeAlpha*).

For more information, see the OpenGL ES 2.0 documentation for
[glBlendEquationSeparate()](http://www.khronos.org/opengles/sdk/docs/man/glBlendEquationSeparate.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBlendEquationSeparate"""
        ...

    def glBlendFuncSeparate(self, srcRGB: Any, dstRGB: Any, srcAlpha: Any, dstAlpha: Any) -> Any:
        """X.glBlendFuncSeparate(srcRGB, dstRGB, srcAlpha, dstAlpha)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glBlendFuncSeparate(GLenum *srcRGB*, GLenum *dstRGB*, GLenum *srcAlpha*, GLenum *dstAlpha*)

Convenience function that calls glBlendFuncSeparate(*srcRGB*, *dstRGB*, *srcAlpha*,
*dstAlpha*).

For more information, see the OpenGL ES 2.0 documentation for
[glBlendFuncSeparate()](http://www.khronos.org/opengles/sdk/docs/man/glBlendFuncSeparate.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glBlendFuncSeparate"""
        ...

    def glCheckFramebufferStatus(self, target: Any) -> int:
        """X.glCheckFramebufferStatus(target) -> int

Supplemental documentation:
Qt 5 reference:

### GLenum QGLFunctions::glCheckFramebufferStatus(GLenum *target*)

Convenience function that calls glCheckFramebufferStatus(*target*).

For more information, see the OpenGL ES 2.0 documentation for
[glCheckFramebufferStatus()](http://www.khronos.org/opengles/sdk/docs/man/glCheckFramebufferStatus.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glCheckFramebufferStatus"""
        ...

    def glClearDepthf(self, depth: Any) -> Any:
        """X.glClearDepthf(depth)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glClearDepthf(GLclampf *depth*)

Convenience function that calls glClearDepth(*depth*) on desktop OpenGL systems and
glClearDepthf(*depth*) on embedded OpenGL ES systems.

For more information, see the OpenGL ES 2.0 documentation for
[glClearDepthf()](http://www.khronos.org/opengles/sdk/docs/man/glClearDepthf.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glClearDepthf"""
        ...

    def glCompileShader(self, shader: Any) -> Any:
        """X.glCompileShader(shader)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glCompileShader(GLuint *shader*)

Convenience function that calls glCompileShader(*shader*).

For more information, see the OpenGL ES 2.0 documentation for
[glCompileShader()](http://www.khronos.org/opengles/sdk/docs/man/glCompileShader.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glCompileShader"""
        ...

    def glCompressedTexImage2D(self, target: Any, level: Any, internalformat: Any, width: Any, height: Any, border: Any, imageSize: Any, data: Any) -> Any:
        """X.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glCompressedTexImage2D(GLenum *target*, GLint *level*, GLenum *internalformat*, GLsizei *width*, GLsizei *height*, GLint *border*, GLsizei *imageSize*, const void \\**data*)

Convenience function that calls glCompressedTexImage2D(*target*, *level*,
*internalformat*, *width*, *height*, *border*, *imageSize*, *data*).

For more information, see the OpenGL ES 2.0 documentation for
[glCompressedTexImage2D()](http://www.khronos.org/opengles/sdk/docs/man/glCompressedTexImage2D.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glCompressedTexImage2D"""
        ...

    def glCompressedTexSubImage2D(self, target: Any, level: Any, xoffset: Any, yoffset: Any, width: Any, height: Any, format: Any, imageSize: Any, data: Any) -> Any:
        """X.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glCompressedTexSubImage2D(GLenum *target*, GLint *level*, GLint *xoffset*, GLint *yoffset*, GLsizei *width*, GLsizei *height*, GLenum *format*, GLsizei *imageSize*, const void \\**data*)

Convenience function that calls glCompressedTexSubImage2D(*target*, *level*, *xoffset*,
*yoffset*, *width*, *height*, *format*, *imageSize*, *data*).

For more information, see the OpenGL ES 2.0 documentation for
[glCompressedTexSubImage2D()](http://www.khronos.org/opengles/sdk/docs/man/glCompressedTexSubImage2D.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glCompressedTexSubImage2D"""
        ...

    def glCreateProgram(self) -> int:
        """X.glCreateProgram() -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLFunctions::glCreateProgram()

Convenience function that calls glCreateProgram().

For more information, see the OpenGL ES 2.0 documentation for
[glCreateProgram()](http://www.khronos.org/opengles/sdk/docs/man/glCreateProgram.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glCreateProgram"""
        ...

    def glCreateShader(self, type: Any) -> int:
        """X.glCreateShader(type) -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLFunctions::glCreateShader(GLenum *type*)

Convenience function that calls glCreateShader(*type*).

For more information, see the OpenGL ES 2.0 documentation for
[glCreateShader()](http://www.khronos.org/opengles/sdk/docs/man/glCreateShader.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glCreateShader"""
        ...

    def glDeleteBuffers(self, n: Any, buffers: Any) -> Any:
        """X.glDeleteBuffers(n, buffers)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDeleteBuffers(GLsizei *n*, const GLuint \\**buffers*)

Convenience function that calls glDeleteBuffers(*n*, *buffers*).

For more information, see the OpenGL ES 2.0 documentation for
[glDeleteBuffers()](http://www.khronos.org/opengles/sdk/docs/man/glDeleteBuffers.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDeleteBuffers"""
        ...

    def glDeleteFramebuffers(self, n: Any, framebuffers: Any) -> Any:
        """X.glDeleteFramebuffers(n, framebuffers)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDeleteFramebuffers(GLsizei *n*, const GLuint \\**framebuffers*)

Convenience function that calls glDeleteFramebuffers(*n*, *framebuffers*).

For more information, see the OpenGL ES 2.0 documentation for
[glDeleteFramebuffers()](http://www.khronos.org/opengles/sdk/docs/man/glDeleteFramebuffers.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDeleteFramebuffers"""
        ...

    def glDeleteProgram(self, program: Any) -> Any:
        """X.glDeleteProgram(program)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDeleteProgram(GLuint *program*)

Convenience function that calls glDeleteProgram(*program*).

For more information, see the OpenGL ES 2.0 documentation for
[glDeleteProgram()](http://www.khronos.org/opengles/sdk/docs/man/glDeleteProgram.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDeleteProgram"""
        ...

    def glDeleteRenderbuffers(self, n: Any, renderbuffers: Any) -> Any:
        """X.glDeleteRenderbuffers(n, renderbuffers)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDeleteRenderbuffers(GLsizei *n*, const GLuint \\**renderbuffers*)

Convenience function that calls glDeleteRenderbuffers(*n*, *renderbuffers*).

For more information, see the OpenGL ES 2.0 documentation for
[glDeleteRenderbuffers()](http://www.khronos.org/opengles/sdk/docs/man/glDeleteRenderbuffers.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDeleteRenderbuffers"""
        ...

    def glDeleteShader(self, shader: Any) -> Any:
        """X.glDeleteShader(shader)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDeleteShader(GLuint *shader*)

Convenience function that calls glDeleteShader(*shader*).

For more information, see the OpenGL ES 2.0 documentation for
[glDeleteShader()](http://www.khronos.org/opengles/sdk/docs/man/glDeleteShader.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDeleteShader"""
        ...

    def glDepthRangef(self, zNear: Any, zFar: Any) -> Any:
        """X.glDepthRangef(zNear, zFar)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDepthRangef(GLclampf *zNear*, GLclampf *zFar*)

Convenience function that calls glDepthRange(*zNear*, *zFar*) on desktop OpenGL systems
and glDepthRangef(*zNear*, *zFar*) on embedded OpenGL ES systems.

For more information, see the OpenGL ES 2.0 documentation for
[glDepthRangef()](http://www.khronos.org/opengles/sdk/docs/man/glDepthRangef.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDepthRangef"""
        ...

    def glDetachShader(self, program: Any, shader: Any) -> Any:
        """X.glDetachShader(program, shader)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDetachShader(GLuint *program*, GLuint *shader*)

Convenience function that calls glDetachShader(*program*, *shader*).

For more information, see the OpenGL ES 2.0 documentation for
[glDetachShader()](http://www.khronos.org/opengles/sdk/docs/man/glDetachShader.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDetachShader"""
        ...

    def glDisableVertexAttribArray(self, index: Any) -> Any:
        """X.glDisableVertexAttribArray(index)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glDisableVertexAttribArray(GLuint *index*)

Convenience function that calls glDisableVertexAttribArray(*index*).

For more information, see the OpenGL ES 2.0 documentation for
[glDisableVertexAttribArray()](http://www.khronos.org/opengles/sdk/docs/man/glDisableVertexAttribArray.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glDisableVertexAttribArray"""
        ...

    def glEnableVertexAttribArray(self, index: Any) -> Any:
        """X.glEnableVertexAttribArray(index)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glEnableVertexAttribArray(GLuint *index*)

Convenience function that calls glEnableVertexAttribArray(*index*).

For more information, see the OpenGL ES 2.0 documentation for
[glEnableVertexAttribArray()](http://www.khronos.org/opengles/sdk/docs/man/glEnableVertexAttribArray.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glEnableVertexAttribArray"""
        ...

    def glFramebufferRenderbuffer(self, target: Any, attachment: Any, renderbuffertarget: Any, renderbuffer: Any) -> Any:
        """X.glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glFramebufferRenderbuffer(GLenum *target*, GLenum *attachment*, GLenum *renderbuffertarget*, GLuint *renderbuffer*)

Convenience function that calls glFramebufferRenderbuffer(*target*, *attachment*,
*renderbuffertarget*, *renderbuffer*).

For more information, see the OpenGL ES 2.0 documentation for
[glFramebufferRenderbuffer()](http://www.khronos.org/opengles/sdk/docs/man/glFramebufferRenderbuffer.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glFramebufferRenderbuffer"""
        ...

    def glFramebufferTexture2D(self, target: Any, attachment: Any, textarget: Any, texture: Any, level: Any) -> Any:
        """X.glFramebufferTexture2D(target, attachment, textarget, texture, level)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glFramebufferTexture2D(GLenum *target*, GLenum *attachment*, GLenum *textarget*, GLuint *texture*, GLint *level*)

Convenience function that calls glFramebufferTexture2D(*target*, *attachment*,
*textarget*, *texture*, *level*).

For more information, see the OpenGL ES 2.0 documentation for
[glFramebufferTexture2D()](http://www.khronos.org/opengles/sdk/docs/man/glFramebufferTexture2D.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glFramebufferTexture2D"""
        ...

    def glGenBuffers(self, n: Any, buffers: Any) -> Any:
        """X.glGenBuffers(n, buffers)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGenBuffers(GLsizei *n*, GLuint \\**buffers*)

Convenience function that calls glGenBuffers(*n*, *buffers*).

For more information, see the OpenGL ES 2.0 documentation for
[glGenBuffers()](http://www.khronos.org/opengles/sdk/docs/man/glGenBuffers.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGenBuffers"""
        ...

    def glGenFramebuffers(self, n: Any, framebuffers: Any) -> Any:
        """X.glGenFramebuffers(n, framebuffers)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGenFramebuffers(GLsizei *n*, GLuint \\**framebuffers*)

Convenience function that calls glGenFramebuffers(*n*, *framebuffers*).

For more information, see the OpenGL ES 2.0 documentation for
[glGenFramebuffers()](http://www.khronos.org/opengles/sdk/docs/man/glGenFramebuffers.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGenFramebuffers"""
        ...

    def glGenRenderbuffers(self, n: Any, renderbuffers: Any) -> Any:
        """X.glGenRenderbuffers(n, renderbuffers)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGenRenderbuffers(GLsizei *n*, GLuint \\**renderbuffers*)

Convenience function that calls glGenRenderbuffers(*n*, *renderbuffers*).

For more information, see the OpenGL ES 2.0 documentation for
[glGenRenderbuffers()](http://www.khronos.org/opengles/sdk/docs/man/glGenRenderbuffers.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGenRenderbuffers"""
        ...

    def glGenerateMipmap(self, target: Any) -> Any:
        """X.glGenerateMipmap(target)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGenerateMipmap(GLenum *target*)

Convenience function that calls glGenerateMipmap(*target*).

For more information, see the OpenGL ES 2.0 documentation for
[glGenerateMipmap()](http://www.khronos.org/opengles/sdk/docs/man/glGenerateMipmap.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGenerateMipmap"""
        ...

    def glGetActiveAttrib(self, program: Any, index: Any, bufsize: Any, length: Any, size: Any, type: Any, name: Any) -> Any:
        """X.glGetActiveAttrib(program, index, bufsize, length, size, type, name)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetActiveAttrib(GLuint *program*, GLuint *index*, GLsizei *bufsize*, GLsizei \\**length*, GLint \\**size*, GLenum \\**type*, char \\**name*)

Convenience function that calls glGetActiveAttrib(*program*, *index*, *bufsize*,
*length*, *size*, *type*, *name*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetActiveAttrib()](http://www.khronos.org/opengles/sdk/docs/man/glGetActiveAttrib.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetActiveAttrib"""
        ...

    def glGetActiveUniform(self, program: Any, index: Any, bufsize: Any, length: Any, size: Any, type: Any, name: Any) -> Any:
        """X.glGetActiveUniform(program, index, bufsize, length, size, type, name)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetActiveUniform(GLuint *program*, GLuint *index*, GLsizei *bufsize*, GLsizei \\**length*, GLint \\**size*, GLenum \\**type*, char \\**name*)

Convenience function that calls glGetActiveUniform(*program*, *index*, *bufsize*,
*length*, *size*, *type*, *name*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetActiveUniform()](http://www.khronos.org/opengles/sdk/docs/man/glGetActiveUniform.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetActiveUniform"""
        ...

    def glGetAttachedShaders(self, program: Any, maxcount: Any, count: Any, shaders: Any) -> Any:
        """X.glGetAttachedShaders(program, maxcount, count, shaders)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetAttachedShaders(GLuint *program*, GLsizei *maxcount*, GLsizei \\**count*, GLuint \\**shaders*)

Convenience function that calls glGetAttachedShaders(*program*, *maxcount*, *count*,
*shaders*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetAttachedShaders()](http://www.khronos.org/opengles/sdk/docs/man/glGetAttachedShaders.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetAttachedShaders"""
        ...

    def glGetAttribLocation(self, program: Any, name: Any) -> int:
        """X.glGetAttribLocation(program, name) -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFunctions::glGetAttribLocation(GLuint *program*, const char \\**name*)

Convenience function that calls glGetAttribLocation(*program*, *name*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetAttribLocation()](http://www.khronos.org/opengles/sdk/docs/man/glGetAttribLocation.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetAttribLocation"""
        ...

    def glGetBufferParameteriv(self, target: Any, pname: Any, params: Any) -> Any:
        """X.glGetBufferParameteriv(target, pname, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetBufferParameteriv(GLenum *target*, GLenum *pname*, GLint \\**params*)

Convenience function that calls glGetBufferParameteriv(*target*, *pname*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetBufferParameteriv()](http://www.khronos.org/opengles/sdk/docs/man/glGetBufferParameteriv.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetBufferParameteriv"""
        ...

    def glGetFramebufferAttachmentParameteriv(self, target: Any, attachment: Any, pname: Any, params: Any) -> Any:
        """X.glGetFramebufferAttachmentParameteriv(target, attachment, pname, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetFramebufferAttachmentParameteriv(GLenum *target*, GLenum *attachment*, GLenum *pname*, GLint \\**params*)

Convenience function that calls glGetFramebufferAttachmentParameteriv(*target*,
*attachment*, *pname*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetFramebufferAttachmentParameteriv()](http://www.khronos.org/opengles/sdk/docs/man/glGetFramebufferAttachmentParameteriv.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetFramebufferAttachmentParameteriv"""
        ...

    def glGetProgramInfoLog(self, program: Any, bufsize: Any, length: Any, infolog: Any) -> Any:
        """X.glGetProgramInfoLog(program, bufsize, length, infolog)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetProgramInfoLog(GLuint *program*, GLsizei *bufsize*, GLsizei \\**length*, char \\**infolog*)

Convenience function that calls glGetProgramInfoLog(*program*, *bufsize*, *length*,
*infolog*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetProgramInfoLog()](http://www.khronos.org/opengles/sdk/docs/man/glGetProgramInfoLog.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetProgramInfoLog"""
        ...

    def glGetProgramiv(self, program: Any, pname: Any, params: Any) -> Any:
        """X.glGetProgramiv(program, pname, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetProgramiv(GLuint *program*, GLenum *pname*, GLint \\**params*)

Convenience function that calls glGetProgramiv(*program*, *pname*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetProgramiv()](http://www.khronos.org/opengles/sdk/docs/man/glGetProgramiv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetProgramiv"""
        ...

    def glGetRenderbufferParameteriv(self, target: Any, pname: Any, params: Any) -> Any:
        """X.glGetRenderbufferParameteriv(target, pname, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetRenderbufferParameteriv(GLenum *target*, GLenum *pname*, GLint \\**params*)

Convenience function that calls glGetRenderbufferParameteriv(*target*, *pname*,
*params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetRenderbufferParameteriv()](http://www.khronos.org/opengles/sdk/docs/man/glGetRenderbufferParameteriv.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetRenderbufferParameteriv"""
        ...

    def glGetShaderInfoLog(self, shader: Any, bufsize: Any, length: Any, infolog: Any) -> Any:
        """X.glGetShaderInfoLog(shader, bufsize, length, infolog)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetShaderInfoLog(GLuint *shader*, GLsizei *bufsize*, GLsizei \\**length*, char \\**infolog*)

Convenience function that calls glGetShaderInfoLog(*shader*, *bufsize*, *length*,
*infolog*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetShaderInfoLog()](http://www.khronos.org/opengles/sdk/docs/man/glGetShaderInfoLog.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetShaderInfoLog"""
        ...

    def glGetShaderPrecisionFormat(self, shadertype: Any, precisiontype: Any, range: Any, precision: Any) -> Any:
        """X.glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetShaderPrecisionFormat(GLenum *shadertype*, GLenum *precisiontype*, GLint \\**range*, GLint \\**precision*)

Convenience function that calls glGetShaderPrecisionFormat(*shadertype*,
*precisiontype*, *range*, *precision*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetShaderPrecisionFormat()](http://www.khronos.org/opengles/sdk/docs/man/glGetShaderPrecisionFormat.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetShaderPrecisionFormat"""
        ...

    def glGetShaderSource(self, shader: Any, bufsize: Any, length: Any, source: Any) -> Any:
        """X.glGetShaderSource(shader, bufsize, length, source)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetShaderSource(GLuint *shader*, GLsizei *bufsize*, GLsizei \\**length*, char \\**source*)

Convenience function that calls glGetShaderSource(*shader*, *bufsize*, *length*,
*source*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetShaderSource()](http://www.khronos.org/opengles/sdk/docs/man/glGetShaderSource.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetShaderSource"""
        ...

    def glGetShaderiv(self, shader: Any, pname: Any, params: Any) -> Any:
        """X.glGetShaderiv(shader, pname, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetShaderiv(GLuint *shader*, GLenum *pname*, GLint \\**params*)

Convenience function that calls glGetShaderiv(*shader*, *pname*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetShaderiv()](http://www.khronos.org/opengles/sdk/docs/man/glGetShaderiv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetShaderiv"""
        ...

    def glGetUniformLocation(self, program: Any, name: Any) -> int:
        """X.glGetUniformLocation(program, name) -> int

Supplemental documentation:
Qt 5 reference:

### int QGLFunctions::glGetUniformLocation(GLuint *program*, const char \\**name*)

Convenience function that calls glGetUniformLocation(*program*, *name*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetUniformLocation()](http://www.khronos.org/opengles/sdk/docs/man/glGetUniformLocation.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetUniformLocation"""
        ...

    def glGetUniformfv(self, program: Any, location: Any, params: Any) -> Any:
        """X.glGetUniformfv(program, location, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetUniformfv(GLuint *program*, GLint *location*, GLfloat \\**params*)

Convenience function that calls glGetUniformfv(*program*, *location*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetUniformfv()](http://www.khronos.org/opengles/sdk/docs/man/glGetUniformfv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetUniformfv"""
        ...

    def glGetUniformiv(self, program: Any, location: Any, params: Any) -> Any:
        """X.glGetUniformiv(program, location, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetUniformiv(GLuint *program*, GLint *location*, GLint \\**params*)

Convenience function that calls glGetUniformiv(*program*, *location*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetUniformiv()](http://www.khronos.org/opengles/sdk/docs/man/glGetUniformiv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetUniformiv"""
        ...

    def glGetVertexAttribPointerv(self, index: Any, pname: Any, pointer: Any) -> Any:
        """X.glGetVertexAttribPointerv(index, pname, pointer)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetVertexAttribPointerv(GLuint *index*, GLenum *pname*, void \\*\\**pointer*)

Convenience function that calls glGetVertexAttribPointerv(*index*, *pname*, *pointer*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetVertexAttribPointerv()](http://www.khronos.org/opengles/sdk/docs/man/glGetVertexAttribPointerv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetVertexAttribPointerv"""
        ...

    def glGetVertexAttribfv(self, index: Any, pname: Any, params: Any) -> Any:
        """X.glGetVertexAttribfv(index, pname, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetVertexAttribfv(GLuint *index*, GLenum *pname*, GLfloat \\**params*)

Convenience function that calls glGetVertexAttribfv(*index*, *pname*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetVertexAttribfv()](http://www.khronos.org/opengles/sdk/docs/man/glGetVertexAttribfv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetVertexAttribfv"""
        ...

    def glGetVertexAttribiv(self, index: Any, pname: Any, params: Any) -> Any:
        """X.glGetVertexAttribiv(index, pname, params)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glGetVertexAttribiv(GLuint *index*, GLenum *pname*, GLint \\**params*)

Convenience function that calls glGetVertexAttribiv(*index*, *pname*, *params*).

For more information, see the OpenGL ES 2.0 documentation for
[glGetVertexAttribiv()](http://www.khronos.org/opengles/sdk/docs/man/glGetVertexAttribiv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glGetVertexAttribiv"""
        ...

    def glIsBuffer(self, buffer: Any) -> int:
        """X.glIsBuffer(buffer) -> int

Supplemental documentation:
Qt 5 reference:

### GLboolean QGLFunctions::glIsBuffer(GLuint *buffer*)

Convenience function that calls glIsBuffer(*buffer*).

For more information, see the OpenGL ES 2.0 documentation for
[glIsBuffer()](http://www.khronos.org/opengles/sdk/docs/man/glIsBuffer.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glIsBuffer"""
        ...

    def glIsFramebuffer(self, framebuffer: Any) -> int:
        """X.glIsFramebuffer(framebuffer) -> int

Supplemental documentation:
Qt 5 reference:

### GLboolean QGLFunctions::glIsFramebuffer(GLuint *framebuffer*)

Convenience function that calls glIsFramebuffer(*framebuffer*).

For more information, see the OpenGL ES 2.0 documentation for
[glIsFramebuffer()](http://www.khronos.org/opengles/sdk/docs/man/glIsFramebuffer.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glIsFramebuffer"""
        ...

    def glIsProgram(self, program: Any) -> int:
        """X.glIsProgram(program) -> int

Supplemental documentation:
Qt 5 reference:

### GLboolean QGLFunctions::glIsProgram(GLuint *program*)

Convenience function that calls glIsProgram(*program*).

For more information, see the OpenGL ES 2.0 documentation for
[glIsProgram()](http://www.khronos.org/opengles/sdk/docs/man/glIsProgram.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glIsProgram"""
        ...

    def glIsRenderbuffer(self, renderbuffer: Any) -> int:
        """X.glIsRenderbuffer(renderbuffer) -> int

Supplemental documentation:
Qt 5 reference:

### GLboolean QGLFunctions::glIsRenderbuffer(GLuint *renderbuffer*)

Convenience function that calls glIsRenderbuffer(*renderbuffer*).

For more information, see the OpenGL ES 2.0 documentation for
[glIsRenderbuffer()](http://www.khronos.org/opengles/sdk/docs/man/glIsRenderbuffer.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glIsRenderbuffer"""
        ...

    def glIsShader(self, shader: Any) -> int:
        """X.glIsShader(shader) -> int

Supplemental documentation:
Qt 5 reference:

### GLboolean QGLFunctions::glIsShader(GLuint *shader*)

Convenience function that calls glIsShader(*shader*).

For more information, see the OpenGL ES 2.0 documentation for
[glIsShader()](http://www.khronos.org/opengles/sdk/docs/man/glIsShader.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glIsShader"""
        ...

    def glLinkProgram(self, program: Any) -> Any:
        """X.glLinkProgram(program)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glLinkProgram(GLuint *program*)

Convenience function that calls glLinkProgram(*program*).

For more information, see the OpenGL ES 2.0 documentation for
[glLinkProgram()](http://www.khronos.org/opengles/sdk/docs/man/glLinkProgram.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glLinkProgram"""
        ...

    def glReleaseShaderCompiler(self) -> Any:
        """X.glReleaseShaderCompiler()

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glReleaseShaderCompiler()

Convenience function that calls glReleaseShaderCompiler().

For more information, see the OpenGL ES 2.0 documentation for
[glReleaseShaderCompiler()](http://www.khronos.org/opengles/sdk/docs/man/glReleaseShaderCompiler.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glReleaseShaderCompiler"""
        ...

    def glRenderbufferStorage(self, target: Any, internalformat: Any, width: Any, height: Any) -> Any:
        """X.glRenderbufferStorage(target, internalformat, width, height)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glRenderbufferStorage(GLenum *target*, GLenum *internalformat*, GLsizei *width*, GLsizei *height*)

Convenience function that calls glRenderbufferStorage(*target*, *internalformat*,
*width*, *height*).

For more information, see the OpenGL ES 2.0 documentation for
[glRenderbufferStorage()](http://www.khronos.org/opengles/sdk/docs/man/glRenderbufferStorage.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glRenderbufferStorage"""
        ...

    def glSampleCoverage(self, value: Any, invert: Any) -> Any:
        """X.glSampleCoverage(value, invert)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glSampleCoverage(GLclampf *value*, GLboolean *invert*)

Convenience function that calls glSampleCoverage(*value*, *invert*).

For more information, see the OpenGL ES 2.0 documentation for
[glSampleCoverage()](http://www.khronos.org/opengles/sdk/docs/man/glSampleCoverage.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glSampleCoverage"""
        ...

    def glShaderBinary(self, n: Any, shaders: Any, binaryformat: Any, binary: Any, length: Any) -> Any:
        """X.glShaderBinary(n, shaders, binaryformat, binary, length)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glShaderBinary(GLint *n*, const GLuint \\**shaders*, GLenum *binaryformat*, const void \\**binary*, GLint *length*)

Convenience function that calls glShaderBinary(*n*, *shaders*, *binaryformat*, *binary*,
*length*).

For more information, see the OpenGL ES 2.0 documentation for
[glShaderBinary()](http://www.khronos.org/opengles/sdk/docs/man/glShaderBinary.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glShaderBinary"""
        ...

    def glShaderSource(self, shader: Any, count: Any, string: Any, length: Any) -> Any:
        """X.glShaderSource(shader, count, string, length)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glShaderSource(GLuint *shader*, GLsizei *count*, const char \\*\\**string*, const GLint \\**length*)

Convenience function that calls glShaderSource(*shader*, *count*, *string*, *length*).

For more information, see the OpenGL ES 2.0 documentation for
[glShaderSource()](http://www.khronos.org/opengles/sdk/docs/man/glShaderSource.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glShaderSource"""
        ...

    def glStencilFuncSeparate(self, face: Any, func: Any, ref: Any, mask: Any) -> Any:
        """X.glStencilFuncSeparate(face, func, ref, mask)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glStencilFuncSeparate(GLenum *face*, GLenum *func*, GLint *ref*, GLuint *mask*)

Convenience function that calls glStencilFuncSeparate(*face*, *func*, *ref*, *mask*).

For more information, see the OpenGL ES 2.0 documentation for
[glStencilFuncSeparate()](http://www.khronos.org/opengles/sdk/docs/man/glStencilFuncSeparate.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glStencilFuncSeparate"""
        ...

    def glStencilMaskSeparate(self, face: Any, mask: Any) -> Any:
        """X.glStencilMaskSeparate(face, mask)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glStencilMaskSeparate(GLenum *face*, GLuint *mask*)

Convenience function that calls glStencilMaskSeparate(*face*, *mask*).

For more information, see the OpenGL ES 2.0 documentation for
[glStencilMaskSeparate()](http://www.khronos.org/opengles/sdk/docs/man/glStencilMaskSeparate.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glStencilMaskSeparate"""
        ...

    def glStencilOpSeparate(self, face: Any, fail: Any, zfail: Any, zpass: Any) -> Any:
        """X.glStencilOpSeparate(face, fail, zfail, zpass)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glStencilOpSeparate(GLenum *face*, GLenum *fail*, GLenum *zfail*, GLenum *zpass*)

Convenience function that calls glStencilOpSeparate(*face*, *fail*, *zfail*, *zpass*).

For more information, see the OpenGL ES 2.0 documentation for
[glStencilOpSeparate()](http://www.khronos.org/opengles/sdk/docs/man/glStencilOpSeparate.xml).

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glStencilOpSeparate"""
        ...

    def glUniform1f(self, location: Any, x: Any) -> Any:
        """X.glUniform1f(location, x)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform1f(GLint *location*, GLfloat *x*)

Convenience function that calls glUniform1f(*location*, *x*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform1f()](http://www.khronos.org/opengles/sdk/docs/man/glUniform1f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform1f"""
        ...

    def glUniform1fv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform1fv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform1fv(GLint *location*, GLsizei *count*, const GLfloat \\**v*)

Convenience function that calls glUniform1fv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform1fv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform1fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform1fv"""
        ...

    def glUniform1i(self, location: Any, x: Any) -> Any:
        """X.glUniform1i(location, x)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform1i(GLint *location*, GLint *x*)

Convenience function that calls glUniform1i(*location*, *x*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform1i()](http://www.khronos.org/opengles/sdk/docs/man/glUniform1i.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform1i"""
        ...

    def glUniform1iv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform1iv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform1iv(GLint *location*, GLsizei *count*, const GLint \\**v*)

Convenience function that calls glUniform1iv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform1iv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform1iv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform1iv"""
        ...

    def glUniform2f(self, location: Any, x: Any, y: Any) -> Any:
        """X.glUniform2f(location, x, y)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform2f(GLint *location*, GLfloat *x*, GLfloat *y*)

Convenience function that calls glUniform2f(*location*, *x*, *y*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform2f()](http://www.khronos.org/opengles/sdk/docs/man/glUniform2f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform2f"""
        ...

    def glUniform2fv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform2fv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform2fv(GLint *location*, GLsizei *count*, const GLfloat \\**v*)

Convenience function that calls glUniform2fv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform2fv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform2fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform2fv"""
        ...

    def glUniform2i(self, location: Any, x: Any, y: Any) -> Any:
        """X.glUniform2i(location, x, y)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform2i(GLint *location*, GLint *x*, GLint *y*)

Convenience function that calls glUniform2i(*location*, *x*, *y*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform2i()](http://www.khronos.org/opengles/sdk/docs/man/glUniform2i.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform2i"""
        ...

    def glUniform2iv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform2iv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform2iv(GLint *location*, GLsizei *count*, const GLint \\**v*)

Convenience function that calls glUniform2iv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform2iv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform2iv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform2iv"""
        ...

    def glUniform3f(self, location: Any, x: Any, y: Any, z: Any) -> Any:
        """X.glUniform3f(location, x, y, z)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform3f(GLint *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

Convenience function that calls glUniform3f(*location*, *x*, *y*, *z*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform3f()](http://www.khronos.org/opengles/sdk/docs/man/glUniform3f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform3f"""
        ...

    def glUniform3fv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform3fv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform3fv(GLint *location*, GLsizei *count*, const GLfloat \\**v*)

Convenience function that calls glUniform3fv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform3fv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform3fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform3fv"""
        ...

    def glUniform3i(self, location: Any, x: Any, y: Any, z: Any) -> Any:
        """X.glUniform3i(location, x, y, z)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform3i(GLint *location*, GLint *x*, GLint *y*, GLint *z*)

Convenience function that calls glUniform3i(*location*, *x*, *y*, *z*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform3i()](http://www.khronos.org/opengles/sdk/docs/man/glUniform3i.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform3i"""
        ...

    def glUniform3iv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform3iv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform3iv(GLint *location*, GLsizei *count*, const GLint \\**v*)

Convenience function that calls glUniform3iv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform3iv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform3iv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform3iv"""
        ...

    def glUniform4f(self, location: Any, x: Any, y: Any, z: Any, w: Any) -> Any:
        """X.glUniform4f(location, x, y, z, w)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform4f(GLint *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

Convenience function that calls glUniform4f(*location*, *x*, *y*, *z*, *w*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform4f()](http://www.khronos.org/opengles/sdk/docs/man/glUniform4f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform4f"""
        ...

    def glUniform4fv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform4fv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform4fv(GLint *location*, GLsizei *count*, const GLfloat \\**v*)

Convenience function that calls glUniform4fv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform4fv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform4fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform4fv"""
        ...

    def glUniform4i(self, location: Any, x: Any, y: Any, z: Any, w: Any) -> Any:
        """X.glUniform4i(location, x, y, z, w)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform4i(GLint *location*, GLint *x*, GLint *y*, GLint *z*, GLint *w*)

Convenience function that calls glUniform4i(*location*, *x*, *y*, *z*, *w*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform4i()](http://www.khronos.org/opengles/sdk/docs/man/glUniform4i.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform4i"""
        ...

    def glUniform4iv(self, location: Any, count: Any, v: Any) -> Any:
        """X.glUniform4iv(location, count, v)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniform4iv(GLint *location*, GLsizei *count*, const GLint \\**v*)

Convenience function that calls glUniform4iv(*location*, *count*, *v*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniform4iv()](http://www.khronos.org/opengles/sdk/docs/man/glUniform4iv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniform4iv"""
        ...

    def glUniformMatrix2fv(self, location: Any, count: Any, transpose: Any, value: Any) -> Any:
        """X.glUniformMatrix2fv(location, count, transpose, value)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniformMatrix2fv(GLint *location*, GLsizei *count*, GLboolean *transpose*, const GLfloat \\**value*)

Convenience function that calls glUniformMatrix2fv(*location*, *count*, *transpose*,
*value*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniformMatrix2fv()](http://www.khronos.org/opengles/sdk/docs/man/glUniformMatrix2fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniformMatrix2fv"""
        ...

    def glUniformMatrix3fv(self, location: Any, count: Any, transpose: Any, value: Any) -> Any:
        """X.glUniformMatrix3fv(location, count, transpose, value)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniformMatrix3fv(GLint *location*, GLsizei *count*, GLboolean *transpose*, const GLfloat \\**value*)

Convenience function that calls glUniformMatrix3fv(*location*, *count*, *transpose*,
*value*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniformMatrix3fv()](http://www.khronos.org/opengles/sdk/docs/man/glUniformMatrix3fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniformMatrix3fv"""
        ...

    def glUniformMatrix4fv(self, location: Any, count: Any, transpose: Any, value: Any) -> Any:
        """X.glUniformMatrix4fv(location, count, transpose, value)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUniformMatrix4fv(GLint *location*, GLsizei *count*, GLboolean *transpose*, const GLfloat \\**value*)

Convenience function that calls glUniformMatrix4fv(*location*, *count*, *transpose*,
*value*).

For more information, see the OpenGL ES 2.0 documentation for
[glUniformMatrix4fv()](http://www.khronos.org/opengles/sdk/docs/man/glUniformMatrix4fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUniformMatrix4fv"""
        ...

    def glUseProgram(self, program: Any) -> Any:
        """X.glUseProgram(program)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glUseProgram(GLuint *program*)

Convenience function that calls glUseProgram(*program*).

For more information, see the OpenGL ES 2.0 documentation for
[glUseProgram()](http://www.khronos.org/opengles/sdk/docs/man/glUseProgram.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glUseProgram"""
        ...

    def glValidateProgram(self, program: Any) -> Any:
        """X.glValidateProgram(program)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glValidateProgram(GLuint *program*)

Convenience function that calls glValidateProgram(*program*).

For more information, see the OpenGL ES 2.0 documentation for
[glValidateProgram()](http://www.khronos.org/opengles/sdk/docs/man/glValidateProgram.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glValidateProgram"""
        ...

    def glVertexAttrib1f(self, indx: Any, x: Any) -> Any:
        """X.glVertexAttrib1f(indx, x)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib1f(GLuint *indx*, GLfloat *x*)

Convenience function that calls glVertexAttrib1f(*indx*, *x*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib1f()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib1f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib1f"""
        ...

    def glVertexAttrib1fv(self, indx: Any, values: Any) -> Any:
        """X.glVertexAttrib1fv(indx, values)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib1fv(GLuint *indx*, const GLfloat \\**values*)

Convenience function that calls glVertexAttrib1fv(*indx*, *values*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib1fv()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib1fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib1fv"""
        ...

    def glVertexAttrib2f(self, indx: Any, x: Any, y: Any) -> Any:
        """X.glVertexAttrib2f(indx, x, y)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib2f(GLuint *indx*, GLfloat *x*, GLfloat *y*)

Convenience function that calls glVertexAttrib2f(*indx*, *x*, *y*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib2f()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib2f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib2f"""
        ...

    def glVertexAttrib2fv(self, indx: Any, values: Any) -> Any:
        """X.glVertexAttrib2fv(indx, values)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib2fv(GLuint *indx*, const GLfloat \\**values*)

Convenience function that calls glVertexAttrib2fv(*indx*, *values*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib2fv()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib2fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib2fv"""
        ...

    def glVertexAttrib3f(self, indx: Any, x: Any, y: Any, z: Any) -> Any:
        """X.glVertexAttrib3f(indx, x, y, z)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib3f(GLuint *indx*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

Convenience function that calls glVertexAttrib3f(*indx*, *x*, *y*, *z*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib3f()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib3f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib3f"""
        ...

    def glVertexAttrib3fv(self, indx: Any, values: Any) -> Any:
        """X.glVertexAttrib3fv(indx, values)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib3fv(GLuint *indx*, const GLfloat \\**values*)

Convenience function that calls glVertexAttrib3fv(*indx*, *values*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib3fv()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib3fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib3fv"""
        ...

    def glVertexAttrib4f(self, indx: Any, x: Any, y: Any, z: Any, w: Any) -> Any:
        """X.glVertexAttrib4f(indx, x, y, z, w)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib4f(GLuint *indx*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

Convenience function that calls glVertexAttrib4f(*indx*, *x*, *y*, *z*, *w*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib4f()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib4f.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib4f"""
        ...

    def glVertexAttrib4fv(self, indx: Any, values: Any) -> Any:
        """X.glVertexAttrib4fv(indx, values)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttrib4fv(GLuint *indx*, const GLfloat \\**values*)

Convenience function that calls glVertexAttrib4fv(*indx*, *values*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttrib4fv()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttrib4fv.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttrib4fv"""
        ...

    def glVertexAttribPointer(self, indx: Any, size: Any, type: Any, normalized: Any, stride: Any, ptr: Any) -> Any:
        """X.glVertexAttribPointer(indx, size, type, normalized, stride, ptr)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::glVertexAttribPointer(GLuint *indx*, GLint *size*, GLenum *type*, GLboolean *normalized*, GLsizei *stride*, const void \\**ptr*)

Convenience function that calls glVertexAttribPointer(*indx*, *size*, *type*,
*normalized*, *stride*, *ptr*).

For more information, see the OpenGL ES 2.0 documentation for
[glVertexAttribPointer()](http://www.khronos.org/opengles/sdk/docs/man/glVertexAttribPointer.xml).

This convenience function will do nothing on OpenGL ES 1.x systems.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#glVertexAttribPointer"""
        ...

    def hasOpenGLFeature(self, feature: Any) -> bool:
        """X.hasOpenGLFeature(feature) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLFunctions::hasOpenGLFeature([QGLFunctions::OpenGLFeature](https://doc.qt.io/archives/qt-5.15/qglfunctions.html#OpenGLFeature-enum) *feature*) const

Returns `true` if *feature* is present on this system's OpenGL implementation; false
otherwise.

It is assumed that the QGLContext associated with this function resolver is current.

**See also**
[openGLFeatures](https://doc.qt.io/archives/qt-5.15/qglfunctions.html#openGLFeatures)().

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#hasOpenGLFeature"""
        ...

    def help(self, *args: Any, **kwargs: Any) -> Any:
        """Shows the help of available methods for this class"""
        ...

    def inherits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns if the class inherits or is of given type name"""
        ...

    def initializeGLFunctions(self, context: Any) -> Any:
        """X.initializeGLFunctions(context)

Supplemental documentation:
Qt 5 reference:

### void QGLFunctions::initializeGLFunctions(const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) \\**context* \\= nullptr)

Initializes GL function resolution for *context*. If *context* is `nullptr`, then the
current QGLContext will be used.

After calling this function, the
[QGLFunctions](https://doc.qt.io/archives/qt-5.15/qglfunctions.html) object can only be
used with *context* and other contexts that share with it. Call initializeGLFunctions()
again to change the object's context association.

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#initializeGLFunctions"""
        ...

    def openGLFeatures(self) -> Any:
        """X.openGLFeatures()

Supplemental documentation:
Qt 5 reference:

### [QGLFunctions::OpenGLFeatures](https://doc.qt.io/archives/qt-5.15/qglfunctions.html#OpenGLFeature-enum) QGLFunctions::openGLFeatures() const

Returns the set of features that are present on this system's OpenGL implementation.

It is assumed that the QGLContext associated with this function resolver is current.

**See also**
[hasOpenGLFeature](https://doc.qt.io/archives/qt-5.15/qglfunctions.html#hasOpenGLFeature)().

Source: https://doc.qt.io/archives/qt-5.15/qglfunctions.html#openGLFeatures"""
        ...
    BlendColor: Any
    BlendEquation: Any
    BlendEquationSeparate: Any
    BlendFuncSeparate: Any
    BlendSubtract: Any
    Buffers: Any
    CompressedTextures: Any
    Framebuffers: Any
    Multisample: Any
    Multitexture: Any
    NPOTTextures: Any
    OpenGLFeature: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    OpenGLFeatures: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Shaders: Any
    StencilSeparate: Any

class QGLPixelBuffer:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

Rendering into a pbuffer is normally done using full hardware acceleration. This can be
significantly faster than rendering into a
[QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html).

There are three approaches to using this class:

1. **We can draw into the pbuffer and convert it to a [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) using [toImage](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#toImage)().** This is normally much faster than calling [QGLWidget::renderPixmap](https://doc.qt.io/archives/qt-5.15/qglwidget.html#renderPixmap)().
2. **We can draw into the pbuffer and copy the contents into an OpenGL texture using [updateDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#updateDynamicTexture)().** This allows us to create dynamic textures and works on all systems with pbuffer support.
3. **On systems that support it, we can bind the pbuffer to an OpenGL texture.** The texture is then updated automatically when the pbuffer contents change, eliminating the need for additional copy operations. This is supported only on Windows and macOS systems that provide the `render_texture` extension. Note that under Windows, a multi-sampled pbuffer can't be used in conjunction with the `render_texture` extension. If a multi-sampled pbuffer is requested under Windows, the `render_texture` extension is turned off for that pbuffer.

**Note:** This class has been deprecated, use
[QOpenGLFramebufferObject](https://doc.qt.io/archives/qt-5.15/qopenglframebufferobject.html)
for offscreen rendering.

### Threading

As of Qt 4.8, it's possible to render into a QGLPixelBuffer using a
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) in a separate thread. Note
that OpenGL 2.0 or OpenGL ES 2.0 is required for this to work.

Pbuffers are provided by the OpenGL `pbuffer` extension; call hasOpenGLPbuffer() to find
out if the system provides pbuffers.

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def bindTexture(self, image: Any, target: Any) -> int:
        """X.bindTexture(image, target) -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLPixelBuffer::bindTexture(const [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) \\&*image*, GLenum *target* \\= GL\\_TEXTURE\\_2D)

Generates and binds a 2D GL texture to the current context, based on *image*. The
generated texture id is returned and can be used in later glBindTexture() calls.

The *target* parameter specifies the texture target.

Equivalent to calling
[QGLContext::bindTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#bindTexture)().

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#deleteTexture)().

### GLuint QGLPixelBuffer::bindTexture(const [QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html) \\&*pixmap*, GLenum *target* \\= GL\\_TEXTURE\\_2D)

This is an overloaded function.

Generates and binds a 2D GL texture based on *pixmap*.

Equivalent to calling
[QGLContext::bindTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#bindTexture)().

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#deleteTexture)().

### GLuint QGLPixelBuffer::bindTexture(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*fileName*)

This is an overloaded function.

Reads the DirectDrawSurface (DDS) compressed file *fileName* and generates a 2D GL
texture from it.

Equivalent to calling
[QGLContext::bindTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#bindTexture)().

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#deleteTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bindTexture(self, fileName: str) -> int
bindTexture(self, image: PySide2.QtGui.QImage, target: int=...) -> int
bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int=...) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#bindTexture"""
        ...

    def bindToDynamicTexture(self, texture: int) -> bool:
        """X.bindToDynamicTexture(texture) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLPixelBuffer::bindToDynamicTexture(GLuint *texture\\_id*)

Binds the texture specified by *texture\\_id* to this pbuffer. Returns `true` on success;
otherwise returns `false`.

The texture must be of the same size and format as the pbuffer.

To unbind the texture, call
[releaseFromDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#releaseFromDynamicTexture)().
While the texture is bound, it is updated automatically when the pbuffer contents
change, eliminating the need for additional copy operations.

Example:

```
QGLPixelBuffer pbuffer(...);
...
pbuffer.makeCurrent();
GLuint dynamicTexture = pbuffer.generateDynamicTexture();
pbuffer.bindToDynamicTexture(dynamicTexture);
...
pbuffer.releaseFromDynamicTexture();
```

**Warning:** This function uses the `render_texture` extension, which is currently not
supported under X11. An alternative that works on all systems (including X11) is to
manually copy the pbuffer contents to a texture using
[updateDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#updateDynamicTexture)().

**Warning:** For the bindToDynamicTexture() call to succeed on the macOS, the pbuffer
needs a shared context, i.e. the
[QGLPixelBuffer](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html) must be created
with a share widget.

**See also**
[generateDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#generateDynamicTexture)()
and
[releaseFromDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#releaseFromDynamicTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bindToDynamicTexture(self, texture: int) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#bindToDynamicTexture"""
        ...

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """Return the classname of the object"""
        ...

    def colorCount(self) -> int:
        """X.colorCount() -> int"""
        ...

    def context(self) -> Any:
        """X.context() -> PythonQt.QtOpenGL.QGLContext

Supplemental documentation:
Qt 5 reference:

### [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) \\*QGLPixelBuffer::context() const

Returns the context of this pixelbuffer.

Upstream PySide2 reference signatures (binding differences may apply):

```python
context(self) -> PySide2.QtOpenGL.QGLContext
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#context"""
        ...

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Deletes the C++ object (at your own risk, my friend!)"""
        ...

    def deleteTexture(self, texture_id: int) -> None:
        """X.deleteTexture(texture_id)

Supplemental documentation:
Qt 5 reference:

### void QGLPixelBuffer::deleteTexture(GLuint *texture\\_id*)

Removes the texture identified by *texture\\_id* from the texture cache.

Equivalent to calling
[QGLContext::deleteTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#deleteTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
deleteTexture(self, texture_id: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#deleteTexture"""
        ...

    def depth(self) -> int:
        """X.depth() -> int"""
        ...

    def devType(self) -> int:
        """X.devType() -> int

Upstream PySide2 reference signatures (binding differences may apply):

```python
devType(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#devType"""
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

    def doneCurrent(self) -> bool:
        """X.doneCurrent() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLPixelBuffer::doneCurrent()

Makes no context the current OpenGL context. Returns `true` on success; otherwise
returns `false`.

Upstream PySide2 reference signatures (binding differences may apply):

```python
doneCurrent(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#doneCurrent"""
        ...

    def drawTexture(self, point: Any, textureId: int, textureTarget: int) -> None:
        """X.drawTexture(point, textureId, textureTarget)

Supplemental documentation:
Qt 5 reference:

### void QGLPixelBuffer::drawTexture(const [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) \\&*target*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

Draws the given texture, *textureId*, to the given target rectangle, *target*, in OpenGL
model space. The *textureTarget* should be a 2D texture target.

Equivalent to the corresponding
[QGLContext::drawTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#drawTexture)().

This function was introduced in Qt 4.4.

### void QGLPixelBuffer::drawTexture(const [QPointF](https://doc.qt.io/archives/qt-5.15/qpointf.html) \\&*point*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

Draws the given texture, *textureId*, at the given *point* in OpenGL model space. The
textureTarget parameter should be a 2D texture target.

Equivalent to the corresponding
[QGLContext::drawTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#drawTexture)().

This function was introduced in Qt 4.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int=...) -> None
drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#drawTexture"""
        ...

    def format(self) -> Any:
        """X.format() -> PythonQt.QtOpenGL.QGLFormat

Supplemental documentation:
Qt 5 reference:

### [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) QGLPixelBuffer::format() const

Returns the format of the pbuffer. The format may be different from the one that was
requested.

Upstream PySide2 reference signatures (binding differences may apply):

```python
format(self) -> PySide2.QtOpenGL.QGLFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#format"""
        ...

    def generateDynamicTexture(self) -> int:
        """X.generateDynamicTexture() -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLPixelBuffer::generateDynamicTexture() const

Generates and binds a 2D GL texture that is the same size as the pbuffer, and returns
the texture's ID. This can be used in conjunction with
[bindToDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#bindToDynamicTexture)()
and
[updateDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#updateDynamicTexture)().

**See also** [size](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#size)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
generateDynamicTexture(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#generateDynamicTexture"""
        ...

    def handle(self) -> int:
        """X.handle()

Supplemental documentation:
Qt 5 reference:

### [Qt::HANDLE](https://doc.qt.io/archives/qt-5.15/qt.html#HANDLE-typedef) QGLPixelBuffer::handle() const

Returns the native pbuffer handle.

Upstream PySide2 reference signatures (binding differences may apply):

```python
handle(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#handle"""
        ...

    def hasOpenGLPbuffers(self) -> bool:
        """X.hasOpenGLPbuffers() -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLPixelBuffer::hasOpenGLPbuffers()

Returns `true` if the OpenGL `pbuffer` extension is present on this system; otherwise
returns `false`.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOpenGLPbuffers() -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#hasOpenGLPbuffers"""
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

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLPixelBuffer::isValid() const

Returns `true` if this pbuffer is valid; otherwise returns `false`.

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#isValid"""
        ...

    def logicalDpiX(self) -> int:
        """X.logicalDpiX() -> int"""
        ...

    def logicalDpiY(self) -> int:
        """X.logicalDpiY() -> int"""
        ...

    def makeCurrent(self) -> bool:
        """X.makeCurrent() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLPixelBuffer::makeCurrent()

Makes this pbuffer the current OpenGL rendering context. Returns true on success;
otherwise returns `false`.

**See also**
[QGLContext::makeCurrent](https://doc.qt.io/archives/qt-5.15/qglcontext.html#makeCurrent)()
and [doneCurrent](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#doneCurrent)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
makeCurrent(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#makeCurrent"""
        ...

    def metric(self, metric: Any) -> int:
        """X.metric(metric) -> int

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` int QGLPixelBuffer::metric([QPaintDevice::PaintDeviceMetric](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#PaintDeviceMetric-enum) *metric*) const

Reimplements:
[QPaintDevice::metric](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#metric)(QPaintDevice::PaintDeviceMetric
metric) const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#metric"""
        ...

    def paintEngine(self) -> Any:
        """X.paintEngine() -> PythonQt.QtGui.QPaintEngine

Supplemental documentation:
Qt 5 reference:

### `[override virtual]` [QPaintEngine](https://doc.qt.io/archives/qt-5.15/qpaintengine.html) \\*QGLPixelBuffer::paintEngine() const

Reimplements:
[QPaintDevice::paintEngine](https://doc.qt.io/archives/qt-5.15/qpaintdevice.html#paintEngine)()
const.

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintEngine(self) -> PySide2.QtGui.QPaintEngine
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#paintEngine"""
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

    def releaseFromDynamicTexture(self) -> None:
        """X.releaseFromDynamicTexture()

Supplemental documentation:
Qt 5 reference:

### void QGLPixelBuffer::releaseFromDynamicTexture()

Releases the pbuffer from any previously bound texture.

**See also**
[bindToDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#bindToDynamicTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
releaseFromDynamicTexture(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#releaseFromDynamicTexture"""
        ...

    def sharedPainter(self) -> Any:
        """X.sharedPainter() -> PythonQt.QtGui.QPainter"""
        ...

    def size(self) -> Any:
        """X.size() -> PythonQt.QtCore.QSize

Supplemental documentation:
Qt 5 reference:

### [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) QGLPixelBuffer::size() const

Returns the size of the pbuffer.

Upstream PySide2 reference signatures (binding differences may apply):

```python
size(self) -> PySide2.QtCore.QSize
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#size"""
        ...

    def toImage(self) -> Any:
        """X.toImage() -> PythonQt.QtGui.QImage

Supplemental documentation:
Qt 5 reference:

### [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) QGLPixelBuffer::toImage() const

Returns the contents of the pbuffer as a
[QImage](https://doc.qt.io/archives/qt-5.15/qimage.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
toImage(self) -> PySide2.QtGui.QImage
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#toImage"""
        ...

    def updateDynamicTexture(self, texture_id: int) -> None:
        """X.updateDynamicTexture(texture_id)

Supplemental documentation:
Qt 5 reference:

### void QGLPixelBuffer::updateDynamicTexture(GLuint *texture\\_id*) const

Copies the pbuffer contents into the texture specified with *texture\\_id*.

The texture must be of the same size and format as the pbuffer.

Example:

```
QGLPixelBuffer pbuffer(...);
...
pbuffer.makeCurrent();
GLuint dynamicTexture = pbuffer.generateDynamicTexture();
...
pbuffer.updateDynamicTexture(dynamicTexture);
```

An alternative on Windows and macOS systems that support the `render_texture` extension
is to use
[bindToDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#bindToDynamicTexture)()
to get dynamic updates of the texture.

**See also**
[generateDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#generateDynamicTexture)()
and
[bindToDynamicTexture](https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#bindToDynamicTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
updateDynamicTexture(self, texture_id: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglpixelbuffer.html#updateDynamicTexture"""
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

class QGLShader:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

This class supports shaders written in the OpenGL Shading Language (GLSL) and in the
OpenGL/ES Shading Language (GLSL/ES).

QGLShader and
[QGLShaderProgram](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html) shelter the
programmer from the details of compiling and linking vertex and fragment shaders.

**Note:** This class has been deprecated in favor of
[QOpenGLShader](https://doc.qt.io/archives/qt-5.15/qopenglshader.html).

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html"""

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

    def compileSourceCode(self, source: Any) -> bool:
        """X.compileSourceCode(source) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShader::compileSourceCode(const char \\**source*)

Sets the *source* code for this shader and compiles it. Returns `true` if the source was
successfully compiled, false otherwise.

**See also**
[compileSourceFile](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceFile)().

### bool QGLShader::compileSourceCode(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*source*)

This is an overloaded function.

Sets the *source* code for this shader and compiles it. Returns `true` if the source was
successfully compiled, false otherwise.

**See also**
[compileSourceFile](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceFile)().

### bool QGLShader::compileSourceCode(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*source*)

This is an overloaded function.

Sets the *source* code for this shader and compiles it. Returns `true` if the source was
successfully compiled, false otherwise.

**See also**
[compileSourceFile](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceFile)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
compileSourceCode(self, source: PySide2.QtCore.QByteArray) -> bool
compileSourceCode(self, source: str) -> bool
compileSourceCode(self, source: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceCode"""
        ...

    def compileSourceFile(self, fileName: str) -> bool:
        """X.compileSourceFile(fileName) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShader::compileSourceFile(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*fileName*)

Sets the source code for this shader to the contents of *fileName* and compiles it.
Returns `true` if the file could be opened and the source compiled, false otherwise.

**See also**
[compileSourceCode](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceCode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
compileSourceFile(self, fileName: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceFile"""
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
        """Native PythonQt.QtOpenGL.QGLShader.destroyed; argument details are not documented."""
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

    def hasOpenGLShaders(self, type: Any, context: Any) -> bool:
        """X.hasOpenGLShaders(type, context) -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLShader::hasOpenGLShaders([QGLShader::ShaderType](https://doc.qt.io/archives/qt-5.15/qglshader.html#ShaderTypeBit-enum) *type*, const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) \\**context* \\= nullptr)

Returns `true` if shader programs of type *type* are supported on this system; false
otherwise.

The *context* is used to resolve the GLSL extensions. If *context* is `nullptr`, then
[QGLContext::currentContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html#currentContext)()
is used.

This function was introduced in Qt 4.7.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOpenGLShaders(type: PySide2.QtOpenGL.QGLShader.ShaderType, context: typing.Optional[PySide2.QtOpenGL.QGLContext]=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#hasOpenGLShaders"""
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

    def isCompiled(self) -> bool:
        """X.isCompiled() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShader::isCompiled() const

Returns `true` if this shader has been compiled; false otherwise.

**See also**
[compileSourceCode](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceCode)()
and
[compileSourceFile](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceFile)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isCompiled(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#isCompiled"""
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

    def log(self) -> str:
        """X.log() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QGLShader::log() const

Returns the errors and warnings that occurred during the last compile.

**See also**
[compileSourceCode](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceCode)()
and
[compileSourceFile](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceFile)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
log(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#log"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtOpenGL.QGLShader.objectNameChanged; argument details are not documented."""
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

    def shaderId(self) -> int:
        """X.shaderId() -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLShader::shaderId() const

Returns the OpenGL identifier associated with this shader.

**See also**
[QGLShaderProgram::programId](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#programId)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
shaderId(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#shaderId"""
        ...

    def shaderType(self) -> Any:
        """X.shaderType()

Supplemental documentation:
Qt 5 reference:

### [QGLShader::ShaderType](https://doc.qt.io/archives/qt-5.15/qglshader.html#ShaderTypeBit-enum) QGLShader::shaderType() const

Returns the type of this shader.

Upstream PySide2 reference signatures (binding differences may apply):

```python
shaderType(self) -> PySide2.QtOpenGL.QGLShader.ShaderType
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#shaderType"""
        ...

    def signalsBlocked(self) -> bool:
        """X.signalsBlocked() -> bool"""
        ...

    def sourceCode(self) -> Any:
        """X.sourceCode() -> PythonQt.QtCore.QByteArray

Supplemental documentation:
Qt 5 reference:

### [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) QGLShader::sourceCode() const

Returns the source code for this shader.

**See also**
[compileSourceCode](https://doc.qt.io/archives/qt-5.15/qglshader.html#compileSourceCode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
sourceCode(self) -> PySide2.QtCore.QByteArray
```

Source: https://doc.qt.io/archives/qt-5.15/qglshader.html#sourceCode"""
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
    Fragment: Any
    Geometry: Any
    ShaderType: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    ShaderTypeBit: type
    "int([x]) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    Vertex: Any
    objectName: Any

class QGLShaderProgram:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

### Introduction

This class supports shader programs written in the OpenGL Shading Language (GLSL) and in
the OpenGL/ES Shading Language (GLSL/ES).

[QGLShader](https://doc.qt.io/archives/qt-5.15/qglshader.html) and QGLShaderProgram
shelter the programmer from the details of compiling and linking vertex and fragment
shaders.

The following example creates a vertex shader program using the supplied source `code`.
Once compiled and linked, the shader program is activated in the current
[QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) by calling
[QGLShaderProgram::bind](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#bind)():

```
QGLShader shader(QGLShader::Vertex);
shader.compileSourceCode(code);

QGLShaderProgram program(context);
program.addShader(shader);
program.link();

program.bind();
```

### Writing Portable Shaders

Shader programs can be difficult to reuse across OpenGL implementations because of
varying levels of support for standard vertex attributes and uniform variables. In
particular, GLSL/ES lacks all of the standard variables that are present on desktop
OpenGL systems: `gl_Vertex`, `gl_Normal`, `gl_Color`, and so on. Desktop OpenGL lacks
the variable qualifiers `highp`, `mediump`, and `lowp`.

The QGLShaderProgram class makes the process of writing portable shaders easier by
prefixing all shader programs with the following lines on desktop OpenGL:

```
#define highp
#define mediump
#define lowp
```

This makes it possible to run most GLSL/ES shader programs on desktop systems. The
programmer should restrict themselves to just features that are present in GLSL/ES, and
avoid standard variable names that only work on the desktop.

### Simple Shader Example

```
program.addShaderFromSourceCode(QGLShader::Vertex,
    "attribute highp vec4 vertex;\\n"
    "uniform highp mat4 matrix;\\n"
    "void main(void)\\n"
    "{\\n"
    "   gl_Position = matrix * vertex;\\n"
    "}");
program.addShaderFromSourceCode(QGLShader::Fragment,
    "uniform mediump vec4 color;\\n"
    "void main(void)\\n"
    "{\\n"
    "   gl_FragColor = color;\\n"
    "}");
program.link();
program.bind();

int vertexLocation = program.attributeLocation("vertex");
int matrixLocation = program.uniformLocation("matrix");
int colorLocation = program.uniformLocation("color");
```

With the above shader program active, we can draw a green triangle as follows:

```
static GLfloat const triangleVertices[] = {
    60.0f,  10.0f,  0.0f,
    110.0f, 110.0f, 0.0f,
    10.0f,  110.0f, 0.0f
};

QColor color(0, 255, 0, 255);

QMatrix4x4 pmvMatrix;
pmvMatrix.ortho(rect());

program.enableAttributeArray(vertexLocation);
program.setAttributeArray(vertexLocation, triangleVertices, 3);
program.setUniformValue(matrixLocation, pmvMatrix);
program.setUniformValue(colorLocation, color);

glDrawArrays(GL_TRIANGLES, 0, 3);

program.disableAttributeArray(vertexLocation);
```

### Binary Shaders and Programs

Binary shaders may be specified using `glShaderBinary()` on the return value from
[QGLShader::shaderId](https://doc.qt.io/archives/qt-5.15/qglshader.html#shaderId)(). The
[QGLShader](https://doc.qt.io/archives/qt-5.15/qglshader.html) instance containing the
binary can then be added to the shader program with
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)() and
linked in the usual fashion with
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)().

Binary programs may be specified using `glProgramBinaryOES()` on the return value from
[programId](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#programId)(). Then
the application should call
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)(), which will
notice that the program has already been specified and linked, allowing other operations
to be performed on the shader program.

**Note:** This class has been deprecated in favor of
[QOpenGLShaderProgram](https://doc.qt.io/archives/qt-5.15/qopenglshaderprogram.html).

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def addShader(self, shader: Any) -> bool:
        """X.addShader(shader) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShaderProgram::addShader([QGLShader](https://doc.qt.io/archives/qt-5.15/qglshader.html) \\**shader*)

Adds a compiled *shader* to this shader program. Returns `true` if the shader could be
added, or false otherwise.

Ownership of the *shader* object remains with the caller. It will not be deleted when
this [QGLShaderProgram](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html)
instance is deleted. This allows the caller to add the same shader to multiple shader
programs.

**See also**
[addShaderFromSourceCode](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceCode)(),
[addShaderFromSourceFile](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceFile)(),
[removeShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeShader)(),
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)(), and
[removeAllShaders](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeAllShaders)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
addShader(self, shader: PySide2.QtOpenGL.QGLShader) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader"""
        ...

    def addShaderFromSourceCode(self, type: Any, source: Any) -> bool:
        """X.addShaderFromSourceCode(type, source) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShaderProgram::addShaderFromSourceCode([QGLShader::ShaderType](https://doc.qt.io/archives/qt-5.15/qglshader.html#ShaderTypeBit-enum) *type*, const char \\**source*)

Compiles *source* as a shader of the specified *type* and adds it to this shader
program. Returns `true` if compilation was successful, false otherwise. The compilation
errors and warnings will be made available via
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)().

This function is intended to be a short-cut for quickly adding vertex and fragment
shaders to a shader program without creating an instance of QGLShader first.

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)(),
[addShaderFromSourceFile](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceFile)(),
[removeShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeShader)(),
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)(),
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)(), and
[removeAllShaders](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeAllShaders)().

### bool QGLShaderProgram::addShaderFromSourceCode([QGLShader::ShaderType](https://doc.qt.io/archives/qt-5.15/qglshader.html#ShaderTypeBit-enum) *type*, const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*source*)

This is an overloaded function.

Compiles *source* as a shader of the specified *type* and adds it to this shader
program. Returns `true` if compilation was successful, false otherwise. The compilation
errors and warnings will be made available via
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)().

This function is intended to be a short-cut for quickly adding vertex and fragment
shaders to a shader program without creating an instance of QGLShader first.

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)(),
[addShaderFromSourceFile](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceFile)(),
[removeShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeShader)(),
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)(),
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)(), and
[removeAllShaders](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeAllShaders)().

### bool QGLShaderProgram::addShaderFromSourceCode([QGLShader::ShaderType](https://doc.qt.io/archives/qt-5.15/qglshader.html#ShaderTypeBit-enum) *type*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*source*)

This is an overloaded function.

Compiles *source* as a shader of the specified *type* and adds it to this shader
program. Returns `true` if compilation was successful, false otherwise. The compilation
errors and warnings will be made available via
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)().

This function is intended to be a short-cut for quickly adding vertex and fragment
shaders to a shader program without creating an instance of QGLShader first.

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)(),
[addShaderFromSourceFile](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceFile)(),
[removeShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeShader)(),
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)(),
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)(), and
[removeAllShaders](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeAllShaders)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
addShaderFromSourceCode(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, source: PySide2.QtCore.QByteArray) -> bool
addShaderFromSourceCode(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, source: str) -> bool
addShaderFromSourceCode(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, source: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceCode"""
        ...

    def addShaderFromSourceFile(self, type: Any, fileName: str) -> bool:
        """X.addShaderFromSourceFile(type, fileName) -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShaderProgram::addShaderFromSourceFile([QGLShader::ShaderType](https://doc.qt.io/archives/qt-5.15/qglshader.html#ShaderTypeBit-enum) *type*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*fileName*)

Compiles the contents of *fileName* as a shader of the specified *type* and adds it to
this shader program. Returns `true` if compilation was successful, false otherwise. The
compilation errors and warnings will be made available via
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)().

This function is intended to be a short-cut for quickly adding vertex and fragment
shaders to a shader program without creating an instance of QGLShader first.

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)() and
[addShaderFromSourceCode](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceCode)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
addShaderFromSourceFile(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, fileName: str) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShaderFromSourceFile"""
        ...

    def attributeLocation(self, name: Any) -> int:
        """X.attributeLocation(name) -> int

Supplemental documentation:
Qt 5 reference:

### int QGLShaderProgram::attributeLocation(const char \\**name*) const

Returns the location of the attribute *name* within this shader program's parameter
list. Returns -1 if *name* is not a valid attribute for this shader program.

**See also**
[uniformLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#uniformLocation)()
and
[bindAttributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#bindAttributeLocation)().

### int QGLShaderProgram::attributeLocation(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*name*) const

This is an overloaded function.

Returns the location of the attribute *name* within this shader program's parameter
list. Returns -1 if *name* is not a valid attribute for this shader program.

**See also**
[uniformLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#uniformLocation)()
and
[bindAttributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#bindAttributeLocation)().

### int QGLShaderProgram::attributeLocation(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*) const

This is an overloaded function.

Returns the location of the attribute *name* within this shader program's parameter
list. Returns -1 if *name* is not a valid attribute for this shader program.

**See also**
[uniformLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#uniformLocation)()
and
[bindAttributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#bindAttributeLocation)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
attributeLocation(self, name: PySide2.QtCore.QByteArray) -> int
attributeLocation(self, name: str) -> int
attributeLocation(self, name: str) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#attributeLocation"""
        ...

    def bind(self) -> bool:
        """X.bind() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShaderProgram::bind()

Binds this shader program to the active QGLContext and makes it the current shader
program. Any previously bound shader program is released. This is equivalent to calling
`glUseProgram()` on
[programId](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#programId)().
Returns `true` if the program was successfully bound; false otherwise. If the shader
program has not yet been linked, or it needs to be re-linked, this function will call
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)().

**See also** [link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)() and
[release](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#release)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bind(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#bind"""
        ...

    def bindAttributeLocation(self, name: Any, location: int) -> None:
        """X.bindAttributeLocation(name, location)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::bindAttributeLocation(const char \\**name*, int *location*)

Binds the attribute *name* to the specified *location*. This function can be called
before or after the program has been linked. Any attributes that have not been
explicitly bound when the program is linked will be assigned locations automatically.

When this function is called after the program has been linked, the program will need to
be relinked for the change to take effect.

**See also**
[attributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#attributeLocation)().

### void QGLShaderProgram::bindAttributeLocation(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*name*, int *location*)

This is an overloaded function.

Binds the attribute *name* to the specified *location*. This function can be called
before or after the program has been linked. Any attributes that have not been
explicitly bound when the program is linked will be assigned locations automatically.

When this function is called after the program has been linked, the program will need to
be relinked for the change to take effect.

**See also**
[attributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#attributeLocation)().

### void QGLShaderProgram::bindAttributeLocation(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*, int *location*)

This is an overloaded function.

Binds the attribute *name* to the specified *location*. This function can be called
before or after the program has been linked. Any attributes that have not been
explicitly bound when the program is linked will be assigned locations automatically.

When this function is called after the program has been linked, the program will need to
be relinked for the change to take effect.

**See also**
[attributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#attributeLocation)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bindAttributeLocation(self, name: PySide2.QtCore.QByteArray, location: int) -> None
bindAttributeLocation(self, name: str, location: int) -> None
bindAttributeLocation(self, name: str, location: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#bindAttributeLocation"""
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
        """Native PythonQt.QtOpenGL.QGLShaderProgram.destroyed; argument details are not documented."""
        ...

    def disableAttributeArray(self, name: Any) -> None:
        """X.disableAttributeArray(name)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::disableAttributeArray(int *location*)

Disables the vertex array at *location* in this shader program that was enabled by a
previous call to
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)().

**See also**
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)(),
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
and
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::disableAttributeArray(const char \\**name*)

This is an overloaded function.

Disables the vertex array called *name* in this shader program that was enabled by a
previous call to
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)().

**See also**
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)(),
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
and
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
disableAttributeArray(self, location: int) -> None
disableAttributeArray(self, name: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray"""
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

    def enableAttributeArray(self, name: Any) -> None:
        """X.enableAttributeArray(name)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::enableAttributeArray(int *location*)

Enables the vertex array at *location* in this shader program so that the value set by
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)()
on *location* will be used by the shader program.

**See also**
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)(),
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)(),
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
and
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::enableAttributeArray(const char \\**name*)

This is an overloaded function.

Enables the vertex array called *name* in this shader program so that the value set by
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)()
on *name* will be used by the shader program.

**See also**
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)(),
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)(),
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
and
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
enableAttributeArray(self, location: int) -> None
enableAttributeArray(self, name: str) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray"""
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

    def geometryInputType(self) -> int:
        """X.geometryInputType() -> int

Supplemental documentation:
Qt 5 reference:

### GLenum QGLShaderProgram::geometryInputType() const

Returns the geometry shader input type, if active.

This parameter takes effect the next time the program is linked.

This function was introduced in Qt 4.7.

**See also**
[setGeometryInputType](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setGeometryInputType)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
geometryInputType(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#geometryInputType"""
        ...

    def geometryOutputType(self) -> int:
        """X.geometryOutputType() -> int

Supplemental documentation:
Qt 5 reference:

### GLenum QGLShaderProgram::geometryOutputType() const

Returns the geometry shader output type, if active.

This parameter takes effect the next time the program is linked.

This function was introduced in Qt 4.7.

**See also**
[setGeometryOutputType](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setGeometryOutputType)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
geometryOutputType(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#geometryOutputType"""
        ...

    def geometryOutputVertexCount(self) -> int:
        """X.geometryOutputVertexCount() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLShaderProgram::geometryOutputVertexCount() const

Returns the maximum number of vertices the current geometry shader program will produce,
if active.

This parameter takes effect the ntext time the program is linked.

This function was introduced in Qt 4.7.

**See also**
[setGeometryOutputVertexCount](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setGeometryOutputVertexCount)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
geometryOutputVertexCount(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#geometryOutputVertexCount"""
        ...

    def hasOpenGLShaderPrograms(self, context: Any) -> bool:
        """X.hasOpenGLShaderPrograms(context) -> bool

Supplemental documentation:
Qt 5 reference:

### `[static]` bool QGLShaderProgram::hasOpenGLShaderPrograms(const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) \\**context* \\= nullptr)

Returns `true` if shader programs written in the OpenGL Shading Language (GLSL) are
supported on this system; false otherwise.

The *context* is used to resolve the GLSL extensions. If *context* is `nullptr`, then
[QGLContext::currentContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html#currentContext)()
is used.

Upstream PySide2 reference signatures (binding differences may apply):

```python
hasOpenGLShaderPrograms(context: typing.Optional[PySide2.QtOpenGL.QGLContext]=...) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#hasOpenGLShaderPrograms"""
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

    def isLinked(self) -> bool:
        """X.isLinked() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLShaderProgram::isLinked() const

Returns `true` if this shader program has been linked; false otherwise.

**See also** [link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isLinked(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#isLinked"""
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

    def link(self) -> bool:
        """X.link() -> bool

Supplemental documentation:
Qt 5 reference:

### `[virtual]` bool QGLShaderProgram::link()

Links together the shaders that were added to this program with
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)().
Returns `true` if the link was successful or false otherwise. If the link failed, the
error messages can be retrieved with
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)().

Subclasses can override this function to initialize attributes and uniform variables for
use in specific shader programs.

If the shader program was already linked, calling this function again will force it to
be re-linked.

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)() and
[log](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
link(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link"""
        ...

    def log(self) -> str:
        """X.log() -> str

Supplemental documentation:
Qt 5 reference:

### [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) QGLShaderProgram::log() const

Returns the errors and warnings that occurred during the last
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)() or
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)() with
explicitly specified source code.

**See also** [link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
log(self) -> str
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#log"""
        ...

    def maxGeometryOutputVertices(self) -> int:
        """X.maxGeometryOutputVertices() -> int

Supplemental documentation:
Qt 5 reference:

### int QGLShaderProgram::maxGeometryOutputVertices() const

Returns the hardware limit for how many vertices a geometry shader can output.

This function was introduced in Qt 4.7.

**See also**
[setGeometryOutputVertexCount](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setGeometryOutputVertexCount)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
maxGeometryOutputVertices(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#maxGeometryOutputVertices"""
        ...

    def metaObject(self) -> Any:
        """X.metaObject() -> PythonQt.QtCore.QMetaObject"""
        ...

    def moveToThread(self, thread: Any) -> Any:
        """X.moveToThread(thread)"""
        ...

    def objectNameChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtOpenGL.QGLShaderProgram.objectNameChanged; argument details are not documented."""
        ...

    def parent(self) -> Any:
        """X.parent() -> PythonQt.private.QObject"""
        ...

    def programId(self) -> int:
        """X.programId() -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLShaderProgram::programId() const

Returns the OpenGL identifier associated with this shader program.

**See also**
[QGLShader::shaderId](https://doc.qt.io/archives/qt-5.15/qglshader.html#shaderId)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
programId(self) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#programId"""
        ...

    def property(self, name: Any) -> Any:
        """X.property(name) -> object"""
        ...

    def release(self) -> None:
        """X.release()

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::release()

Releases the active shader program from the current QGLContext. This is equivalent to
calling `glUseProgram(0)`.

**See also** [bind](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#bind)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
release(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#release"""
        ...

    def removeAllShaders(self) -> None:
        """X.removeAllShaders()

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::removeAllShaders()

Removes all of the shaders that were added to this program previously. The QGLShader
objects for the shaders will not be deleted if they were constructed externally.
QGLShader objects that are constructed internally by
[QGLShaderProgram](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html) will be
deleted.

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)() and
[removeShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeShader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
removeAllShaders(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeAllShaders"""
        ...

    def removeEventFilter(self, obj: Any) -> Any:
        """X.removeEventFilter(obj)"""
        ...

    def removeShader(self, shader: Any) -> None:
        """X.removeShader(shader)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::removeShader([QGLShader](https://doc.qt.io/archives/qt-5.15/qglshader.html) \\**shader*)

Removes *shader* from this shader program. The object is not deleted.

The shader program must be valid in the current QGLContext.

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)(),
[link](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#link)(), and
[removeAllShaders](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeAllShaders)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
removeShader(self, shader: PySide2.QtOpenGL.QGLShader) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeShader"""
        ...

    def sender(self) -> Any:
        """X.sender() -> PythonQt.private.QObject"""
        ...

    def senderSignalIndex(self) -> int:
        """X.senderSignalIndex() -> int"""
        ...

    def setAttributeArray(self, name: Any, type: Any, values: Any, tupleSize: Any, stride: Any) -> Any:
        """X.setAttributeArray(name, type, values, tupleSize, stride)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setAttributeArray(int *location*, const GLfloat \\**values*, int *tupleSize*, int *stride* \\= 0\\)

Sets an array of vertex *values* on the attribute at *location* in this shader program.
The *tupleSize* indicates the number of components per vertex (1, 2, 3, or 4), and the
*stride* indicates the number of bytes between vertices. A default *stride* value of
zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *location*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *location* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(int *location*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\**values*, int *stride* \\= 0\\)

Sets an array of 2D vertex *values* on the attribute at *location* in this shader
program. The *stride* indicates the number of bytes between vertices. A default *stride*
value of zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *location*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *location* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(int *location*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\**values*, int *stride* \\= 0\\)

Sets an array of 3D vertex *values* on the attribute at *location* in this shader
program. The *stride* indicates the number of bytes between vertices. A default *stride*
value of zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *location*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *location* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(int *location*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\**values*, int *stride* \\= 0\\)

Sets an array of 4D vertex *values* on the attribute at *location* in this shader
program. The *stride* indicates the number of bytes between vertices. A default *stride*
value of zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *location*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *location* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(int *location*, GLenum *type*, const void \\**values*, int *tupleSize*, int *stride* \\= 0\\)

Sets an array of vertex *values* on the attribute at *location* in this shader program.
The *stride* indicates the number of bytes between vertices. A default *stride* value of
zero indicates that the vertices are densely packed in *values*.

The *type* indicates the type of elements in the *values* array, usually `GL_FLOAT`,
`GL_UNSIGNED_BYTE`, etc. The *tupleSize* indicates the number of components per vertex:
1, 2, 3, or 4\\.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *location*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *location* will be used.

The
[setAttributeBuffer](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeBuffer)()
function can be used to set the attribute array to an offset within a vertex buffer.

**Note:** Normalization will be enabled. If this is not desired, call
glVertexAttribPointer directly through QGLFunctions.

This function was introduced in Qt 4.7.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)(),
and
[setAttributeBuffer](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeBuffer)().

### void QGLShaderProgram::setAttributeArray(const char \\**name*, const GLfloat \\**values*, int *tupleSize*, int *stride* \\= 0\\)

This is an overloaded function.

Sets an array of vertex *values* on the attribute called *name* in this shader program.
The *tupleSize* indicates the number of components per vertex (1, 2, 3, or 4), and the
*stride* indicates the number of bytes between vertices. A default *stride* value of
zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on *name*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *name* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(const char \\**name*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\**values*, int *stride* \\= 0\\)

This is an overloaded function.

Sets an array of 2D vertex *values* on the attribute called *name* in this shader
program. The *stride* indicates the number of bytes between vertices. A default *stride*
value of zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on *name*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *name* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(const char \\**name*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\**values*, int *stride* \\= 0\\)

This is an overloaded function.

Sets an array of 3D vertex *values* on the attribute called *name* in this shader
program. The *stride* indicates the number of bytes between vertices. A default *stride*
value of zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on *name*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *name* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(const char \\**name*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\**values*, int *stride* \\= 0\\)

This is an overloaded function.

Sets an array of 4D vertex *values* on the attribute called *name* in this shader
program. The *stride* indicates the number of bytes between vertices. A default *stride*
value of zero indicates that the vertices are densely packed in *values*.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on *name*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *name* will be used.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
and
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)().

### void QGLShaderProgram::setAttributeArray(const char \\**name*, GLenum *type*, const void \\**values*, int *tupleSize*, int *stride* \\= 0\\)

This is an overloaded function.

Sets an array of vertex *values* on the attribute called *name* in this shader program.
The *stride* indicates the number of bytes between vertices. A default *stride* value of
zero indicates that the vertices are densely packed in *values*.

The *type* indicates the type of elements in the *values* array, usually `GL_FLOAT`,
`GL_UNSIGNED_BYTE`, etc. The *tupleSize* indicates the number of components per vertex:
1, 2, 3, or 4\\.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *name*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *name* will be used.

The
[setAttributeBuffer](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeBuffer)()
function can be used to set the attribute array to an offset within a vertex buffer.

This function was introduced in Qt 4.7.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)(),
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)(),
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)(),
[disableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#disableAttributeArray)(),
and
[setAttributeBuffer](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeBuffer)().

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray"""
        ...

    def setAttributeBuffer(self, name: Any, type: int, offset: int, tupleSize: int, stride: int) -> None:
        """X.setAttributeBuffer(name, type, offset, tupleSize, stride)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setAttributeBuffer(int *location*, GLenum *type*, int *offset*, int *tupleSize*, int *stride* \\= 0\\)

Sets an array of vertex values on the attribute at *location* in this shader program,
starting at a specific *offset* in the currently bound vertex buffer. The *stride*
indicates the number of bytes between vertices. A default *stride* value of zero
indicates that the vertices are densely packed in the value array.

The *type* indicates the type of elements in the vertex value array, usually `GL_FLOAT`,
`GL_UNSIGNED_BYTE`, etc. The *tupleSize* indicates the number of components per vertex:
1, 2, 3, or 4\\.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *location*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *location* will be used.

**Note:** Normalization will be enabled. If this is not desired, call
glVertexAttribPointer directly though QGLFunctions.

This function was introduced in Qt 4.7.

**See also**
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)().

### void QGLShaderProgram::setAttributeBuffer(const char \\**name*, GLenum *type*, int *offset*, int *tupleSize*, int *stride* \\= 0\\)

This is an overloaded function.

Sets an array of vertex values on the attribute called *name* in this shader program,
starting at a specific *offset* in the currently bound vertex buffer. The *stride*
indicates the number of bytes between vertices. A default *stride* value of zero
indicates that the vertices are densely packed in the value array.

The *type* indicates the type of elements in the vertex value array, usually `GL_FLOAT`,
`GL_UNSIGNED_BYTE`, etc. The *tupleSize* indicates the number of components per vertex:
1, 2, 3, or 4\\.

The array will become active when
[enableAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#enableAttributeArray)()
is called on the *name*. Otherwise the value specified with
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)()
for *name* will be used.

This function was introduced in Qt 4.7.

**See also**
[setAttributeArray](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeArray)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAttributeBuffer(self, location: int, type: int, offset: int, tupleSize: int, stride: int=...) -> None
setAttributeBuffer(self, name: str, type: int, offset: int, tupleSize: int, stride: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeBuffer"""
        ...

    def setAttributeValue(self, name: Any, x: Any, y: Any, z: Any, w: Any) -> None:
        """X.setAttributeValue(name, x, y, z, w)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setAttributeValue(int *location*, GLfloat *value*)

Sets the attribute at *location* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, GLfloat *x*, GLfloat *y*)

Sets the attribute at *location* in the current context to the 2D vector (*x*, *y*).

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

Sets the attribute at *location* in the current context to the 3D vector (*x*, *y*,
*z*).

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

Sets the attribute at *location* in the current context to the 4D vector (*x*, *y*, *z*,
*w*).

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\&*value*)

Sets the attribute at *location* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\&*value*)

Sets the attribute at *location* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\&*value*)

Sets the attribute at *location* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, const [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) \\&*value*)

Sets the attribute at *location* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(int *location*, const GLfloat \\**values*, int *columns*, int *rows*)

Sets the attribute at *location* in the current context to the contents of *values*,
which contains *columns* elements, each consisting of *rows* elements. The *rows* value
should be 1, 2, 3, or 4\\. This function is typically used to set matrix values and
column vectors.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, GLfloat *value*)

This is an overloaded function.

Sets the attribute called *name* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, GLfloat *x*, GLfloat *y*)

This is an overloaded function.

Sets the attribute called *name* in the current context to the 2D vector (*x*, *y*).

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

This is an overloaded function.

Sets the attribute called *name* in the current context to the 3D vector (*x*, *y*,
*z*).

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

This is an overloaded function.

Sets the attribute called *name* in the current context to the 4D vector (*x*, *y*, *z*,
*w*).

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\&*value*)

This is an overloaded function.

Sets the attribute called *name* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\&*value*)

This is an overloaded function.

Sets the attribute called *name* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\&*value*)

This is an overloaded function.

Sets the attribute called *name* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, const [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) \\&*value*)

This is an overloaded function.

Sets the attribute called *name* in the current context to *value*.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

### void QGLShaderProgram::setAttributeValue(const char \\**name*, const GLfloat \\**values*, int *columns*, int *rows*)

This is an overloaded function.

Sets the attribute called *name* in the current context to the contents of *values*,
which contains *columns* elements, each consisting of *rows* elements. The *rows* value
should be 1, 2, 3, or 4\\. This function is typically used to set matrix values and
column vectors.

**See also**
[setUniformValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAttributeValue(self, location: int, value: float) -> None
setAttributeValue(self, location: int, value: PySide2.QtGui.QColor) -> None
setAttributeValue(self, location: int, value: PySide2.QtGui.QVector2D) -> None
setAttributeValue(self, location: int, value: PySide2.QtGui.QVector3D) -> None
setAttributeValue(self, location: int, value: PySide2.QtGui.QVector4D) -> None
setAttributeValue(self, location: int, x: float, y: float) -> None
setAttributeValue(self, location: int, x: float, y: float, z: float) -> None
setAttributeValue(self, location: int, x: float, y: float, z: float, w: float) -> None
setAttributeValue(self, name: str, value: float) -> None
setAttributeValue(self, name: str, value: PySide2.QtGui.QColor) -> None
setAttributeValue(self, name: str, value: PySide2.QtGui.QVector2D) -> None
setAttributeValue(self, name: str, value: PySide2.QtGui.QVector3D) -> None
setAttributeValue(self, name: str, value: PySide2.QtGui.QVector4D) -> None
setAttributeValue(self, name: str, x: float, y: float) -> None
setAttributeValue(self, name: str, x: float, y: float, z: float) -> None
setAttributeValue(self, name: str, x: float, y: float, z: float, w: float) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue"""
        ...

    def setGeometryInputType(self, inputType: int) -> None:
        """X.setGeometryInputType(inputType)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setGeometryInputType(GLenum *inputType*)

Sets the input type from *inputType*.

This parameter takes effect the next time the program is linked.

**See also**
[geometryInputType](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#geometryInputType)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setGeometryInputType(self, inputType: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setGeometryInputType"""
        ...

    def setGeometryOutputType(self, outputType: int) -> None:
        """X.setGeometryOutputType(outputType)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setGeometryOutputType(GLenum *outputType*)

Sets the output type from the geometry shader, if active, to *outputType*.

This parameter takes effect the next time the program is linked.

This function was introduced in Qt 4.7.

**See also**
[geometryOutputType](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#geometryOutputType)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setGeometryOutputType(self, outputType: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setGeometryOutputType"""
        ...

    def setGeometryOutputVertexCount(self, count: int) -> None:
        """X.setGeometryOutputVertexCount(count)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setGeometryOutputVertexCount(int *count*)

Sets the maximum number of vertices the current geometry shader program will produce, if
active, to *count*.

This parameter takes effect the next time the program is linked.

This function was introduced in Qt 4.7.

**See also**
[geometryOutputVertexCount](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#geometryOutputVertexCount)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setGeometryOutputVertexCount(self, count: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setGeometryOutputVertexCount"""
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

    def setUniformValue(self, name: Any, x: Any, y: Any, z: Any, w: Any) -> None:
        """X.setUniformValue(name, x, y, z, w)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setUniformValue(int *location*, GLfloat *value*)

Sets the uniform variable at *location* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, GLint *value*)

Sets the uniform variable at *location* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) \\&*color*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to the red, green, blue,
and alpha components of *color*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QPoint](https://doc.qt.io/archives/qt-5.15/qpoint.html) \\&*point*)

This is an overloaded function.

Sets the uniform variable associated with *name* in the current context to the x and y
coordinates of *point*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QPointF](https://doc.qt.io/archives/qt-5.15/qpointf.html) \\&*point*)

This is an overloaded function.

Sets the uniform variable associated with *name* in the current context to the x and y
coordinates of *point*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) \\&*size*)

This is an overloaded function.

Sets the uniform variable associated with *name* in the current context to the width and
height of the given *size*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QSizeF](https://doc.qt.io/archives/qt-5.15/qsizef.html) \\&*size*)

This is an overloaded function.

Sets the uniform variable associated with *name* in the current context to the width and
height of the given *size*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix2x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x2-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 2x2 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix2x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x3-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 2x3 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix2x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x4-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 2x4 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix3x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x2-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 3x2 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix3x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x3-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 3x3 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix3x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x4-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 3x4 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix4x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x2-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 4x2 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix4x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x3-typedef) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 4x3 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QMatrix4x4](https://doc.qt.io/archives/qt-5.15/qmatrix4x4.html) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 4x4 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const GLfloat \\[2\\]\\[2\\] *value* \\= 2\\)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 2x2 matrix *value*.
The matrix elements must be specified in column-major order.

This function was introduced in Qt 4.7.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const GLfloat \\[3\\]\\[3\\] *value* \\= 3\\)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 3x3 matrix *value*.
The matrix elements must be specified in column-major order.

This function was introduced in Qt 4.7.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const GLfloat \\[4\\]\\[4\\] *value* \\= 4\\)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 4x4 matrix *value*.
The matrix elements must be specified in column-major order.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QTransform](https://doc.qt.io/archives/qt-5.15/qtransform.html) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to a 3x3 transformation
matrix *value* that is specified as a
[QTransform](https://doc.qt.io/archives/qt-5.15/qtransform.html) value.

To set a [QTransform](https://doc.qt.io/archives/qt-5.15/qtransform.html) value as a 4x4
matrix in a shader, use `setUniformValue(name, QMatrix4x4(value))`.

### void QGLShaderProgram::setUniformValue(int *location*, GLuint *value*)

Sets the uniform variable at *location* in the current context to *value*. This function
should be used when setting sampler values.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, GLfloat *x*, GLfloat *y*)

Sets the uniform variable at *location* in the current context to the 2D vector (*x*,
*y*).

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

Sets the uniform variable at *location* in the current context to the 3D vector (*x*,
*y*, *z*).

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

Sets the uniform variable at *location* in the current context to the 4D vector (*x*,
*y*, *z*, *w*).

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\&*value*)

Sets the uniform variable at *location* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\&*value*)

Sets the uniform variable at *location* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\&*value*)

Sets the uniform variable at *location* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) \\&*color*)

Sets the uniform variable at *location* in the current context to the red, green, blue,
and alpha components of *color*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QPoint](https://doc.qt.io/archives/qt-5.15/qpoint.html) \\&*point*)

Sets the uniform variable at *location* in the current context to the x and y
coordinates of *point*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QPointF](https://doc.qt.io/archives/qt-5.15/qpointf.html) \\&*point*)

Sets the uniform variable at *location* in the current context to the x and y
coordinates of *point*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QSize](https://doc.qt.io/archives/qt-5.15/qsize.html) \\&*size*)

Sets the uniform variable at *location* in the current context to the width and height
of the given *size*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QSizeF](https://doc.qt.io/archives/qt-5.15/qsizef.html) \\&*size*)

Sets the uniform variable at *location* in the current context to the width and height
of the given *size*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix2x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x2-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 2x2 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix2x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x3-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 2x3 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix2x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x4-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 2x4 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix3x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x2-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 3x2 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix3x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x3-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 3x3 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix3x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x4-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 3x4 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix4x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x2-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 4x2 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix4x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x3-typedef) \\&*value*)

Sets the uniform variable at *location* in the current context to a 4x3 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QMatrix4x4](https://doc.qt.io/archives/qt-5.15/qmatrix4x4.html) \\&*value*)

Sets the uniform variable at *location* in the current context to a 4x4 matrix *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const GLfloat \\[2\\]\\[2\\] *value* \\= 2\\)

This is an overloaded function.

Sets the uniform variable at *location* in the current context to a 2x2 matrix *value*.
The matrix elements must be specified in column-major order.

This function was introduced in Qt 4.7.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const GLfloat \\[3\\]\\[3\\] *value* \\= 3\\)

This is an overloaded function.

Sets the uniform variable at *location* in the current context to a 3x3 matrix *value*.
The matrix elements must be specified in column-major order.

This function was introduced in Qt 4.7.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const GLfloat \\[4\\]\\[4\\] *value* \\= 4\\)

This is an overloaded function.

Sets the uniform variable at *location* in the current context to a 4x4 matrix *value*.
The matrix elements must be specified in column-major order.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(int *location*, const [QTransform](https://doc.qt.io/archives/qt-5.15/qtransform.html) \\&*value*)

Sets the uniform variable at *location* in the current context to a 3x3 transformation
matrix *value* that is specified as a
[QTransform](https://doc.qt.io/archives/qt-5.15/qtransform.html) value.

To set a [QTransform](https://doc.qt.io/archives/qt-5.15/qtransform.html) value as a 4x4
matrix in a shader, use `setUniformValue(location, QMatrix4x4(value))`.

### void QGLShaderProgram::setUniformValue(const char \\**name*, GLfloat *value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, GLint *value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, GLuint *value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to *value*. This function
should be used when setting sampler values.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, GLfloat *x*, GLfloat *y*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to the 2D vector (*x*,
*y*).

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, GLfloat *x*, GLfloat *y*, GLfloat *z*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to the 3D vector (*x*,
*y*, *z*).

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, GLfloat *x*, GLfloat *y*, GLfloat *z*, GLfloat *w*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to the 4D vector (*x*,
*y*, *z*, *w*).

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValue(const char \\**name*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\&*value*)

This is an overloaded function.

Sets the uniform variable called *name* in the current context to *value*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setUniformValue(self, location: int, color: PySide2.QtGui.QColor) -> None
setUniformValue(self, location: int, point: PySide2.QtCore.QPoint) -> None
setUniformValue(self, location: int, point: PySide2.QtCore.QPointF) -> None
setUniformValue(self, location: int, size: PySide2.QtCore.QSize) -> None
setUniformValue(self, location: int, size: PySide2.QtCore.QSizeF) -> None
setUniformValue(self, location: int, value: float) -> None
setUniformValue(self, location: int, value: int) -> None
setUniformValue(self, location: int, value: int) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x2) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x3) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x4) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x2) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x3) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x4) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x2) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x3) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x4) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QTransform) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QVector2D) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QVector3D) -> None
setUniformValue(self, location: int, value: PySide2.QtGui.QVector4D) -> None
setUniformValue(self, location: int, x: float, y: float) -> None
setUniformValue(self, location: int, x: float, y: float, z: float) -> None
setUniformValue(self, location: int, x: float, y: float, z: float, w: float) -> None
setUniformValue(self, name: str, color: PySide2.QtGui.QColor) -> None
setUniformValue(self, name: str, point: PySide2.QtCore.QPoint) -> None
setUniformValue(self, name: str, point: PySide2.QtCore.QPointF) -> None
setUniformValue(self, name: str, size: PySide2.QtCore.QSize) -> None
setUniformValue(self, name: str, size: PySide2.QtCore.QSizeF) -> None
setUniformValue(self, name: str, value: float) -> None
setUniformValue(self, name: str, value: int) -> None
setUniformValue(self, name: str, value: int) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix2x2) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix2x3) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix2x4) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix3x2) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix3x3) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix3x4) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix4x2) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix4x3) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QMatrix4x4) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QTransform) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QVector2D) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QVector3D) -> None
setUniformValue(self, name: str, value: PySide2.QtGui.QVector4D) -> None
setUniformValue(self, name: str, x: float, y: float) -> None
setUniformValue(self, name: str, x: float, y: float, z: float) -> None
setUniformValue(self, name: str, x: float, y: float, z: float, w: float) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValue"""
        ...

    def setUniformValueArray(self, name: Any, values: Any, count: Any, tupleSize: Any) -> Any:
        """X.setUniformValueArray(name, values, count, tupleSize)

Supplemental documentation:
Qt 5 reference:

### void QGLShaderProgram::setUniformValueArray(int *location*, const GLfloat \\**values*, int *count*, int *tupleSize*)

Sets the uniform variable array at *location* in the current context to the *count*
elements of *values*. Each element has *tupleSize* components. The *tupleSize* must be
1, 2, 3, or 4\\.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const GLint \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count*
elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const GLuint \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count*
elements of *values*. This overload should be used when setting an array of sampler
values.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 2D
vector elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 3D
vector elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 4D
vector elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix2x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x2-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 2x2
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix2x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x3-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 2x3
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix2x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x4-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 2x4
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix3x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x2-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 3x2
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix3x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x3-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 3x3
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix3x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x4-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 3x4
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix4x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x2-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 4x2
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix4x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x3-typedef) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 4x3
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(int *location*, const [QMatrix4x4](https://doc.qt.io/archives/qt-5.15/qmatrix4x4.html) \\**values*, int *count*)

Sets the uniform variable array at *location* in the current context to the *count* 4x4
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const GLfloat \\**values*, int *count*, int *tupleSize*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count*
elements of *values*. Each element has *tupleSize* components. The *tupleSize* must be
1, 2, 3, or 4\\.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const GLint \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count*
elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const GLuint \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count*
elements of *values*. This overload should be used when setting an array of sampler
values.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QVector2D](https://doc.qt.io/archives/qt-5.15/qvector2d.html) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 2D
vector elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QVector3D](https://doc.qt.io/archives/qt-5.15/qvector3d.html) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 3D
vector elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QVector4D](https://doc.qt.io/archives/qt-5.15/qvector4d.html) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 4D
vector elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix2x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x2-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 2x2
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix2x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x3-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 2x3
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix2x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix2x4-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 2x4
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix3x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x2-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 3x2
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix3x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x3-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 3x3
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix3x4](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix3x4-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 3x4
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix4x2](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x2-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 4x2
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix4x3](https://doc.qt.io/archives/qt-5.15/qgenericmatrix.html#QMatrix4x3-typedef) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 4x3
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

### void QGLShaderProgram::setUniformValueArray(const char \\**name*, const [QMatrix4x4](https://doc.qt.io/archives/qt-5.15/qmatrix4x4.html) \\**values*, int *count*)

This is an overloaded function.

Sets the uniform variable array called *name* in the current context to the *count* 4x4
matrix elements of *values*.

**See also**
[setAttributeValue](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setAttributeValue)().

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#setUniformValueArray"""
        ...

    def shaders(self) -> tuple:
        """X.shaders() -> tuple

Supplemental documentation:
Qt 5 reference:

### [QList](https://doc.qt.io/archives/qt-5.15/qlist.html)\\<[QGLShader](https://doc.qt.io/archives/qt-5.15/qglshader.html) \\*\\> QGLShaderProgram::shaders() const

Returns a list of all shaders that have been added to this shader program using
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)().

**See also**
[addShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#addShader)() and
[removeShader](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#removeShader)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
shaders(self) -> typing.List[PySide2.QtOpenGL.QGLShader]
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#shaders"""
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

    def uniformLocation(self, name: Any) -> int:
        """X.uniformLocation(name) -> int

Supplemental documentation:
Qt 5 reference:

### int QGLShaderProgram::uniformLocation(const char \\**name*) const

Returns the location of the uniform variable *name* within this shader program's
parameter list. Returns -1 if *name* is not a valid uniform variable for this shader
program.

**See also**
[attributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#attributeLocation)().

### int QGLShaderProgram::uniformLocation(const [QByteArray](https://doc.qt.io/archives/qt-5.15/qbytearray.html) \\&*name*) const

This is an overloaded function.

Returns the location of the uniform variable *name* within this shader program's
parameter list. Returns -1 if *name* is not a valid uniform variable for this shader
program.

**See also**
[attributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#attributeLocation)().

### int QGLShaderProgram::uniformLocation(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*name*) const

This is an overloaded function.

Returns the location of the uniform variable *name* within this shader program's
parameter list. Returns -1 if *name* is not a valid uniform variable for this shader
program.

**See also**
[attributeLocation](https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#attributeLocation)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
uniformLocation(self, name: PySide2.QtCore.QByteArray) -> int
uniformLocation(self, name: str) -> int
uniformLocation(self, name: str) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglshaderprogram.html#uniformLocation"""
        ...
    objectName: Any

class QGLWidget:
    """PythonQtInstanceWrapper object

Native bases: PythonQtInstanceWrapper

Supplemental documentation:
Qt 5 reference:

## Detailed Description

QGLWidget provides functionality for displaying OpenGL graphics integrated into a Qt
application. It is very simple to use. You inherit from it and use the subclass like any
other [QWidget](https://doc.qt.io/archives/qt-5.15/qwidget.html), except that you have
the choice between using [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html)
and standard OpenGL rendering commands.

**Note:** This class is part of the legacy [Qt
OpenGL](https://doc.qt.io/archives/qt-5.15/qtopengl-index.html) module and, like the
other `QGL` classes, should be avoided in the new applications. Instead, starting from
Qt 5.4, prefer using
[QOpenGLWidget](https://doc.qt.io/archives/qt-5.15/qopenglwidget.html) and the `QOpenGL`
classes.

QGLWidget provides three convenient virtual functions that you can reimplement in your
subclass to perform the typical OpenGL tasks:

- [paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() \\- Renders the OpenGL scene. Gets called whenever the widget needs to be updated.
- [resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)() \\- Sets up the OpenGL viewport, projection, etc. Gets called whenever the widget has been resized (and also when it is shown for the first time because all newly created widgets get a resize event automatically).
- [initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() \\- Sets up the OpenGL rendering context, defines display lists, etc. Gets called once before the first time [resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)() or [paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() is called.

Here is a rough outline of how a QGLWidget subclass might look:

```
class MyGLDrawer : public QGLWidget
{
    Q_OBJECT        // must include this if you use Qt signals/slots

public:
    MyGLDrawer(QWidget *parent)
        : QGLWidget(parent) {}

protected:

    void initializeGL() override
    {
        // Set up the rendering context, define display lists etc.:
        ...
        glClearColor(0.0, 0.0, 0.0, 0.0);
        glEnable(GL_DEPTH_TEST);
        ...
    }

    void resizeGL(int w, int h) override
    {
        // setup viewport, projection etc.:
        glViewport(0, 0, (GLint)w, (GLint)h);
        ...
        glFrustum(...);
        ...
    }

    void paintGL() override
    {
        // draw the scene:
        ...
        glRotatef(...);
        glMaterialfv(...);
        glBegin(GL_QUADS);
        glVertex3f(...);
        glVertex3f(...);
        ...
        glEnd();
        ...
    }

};
```

If you need to trigger a repaint from places other than
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() (a typical
example is when using [timers](https://doc.qt.io/archives/qt-5.15/qtimer.html) to
animate scenes), you should call the widget's
[updateGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#updateGL)() function.

Your widget's OpenGL rendering context is made current when
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)(),
[resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)(), or
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() is
called. If you need to call the standard OpenGL API functions from other places (e.g. in
your widget's constructor or in your own paint functions), you must call
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeCurrent)() first.

QGLWidget provides functions for requesting a new display
[format](https://doc.qt.io/archives/qt-5.15/qglformat.html) and you can also create
widgets with customized rendering
[contexts](https://doc.qt.io/archives/qt-5.15/qglcontext.html).

You can also share OpenGL display lists between QGLWidget objects (see the documentation
of the QGLWidget constructors for details).

Note that under Windows, the
[QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) belonging to a
QGLWidget has to be recreated when the QGLWidget is reparented. This is necessary due to
limitations on the Windows platform. This will most likely cause problems for users that
have subclassed and installed their own
[QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) on a QGLWidget. It is
possible to work around this issue by putting the QGLWidget inside a dummy widget and
then reparenting the dummy widget, instead of the QGLWidget. This will side-step the
issue altogether, and is what we recommend for users that need this kind of
functionality.

On macOS, when Qt is built with Cocoa support, a QGLWidget can't have any sibling
widgets placed ontop of itself. This is due to limitations in the Cocoa API and is not
supported by Apple.

### Overlays

The QGLWidget creates a GL overlay context in addition to the normal context if overlays
are supported by the underlying system.

If you want to use overlays, you specify it in the
[format](https://doc.qt.io/archives/qt-5.15/qglformat.html). (Note: Overlay must be
requested in the format passed to the QGLWidget constructor.) Your GL widget should also
implement some or all of these virtual methods:

- [paintOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintOverlayGL)()
- [resizeOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeOverlayGL)()
- [initializeOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeOverlayGL)()

These methods work in the same way as the normal
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() etc. functions,
except that they will be called when the overlay context is made current. You can
explicitly make the overlay context current by using
[makeOverlayCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeOverlayCurrent)(),
and you can access the overlay context directly (e.g. to ask for its transparent color)
by calling
[overlayContext](https://doc.qt.io/archives/qt-5.15/qglwidget.html#overlayContext)().

On X servers in which the default visual is in an overlay plane, non-GL Qt windows can
also be used for overlays.

### Painting Techniques

As described above, subclass QGLWidget to render pure 3D content in the following way:

- Reimplement the [QGLWidget::initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() and [QGLWidget::resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)() to set up the OpenGL state and provide a perspective transformation.
- Reimplement [QGLWidget::paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() to paint the 3D scene, calling only OpenGL functions to draw on the widget.

It is also possible to draw 2D graphics onto a QGLWidget subclass, it is necessary to
reimplement
[QGLWidget::paintEvent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintEvent)()
and do the following:

- Construct a [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) object.
- Initialize it for use on the widget with the [QPainter::begin](https://doc.qt.io/archives/qt-5.15/qpainter.html#begin)() function.
- Draw primitives using [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html)'s member functions.
- Call [QPainter::end](https://doc.qt.io/archives/qt-5.15/qpainter.html#end)() to finish painting.

### Threading

As of Qt version 4.8, support for doing threaded GL rendering has been improved. There
are three scenarios that we currently support:

- 1\\. Buffer swapping in a thread.

  Swapping buffers in a double buffered context may be a synchronous, locking call that
  may be a costly operation in some GL implementations. Especially so on embedded devices.
  It's not optimal to have the CPU idling while the GPU is doing a buffer swap. In those
  cases it is possible to do the rendering in the main thread and do the actual buffer
  swap in a separate thread. This can be done with the following steps:

  1\\. Call [doneCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#doneCurrent)()
  in the main thread when the rendering is finished.

  2\\. Call
  [QGLContext::moveToThread](https://doc.qt.io/archives/qt-5.15/qglcontext.html#moveToThread)(swapThread)
  to transfer ownership of the context to the swapping thread.

  3\\. Notify the swapping thread that it can grab the context.

  4\\. Make the rendering context current in the swapping thread with
  [makeCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeCurrent)() and then
  call [swapBuffers](https://doc.qt.io/archives/qt-5.15/qglwidget.html#swapBuffers)().

  5\\. Call [doneCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#doneCurrent)()
  in the swapping thread.

  6\\. Call
  [QGLContext::moveToThread](https://doc.qt.io/archives/qt-5.15/qglcontext.html#moveToThread)([qApp](https://doc.qt.io/archives/qt-5.15/qapplication.html#qApp)-\\>[thread](https://doc.qt.io/archives/qt-5.15/qobject.html#thread)())
  and notify the main thread that swapping is done.

  Doing this will free up the main thread so that it can continue with, for example,
  handling UI events or network requests. Even if there is a context swap involved, it may
  be preferable compared to having the main thread wait while the GPU finishes the swap
  operation. Note that this is highly implementation dependent.
- 2\\. Texture uploading in a thread.

  Doing texture uploads in a thread may be very useful for applications handling large
  amounts of images that needs to be displayed, like for instance a photo gallery
  application. This is supported in Qt through the existing
  [bindTexture](https://doc.qt.io/archives/qt-5.15/qglwidget.html#bindTexture)() API. A
  simple way of doing this is to create two sharing QGLWidgets. One is made current in the
  main GUI thread, while the other is made current in the texture upload thread. The
  widget in the uploading thread is never shown, it is only used for sharing textures with
  the main thread. For each texture that is bound via
  [bindTexture](https://doc.qt.io/archives/qt-5.15/qglwidget.html#bindTexture)(), notify
  the main thread so that it can start using the texture.
- 3\\. Using [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) to draw into a QGLWidget in a thread.

  In Qt 4.8, it is possible to draw into a QGLWidget using a
  [QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) in a separate thread. Note
  that this is also possible for QGLPixelBuffers and QGLFramebufferObjects. Since this is
  only supported in the GL 2 paint engine, OpenGL 2.0 or OpenGL ES 2.0 is required.

  QGLWidgets can only be created in the main GUI thread. This means a call to
  [doneCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#doneCurrent)() is
  necessary to release the GL context from the main thread, before the widget can be drawn
  into by another thread. You then need to call
  [QGLContext::moveToThread](https://doc.qt.io/archives/qt-5.15/qglcontext.html#moveToThread)()
  to transfer ownership of the context to the thread in which you want to make it current.
  Also, the main GUI thread will dispatch resize and paint events to a QGLWidget when the
  widget is resized, or parts of it becomes exposed or needs redrawing. It is therefore
  necessary to handle those events because the default implementations inside QGLWidget
  will try to make the QGLWidget's context current, which again will interfere with any
  threads rendering into the widget. Reimplement
  [QGLWidget::paintEvent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintEvent)()
  and
  [QGLWidget::resizeEvent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeEvent)()
  to notify the rendering thread that a resize or update is necessary, and be careful not
  to call the base class implementation. If you are rendering an animation, it might not
  be necessary to handle the paint event at all since the rendering thread is doing
  regular updates. Then it would be enough to reimplement
  [QGLWidget::paintEvent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintEvent)()
  to do nothing.

As a general rule when doing threaded rendering: be aware that binding and releasing
contexts in different threads have to be synchronized by the user. A GL rendering
context can only be current in one thread at any time. If you try to open a
[QPainter](https://doc.qt.io/archives/qt-5.15/qpainter.html) on a QGLWidget and the
widget's rendering context is current in another thread, it will fail.

In addition to this, rendering using raw GL calls in a separate thread is supported.

*OpenGL is a trademark of Silicon Graphics, Inc. in the United States and other
countries.*

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html"""

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

    def autoBufferSwap(self) -> bool:
        """X.autoBufferSwap() -> bool

Supplemental documentation:
Qt 5 reference:

### `[protected]` bool QGLWidget::autoBufferSwap() const

Returns `true` if the widget is doing automatic GL buffer swapping; otherwise returns
`false`.

**See also**
[setAutoBufferSwap](https://doc.qt.io/archives/qt-5.15/qglwidget.html#setAutoBufferSwap)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
autoBufferSwap(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#autoBufferSwap"""
        ...

    def backgroundRole(self) -> Any:
        """X.backgroundRole()"""
        ...

    def backingStore(self) -> Any:
        """X.backingStore() -> PythonQt.QtGui.QBackingStore"""
        ...

    def bindTexture(self, image: Any, target: Any, format: Any, options: Any) -> int:
        """X.bindTexture(image, target, format, options) -> int

Supplemental documentation:
Qt 5 reference:

### GLuint QGLWidget::bindTexture(const [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) \\&*image*, GLenum *target* \\= GL\\_TEXTURE\\_2D, GLint *format* \\= GL\\_RGBA)

Calls QGLContext:::bindTexture(*image*, *target*, *format*) on the currently set
context.

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglwidget.html#deleteTexture)().

### GLuint QGLWidget::bindTexture(const [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) \\&*image*, GLenum *target*, GLint *format*, [QGLContext::BindOptions](https://doc.qt.io/archives/qt-5.15/qglcontext.html#BindOption-enum) *options*)

This is an overloaded function.

The binding *options* are a set of options used to decide how to bind the texture to the
context.

This function was introduced in Qt 4.6.

### GLuint QGLWidget::bindTexture(const [QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html) \\&*pixmap*, GLenum *target*, GLint *format*, [QGLContext::BindOptions](https://doc.qt.io/archives/qt-5.15/qglcontext.html#BindOption-enum) *options*)

This is an overloaded function.

Generates and binds a 2D GL texture to the current context, based on *pixmap*. The
generated texture id is returned and can be used in

The binding *options* are a set of options used to decide how to bind the texture to the
context.

This function was introduced in Qt 4.6.

### GLuint QGLWidget::bindTexture(const [QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html) \\&*pixmap*, GLenum *target* \\= GL\\_TEXTURE\\_2D, GLint *format* \\= GL\\_RGBA)

Calls QGLContext:::bindTexture(*pixmap*, *target*, *format*) on the currently set
context.

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglwidget.html#deleteTexture)().

### GLuint QGLWidget::bindTexture(const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*fileName*)

This is an overloaded function.

Calls
[QGLContext::bindTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#bindTexture)(*fileName*)
on the currently set context.

**See also**
[deleteTexture](https://doc.qt.io/archives/qt-5.15/qglwidget.html#deleteTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
bindTexture(self, fileName: str) -> int
bindTexture(self, image: PySide2.QtGui.QImage, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
bindTexture(self, image: PySide2.QtGui.QImage, target: int=..., format: int=...) -> int
bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int=..., format: int=...) -> int
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#bindTexture"""
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

    def colormap(self) -> Any:
        """X.colormap() -> PythonQt.QtOpenGL.QGLColormap

Supplemental documentation:
Qt 5 reference:

### const [QGLColormap](https://doc.qt.io/archives/qt-5.15/qglcolormap.html) \\&QGLWidget::colormap() const

Returns the colormap for this widget.

Usually it is only top-level widgets that can have different colormaps installed. Asking
for the colormap of a child widget will return the colormap for the child's top-level
widget.

If no colormap has been set for this widget, the QGLColormap returned will be empty.

**See also**
[setColormap](https://doc.qt.io/archives/qt-5.15/qglwidget.html#setColormap)() and
[QGLColormap::isEmpty](https://doc.qt.io/archives/qt-5.15/qglcolormap.html#isEmpty)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
colormap(self) -> PySide2.QtOpenGL.QGLColormap
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#colormap"""
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

    def context(self) -> Any:
        """X.context() -> PythonQt.QtOpenGL.QGLContext

Supplemental documentation:
Qt 5 reference:

### [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) \\*QGLWidget::context() const

Returns the context of this widget.

It is possible that the context is not valid (see
[isValid](https://doc.qt.io/archives/qt-5.15/qglwidget.html#isValid)()), for example, if
the underlying hardware does not support the format attributes that were requested.

**See also**
[setContext](https://doc.qt.io/archives/qt-5.15/qglwidget-obsolete.html#setContext)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
context(self) -> PySide2.QtOpenGL.QGLContext
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#context"""
        ...

    def contextMenuEvent(self, event: Any) -> Any:
        """X.contextMenuEvent(event)"""
        ...

    def convertToGLFormat(self, img: Any) -> Any:
        """X.convertToGLFormat(img) -> PythonQt.QtGui.QImage

Supplemental documentation:
Qt 5 reference:

### `[static]` [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) QGLWidget::convertToGLFormat(const [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) \\&*img*)

Converts the image *img* into the unnamed format expected by OpenGL functions such as
glTexImage2D(). The returned image is not usable as a
[QImage](https://doc.qt.io/archives/qt-5.15/qimage.html), but
[QImage::width](https://doc.qt.io/archives/qt-5.15/qimage.html#width)(),
[QImage::height](https://doc.qt.io/archives/qt-5.15/qimage.html#height)() and
[QImage::bits](https://doc.qt.io/archives/qt-5.15/qimage.html#bits)() may be used with
OpenGL. The GL format used is `GL_RGBA`.

Upstream PySide2 reference signatures (binding differences may apply):

```python
convertToGLFormat(img: PySide2.QtGui.QImage) -> PySide2.QtGui.QImage
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#convertToGLFormat"""
        ...

    def createWinId(self) -> Any:
        """X.createWinId()"""
        ...

    def createWindowContainer(self, window: Any, parent: Any, arg2: flags) -> Any:
        """X.createWindowContainer(window, parent, flags) -> PythonQt.QtGui.QWidget"""
        ...

    def customContextMenuRequested(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtOpenGL.QGLWidget.customContextMenuRequested; argument details are not documented."""
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

    def deleteTexture(self, tx_id: int) -> None:
        """X.deleteTexture(tx_id)

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::deleteTexture(GLuint *id*)

Calls
[QGLContext::deleteTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#deleteTexture)(*id*)
on the currently set context.

**See also**
[bindTexture](https://doc.qt.io/archives/qt-5.15/qglwidget.html#bindTexture)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
deleteTexture(self, tx_id: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#deleteTexture"""
        ...

    def depth(self) -> int:
        """X.depth() -> int"""
        ...

    def destroy(self, destroyWindow: Any, destroySubWindows: Any) -> Any:
        """X.destroy(destroyWindow, destroySubWindows)"""
        ...

    def destroyed(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtOpenGL.QGLWidget.destroyed; argument details are not documented."""
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

    def doneCurrent(self) -> None:
        """X.doneCurrent()

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::doneCurrent()

Makes no GL context the current context. Normally, you do not need to call this
function; QGLContext calls it as necessary. However, it may be useful in multithreaded
environments.

Upstream PySide2 reference signatures (binding differences may apply):

```python
doneCurrent(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#doneCurrent"""
        ...

    def doubleBuffer(self) -> bool:
        """X.doubleBuffer() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLWidget::doubleBuffer() const

Returns `true` if the contained GL rendering context has double buffering; otherwise
returns `false`.

**See also**
[QGLFormat::doubleBuffer](https://doc.qt.io/archives/qt-5.15/qglformat.html#doubleBuffer)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
doubleBuffer(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#doubleBuffer"""
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

    def drawTexture(self, point: Any, textureId: int, textureTarget: int) -> None:
        """X.drawTexture(point, textureId, textureTarget)

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::drawTexture(const [QRectF](https://doc.qt.io/archives/qt-5.15/qrectf.html) \\&*target*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

Calls the corresponding
[QGLContext::drawTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#drawTexture)()
with *target*, *textureId*, and *textureTarget* for this widget's context.

This function was introduced in Qt 4.4.

### void QGLWidget::drawTexture(const [QPointF](https://doc.qt.io/archives/qt-5.15/qpointf.html) \\&*point*, GLuint *textureId*, GLenum *textureTarget* \\= GL\\_TEXTURE\\_2D)

Calls the corresponding
[QGLContext::drawTexture](https://doc.qt.io/archives/qt-5.15/qglcontext.html#drawTexture)()
with *point*, *textureId*, and *textureTarget* for this widget's context.

This function was introduced in Qt 4.4.

Upstream PySide2 reference signatures (binding differences may apply):

```python
drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int=...) -> None
drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#drawTexture"""
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

    def event(self, arg__1: Any) -> bool:
        """X.event(arg__1) -> bool

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` bool QGLWidget::event([QEvent](https://doc.qt.io/archives/qt-5.15/qevent.html) \\**e*)

Reimplements:
[QWidget::event](https://doc.qt.io/archives/qt-5.15/qwidget.html#event)(QEvent \\*event).

Upstream PySide2 reference signatures (binding differences may apply):

```python
event(self, arg__1: PySide2.QtCore.QEvent) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#event"""
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

    def format(self) -> Any:
        """X.format() -> PythonQt.QtOpenGL.QGLFormat

Supplemental documentation:
Qt 5 reference:

### [QGLFormat](https://doc.qt.io/archives/qt-5.15/qglformat.html) QGLWidget::format() const

Returns the format of the contained GL rendering context.

**See also**
[setFormat](https://doc.qt.io/archives/qt-5.15/qglwidget-obsolete.html#setFormat)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
format(self) -> PySide2.QtOpenGL.QGLFormat
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#format"""
        ...

    def glDraw(self) -> None:
        """X.glDraw()

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::glDraw()

Executes the virtual function
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)().

The widget's rendering context will become the current context and
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() will be
called if it hasn't already been called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
glDraw(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#glDraw"""
        ...

    def glInit(self) -> None:
        """X.glInit()

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::glInit()

Initializes OpenGL for this widget's context. Calls the virtual function
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
glInit(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#glInit"""
        ...

    def grab(self, rectangle: Any) -> Any:
        """X.grab(rectangle) -> PythonQt.QtGui.QPixmap"""
        ...

    def grabFrameBuffer(self, withAlpha: bool) -> Any:
        """X.grabFrameBuffer(withAlpha) -> PythonQt.QtGui.QImage

Supplemental documentation:
Qt 5 reference:

### [QImage](https://doc.qt.io/archives/qt-5.15/qimage.html) QGLWidget::grabFrameBuffer(bool *withAlpha* \\= false)

Returns an image of the frame buffer. If *withAlpha* is true the alpha channel is
included.

Depending on your hardware, you can explicitly select which color buffer to grab with a
glReadBuffer() call before calling this function.

On QNX the back buffer is not preserved when
[swapBuffers](https://doc.qt.io/archives/qt-5.15/qglwidget.html#swapBuffers)() is
called. The back buffer where this function reads from, might thus not contain the same
content as the front buffer. In order to retrieve what is currently visible on the
screen, [swapBuffers](https://doc.qt.io/archives/qt-5.15/qglwidget.html#swapBuffers)()
has to be executed prior to this function call.

Upstream PySide2 reference signatures (binding differences may apply):

```python
grabFrameBuffer(self, withAlpha: bool=...) -> PySide2.QtGui.QImage
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#grabFrameBuffer"""
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

    def initializeGL(self) -> None:
        """X.initializeGL()

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::initializeGL()

This virtual function is called once before the first call to
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() or
[resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)(), and then once
whenever the widget has been assigned a new QGLContext. Reimplement it in a subclass.

This function should set up any required OpenGL context rendering flags, defining
display lists, etc.

There is no need to call
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeCurrent)() because
this has already been done when this function is called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
initializeGL(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL"""
        ...

    def initializeOverlayGL(self) -> None:
        """X.initializeOverlayGL()

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::initializeOverlayGL()

This virtual function is used in the same manner as
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() except
that it operates on the widget's overlay context instead of the widget's main context.
This means that initializeOverlayGL() is called once before the first call to
[paintOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintOverlayGL)() or
[resizeOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeOverlayGL)().
Reimplement it in a subclass.

This function should set up any required OpenGL context rendering flags, defining
display lists, etc. for the overlay context.

There is no need to call
[makeOverlayCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeOverlayCurrent)()
because this has already been done when this function is called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
initializeOverlayGL(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeOverlayGL"""
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

    def isSharing(self) -> bool:
        """X.isSharing() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLWidget::isSharing() const

Returns `true` if this widget's GL context is shared with another GL context, otherwise
false is returned. Context sharing might not be possible if the widgets use different
formats.

**See also** [format](https://doc.qt.io/archives/qt-5.15/qglwidget.html#format)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
isSharing(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#isSharing"""
        ...

    def isSignalConnected(self, signal: Any) -> bool:
        """X.isSignalConnected(signal) -> bool"""
        ...

    def isValid(self) -> bool:
        """X.isValid() -> bool

Supplemental documentation:
Qt 5 reference:

### bool QGLWidget::isValid() const

Returns `true` if the widget has a valid GL rendering context; otherwise returns
`false`. A widget will be invalid if the system has no [OpenGL
support](https://doc.qt.io/archives/qt-5.15/qglformat.html#hasOpenGL).

Upstream PySide2 reference signatures (binding differences may apply):

```python
isValid(self) -> bool
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#isValid"""
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

    def makeCurrent(self) -> None:
        """X.makeCurrent()

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::makeCurrent()

Makes this widget the current widget for OpenGL operations, i.e. makes the widget's
rendering context the current OpenGL rendering context.

Upstream PySide2 reference signatures (binding differences may apply):

```python
makeCurrent(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeCurrent"""
        ...

    def makeOverlayCurrent(self) -> None:
        """X.makeOverlayCurrent()

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::makeOverlayCurrent()

Makes the overlay context of this widget current. Use this if you need to issue OpenGL
commands to the overlay context outside of
[initializeOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeOverlayGL)(),
[resizeOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeOverlayGL)(),
and
[paintOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintOverlayGL)().

Does nothing if this widget has no overlay.

**See also**
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeCurrent)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
makeOverlayCurrent(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeOverlayCurrent"""
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
        """Native PythonQt.QtOpenGL.QGLWidget.objectNameChanged; argument details are not documented."""
        ...

    def overlayContext(self) -> Any:
        """X.overlayContext() -> PythonQt.QtOpenGL.QGLContext

Supplemental documentation:
Qt 5 reference:

### const [QGLContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html) \\*QGLWidget::overlayContext() const

Returns the overlay context of this widget, or `nullptr` if this widget has no overlay.

**See also** [context](https://doc.qt.io/archives/qt-5.15/qglwidget.html#context)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
overlayContext(self) -> PySide2.QtOpenGL.QGLContext
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#overlayContext"""
        ...

    def overrideWindowFlags(self, type: Any) -> Any:
        """X.overrideWindowFlags(type)"""
        ...

    def overrideWindowState(self, state: Any) -> Any:
        """X.overrideWindowState(state)"""
        ...

    def paintEngine(self) -> Any:
        """X.paintEngine() -> PythonQt.QtGui.QPaintEngine

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintEngine(self) -> PySide2.QtGui.QPaintEngine
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintEngine"""
        ...

    def paintEvent(self, arg__1: Any) -> None:
        """X.paintEvent(arg__1)

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` void QGLWidget::paintEvent([QPaintEvent](https://doc.qt.io/archives/qt-5.15/qpaintevent.html) \\**event*)

Reimplements:
[QWidget::paintEvent](https://doc.qt.io/archives/qt-5.15/qwidget.html#paintEvent)(QPaintEvent
\\*event).

Handles paint events passed in the *event* parameter. Will cause the virtual
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() function to be
called.

The widget's rendering context will become the current context and
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() will be
called if it hasn't already been called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintEvent"""
        ...

    def paintGL(self) -> None:
        """X.paintGL()

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::paintGL()

This virtual function is called whenever the widget needs to be painted. Reimplement it
in a subclass.

There is no need to call
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeCurrent)() because
this has already been done when this function is called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintGL(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL"""
        ...

    def paintOverlayGL(self) -> None:
        """X.paintOverlayGL()

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::paintOverlayGL()

This virtual function is used in the same manner as
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() except that it
operates on the widget's overlay context instead of the widget's main context. This
means that paintOverlayGL() is called whenever the widget's overlay needs to be painted.
Reimplement it in a subclass.

There is no need to call
[makeOverlayCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeOverlayCurrent)()
because this has already been done when this function is called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
paintOverlayGL(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintOverlayGL"""
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

    def qglClearColor(self, c: Any) -> None:
        """X.qglClearColor(c)

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::qglClearColor(const [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) \\&*c*) const

Convenience function for specifying the clearing color to OpenGL. Calls glClearColor (in
RGBA mode) or glClearIndex (in color-index mode) with the color *c*. Applies to this
widgets GL context.

**See also** [qglColor](https://doc.qt.io/archives/qt-5.15/qglwidget.html#qglColor)(),
[QGLContext::currentContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html#currentContext)(),
and [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
qglClearColor(self, c: PySide2.QtGui.QColor) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#qglClearColor"""
        ...

    def qglColor(self, c: Any) -> None:
        """X.qglColor(c)

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::qglColor(const [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html) \\&*c*) const

Convenience function for specifying a drawing color to OpenGL. Calls glColor4 (in RGBA
mode) or glIndex (in color-index mode) with the color *c*. Applies to this widgets GL
context.

**Note:** This function is not supported on OpenGL/ES 2.0 systems.

**See also**
[qglClearColor](https://doc.qt.io/archives/qt-5.15/qglwidget.html#qglClearColor)(),
[QGLContext::currentContext](https://doc.qt.io/archives/qt-5.15/qglcontext.html#currentContext)(),
and [QColor](https://doc.qt.io/archives/qt-5.15/qcolor.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
qglColor(self, c: PySide2.QtGui.QColor) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#qglColor"""
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

    def renderPixmap(self, w: int, h: int, useContext: bool) -> Any:
        """X.renderPixmap(w, h, useContext) -> PythonQt.QtGui.QPixmap

Supplemental documentation:
Qt 5 reference:

### [QPixmap](https://doc.qt.io/archives/qt-5.15/qpixmap.html) QGLWidget::renderPixmap(int *w* \\= 0, int *h* \\= 0, bool *useContext* \\= false)

Renders the current scene on a pixmap and returns the pixmap.

You can use this method on both visible and invisible
[QGLWidget](https://doc.qt.io/archives/qt-5.15/qglwidget.html) objects.

Internally the function renders into a framebuffer object and performs pixel readback.
This has a performance penalty, meaning that this function is not suitable to be called
at a high frequency.

After creating and binding the framebuffer object, the function will call
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)(),
[resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)(), and
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)(). On the next
normal update
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() and
[resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)() will be
triggered again since the size of the destination pixmap and the
[QGLWidget](https://doc.qt.io/archives/qt-5.15/qglwidget.html)'s size may differ.

The size of the pixmap will be *w* pixels wide and *h* pixels high unless one of these
parameters is 0 (the default), in which case the pixmap will have the same size as the
widget.

Care must be taken when using framebuffer objects in
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() in combination
with this function. To switch back to the default framebuffer, use
[QGLFramebufferObject::bindDefault](https://doc.qt.io/archives/qt-5.15/qglframebufferobject.html#bindDefault)().
Binding FBO 0 is wrong since renderPixmap() uses a custom framebuffer instead of the one
provided by the windowing system.

*useContext* is ignored. Historically this parameter enabled the usage of the existing
GL context. This is not supported anymore since additional contexts are never created.

Overlays are not rendered onto the pixmap.

If the GL rendering context and the desktop have different bit depths, the result will
most likely look surprising.

Note that the creation of display lists, modifications of the view frustum etc. should
be done from within
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)(). If
this is not done, the temporary QGLContext will not be initialized properly, and the
rendered pixmap may be incomplete/corrupted.

Upstream PySide2 reference signatures (binding differences may apply):

```python
renderPixmap(self, w: int=..., h: int=..., useContext: bool=...) -> PySide2.QtGui.QPixmap
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#renderPixmap"""
        ...

    def renderText(self, x: Any, y: Any, z: Any, str: str, fnt: Any) -> None:
        """X.renderText(x, y, z, str, fnt)

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::renderText(int *x*, int *y*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*str*, const [QFont](https://doc.qt.io/archives/qt-5.15/qfont.html) \\&*font* \\= QFont())

Renders the string *str* into the GL context of this widget.

*x* and *y* are specified in window coordinates, with the origin in the upper left-hand
corner of the window. If *font* is not specified, the currently set application font
will be used to render the string. To change the color of the rendered text you can use
the glColor() call (or the
[qglColor](https://doc.qt.io/archives/qt-5.15/qglwidget.html#qglColor)() convenience
function), just before the renderText() call.

**Note:** This function clears the stencil buffer.

**Note:** This function is not supported on OpenGL/ES systems.

**Note:** This function temporarily disables depth-testing when the text is drawn.

**Note:** This function can only be used inside a
[QPainter::beginNativePainting](https://doc.qt.io/archives/qt-5.15/qpainter.html#beginNativePainting)()/[QPainter::endNativePainting](https://doc.qt.io/archives/qt-5.15/qpainter.html#endNativePainting)()
block if a painter is active on the
[QGLWidget](https://doc.qt.io/archives/qt-5.15/qglwidget.html).

### void QGLWidget::renderText(double *x*, double *y*, double *z*, const [QString](https://doc.qt.io/archives/qt-5.15/qstring.html) \\&*str*, const [QFont](https://doc.qt.io/archives/qt-5.15/qfont.html) \\&*font* \\= QFont())

This is an overloaded function.

*x*, *y* and *z* are specified in scene or object coordinates relative to the currently
set projection and model matrices. This can be useful if you want to annotate models
with text labels and have the labels move with the model as it is rotated etc.

**Note:** This function is not supported on OpenGL/ES systems.

**Note:** If depth testing is enabled before this function is called, then the drawn
text will be depth-tested against the models that have already been drawn in the scene.
Use `glDisable(GL_DEPTH_TEST)` before calling this function to annotate the models
without depth-testing the text.

**Note:** This function can only be used inside a
[QPainter::beginNativePainting](https://doc.qt.io/archives/qt-5.15/qpainter.html#beginNativePainting)()/[QPainter::endNativePainting](https://doc.qt.io/archives/qt-5.15/qpainter.html#endNativePainting)()
block if a painter is active on the
[QGLWidget](https://doc.qt.io/archives/qt-5.15/qglwidget.html).

Upstream PySide2 reference signatures (binding differences may apply):

```python
renderText(self, x: float, y: float, z: float, str: str, fnt: PySide2.QtGui.QFont=...) -> None
renderText(self, x: int, y: int, str: str, fnt: PySide2.QtGui.QFont=...) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#renderText"""
        ...

    def repaint(self, x: Any, y: Any, w: Any, h: Any) -> Any:
        """X.repaint(x, y, w, h)"""
        ...

    def resize(self, w: Any, h: Any) -> Any:
        """X.resize(w, h)"""
        ...

    def resizeEvent(self, arg__1: Any) -> None:
        """X.resizeEvent(arg__1)

Supplemental documentation:
Qt 5 reference:

### `[override virtual protected]` void QGLWidget::resizeEvent([QResizeEvent](https://doc.qt.io/archives/qt-5.15/qresizeevent.html) \\**event*)

Reimplements:
[QWidget::resizeEvent](https://doc.qt.io/archives/qt-5.15/qwidget.html#resizeEvent)(QResizeEvent
\\*event).

Handles resize events that are passed in the *event* parameter. Calls the virtual
function [resizeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeEvent"""
        ...

    def resizeGL(self, w: int, h: int) -> None:
        """X.resizeGL(w, h)

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::resizeGL(int *width*, int *height*)

This virtual function is called whenever the widget has been resized. The new size is
passed in *width* and *height*. Reimplement it in a subclass.

There is no need to call
[makeCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeCurrent)() because
this has already been done when this function is called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
resizeGL(self, w: int, h: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeGL"""
        ...

    def resizeOverlayGL(self, w: int, h: int) -> None:
        """X.resizeOverlayGL(w, h)

Supplemental documentation:
Qt 5 reference:

### `[virtual protected]` void QGLWidget::resizeOverlayGL(int *width*, int *height*)

This virtual function is used in the same manner as
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() except that it
operates on the widget's overlay context instead of the widget's main context. This
means that resizeOverlayGL() is called whenever the widget has been resized. The new
size is passed in *width* and *height*. Reimplement it in a subclass.

There is no need to call
[makeOverlayCurrent](https://doc.qt.io/archives/qt-5.15/qglwidget.html#makeOverlayCurrent)()
because this has already been done when this function is called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
resizeOverlayGL(self, w: int, h: int) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#resizeOverlayGL"""
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

    def setAutoBufferSwap(self, on: bool) -> None:
        """X.setAutoBufferSwap(on)

Supplemental documentation:
Qt 5 reference:

### `[protected]` void QGLWidget::setAutoBufferSwap(bool *on*)

If *on* is true automatic GL buffer swapping is switched on; otherwise it is switched
off.

If *on* is true and the widget is using a double-buffered format, the background and
foreground GL buffers will automatically be swapped after each
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() call.

The buffer auto-swapping is on by default.

**See also**
[autoBufferSwap](https://doc.qt.io/archives/qt-5.15/qglwidget.html#autoBufferSwap)(),
[doubleBuffer](https://doc.qt.io/archives/qt-5.15/qglwidget.html#doubleBuffer)(), and
[swapBuffers](https://doc.qt.io/archives/qt-5.15/qglwidget.html#swapBuffers)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setAutoBufferSwap(self, on: bool) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#setAutoBufferSwap"""
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

    def setColormap(self, map: Any) -> None:
        """X.setColormap(map)

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::setColormap(const [QGLColormap](https://doc.qt.io/archives/qt-5.15/qglcolormap.html) \\&*cmap*)

Set the colormap for this widget to *cmap*. Usually it is only top-level widgets that
can have colormaps installed.

**See also** [colormap](https://doc.qt.io/archives/qt-5.15/qglwidget.html#colormap)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
setColormap(self, map: PySide2.QtOpenGL.QGLColormap) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#setColormap"""
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

    def swapBuffers(self) -> None:
        """X.swapBuffers()

Supplemental documentation:
Qt 5 reference:

### void QGLWidget::swapBuffers()

Swaps the screen contents with an off-screen buffer. This only works if the widget's
format specifies double buffer mode.

Normally, there is no need to explicitly call this function because it is done
automatically after each widget repaint, i.e. each time after
[paintGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintGL)() has been
executed.

**See also**
[doubleBuffer](https://doc.qt.io/archives/qt-5.15/qglwidget.html#doubleBuffer)(),
[setAutoBufferSwap](https://doc.qt.io/archives/qt-5.15/qglwidget.html#setAutoBufferSwap)(),
and
[QGLFormat::setDoubleBuffer](https://doc.qt.io/archives/qt-5.15/qglformat.html#setDoubleBuffer)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
swapBuffers(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#swapBuffers"""
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

    def updateGL(self) -> None:
        """X.updateGL()

Supplemental documentation:
Qt 5 reference:

### `[virtual slot]` void QGLWidget::updateGL()

Updates the widget by calling
[glDraw](https://doc.qt.io/archives/qt-5.15/qglwidget.html#glDraw)().

Upstream PySide2 reference signatures (binding differences may apply):

```python
updateGL(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#updateGL"""
        ...

    def updateGeometry(self) -> Any:
        """X.updateGeometry()"""
        ...

    def updateOverlayGL(self) -> None:
        """X.updateOverlayGL()

Supplemental documentation:
Qt 5 reference:

### `[virtual slot]` void QGLWidget::updateOverlayGL()

Updates the widget's overlay (if any). Will cause the virtual function
[paintOverlayGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#paintOverlayGL)() to
be executed.

The widget's rendering context will become the current context and
[initializeGL](https://doc.qt.io/archives/qt-5.15/qglwidget.html#initializeGL)() will be
called if it hasn't already been called.

Upstream PySide2 reference signatures (binding differences may apply):

```python
updateOverlayGL(self) -> None
```

Source: https://doc.qt.io/archives/qt-5.15/qglwidget.html#updateOverlayGL"""
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
        """Native PythonQt.QtOpenGL.QGLWidget.windowIconChanged; argument details are not documented."""
        ...

    def windowIconTextChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtOpenGL.QGLWidget.windowIconTextChanged; argument details are not documented."""
        ...

    def windowRole(self) -> str:
        """X.windowRole() -> str"""
        ...

    def windowState(self) -> Any:
        """X.windowState()"""
        ...

    def windowTitleChanged(self, *args: Any, **kwargs: Any) -> Any:
        """Native PythonQt.QtOpenGL.QGLWidget.windowTitleChanged; argument details are not documented."""
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
__all__ = ['QGLBuffer', 'QGLColormap', 'QGLContext', 'QGLFormat', 'QGLFramebufferObject', 'QGLFramebufferObjectFormat', 'QGLFunctions', 'QGLPixelBuffer', 'QGLShader', 'QGLShaderProgram', 'QGLWidget']
