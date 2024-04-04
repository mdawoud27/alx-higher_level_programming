#!/usr/bin/node

const movieID = process.argv[2];

const request = require('request');
request.get(
  `https://swapi-api.alx-tools.com/api/films/${movieID}/`,
  (err, res, body) => {
    if (err) throw err;
    const movie = JSON.parse(body);
    console.log(movie['title']);
  }
);
