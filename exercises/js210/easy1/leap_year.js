
function isLeapYear(year) {
  if (year < 0) {
    console.log(false);
    return false;
  }
  
  if (year % 400 === 0) {
    console.log(true);
    return true;
  } else if (year % 100 === 0) {
    console.log(false);
    return false;
  } else if (year % 4 === 0) {
    console.log(true);
    return true;
  } else {
    console.log(false);
    return false;
  }
}

isLeapYear(2016);      // true
isLeapYear(2015);      // false
isLeapYear(2100);      // false
isLeapYear(2400);      // true
isLeapYear(240000);    // true
isLeapYear(240001);    // false
isLeapYear(2000);      // true
isLeapYear(1900);      // false
isLeapYear(1752);      // true
isLeapYear(1700);      // false
isLeapYear(1);         // false
isLeapYear(100);       // false
isLeapYear(400);       // true