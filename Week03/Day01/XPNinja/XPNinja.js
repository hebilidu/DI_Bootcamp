/* *********************************************************************************** */
console.log("\n****** Week03 Day01 - XP Ninja Exercise 1 : Calendar ******");
// Prompt for month to be displayed
const regExNum = /^\d+$/;
let inputOK = false;
let year = '2000';
let month = '01';
while (!inputOK) {
    let yearmonth = prompt('Please enter a month in the format yyyymm : ');
    year = +yearmonth.substr(0, 4);
    month = +yearmonth.substr(4, 2);
    if (regExNum.test(month) && month > 0 && month < 13) { inputOK = true };
};

// Get day in the week for 1st of month to be displayed and number of days in month
var day1stOfMonth = new Date(year + '-' + month + '-01').getDay();
var nbDays = new Date(year, month, 0).getDate();

// Prepare table
for (i = 0; i < nbDays; i++) {
    //
};