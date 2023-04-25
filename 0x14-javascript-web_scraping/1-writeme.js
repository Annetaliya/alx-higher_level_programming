#!/usr/bin/node
const fs = require('fs');
function writeToFile (error) {
  if (error) {
    console.log(error);
  }
}
fs.writeFile(process.argv[2], process.argv[3], writeToFile);
