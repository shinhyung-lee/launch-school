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

console.log(substrings('abcde'));

// returns
// [ "a", "ab", "abc", "abcd", "abcde",
//   "b", "bc", "bcd", "bcde",
//   "c", "cd", "cde",
//   "d", "de",
//   "e" ]