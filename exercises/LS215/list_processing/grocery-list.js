
function buyFruit(fruits) {
  // map then reduce 
  // helper function `repeat` (takes array [fruitName, count])
  //  returns 1D array with fruitName included `count` times in it
  return fruits.map(repeat)
               .reduce((groceryList, list) => groceryList.concat(list), []);
}

function repeat([fruitName, count]) {
  let result = [];
  for (let idx = 0; idx < count; idx += 1) {
    result.push(fruitName);
  }

  return result;
}

console.log(buyFruit([['apple', 3], ['orange', 1], ['banana', 2]]));
// returns ["apple", "apple", "apple", "orange", "banana", "banana"]