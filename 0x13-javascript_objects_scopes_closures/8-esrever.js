#!/usr/bin/node

exports.esrever = function (list) {
  const listed = [];
  list.forEach(elem => {
    listed.unshift(elem);
  });
  return listed;
};
