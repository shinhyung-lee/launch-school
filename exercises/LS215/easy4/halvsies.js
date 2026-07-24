
/*

=== Problem ===
Input: 1D array
Output: array with two nested array elements
        - first arr:  first half of the original arr
        - second arr: second half of the original arr

Rules:
- If the original array contains an odd number of elements, place the middle element in the first half array.

=== Data Structures ===
- array
- int

=== Brainstorm ===
- get the middle index:
  - arr.length / 2

=== Algorithm === 


  [1, 2, 3, 4] => [[1, 2], [3, 4]]
  middleIdx = 2
  firstHalf = nums(0, 2) => [1, 2]
  secondHalf = nums(2)   => [3, 4]
  return  [[1, 2], [3, 4]]

  [1, 5, 2, 4, 3] => [[1, 5, 2], [4, 3]]
  middleIdx = Math.floor(2.5) = 2
  arr has odd length, middleIdx += 1, 
    middleIdx = 3
  firstHalf = nums(0, 3) => [1, 5, 2]
  secondHalf = nums(3)   => [4, 3]
  returns [[1, 5, 2], [4, 3]]


- initialize a variable `middleIdx` to length of the array divided by 2
- Math.floor(nums.length / 2)
- convert the number to int using Math.floor() method

- if original arr has an odd length, add 1 to `middleIdx`
- initialize an arr `firstHalf` to original sliced with (0, middle)
  - nums.slice(0, middle)
- initialize an arr `secondHalf` to original sliced with (middle)
  - nums.slice(middle)
- return [firstHalf, secondHalf
  - array with two nested array elements
*/
function halvsies(nums) {
  let middleIdx = Math.floor(nums.length / 2);
  if (isOddArr(nums)) middleIdx += 1;

  // console.log(middleIdx); // 2, 3, 1, 0
  let firstHalf = nums.slice(0, middleIdx);
  let secondHalf = nums.slice(middleIdx);
  
  return [firstHalf, secondHalf];
}

const isOddArr = (arr) => arr.length % 2 === 1;

console.log(halvsies([1, 2, 3, 4]));       // [[1, 2], [3, 4]]
console.log(halvsies([1, 5, 2, 4, 3]));    // [[1, 5, 2], [4, 3]]
console.log(halvsies([5]));                // [[5], []]
console.log(halvsies([]));                 // [[], []]