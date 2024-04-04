#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, (err, res, body) => {
  if (err) throw err;
  const count = body.split('/people/18/').length - 1;
  console.log(count);
});
