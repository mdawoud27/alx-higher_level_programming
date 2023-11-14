#!/usr/bin/node
const baseSquare = require('./5-square.js');

class Square extends baseSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    const char = (c === undefined || c.length > 1) ? 'X' : c;

    for (let i = 0; i < this.size; i++) {
      let squRow = '';
      for (let j = 0; j < this.size; j++) {
        squRow += char;
      }
      console.log(squRow);
    }
  }
}

module.exports = Square;
