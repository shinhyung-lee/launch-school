/*
Solved: 7/7/2026

Write a function that returns the position of the closest active opponent. 
If two opponents are equidistant, 
  return the opponent with the higher position on the board.

Understand the Problem
Implicit Rules:
  -

Explicit Rules:
  - For two opponents with equidistant,
    - return the opponent with the higher position on the board.

===== Questions =====
Q. Will my position always be a int? If not, how to handle it?
  - return undefined

Q. If opponent's position is not a valid number, how to handle it?
  - What is valid position? ( >= 0) ?
  - null, undefined, array, object, etc.
  - ignore them.

Q. What if opponent position object is an empty object?
  - return undefined

Q. What if opponent position object is not an object type?
  - return undefined

===== Test Cases =====


Data Structures
- arrays 
  - Object.values(positions) to extract opponents' positions
- Math.max() to get higher position value, if two positions are equidistant
- Number
  - Calculate distance difference

Algorithms

positions = {
  "Opponent 1a" : 1,
  "Opponent 1b" : 5
}
distances = [1, 5]
closestPosition = 1
my position = 3
returns 5

positions = {
  "Opponent 1" : 1,
  "Opponent 2" : 15,
  "Opponent 3" : 37
}
my position = 10
returns 15

  - If `position` is not a number, return undefined
  - If `positions` is not an object, return undefined
  - If `positions` is an empty object, return undefined

  - Get op distances by extracting Object values (`positionArr`)
  - Clean `positionArr` by removing non-number values
    - `filter` numbers only 
    - if `cleanedArray` 's length is 0, return `undefined`
  - Initialize `closestPosition` to first (0th) element of `cleanedArray`
  - Iterate through every element in `closestPosition`
    - `currentDistance` is `Math.abs(myPosition - element)`
    - `closestDistance` is `Math.abs(myPosition - closestPosition)`
    - if `currentDistance < closestDistance`,
      - Update `closestPosition` to `element`
    - if `currentDistance === closestDistance`,
      - Update `closestPosition` to bigger value between `element` and `closestPosition` (Math.max)
  
  - return `closestPosition`
*/

function findClosestOpponent(positions, position) {
  if (typeof position !== 'number' || typeof positions !== 'object' || Object.keys(positions).length === 0) {
    return undefined;
  }

  let positionNums = Object.values(positions).filter(position => typeof position === 'number');
  // console.log(positionNums); // [1, 15, 37]
  if (positionNums.length === 0) {
    return undefined;
  }

  return positionNums.reduce((closestPos, currPos) => {
    let currDistance = Math.abs(position - currPos);
    let closestDistance = Math.abs(position - closestPos);
    if (currDistance < closestDistance) {
      closestPos = currPos;
    } else if (currDistance === closestDistance) {
      closestPos = Math.max(closestPos, currPos);
    }

    return closestPos;
  }, positionNums[0]);

}

// console.log(typeof {});

console.log(findClosestOpponent({
  "Opponent 1" : 1,
  "Opponent 2" : 15,
  "Opponent 3" : 37
}, 10)); // 15

console.log(findClosestOpponent({
  "Opponent 1a" : 1,
  "Opponent 1b" : 5
}, 3)); // 5

console.log(findClosestOpponent({
  "Opponent 1a" : 1, "Opponent 1b" : 5,
  "Opponent 1c" : 50, "Opponent 1d" : 100, "Opponent 1e" : null
}, 150)); // 100