#!/usr/bin/node
const list = process.argv[2];

if (isNaN(list)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < list; i++) {
    let show = '';
    for (let j = 0; j < list; j++) {
      show = show + 'X';
    }
    console.log(show);
  }
}
