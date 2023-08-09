#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');

const asyncRequest = promisify(request);

async function getCharacter (filmUrl) {
  try {
    const filmResponse = await asyncRequest(filmUrl);
    const filmData = JSON.parse(filmResponse.body);
    const characters = filmData.characters;

    for (const url of characters) {
      const characterResponse = await asyncRequest(url);
      const charObj = JSON.parse(characterResponse.body);
      console.log(charObj.name);
    }
  } catch (error) {
    console.log(`An error occurred: ${error.message}`);
  }
}

try {
  const filmId = Number(process.argv[2]);
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
  getCharacter(filmUrl);
} catch (error) {
  console.log(error.message);
}
