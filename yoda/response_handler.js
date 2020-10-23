// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function respond() {
    // Your Code Here
    console.log("Hello World!");
    var txtbxtxt = document.getElementById("myInput").value;
    console.log(txtbxtxt);

    var isbaby;
    var pic = "img/";
    var qtype = "std";

    if (txtbxtxt.includes("cute") || txtbxtxt.includes("baby")){
    	isbaby = true;
    	pic += names[0] + "-";
    }else{
    	isbaby = false;
    	pic += names[1] + "-";
    }

    if (txtbxtxt.includes("force") && txtbxtxt.includes("dark")){
    	qtype = moods[0];
    	pic += qtype + ".jpg";
    }else if (txtbxtxt.includes("force")){
    	qtype = moods[1];
    	pic += qtype + ".jpg";
    }else{
    	qtype = moods[2];
    	pic += qtype + ".jpg";;
    }

   	document.getElementById("pic").setAttribute("src", pic);
    document.getElementById("response").innerHTML = getRandomResponse(isbaby, qtype);
    document.getElementById("myInput").value = "";

}

function getRandomResponse(isbaby, qtype){
	var res;
	if (isbaby == true){
		m = "m";
		res = "h" + m.repeat(Math.floor((Math.random() * 20) + 1));
	}else{
		var index = Math.floor((Math.random() * 5));
		if (qtype == moods[0]){
			res = dark_quotes[index];
		}else if (qtype == moods[1]){
			res = force_quotes[index];
		}else{
			res = std_quotes[index];
		}
	}
	return res;
}