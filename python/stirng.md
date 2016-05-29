# some notes about string
```python
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Br≠ing out the holy {name!r}"    # Calls repr() on the argument first
```

* repr? str?
    [this thread](http://stackoverflow.com/questions/7784148/understanding-repr-function-in-python) talks about the difference between str and repr.
    > repr actually calls a magic method __repr__ of x, which gives the string containing the representation of the value 'foo' assigned to x. So it returns 'foo' inside the string "" resulting in "'foo'". The idea of repr is to give a string which contains a series of symbols which we can type in the interpreter and get the same value which was sent as an argument to repr.
