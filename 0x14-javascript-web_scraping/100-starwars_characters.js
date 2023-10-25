#!/usr/bin/node

const request = require('request');

const movId = process.argv[2];
const url = `https://swapi.dev/api/films/${movId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const dataList = JSON.parse(body);
  const characters = dataList.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterDataJ = JSON.parse(body);
      console.log(characterDataJ.name);
    });
  }
});
