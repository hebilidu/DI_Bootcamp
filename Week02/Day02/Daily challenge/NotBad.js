// Use RegEx to check that "not" and "bad" are standalone words
var sentence = prompt("Please enter a sentence including the \"not \" and \"bad \" terms:");
wordNot = sentence.search(/\bnot\b/);
wordBad = sentence.search(/\bbad\b/);

var newSentence = sentence;
if (wordNot < wordBad && wordNot > -1) {
    var chunk = sentence.slice(wordNot, wordBad + 3);
    newSentence = sentence.replace(chunk, "good");
};

console.log("Your string is : \'" + sentence + "\'");
console.log("--> the result is : \'" + newSentence + "\'");