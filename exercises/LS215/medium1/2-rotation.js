
/*
Write a function that rotates the last n digits of a number. 
For the rotation, rotate by one digit to the left, moving the 
first digit to the end.

===== Problem =====
Input: two numbers
Output: a number 

===== Questions =====
Q) What if either or both arguments are not a number?
  - return null


Q) What if `digitsToRotate` is greater than the number of digits in the `number`?
  - roll over?
  - return null

Q) 

Test Cases
735291, 1 => 735291 (no change)
735291, 2 => 735219 (last 2 digits, first digit rotated to the end)

735291, 4 => 732915
735291, 5 => 752913 (last 5 digits, first digit rotated to the end)
735291, 6 => 352917

===== Data Structures =====
- array (convert num to an array of nums)
  - slice
  - concat 
- int

===== Algorithms ===== 
- if `num` or `digits` is not an integer, return null
- Split `String(num)` with empty string separator `nums` array
- if `digits` is greater than the length of `nums` array, return null
- Keep the part of array that doesn't need to be rotated
  - `untouched` = first `n` elements of `nums` array
  - `n` = `nums.length` - `digits`
  - `nums.slice(0, n)`
- Initialize an array `toRotate` = `nums.slice(nums.length - digits)`
  - rotate `toRotate` and save to `rotated` array
- rotatedStr = concatenate `untouched` and `rotated` (array of strings)
- join `rotatedStr` to empty string separator
- return int version of `rotatedStr` (parseInt)
*/
function rotate(arr) {
  return arr.slice(1).concat(arr[0]);
}

function rotateRightmostDigits(num, digits) {
  if (!Number.isInteger(num) || !Number.isInteger(digits)) { return null; }

  let nums = String(num).split('');
  if (digits > nums.length) {
    return null;
  }

  let untouched = nums.slice(0, nums.length - digits);
  console.log(untouched); // [7, 3, 5, 2, 9]
  let toRotate = nums.slice(nums.length - digits);
  let rotated = rotate(toRotate);

  let rotatedStr = untouched.concat(rotated);
  return parseInt(rotatedStr.join(''), 10);
}

// Invalid arguments
console.log(rotateRightmostDigits(735291, '')); // null
console.log(rotateRightmostDigits(735291)); // null
console.log(rotateRightmostDigits([], '')); // null
console.log(rotateRightmostDigits(123, {})); // null

// `digits` is greater than the number of digits in the `number`
console.log(rotateRightmostDigits(123, 7));  // null

// General test cases
console.log(rotateRightmostDigits(735291, 1));      // 735291
console.log(rotateRightmostDigits(735291, 2));      // 735219
console.log(rotateRightmostDigits(735291, 3));      // 735912
console.log(rotateRightmostDigits(735291, 4));      // 732915
console.log(rotateRightmostDigits(735291, 5));      // 752913
console.log(rotateRightmostDigits(735291, 6));      // 352917