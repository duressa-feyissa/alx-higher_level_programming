#!/usr/bin/node
const occurence = require('./101-data').dict;
const newDict = {};
for (const key in occurence) {
  if (newDict[occurence[key]] === undefined) {
    newDict[occurence[key]] = [];
  }
  newDict[occurence[key]].push(key);
}
console.log(newDict);
