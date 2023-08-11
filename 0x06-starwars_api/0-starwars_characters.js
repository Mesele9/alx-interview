#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const character = film.characters;

    // Fetch character names using their individual URLs and create an array of promises
    fetchAndPrint(character);
  }
});

function fetchAndPrint (characterUrls) {
  let count = 0;

  characterUrls.forEach(characterUrl => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error(characterError);
      } else {
        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);

        count++;
        if (count === characterUrls.length) {
          process.exit(0);
        }
      }
    });
  });
}
