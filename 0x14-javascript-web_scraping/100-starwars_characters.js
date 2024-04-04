#!/usr/bin/node

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const request = require('request');

request.get(url, (err, req, body) => {
  if (err) throw err;
  const charactersURL = JSON.parse(body).characters;

  for (const character of charactersURL) {
    request.get(character, (err, req, body) => {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});
