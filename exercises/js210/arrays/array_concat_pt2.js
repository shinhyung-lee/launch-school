

function concat(firstArgument, ...args) {
  let result = firstArgument;
  for (const arg of args) {
    if (Array.isArray(arg)) {
      result = result.concat(arg);
    } else {
      result.push(arg);
    }
  }

  return result;
}

console.log(concat([1, 2, 3], [4, 5, 6], [7, 8, 9]));    // [1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(concat([1, 2], 'a', ['one', 'two']));        // [1, 2, "a", "one", "two"]
console.log(concat([1, 2], ['three'], 4));               // [1, 2, "three", 4]