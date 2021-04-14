console.log("****** Week 02 Day 04 - JS: Functions - Exercise 1 ******");

function calcAgeParents(myAge) {
    let ageMom = 2 * myAge;
    let ageDad = Math.round(1.2 * ageMom);
    return ("I am " + myAge + ". Mom is : " + ageMom + " and Dad is : " + ageDad);
};

while (true) {
    age = +prompt("Enter age (999 to stop):");
    if (age === 999) { break }
    console.log(calcAgeParents(age));
};

function test01() {
    return "Coucou";
};

let test02 = () => {
    return "Coucoucroucoucou"
};

console.log(test01(), test02());
console.log(typeof(test02));
funcstr = test02.toString;
console.log(funcstr);

// Arrow function
const show = x => x * 2;
console.log(show(3)); // 6

const plus = (a, b) => a + b;
const minus = (a, b) => a - b;
const times = (a, b) => a * b;
const divide = (a, b) => Math.round(a / b);

let test03 = (uname, upwd) => [uname, upwd];
let result = test03("Batman", "123Four");
console.log(result);

// Callback function
function opera(a, b, op) {
    let res = op(a, b);
    return res;
};

console.log(opera(5, 7, plus));

// Object method
let person = {
    firstName: "Sarah",
    eye_color: "blue",
    eat: function() {
        console.log("My name is " + this.firstName + ". I love chocolate.");
    }
};
person.eat();