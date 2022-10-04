#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  const len = parseInt(args[2]);
  for (let i = 0; i < len; i++) {
    let x = '';
    for (let j = 0; j < len; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
