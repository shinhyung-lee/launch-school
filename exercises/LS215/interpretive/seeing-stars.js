/*
=== Problem ===
In: an int (odd number to make n * n grid)
Out: a string

Explicit Rules:
  - n is an odd integer
  - n >= 7 

Implicit Rules:
  - middle row is n number of stars (*)
  - other rows have 3 stars 

=== Questions ===
- What if n is not a number?
  - return undefined
- What if n is not a odd number that is >= 7?
  - return undefined


=== Examples ===
n = 7
*  *  *   i = 0, start/end indent: 0, middle indent: 2
 * * *.   i = 1, start/end indent: 1, middle indent: 1
  ***.    i = 2, start/end indent: 2, middle indent: 0
*******
  ***     i = 4, start/end indent: 2, middle indent: 0
 * * *    i = 5, start/end indent: 1, middle indent: 1
*  *  *.  i = 6, start/end indent: 0, middle indent: 2

n = 9
*   *   *.  i = 0, start/end indent: 0, middle indent: 3
 *  *  *.   i = 1, start/end indent: 1, middle indent: 2
  * * *.    i = 2, start/end indent: 2, middle indent: 1
   ***      i = 3, start/end indent: 3, middle indent: 0
*********   i = 4, n * stars
   ***      i = 5, start/end indent: 3, middle indent: 0
  * * *     i = 6, start/end indent: 2, middle indent: 1
 *  *  *.   i = 7, start/end indent: 1, middle indent: 2
*   *   *.  i = 8, start/end indent: 0, middle indent: 3

=== Data Structures ===
- string
  - n lines of string
  - between each line, insert '\n' (newline characater)

- int
  - to calculate start/end indent & middle indent 

=== Brainstorm ===
- middle row is n number of stars (*)
- get the middleIdx
  - middleIdx = Math.floor(n / 2)
  - ie. 7 => 3  Math.floor(n / 2)
  - 9 => 4  
- start idx: 
  - starts from 0 (same as iterating idx)
  - increment by 1 for each following line until `middleIdx`
  - right after middleIdx, still use same start idx
  - subsequently decrement by 1

  - for n = 0 to middleRow
    - startIndent = loop idx (i= 0, 1, 2, 3)
    - when i > middleRow,
      - startIndent = n - idx - 1

- middle idx:
  - except for middle row 
    - numStars = 3
    - (n - ((numStars) + 2 * startIndent)) / 2
    - ie. 7 - ((3) + 2 * 0) = 4 => 4 / 2 = 2
    - ie. 7 - ((3) + 2 * 1) = 2 => 2 / 2 = 1

=== Algorithm ===
- if n is not a number, 
  - return undefined
- if n is less than 7 OR n is not an odd number,
  - return undefined

- initialize `lines` to an empty str
- initialize `startIndent` to 0
- initialize `middleIndent` to 0
- initialize `middleIdx` = Math.floor(n / 2)
- initialize `numStars` = 3
- for every idx in i = 0 to i = n - 1,
  - if i is equal to middleIdx,
    - concatenate star repeated "n" times to "lines" + '\n'
    - continue

  - startIndent = loop idx (i= 0, 1, 2, 3)
  - middleIndent = (n - ((numStars) + 2 * startIndent)) / 2
  - line = `${' '.repeat(startIndent)}*${' '.repeat(middleIndent)}*${' '.repeat(middleIndent)}*`
  - concatenate `line` to `lines`

  - if i is not equal to n - 1, append '\n' to lines 

- return `lines`
*/

function star(n) {
  if (typeof n !== 'number') { return undefined; }
  if (n < 7 || n % 2 === 0) { return undefined; }

  let lines = '';
  let numStars = 3;
  let middleIdx = Math.floor(n / 2);

  for (let i = 0; i < n; i += 1) {
    if (i === middleIdx) {
      lines += ('*'.repeat(n));
      lines += '\n';
      continue;
    }
    let startIndent;
    if (i < middleIdx) {
      startIndent = i;
    } else {
      startIndent = n - i - 1;
    }
    let middleIndent = (n - ((numStars) + 2 * startIndent)) / 2;
    let line = `${' '.repeat(startIndent)}*${' '.repeat(middleIndent)}*${' '.repeat(middleIndent)}*`;
    lines += line;

    if (i !== n - 1) {
      lines += '\n';
    }
  }

  return lines;
}

// Edge Cases 
console.log(star([])); // undefined
console.log(star(6)); // undefined
console.log(star(-7)); // undefined

// General Test Cases 
console.log(star(7));
/*

*  *  *
 * * *
  ***
*******
  ***
 * * *
*  *  *

*/

console.log('\n\n');
console.log(star(9));
/*

*   *   *
 *  *  *
  * * *
   ***
*********
   ***
  * * *
 *  *  *
*   *   *

*/