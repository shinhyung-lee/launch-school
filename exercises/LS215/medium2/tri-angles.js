/*

=== Problem ===
Input: 3 int values
Output: a string
      - 'acute': all three angles < 90
      - 'right': one angle === 90
      - 'obtuse': one angle > 90
      - 'invalid':
        - to be valid:
          - sum of angles exactly 180
          - every angle > 0


=== Examples ===
60, 70, 50 => acute
  - sum is 180
120, 50, 10  // "obtuse"
  - sum is 180
0, 90, 90    // "invalid"
  - one angle is 0 degree
50, 50, 50   // "invalid"
  - sum less than 180

=== Data Structures ===
- Number (int)
- array 
  - put angles in an array
  - angles = [s1, s2, s3]

=== Brainstorm ===
- angles = [s1, s2, s3]
  - use for `every` method
  - acute: `every` method
  - right: `filter`, then length should be 1
    - angle === 90
  - obtuse: `filter`, then length should be 1
    - angle > 90

- valid angles
  - sum of angles exactly 180
    - `reduce` to sum angles === 180 
  - every angle > 0
    - `every` angle > 0

=== Algorithms ===
- initialize a variable `angles` with three angles 
  - angles = [a1, a2, a3]
- if `angles` is not valid, 
  - return 'invalid'

- if angles are `acute`, (HELPER isAcute)
  - return `acute`
- if angles are `right`, (HELPER isRight)
  - return `right`
- if angles are `obtuse`, (HELPER isObtuse)
  - return `obtuse`
*/

function isRight(angles) {
  return angles.filter(angle => angle === 90).length === 1;
}

function isAcute(angles) {
  return angles.every(angle => angle < 90);
}

function isObtuse(angles) {
  return angles.filter(angle => angle > 90).length === 1;
}


function isValid(angles) {
  let sum = angles.reduce((accm, angle) => accm + angle, 0);
  let allGreaterThanZero = angles.every((angle) => angle > 0);

  if (sum !== 180 || !allGreaterThanZero) {
    return false;
  }

  return true;
}


function triangle(a1, a2, a3) {
  let angles = [a1, a2, a3];
  if (!isValid(angles)) {
    return 'invalid';
  }

  if (isAcute(angles)) {
    return 'acute';
  } else if (isRight(angles)) {
    return 'right';
  } else if (isObtuse(angles)) {
    return 'obtuse';
  }
}

console.log(triangle(60, 70, 50));       // "acute"
console.log(triangle(30, 90, 60));       // "right"
console.log(triangle(120, 50, 10));      // "obtuse"
console.log(triangle(0, 90, 90));        // "invalid"
console.log(triangle(50, 50, 50));       // "invalid"