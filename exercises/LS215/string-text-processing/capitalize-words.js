function capitalizeWord(word) {
  // word is a string 
  return word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase();
}

function wordCap(sentence) {
  let altered = sentence.split(' ').map(capitalizeWord).join(' ');
  console.log(sentence);
  console.log(altered);
}

console.log(wordCap('four score and seven'));       
// "Four Score And Seven"
console.log(wordCap('the javaScript language'));    
// "The Javascript Language"
console.log(wordCap('this is a "quoted" word'));    
// 'This Is A "quoted" Word'