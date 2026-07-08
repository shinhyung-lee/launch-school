/*
Write a function called swap that takes a string as an argument, 
and returns a new string, where the alphabetic characters have taken 
the place of the numeric characters, and vice versa.

Input: string
Output: string

===== Questions =====
Q. What if the string is all alphabetic characters or digits?
  - return string as is

Q. Empty string argument?
  - return string as is

Q. What if the argument is not a string?
  - return null

Q. What if there is more alphabetic chars or digits than the other?
  - preserve the remaining ones' positions

Q. What if string has non-letter, non-digit characters?
  - ignore them

Data Structures
- array
  - [['a', 1], ['b', 2]];
  - [[1, 4], [2, 5], [3, 5]];
- object
  - store letters, digits

- string
  - input
  - output

Algo
swap (Main Func)
- Initialize an empty array `letters`
- Initialize an empty array `digits`
- If string is an empty string, return as is
- If argument is not of type string, return null
- Split string with empty string delimiter and initialize an array `strArr`
- Iterate over every character in string, with idx
  - If char is letter,
    - Push `idx` into `letters`
  - If char is digit,
    - Push `idx`into `digits`
- Initialize `swapLength` and assign smaller value between `letters.length` vs.
    `digits.length`
- for `idx` from `0` to `swapLength - 1`,
  - `letterIdx` = `letters[idx]`
  - `digitIdx` = `digits[idx]`
  - swap (HELPER) chars (digit <> letter) from `strArr` array.
  
- Join `strArr` and return

swapValuesInArray 
- Input: reference to an array, idx, idx
- Output: none (side effect only)

Data Structures:
  - Array
  - Numbers (idx value)

Algo:
  - Swap 
    arr[digitIdx], arr[letterIdx] = arr[letterIdx], arr[digitIdx]
*/

function isLetter(char) {
  return /[a-z]/i.test(char);
}

function isDigit(char) {
  return /[0-9]/.test(char);
}

function swap(str) {
  if (typeof str !== 'string') { return null; }

  if (str === '') { return str; }

  let strArr = str.split('');
  let letters = [];
  //strArr.filter(isLetter);
  let digits = [];
  //strArr.filter(isDigit);
  // console.log(letters);
  // console.log(digits);
  // console.log(strArr);
  for (let i = 0; i < strArr.length; i += 1) {
    let char = strArr[i];
    if (isLetter(char)) {
      letters.push(i);
    }

    if (isDigit(char)) {
      digits.push(i);
    }
  }

  // console.log(letters);
  // console.log(digits)
  let swapLength = Math.min(letters.length, digits.length);
  // console.log(swapLength)
  for (let i = 0; i < swapLength; i += 1) {
    let letterIdx = letters[i];
    let digitIdx = digits[i];
    // let temp = strArr[digitIdx];
    // strArr[digitIdx] = strArr[letterIdx];
    // strArr[letterIdx] = temp;
    [strArr[digitIdx], strArr[letterIdx]] = [strArr[letterIdx], strArr[digitIdx]];
  }
  // console.log(strArr);
  return strArr.join('');
}

// Edge Cases
console.log(swap("") === "")
console.log(swap([1, 2, 3]) === null);
console.log(swap({ a: 1, b: 2, c: 3 }) === null);


// General Cases
console.log(swap("1a2b3c") === "a1b2c3"); // true
console.log(swap("abcd123") === "123dabc"); // true
console.log(swap("abcd") === "abcd"); // true

// // Non-letter, non-digit cases
console.log(swap("abcd_-.123") === "123d_-.abc"); // true
console.log(swap("_-.123") === "_-.123"); // true
console.log(swap("abc _-.") === "abc _-."); // true