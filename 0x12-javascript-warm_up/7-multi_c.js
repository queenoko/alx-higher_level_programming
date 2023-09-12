#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let z = 0; z < x; z++) {
    console.log('C is fun');
  }
}
