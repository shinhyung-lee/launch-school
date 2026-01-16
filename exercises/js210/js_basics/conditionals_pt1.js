const myBoolean = true;
const myString = 'hello';
const myArray = [];
const myOtherString = '';

if (myBoolean) {
  console.log('Hello'); // prints 
}

if (!myString) {
  console.log('World'); // does not print 
}

if (!!myArray) {
  console.log('World'); // prints
}

if (myOtherString || myArray) {
  console.log('!'); // prints
}