#!/usr/bin/node

const dict = require('./101-data').dict;

const userId = {};
for (const id in dict) {
  const occurrences = dict[id];

  if (!userId[occurrences]) {
    userId[occurrences] = [];
  }

  userId[occurrences].push(id);
}
console.log(userId);
