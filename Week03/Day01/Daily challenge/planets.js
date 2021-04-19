console.log("****** Week03 Day01 - Daily challenge: Planets ******");
/*
 */
planetList = [
    ["Mercury", 0],
    ["Venus", 0],
    ["Earth", 1],
    ["Mars", 2],
    ["Jupiter", 67],
    ["Saturn", 62],
    ["Uranus", 27],
    ["Neptune", 14],
];
// Create div for each planet
for (i in planetList) {
    let planetdiv = document.createElement('div');
    planetdiv.classList.add("planet", planetList[i][0]);
    let urlimage = "url('./media/" + planetList[i][0] + ".png')";
    planetdiv.style.backgroundImage = urlimage;
    planetdiv.style.backgroundSize = "contain";
    planetdiv.style.backgroundRepeat = "no-repeat";
    document.getElementsByTagName('section')[0].appendChild(planetdiv);
};