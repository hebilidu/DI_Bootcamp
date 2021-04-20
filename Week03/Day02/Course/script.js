// Week03 Day02 - Course - Exercise 1
function insert_Row() {
    newRow = document.createElement('tr');
    newCell1 = document.createElement('td');
    newCell2 = document.createElement('td');
    table = document.getElementById('sampleTable');
    nbRows = table.children[0].children.length;
    newCell1.innerText = "Row " + (nbRows + 1) + " col 1";
    newCell2.innerText = "Row " + (nbRows + 1) + " col 2";
    newRow.appendChild(newCell1);
    newRow.appendChild(newCell2);
    document.getElementsByTagName('tbody')[0].appendChild(newRow);
}

function insert_Col() {
    newCellRow1 = document.createElement('td');
    newCellRow1.innerText = "Cell";
    document.getElementsByTagName('tbody')[0].firstElementChild.appendChild(newCellRow1);
}