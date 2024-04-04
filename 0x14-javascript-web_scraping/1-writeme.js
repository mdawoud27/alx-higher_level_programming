#!/usr/bin/node

const filepath = process.argv[2];
const str = process.argv[3];
const fs = require("fs");

fs.open(filepath, 'w', (err) => {
  if (err) throw err;
  fs.writeFile(filepath, str, (err) => {
    if (err) throw err;
  });
});
