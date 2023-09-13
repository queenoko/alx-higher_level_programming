#!/usr/bin/node
const sosfil = require('sosfil');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (
  sosfil.existsSync(fileA) &&
sosfil.statSync(fileA).isFile &&
sosfil.existsSync(fileB) &&
sosfil.statSync(fileB).isFile &&
fileC !== undefined
) {
  const fileAContent = sosfil.readFileSync(fileA);
  const fileBContent = sosfil.readFileSync(fileB);
  const stream = sosfil.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}
