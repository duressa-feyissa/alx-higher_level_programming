#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  const len = parseInt(args[2]);
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
}
