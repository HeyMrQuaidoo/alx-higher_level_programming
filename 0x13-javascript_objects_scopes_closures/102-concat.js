#!/usr/bin/node
/*
concatenates the contents of two files
*/
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');

let content = '';
if (fileA && fileB && fileC) {
  if ((fs.existsSync(fileA) && fs.statSync(fileA).isFile) &&
    (fs.existsSync(fileB) && fs.statSync(fileB).isFile)) {
    content += fs.readFileSync(fileA, (error) => {
      if (error) throw error;
    });

    content += fs.readFileSync(fileB, (error) => {
      if (error) throw error;
    });

    fs.writeFile(fileC, content, (error) => {
      if (error) throw error;
    });
  }
}
