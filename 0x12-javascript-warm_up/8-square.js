#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let z = 0; z < x; z++) {
    let k = 0;
    let myVarSize = '';

    while (k < x) {
      myVarSize = myVarSize + 'X';
      k++;
    }
    console.log(myVarSize);
  }
}
