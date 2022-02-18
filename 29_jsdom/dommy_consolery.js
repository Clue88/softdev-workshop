// Team PurplePotatoes :: Christopher Liu, Zhaoyu Lin
// SoftDev pd0
// K29 -- Getting more comfortable with the dev console and the DOM
// 2022-02-09w
// --------------------------------------------------


// send diagnostic output to console
// (Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

let i = "hello";
let j = 20;


// assign an anonymous fxn to a var
let f = function (x) {
  let j = 30;
  return j + x;
};


// instantiate an object
let o = {
  'name': 'Thluffy',
  age: 15,
  items: [10, 20, 30, 40],
  morestuff: { a: 1, b: 'ayo' },
  func: function (x) {
    return x + 30;
  }
};


let addItem = function (text) {
  let list = document.getElementById("thelist");
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


let removeItem = function (n) {
  let listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


let red = function () {
  let items = document.getElementsByTagName("li");
  for (let i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


let stripe = function () {
  let items = document.getElementsByTagName("li");
  for (let i = 0; i < items.length; i++) {
    if (i % 2 == 0) {
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

// insert your implementations here for...
// FIB
function fib(n) {
  let item = document.getElementById("fib");
  item.innerHTML = `fib(${n}) = ${fib2(n)}`
}

function fib2(n) {
  if (n <= 1) return n;
  return (fib2(n - 1) + fib2(n - 2))
}

fib(0);
let fibCount = 0;
function incrementFib() {
  fibCount++;
  fib(fibCount);
}

document.getElementById("fibButton").addEventListener("click", incrementFib);

// FAC
function fac(n) {
  let item = document.getElementById("fac");
  item.innerHTML = `fac(${n}) = ${fac2(n)}`
}

function fac2(n) {
  if (n <= 1) return 1;
  return n * fac2(n - 1);
}

fac(0);
let facCount = 0;
function incrementFac() {
  facCount++;
  fac(facCount);
}

document.getElementById("facButton").addEventListener("click", incrementFac);

// GCD
function gcd(a, b) {
  let item = document.getElementById("gcd");
  item.innerHTML = `gcd(${a}, ${b}) = ${gcd2(a, b)}`
}

function gcd2(a, b) {
  let c = Math.max(a, b);
  let d = Math.min(a, b);

  if (c == 0) return d;
  if (d == 0) return c;
  return gcd2(d, c % d);
}

gcd(4, 6);
document.getElementById("gcdButton").addEventListener("click", () => {
  gcd(
    document.getElementById("gcd1").value,
    document.getElementById("gcd2").value
  );
});
