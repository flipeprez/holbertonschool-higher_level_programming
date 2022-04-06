#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let i = '';
      for (let k = i; k < this.width; k++) {
        i = i + c;
      }
      console.log(i);
    }
  }
}
module.exports = Square;
