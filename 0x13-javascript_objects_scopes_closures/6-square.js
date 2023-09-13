#!/usr/bin/node
/**
 * The Square class that inherits from previous square class module
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let z = 0; z < this.height; z++) {
      let myVar = '';
      let k = 0;
      while (k < this.width) {
        myVar += myChar;
        k++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
