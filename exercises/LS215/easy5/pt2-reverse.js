/*
  split the string into words (' ' delimiter)
  iterate through words (array)
    if word.length >= 5, reverse the word 
    assign the reversed word to mutate the words array

  join array into a string (' ' separator)
  return the string
*/
const fiveOrMore = (str) => str.length >= 5;

function reverseWords(sentence) {
  let result = '';
  let words = sentence.split(' ');

  for (let i = 0; i < words.length; i += 1) {
    let reversedWord = '';
    let currentWord = words[i];
    if (fiveOrMore(currentWord)) {
      for (let j = currentWord.length - 1; j >= 0; j -= 1) {
        let char = currentWord[j];
        reversedWord += char;
      }
      words[i] = reversedWord;
    }
  }
  return words.join(' ');
}


console.log(reverseWords('Professional'));             
// "lanoisseforP"
console.log(reverseWords('Walk around the block'));    
// "Walk dnuora the kcolb"
console.log(reverseWords('Launch School'));            
// "hcnuaL loohcS"