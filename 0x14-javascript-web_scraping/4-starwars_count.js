#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/people/18', (err, res, body) => {
  if (err) throw err;
  const bodyObj = JSON.parse(body);
  console.log(bodyObj.films.length);
//   console.log(body.split('/people/18/'.length - 1));
});
