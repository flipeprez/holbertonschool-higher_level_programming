#!/usr/bin/node
exports.converter = function (base) {
  return function (changeBase) {
    changeBase.toString(base);
  };
};
