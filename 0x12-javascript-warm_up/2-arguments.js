#!/usr/bin/node
const argcCount = process.argv.length;

if (argcCount > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
