
/*
'x' => 'x' => idx 1
'Launch' => 'un' idx 2, 3
'Launch School' => ' ' idx 6
Math.floor(str.length / 2)

odd length:  return one character
even length: return two characters
*/
const isEvenLength = (string) => string.length % 2 === 0;

function centerOf(string) {
  let middleIdx = Math.floor(string.length / 2);

  if (isEvenLength(string)) {
    return string.slice(middleIdx - 1, middleIdx + 1);
  } else {
    return string[middleIdx];
  }
}


console.log(centerOf('I Love JavaScript')); // "a"
console.log(centerOf('Launch School'));     // " "
console.log(centerOf('Launch'));            // "un"
console.log(centerOf('Launchschool'));      // "hs"
console.log(centerOf('x'));                 // "x"