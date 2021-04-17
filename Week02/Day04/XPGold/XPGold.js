/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Gold Exercise 1 : is_Blank ******");
/*
Write a program to check whether a string is blank or not.
console.log(is_Blank('')); --> true
console.log(is_Blank('abc')); --> false
*/
function is_Blank(txt) { if (txt === "") { return true } else { return false }; }
console.log(is_Blank(''));
console.log(is_Blank('abc'));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Gold Exercise 2 : Abbrev_name ******");
/*
Write a JavaScript function to convert a string into an abbreviated form.
console.log(abbrev_name("Robin Singh")); --> "Robin S."
*/
function abbrev_name(fullName) {
    output = "";
    for (let i = 0; i < fullName.length; i++) {
        if (fullName[i] === " ") {
            output += fullName[i] + fullName[i + 1] + ".";
            break;
        } else {
            output += fullName[i];
        }
    };
    return output;
}
console.log(abbrev_name("Robin Singh"));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Gold Exercise 3 : SwapCase ******");
/*
Write a JavaScript function which takes a string as an argument and swaps the case of each character.
For example :
if you input 'The Quick Brown Fox' 
the output should be 'tHE qUICK bROWN fOX'.
*/
function swap(txt) {
    let output = "";
    for (l of txt) { if (l === l.toUpperCase()) { output += l.toLowerCase() } else { output += l.toUpperCase() }; };
    return output;
}
console.log(swap('The Quick Brown Fox'));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Gold Exercise 4 : Omnipresent value ******");
/*
Create a function that determines whether an argument is omnipresent for a given array.
A value is omnipresent if it exists in every subarray inside the main array.
To illustrate:
[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// 3 exists in every element inside this array, so is omnipresent.
Examples
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false
*/
function isOmnipresent(arr, ref) {
    isIt = true;
    for (i of arr) {
        if (!i.includes(ref)) {
            isIt = false;
            break;
        }
    }
    return isIt;
}
console.log(isOmnipresent([
    [1, 1],
    [1, 3],
    [5, 1],
    [6, 1]
], 1));
console.log(isOmnipresent([
    [1, 1],
    [1, 3],
    [5, 1],
    [6, 1]
], 6));