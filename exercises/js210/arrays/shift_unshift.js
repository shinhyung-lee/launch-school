

function shift(arr) {
  if (arr.length === 0) {
    return undefined;
  }

  let value = arr[0];
  arr.splice(0, 1);
  return value;
}

console.log(shift([1, 2, 3]));                // 1
console.log(shift([]));                       // undefined
console.log(shift([[1, 2, 3], 4, 5]));        // [1, 2, 3]

function unshift(arr, ...values) {
  for(let i = 0; i < values.length; i += 1) {
    arr.splice(i, 0, values[i]);
  }
  return arr.length;
}

console.log(unshift([1, 2, 3], 5, 6));        // 5
console.log(unshift([1, 2, 3]));              // 3
console.log(unshift([4, 5], [1, 2, 3]));      // 3

const testArray = [1, 2, 3];
console.log(shift(testArray));                // 1
console.log(testArray);                       // [2, 3]
console.log(unshift(testArray, 5, 6));           // 3
console.log(testArray);                       // [5, 2, 3]