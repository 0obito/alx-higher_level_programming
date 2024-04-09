#!/usr/bin/node

const arg = parseInt(process.argv[2]);
let line = '';

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let h = 0; h < arg; h++) {
    line += 'X';
  }
  for (let i = 0; i < arg; i++) {
    console.log(line);
  }
}
