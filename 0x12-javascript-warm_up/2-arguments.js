#!/usr/bin/node
const argcCount = process.argv.length;

if (argcCount > 0) {
  console.log('Argument found');
} else if (argcCount > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
