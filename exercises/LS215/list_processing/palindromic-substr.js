function leadingSubstrings(string) {
  let substrings = [];
  for (let idx = 0; idx < string.length; idx += 1) {
    substrings.push(string.slice(0, idx + 1));
  }
  
  return substrings;
}

function substrings(string) {
  // apply `leadingSubstrings` function to string idx 0 to
  // string.length - 1 
  // with nested arrays, use reduce. 
  // Inside reduce, use concat method 
  let result = [];
  for (let idx = 0; idx < string.length; idx += 1) {
    let substring = string.slice(idx);
    result = result.concat(leadingSubstrings(substring))
  }
  return result;
} 

function isPalindrome(word) {
  return word.length > 1 && word === word.split('').reverse().join('')
}

function palindromes(string) {
  return substrings(string).filter(isPalindrome);
}



console.log(palindromes('abcd'));       // []
console.log(palindromes('madam'));      // [ "madam", "ada" ]

console.log(palindromes('hello-madam-did-madam-goodbye'));
// returns
// [ "ll", "-madam-", "-madam-did-madam-", "madam", "madam-did-madam", "ada",
//   "adam-did-mada", "dam-did-mad", "am-did-ma", "m-did-m", "-did-", "did",
//   "-madam-", "madam", "ada", "oo" ]

console.log(palindromes('knitting cassettes'));
// returns
// [ "nittin", "itti", "tt", "ss", "settes", "ette", "tt" ]