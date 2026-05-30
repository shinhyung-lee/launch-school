
function sumNums(num) {
  let sum = 0;
  for (let counter = 1; counter <= num; counter += 1) {
    sum += counter;
  }

  return sum;
}

function multiplyNums(num) {
  let multiplied = 1;
  for (let counter = 1; counter <= num; counter += 1) {
    multiplied *= counter;
  }

  return multiplied;
}

const readlineSync = require('readline-sync');

let num = Number(readlineSync.question('Enter a number greater than 0: '));
let operation = readlineSync.question('Enter "s" to compute the sum, or "p" to compute the product. ');

if (operation === 's') {
  let sum = sumNums(num);
  console.log(`The sum of the integers between 1 and 5 is ${sum}.`);
} else if (operation === 'p') {
  let product = multiplyNums(num);
  console.log(`The product of the integers between 1 and 5 is ${product}.`);
}

