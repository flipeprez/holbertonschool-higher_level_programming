#!/usr/bin/node
function fact (num) {
  if (isNaN(parseInt(num))) {
    return (1);
  }
  if (num === 1) {
    return (1);
  }
  return (num * fact(num - 1));
}
console.log(fact(parseInt(process.argv[2])));
