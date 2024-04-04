#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
let cnt = 0;

request.get(url, (err, res, body) => {
  if (err) throw err;
  // console.log(JSON.parse(body).results);
  for (const res of JSON.parse(body).results) {
    for (const ll of res.characters) {
      if (ll.endsWith('/18/')) cnt++;
    }
  }
  console.log(cnt);
});
