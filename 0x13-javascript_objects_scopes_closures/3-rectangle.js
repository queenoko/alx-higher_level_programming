#!/usr/bin/node
/**
 * This Checks the module parameters provided
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
}
module.exports = Rectangle;
