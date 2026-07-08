


function missing(arr) {
  let first = arr[0] + 1;
  let last = arr[arr.length - 1] - 1;

  let missing = [];
  for (let counter = first; counter <= last; counter += 1) {
    if (arr.indexOf(counter) === -1) {
      missing.push(counter);
    }
  }

  return missing.toSorted();
}

console.log(missing([-3, -2, 1, 5]));                  // [-1, 0, 2, 3, 4]
console.log(missing([1, 2, 3, 4]));                    // []
console.log(missing([1, 5]));                          // [2, 3, 4]
console.log(missing([6]));                             // []