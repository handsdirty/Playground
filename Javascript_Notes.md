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

