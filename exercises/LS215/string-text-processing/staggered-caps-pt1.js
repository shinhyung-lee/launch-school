
function staggeredCase(sentence) {
  return sentence.split('').map((char, idx) => {
    if (idx % 2 === 0) {
      return char.toUpperCase();
    } else if (idx % 2 === 1) {
      return char.toLowerCase();
    } 
  }).join('');
}

console.log(staggeredCase('I Love Launch School!'));        
// "I LoVe lAuNcH ScHoOl!"
console.log(staggeredCase('ALL_CAPS'));                     
// "AlL_CaPs"
console.log(staggeredCase('ignore 77 the 4444 numbers'));   
// "IgNoRe 77 ThE 4444 nUmBeRs"