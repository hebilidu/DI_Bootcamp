// Week 02 Day 03 - Daily challenge: Stars
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops 
// (Nested means one inside the other - check out “nested for loops” on Google).
// Do this Daily Challenge by youself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *
// Single loop solution :
let str1 = "*";
for (let i = 0; i < 6; i++) {
    console.log(str1);
    str1 += "*";
};
// Nested loops solution :
let str2 = "*";
for (let i = 0; i < 6; i++) {
    let str2 = "";
    for (j = 0; j < i + 1; j++) {
        str2 += "*";
    }
    console.log(str2);
}