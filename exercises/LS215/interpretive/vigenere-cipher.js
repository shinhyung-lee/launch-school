/*
=== Problem ===
In:  two strings
  - plaintext, keyword
Out: a string
  - text transformed using vigenere cipher keyword

Rules:
- cipher is applied to letters(/a-z/i) only
- each letter of the `keyword` is a shift value
  - 'A' => shift value of 0
  - 'B' => shift value of 1
  - 'd' => shift value of 3
  - 'z' or 'Z' => shift value of 25

- 'a'-'z' are equivalent to the numbers 0-25
- 'A'-'Z' are also equivalent to 0-25

=== Questions ===
- What if `keyword` is an empty string?
  - return plaintext as is

- What if plaintext is empty?
  - return an empty string 

- What if plaintext or keyword is not a string?
  - return undefined

=== Example ===
"Pineapples don't go on pizzas!", 'meat'
=> returns 'Bmnxmtpeqw dhz'x gh ar pbldal!'

=== Data Structures ===
- string


=== Brainstorm ===
- take care of edge case
  - if either argument is not a string, 
    - return undefined
  - if keyword is an empty string,
    - return `plaintext` as is 
  - if `plaintext` is an empty string,
    - return an empty string 
  
- initialize an empty string `transformed` (will be return value)
- use a string 
  - `lowercase` = 'abcdefghijklmnopqrstuvwxyz'
  - uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
- keyword case doesn't matter, so make `keyword` lowercase off the bat 
  - keyword = keyword.toLowerCase();

- if char is a letter (/a-z/i)
  - apply vig-cipher character
  - concatenate return value to `transformed`
  - keep track of keyword as we iterate through `keyword` (moves forward)
    - if keyword char is on the last character, 
      - for the next transformation, change idx to 0.
- else (if char is not a letter)
  - concatenate to `transformed` as is

- return `transformed` 

*** HELPER FUNCTION ***
vigenereTransformation
Input: `char` (one character string), `toAdd` (one char), `letters` (lowercase or uppercase depending casing)
Output: a char (one character string)


- if `letters.indexOf(char) + letters.indexOf(toAdd)` > letters.length
  - letters += letters
- find char from letters (string) that has an idx of `toAdd` + `char` and return


=== Algorithms ===

*/
/*
- take care of edge case
  - if either argument is not a string, 
    - return undefined
  - if keyword is an empty string,
    - return `plaintext` as is 
  - if `plaintext` is an empty string,
    - return an empty string 
  
- initialize an empty string `transformed` (will be return value)
- use a string 
  - `lowercase` = 'abcdefghijklmnopqrstuvwxyz'
  - uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
- keyword case doesn't matter, so make `keyword` lowercase off the bat 
  - keyword = keyword.toLowerCase();

- if char is a letter (/a-z/i)
  - apply vig-cipher character
  - concatenate return value to `transformed`
  - keep track of keyword as we iterate through `keyword` (moves forward)
    - if keyword char is on the last character, 
      - for the next transformation, change idx to 0.

- move `toAdd` by 1. 
  - if `toAdd is equal to keyword.length - 1`, 
    - reassign `toAdd` to 0
  - else,
    - increment `toAdd` by 1 
- else (if char is not a letter)
  - concatenate to `transformed` as is

- return `transformed` 
*/
/*
- if `letters.indexOf(char) + letters.indexOf(toAdd)` > letters.length
  - letters += letters
- find char from letters (string) that has an idx of `toAdd` + `char` and return
*/
function charTransformation(char, addedPos, letters) {
  // max idx is 25
  // letters.length is 25 
  const letterPos = letters.indexOf(char); // 'a' => 0
  // for addedNum 24
  if (!letters[letterPos + addedPos]) {
    letters += letters;
  }

  // prev (shin) version
  // if (letters.indexOf(char) + addedPos + 1 >= letters.length) {
  //   letters += letters;
  // }
  
  let targetIdx = letters.indexOf(char) + addedPos;
  return letters[targetIdx];
}

function vigenereCipher(plaintext, keyword) {
  if (typeof plaintext !== 'string' || typeof keyword !== 'string') {
    return undefined;
  }

  if (keyword === '') {
    return plaintext;
  }

  if (plaintext === '') {
    return '';
  }

  const LOWERCASE = 'abcdefghijklmnopqrstuvwxyz';
  const UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  let transformed = '';
  keyword = keyword.toLowerCase();
  let toAddIdx = 0;
  let toAdd = '';

  for (let i = 0; i < plaintext.length; i += 1) {
    toAdd = keyword[toAddIdx];
    // console.log(`curr keyword char: ${toAdd}`);

    let currChar = plaintext[i];
    let addedNum = LOWERCASE.indexOf(toAdd);
    if (/[^a-z]/i.test(currChar)) {
      transformed += currChar;
      continue;
    }

    if (/[a-z]/.test(currChar)) {
      transformed += charTransformation(currChar, addedNum, LOWERCASE);
    } else if (/[A-Z]/.test(currChar)) {
      transformed += charTransformation(currChar, addedNum, UPPERCASE);
    } 

    // 3 -> 4 / 4 % 4 = 0 
    // 2 -> 3 / 3 % 4 = 3
    toAddIdx = (toAddIdx + 1) % keyword.length; // refactored
    // console.log(`curr keyword char: ${keyword[toAddIdx]}`);
    // if (toAddIdx === keyword.length - 1) {
    //   toAddIdx = 0;
    //   console.log(`at limit`);
    // } else {
    //   toAddIdx += 1;
    // }
  }

  return transformed;
}

// *** Edge cases ***

// one or more arguments are not a string
console.log(vigenereCipher([], 'meat'));
// return undefined

console.log(vigenereCipher('apple mango blue', {a: 1, b: 2}));
// return undefined

// empty plaintext
console.log(vigenereCipher('', 'meat'));
// return an empty string 

// empty string keyword => return plaintext as is
console.log(vigenereCipher("Pineapples don't go on pizzas!", ''));
// "Pineapples don't go on pizzas!"


// *** General Test Case ***
console.log(vigenereCipher("Pineapples don't go on pizzas!", 'meat'));
// 'Bmnxmtpeqw dhz'x gh ar pbldal!'