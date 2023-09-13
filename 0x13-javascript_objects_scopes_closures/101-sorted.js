#!/usr/bin/node
const dict = require('./101-data.js').dict;

const mynewDict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (mynewDict[dict[occurences]] === undefined) {
    mynewDict[dict[occurences]] = [occurences];
  } else {
    mynewDict[dict[occurences]].push(occurences);
  }
});
console.log(mynewDict);
