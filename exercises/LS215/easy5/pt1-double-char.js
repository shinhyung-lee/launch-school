
function repeater(string) {
  let result = '';
  for (let idx = 0; idx < string.length; idx += 1) {
    let char = string[idx];
    result += (char.repeat(2));
  }

  return result;
}

console.log(repeater('Hello') === "HHeelllloo");        
// "HHeelllloo"
console.log(repeater('Good job!') === "GGoooodd  jjoobb!!");    
// "GGoooodd  jjoobb!!"
console.log(repeater('') === "");             // ""