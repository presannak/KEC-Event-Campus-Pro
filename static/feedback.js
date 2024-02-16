window.addEventListener("load", start, false);
function start() {
    document.getElementById("name").addEventListener("focus", focusone, false);
    document.getElementById("name").addEventListener("blur", blurone, false);
    document.getElementById("emailid").addEventListener("focus", focustwo, false);
    document.getElementById("emailid").addEventListener("blur", blurtwo, false);
    document.getElementById("phone").addEventListener("focus", focusthree, false);
    document.getElementById("phone").addEventListener("blur", blurthree, false);
    document.getElementById("myform").addEventListener("submit", submitfun, false);
    document.getElementById("myform").addEventListener("reset", resetfun, false);
    document.getElementById("lastname").addEventListener("focus", focusfour, false);
    document.getElementById("lastname").addEventListener("blur", blurfour, false);
    document.getElementById("text").addEventListener("focus", focusfive, false);
    document.getElementById("text").addEventListener("blur", blurfive, false);
}

function focusone() {
    document.getElementById("help").innerHTML = "Enter first name";
}
function focustwo() {
    document.getElementById("help").innerHTML = "Enter email id";
}
function focusthree() {
    document.getElementById("help").innerHTML = "Enter phone number";
}
function focusfour() {
    document.getElementById("help").innerHTML = "Enter last name";
}
function focusfive() {
    document.getElementById("help").innerHTML = "Enter your feedback message";
}

function blurone() {
    document.getElementById("help").innerHTML = "";
}
function blurtwo() {
    document.getElementById("help").innerHTML = "";
}
function blurthree() {
    document.getElementById("help").innerHTML = "";
}
function blurfour() {
    document.getElementById("help").innerHTML = "";
}
function blurfive() {
    document.getElementById("help").innerHTML = "";
}

function submitfun() {
    window.alert("Are you Sure to submit");
    window.alert("Thank you");
}
function resetfun() {
    window.alert("Are you Sure to reset");
}

function moveone() {
    document.getElementById("move").innerHTML = "Feedback form";
}