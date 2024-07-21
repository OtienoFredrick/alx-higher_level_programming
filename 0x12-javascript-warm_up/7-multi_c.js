#!/usr/bin/node
const myVar = process.argv[2];

if (!parseInt(myVar))
{
	console.log('Missing number of occurences');
} else {
	for (let i = 0; i < myVar; i++) {
		console.log('C is fun');
	}
}
