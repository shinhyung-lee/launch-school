
## Table of Contents
OOP with JS Book. 

[Prototypal Inheritance](#prototypal-inheritance). 

[Constuctor Function vs. Pseudo Classical Pattern](#constuctor-function-vs-pseudo-classical-pattern). 

[Factory Functions](#factory-functions). 

[Object Factory](#object-factory). 

[Private Fields](#private-fields). 

[Static Fields and Methods](#static-fields-and-methods). 

[Garbage Collection](#garbage-collection). 

[PFA](#pfa). 

[IIFE](#iife). 


## Colors
<span style="color: #E74689; font-weight: bold;">pink</span>\
<span style="color: #0096FF; font-weight: bold;">blue</span>\
<span style="color: #40E0D0; font-weight: bold;">mint</span>


## Prototypal-Inheritance
- Need to understand prototypes (2 kinds exist)
  - function prototypes
  - object prototypes

## Prototype are Objects
- Prototypes in JS are "objects" (function prototype and object prototype alike)
  - Down the prototype chain, `null` is the terminator, which is not an object


### Function Prototype
- aka: constructor's prototype, constructor's prototype object, `prototype` property 
- Note that constructors don't inherit from the constructor's prototype object.
  - Instead, the objects that the constructor creates inherit from it.
<br>

- <span style='color: #40E0D0; font-weight: bold;'>"Most"</span> JS functions and classes have a property named `prototype`
- This property usually <span style='color: #E74689; font-weight: bold;'>references an object</span> that is called the function prototype.

- imagine we have the following code:

```javascript
class Cat {
  constructor(name, color) {
    this.name = name;
    this.color = color;
  }

  whoAmI() {
    console.log(`My name is ${this.name}.`,
                `\nI am a ${this.color} cat.`);
  }
}
```

- When JS encounters the class definition in the code, it creates a `Cat` function called the constructor function (not the same as constructor method)
- It then creates an object that contains the `constructor` and `whoAmI` methods
- and assigns the object to the `Cat.prototype` property
- This object is referred to as the "function prototype" for the `Cat` class.

- (continuing...)
- `Cat.prototype` object is the function prototype for `Cat`, and it contains the methods (`constructor` and `whoAmI`) that will be shared by all instances created from the `Cat` class.
  - The `Animal.prototype` contains methods defined in the Animal class, and `Cat.prototype` contains methods defined in the Cat class

### ⭐️ Quirks with `prototype` property
- most JS functions have a `prototype` property
- However, JS only uses the property when we call that function as a constructor, with using the `new` keyword


### Object Prototype
- All JavaScript objects have an object prototype
- The object prototype for an object is an object that contains the methods that an object inherits

```javascript
class Cat {
  constructor(name, color) {
    this.name = name;
    this.color = color;
  }

  whoAmI() {
    console.log(`My name is ${this.name}.`,
                `\nI am a ${this.color} cat.`);
  }
}

let cheddar = new Cat('Cheddar', 'ginger');
let cheddarProto = Object.getPrototypeOf(cheddar);

console.log(Object.getPrototypeOf(cheddar) === Cat.prototype);
// object prototype of cheddar is function prototype of the constructor function(Cat.prototype)
console.log(Object.getOwnPropertyNames(cheddarProto));
// ['constructor', 'whoAmI'];

cheddar.whoAmI();  // My name is Cheddar.
                   // I am a ginger cat.
```

- we create an instance of Cat class, `cheddar`
- <span style="color: #40E0D0; font-weight: bold;">When we call a constructor function with the `new` keyword, JavaScript takes the function prototype of the constructor (Cat.prototype here) and assigns it as the object prototype of the object created by the constructor.</span>
- an object prototype is, by default, identical to the function prototype of the object's constructor function


### Above Process in More Detail
<b>IMPORTANT</b>\
`let cheddar = new Cat('Cheddar', 'ginger');`
1. It creates an <u>entirely new object</u>.
2. It sets `Cat.prototype` as the (object) prototype for the new object. That is, the new object inherits from the object referenced by `Foo.prototype`.
3. It sets the execution context (`this`) for the function to point to the new object.
4. It invokes the function.
5. It returns the new object unless the function returns another object.
<br>
<br>

### Significance of `constructor` property
- lets us determine the type of an object
```javascript
// code omitted for Dog constructor function
let maxi = new Dog('Maxi', 'German Shepherd', 32);

if (maxi.constructor === Dog) {
  console.log("It's a dog");
} else {
  console.log("It's not a dog");
}
```

- It is possible to reassign the `constructor` property to something else.
```javascript
Dog.prototype.constructor = function() {};

maxi.constructor === Dog; // false
maxi instanceof Dog; // true (still works)
```



### Accessing Object Prototype of an instance
`let cheddar = new Cat('cheddar', 'ginger')`

Object prototype accessible via: `Object.getPrototypeOf(cheddar)`
- object prototype is identical to function prototype of the object's constructor function `Cat.prototype` 

### Checking Prototype Chain 
- via `Object.prototype.isPrototypeOf`
  - to determine whether an object is part of another object's prototype chain

```javascript
let foo = { a: 1, b: 2 }

let bar = Object.create(foo);
let baz = Object.create(bar);
let qux = Object.create(baz);

Object.getPrototypeOf(qux) === baz; // true
Object.getPrototypeOf(baz) === bar; // true
Object.getPrototypeOf(bar) === foo; // true

foo.isPrototypeOf(qux); // true - because foo is on qux's prototype chain
```
- interesting analogy: my grandma ("정을순 할머니").isPrototypeOf("Shin")
  - `("정을순 할머니").isPrototypeOf("Shin")` traverses `Shin`'s prototype chain until we find `정을순 할머니`
- `foo.isPrototypeOf(qux)` traverses `qux`'s prototype chain until we find `foo`

### Object.prototype at the end of the prototype chain for all Javascript objects
- if you don't create an object from a prototype, its prototype is the `Object.prototype` object

```javascript
let foo = { a: 1, b: 2 };
Object.getPrototypeOf(foo) === Object.prototype; // true
```


### Reassigning Object Prototypes
- Possible with `Object.setPrototypeOf()` method
  - Gives an object an entirely new object prototype

```javascript
class Animal {}
class Cat extends Animal {}

let cat = new Cat();
let catProto = Object.getPrototypeOf(cat);
console.log(catProto === Cat.prototype);   // true

let myProto = {
  meow() {
    console.log("Meow!");
  }
};

Object.setPrototypeOf(cat, myProto);
catProto = Object.getPrototypeOf(cat);

cat.meow();                                // Meow!
console.log(catProto === Cat.prototype);   // false
console.log(catProto === myProto);         // true
```


### Function Prototype's Object Prototype
- Yes. Interestingly, function prototypes also have object prototypes. 
- <span style="color: #0096FF; font-weight: bold;">By default, the object prototype of a function prototype is the function prototype of the superclass.</span>


```javascript
class Animal {
  constructor(type) {
    this.type = type;
  }

  eat() {
    console.log("I am eating.");
  }
}

class Cat extends Animal {
  constructor(name, color) {
    super();
    this.name = name;
    this.color = color;
  }

  whoAmI() {
    console.log(`My name is ${this.name}.`,
                `\nI am a ${this.color} cat.`);
  }
}

let cheddar = new Cat('Cheddar', 'ginger');
let cheddarProto = Object.getPrototypeOf(cheddar);
console.log(Object.getPrototypeOf(cheddar) === Cat.prototype);
// cheddar's object prototype is Cat constructor function's function prototype

let cheddarProto2 = Object.getPrototypeOf(cheddarProto);
// Getting the Object prototype (via Object.getPrototypeOf)
// of Function prototype (cheddarProto, we know cheddarProto === Cat.prototype)
console.log(Object.getOwnPropertyNames(cheddarProto));
// ['constructor', 'whoAmI'];

console.log(Object.getOwnPropertyNames(cheddarProto2));
// ['constructor', 'eat'];

console.log(cheddarProto2 === Animal.prototype); // true
// Object prototype of function prototype 
// is the function prototype of the superclass (Animal.prototype)

cheddar.whoAmI();  // My name is Cheddar.
                   // I am a ginger cat.
cheddar.eat();     // I am eating.
```

### Prototype Chain
With almost all objects, you can follow this "chain" of object prototypes all the way back to a prototype object called `Object.prototype`
- Since `Object.prototype`'s object prototype is `null`, every JavaScript prototype chain ultimately ends with `null`

- When JavaScript looks for a method associated with an instance object, JavaScript first looks for it in the object itself
  - If it doesn't find the method, it looks at the <span style='color: #E74689; font-weight: bold;'>object prototype</span> next
- However, JavaScript won't always find the method in one of these locations. 
  - When it doesn't find it, JavaScript searches the remainder of the object's prototype chain. 
  - It stops searching when it sees the method or reaches the end of the chain (`null`)

1. The prototype chain begins by looking for the requested method in the calling object
if it doesn't find the method there,
2. JavaScript next looks in the object prototype for the calling object
if the method still isn't found
3. JavaScript searches the object prototype of the inherited object, if any.
4. JavaScript will continue to search inherited object prototypes until it finds the method or an object prototype of null

```javascript
function SmartPhone(brand, model, releaseYear) {
  this.brand = brand;
  this.model = model;
  this.releaseYear = releaseYear;
}

SmartPhone.prototype.checkBattery = function() {
  console.log(`Phone has ${this.batteryLevel}% battery left`);
};

SmartPhone.prototype.displayInfo = function() {
  console.log(`${this.brand} ${this.model} released in ${this.releaseYear}`);
};

SmartPhone.prototype.batteryLevel = 100;

let iphone12 = new SmartPhone('Apple', 'iPhone12', 2020);

// iphone12.checkBattery();
// iphone12.displayInfo();
// console.log(Object.getOwnPropertyNames(SmartPhone.prototype));
// console.log(SmartPhone.prototype.constructor === SmartPhone);
let iphoneProto = Object.getPrototypeOf(iphone12);
console.log(iphoneProto === SmartPhone.prototype);
console.log(Object.getOwnPropertyNames(iphoneProto));
// [ 'constructor', 'checkBattery', 'displayInfo', 'batteryLevel' ]

let iphoneProto2 = Object.getPrototypeOf(iphoneProto);
console.log(iphoneProto2 === Object.prototype);
console.log(Object.getOwnPropertyNames(iphoneProto2));
/*
[
  'constructor',
  '__defineGetter__',
  '__defineSetter__',
  'hasOwnProperty',
  '__lookupGetter__',
  '__lookupSetter__',
  'isPrototypeOf',
  'propertyIsEnumerable',
  'toString',
  'valueOf',
  '__proto__',
  'toLocaleString'
]
*/
let iphoneProto3 = Object.getPrototypeOf(iphoneProto2);
console.log(iphoneProto3 === null);
console.log(Object.getOwnPropertyNames(iphoneProto3)); 
// raises an error
// TypeError: Cannot convert undefined or null to object
```

### Prototypal Inheritance and Behavior Delegation
Advantages of using prototypal inheritance and behavior delegation
- We can create dogs much more easily with the dog prototype, and don't have to duplicate say and run on every single dog object
- If we need to add/remove/update behavior to apply to all dogs, we can just modify the prototype object, and all dogs will pick up the changed behavior automatically

- We define a method once in the prototype object, and
  - let the inheriting objects delegate the method calls to the prototype


## Behavior Delegation Perspective
- Top-Down / Design view:
  - objects on the bottom of the prototype chain "inherited" the properties and behaviors of all the upstream objects on the prototype chain

- Bottom-Up / Run time Point of View:
  - objects on the bottom of the prototype chain can "delegate" requests to the upstream objects to be handled



### Objects Created from Object Literal
- aka. "When objects inherit directly from object"
- All objects created from an object literal are instances of the Object class
  - Therefore, their object prototype is the function prototype of the constructor function `Object` (e.g. `Object.prototype`)

```javascript
let obj = { // Object literal
  foo: 42,
};

let objProto = Object.getPrototypeOf(obj);
console.log(objProto === Object.prototype); // true
```

Since object factories use object literals, they also create objects that have Object.prototype as their object prototype:

```javascript
function createObj() {
  return {
    foo: 42,
    hello() {
      console.log('hello world!');
    },
  };
}

let obj = createObj();
let objProto = Object.getPrototypeOf(obj);
console.log(objProto === Object.prototype); // true
```

Note that objects created by new Object() also have Object.prototype as their prototype:
```javascript
let obj = new Object();
let objProto = Object.getPrototypeOf(obj);
console.log(objProto === Object.prototype); // true
```

### Accessing Object Prototypes
- In JS, every object has a hidden property called `[[Prototype]]` that points to its object prototype or `null`.
  - While you can't refer to `[[Prototype]]` directly, you can access the object prototype with the `Object.getPrototypeOf` method 

```javascript
class Animal {}
class Cat extends Animal {}

let cat = new Cat();
console.log(Object.getPrototypeOf(cat));   // Animal {}
```

- `Object.getPrototypeOf` returns the object prototype of an object.
- `Object.getOwnPropertyNames` returns an array with the names of all properties defined by the object given as an argument


### Deprecated __proto__ property
- can be used to access and reassign <span style='color: #E74689; font-weight: bold;'>object prototype</span>
- `__proto__` is officially deprecated
- You should not use it in production code.
  - it's reasonably safe to use when testing or debugging
  - in production code, use `Object.getPrototypeOf` and `Object.setPrototypeOf` instead


```javascript
class Animal {}
class Cat extends Animal {}

let cat = new Cat();
console.log(cat.__proto__); 
// cat's object prototype
// which is function prototype of constructor function `Cat`

class Foo {}
cat.__proto__ = Foo;
console.log(cat.__proto__); // [class Foo]
```

### Accessing Function Prototypes
A function prototype can be <span style='color: #E74689; font-weight: bold;'>accessed or changed</span> by using the `prototype` property on the function or class


```javascript
class Animal {
  hello() {
    console.log('hello');
  }

  bye() {
    console.log('bye');
  }
}
console.log(Animal.prototype); // {}

Animal.prototype.foo = function() {
  console.log('this is foo');
};

Animal.prototype.bar = function() {
  console.log('this is bar');
};

console.log(Animal.prototype);
// { foo: [Function (anonymous)],
//   bar: [Function (anonymous)] }
```

### Object Prototypes for Functions and Classes
- Functions and classes are also objects
  - That means they have object prototypes in addition to the function prototypes

- With function and class objects, <span style="color: #0096FF; font-weight: bold;">the object prototypes define where JavaScript should look for static methods.</span>

- The object prototypes for functions and classes ultimately chain to `Function.prototype`, which has some useful static methods such as `apply`, `call`, and `bind`

```javascript
class Foo {
  static identity() {
    console.log('This is Foo.identity()');
  }
}

class Bar {
  static whoAmI() {
    console.log('This is Bar.whoAmI()');
  }
}

// Foo and Bar initially have Function.prototype as their
// object prototypes.

// The names `FooProto` and `BarProto` are not consistent
// with JS conventions. We've done this intentionally for
// clarity.

let FooProto = Object.getPrototypeOf(Foo);
console.log(FooProto === Function.prototype); // true

let BarProto = Object.getPrototypeOf(Bar);
console.log(BarProto === Function.prototype); // true

// Let's change Bar's object prototype to Foo, which lets
// Bar inherit Foo's static methods. However, Bar does
// *not* inherit Foo's instance methods.
Object.setPrototypeOf(Bar, Foo);

// Bar can access both Bar.whoAmI and Foo.identity
Bar.whoAmI();       // This is Bar.whoAmI()
Bar.identity();     // This is Foo.identity()
```


### Class Invocation Without `new`
- results in "TypeError: Class constructor Cat cannot be invoked without 'new'"

```javascript
class Cat {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

let ginger = new Cat('ginger', 5);
// TypeError: Class constructor Cat cannot be invoked without 'new'
```

## Arrow Functions and Function Prototypes
- Arrow functions do not have function prototypes.
  - However, they do have object prototypes.

```javascript
let foo = () => console.log('foo');
let fooProto = Object.getPrototypeOf(foo);

console.log(foo.prototype);                   // undefined
console.log(fooProto);                        // {}
console.log(fooProto === Function.prototype); // true
```

- `Object.getPrototypeOf` returns the object prototype of an object
  - In this case, the object is a function, and the function's object prototype is `Function.prototype`
  - That happens to be a function prototype, but it is not the function prototype for foo.
  - The function prototype, which would be referenced by `foo.prototype` if it existed, is undefined since `foo` doesn't have a `prototype` property.

## Prototypal Inheritance vs. Classical Inheritance
Classical Inheritance
- Used in traditional OO languages (Java, C++, Python)
- A class defines the structure and behaviors (methods) objects instantiated from it should have
- A subclass inherits from a superclass and can add or override methods
  - The superclass's methods are available to instances of the subclass unless overridden
- Class-based inheritance is static; 
  - relationships between classes and instances are established at compile time and cannot usually be altered dynamically.
- The lack of flexibility, however, makes classical OO more intuitive to most developers

Prototypal Inheritance
- objects inherit directly from other objects
- There are no actual classes in pure prototypal inheritance
  - the `class` keyword in JS is syntactic sugar that maps to a constructor function and a function prototype
- Prototypal Inheritance allows any object to inherit from any other
- It is dynamic, meaning objects can extend or change their prototype at runtime
- Since the prototypes are all linked via pointers, prototypal inheritance can also use memory more efficiently


### Constructor/Prototype Pattern
- Read code comments for explanation

```javascript
function Animal(name) {
  this.name = name;
}

Animal.prototype.eat = function() {
  console.log(`${this.name} is eating.`);
};

function Mammal(name, hasFur) { // extends Animal
  // super(name) - we need to simulate super()
  Animal.call(this, name); // simulates super()
  // calling Animal constructor function 
  // with `this` as execution context and `name` as an argument
  this.hasFur = hasFur;
}

Mammal.prototype = Object.create(Animal.prototype);
// creating function prototype for Mammal
// Mammal constructor inherits the function prototype of Animal
// `Object.create()` static method creates a new object, using an existing object as the prototype of the newly created object

Mammal.prototype.constructor = Mammal;

Mammal.prototype.sleep = function() {
  console.log(`${this.name} is sleeping.`);
};

function Dog(name, hasFur, breed) { // extends Mammal
  // super(name, hasFur) - we need to simulate super()
  Mammal.call(this, name, hasFur); // simulates super()
  /* 
    - calling Mammal constructor function with
        `this` as execution context and `name` and `hasFur` as arguments 
    - With `this` as the first argument,
        if you're creating a Dog instance, then the `this` argument will reference the Dog instance.
    - Thus, all of the constructors will see the Dog instance as the calling  object

  */
  this.breed = breed;
}

Dog.prototype = Object.create(Mammal.prototype);
/*
By default, a constructor function's `prototype.constructor` property is a reference back to the constructor function
  - When you reassign the prototype property, the constructor subproperty's value no longer references the correct constructor
  - Some JavaScript libraries may break if prototype.constructor is not set correctly

- To ensure it doesn't become a problem, you should assign the prototype.constructor property for each subtype to refer to the subtype's constructor function (BELOW)
*/

Dog.prototype.construtor = Dog;

Dog.prototype.bark = function() {
  console.log(`${this.name} the ${this.breed} is barking.`);
}

let myDog = new Dog('Rex', true, 'German Shepherd');
// Following lines enabled by
// Dog.prototype = Object.create(Mammal.prototype);
console.log(myDog instanceof Dog);     // true
console.log(myDog instanceof Mammal);  // true
console.log(myDog instanceof Animal);  // true
```

### (Digging) inner workings of `instanceof` 
- The `instanceof` operator tests whether the prototype property of a constructor appears anywhere in the prototype chain of an object. It returns `true` if it does, and `false` if it doesn't.

How `instanceof` works

Here's a step-by-step look at the inner workings when you run an expression like object instanceof Constructor:

1.  JavaScript first gets the object that `Constructor.prototype` points to.
2.  Then, it gets the prototype of object using an internal equivalent of `Object.getPrototypeOf(object)`.
3.  It compares the two. If they are the same object, `instanceof` returns true.
4.  If they are not the same, JavaScript traverses up the prototype chain. It gets the prototype of the current prototype object and repeats the comparison.
5.  This process continues until it either finds a match (returning true) or reaches the end of the prototype chain, where the prototype is null (returning false).

Following the Prototype Chain

Yes, instanceof is designed specifically to follow the prototype chain. This is its primary function.

Let's look at an example from the curriculum to illustrate this:

```javascript
// A constructor function
let Point = function(x = 0, y = 0) {
  this.x = x;
  this.y = y;
};

// Create a new object using the constructor
let pointA = new Point(30, 40);

// Let's check the relationships
console.log(pointA instanceof Point);   // => true
console.log(pointA instanceof Object);  // => true
```

Here’s why both of those checks return true:

1.  ​pointA instanceof Point​:
  - JavaScript checks if Point.prototype is in pointA's prototype chain.
  - When we created pointA with new Point(), JavaScript set pointA's prototype to Point.prototype.
  - Since Object.getPrototypeOf(pointA) is strictly equal to Point.prototype, the check finds a match on the first step and returns true.

2.  ​pointA instanceof Object​:
  - JavaScript checks if Object.prototype is in pointA's prototype chain.
  - The prototype of pointA is Point.prototype.
  - The prototype of Point.prototype is Object.prototype (since the Point constructor's prototype is a plain object created by JavaScript).
  - Because instanceof traverses the chain, it finds Object.prototype one level up from Point.prototype and returns true.

The prototype chain for pointA looks like this:

`pointA ---> Point.prototype ---> Object.prototype ---> null`

As you can see, both `Point.prototype` and `Object.prototype` are on the chain, which is why instanceof works for both constructors.


### Object.create()
[mdn link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
- `Object.create()` static method creates a new object, using an existing object as the prototype of the newly created object

```javascript
const person = {
  isHuman: false,
  printIntroduction() {
    console.log(`My name is ${this.name}. Am I human? ${this.isHuman}`);
  },
};

const me = Object.create(person);
console.log(Object.getPrototypeOf(me) === person);
```

- `me` is a new object whose prototype is `person`.

### Object.prototype.hasOwnProperty()
- returns a boolean indicating whether this object has the specified property as its own property (as opposed to inheriting it)

## Object.prototype.hasOwnProperty() vs. Object.hasOwn()
static method [Object.hasOwn](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)

instance method [Object.prototype.hasOwnProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty)

- Object.hasOwn static method is recommended over Object.prototype.hasOwnProperty
- `Object.prototype.hasOwnproperty` assumes we have access to `hasOwnProperty` method through its prototype chain.
- `Object.hasOwn` static method doesn't depend on the object's prototype

```javascript
const me = Object.create(null);
me.age = 45;

console.log(Object.hasOwn(me, 'age')); // 45
console.log(me.hasOwnProperty('age')); // TypeError: me.hasOwnProperty is not a function
```

Another possibility: an object can override `hasOwnProperty`

```javascript
const person = {
  name: "John",
  hasOwnProperty: "hello",
};

person.hasOwnProperty("name"); // TypeError: person.hasOwnProperty is not a function

// On the other hand, still safe to use `Object.hasOwn` static method
console.log(Object.hasOwn(person, 'name')); // true
```


## Three Significant Steps to have subtype inherit from supertype when using constructor/prototype pattern
1. Replace the function prototype for each subtype's constructor. To do that, use Object.create with an argument referencing the supertype's function prototype, and assign it to the subtype constructor's prototype property
2. Set the subtype's prototype.constructor property to the subtype's constructor function
3. In the subtype's constructor, call the supertype's constructor using Function.prototype.call. You should pass this as the first argument to call followed by the arguments for the supertype's constructor

## Constuctor-Function-vs-Pseudo-Classical-Pattern
- The Pseudo-classical pattern is a combination of the constructor pattern and the prototype pattern
- we use a constructor to set object states, 
- and put shared methods on the constructor function's prototype
- A constructor function is a component of the pseudo-classical pattern

- A ​constructor function​ is a function used with the new keyword to create and initialize an object's state (its unique properties).
- The ​pseudo-classical pattern​ is a complete object-creation pattern that uses a constructor function to set "state", and then defines "shared behaviors" (methods) on the constructor's prototype property.

```javascript
// This is the constructor function. It defines the 'state' of a person.
function Person(name) {
  this.name = name;
}

// This is the other part of the pseudo-classical pattern:
// defining shared behavior on the constructor's prototype.
Person.prototype.sayHello = function() {
  console.log(`Hello, my name is ${this.name}.`);
};

// 'new Person()' uses the constructor to create an object,
// which also inherits methods from Person.prototype.
let shin = new Person('Shin');
shin.sayHello(); // => Hello, my name is Shin.
```

- `Person` is the constructor function
- the combination of `Person` constructor and the assignment to `Person.prototype.sayHello` demonstrates the full pseudo-classical pattern.

## OLOO (Object Linking to Other Objects)
- not widely used these days
- included in LS curriculum for historical reasons
- Won't be on JS229 assessment.

This pattern doesn't use constructor functions. Instead, it defines methods on a prototype object, then uses Object.create to instantiate objects that inherit from the prototype.


## Factory-Functions
- aka. Using functions as object factories
- provides a way to create objects based on a pre-defined template

```javascript
function createPerson(firstName, lastName) {
  let person = {};
  person.firstName = firstName;
  person.lastName = lastName || '';
  person.fullName = function() {
    return (this.firstName + ' ' + this.lastName).trim();
  };

  return person;
}

let john = createPerson('John', 'Doe');
let jane = createPerson('Jane');

john.fullName();        // "John Doe"
jane.fullName();        // "Jane"
```

We could just return an object literal, as follows:
```javascript
function createPerson(firstName, lastName='') {
  return {
    firstName,
    lastName,
    fullName() {
      return (this.firstName + ' ' + this.lastName).trim();
    },
  };
}
```

Limitations of Factory Function
- Every object created with the factory function has a full copy of all the methods and properties, which can be redundant.
- There isn't a way for us to inspect an object and know whether we created it from a factory function. This makes it difficult to identify whether an object is of a specific "type."

## Object-Factory
- in Study Guide, so study with care
- in JS, object factories enables creation of multiple instances of similar objects <u>without defining a specific type</u>.

- Factory function below:

```javascript
function createCat(name, color, age) {
  return {
    name: name,
    color: color,
    age: age,

    speak() {
      console.log(
        `Meow. I am ${this.name}. ` +
        `I am a ${this.age}-year-old ${this.color} cat.`
      );
    }
  };
}

let cocoa = createCat("Cocoa", "black", 5);
let leo = createCat("Leo", "orange", 3);

cocoa.speak();
// Meow. I am Cocoa. I am a 5-year-old black cat.

leo.speak();
// Meow. I am Leo. I am a 3-year-old orange cat.
```
<br>

- `createCat` returns an object, that represents a cat with name, color, and age provided by the arguments.

Advantages of Object Factory
- when inheritance isn't needed, object factories can provide a more straightforward way to create objects 
- Object factories also bypass execution context `this` 
- Everything your object needs will typically be built-in to the object, with no dependencies on the execution context
<br>
<br>

Disadvantages of Object Factory
- Each object created by a factory function gets copies of the methods defined by the returned object
  - For this reason, <u>factory functions</u> can use high amounts of memory when creating many objects
- Implementing inheritance using object factories can be more cumbersome and less performance-efficient than the more advanced approaches.
  - it can involve manually copying methods from one object type to another.
  - <span style='color: pink;'>How is this done? Look into it</span>
- <span style='color: #40E0D0; font-weight: bold;'>objects created by object factory don't have a "type"</span>

```javascript
function Foo() {
  return {
    foo: 42,
  };
}

let obj = Foo();
console.log(obj instanceof Foo); // false
console.log(obj.constructor);    // [Function: Object]
```


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

### Static Properties (Constructor/Prototype Syntax)
- Static properties are defined and accessed directly on the constructor, not on an instance or a prototype
  - static properties belong to the type (e.g., Dog) rather than to the individual instances or the prototype object

```javascript
// static property about Dog species
// does not belong to instance objects
Dog.species = "Canis lupus";

console.log(`Dogs belong to the species ${Dog.species}`);
```

Common use case 
- to keep track of all of the objects created by a constructor
```javascript
function Dog(name, breed, weight) {
  this.name = name;
  this.breed = breed;
  this.weight = weight;
  Dog.allDogs.push(this);
}

Dog.allDogs = [];
```

### Static Methods (Constructor/Prototype Syntax)
- Static properties don't have to be ordinary data properties. 
- You can also define static methods:
```javascript
Dog.showSpecies = function() {
  console.log(`Dogs belong to the species ${Dog.species}`);
};

Dog.showSpecies();
```
- Other examples of static methods on built in javascript constructors:
  - `Object.assign`, `Array.isArray`, `Date.now`

## Static Fields (Class syntax)
- aka 'static properties' or 'class properties'
- properties defined on the class itself.
- not tied to an instance of the class
  - used to store constants or utility data shared across all class instances


## Static Methods (Class syntax)
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

## Garbage-Collection
In JS, values are allocated memory when they are created, and they are eventually,
"automatically" freed up when not in use.\
This process of "automatically" freeing memory up is called **garbage-collection**.

Unlike JavaScript, programming languages (such as C) that don't have garbage collection make the developer write code to deallocate (unclaim or release) memory when the program no longer needs the data. 

JavaScript allocates memory for us and has GC, so this intricate dance of claim/test/copy/use/release isn't necessary

```javascript
let name = 'Sarah';   // Declare a variable and set its value. The JavaScript
                      // runtime automatically allocates the memory.
console.log(name);    // Do something with name
```

- we don't need code to claim and release memory
  - JavaScript runtime handles that for us.
- That is, when there are no variables, objects, or closures that maintain a reference to the object or value, JavaScript marks the memory as eligible for GC.


<span style="color: #E74689; font-weight: bold;">That is, when there are no variables, objects, or closures that maintain a reference to the object or value, JavaScript marks the memory as eligible for GC.</span>



## PFA 
Partial Function Application

What is PFA?
- Partial function application uses a function (we'll call it the generator) that creates a new function (the applicator) to call a third function (the primary).

```javascript
function makeAddN(addend) {                 // generator
  // Saves addend via closure; uses addend when function invoked.
  return function(number) {                 // applicator
    return add(addend, number);             // call primary
  }
}

let add1 = makeAddN(1);
add1(1);                           // 2
add1(41);                          // 42

let add9 = makeAddN(9);
add9(1);                           // 10
add9(9);                           // 18
```

PFA applies some of the function's arguments (the add function's first argument here) when called, and supplies the remaining arguments when you call the returned function.
- Partial function application refers to the creation of a function that can call a second function with fewer arguments than the second function expects.



## IIFE
Immediately Invoked Function Expression

Function that we define and invoke simultaneously.

#### Valid Syntax
```javascript
(function() {
  console.log('hello');
})();                     // => hello
```

- parentheses around function expression are needed
- Without them, we can't invoke the function right away: 

#### Invalid Syntax
```javascript
function() {
  console.log('hello');
}();                      // SyntaxError: Unexpected token
```

In JS, surrounding a value with parentheses ( ) doesn't change the value. 
- It is a grouping operator that controls the evaluation in expressions.

```javascript
> (3)
= 3
> (['apple', 'carrot'])
= ["apple", "carrot"]
```

With IIFEs, we use the parentheses to make it explicit that we want to parse the function definition as an expression. 
- As an expression it means that there is a value returned — the function — that we can immediately "invoke."

### Alternate Style IIFE

```javascript
(function() {
  console.log('hello');
}());
```
- argument list is inside the outer set of parentheses.

We can omit the parentheses around an IIFE when the function definition is an expression that doesn't occur at the beginning of a line (recall the earlier invalid syntax example):

```javascript
let foo = function() {
  return function() {
    return 10;
  }();
}();

console.log(foo);       // => 10
```

### IIFE to return a function with access to private data

```javascript
let generateStudentId = (function() {
  let studentId = 0;

  return function() {
    studentId += 1;
    return studentId;
  };
})();

generateStudentId();          // 1
generateStudentId();          // 2
generateStudentId();          // 3
```


### IIFE to return an Object with private data
- we have an inventory object that maintains a list of stock objects
- has a method that logs the stock count of each item.

```javascript
let inventory = (function() {
  let stocks = [];
  let isValid = function(newStock) {
    return stocks.every(function(stock) {
      return newStock.name !== stock.name;
    });
  }

  return {
    stockCounts() {
      stocks.forEach(function(stock) {
        console.log(stock.name + ': ' + String(stock.count));
      });
    },
    addStock(newStock) {
      if (isValid(newStock)) { stocks.push(newStock) }
    },
  }
})()
```

- prevents stock with same name from being added to stock
- stock is added through `addStock` method only

