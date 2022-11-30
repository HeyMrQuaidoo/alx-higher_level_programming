#!/usr/bin/node
/*
creating a new list from an old one
new one contain the key value, occurrences: index
*/
const oldDict = require('./101-data').dict;
const newDict = {};
for (const key in oldDict) {
  if (newDict[oldDict[key]]) {
    newDict[oldDict[key]].push(key);
  } else {
    newDict[oldDict[key]] = [key];
  }
}
console.log(newDict);
