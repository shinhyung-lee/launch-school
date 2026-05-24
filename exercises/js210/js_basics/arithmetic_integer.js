let readlineSync = require('readline-sync');

let num1 = Number(readlineSync.question("==> Enter the first number: "));
let num2 = Number(readlineSync.question("==> Enter the second number: "));

console.log(`==> ${num1} + ${num2} = ${num1 + num2}`)
console.log(`==> ${num1} - ${num2} = ${num1 - num2}`)
console.log(`==> ${num1} * ${num2} = ${num1 * num2}`)
console.log(`==> ${num1} / ${num2} = ${num1 / num2}`)
console.log(`==> ${num1} % ${num2} = ${num1 % num2}`)
console.log(`==> ${num1} ** ${num2} = ${num1 ** num2}`)