#!/usr/bin/node

function factorial (a) {
  if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

const argv = process.argv;

if (argv[2] && argv[2] > 0) {
  console.log(factorial(argv[2]));
} else if (argv[2] === undefined) {
  console.log(1);
}
