
function showMultiplicativeAverage(nums) {
  let numValues = nums.length;
  let multiple = nums.reduce((mul, num) => mul * num, 1);
  let multiplicativeAvg = multiple / numValues;
  return multiplicativeAvg.toFixed(3);

}

console.log(showMultiplicativeAverage([3, 5]));                   // "7.500"
console.log(showMultiplicativeAverage([2, 5, 7, 11, 13, 17]));    // "28361.667"