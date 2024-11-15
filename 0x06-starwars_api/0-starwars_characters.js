#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const fetchMovie = url => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(new Error('Error:' + err));
      } else if (res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(new Error(`Failed to fetch with status code: ${res.statusCode}`));
      }
    });
  });
};

const getCharacters = async () => {
  try {
    const movie = await fetchMovie(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const characterUrls = movie.characters;

    for (const url of characterUrls) {
      const character = await fetchMovie(url);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
};

getCharacters();
