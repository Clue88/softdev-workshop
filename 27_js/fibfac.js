// Team PurplePotatoes2: Christopher Liu, Deven Maheshwari
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


// Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

let fac = n => ((n <= 1) ? 1 : (n * fac(n - 1)))

let fib = n => ((n <= 1) ? n : (fib(n - 1) + fib(n - 2)))


function fac2(n) {
    if (n <= 1) return 1;
    return n * fac2(n - 1);
}

function fib2(n) {
    if (n <= 1) return n;
    return (fib2(n - 1) + fib2(n - 2))
}
