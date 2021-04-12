let usr1 = { // OBJECT
    username: "toto",
    password: "123quatre",
};

let usr2 = { // OBJECT
    username: "tutu",
    password: "123cinq",
};

let database = [ // ARRAY
    usr1,
    usr2,
];

let newsfeed = [ // ARRAY
    {
        username: "titi",
        timeline: 5,
    },
    {
        username: "tata",
        timeline: 7,
    },
    {
        username: "tutu",
        timeline: 6,
    }
];

console.log(usr1);
console.log(newsfeed[0].username);
console.log(newsfeed[0]["username"]);