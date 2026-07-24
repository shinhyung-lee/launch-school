
let stack = [];
let register = 0;

function isNumber(str) {
  return typeof parseInt(str, 10) === 'number';
}

function minilang(prompt) {
  let words = prompt.split(' ');
  console.log(words);
  for (let word of words) {
    if (isNumber(word)) {
      stack.push(parseInt(word, 10));
    }
  }
  console.log(stack);
}


// console.log(minilang('PRINT'));
// 0

console.log(minilang('5 PUSH 3 MULT PRINT'));
// 15

// console.log(minilang('5 PRINT PUSH 3 PRINT ADD PRINT'));
// 5
// 3
// 8

// console.log(minilang('5 PUSH POP PRINT'));
// 5

// console.log(minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT'));
// 5
// 10
// 4
// 7

// console.log(minilang('3 PUSH PUSH 7 DIV MULT PRINT'));
// 6

// console.log(minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT'));
// 12

// console.log(minilang('-3 PUSH 5 SUB PRINT'));
// 8

// console.log(minilang('6 PUSH'));
// (nothing is printed because the `program` argument has no `PRINT` commands)