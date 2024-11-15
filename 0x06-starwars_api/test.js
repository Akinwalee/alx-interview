#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.log(`Failed with status code: ${res.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  // Fetch chracter names
  const getCharacter = (url, callback) => {
    request(url, (err, res, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }

      if (res.statusCode === 200) {
        const character = JSON.parse(body);
        console.log(character.name);
        callback();
      }
    });
  };

  const printNames = (urls) => {
    let complete = 0;

    urls.forEach((url) => {
      getCharacter(url, () => {
        complete++;

        if (complete === urls.length) {
          process.exit(0);
        }
      });
    });
  };

  printNames(characterUrls);
});
