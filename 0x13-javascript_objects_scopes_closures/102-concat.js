#!/usr/bin/node
const files = require('files');
const file1 = files.readFileSync(process.argv[2], 'utf8');
const file2 = files.readFileSync(process.argv[3], 'utf8');
files.writeFileSync(process.argv[4], file1 + file2);
