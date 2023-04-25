#!/usr/bin/node
const fs = require('fs');
const args = process.argv[2];
fs.readFile(args, 'utf8', function (err, data) {
  console.log(err);
  console.log(data);
});
