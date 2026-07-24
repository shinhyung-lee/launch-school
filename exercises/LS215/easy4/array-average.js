
function average(nums) {
  let numElement = nums.length;
  return Math.floor(nums.reduce((accm, elem) => accm + elem, 0) / numElement);
}

console.log(average([1, 5, 87, 45, 8, 8]));       // 25
console.log(average([9, 47, 23, 95, 16, 52]));    // 40