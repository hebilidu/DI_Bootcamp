/* Week 02 Day 1 - XP Gold - Part 1 Favorite color */
let me = ["my", "favorite", "color", "is", "blue"];
console.log(me.join("_"));
console.log(me.join(".."));

/* Week 02 Day 1 - XP Gold - Part 2 Mixup */
let str1 = "mix";
let str2 = "pod";
int1 = str1.substr(0, 2);
int2 = str2.substr(0, 2);
str3 = str1 + " " + str2;
console.log("BEFORE: ", str1, str2);
str1 = int2 + str1.substr(2, 1);
str2 = int1 + str2.substr(2, 1);
console.log("AFTER: ", str1, str2);
console.log("Concatenation: \"" + str3 + "\"");

/* Week 02 Day 1 - XP Gold - Part 3 Calculator */
let num1 = prompt('Enter number 1');
let num2 = prompt('Enter number 2');
alert(`${num1} + ${num2} = ${parseInt(num1) + parseInt(num2)}\r\n${num1} - ${num2} = ${parseInt(num1) - parseInt(num2)}\r\n${num1} * ${num2} = ${parseInt(num1) * parseInt(num2)}\r\n${num1} / ${num2} = ${parseInt(num1) / parseInt(num2)}`);

let num3 = prompt('Enter number 3');
let num4 = prompt('Enter number 4');
let op = prompt('Choose an operation', '+, -, * or /');
if (op == "+") {
    alert(`${num3} ${op} ${num4} = ${parseInt(num3) + parseInt(num4)}`);
} else if (op == "-") {
    alert(`${num3} ${op} ${num4} = ${parseInt(num3) - parseInt(num4)}`);
} else if (op == "*") {
    alert(`${num3} ${op} ${num4} = ${parseInt(num3) * parseInt(num4)}`);
} else {
    alert(`${num3} ${op} ${num4} = ${parseInt(num3) / parseInt(num4)}`);
}