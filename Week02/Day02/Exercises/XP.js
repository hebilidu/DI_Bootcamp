// Exercise 1: Simple if/else statement
var x = 7;
var y = 15;

if (x > y) {
    console.log("x is bigger")
} else {
    console.log("x is not bigger")
};

// Exercise 2: Chihuahua
var newDog = "Chihuahua";
console.log(newDog, "is", newDog.length, "characters long.");
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog === "Chihuahua") {
    console.log("I love Chihuahuas, it’s my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats")
}

// Exercise 3: Even or Odd
var input = +prompt("Enter a number, please:");
if (input % 2 === 0) {
    console.log(input + " is even");
} else if (input % 2 === 1) {
    console.log(input + " is odd");
} else {
    console.log("This is not a number!")
};

// Exercise 4 : Switch Case
function moveCommand(direction) {
    var whatHappens;
    switch (direction) {
        case "forward":
            break;
            whatHappens = "you encounter a monster";
        case "back":
            whatHappens = "you arrived home";
            break;
            break;
        case "right":
            return whatHappens = "you found a river";
            break;
        case "left":
            break;
            whatHappens = "you run into a troll";
            break;
        default:
            whatHappens = "please enter a valid direction";
    }
    return whatHappens;
};
/*
What is the returned value when moveCommand("forward")
What is the returned value when moveCommand("back")
What is the returned value when moveCommand("right")
What is the returned value when moveCommand("left")
*/
console.log(moveCommand("forward")); // undefined
console.log(moveCommand("back")); // "you arrived home"
console.log(moveCommand("right")); // "you found a river"
console.log(moveCommand("left")); // undefined

// Exercise 5: Group Chat
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
var nbConnected = users.length;
switch (nbConnected) {
    case 0:
        console.log("no one is online");
        break;
    case 1:
        console.log(users[0] + " is online");
        break;
    case 2:
        console.log(users[0] + " & " + users[1] + " are online");
        break;
    default:
        console.log(users[0] + " & " + users[1] + " and " + (nbConnected - 2) + " additional users are online");
};