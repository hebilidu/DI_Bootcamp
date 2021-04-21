console.log("\n****** Week03 Day03 - JS DOM Animations - XP Exercise 2: Drag & Drop ******");

function dropHere(ev) {
    ev.preventDefault();
}

function dragStart(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}