#!/usr/bin/node

const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');

request.get(url, (err, req, body) => {
  fs.open(filePath, 'w', (err) => {
    if (err) throw err;
    fs.writeFile(filePath, body, (err) => {
      if (err) throw err;
    });
  });
});
