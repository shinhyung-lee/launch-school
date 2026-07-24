/*
Write a function that rotates an array by moving the first element to the end of the array. Do not modify the original array.

If the input is not an array, return undefined.
If the input is an empty array, return an empty array.

===== Problem =====
Input: array
Output: array

===== Examples, Test Cases =====
[7, 3, 5, 2, 9, 1] => [3, 5, 2, 9, 1, 7]
['a', 'b', 'c'] => ["b", "c", "a"]
['a'] => ['a']

Non-array arguments
no argument => undefined
1 => undefined

Data Structures:
- array

Algorithms:
- if arg is undefined, return undefined
- if arg is not an array, return undefined
- slice array from index 1
- add first (0th) element of the array to the sliced array 
- return 
*/
function rotateArray(arr) {
  if (arr === undefined || !Array.isArray(arr)) { return undefined; }
  if (arr.length === 0) { return arr; }
  let rotatedArr =  arr.slice(1)
  rotatedArr.push(arr[0]);

  return rotatedArr;
}

console.log(rotateArray([7, 3, 5, 2, 9, 1]));       // [3, 5, 2, 9, 1, 7]
console.log(rotateArray(['a', 'b', 'c']));          // ["b", "c", "a"]
console.log(rotateArray(['a']));                    // ["a"]
console.log(rotateArray([1, 'a', 3, 'c']));         // ["a", 3, "c", 1]
console.log(rotateArray([{ a: 2 }, [1, 2], 3]));    // [[1, 2], 3, { a: 2 }]
console.log(rotateArray([]));                       // []

// return `undefined` if the argument is not an array
console.log(rotateArray());                         // undefined
console.log(rotateArray(1));                        // undefined


// the input array is not mutated
const array = [1, 2, 3, 4];
console.log(rotateArray(array));                    // [2, 3, 4, 1]
console.log(array);                                 // [1, 2, 3, 4]