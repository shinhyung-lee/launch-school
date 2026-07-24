
function interleave(arr1, arr2) {
  let result = [];
  let arrLength = arr1.length;
  for (let idx = 0; idx < arrLength; idx += 1) {
    result.push(arr1[idx], arr2[idx]);
  }

  return result;
}

console.log(interleave([1, 2, 3], ['a', 'b', 'c']));    // [1, "a", 2, "b", 3, "c"]