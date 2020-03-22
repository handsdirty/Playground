# Setup
Command + Option + J

# Basics
-  JS number type, only one, for both integer and floating numbers. Like an 64-bit double.
-  true/ false, NOT True/False.
- String: no character datatype. Prefer using single quote (HTML traditionally use double quote). Immutable. .length is a property. .charAt(2) .big() result in html big tag.
- Arrays. .shift() , .pop(), .sort(), .join().

# Objects (重点)

Never use trailing commas because IE throws syntax error.

JS compiler may rename property name. In problem, use quotes to avoid renaming.

```
if ('a' in d)

delete obj.title
```

Don't use array for map, the array.lengh will be 0 confusingly.

Null v..s Undefined.
typeof, instanceof

```
console.log(typeof(123))
console.log([1,2,3] instanceof Array)
```

## Operators
```
Math.min(), Math.sin(), Math.random(), Math.floor()
```

===, checks if compared values are equal and have same type.

1 == '1'   // true, it cast to same type to compare.

In short, === really really equal. == sort of equal.
```
315 + ' meters' // "315 meters".  It automatically converts anything to a string if one is.
```

string immutable may eat up memory. may use [] to optimize.

true & 42 returns 42. Lazy about return value of &&, the 

false, 0 and NaN, '', null  and undefined, evaluates to true.

## Conversions, String(), Number(), Boolean().

## Primitive v.s. Reference types

# Statements
```
var now = new Date(); now.getDay();

switch(event.keyCode); // Common application is handling keyboard input.

for (key in obj) {}
```

# Functions
Functions are objects, and can be dynamically created, and passed on.

```
function sum(var_args) { return arguments; }
```

Pass by Value (primitive) v.s. Pass by Reference (objects and arrays)

Function define scope. Local variable can live outside of function. JS has no block-level scope.

## Namespaces. A JS module should never add more than a single symbol to global namespace.

## Functions as Data, can be assigned to variables. 

preferred 
```
var sum = function(a,b) {return a+b;}; // All functions are nameless in js.
```

Functions as Data // To pass around.

Functions as Methods // A method is a function, and a property of an object.

# Objects
JS objects are based on prototype, not classes. Far more dynamic than more language.

Use new keyword to create an object instance of a class.

```
var Foo = function(attr1, attr2) {
  // this is automatically defined as {}
  this.name = attr1; this.age = attr2;
  // this is automatically returned.
}

var instance_1 = new Foo(xx, bb);
```

Prototype: blueprint for how to build object.

```
ClassA.prototype.funcB = ...
```

this: depends on how it was called, Not how it is defined.

Js has no private or protected. We use trailing underscore for style.

# Javascript on the Web

  Write js code in external file and include using <script> tag.
  ```
  <script src='code.js'></script>
  ```
  Never use self-closing script tag. Won't work in many browsers.
  

  !1 instead of false
  
  Compiler concatenate all the file together.  Compiler does compression, but not real obfuscation.
  
  Best practices: bundle all js code into one file, minimize http requests.
  
## DOM
document object refers to the body. More in Mozilla's DOM reference.
Tutorial on Javascript accesing DOM: https://dom-tutorials.appspot.com/static/1.html

```
document.getElementById('elementId')
document.getElementById('star').src = 'star_on.gif';
childNodes
lastChild; firstChild;
parentNode;
previousSibling; nextSibling;
document.getElementById('stars').childNodes[1].src = 'star_on.gif';
document.getElementById('phrase').lastChild.firstChild.src = 'star_on.gif';
document.getElementById('laststar').previousSibling.previousSibling.src = 'star_on.gif';
```
  
Exercise: write a tree walker for next node.
  
## Node Properties
querySelectorAll()
Many selectors are not supported in IE7 and earlier.
jQuery 就是专门做这件事的，兼容地做query select.

## Manipulating the DOM
Tutorial

```
node.innerHTML // Never use again. It's very dangerous for script injection.
node1.removeChild(node2);
node1.appendChild(node2);
document.createTextNode('hi')
document.createElement('IMG');  // params is the TAG name.
```

## Creating DOM Nodes
```
createElement()
setAttribute()
appendChild()
.className = 'xxx;

.insertBefore
.replaceChild
.removeChild
```

## Javascript and CSS
Learn CSS and use it as much as possible. Realy powerful.
```
img.className += 'abc'
Closure: .hasClass; .addClass, .removeClass
node.style.XXX = 'xxx';
```

# Event Handling
