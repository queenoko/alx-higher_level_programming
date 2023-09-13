#!/usr/bin/node
/**
 * Returns reverse version
 */

exports.esrever = function (list) {
  const myreversedList = [];
  for (let z = list.length - 1; z >= 0; z--) {
    myreversedList.push(list[z]);
  }

  return (myreversedList);
};
