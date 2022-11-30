#!/usr/bin/node
const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    let cp = c;
    if (!c) {
      cp = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(cp.repeat(this.width));
    }
  }
}

module.exports = Square;
