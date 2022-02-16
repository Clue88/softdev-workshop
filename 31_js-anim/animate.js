// Team PurplePotatoes2 :: Christopher Liu, Deven Maheshwari
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// access canvas and buttons via DOM
let c = document.getElementById("playground");
let dotButton = document.getElementById("buttonCircle");
let stopButton = document.getElementById("buttonStop");

// prepare to interact with canvas in 2D
let ctx = c.getContext("2d");

// set fill color to team color
ctx.fillStyle = "purple";

let requestID;  // init global let for use with animation frames


let clear = (e) => {
  console.log("clear invoked...");
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
};


let radius = 0;
let growing = true;


let drawDot = () => {
  console.log("drawDot invoked...");

  window.cancelAnimationFrame(requestID);
  clear();

  if (growing) {
    radius += 2;
  } else {
    radius -= 2;
  }
  
  ctx.beginPath();
  ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 360);
  ctx.fill();
  ctx.stroke();
  
  if (radius >= c.clientWidth/2) {
    growing = false;
  } else if (radius <= 0) {
    growing = true;
  }

  requestID = window.requestAnimationFrame(drawDot);
};


let stopIt = () => {
  console.log("stopIt invoked...")
  console.log(requestID);
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
