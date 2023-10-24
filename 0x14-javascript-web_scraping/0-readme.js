#!/usr/bin/node
# script that reads and print content of file
const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
