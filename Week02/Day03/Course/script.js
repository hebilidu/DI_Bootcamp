// Exercise 1 - for loop
// Create a structured HTML file linked to a JS file
// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, 
// it will check if the current number is odd or even, and display a message to the screen.
// Sample Output: //"0 is even" //"1 is odd" //"2 is even"
// for (let i = 0; i < 16; i++) {
//     if (i % 2 === 0) {
//         console.log(i + " is even");
//     } else {
//         console.log(i + " is odd");
//     };
// };

// let person = { fname: "John", lname: "Doe", age: 25 };
// for (let x in person) {
//     console.log(x) //fname lname age
//     console.log(person[x]) // John Doe 25
// }

// Exercise 2 - loop
let names = ["john", "sarah", 23, "Rudolf", 34]
    // 1. Write a JavaScript for loop that will go through the variable names.
    //     if the item is not a string, pass.
    //     if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase 
    //     and then display the name.
for (item of names) {
    if (typeof(item) === "string") {
        item = item.charAt(0).toUpperCase() + item.slice(1);
        console.log(item);
    } else {
        continue;
    }
};
// 2. Write a JavaScript for loop that will go through the variable names
//     if the item is not a string, go out of the loop.
//     if the item is a string, display it.
for (item of names) {
    if (typeof(item) === "string") {
        console.log(item);
    } else {
        break;
    }
};