#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  for (let i = list.length - 1; i > -1; i--) {
    newList.push(list[i]);
  }
  return newList;
};

