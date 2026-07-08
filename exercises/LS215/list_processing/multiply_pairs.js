

function multiplyAllPairs(numArr1, numArr2) {
  let multipliedNums = [];
  numArr1.forEach(num1 => {
    numArr2.forEach(num2 => {
      multipliedNums.push(num1 * num2);
    })
  })

  return multipliedNums.sort((a, b) => a - b);
}

console.log(multiplyAllPairs([2, 4], [4, 3, 1, 2]));    
// [2, 4, 4, 6, 8, 8, 12, 16]