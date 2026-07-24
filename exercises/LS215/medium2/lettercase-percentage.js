/*

Number.toFixed(3)

=== Problem ===
Input: a string
Output: an object
      - 3 key-value pairs
      - lowercase letters
      - uppercase letters
      - neither

=== Data Structures ===
- string: input
- Number (int)
  - keeping track of lowercase, uppercase, and neither
- object: output

=== Algorithms ===
- initialize variable `lower` to 0
- initialize `upper` to 0
- initialize `neither` to 0
- iterate through every char in `string`
  - increment `lower`, `upper`, and `neither` accordingly
- initialize variable `total` = sum of `lower + upper + neither`
- get percentage 
  ex) lowercase = (lower / total * 100).toFixed(2)
  uppercase, neither
- return an object 
  {
    lowercase,
    uppercase,
    neither,
  }
object property shorthand syntax

'abCdef 123' =>
{ lowercase: "50.00", uppercase: "10.00", neither: "40.00" }

'123' =>
{ lowercase: "0.00", uppercase: "0.00", neither: "100.00" }

- initialize variable `lower` to 0
- initialize `upper` to 0
- initialize `neither` to 0
- iterate through every char in `string`
  - increment `lower`, `upper`, and `neither` accordingly
- initialize variable `total` = sum of `lower + upper + neither`
- get percentage 
  ex) lowercase = (lower / total * 100).toFixed(2)
  uppercase, neither
- return an object 
  {
    lowercase, uppercase, neither,
  } 
*/

function letterPercentages(string) {
  let lower = 0;
  let upper = 0;
  let neither = 0;
  
  for (let char of string) {
    if (isLower(char)) {
      lower += 1;
    } else if (isUpper(char)) {
      upper += 1;
    } else {
      neither += 1;
    }
  }

  let sum = lower + upper + neither;
  let lowercase = (lower / sum * 100).toFixed(2);
  let uppercase = (upper / sum * 100).toFixed(2);
  neither = (neither / sum * 100).toFixed(2);

  return {
    lowercase,
    uppercase,
    neither,
  }
}

const isLower = (char) => /[a-z]/.test(char);
const isUpper = (char) => /[A-Z]/.test(char);
// console.log((40.123).toFixed(1))

console.log(letterPercentages('abCdef 123'));
// { lowercase: "50.00", uppercase: "10.00", neither: "40.00" }

console.log(letterPercentages('AbCd +Ef'));
// { lowercase: "37.50", uppercase: "37.50", neither: "25.00" }

console.log(letterPercentages('123'));
// { lowercase: "0.00", uppercase: "0.00", neither: "100.00" }