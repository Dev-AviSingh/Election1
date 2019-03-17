function changestateactive(item){
	item.style.backgroundColor = "yellow";
}
function changestateidle(item){
	item.style.backgroundColor = "black";
}
box1 = false;
box2 = false;
box3 = false;
box4 = false;

box5 = false;
box6 = false;
box7 = false;
box8 = false;

box9 = false;
box10 = false;
box11 = false;
box12 = false;

function setrow1(item, name){
	switch(name){
		case "box1":
		changestateactive(item);
		changestateidle(document.getElementById("box2"));
		changestateidle(document.getElementById("box3"));
		changestateidle(document.getElementById("box4"));
		box1 = true;
		box2 = false;
		box3 = false;
		box4 = false;
		break;
		case "box2":
		changestateactive(item);
		changestateidle(document.getElementById("box1"));
		changestateidle(document.getElementById("box3"));
		changestateidle(document.getElementById("box4"));
		box1 = false;
		box2 = true;
		box3 = false;
		box4 = false;
		break;
		case "box3":
		changestateactive(item);
		changestateidle(document.getElementById("box2"));
		changestateidle(document.getElementById("box1"));
		changestateidle(document.getElementById("box4"));
		box1 = false;
		box2 = false;
		box3 = true;
		box4 = false;
		break;
		case "box4":
		changestateactive(item);
		changestateidle(document.getElementById("box2"));
		changestateidle(document.getElementById("box3"));
		changestateidle(document.getElementById("box1"));
		box1 = false;
		box2 = false;
		box3 = false;
		box4 = true;
		break;
		default:break;
	}
}
function setrow2(item, name){
	switch(name){
		case "box5":
		changestateactive(item);
		changestateidle(document.getElementById("box6"));
		changestateidle(document.getElementById("box7"));
		changestateidle(document.getElementById("box8"));
		box5 = true;
		box6 = false;
		box7 = false;
		box8 = false;
		break;
		case "box6":
		changestateactive(item);
		changestateidle(document.getElementById("box5"));
		changestateidle(document.getElementById("box7"));
		changestateidle(document.getElementById("box8"));
		box5 = false;
		box6 = true;
		box7 = false;
		box8 = false;
		break;
		case "box7":
		changestateactive(item);
		changestateidle(document.getElementById("box6"));
		changestateidle(document.getElementById("box5"));
		changestateidle(document.getElementById("box8"));
		box5 = false;
		box6 = false;
		box7 = true;
		box8 = false;
		break;
		case "box8":
		changestateactive(item);
		changestateidle(document.getElementById("box6"));
		changestateidle(document.getElementById("box7"));
		changestateidle(document.getElementById("box5"));
		box5 = false;
		box6 = false;
		box7 = false;
		box8 = true;
		break;
		default:break;
	}
}
function setrow3(item, name){
	switch(name){
		case "box9":
		changestateactive(item);
		changestateidle(document.getElementById("box10"));
		changestateidle(document.getElementById("box11"));
		changestateidle(document.getElementById("box12"));
		box9 = true;
		box10 = false;
		box11 = false;
		box12 = false;
		break;
		case "box10":
		changestateactive(item);
		changestateidle(document.getElementById("box9"));
		changestateidle(document.getElementById("box11"));
		changestateidle(document.getElementById("box12"));
		box9 = false;
		box10 = true;
		box11 = false;
		box12 = false;
		break;
		case "box11":
		changestateactive(item);
		changestateidle(document.getElementById("box10"));
		changestateidle(document.getElementById("box9"));
		changestateidle(document.getElementById("box12"));
		box9 = false;
		box10 = false;
		box11 = true;
		box12 = false;
		break;
		case "box12":
		changestateactive(item);
		changestateidle(document.getElementById("box10"));
		changestateidle(document.getElementById("box11"));
		changestateidle(document.getElementById("box9"));
		box9 = false;
		box10 = false;
		box11 = false;
		box12 = true;
		break;
		default:break;
	}
}

function setactive(item, name){
	if (name == "box1" || name == "box2" || name == "box3" || name == "box4"){
		setrow1(item, name);
	}
	else if (name == "box5" || name == "box6" || name == "box7" || name == "box8"){
		setrow2(item, name);
	}
	else{
		setrow3(item, name);
	}
}

cand1 = 0;
cand2 = 0;
cand3 = 0;
cand4 = 0;
cand5 = 0;
cand6 = 0;
cand7 = 0;
cand8 = 0;
cand9 = 0;
cand10 = 0;
cand11 = 0;
cand12 = 0;

function submit(){
	document.getElementById("box1").style.backgroundColor = "black";
	document.getElementById("box2").style.backgroundColor = "black";
	document.getElementById("box3").style.backgroundColor = "black";
	document.getElementById("box4").style.backgroundColor = "black";
	document.getElementById("box5").style.backgroundColor = "black";
	document.getElementById("box6").style.backgroundColor = "black";
	document.getElementById("box7").style.backgroundColor = "black";
	document.getElementById("box8").style.backgroundColor = "black";
	document.getElementById("box9").style.backgroundColor = "black";
	document.getElementById("box10").style.backgroundColor = "black";
	document.getElementById("box11").style.backgroundColor = "black";
	document.getElementById("box12").style.backgroundColor = "black";
	if(box1 == true){
		cand1 += 1;
	}
	if(box2 == true){
		cand2 += 1;
	}
	if(box3 == true){
		cand3 += 1;
	}
	if(box4 == true){
		cand4 += 1;
	}
	if(box5 == true){
		cand5 += 1;
	}
	if(box6 == true){
		cand6 += 1;
	}
	if(box7 == true){
		cand7 += 1;
	}
	if(box8 == true){
		cand8 += 1;
	}
	if(box9 == true){
		cand9 += 1;
	}
	if(box10 == true){
		cand10 += 1;
	}
	if(box11 == true){
		cand11 += 1;
	}
	if(box12 == true){
		cand12 += 1;
	}
	else{
		console.log("none");	
	}
	box1 = false;
	box2 = false;
	box3 = false;
	box4 = false;
	box5 = false;
	box6 = false;
	box7 = false;
	box8 = false;
	box9 = false;
	box10 = false;
	box11 = false;
	box12 = false;
	console.log(cand1 + " ," + cand2 + " ," + cand3 + " ," + cand4 + " ," + cand5 + " ," + cand6 + " ," + cand7 + " ," + cand8 + " ," + cand9 + " ," + cand10 + " ," + cand11 + " ," + cand12);
	nextroll();
}
var rollno  = 1;
function nextroll(){
	rollno++;
	document.getElementById("roll").innerHTML = rollno;
}
function setvalue(val){
	if (val < 10){
		return "00" + val;
	}
	else if( val < 100 && val >= 10){
		return "0" + val
	}
	else{
		return val
	}
	
}

function submittoserver(){
	var final_string; 
	cand1 = setvalue(cand1);
	cand2 = setvalue(cand2);
	cand3 = setvalue(cand3);
	cand4 = setvalue(cand4);
	cand5 = setvalue(cand5);
	cand6 = setvalue(cand6);
	cand7 = setvalue(cand7);
	cand8 = setvalue(cand8);
	cand9 = setvalue(cand9);
	cand10 = setvalue(cand10);
	cand11 = setvalue(cand11);
	cand12 = setvalue(cand12);
	
	final_string = cand1 + " ," + cand2 + " ," + cand3 + " ," + cand4 + " ," + cand5 + " ," + cand6 + " ," + cand7 + " ," + cand8 + " ," + cand9 + " ," + cand10 + " ," + cand11 + " ," + cand12;
	
	console.log(final_string);
	var xhttp = new XMLHttpRequest();
	xhttp.open("GET", "submit/" + final_string, true)
	xhttp.send()
	cand1 = 0;
	cand2 = 0;
	cand3 = 0;
	cand4 = 0;
	cand5 = 0;
	cand6 = 0;
	cand7 = 0;
	cand8 = 0;
	cand9 = 0;
	cand10 = 0;
	cand11 = 0;
	cand12 = 0;
}