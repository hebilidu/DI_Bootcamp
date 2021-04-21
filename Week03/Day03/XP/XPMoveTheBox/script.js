console.log("\n****** Week03 Day03 - JS DOM Animations - XP Exercise 1 : Move The Box ******");

let container = document.getElementById("container");
container.style.position = "absolute";
const containerWidth = container.clientWidth;

let box = document.getElementById("animate");
box.style.position = 'relative';
const boxWidth = box.clientWidth;

let isMoving = false;
let step = 3;

function myMove() {
    console.log("isMoving =", isMoving);
    if (!isMoving) {
        var myTimer = setInterval(calcMove, 15);
    } else {
        clearInterval(myTimer);
        box.style.left = "0px";
    }
    isMoving = !isMoving;
}

function calcMove() {
    let posx = box.offsetLeft;
    if (posx >= (containerWidth - boxWidth) || posx < 0) { step = -step; };
    box.style.left = (posx + step).toString() + 'px';
}