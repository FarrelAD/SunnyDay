// TITLE: MAKE A CIRCLE WITH OOP
// TASK : Create a Circle constructor that creates a circle with a radius provided by an argument. 
//        The circles constructed must have two methods getArea() (PI*r^2) and getPerimeter() (2*PI*r) 
// Source: https://edabit.com/challenge/Hgb38yhWGwJCMHbRQ
// 6 February 2024

// Example class to count the area and perimeter of rectangle
class Rectangle {
    constructor(sideA, sideB) {
        this.sideA = sideA
        this.sideB = sideB
    }
    getArea(){return this.sideA*this.sideB}
    getPerimeter(){return (this.sideA + this.sideB) *2}
}

// 1st method
// class Circle {
//     constructor(radius) {
//         this.radius = radius
//         this.pi = Math.PI
//     }

//     getArea() {return this.pi * this.radius ** 2}
//     getPerimeter() {return 2 * this.pi * this.radius}
// }

// 2nd method
class Circle {
    constructor(radius) {
        this.radius = radius
        this.pi = Math.PI
    }

    // Use Math.pow() function
    getArea() {return this.pi * Math.pow(this.radius, 2)}
    getPerimeter() {return 2 * this.pi * this.radius}
}

// Testing
let q = new Circle(4.44);
console.log(q.getArea());
console.log(q.getPerimeter());