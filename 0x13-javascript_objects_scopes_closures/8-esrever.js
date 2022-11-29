#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = list.map((_, index, arr) => arr[arr.length - 1 - index]);
  return reversedList;
};
