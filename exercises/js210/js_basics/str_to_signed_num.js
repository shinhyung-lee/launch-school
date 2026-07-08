

const DIGITS = {
  '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
  '6': 6, '7': 7, '8': 8, '9': 9,
};

function stringToSignedInteger(string) {
  let value = 0;
  const { numbers, isNegative } = stringToNumber(string);

  for (let i = 0; i < numbers.length; i += 1) {
    value = 10 * value + numbers[i];
  }

  if (isNegative) {
    return -value;
  } else {
    return value;
  }

}

function stringToNumber(string) {
  const result = {
    numbers: [],
    isNegative: false,
  };

  for (let i = 0; i < string.length; i += 1) {
    if (string[i] === '-') {
      result.isNegative = true;
      continue;
    } else if (string[i] === '+') {
      continue;
    }

    result.numbers.push(DIGITS[string[i]]);
  }

  return result;
}

console.log(stringToSignedInteger('4321'));      // 4321
console.log(stringToSignedInteger('-570'));      // -570
console.log(stringToSignedInteger('+100'));      // 100