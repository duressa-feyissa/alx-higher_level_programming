#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const tmp = [];
  for (let i = 2; i < args.length; i++) {
    tmp.push(parseInt(args[i]));
  }
  tmp.sort(function (a, b) { return b - a; });
  console.log(tmp[1]);
}
