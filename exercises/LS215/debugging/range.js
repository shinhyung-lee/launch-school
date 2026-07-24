function range(start, end) {
  if (arguments.length === 1) {
    end = start;
    start = 0;
  }
  const range = [];

  for (let element = start; element <= end; element++) {
    range.push(element);
  }

  return range;
}

// function range(end) {
//   return range(0, end);
// }

// Examples

console.log(range(10, 20)); // [10, 11, 12, ... , 20]
console.log(range(5)); // [0, 1, 2, 3, 4, 5]