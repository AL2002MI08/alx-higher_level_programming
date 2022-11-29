#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (!c) this.print();
    else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
    /*
    else {
      for (let i = 0; i < this.height; i++) {
        const temp = [];
        for (let j = 0; j < this.width; j++) temp.push('C');
        console.log(`${temp.join('')}`);
      }
    }
    */
  }
}

module.exports = Square;
