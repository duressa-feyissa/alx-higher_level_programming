#!/usr/bin/node
const args = process.argv;
if (args[2] !== undefined) {
  if ( /^\d+\.\d+$|^\d+$/.test(args[2])) {
    x = parseInt(args[2])
    console.log('My number:',x);
  }  else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
