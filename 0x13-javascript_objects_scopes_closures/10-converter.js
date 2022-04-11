#!/usr/bin/node
exports.converter = function (base) {
  return function (changeBase) {
    return changeBase.toString(base);
  };
};
