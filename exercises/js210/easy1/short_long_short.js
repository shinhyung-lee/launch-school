function generateString(shortStr, longStr) {
  return shortStr + longStr + shortStr;
}

function shortLongShort(str1, str2) {
  let result = '';
  if (str1.length > str2.length) {
    result = generateString(str2, str1);
  } else {
    result = generateString(str1, str2);
  }
  return result;
}

console.log(shortLongShort('abc', 'defgh'));    // "abcdefghabc"
console.log(shortLongShort('abcde', 'fgh'));    // "fghabcdefgh"
console.log(shortLongShort('', 'xyz'));         // "xyz"