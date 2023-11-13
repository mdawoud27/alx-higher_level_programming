#!/usr/bin/node

const argv = process.argv;
// console.log(argv);
argv.length === 2
  ? console.log('No argument')
  : argv.length === 3
    ? console.log('Argument found')
    : console.log('Arguments found');
