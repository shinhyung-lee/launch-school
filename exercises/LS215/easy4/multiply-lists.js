

function multiplyList(numArr1, numArr2) {
  let result = [];
  let arrLength = numArr1.length;

  for (let idx = 0; idx < arrLength; idx += 1) {
    result.push(numArr1[idx] * numArr2[idx]);
  }

  return result;
}

console.log(multiplyList([3, 5, 7], [9, 10, 11]));    
// [27, 50, 77]