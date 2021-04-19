console.log("****** Week03 Day01 - Daily challenge: Planets ******");
/*
 */
/* Get the documentElement (<html>) to display the page in fullscreen */
var elem = document.documentElement;
var fullscreen = false;

/* View in fullscreen */
function openFullscreen() {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
}

/* Close fullscreen */
function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
    }
}

function toggle() {
    if (fullscreen) { closeFullscreen() } else { openFullscreen() };
    fullscreen = !fullscreen;
}

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
    let setdiv = document.createElement('div');
    setdiv.classList.add("set");
    document.getElementsByTagName('section')[0].appendChild(setdiv);

    let planetdiv = document.createElement('div');
    planetdiv.classList.add("planet", planetList[i][0]);
    let urlimage = "url('./media/" + planetList[i][0] + ".png')";
    planetdiv.style.backgroundImage = urlimage;
    planetdiv.style.backgroundSize = "contain";
    planetdiv.style.backgroundRepeat = "no-repeat";
    setdiv.appendChild(planetdiv);

    for (j = 0; j < planetList[i][1]; j++) {
        let moondiv = document.createElement('div');
        moondiv.classList.add("moon");
        setdiv.appendChild(moondiv);
    };
};

// for (i in planetList) {
//     let planetdiv = document.createElement('div');
//     planetdiv.classList.add("planet", planetList[i][0]);
//     let urlimage = "url('./media/" + planetList[i][0] + ".png')";
//     planetdiv.style.backgroundImage = urlimage;
//     planetdiv.style.backgroundSize = "contain";
//     planetdiv.style.backgroundRepeat = "no-repeat";
//     document.getElementsByTagName('section')[0].appendChild(planetdiv);
// };