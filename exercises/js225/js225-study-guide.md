
## Table of Contents
OOP with JS Book. 

[Private Fields](#private-fields). 
[Static Fields and Methods](#static-fields-and-methods). 


## Private-Fields
- aka 'private instance properties', or confusingly, 'private class fields'
  - object properties that are private to an object
  - No other objects can access them directly.
  - aids encapsulation and prevents your class's users from misusing your object properties

- Private field name is prefixed by a `#` character
- Must declare (and optionally initialize) the field at the class level:
```javascript
class Foo {
  // Next 2 lines declare #data and #initializedData fields
  #data;                      // uninitialized private field
  #initializedData = 43;      // initialized private field

  constructor(value) {
    this.#data = value;
  }

  show() {
    console.log(this.#data, this.#initializedData);
  }
}

let foo = new Foo(42);
foo.show();         // 42 43
```



## Static-Fields-and-Methods

## Static Fields
- aka 'static properties' or 'class properties'
- properties defined on the class itself.
- not tied to an instance of the class
  - used to store constants or utility data shared across all class instances

## Static Methods
- aka 'class methods'
- defined on a class rather than instance objects
- NOT available from class instances
- provides utility functions that perform tasks relevant to the class but do not require access to instance-specific data.

```javascript
class MyClass {
  static staticMethod() {
    console.log('This is a static method.');
  }

  instanceMethod() {
    console.log('This is an instance method.');
  }
}

// Calling the static method
MyClass.staticMethod();    // This is a static method.

const instance = new MyClass();

instance.instanceMethod(); // This is an instance method.
instance.staticMethod();   // Raises error
```

A common use case for static methods is to report data relevant to a class:

```javascript
class Student {
  static counter = 0;

  static showCounter() {
    console.log(`We have created ${Student.counter} students!`);
  }

  constructor(name) {
    this.name = name;
    Student.counter += 1;
  }

}

let ken = new Student('Ken');
let lynn = new Student('Lynn');
Student.showCounter();        // We have created 2 students!
```





    