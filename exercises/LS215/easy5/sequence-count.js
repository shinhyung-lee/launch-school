
function sequence(count, startingNum) {
  if (count === 0) {
    return [];
  }
  
  let result = [];
  for (let multiplicant = 1; multiplicant <= count; multiplicant += 1) {
    result.push(multiplicant * startingNum);
  }

  return result;
}

console.log(sequence(5, 1));          // [1, 2, 3, 4, 5]
console.log(sequence(4, -7));         // [-7, -14, -21, -28]
console.log(sequence(3, 0));          // [0, 0, 0]
console.log(sequence(0, 1000000));    // []