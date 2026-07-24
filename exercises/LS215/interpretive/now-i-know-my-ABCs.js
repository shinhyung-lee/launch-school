/*

=== Problem ===

Input: a string (`word`)
Output: a boolean
      - `true` if the word can be spelled using a set of blocks,
      - `false` otherwise

Rules:
- can also only use each block once
  - cannot use both B and O from the same block, for example
- case does not matter
  - treat the string case-insensitively 

=== Test Cases ===
'BATCH' => false
B:O, N:A, G:T, C:P, H:U 
true

'BUTCH' => false
B:O, H:U, G:T, C:P, H:U (duplicated)
false
  
'jest' => true
J:W, R:E, F:S, G:T
true 

=== Questions ===
- What if the input string is empty?
  - return undefined

- What if the input is not a string?
  - return undefined 

=== Data Structures ===
- string: 
  - input 

- boolean:
  - output 

- intermediate data structure
  - array 
  - let letterBlocks = [['b', 'o'], ['x', 'k'], ['d', 'q'], ['c', 'p'], ['n', 'a'], 
  ['g', 't'], ['r', 'e'], ['f', 's'], ['j', 'w'], ['h', 'u'], ['v', 'i'],
  ['l', 'y'], ['z', 'm']]

B:O   X:K   D:Q   C:P   N:A
G:T   R:E   F:S   J:W   H:U
V:I   L:Y   Z:M

=== Brainstorm ===
- if `string` is not of type string, return `undefined`
- 

=== Algorithms ===
- if (`string` is not of type string || `string` is empty), 
  - return `undefined`
- initailize a variable `letter_blocks` = [['b', 'o'], ['x', 'k'], ['d', 'q'], ['c', 'p'], ['n', 'a'], 
  ['g', 't'], ['r', 'e'], ['f', 's'], ['j', 'w'], ['h', 'u'], ['v', 'i'],
  ['l', 'y'], ['z', 'm']]

- reassign `string` to `toLowerCase` version of it 
- initialize an empty array `usedLetter`
- iterate through every `char` in `string` with `idx` (forEach, for-loop)
  - if `usedLetter` includes `char` 
    - return false (from the entire func)
  - iterate through each `block` in `LETTER_BLOCKS` (MUST USE for-loop 'j')
    - if `block` includes `char` 
      - push both letters (ex: 'b', 'o') to `usedLetter` 
      - letter_blocks will be all elements except for the current one (reassignment)
      - letter_blocks = letter_blocks.filter((elem, idx) => idx !== j)
      - break out of the for loop 
    
- return true 

'' => undefined
'BATCH' => true 
'batch' 
'usedLetter' = ['b', 'o', 'n', 'a', 'g', 't', 'c', 'p', 'h', 'u']
'b', 'a', 't', 'c', 'h' 
returns true 

'BUTCH' => false 
'butch' 
'usedLetter' = ['b', 'o', 'h', 'u', 'g', 't', 'c', 'p', ]

=== Algorithms ===
- if (`string` is not of type string || `string` is empty), 
  - return `undefined`
- initailize a variable `letter_blocks` = [['b', 'o'], ['x', 'k'], ['d', 'q'], ['c', 'p'], ['n', 'a'], 
  ['g', 't'], ['r', 'e'], ['f', 's'], ['j', 'w'], ['h', 'u'], ['v', 'i'],
  ['l', 'y'], ['z', 'm']]

- reassign `string` to `toLowerCase` version of it 
- initialize an empty array `usedLetter`
- iterate through every `char` in `string` with `idx` (forEach, for-loop)
  - if `usedLetter` includes `char` 
    - return false (from the entire func)
  - iterate through each `block` in `LETTER_BLOCKS` (MUST USE for-loop 'j')
    - if `block` includes `char` 
      - push both letters (ex: 'b', 'o') to `usedLetter` 
      - letter_blocks will be all elements except for the current one (reassignment)
      - letter_blocks = letter_blocks.filter((elem, idx) => idx !== j)
      - break out of the for loop 
    
- return true 
*/
function isBlockWord(word) {
  const blocks = ['B:O', 'X:K', 'D:Q', 'C:P', 'N:A', 'G:T', 'R:E', 'F:S', 'J:W', 'H:U', 'V:I', 'L:Y', 'Z:M'];
  const regExps = blocks.map(block => new RegExp(block.replace(':', '|'), 'gi'));

  return regExps.every(regExp => (word.match(regExp) || []).length < 2);
}

// edge cases 
// console.log(isBlockWord('')); // undefined
// console.log(isBlockWord(['a', 'b', 'c'])); // undefined
// console.log(isBlockWord({a: 1, b: 2})); // undefined

// general test cases
console.log(isBlockWord('BATCH'));      // true
console.log(isBlockWord('BUTCH'));      // false
console.log(isBlockWord('jest'));       // true