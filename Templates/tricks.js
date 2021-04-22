// 1. isAlphanumeric
// 2. isNum_isAlpha
// 3. getRandomColor

function isAlphaNumeric(str) {
    var code, i, len;

    for (i = 0, len = str.length; i < len; i++) {
        code = str.charCodeAt(i);
        if (!(code > 47 && code < 58) && // numeric (0-9)
            !(code > 64 && code < 91) && // upper alpha (A-Z)
            !(code > 96 && code < 123)) { // lower alpha (a-z)
            return false;
        }
    }
    return true;
};

function isNum_isAlpha(str) {
    var code, i, len;
    var isNumeric = false,
        isAlpha = false; // I assume that it is all non-alphanumeric

    for (i = 0, len = str.length; i < len; i++) {
        code = str.charCodeAt(i);

        switch (true) {
            case code > 47 && code < 58: // check if 0-9
                isNumeric = true;
                break;

            case (code > 64 && code < 91) || (code > 96 && code < 123): // check if A-Z or a-z
                isAlpha = true;
                break;

            default:
                // not 0-9, not A-Z or a-z
                return false; // stop function with false result, no more checks
        }
    }

    return isNumeric && isAlpha; // return the loop results, if both are true, the string is certainly alphanumeric
}

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}