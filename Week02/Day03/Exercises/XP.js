console.log("\n****** Week 02 Day 03 - XP Exercise 1: Your favorite colors ******");
// 1. Create an array called colors where the value is a list of your favorite colors.
// 2. Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, 
//    “My #2 choice is red” ect… .
// 3. Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix 
//    for each number.
// Hint : create an array of suffixes to do the Bonus
let colors = ["green", "blue", "red"];
let suffixes = {
    1: "st",
    2: "nd",
    3: "rd",
    4: "th",
    5: "th "
};
console.log("First version :");
for (i in colors) {
    console.log(`My #${+i+1} color is ${colors[i]}`);
};
console.log("Second version :");
for (i in colors) {
    console.log(`My ${+i+1}${suffixes[+i+1]} choice is ${colors[i]}`);
};

console.log("\n****** Week 02 Day 03 - XP Exercise 2 : List of people ******");
let people = ["Greg", "Mary", "Devon", "James"];
console.log(people);
//     Write code to remove “Greg” from the people array.
people.shift();
console.log("Kick Greg out:", people);
//     Write code to replace “James” to “Jason”.
var index = people.indexOf("James");
if (index !== -1) {
    people[index] = "Jason";
};
console.log("Substitute Jason to James:", people);
//     Write code to add your name to the end of the people array.
people.push("Liên");
console.log("Add my name at the end of the list:", people);
//     Using a loop, iterate through the people array and console.log each person.
console.log("Enumerate all people from array:");
for (item of people) { console.log(item); };
//     Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
console.log("Enumerate all people from array up to Jason:");
for (item of people) {
    console.log(item);
    if (item === "Jason") { break; };
};
//     Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
var idx1 = people.indexOf("Mary");
var idx2 = people.indexOf("Liên");
result = people.slice(idx1 + 1, idx2);
console.log("Slice excluding Mary and Liên:", result)
    //     Write code that console.logs Mary’s index. take a look at indexOf on google.
var index = people.indexOf("Mary");
console.log("Find Mary's index:", index);
//     Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
var index = people.indexOf("Foo");
console.log("Find Foo's index (-1 means item not in array):", index);
//     Create a variable called last which value is the last element of the array.
//     Hint: What is the relationship between the index of the last element in the array and the length of the array?
let last = people[people.length - 1];
console.log("The value for last is:", last);

console.log("\n****** Week 02 Day 03 - XP Exercise 3 : Repeat the question ******");
//     Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
//     Tip : Which while loop is more relevant for this situation?
//     Hint : Check the data type you receive from the prompt (ie. typeof method)
do {
    nombre = +prompt("Please enter a number (\"999\" to stop):");
    if (isNaN(nombre)) {
        console.log("That is not a number !");
    } else {
        console.log("nombre = " + nombre);
    };
} while (nombre < 10 || isNaN(nombre));

console.log("\n****** Week 02 Day 03 - XP Exercise 4 : Attendance ******");
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
};
// Given the object above where the key is the students name and the value is the country they are from.
//     Prompt the student for their name :
//         If the name is in the object, console.log the name of the student and the country they come from.
//         example: "Hi! I'm [name], and I'm from [country]."
//         Hint: Look up the statement if ... in
//         If the name is not in the object, console.log: "Hi! I'm a guest."
let inp = prompt("Please enter a name:");
if (inp in guestList) {
    console.log(`Hi! I'm ${inp}, and I'm from ${guestList[inp]}.`);
} else {
    console.log("Hi! I'm a guest");
};

console.log("\n****** Week 02 Day 03 - XP Exercise 5 : Family ******");
//     Create an object called family with a few key value pairs.
//     Console.log the keys. (using a for loop).
//     Console.log the values. (using a for loop).
let family = {
    Durand: "rugby",
    Robinson: "tennis",
    Stevens: "soccer",
    Castelli: "bowling"
};
// let keylist = [];
// let valuelist = [];
// for (nam in family) {
//     keylist.push(nam);
//     valuelist.push(family[nam]);
// }
let keylist = Object.keys(family);
let valuelist = Object.values(family);
let entrylist = Object.entries(family);
console.log("List of keys = ", keylist);
console.log("List of values = ", valuelist);
console.log("List of entries = ", entrylist);

console.log("\n****** Week 02 Day 03 - XP Exercise 6 ******");
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
};
//     Given the object above, console.log “my name is Rudolf the raindeer”
let text = "";
for (key in details) {
    text += key + " " + details[key] + " ";
};
console.log(text);

console.log("\n****** Week 02 Day 03 - XP Exercise 7 : Secret Group ******");
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
//     A group of friends have decided to start a secret society. The society’s name will be the first letter of 
//     each of their names sorted in alphabetical order.
//     Hint: a string is an array of letters
//     Console.log the name of their secret society.
let societyNameArray = [];
for (let i = 0; i < names.length; i++) {
    societyNameArray.push(names[i][0]);
};
societyNameArray.sort();
console.log(societyNameArray.join(""));