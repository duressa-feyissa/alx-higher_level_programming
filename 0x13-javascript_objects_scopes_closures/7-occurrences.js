#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (const i of list) {
    if (i === searchElement) {
      x += 1;
    }
  }
  return x;
};
