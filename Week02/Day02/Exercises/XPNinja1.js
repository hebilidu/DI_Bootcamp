// Week 02 Day 2 Ninja 1 : Age difference
let year1 = prompt("Please enter birth year of person 1 (YYYY):");
let year2 = prompt("Please enter birth year of person 2 (YYYY):");
var resultYear = 0;
console.log("Person1 was born in " + year1 + ". Person2 was born in " + year2 + ".")
if (year1 > year2) {
    resultYear = 2 * year1 - year2;
    console.log("In " + resultYear + ", person1 will be half the age of person2");
} else {
    resultYear = 2 * year2 - year1;
    console.log("In " + resultYear + ", person2 will be half the age of person1");
}