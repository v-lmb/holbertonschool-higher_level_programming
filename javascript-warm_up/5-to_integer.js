#!/usr/bin/node

const arg = process.argv[2];
const n = parseInt(arg);

if (!isNaN(n)) {
  console.log('My number: ' + n);
} else {
  console.log('Not a number');
}
