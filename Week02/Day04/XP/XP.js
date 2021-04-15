console.log("\n****** Week02 Day 04 - XP Exercise 1 : Keyless car ******");

function checkDriverAge(age) {
    if (age < 18) {
        alert('Sorry, you are too young to drive this car. Powering off');
    } else if (age === 18) {
        alert('Congratulations on your first year of driving. Enjoy the ride!');
    } else {
        alert('You are old enough to drive, Powering On. Enjoy the ride!');
    };
    return;
};
while (true) {
    do { userAge = +prompt("Please enter your age (999 to exit): "); } while (userAge <= 0 || isNaN(userAge));
    if (userAge === 999) { break; };
    checkDriverAge(userAge);
};

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Exercise 2 : What’s in my wallet ? ******");
Quarters = 0.25;
Dimes = 0.10;
Nickels = 0.05;
Pennies = 0.01;
faceValues = [0.25, 0.10, 0.05, 0.01];

function changeEnough(pocket, cost) {
    let sum = 0;
    for (face in pocket) { sum += faceValues[face] * pocket[face] };
    if (sum >= cost) { return true; } else { return false; };
};
console.log("changeEnough([2, 100, 0, 0], 14.11) -> ", changeEnough([2, 100, 0, 0], 14.11));
console.log("changeEnough([0, 0, 20, 5], 0.75) -> ", changeEnough([0, 0, 20, 5], 0.75));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Exercise 3: Find the multiples of 23 ******");

function genMultiples(base, limit) {
    let sum = 0;
    let outcome = "";
    for (i = 0; i < limit; i += base) {
        outcome += i + " ";
        sum += i;
    };
    return [outcome, sum];
};
while (true) {
    base = +prompt("Please enter a base (default=23)(0 to exit) : ", 23);
    if (base === 0) { break; };
    limit = +prompt("Up to how much do you want to go (default=500) : ", 500);
    result = genMultiples(base, limit);
    console.log("Outcome: ", result[0]);
    console.log("Sum: ", result[1]);
};

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Exercise 4 : Amazon Shopping ******");
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
};

function checkBasket(basket) {
    item = prompt("Enter an item (default=books): ", "books");
    if (basket[item] === undefined) { return false; } else { return true; };
};
if (checkBasket(amazonBasket)) { console.log("Yes it is there"); } else { console.log("Not in here"); };


/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Exercise 5: Shopping List ******");
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};
let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
};
let shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let bill = 0;
    for (item of shoppingList) {
        if (stock[item] > 0) {
            bill += prices[item];
            stock[item] -= 1;
        };
    };
    return bill;
};
console.log("Cart total amount = ", myBill());

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Exercise 6: Tips ******");

function inclTip(num) {
    let perc = 0;
    if (num < 50) { perc = 1.2 } else if (num < 200) { perc = 1.15 } else { perc = 1.1 };
    return (num * perc);
};
console.log("Total including tip = ", Math.round(inclTip(+prompt("John, enter the amount of the bill : "))));

/* *********************************************************************************** */
console.log("\n****** Week02 Day 04 - XP Exercise 7: Vacations Costs ******");
const dests = {
    "London": 183,
    "Paris": 220,
    "other": 300
};

let hotel_cost = (nb) => nb * 140;

function plane_ride_cost(d) {
    if (d in dests) { return dests[d] } else { return dests["other"] };
};

let rental_car_cost = (nb) => nb * 40 * (1 - 0.05 * (nb > 10));

function total_vacation_cost() {
    let nbnights = 0;
    while (!(nbnights > 0)) {
        nbnights = +prompt("How many nights (positive number, please)? ");
    };
    let dest = "";
    while (dest.length === 0) {
        dest = prompt("Destination ? ");
    };
    let nbdays = 0;
    while (!(nbdays > 0)) {
        nbdays = +prompt("How many car rental days ? ");
    };
    let brkdwn = [hotel_cost(nbnights), plane_ride_cost(dest), rental_car_cost(nbdays)];
    let total = brkdwn.reduce((a, b) => a + b, 0);
    return `${nbnights} nights:${brkdwn[0]} + ${dest}:${brkdwn[1]} + ${nbdays} car rental days:${brkdwn[2]} = ${total}`;
};

console.log(total_vacation_cost());