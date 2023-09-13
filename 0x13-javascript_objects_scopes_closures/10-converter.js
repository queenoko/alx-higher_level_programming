#!/usr/bin/node
/**
 * converts num from base 10 to another base
 */

exports.converter = function (base) {
  function myConverterBase (n) {
    return n.toString(base);
  }

  return myConverterBase;
};
