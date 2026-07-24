/*
=== Problem ===
Input: a number (int)
Output: a number (int)
      - next featured number greater than the input

Rules:
  *** Featured Number ***
    - odd number
    - multiple of 7
    - all of its digits occurring exactly once each

  - Largest possible featured number: 9876543201

=== Examples ===
12 => 21
20 => 21
21 => 35 
  - odd, multiple of 7, all digits occurring exactly once 

=== Data Structures ===
- Number (int): 
  - input
  - output

- String:
  - indexOf (returns the first occurrence)

=== Brainstorm ===
- 3 HELPER functions
  - isOdd
    - input: number
    - output: boolean

  - isMultipleSeven
    - input: number
    - output: boolean

  - hasUniqueDigits
    - input: number
    - output: boolean
    - convert number to string `numString`
    - for loop - each char in `numString` (with `idx`)
      - initialize `char` to string at idx `numString[idx]`
      - if `numString.indexOf(char) !== idx`,
        - return false

    - return true 

=== Algorithms ===
- hasUniqueDigits
    - input: number
    - output: boolean
    - convert number to string `numString`
    - for loop - each char in `numString` (with `idx`)
      - initialize `char` to string at idx `numString[idx]`
      - if `numString.indexOf(char) !== idx`,
        - return false

    - return true

MAIN ALGORITHM
- initialize a variable `currNum` 
- if `num + 1` is odd, `num + 1` 
- else `num + 2` is assigned to `currNum`
- initialize a variable `isOddMultipleOfSeven` to `false`
- while `currNum` is not a multiple of seven, 
  - increment `currNum` by 2 each iteration
  - if a multiple of seven is found, 
    - reassign `isOddMultipleOfSeven` to `true`
- at this point, number is a multiple of seven and odd 
- while `currNum` is not `hasUniqueDigits` number && 
        `currNum` <= 9876543201
  - increment `currNum` by 7
- return currNum
*/
const isOdd = (num) => num % 2 === 1;
const isMultipleSeven = (num) => num % 7 === 0;

function featured(num) {
  let currNum = isOdd(num + 1) ? num + 1 : num + 2;

  let isOddMultipleOfSeven = false;
  while (!isMultipleSeven(currNum)) {
    currNum += 2; // already odd number, so increment by 2 and check
  }

  while (!hasUniqueDigits(currNum) && currNum <= 9876543201) {
    currNum += 14;
  }

  if (currNum > 9876543201) {
    return 'There is no possible number that fulfills those requirements.';
  }

  return currNum;
}


function hasUniqueDigits(num) {
  let numString = String(num);
  for (let idx = 0; idx < numString.length; idx += 1) {
    let char = numString[idx];
    if (numString.indexOf(char) !== idx) {
      return false;
    }
  }

  return true;
}

console.log(featured(12));           // 21
console.log(featured(20));           // 21
console.log(featured(21));           // 35
console.log(featured(997));          // 1029
console.log(featured(1029));         // 1043
console.log(featured(999999));       // 1023547
console.log(featured(999999987));    // 1023456987
console.log(featured(9876543186));   // 9876543201
console.log(featured(9876543200));   // 9876543201
console.log(featured(9876543201));   // "There is no possible number that fulfills those requirements."