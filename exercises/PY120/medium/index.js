function binarySearch(sortedArray, target) {
  let start = 0;
  let end = sortedArray.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (sortedArray[mid] === target) {
      return mid; // Target found
    } else if (sortedArray[mid] < target) {
      start = mid + 1; // Search right half
    } else {
      end = mid - 1; // Search left half
    }
  }
  return -1; // Target not found
}

arr = [1, 3, 5, 7, 10, 12]
console.log(binarySearch(arr, 7))