#!/usr/bin/node
const argc = process.argv.length;
if (argc === 1) {
  console.log('No argument');
} else if (argc === 2) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
