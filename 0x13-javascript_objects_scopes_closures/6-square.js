#!/usr/bin/node
const baseSquare = require('./5-square.js');

class Square extends baseSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      let squRow = '';
      for (let j = 0; j < this.size; j++) {
        squRow += c;
      }
      console.log(squRow);
    }
  }
}

module.exports = Square;
