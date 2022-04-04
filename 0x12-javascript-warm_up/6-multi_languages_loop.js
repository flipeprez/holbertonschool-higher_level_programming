#!/usr/bin/node
const list = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (const property in list) {
  console.log(`${list[property]}`);
}
