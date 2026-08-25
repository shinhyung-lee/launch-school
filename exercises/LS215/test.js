
function makeProduct(id, name, stock, price) {
  return {
    id,
    name,
    stock,
    price, 

    describe() {
      console.log(
        `=> Name: ${this.name}\n` + 
        `=> ID: ${this.id}\n` + 
        `=> Price: ${this.price}\n` + 
        `=> Stock: ${this.stock}`
      );
    },

    setPrice(newPrice) {
      if (typeof newPrice !== 'number' || newPrice < 0) {
        throw new RangeError('Invalid price value!');
      }

      this.price = newPrice;
    }
  }
}

let scissors = makeProduct(0, 'Scissors', 8, 10);
let drill = makeProduct(1, 'Cordless Drill', 15, 45);

// let scissors = {
//   id: 0,
//   name: 'Scissors',
//   stock: 8,
//   price: 10,
// };

// let drill = {
//   id: 1,
//   name: 'Cordless Drill',
//   stock: 15,
//   price: 45,
// };

// function changePrice(product, newPrice) {
//   if (typeof newPrice !== 'number' || newPrice < 0) {
//     throw new RangeError('Invalid price value!');
//   }

//   product.price = newPrice;
// }

// function describeProduct(product) {
//   console.log(
//     `=> Name: ${product.name}\n` + 
//     `=> ID: ${product.id}\n` + 
//     `=> Price: ${product.price}\n` + 
//     `=> Stock: ${product.stock}`
//   )
// }

// changePrice(drill, 100);
// console.log(drill);
// describeProduct(scissors);
