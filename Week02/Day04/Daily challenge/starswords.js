console.log("****** Week 02 Day 04 - Daily challenge: Words in the Stars ******");

// Get the words
let wordList = [];
while (true) {
    oneWord = prompt("Please enter a word (just hit <enter> when finished):");
    if (oneWord.length === 0) { break };
    wordList.push(oneWord);
};
// Find out the longest words
let longest = 0;
for (item of wordList) {
    if (item.length > longest) { longest = item.length; };
};
// Build each line and send it to console
function buildLine(word, reflen) {
    len = word.length;
    line = "* " + word;
    for (i = 0; i < reflen - len; i++) {
        line += " ";
    };
    line += " *";
    return line;
};
let full = "";
for (i = 0; i < (longest + 4); i++) { full += "*"; };
output = full;
for (item of wordList) { output += "\n" + buildLine(item, longest); };
output += "\n" + full;
console.log(output);