// You Can Pick :: Christopher Liu, Renggeng Zheng
// SoftDev pd1
// K32 -- DVD Screensaver
// 2022-02-17r

// access canvas and buttons via DOM
let c = document.getElementById("playground");
let dotButton = document.getElementById("buttonCircle");
let dvdButton = document.getElementById("buttonDvd");
let stopButton = document.getElementById("buttonStop");

// prepare to interact with canvas in 2D
let ctx = c.getContext("2d");

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
  ctx.arc(c.clientWidth / 2, c.clientHeight / 2, radius, 0, 360);
  ctx.fillStyle = "purple";
  ctx.fill();

  if (radius >= c.clientWidth / 2) {
    growing = false;
  } else if (radius <= 0) {
    growing = true;
  }

  requestID = window.requestAnimationFrame(drawDot);
};


// set up image eleemnt
let img = new Image(60, 40);
img.src = "logo_dvd.png";

// initialize x and y position and velocity variables
let x = Math.floor(Math.random() * (c.width - img.width));
let y = Math.floor(Math.random() * (c.height - img.height));
let xVelo = -1;
let yVelo = Math.PI;
let hue = 90;

let drawDvd = () => {
  console.log("screensaving");
  requestID = window.cancelAnimationFrame(requestID);
  clear();

  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, c.width, c.height);

  ctx.beginPath();
  ctx.filter = `invert() saturate(50%) hue-rotate(${hue}deg)`;
  ctx.drawImage(img, x, y, img.width, img.height);
  ctx.filter = "none";

  if (x <= 0 || x >= c.width - img.width) {
    xVelo = -1 * xVelo;
    hue += 45;
    hue %= 360;
  }

  if (y <= 0 || y >= c.height - img.height) {
    yVelo = -1 * yVelo;
    hue += 45;
    hue %= 360;
  }

  x += xVelo;
  y += yVelo;

  requestID = window.requestAnimationFrame(drawDvd);
}


let stopIt = () => {
  console.log("stopIt invoked...")
  console.log(requestID);
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", () => {
  x = Math.floor(Math.random() * (c.width - img.width));
  y = Math.floor(Math.random() * (c.height - img.height));
  drawDvd();
});
stopButton.addEventListener("click", stopIt);
