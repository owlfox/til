# Some notes of ports.

1. you can find the well-known port-service relationship in your ```/etc/services```
file, if you're using unix/linux system.
2. we use 16 bits to represent this field.
3. 0~1023
4. 1024~49151 see [the services file on macosx 10.11](Networking/services), or you can check it out on [IANA](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
5. 49152~65535 is used by os for temporary tool ...

```python
# about how to solve
import socket
>>> socket.getservbyname('domain')
53
```
