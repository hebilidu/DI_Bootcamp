/* Week 02 Day 1 - XP Ninja - Part 1 Finding Nemo */
let phrase = prompt('Enter a phrase with \"Nemo\" inside:');
pos = phrase.indexOf("Nemo");
if (pos == -1) {
    console.log("I can’t find Nemo")
} else {
    console.log("I found Nemo at position", phrase.search("Nemo"));
    // console.log("I found Nemo at position", phrase.indexOf("Nemo"));
}

/* Week 02 Day 1 - XP Ninja - Part 2 Evaluation 1 */
console.log(5 >= 1); // true
console.log(0 === 1); // false
console.log(4 <= 1); // false
console.log(1 != 1); // false
console.log("A" > "B"); // false
console.log("B" < "C"); // true
console.log("a" > "A"); // true
console.log("b" < "A"); // false
console.log(true === false); // false
console.log(true != true); // false

/* Week 02 Day 1 - XP Ninja - Part 3 Evaluation 2 */
let c;
console.log(c); // undefined
let a = 34;
console.log(a); // 34
let b = 21;
console.log(b); // 21
a = 2;
console.log(a); // 2
console.log(typeof([1, 2, 3])); // object
console.log(a + b); // 23
console.log((3 + 4 + "5")); // 12 -> "75"
console.log(typeof(3 + 4 + "5"));

/* Week 02 Day 1 - XP Ninja - Part 4 Ask For Numbers */
outSum = 0;
listNb = prompt("Enter a list of numbers :");
let len = listNb.length;
console.log(typeof(listNb), len)
var ind = 0
if (len > 0) {
    do {
        outSum += parseInt(listNb[ind]);
        ind++;
    }
    while (ind < listNb.length)
};
console.log("Somme des elements de la liste =", outSum);