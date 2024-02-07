// TITLE: TEMPERATURE CONVERSION
// TASK : Write a program that takes a temperature input in celsius and converts it to Fahrenheit and Kelvin.
//        Return the converted temperature values in an array.
// Source: https://edabit.com/challenge/QW5CApff3WAGszrWY
// 7 Febuary 2024

// Function to convert temperature
// 1st method
// function tempConversion(celsius) {
//     const kelvinTemp = Math.round((celsius + 273.15) * 100) / 100
//     const fahrenheitTemp = Math.round((celsius * 9 / 5 + 32) * 100) / 100
//     const convertedTemp = [fahrenheitTemp, kelvinTemp]
//     const result = kelvinTemp > 0 ? convertedTemp : 'Invalid'
//     return result
// }

// 2nd method
function tempConversion(celsius) {
    const kelvinTemp = Math.round((celsius + 273.15) * 100) / 100
    const fahrenheitTemp = Math.round((celsius * 9 / 5 + 32) * 100) / 100
    const result = kelvinTemp > 0 ? [fahrenheitTemp, kelvinTemp] : 'Invalid'
    return result
}

// 3rd method
// function tempConversion(celsius) {
//     const result = Math.round((celsius + 273.15) * 100) / 100 > 0 ? [(Math.round((celsius * 9 / 5 + 32) * 100) / 100), (Math.round((celsius + 273.15) * 100) / 100)] : 'Invalid'
//     return result
// }

// Testing
console.log(tempConversion(100))
console.log(tempConversion(-10))
console.log(tempConversion(300.4))
console.log(tempConversion(-273.16))