#!/usr/bin/node

const filePath = process.argv[2];
const fs = require('fs');

fs.open(filePath, 'r', (err, file) => {
  if (err) throw err;
  fs.readFile(filePath, (err, data) => {
    if (err) throw err;
    console.log(data.toString());
  });
});
