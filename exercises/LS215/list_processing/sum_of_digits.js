
function sum(number) {
  const numArray = String(number).split('');
  const numberSum = numArray.reduce((accm, numChar) => accm + Number(numChar), 0);
  return numberSum;
}

console.log(sum(23));           // 5
console.log(sum(496));          // 19
console.log(sum(123456789));    // 45