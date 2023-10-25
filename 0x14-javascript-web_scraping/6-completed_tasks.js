#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const comptTask = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!comptTask[todo.userId]) {
        comptTask[todo.userId] = 1;
      } else {
        comptTask[todo.userId] += 1;
      }
    }
  });
  console.log(comptTask);
});
