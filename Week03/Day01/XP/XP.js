console.log("\n****** Week03 Day 01 - XP Exercice 1 : Change the navbar ******");

// Change id
let elem = document.getElementById("navBar");
document.getElementById('navBar').setAttribute('id', 'socialNetworkNavigation');

// Create element
const ul = document.getElementsByTagName("ul")[0];
const li = document.createElement("li");

li.innerHTML = '<a href="#">Logout</a>';
ul.appendChild(li);
// Show text element content
const firstChild = ul.firstElementChild.textContent;
const lastChild = ul.lastElementChild.textContent;
console.log("Text of first line item = " + firstChild);
console.log("Text of last line item = " + lastChild);

/* **************************************************************************** */
console.log("\n****** Week03 Day 01 - XP Exercice 2 : Users ******");

// Change Pete to Richard
var items = document.getElementsByTagName('li');

for (i = 0; i < items.length; i++) {
    if (items[i].innerText === "Pete") { items[i].innerText = "Richard" };
    if (items[i].innerText === "Sarah") { items[i].parentNode.removeChild(items[i]) };
};

// Change content of first li of each ul
var uls = document.getElementsByClassName('list');
const addli = document.createElement("li");
addli.innerText = "Hey students";

for (i = 0; i < uls.length; i++) {
    uls[i].firstElementChild.innerText = "Liên";
    let addli = document.createElement("li");
    addli.innerText = "Hey students";
    uls[i].appendChild(addli);
};

/* **************************************************************************** */
console.log("\n****** Week03 Day 01 - XP Exercice 3 : Users and style ******");
const divex3 = document.getElementById('ex3');
divex3.style.backgroundColor = "lightblue";
divex3.style.padding = "20px";

const ulex3 = document.getElementById('ulex3');
ulex3.firstElementChild.style.display = "none";
ulex3.lastElementChild.style.border = "3px solid";
document.body.style.fontSize = "x-large";