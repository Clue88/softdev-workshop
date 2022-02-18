// retrieve node in DOM via ID
let c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
let ctx = c.getContext("2d");

// init global state var
let mode = "rect";

let toggleMode = function (e) {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circle";
        e.target.innerHTML = "circle";
    } else {
        mode = "rect";
        e.target.innerHTML = "rectangle";
    }
}

let drawRect = function (e) {
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    ctx.beginPath();
    ctx.rect(mouseX, mouseY, 75, 150);
    ctx.fillStyle = "red";
    ctx.fill();
}

let drawCircle = function (e) {
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 360);
    ctx.fillStyle = "red";
    ctx.strokeStyle = "black";
    ctx.fill();
    ctx.stroke();
}

let draw = function (e) {
    if (mode === "rect") {
        drawRect(e);
    } else {
        drawCircle(e);
    }
}

let wipeCanvas = function () {
    console.log("wiping canvas...")
    ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
}

c.addEventListener("click", draw);
let bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);;
let clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
