console.log("****** Week03 Day03 - DOM Animations - Daily challenge : Show only the letters ******");

let newInput = document.getElementById('input1');

newInput.addEventListener("input", changeInput);

let cleanString = '';

function changeInput(event) {
    let lastChar = event.target.value.slice(-1);
    if (isAlpha(lastChar)) { cleanString += lastChar; }
    document.getElementById('result1').textContent = cleanString;
}

function isAlpha(char) {
    var code = char.charCodeAt(0);
    if (!(code > 64 && code < 91) && // upper alpha (A-Z)
        !(code > 96 && code < 123)) { // lower alpha (a-z)
        return false;
    } else { return true; };
};