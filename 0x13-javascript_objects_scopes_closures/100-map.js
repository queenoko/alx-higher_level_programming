#!/usr/bin/node
const list = require('./100-data.js').list;

const mynewList = list.map((val, idx) => val * idx);
console.log(list);
console.log(mynewList);
