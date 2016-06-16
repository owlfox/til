# ref
[mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)
### Spec
available from EC5

> from *Javascript the definitive guide*
## Synopsis
array.reduce(f)
array.reduce(f, initial)
## Arguments
To compute a value from the elements of an array,.
f
A function that combines two values (such as two array elements) and returns a new “reduced” value.
## initial
An optional initial value to seed the array reduction with. If this argument is specified, reduce() behaves as if it had been inserted at the start of array.
## Returns
The reduced value of the array, which is the return value of the last invocation of f.

```js
// a example from freecodecamp
function range(lowEnd,highEnd){
    var arr = [],
    c = highEnd - lowEnd + 1;
    while ( c-- ) {
        arr[c] = highEnd--;
    }
    return arr;
}

function sumAll(arr) {
  var a = range(Math.min(arr[0], arr[1]), Math.max(arr[0], arr[1]));
  return a.reduce(function(a,b){return a+b;});
}

sumAll([1, 4]);//should equal to 10
```
