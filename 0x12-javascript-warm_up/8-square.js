#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
	console.log('Missiing size');
} else {
  for (let i = 0; i < x; i++) {
     let y = 0;
     let myVar = '';
     
     while (y < x) {
	     myVar = myVar + 'X';
	     y++;
     }
	  console.log(myVar);
  }
}
