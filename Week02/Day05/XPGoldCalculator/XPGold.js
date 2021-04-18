/* *********************************************************************************** */
console.log("\n****** Week02 Day05 - JS: Mini project - XP Gold : Calculator ******");

let mem1 = 0;
let mem2 = 0;
let txt1 = "0";
let txt2 = "0";
let statuses = { 0: "Entering 1st operand", 1: "+", 2: "-", 3: "*", 4: "/", 5: "=" };
let status = 0;

function addVal(txt) {
    document.getElementById('display').value = txt;
}

function number(n) {
    if (status === "=") { reset(); };
    if (status === 0) {
        if (n === '.') { txt1 += n; } else { txt1 = Number(txt1 += n).toString(); };
        addVal(txt1);
    } else {
        if (n === '.') { txt2 += n; } else { txt2 = Number(txt2 += n).toString(); };
        addVal(txt2);
    };
}

function operator(op) {
    if (status === 0) {
        status = op;
    }
}

function equal() {
    let result = 0;
    switch (status) {
        case "+":
            result = Number(txt1) + Number(txt2);
            break;
        case "-":
            result = Number(txt1) - Number(txt2);
            break;
        case "*":
            result = Number(txt1) + Number(txt2);
            break;
        case "/":
            result = Number(txt1) / Number(txt2);
            break;
    }
    status = "=";
    txt1 = result.toString();
    addVal(txt1);
}

function clar() {
    if (status === 0) { txt1 = "0"; } else { txt2 = "0"; };
    addVal("0");
};

function reset() {
    txt1 = "0";
    txt2 = "0";
    status = 0;
    addVal("0");
};