var sentence = prompt("Please enter a sentence including the \"not \" and \"bad \" terms:");
// What happens when not or bad is a part of another word ?
// Shoud verify that they are standalone words...
wordNot = sentence.search("not");
console.log(wordNot);
wordBad = sentence.search("bad");
console.log(wordBad);

var newSentence = sentence;

if (wordNot < wordBad && wordNot > 0) {
    var chunk = sentence.slice(wordNot, wordBad + 3);
    console.log(chunk);

    // To replace not...bad with good, not has to disappear and good replaces bad
    newSentence = sentence.replace(chunk, "good");
}

console.log("Your string is : \'" + sentence + "\'");
console.log("--> the result is : \'" + newSentence + "\'");