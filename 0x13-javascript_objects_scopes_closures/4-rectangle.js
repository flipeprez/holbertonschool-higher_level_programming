#!/usr/bin/node
class Rectangle {
  constructor(w , h){
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  }
  print() {
  for (let i = 0; i < this.height; i++) {
    let i = '';
    for (let k = 0; k < this.width; k++) {
      i = i + 'X';
    }
    console.log(i);
  }
  }
  rotate() {
  let tmp = this.width;
  this.width = this.height;
  this.height = tmp;
  }
  double() {
  this.width = (this.width * 2);
  this.height = (this.height * 2);
  }  
 }
module.exports = Rectangle;

