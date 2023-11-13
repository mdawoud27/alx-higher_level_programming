#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const argv = process.argv;
const result = add(Number(argv[2]), Number(argv[3]));
console.log(result);
