console.log("\n****** Week03 Day 01 - XP Exercice 1 : Change the article *******");

// Remove last paragraph of article
lastpara = document.querySelector('article').lastElementChild;
lastpara.parentNode.removeChild(lastpara);

// event-listener to change background color of h2
const bouquet = ['red', 'yellow', 'white', 'pink', 'grey'];
let zoneh2 = document.querySelector('h2');
zoneh2.addEventListener("click", chgbgcolor);

function chgbgcolor() {
    zoneh2.style.backgroundColor = bouquet[Math.floor(Math.random() * bouquet.length)];
}

// event-listener to change h1 font-size
let zoneh1 = document.querySelectorAll('h1')[1];
zoneh1.addEventListener("click", chfontsize);

function chfontsize() {
    zoneh1.style.fontSize = [Math.floor(10 + Math.random() * 90)].toString() + 'px';
}

// event-listener to change hide h3
let zoneh3 = document.querySelector('h3');
zoneh3.addEventListener("click", hide);

function hide() {
    zoneh3.style.display = 'none';
}

// add button to make all paragraph in article bolder
let btn = document.createElement('button');
btn.innerText = 'BOLD';
btn.onclick = boldpara;
document.querySelector('article').appendChild(btn);

function boldpara() {
    let allp = document.querySelectorAll('article > p');
    for (i = 0; i < allp.length; i++) {
        allp[i].style.fontWeight = 900;
    }
}

// Create usersAnswer table header
let tabl = document.createElement('table');
tabl.setAttribute('id', 'tabl');
tabl.style.border = 'solid 2px';
let rowh = document.createElement('tr');
let colh1 = document.createElement('th');
let colh2 = document.createElement('th');
colh1.innerText = 'First name';
colh1.style.border = 'solid 1px';
colh2.innerText = 'Last name';
colh2.style.border = 'solid 1px';
rowh.appendChild(colh1);
rowh.appendChild(colh2);
tabl.appendChild(rowh);
document.getElementsByClassName('usersAnswer')[0].appendChild(tabl);

function addPerson(e) {
    // Solution without form tag
    // let fname = document.getElementById('fname').value;
    // let lname = document.getElementById('lname').value;
    // // Look for empty fields
    // let abort = false;
    // for (item of document.getElementsByTagName('input')) {
    //     if (item.value.length === 0) {
    //         item.style.borderColor = "red";
    //         abort = true;
    //     } else {
    //         item.style.borderColor = "black"
    //     };
    // };
    // if (abort) { return; };

    // Solution with form tag
    e.preventDefault();
    let fname = form.elements[0].value;
    let lname = form.elements[1].value;

    // Add values into userAnswer table
    let row = document.createElement('tr');
    let col1 = document.createElement('td');
    col1.innerText = fname;
    col1.style.border = 'solid 1px';
    let col2 = document.createElement('td');
    col2.innerText = lname;
    col2.style.border = 'solid 1px';
    row.appendChild(col1);
    row.appendChild(col2);
    document.getElementById('tabl').appendChild(row);
}

// Event management
// document.getElementById("submit").addEventListener("click", addPerson);
let form = document.querySelector('form');
form.addEventListener("submit", addPerson)

// Fade animation on second paragraph
document.querySelectorAll('p')[1].classList.add('fade');

/* *************************************************************************** */
console.log("\n****** Week03 Day 01 - XP Exercice 2 : Transform the sentence *******");

function getBold_items() {
    allBold = document.querySelectorAll('strong');
    return allBold;
}

function highlight(element) {
    items = getBold_items();
    for (item of items) {
        item.style.color = 'blue';
    }
}

function return_normal(element) {
    items = getBold_items();
    for (item of items) {
        item.style.color = 'black';
    }
}