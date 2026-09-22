
function reassignArr(arr) {
  arr.push(2);
}

let a = [1];
reassignArr(a);
console.log(a); // [ 1, 2 ]