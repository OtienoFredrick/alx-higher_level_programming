#!/usr/bin/node
exports.callMemoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
