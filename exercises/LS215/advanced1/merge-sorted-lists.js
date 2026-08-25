/*
Write a function that takes two sorted arrays as arguments and returns a new array that contains all the elements from both input arrays in sorted order.

You may not provide any solution that requires you to sort the result array. You must build the result array one element at a time in the proper order.

Your solution should not mutate the input arrays.

=== Problem ===
In: two sorted arrays
Out: an array
  - contains all the elements from both input arrays in sorted order

Rules:
  - function should NOT mutate the input arrays 
  - build the result array one element at a time in the proper order
  - If one of the array is empty, return the other array 

=== Questions ===
Q. Will array arguments be always sorted?
  - YES.

Q. Can either/both arguments be of different data type?
  - string, object, bool, etc,
  - YES. If so, return undefined

Q. Can arrays have non-number elements?
  - undefined, string, bool, object 
  - YES, return undefined

Q. Can arrays have special numbers as elements?
  - Infinity, NaN
  - YES, return undefined

=== Examples ===
[1, 5, 9], [2, 6, 8]      // [1, 2, 5, 6, 8, 9]
[1, 1, 3], [2, 2]         // [1, 1, 2, 2, 3]
[1, 4, 5], []             // [1, 4, 5]
=== Data Structures ===
- array
- two pointers
  - int 
  - idx i for arr1, 
  - idx j for arr2

  
=== Brainstorm ===
=== Algorithm ===
- HELPER function (isValidInput)
  - In: an array
  - Out: a bool (true, false)
    - if all elements are valid, return true 
    - else, return false 

  - if either array contains special number elements or non-number elements, 
    - return undefined
  - !arr1.every(num => typeof num === 'number')
    - return false
  - arr1.some(num => [Infinity, -Infinity, NaN].includes(num))
    - return false 

EDGE CASE HANDLING
- !Array.isArray(nums1) || !Array.isArray(nums2)
  - return undefined
- if either arr (nums1, nums2) is invalid (*** HELPER *** isValidInput)
  - return undefined

- if at least one of the arrays is empty (EDGE CASE)
  - return the other arr 
  - if (nums1.length === 0 || nums2.length === 0)
    - return nums1.length === 0 ? nums2 : nums1
- 

- create a new array `sortedArr`, for building sorted numbers 
- use two pointers, for comparing values from two arrays
  - i = 0, j = 0
  - idx `i` for arr1, idx `j` for arr2 (start with i = 0, j = 0)
  - while (i < arr1.length || j < arr2.length)
  - while (True)
    - if num1[i] is greater than or equal to nums2[j],
      - push nums1[i] to `sortedArr`
      - increment `i` by 1
    - else
      - push nums2[j] to `sortedArr`
      - increment `j` by 1 
  - break condition:
    - if i === nums1.length - 1 || j === nums2.length - 1
      - break out of while loop

- What if one array is done with iteration?
  - add the rest of elements from the other array 
- if i !== nums1.length - 1
  - slice nums1(i) and push to `sortedArr`
- else if j !== nums2.length - 1
  - slice nums2(j) and push to `sortedArr` 

- return `sortedArr` 
*/
/*
- create a new array `sortedArr`, for building sorted numbers 
- use two pointers, for comparing values from two arrays
  - i = 0, j = 0
  - idx `i` for arr1, idx `j` for arr2 (start with i = 0, j = 0)
  - while (True)
    - if num1[i] is greater than or equal to nums2[j],
      - push nums1[i] to `sortedArr`
      - increment `i` by 1
    - else
      - push nums2[j] to `sortedArr`
      - increment `j` by 1 
  - break condition:
    - if i === nums1.length - 1 || j === nums2.length - 1
      - break out of while loop

- What if one array is done with iteration?
  - add the rest of elements from the other array 
- if i !== nums1.length - 1
  - slice nums1(i) and push to `sortedArr`
- else if j !== nums2.length - 1
  - slice nums2(j) and push to `sortedArr` 

- return `sortedArr` 
*/
function merge(nums1, nums2) {
  if (!Array.isArray(nums1) || !Array.isArray(nums2)) {
    return undefined;
  }
  if (!isValidInput(nums1) || !isValidInput(nums2)) {
    return undefined;
  }
  if (nums1.length === 0 || nums2.length === 0) {
    return nums1.length === 0 ? nums2 : nums1;
  }

  let sortedArr = [];
  let i = 0;
  let j = 0;

  while (true) {
    // if num1[i] is greater than or equal to nums2[j],
    if (nums1[i] < nums2[j]) {
      sortedArr.push(nums1[i]);
      i += 1;
    } else {
      sortedArr.push(nums2[j]);
      j += 1;
    }

    if (i === nums1.length || j === nums2.length) {
      break;
    }
  }

  if (i < nums1.length) {
    sortedArr.push(...nums1.slice(i));
  } else {
    sortedArr.push(...nums2.slice(j));
  }

  return sortedArr;
}

function isValidInput(arr) {
  if (!arr.every(num => typeof num === 'number') || arr.some(num => [Infinity, -Infinity, NaN].includes(num))) {
    return false;
  }

  return true;
}

// Edge Cases
console.log(merge([1, 4, 5], true));           // undefined
console.log(merge({a: 1, b: 2}, [1, 4, 5]));   // undefined

// non-number elements
console.log(merge([1, 5, true], [2, 6, 8])); // undefined
// special number elements
console.log(merge([1, 5, Infinity], [2, 6, {a: 1, b: 2}])); // undefined

// General Test Cases
console.log(merge([1, 5, 9], [2, 6, 8]));      // [1, 2, 5, 6, 8, 9]
console.log(merge([1, 1, 3], [2, 2]));         // [1, 1, 2, 2, 3]
console.log(merge([], [1, 4, 5]));             // [1, 4, 5]
console.log(merge([1, 4, 5], []));             // [1, 4, 5]

console.log(merge([1, 5, 9], [1, 4, 5, 9])); // [1, 1, 4, 5, 5, 9, 9]