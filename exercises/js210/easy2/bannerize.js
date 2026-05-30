function repeatString(str, times) {
  return str.repeat(times + 2);
}

function logInBox(sentence) {
  let strLength = sentence.length;
  let result = '';
  result += `+${repeatString('-', strLength)}+\n`;
  result += `|${repeatString(' ', strLength)}|\n`;
  result += `| ${sentence} |\n`;
  result += `|${repeatString(' ', strLength)}|\n`;
  result += `+${repeatString('-', strLength)}+`;

  return result;
}

console.log(logInBox('To boldly go where no one has gone before.'));
console.log(logInBox(''));