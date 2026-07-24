
const isConsonant = (char) => /[^aioue]/i.test(char);
const isLetter = (char) => /[a-z]/i.test(char);

function doubleConsonants(string) {
  let result = '';
  for (let idx = 0; idx < string.length; idx += 1) {
    let char = string[idx];
    if (isConsonant(char) && isLetter(char)) {
      result += (char.repeat(2));
    } else {
      result += char;
    }
  }

  return result;
}

console.log(doubleConsonants('String'));          // "SSttrrinngg"
console.log(doubleConsonants('Hello-World!'));    // "HHellllo-WWorrlldd!"
console.log(doubleConsonants('July 4th'));        // "JJullyy 4tthh"
console.log(doubleConsonants(''));                // ""