#!/usr/bin/node
/**
 * Class Rectangle with two arguments h and w
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0)
      this.width = w;
      this.height = h;
  }
}
module.exports = Rectangle;
