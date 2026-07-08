
function staggeredCase(string) {
  let needUpper = true;
  let newChar;

  return string.split('').map((char) => {
    if (/[a-z]/i.test(char)) {
      if (needUpper) {
        newChar = char.toUpperCase();
      } else {
        newChar = char.toLowerCase();
      }

      needUpper = !needUpper;
      return newChar;
    } else {
      return char;
    }
  }).join('');
}

console.log(staggeredCase('I Love Launch School!'));        
// "I lOvE lAuNcH sChOoL!"
console.log(staggeredCase('ALL CAPS'));                     
// "AlL cApS"
console.log(staggeredCase('ignore 77 the 444 numbers'));    
// "IgNoRe 77 ThE 444 nUmBeRs"