/* *********************************************************************************** */
console.log("\n****** Week02 Day 05 - XP Ninja Mini-Project : Hanging Game ******");

/* Player1 provides with word to guess */
function provide() {
    let secretWord = "";
    let len = 0;
    while (true) {
        secretWord = prompt("Hey, Player1, please enter a word (8 letters or more, no spaces, no digits) : ");
        if (secretWord.length > 7) { break; }
    };
    secretWord = secretWord.toLowerCase();
    let secretLetters = secretWord.split("");
    return secretLetters
}

/* Loop to guess secret word */
function guess(array, nbTries) {
    let triedLetters = [];
    let len = array.length;
    nbUncovered = len;
    let uncovered = [];
    for (count = 0; count < len; count++) { uncovered.push("_"); };

    let i = 0;
    while (i < nbTries) {
        let l = "";
        let cont = true;
        while (cont) {
            console.log("Guess : " + uncovered.join(" "));
            l = prompt("Player2, please enter a letter : ");
            if (l.match(/^[A-Za-z]+$/)) {
                l = l.toLowerCase();
                if (triedLetters.includes(l)) {
                    alert("You've already used that letter !");
                } else {
                    triedLetters.push(l);
                    console.log("Used letters so far : ", triedLetters);
                    cont = false;
                };
            };
        };

        found = false;
        for (let j = 0; j < len; j++) {
            if (array[j] === l) {
                found = true
                uncovered[j] = l;
                nbUncovered--;
            };
        };
        if (!found) { i++ }

        if (nbUncovered === 0) {
            alert("Player2 wins !");
            return;
        };
    };
    alert("Player1 wins !");
    return;
};

guess(provide(), 10);