/*

=== Problem ===

=== Examples ===
Input: an int that signifies year
Output: an int
        -number of 'Friday the 13ths' in that year

Rules:
  - year > 1752 (given)

=== Data Structures ===
- Date: 
- int

=== Brainstorm ===
- Date: 
  - need new Date(year, month, day)
    - year: given
    - month: loop 0 ~ 11 (Jan ~ Dec)
    - day: 13 (fixed)
  - if this Date is getDate() === 6 (Friday)  
    - increment numFridays by 1

=== Algorithms ===
- initialize a variable `numFridays` to 0
- iterate Jan - Dec (0 - 11 for month) of the given year,
  - if new Date(year, month, day)'s getDate() === 6 (Friday)
    - increment `numFridays` by 1
- return `numFridays`

*/

function fridayThe13ths(year) {
  let numFridays = 0;
  for (let month = 0; month <= 11; month += 1) {
    let date = new Date(year, month, 13);
    if (date.getDay() === 5) {
      numFridays += 1;
    }
  }

  return numFridays;
}

console.log(fridayThe13ths(1986));      // 1
console.log(fridayThe13ths(2015));      // 3
console.log(fridayThe13ths(2017));      // 2