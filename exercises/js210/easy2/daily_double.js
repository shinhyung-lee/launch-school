
function crunch(string) {
  let index = 0;
  let crunchText = '';

  while (index <= string.length - 1) {
    if (string[index] !== string[index + 1]) {
      crunchText += string[index];
    }

    index += 1;
  }
  
  console.log(crunchText);
  return crunchText;
}

crunch('ddaaiillyy ddoouubbllee');    // "daily double"
crunch('4444abcabccba');              // "4abcabcba"
crunch('ggggggggggggggg');            // "g"
crunch('a');                          // "a"
crunch('');                           // ""