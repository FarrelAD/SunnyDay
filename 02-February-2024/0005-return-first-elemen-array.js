// Return first value
// Source: https://edabit.com/challenge/QaApgtePE6QrCZ64o
// 1 February 2024

// Function to return first value of array
// 1st method - basic function
// function getFirstValue(arr) {
// 	return arr[0]
// }

// 2nd method - lambda function
// const getFirstValue = arr => arr[0]


// 3rd method - inefficient method
function getFirstValue(arr) {
	let maxArrayLength = arr.length;
	let firstValueOfArray = 0;
	for (let i = maxArrayLength -1; i >= 0; i--) {
		if (i == 0) {
			return firstValueOfArray = arr[i]
		}
	}
}

console.log(getFirstValue([4, 5, 6, 800]))