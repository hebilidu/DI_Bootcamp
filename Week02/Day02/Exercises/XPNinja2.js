// Week 02 Day 2 Ninja 2 : ZIP Code
/* 
Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

    While working in a Post Office you must have the clients’ zip code in order to send them their letters.
    Ask the client for their zip code and console.log “success” or “error” based on the following rules.
        Zip codes consists of 5 numbers
        Must only contain numbers
        Must not contain any whitespace (spaces)
        Must not be greater than 5 digits in length
*/

// Without regular expressions
console.log("Outcome without regular expression:");
let zipCode = prompt("Please enter your ZIP code (5 digits expected): ");
let success = true;
if (isNaN(zipCode)) {
    success = false;
    console.log(zipCode + " is not a number.");
};
if (zipCode.length !== 5) {
    success = false;
    console.log(zipCode + " does not have 5 digits.");
};
if (success) {
    console.log("success");
} else {
    console.log("error");
};

// With regular expressions
console.log("Outcome with regular expression:");
let isOK = true;
var patt1 = /[^1-9]/g;
var result = zipCode.match(patt1);
if (result > 0) {
    isOK = false;
    console.log(zipCode + " is not a number.");
};
if (zipCode.length !== 5) {
    isOK = false;
    console.log(zipCode + " does not have 5 digits.");
};
if (isOK) {
    console.log("success");
} else {
    console.log("error");
};