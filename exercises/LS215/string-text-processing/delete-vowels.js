function vowelRemovedString(word) {
  let matches = word.match(/[^aioue]/ig);
  return matches === null ? '' : matches.join('');
}

function removeVowels(words) {
  return words.map(vowelRemovedString);
}

console.log(removeVowels(['abcdefghijklmnopqrstuvwxyz']));         // ["bcdfghjklmnpqrstvwxyz"]
console.log(removeVowels(['green', 'YELLOW', 'black', 'white']));  // ["grn", "YLLW", "blck", "wht"]
console.log(removeVowels(['ABC', 'AEIOU', 'XYZ']));                // ["BC", "", "XYZ"]