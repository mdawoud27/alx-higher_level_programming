#!/usr/bin/node

const argv = process.argv;
const array = [];

for (const i of argv) {
  if (!isNaN(i)) {
    array.push(Number(i));
  }
}

if (array.length <= 1) {
  console.log(0);
} else {
  array.sort().reverse();
  // console.log(array);
  console.log(array[1]);
}
