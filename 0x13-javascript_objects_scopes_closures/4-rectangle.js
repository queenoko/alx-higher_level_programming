#!/usr/bin/node
/**
 * This Checks the module of parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let z = 0; z < this.height; z++) {
      let myVar = '';
      let k = 0;
      while (k < this.width) {
        myVar += 'X';
        k++;
      }

      console.log(myVar);
    }
  }

  rotate () {
    let tempRot = 0;
    tempRot = this.width;
    this.width = this.height;
    this.height = tempRot;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
