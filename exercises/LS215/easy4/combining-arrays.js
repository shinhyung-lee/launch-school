
function union(...nums) {
  let unionArr = [];
  nums.forEach(numArr => {
    numArr.forEach(num => {
      if (!unionArr.includes(num)) {
        unionArr.push(num);
      }
    })
  })

  return unionArr;
}

console.log(union([1, 3, 5], [3, 6, 9]));    // [1, 3, 5, 6, 9]