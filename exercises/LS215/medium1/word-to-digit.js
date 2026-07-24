/*
Input: a string
Output: a string

===== Problem =====
Explicit Rules
  - all "number words" are converted to "digit character".

===== Test Cases & Examples =====
"five five five one two three four." => "5 5 5 1 2 3 4."
delimiter: period, whitespace


===== Data Structures =====
- array
  - split string into words
  - predefined `NUMBER_WORDS` = ['zero', 'one', 'two', 'three', 'four',
  'five', 'six', 'seven', 'eight', 'nine'];

- string
  - regex? 

===== Algo =====
- Define `NUMBER_WORDS`
- Split a string into words 
- Iterate through each word in `words`
  - if `word` is included in `NUMBER_WORDS`, replace its value with 
    `indexOf` the word
  - otherwise, keep the word as is 
- Join words into a string and return
*/
const NUM_WORDS = {
  zero: 0,
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9,
}

function wordToDigit(string) {
  Object.keys(NUM_WORDS).forEach(word => {
    let regex = new RegExp(word, 'g');
    string = string.replace(regex, NUM_WORDS[word]);
  })

  return string;
}

console.log(wordToDigit('Please call me at five five five one two three four. Thanks.'));
// "Please call me at 5 5 5 1 2 3 4. Thanks."