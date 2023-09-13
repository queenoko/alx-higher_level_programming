#!/usr/bin/node
/**
 * function returns nmber of occurences
 */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let z = 0; z < list.length; z++) {
    count = (list[z] === searchElement ? count + 1 : count);
  }

  return count;
};
