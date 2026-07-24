/*
Write a function that displays a four-pointed diamond in an "nxn" grid, 
where n is an odd integer supplied as an argument to the function. 
You may assume that the argument will always be an odd integer.

=== Problem ===
Input: an int (n)
Output: a string (n * n) 

Rules:
  - argument will always be an odd integer

=== Examples ===
1 => *
3 => 
 *
***
 *

9 =>
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

=== Data Structures ===
- Int: (input)
- string: (output) 

=== Brainstorm ===
- for each line, number of char = `num` (input)
- middle line (idx)
  - Math.ceil(num / 2)
  - Math.ceil(3 / 2) = 1
  - Math.ceil(9 / 2) = 4

- numStar = 1
- idx 0 to middleIdx,
  - start from 1 star in that line
  - increment `numStar` by 2
- idx middleIdx to String(num).length - 1,
  - decrement `numStar` by 2

How to center the stars?
  - totalChar = `num`
  - numSpace = (`totalChar` - `numStar`) / 2
  - line = `${' '.repeat(numSpace)}${'*'.repeat(numStar)}${' '.repeat(numSpace)}\n`

=== Algorithms ===
- initialize a variable `result` to an empty string
- initialize a variable `middleIdx` to `Math.ceil(num / 2)`
- initialize a variable `numStar` = 1
- initialize a variable `totalChar` to `num`
- for `idx` 0 to idx < num,
  - if idx >= 1 && idx <= middleIdx
    - increment `numStar` by 2
  - else if idx > middleIdx
    - decrement `numStar` by 2

  - numSpace = (`totalChar` - `numStar`) / 2
  - line = `${' '.repeat(numSpace)}${'*'.repeat(numStar)}${' '.repeat(numSpace)}\n`
  - concatenate `line` to `result`

- return result
*/

function diamond(num) {
  let result = '';
  let middleIdx = Math.floor(num / 2);
  let numStar = 1;
  let totalChar = num;

  for (let idx = 0; idx < num; idx += 1) {
    if (idx >= 1 && idx <= middleIdx) {
      numStar += 2;
    } else if (idx > middleIdx) {
      numStar -= 2;
    }

    let numSpace = (totalChar - numStar) / 2;
    let line = `${' '.repeat(numSpace)}${'*'.repeat(numStar)}${' '.repeat(numSpace)}\n`
    result += line;
  }

  return result;
}


console.log(diamond(1));
// logs
// *

console.log(diamond(3));
// logs
//  *
// ***
//  *

console.log(diamond(9));
// logs
//     *
//    ***
//   *****
//  *******
// *********
//  *******
//   *****
//    ***
//     *