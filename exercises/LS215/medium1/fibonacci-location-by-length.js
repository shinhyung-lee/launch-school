/*
using BigInt integers

Input: BigInt integer
  - number of digits 
Output: BigInt integer
  - "index of the first fibonacci number"(output) that has the "number of digits" (input)
    specified by the argument
    
Explicit Rules:
  - First fibonacci number has an index of 1
  - Argument is always an int >= 2

===== Test Cases =====
- 2n => 7n
1, 1, 2, 3, 5, 8, 13

- 3n => 12n
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

Data Structures:
- int:  
  - input
  - output
- string: 
  - to compute the number of digits String(fibonacciNum).length === numDigit

===== Algorithms =====
- numDigit is BigInt. 
- initialize `fibonacciIndex` to 1
- while true, 
  - find `fibonacciNum` number from `fibonacci(fibonacciIndex)`
  - if length of `String(fibonacciNum)` is equal to `numDigit`
    - use `BigInt()`
    - return `fibonacciIndex`
  - else, 
    - increment `fibonacciIndex` by 1


fibonacci (HELPER FUNCTION)
- Input: BigInt
- Output: number
  - fibonacci number

Algo
- if n is less than or equal to 2,
  - return 1
- else,
  - return `fibonacci(n-1) + fibonacci(n-2)`
*/

function findFibonacciIndexByLength(digits) {
  let first = 1n;
  let second = 1n;
  let count = 2n;
  let fibonacci;
  
  do {
    fibonacci = first + second;
    count += 1n;
    first = second;
    second = fibonacci;  
  } while(String(fibonacci).length < digits);

  return count;
}

console.log(findFibonacciIndexByLength(2n) === 7n);    // 1 1 2 3 5 8 13
console.log(findFibonacciIndexByLength(3n) === 12n);   // 1 1 2 3 5 8 13 21 34 55 89 144
console.log(findFibonacciIndexByLength(10n) === 45n);
console.log(findFibonacciIndexByLength(16n) === 74n);
console.log(findFibonacciIndexByLength(100n) === 476n);
// findFibonacciIndexByLength(1000n) === 4782n;
// findFibonacciIndexByLength(10000n) === 47847n;

// The last example may take a minute or so to run.