#!/usr/bin/node

const argv = process.argv;

if (argv.length < 3 || isNaN(argv[2])) {
  console.log('Missing size');
} else if (argv.length === 3 && !isNaN(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    let sqRow = '';
    for (let j = 0; j < argv[2]; j++) {
      sqRow += 'X';
    }
    console.log(sqRow);
  }
}
