
/*
===== Problem ===== 
Depending on the argument, we have n number of switches
ex) n = 5, we have switches 1...5
ex) n = 100, switches 1...100

Explicit Rules:

Implicit Rules:
- `n` needs to be greater than or equal to 1

===== Questions =====
Q) What if n is not an int?

Q) What if n is an int less than or equal to 1?
  - return an empty array 

===== Examples and Test Cases =====
n = 5 => [1, 4]
n = 100 => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

n = 3 => [1, 2 ,3]
Round 1: all lights on 
Round 2: light 2 off 
Round 3: light 3 off
At the end, we have [1]

===== Data Structures =====
- object
  - { num: n, isOn: true / false, }
- array
  - toggle each number, each iteration

===== Algo =====
- initialize an empty obj `lightInfo` []
- Iterate through numbers 1 to n (inclusive),
  - set property { num: idx, isOn: false, }
  - push this object to `lightInfo` array 

- Iterate through numbers 1 to n (inclusive),
  Round 1
  - idx: multiples of 1
  - Toggle `isOn` property 
  Round 2
  - idx: multiples of 2
  - Toggle `isOn` property 
  - modulo 
  - currIdx
  - as we iterate through each obj inside of `lightInfo` with `divisor + 1` (idx)
    - iterate through each obj in `lightInfo` with `num + 1` (idx)
      - `num + 1` % `divisor + 1` is equal to `0`,
        - toggle `isOn` property at `num + 1`th object in `lightInfo`
  - iterate through `lightInfo` array (map)
    - extract `obj.num` if `obj.isOn` is true
  - return the array 

HELPER function `toggleLight` 
Input: obj
Output: n/a
Side Effect: `isOn` property will be toggled

obj[isOn] = !obj[isOn];

n = 3
[ 
  {num: 1, isOn: false}, 
  {num: 2, isOn: false}, 
  {num: 3, isOn: false}
]
idx = 0, divisor + 1 = 1
  idx = 0, num + 1 = 1
    (divisor + 1) % (num + 1) === 0
    toggle
  idx = 1, num + 1 = 2
    (divisor + 1) % (num + 1) === 0
    toggle
  idx = 2, num + 1 = 3
    (num + 1) % (divisor + 1) === 0
    toggle

idx = 1, divisor + 1 = 2
  idx = 0, num + 1 = 1
    (num + 1) % (divisor + 1) === 0
    1 % 2 !== 0
    don't touch
  idx = 1, num + 1 = 2
    (num + 1) % (divisor + 1) === 0
    2 % 2 === 0
    toggle
  idx = 2, num + 1 = 3
    (num + 1) % (divisor + 1) === 0
    3 % 2 !== 0
    don't touch 

idx = 2, divisor + 1 = 3
  idx = 0, num + 1 = 1
    (num + 1) % (divisor + 1) === 0
    1 % 3 !== 0
    don't touch
  idx = 1, num + 1 = 2
    (num + 1) % (divisor + 1) === 0
    2 % 3 !== 0
    don't touch
  idx = 2, num + 1 = 3
    (num + 1) % (divisor + 1) === 0
    3 % 3 === 0
    toggle 
*/
function toggleLight(obj) {
  obj.isOn = !obj.isOn;
}

function lightsOn(num) {
  if (typeof num !== 'number') {
    return null;
  }
  if (num < 1) { return []; }

  let lightInfo = [];
  for (let idx = 1; idx <= num; idx += 1) {
    lightInfo.push({ num: idx, isOn: false, });
  }
  lightInfo.forEach((lightObj, divisor) => {
    divisor = divisor + 1;
    lightInfo.forEach((obj, number) => {
      number = number + 1;
      if (number % divisor === 0) {
        toggleLight(obj);
      }
    })
  })

  return lightInfo.reduce((accm, obj) => {
    if (obj.isOn) {
      accm.push(obj.num);
    }
    return accm;
  }, [])
}



// n is not an int, return null
console.log(lightsOn({a: 1, b: 1}));      // null
console.log(lightsOn([1, 2, 3]));         // null
console.log(lightsOn(true));              // null

// n less than or equal to 1
console.log(lightsOn(0));        // []
console.log(lightsOn(-100));     // []

console.log(lightsOn(5));        // [1, 4]
// // Detailed result of each round for `5` lights
// // Round 1: all lights are on
// // Round 2: lights 2 and 4 are now off;     1, 3, and 5 are on
// // Round 3: lights 2, 3, and 4 are now off; 1 and 5 are on
// // Round 4: lights 2 and 3 are now off;     1, 4, and 5 are on
// // Round 5: lights 2, 3, and 5 are now off; 1 and 4 are on

console.log(lightsOn(100));      // [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]