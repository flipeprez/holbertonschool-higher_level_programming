#!/usr/bin/node
let list = process.argv[2];

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < list; i++) {
  console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
