#!/usr/bin/node

/**
 * Logme function
 */

let logCounter = 0;

exports.logMe = function count (item) {
  console.log(`${logCounter}: ${item}`);
  logCounter += 1;
};
