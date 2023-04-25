#!/usr/bin/node
const request = require('request');
const args = process.argv[2];
request.get(args).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
