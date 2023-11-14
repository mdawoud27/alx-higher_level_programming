#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1, k = 0; i >= 0; i--, k++) {
    reversedList[k] = list[i];
    // Or `reversedList.push(list[i]);`
  }
  return reversedList;
};
