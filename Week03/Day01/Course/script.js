alert(`Week03 Day01 - Course notes`);

// let div = document.getElementById('first_div');

// let my_h2 = document.createElement('h2');
// my_h2.innerHTML = "Hello I am Daniel";
// div.appendChild(my_h2);

// console.log("Test");

// 1 
let divnodes = document.getElementsByTagName('div');
console.log(divnodes);
// 1 alternative
let divnodes2 = document.querySelector('#container');

// 2
let ulnodes = document.getElementsByTagName('ul');
console.log(ulnodes);

console.log(ulnodes[0].children[0].innerText);
console.log(ulnodes[0].children[1].innerText);
console.log(ulnodes[1].children[0].innerText);
console.log(ulnodes[1].children[1].innerText);

for (i = 0; i < ulnodes.length; i++) {
    console.log("ulnodes[" + i + "] = ", ulnodes[i]);

    for (j = 0; j < ulnodes[i].length; j++) {
        console.log(i, j);
        console.log(ulnodes[i].children[j].innerText);
    };
};
// 3

let list0 = document.getElementsByClassName('list')[0];
let list1 = document.getElementsByClassName('list')[1];
console.table([list0.textContent, list1.textContent]);