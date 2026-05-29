
const readlineSync = require('readline-sync');

let lengthInMeters = Number(readlineSync.question("Enter the length in m: "));
let widthInMeters = Number(readlineSync.question("Enter the width in m: "));

let areaInMeters = lengthInMeters * widthInMeters;

console.log(`The area of the room is ${areaInMeters} square meters (${areaInMeters * 10.7639} square feet).`)