#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileStore = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileStore, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
