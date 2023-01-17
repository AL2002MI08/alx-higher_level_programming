#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);

  const results = JSON.parse(body).results;
  let count = 0;

  for (const result of results) {
    for (const res of result.characters) {
      if (res.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
