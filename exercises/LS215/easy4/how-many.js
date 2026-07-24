


const vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
                'motorcycle', 'suv', 'motorcycle', 'car', 'truck'];

function logOccurrences(obj) {
  for (let key in obj) {
    console.log(`${key} => ${obj[key]}`);
  }
}

function countOccurrences(vehicles) {
  let vehicleCount = {};
  for (let vehicle of vehicles) {
    if (vehicleCount[vehicle]) {
      vehicleCount[vehicle] += 1;
    } else {
      vehicleCount[vehicle] = 1;
    }
  }

  logOccurrences(vehicleCount);
}                
countOccurrences(vehicles);

// console output
// car => 4
// truck => 3
// SUV => 1
// motorcycle => 2
// suv => 1