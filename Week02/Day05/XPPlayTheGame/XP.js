console.log("\n****** Week02 Day 05 - XP Ninja Mini Project : Play The Game ******");

function askNumber() {
    while (true) {
        let num = +prompt("Please enter a number between 0 and 10 : ");
        if (isNaN(num)) {
            alert("Sorry Not a number. Try again.");
            continue;
        } else if (num < 0 || num > 10) {
            alert("Sorry it’s not a good number. Try again.");
            continue;
        };
        return num;
    };
}

function playTheGame() {
    let r = confirm("Do you really want to play the game ?");
    if (!r) {
        alert("No problem, Goodbye");
        return;
    };
    // At this stage, user wants to play
    num = askNumber()
    let computerNumber = Math.round(Math.random() * 10);
    console.table({ "num": num, "computerNumber": computerNumber });
    test(num, computerNumber);
    return;
}

function test(userNumber, computerNumber) {
    let nbTries = 0;
    while (true) {
        console.log(nbTries);
        if (userNumber === computerNumber) {
            alert("WINNER");
            return;
        } else if (nbTries > 2) {
            alert(`Out of chances. Number to guess was ${computerNumber}`);
            return
        } else if (userNumber > computerNumber) {
            alert("Your number is bigger than the computer’s, guess again");
            userNumber = askNumber();
        } else {
            alert("Your number is smaller than the computer’s, guess again");
            userNumber = askNumber();
        }
        nbTries++;
    };
}