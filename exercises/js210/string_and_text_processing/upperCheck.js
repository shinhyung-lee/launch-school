/* 
Write a function that takes a string argument and returns true if all of the alphabetic characters inside the string are uppercase; otherwise, return false. Ignore characters that are not alphabetic.

P (understand the Problem)
 
Explicit Rules:
  - only alphabetic chars count
  - empty space, number, special characters don't count
Implicit Rules:
  - empty string returns true 

E (Examples)
  '' => true
  '4SCORE!' => true
  't' => false
D
  - string 
    - string iteration   
A
  function `isUppercase` Algo
  - input: string
  - output: boolean 

  - if `string` is an empty string, return `true`
  - iterate string from `idx` 0 to `string.length - 1`
    - `char` is a character at current `idx`
    - if `char` is alphabetic
      - if `char` is NOT equal to lowerCased `char`
        - return `false`
  - return `true` 

  function `isAlpha` Algo
  - input: `char` is a string with length 1 
  - output: boolean
  
  - if `char` is greater than or equal to `a` and less than or equal to `z`
    - OR
    - if `char` is greater than or equal to `A` and less than or equal to `Z`
      - return `true`
  - otherwise, return `false`
C

*/

function isAlpha(char) {
  return (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z');
}

function isUppercase(string) {
  if (string === '') {
    return true;
  }

  for (let idx = 0; idx < string.length; idx += 1) {
    let char = string[idx];
    // console.log(`idx ${idx}`);
    if (isAlpha(char)) {
      // console.log(`char ${char}`);
      // trying to see if string is all uppercase letters 
      if (char !== char.toUpperCase()) {
        return false;
      }
    }
  }

  return true;
}

console.log(isUppercase('t'));               // false
console.log(isUppercase('T'));               // true
console.log(isUppercase('Four Score'));      // false
console.log(isUppercase('FOUR SCORE'));      // true
console.log(isUppercase('4SCORE!'));         // true
console.log(isUppercase(''));                // true