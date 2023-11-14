#!/usr/bin/node

const list = require('./100-data').list;
let i = 0;
const _list = list.map((x) => x * i++);
console.log(list);
console.log(_list);
