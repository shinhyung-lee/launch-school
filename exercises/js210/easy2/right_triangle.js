
function triangle(num) {
  let result = '';

  for (let i = 1; i <= num; i += 1) {
    let numSpaces = num - i;
    for (let j = 1; j <= numSpaces; j += 1) {
      result += ' ';
    }
    for (let k = 1; k <= i; k += 1) {
      result += '*'
    }
    result += '\n';
  }
  return result;
}

console.log(triangle(5));
console.log(triangle(9));