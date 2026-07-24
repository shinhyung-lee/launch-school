/*

=== Problem ===
Input: floating point number
        - representing an angle between 0 and 360 degrees
Output: a string
        - representing that angle in degrees, minutes, and seconds

Rules:
  - use a degree symbol (°) to represent degrees, 
  - a single quote (') to represent minutes, and 
  - a double quote (") to represent seconds.

  - There are 60 minutes in a degree, and 
  - there are 60 seconds in a minute.

=== Examples === 
30 => "30°00'00\""
76.73 => "76°43'48\""
0 => "0°00'00\""
254.6 => "254°35'59\""
360 => "360°00'00\"" || "0°00'00\""

=== Questions === 
- What if angle is not an int
  - angle will be an int 
- What if angle is a number less than 0
  - angle will always be an int greater than or equal to 0

=== Data Structures ===
- Number (int, float)
  - decimal = angle % 1
  - 60 mins in an angle
    - 1 angle = 60 mins
    - 1 / 60 angle = min 
    - 0.5 => what minute? 
    - 0.5 angle => 30 mins 
    - angle * 60
  - 60 sec in a min
    - 1 min = 60 sec

=== Algo === 
- Filter out whole number and decimal
  - wholeNumber = Math.floor(angle / 1)
  - decimal = angle % 1


*/

const DEGREE = '\u00B0'; // degree symbol
// console.log(Math.floor(76.73 / 1));
// console.log(Math.floor(360 / 1));
// console.log(Math.floor(0 / 1));
// console.log(Math.floor(93.034773 / 1));

function dms(angle) {
  let decimal = angle % 1;
  let wholeNumber = Math.floor(angle / 1);
  // console.log(String(decimal * 60).padStart(0, 2));
  // console.log(decimal * 60);
  // console.log(String(Math.floor(decimal * 60)).padStart(2, 0));
  let minute = Math.floor(decimal * 60);
  let second = Math.floor(((decimal * 60) % 1) * 60);

  console.log(`${String(wholeNumber)}${DEGREE}${String(minute).padStart(2, 0)}'${String(second).padStart(2, 0)}"`);
  return `${String(wholeNumber)}${DEGREE}${String(minute).padStart(2, 0)}'${String(second).padStart(2, 0)}"`
}

// All test cases should return true
console.log(dms(30) === "30°00'00\"");
console.log(dms(76.73) === "76°43'48\"");
console.log(dms(254.6) === "254°35'59\"");
console.log(dms(93.034773) === "93°02'05\"");
console.log(dms(0) === "0°00'00\"");
console.log(dms(360) === "360°00'00\"" || dms(360) === "0°00'00\"");