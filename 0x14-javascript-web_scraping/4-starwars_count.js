#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const castId = '18';
let countChar = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(castId)) {
          countChar += 1;
        }
      });
    });
    console.log(countChar);
  }
});
