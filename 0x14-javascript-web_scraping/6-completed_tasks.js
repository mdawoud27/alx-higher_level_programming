#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const completedTask = {};

request.get(url, (err, req, body) => {
  if (err) throw err;
  const bodyObject = JSON.parse(body);
  //   console.log(bodyObject);

  for (const obj of bodyObject) {
    if (obj.completed) {
      completedTask[obj.userId]
        ? completedTask[obj.userId]++
        : (completedTask[obj.userId] = 1);
    }
  }
  console.log(completedTask);
});
