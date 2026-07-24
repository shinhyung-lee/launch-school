
/*
# Supermarket (from Codewars)

There is a queue for the self-checkout tills at the supermarket. Your task is
write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer
represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.

output
The function should return an integer, the total time required.

Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.





*/

/*
Q) What if the input array (customers) is an empty array?

Q) So said test input will be valid, so the second arg will always be a positive int?

Q) What if the first arg is not an array?
	- prolly doesn't happen
	  
	  
Q) What if the second arg is not an int?
	- prolly doesn't happen 
	  
Q) Will the customer array ever be a sparse array?

Aman's question
Q) Do we immediately switch to the next customer when the curr value at till is 0? 

Data Structures:
- create n arrays 
- let tills = [];
- let totalSecond = 0;
- for (let num = 1; num < numCustomers; num += 1) {
	if (customers.length !== 0) {
		tills.push(customers.shift());
	}
}

- while(!tills.every(timeLeft => timeLeft === 0)) {
	tills = tills.map(timeLeft => timeLeft - 1);
	totalSecond += 1;
	// if one (or more lines) are 0, add the next customer 
	// how many? 
	// 
}
*/
function queueTime(customers, numTills) {
  let tills = [];
  let totalSecond = 0;
  for (let num = 1; num <= numTills; num += 1) {
    if (customers.length !== 0) {
      tills.push(customers.shift());
    }
  }
  console.log(tills);
  while(!tills.every(timeLeft => timeLeft === 0)) {
    tills = tills.map(timeLeft => timeLeft - 1);
    totalSecond += 1;
    // if any of the element is 0, and we have anything left in customers
    // push the customer to the till.
    tills.forEach((till, idx, arr) => {
      console.log(till);
      if (till === 0 && customers.length !== 0) {
        arr[idx] = customers.shift();
      }
    })
    // console.log(customers);
    // console.log(tills);
  }

  // console.log(totalSecond);
}

console.log(queueTime([5,3,4], 1));
// should return 12
// because when there is 1 till, the total time is just the sum of the times

// console.log(queueTime([10,2,3,3], 2));
// should return 10
// because here n=2 and the 2nd, 3rd, and 4th people in the
// queue finish before the 1st person has finished.

// console.log(queueTime([2,3,10], 2));
// should return 12