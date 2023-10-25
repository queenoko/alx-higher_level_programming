#!/usr/bin/node

const request = require('request');

const movId = process.argv[2];
const url = `https://swapi.dev/api/films/${movId}/`;
let characters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  characters = data.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterDataJ = JSON.parse(body);
    console.log(characterDataJ.name);
    getCharacters(index + 1);
  });
};
