/* Week 02 Day 1 - Day challenge - Part 1 */
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
/* 1. Remove banana from array */
console.log("fruits = ", fruits);
let subset = fruits.shift();
console.log("AFTER SHIFT() :");
console.log("subset = ", subset);
console.log("fruits = ", fruits);
/* 2. Sort fruits in alphabetical order */
console.log("fruits = ", fruits);
fruits.sort();
console.log("AFTER SORT() :")
console.log("fruits = ", fruits);
/* 3. Add Kiwi at end of array */
fruits.push("Kiwi");
console.log("AFTER PUSH() :");
console.log("fruits = ", fruits);
/* 4. Remove Apples */
fruits = fruits.slice(1);
console.log("AFTER SLICE() :");
console.log("fruits = ", fruits);
/* 5. Sort array in descending order */
fruits.reverse();
console.log("AFTER REVERSE() :");
console.log("fruits = ", fruits);

/* Week 02 Day 1 - Day challenge - Part 2 */
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log("Here comes the Oranges :")
console.log(moreFruits[1][1][0])