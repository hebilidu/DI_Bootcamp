console.log("\n****** Week02 Day 04 - XP Ninja Exercise 1: Random Number ******");
/* Get a random number between 1 and 100.
   Console.log all even numbers from 0 to the random number.
*/
let pick = Math.floor(1 + Math.random() * 100);
for (i = 0; i <= pick; i += 2) { console.log(i) };

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Ninja Exercise 2: Capitalized letters ******");
/*
Create a function that takes a string as an argument.
Have the function return:
        The string but all letters in even indexes should be capitalized.
        The string but all letters in odd indexes should be capitalized.
        Note:
        Index 0 will be considered even.
        The argument of the function should be a lowercase string with no spaces.
For example,
capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']
*/
function capitalize(str) {
    out1 = "";
    out2 = "";
    for (i in str) {
        if (i % 2 === 0) {
            out1 += str[i].toUpperCase();
            out2 += str[i];
        } else {
            out1 += str[i];
            out2 += str[i].toUpperCase();
        }
    };
    return [out1, out2];
};
console.log(capitalize("abcdef"));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Ninja Exercise 3 : Is palindrome? ******");
/* 
Write a JavaScript function that checks whether a string is a palindrome or not.
Note A palindrome is a word, phrase or sequence that is spelled the same both 
backwards and forward, e.g., madam, bob or kayak. palindrome 
*/
txt = prompt("Enter a text : ");

function isPalindrome(txt) {
    len = txt.length;
    for (i = 0; i < Math.floor(len / 2); i++) {
        if (txt[i] !== txt[len - 1 - i]) { return false };
    };
    return true;
};

console.log("Is \"" + txt + "\" a palindrome ? " + isPalindrome(txt));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Ninja Exercise 4 : Biggest Number ******");
/* 
Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
Note : This function should work with any array;
*/
const array1 = [-1, 0, 3, 100, 99, 2, 99]; // should return 100 
const array2 = ['a', 3, 4, 2]; // should return 4 
const array3 = []; // should return 0
const array4 = [-4, -3]

function biggestNumberInArray(arrayNumber) {
    let biggest = "";
    for (item of arrayNumber) {
        if (isNaN(item) === false && biggest === "") { biggest = item };
        if (isNaN(item) === false && item > biggest) { biggest = item };
    };
    return biggest + 0;
}
console.log("Biggest item from \[" + array1 + "\] is : " + biggestNumberInArray(array1));
console.log("Biggest item from \[" + array2 + "\] is : " + biggestNumberInArray(array2));
console.log("Biggest item from \[" + array3 + "\] is : " + biggestNumberInArray(array3));
console.log("Biggest item from \[" + array4 + "\] is : " + biggestNumberInArray(array4));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Ninja Exercise 5: Unique Elements ******");
/*
Write a JS function that takes an array and returns a new array with only unique elements.
Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
*/

function filtre(array) {
    let output = [];
    for (i of array) {
        isIn = false;
        for (j of output) { if (j === i) { isIn = true }; }
        if (!isIn) { output.push(i) };
    }
    return output;
}
const arr1 = [1, 2, 3, 3, 3, 3, 4, 5];
const arr2 = [1, 2, 3, 7, 3, 4, 3, 5];
console.log("[", arr1, "] gives : ", filtre(arr1));
console.log("[", arr2, "] gives : ", filtre(arr2));