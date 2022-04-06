#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let i = '';
      for (let k = 0; k < this.width; k++) {
        i = i + 'X';
      }
      console.log(i);
    }
  }
}
module.exports = Rectangle;
