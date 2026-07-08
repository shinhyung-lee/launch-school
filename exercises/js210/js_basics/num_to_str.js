
function integerToString(number) {
  if (number === 0) {
    return '0';
  }

  let result = '';
  const isNegative = number < 0 ? true : false;

  number = Math.abs(number);

  do {
    let digitToAdd = number % 10; // 1, 2, 3, 4
    number = Math.floor(number / 10); // 0
    
    result = digitToAdd + result; // 4321
  } while (number !== 0)

  return isNegative ? '-' + result : '+' + result;
}

console.log(integerToString(4321));      // "4321"
console.log(integerToString(0));         // "0"
console.log(integerToString(-5000));      // "5000"