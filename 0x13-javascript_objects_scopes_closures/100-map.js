#!/usr/bin/node
/*
Creating a new list and multiplying values by their idx
*/
const listed = require('./100-data');
const newList = listed.list.map((e, idx) => e * idx);
console.log(listed.list);
console.log(newList);
