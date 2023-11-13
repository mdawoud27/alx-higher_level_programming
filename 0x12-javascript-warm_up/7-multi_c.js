#!/usr/bin/node

const argv = process.argv;

if (argv.length < 3) {
  console.log('Missing number of occurrences');
} else if (argv.length === 3 && !isNaN(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
