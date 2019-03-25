function onload() {
    document.getElementsByClassName('curtain')[0].style.display = 'block';
    document.getElementsByClassName('welcome')[0].classList.add('welcome-animate');
    setTimeout(execute, 3000);
}

function myFunction() {
    var x = document.getElementById("hright");
    if ((x.className === "header header-animate") || x.className === "header") {
        x.className += " responsive";
    } else {
        x.className = "header";
    }
}

function execute() {
    document.getElementsByClassName('curtain')[0].style.display = 'none';
    window.location.href = "home";
}