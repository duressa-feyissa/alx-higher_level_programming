#!/usr/bin/node
const args = process.argv;

if (isNaN(args[2])) {
  console.log(1);
} else {
  const x = parseInt(args[2]);
  let pro = 1;
  for (let i = 1; i <= x; i++) {
    pro *= i;
  }
  console.log(pro);
}
