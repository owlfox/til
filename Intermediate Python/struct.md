# struct
> This module performs conversions between Python values and C structs represented as Python strings. This can be used in handling binary data stored in files or from network connections, among other sources. It uses Format Strings as compact descriptions of the layout of the C structs and the intended conversion to/from Python values.

* **struck.pack**
    >  Pack the values v1, v2, ... according to the given format, write the packed bytes into the writable buffer starting at offset. Note that the offset is a required argument.

    exampleto pack a ethernet packet mac address:
    ```py
    hw = pack("BBBBBB",0x00, 0x21, 0x9b, 0xe3, 0xae, 0x81)
    ```
