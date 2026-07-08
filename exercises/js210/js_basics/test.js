function capitalize(word) {
  return word[0].toUpperCase() + word.slice(1);
}

function exclaim(word) {
  return word += '!!!';
}

let word = 'hello';
let capitalizedWord = capitalize(word); // 'Hello'
let exclaimedWord = exclaim(capitalizedWord); // 'Hello!!!'

console.log(word); //'hello'
console.log(capitalizedWord);
console.log(exclaimedWord);