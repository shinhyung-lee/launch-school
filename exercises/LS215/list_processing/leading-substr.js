
function leadingSubstrings(string) {
  let substrings = [];
  for (let idx = 0; idx < string.length; idx += 1) {
    substrings.push(string.slice(0, idx + 1));
  }
  
  return substrings;
  // return string.split('')
  //              .map((char, idx, arr) => arr.slice(0, idx + 1).join(''))
}

console.log(leadingSubstrings('abc'));      
// ["a", "ab", "abc"]
console.log(leadingSubstrings('a'));        
// ["a"]
console.log(leadingSubstrings('xyzzy'));    
// ["x", "xy", "xyz", "xyzz", "xyzzy"]