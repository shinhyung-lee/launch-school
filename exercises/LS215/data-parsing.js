const traineeData = `ID: T01
Name: Kim Minjun
Skills: Vocal 85, Dance 92, Rap 78, Charisma 88

ID: T02
Name: Lee Sora
Skills: Vocal 95, Dance 91, Visual 93

ID: T03
Name: Park Jiwoo
Skills: Rap 65, Dance 75, Songwriting 72`;

let dataArr = traineeData.split('\n\n');

dataArr = dataArr.map(traineeData => {
  return traineeData.split('\n');
});

dataArr = dataArr.map(traineeInfoArr => {
  return traineeInfoArr.map((string, idx) => {
    if (idx !== 2) {
      return string.split(': ')[1];
      // ['ID', 'T01'] => 'T01'
      // ['Name', 'Kim Min'] => 'Kim Min'
    } else {
      return string.match(/\d{1,3}/g);
      // [65, 75, 72]
    }
  })
});
console.log(dataArr);
/*
Output
[
  [ 'T01', 'Kim Minjun', [ '85', '92', '78', '88' ] ],
  [ 'T02', 'Lee Sora', [ '95', '91', '93' ] ],
  [ 'T03', 'Park Jiwoo', [ '65', '75', '72' ] ]
]
*/