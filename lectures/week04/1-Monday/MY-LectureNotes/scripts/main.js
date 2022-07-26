// let firstName = 'Christian'

// let lastName = "Votion"

// console.log(firstName+' '+lastName)

// let greeting = `my name is ${firstName} ${lastName}`
// console.log(greeting)


// let a = 50
// let b = 50

// let sum = a+b

// console.log(`the sum of a and b is ${sum}`)

// let firstLength = firstName.length
// let lastLength = lastName.length

// let nameSum = firstLength+lastLength

// console.log(`The combined length of first and last name is ${nameSum}`)

// let name1 = firstName + " " + lastName



// console.log(name1.indexOf(lastName))

// if (a > b){
//     console.log(`${a} is greater than ${b}`)
// }
// else if (b>a){
//     console.log(`${a} is less than ${b}`)
// }
// else {
//     console.log(`${a} is equal to ${b}`)
// }

// let month = 13

// switch(month){
//     case 1:
//     case 3:
//     case 5:
//     case 7:
//     case 8:    
//     case 10:
//     case 12:
//         console.log(`${month} has 31 days`);
//         break;
//     case 4:
//     case 6:
//     case 9:
//     case 11:
//         console.log(`${month} has 30 days`)
//         break;
//     case 2:
//         console.log(`${month} has 28 days`)
//         break;   
//     default:
//         console.log("That is not a valid month")             
// }

// count = 0
// while (count <= 20){
//     if (count %2 == 0){
//         console.log(count)
//     }
//     count += 1
// }

// for (let count = 0; count <= 20; count ++){
//     if (count %2==0){
//         console.log(count)
//     }
// }

for (let count = 1; count <= 30; count++){
    if(count %3==0 && count%5==0){
        console.log("fizz buzz")
    }
    else if (count %3 ==0){
        console.log("fizz")
    }
    else if (count %5==0){
        console.log("buzz")
    }
    else {
        console.log(count)
    }
}


// Given a string change the every second letter to an uppercase ‘Z’.
// Assume there are no spaces.







let str1 = "javascript";
arr = str1.split('')
console.log(arr)
let count = 0
while (count <= arr.length){
    if (count %2 != 0){
        arr[count] = 'Z'
    }
    count += 1
}
console.log(arr.join(''))


// Example output:
// jZvZsZrZpZ OR each letter on a new line
// HINT: You can use  if((i+1) % 2 == 0) to check for even indexes

// Directions
// JavaScript 101 Exercises
// You will be rewriting in JavaScript a series of exercises you've written in Python. There will also be a few new challenges. Because JavaScript's pop-up prompt is annoying (and doesn't work in Node.js), we won't take in any user input. Instead, you will write each exercise as a function, and any required input will be supplied to the function as arguments.

// For each exercise, create a new file. To run a file javascript file using node, you can run it from your terminal like this:

// $ node theNameOfTheFile.js
// Hello You!
// Write a function hello which given a name, says hello to the name. Use the following template:

// function hello(name) {
  // put your code here
// }
// hello('Mustache');
// Make the above program print the following to the console:

// Hello, Mustache!
// Hello You! Part 2
// Modify your hello program such that if no name is given: hello(), it will print "Hello, world!", otherwise it behaves the same as previously.

// Madlib
// Write a madlib function, which is given a name and a subject. It will return(not print) a new string: (name)'s favorite subject in school is (subject).

// Example:

// madlib('Anushka', 'art');
// Output

// 'Anushka's favorite subject in school is art.'
// Tip Calculator
// Write a function tipAmount that is given the bill amount and the level of service (one of good, fair and poor) and returns the dollar amount for the tip. Based on:

// good -> 20%

// fair -> 15%

// bad -> 10%

// tipAmount(100, 'good');
// 20

// tipAmount(40, 'fair');
// 6
// Tip Calculator 2
// Write a function totalAmount that takes the same arguments as tipAmount except it returns the total as the tip amount plus the bill amount. This function may make use of tipAmount as a sub-task.

// > totalAmount(100, 'good')
// 120

// > totalAmount(40, 'fair')
// 46
// Tip Calculator 3
// Write a function splitAmount that takes the bill amount and the level of service, and the number of people to split the bill between. It will return the final amount for each person.

// splitAmount(100, 'good', 5);
// 24

// splitAmount(40, 'fair', 2);
// 23
