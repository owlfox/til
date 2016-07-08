# forword
I happened to find this module handy to help. Here are some recipe you may find helpful like me. For more information, please check the official document about [```__future__``` module](https://docs.python.org/2/library/__future__.html)

* [print_function](https://www.python.org/dev/peps/pep-3105/)

```print``` is a function in python 3, for people who like to write code compatible with both 2 and 3.

```py
from __future__ import print_function #put this on the first line of the file
print("it works")//then print() will do the trick for you
```

* [absolute_import](https://www.python.org/dev/peps/pep-0328/)

If you want to import a module, while the module name is confilct with standard module, ```absolute import``` is your friend.

```py
from __future__ import absolute_import
import os #import the standard module of python.
from . import os # import your os.py in the current directory.
```
