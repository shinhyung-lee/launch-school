/*
Write a function that implements the Caesar Cipher. The Caesar Cipher is one of the earliest and simplest ways to encrypt plaintext so that a message can be transmitted securely. It is a substitution cipher in which each letter in a plaintext is substituted by the letter located a given number of positions away in the alphabet. For example, if the letter 'A' is right-shifted by 3 positions, it will be substituted with the letter 'D'. This shift value is often referred to as the key. The "encrypted plaintext" (ciphertext) can be decoded using this key value.

The Caesar Cipher only encrypts letters (including both lower and upper case). Any other character is left as is. The substituted letters are in the same letter case as the original letter. If the key value for shifting exceeds the length of the alphabet, it wraps around from the beginning.

=== Problem === 
Input: a string, number
Output: a string (rotated according to number)

Rules:
- only encrypt letters (lower and upper case letters)

=== Questions ===
- What if the first input is not a string?
- What if the second input is not a number?


=== Examples ===


=== Data Structures ===
- string
  - iterate through the string

- regex:
  - filter lowercase and uppercase letters /[a-z]/i

=== Brainstorm ===

=== Algorithms ===

rotate(char, shiftBy)
- char: one letter (either lower or upper case)
- shiftBy: digit to shift by
- If the key value for shifting exceeds the length of the alphabet, it wraps around from the beginning. 
  - ex) 'y', 5 => 'z', 'a', 'b', 'c', 'd' => returns 'd'
  String.fromChar
  - WRAP_ALPHABET_DIFFERENCE = 26 
  - if char is lower (/[a-z]/.test(char))
    - if 'y'.charCodeAt(0) + shiftBy > 'z'.charCodeAt(0),
      - return String.fromCharCode('y'.charCodeAt(0) + shiftBy - diff)

  - if char is upper (/[A-Z]/.test(char))
    - if 'Y'.charCodeAt(0) + shiftBy > 'Z'.charCodeAt(0),
      - return String.fromCharCode('Y'.charCodeAt(0) + shiftBy - diff)
  
      - default:
    - String.fromCharCode('y'.charCodeAt(0) + shiftBy)


caesarEncrypt (MAIN function)
- iterate through every char in the original string
  - if char is a letter, rotate then concatenate to result string
    - rotate (HELPER function)
  - otherwise, concatenate the char to result string

- return result string

*/

/*
 - WRAP_ALPHABET_DIFFERENCE = 26 
  - if char is lower (/[a-z]/.test(char))
    - if 'y'.charCodeAt(0) + shiftBy > 'z'.charCodeAt(0),
      - return String.fromCharCode('y'.charCodeAt(0) + shiftBy - diff)

  - if char is upper (/[A-Z]/.test(char))
    - if 'Y'.charCodeAt(0) + shiftBy > 'Z'.charCodeAt(0),
      - return String.fromCharCode('Y'.charCodeAt(0) + shiftBy - diff)
  
      - default:
    - String.fromCharCode('y'.charCodeAt(0) + shiftBy)
*/
function rotate(char, shiftBy) {
  let WRAP_ALPHABET_DIFFERENCE = 26;
  if (/[a-z]/.test(char)) { // lowercase
    if (char.charCodeAt(0) + shiftBy > 'z'.charCodeAt(0)) {
      return String.fromCharCode(char.charCodeAt(0) + shiftBy - WRAP_ALPHABET_DIFFERENCE);
    }
  }

  if (/[A-Z]/.test(char)) {
    if (char.charCodeAt(0) + shiftBy > 'Z'.charCodeAt(0)) {
      return String.fromCharCode(char.charCodeAt(0) + shiftBy - WRAP_ALPHABET_DIFFERENCE);
    }
  }

  return String.fromCharCode(char.charCodeAt(0) + shiftBy);
}

function caesarEncrypt(string, shiftBy) {
  let result = '';
  for (let char of string) {
    if (/[a-z]/i.test(char)) {
      result += rotate(char, shiftBy); 
    } else {
      result += char;
    }
  }

  return result;
}

// simple shift
console.log(caesarEncrypt('A', 0));       // "A"
console.log(caesarEncrypt('A', 3));       // "D"

// wrap around
console.log(caesarEncrypt('y', 5));       // "d"
console.log(caesarEncrypt('a', 47));      // "v"

// all letters
console.log(caesarEncrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 25));
// "ZABCDEFGHIJKLMNOPQRSTUVWXY"
console.log(caesarEncrypt('The quick brown fox jumps over the lazy dog!', 5));
// "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl!"

// many non-letters
console.log(caesarEncrypt('There are, as you can see, many punctuations. Right?; Wrong?', 2));
// "Vjgtg ctg, cu aqw ecp ugg, ocpa rwpevwcvkqpu. Tkijv?; Ytqpi?"