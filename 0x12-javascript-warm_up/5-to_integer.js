#!/usr/bin/node

if (process.argv[2]) {
  if (!isNaN(parseInt(process.argv[2]))) {
    console.log('My number: ', parseInt(process.argv[2]));
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
