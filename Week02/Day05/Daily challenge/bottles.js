console.log("****** Week 02 Day 05 - Daily challenge: 99bottles ******");
/*
Have you heard the infamous song “99 Bottles of Beer?”
In ths exercise you need to console.log the lyrics to the song 99 Bottles of Beer as an output.
    Prompt the user for a number to begin counting down bottles.
    In the song everytime a bottle falls we subtract the bottles by 1.
        What your code should do is:
            instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
            For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.
Take a look below for more help.
==============================
99 bottles of beer on the wall
99 bottles of beer
Take 1 down, pass it around
98 bottles of beer on the wall
98 bottles of beer on the wall
98 bottles of beer
Take 2 down, pass them around
96 bottles of beer on the wall
96 bottles of beer on the wall
96 bottles of beer
Take 3 down, pass them around
93 bottles of beer on the wall
==============================
How will you choose to make the song end?
Make sure you get the grammar correct.
    For 1 bottle, you pass “it” around.
    For more than one bottle, you pass “them” around.

*/
while (true) {
    nb = +prompt("Please enter number of bottles : ");
    if (!(isNaN(nb) || nb < 1)) { break };
};
let nb_left = nb;
counter = 1;
while (nb_left > 0) {
    bot = " bottles";
    if (nb_left === 1) { bot = " bottle" };
    console.log(nb_left + bot + " of beer on the wall");
    console.log(nb_left + bot + " of beer");
    console.log("Take ", counter, "down, pass it around");
    nb_left -= counter;
    counter++;
};