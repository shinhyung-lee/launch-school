/*
Input: 3 triangle sides (Number, int)
Output: a string 
      - 3 valid types or 'invalid'

Rules:
- valid triangle:
  - sum of the lengths of the two shortest sides must be greater than the length of the longest side
  - every side must have a length greater than 0
  - "invalid" triangle

=== Data Structures ===
- number (int)
- array: Array.prototype.every method

=== Branstorm ===
- longest = Math.max(s1, s2, s3)
- shortest = Math.min(s1, s2, s3)
- middle = sum - (longest + shortest)
    => shortest + middle > longest 
- [s1, s2, s3].every(length all greater than 0)

=== Algorithms === 
*** isEquilateral (HELPER function) ***
- Input: 2 ints
  - max and min lengths
- Output: boolean
  - if (max === min), return true
  - otherwise, return false 

*** isScalene (HELPER function) *** 
- Input: 3 ints
- Output: boolean
  - if s1 !== s2 && s2 !== s3, return true
  - else, return false 

*** isInvalid (HELPER function) ***
- Input: 3 ints
- Output: boolean
  - if 3 sides consist invalid, return `true`
  - otherwise, return `false`

- if not shortest + middle > longest 
- if not [s1, s2, s3].every(length all greater than 0)

*** Main function (triangle) ***
- longest = Math.max(s1, s2, s3)
- shortest = Math.min(s1, s2, s3)
- middle = sum - (longest + shortest)
    => shortest + middle > longest 
- [s1, s2, s3].every(length all greater than 0)

- If 3 sides consist invalid triangle, return 'invalid'
  - HELPER (isInvalid)

- If 3 sides consist `Equilateral` (HELPER, isEquilateral)
  - return `equilateral`
- else if 3 sides consist `Scalene` (HELPER, isScalene)
  - return `scalene`
- else,
  - return `isosceles`
*/
function triangle(s1, s2, s3) {
  let sum = [s1, s2, s3].reduce((accm, num) => accm + num, 0);
  let longest = Math.max(s1, s2, s3);
  let shortest = Math.min(s1, s2, s3);
  let middle = sum - (longest + shortest);

  if (isInvalid(shortest, middle, longest)) {
    return 'invalid';
  }

  if (isEquilateral(shortest, longest)) {
    return 'equilateral';
  } else if (isScalene(shortest, middle, longest)) {
    return 'scalene';
  } else {
    return 'isosceles';
  }
}

function isEquilateral(min, max) {
  if (min === max) {
    return true;
  }

  return false;
}

function isScalene(s1, s2, s3) {
  if (s1 !== s2 && s2 !== s3) {
    return true;
  }

  return false;
}

function isInvalid(short, middle, long) {
  let sides = [short, middle, long];
  if (short + middle <= long) {
    return true;
  } else if (!sides.every(side => side > 0)) {
    return true;
  }

  return false;
}

console.log(triangle(3, 3, 3));        // "equilateral"
console.log(triangle(3, 3, 1.5));      // "isosceles"
console.log(triangle(3, 4, 5));        // "scalene"
console.log(triangle(0, 3, 3));        // "invalid"
console.log(triangle(3, 1, 1));        // "invalid"