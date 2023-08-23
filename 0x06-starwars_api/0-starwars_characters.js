#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

function fetchAndPrint (characterUrls, index) {
  if (characterUrls.length === index) {
    return;
  }

  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      fetchAndPrint(characterUrls, index + 1);
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characterUrls = film.characters;

    // Fetch character names using their individual URLs and create an array of promises
    fetchAndPrint(characterUrls, 0);
  }
});
